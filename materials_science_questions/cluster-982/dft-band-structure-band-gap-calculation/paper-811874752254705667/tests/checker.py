import os
import json
import csv

# === author imports / helpers ===
import json, os, math


import os as _ff_os
import json as _ff_json


def _ff_validate_output_contract():
    """Return a list of shape violations against grading_spec['output_contract']."""
    spec_path = "/tests/grading_spec.json"
    if not _ff_os.path.exists(spec_path):
        return []
    with open(spec_path) as _f:
        _spec = _ff_json.load(_f)
    contract = _spec.get("output_contract", {}) or {}
    outputs = contract.get("outputs", []) or []
    out_dir = "/app/outputs"
    violations = []
    for out in outputs:
        base = str(out.get("file", "")).split("/")[-1]
        if not base:
            continue
        path = _ff_os.path.join(out_dir, base)
        if not _ff_os.path.isfile(path):
            violations.append("missing output_contract file: " + base)
            continue
        fmt = out.get("format", "")
        schema = out.get("schema", {}) or {}
        if fmt == "json":
            try:
                data = _ff_json.load(open(path))
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": invalid JSON (" + str(exc) + ")")
                continue
            required = schema.get("required", {})
            fields = required.keys() if isinstance(required, dict) else (required or [])
            if isinstance(data, dict):
                for field in fields:
                    if field not in data:
                        violations.append(base + ": missing JSON field '" + str(field) + "'")
        elif fmt in ("csv", "tsv"):
            import csv as _ff_csv
            delim = "\t" if fmt == "tsv" else ","
            try:
                with open(path, newline="") as _f:
                    cols = set((_ff_csv.reader(_f, delimiter=delim).__next__() or []))
            except StopIteration:
                cols = set()
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": cannot read table (" + str(exc) + ")")
                continue
            required_cols = schema.get("required_columns", []) or []
            for col in required_cols:
                name = col.get("name") if isinstance(col, dict) else col
                if name and name not in cols:
                    violations.append(base + ": missing table column '" + str(name) + "'")
    return violations


def _ff_contract_gate():
    """Zero the reward and exit if the submission violates the output_contract shape."""
    violations = _ff_validate_output_contract()
    if not violations:
        return
    _ff_os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as _f:
        _f.write("0.0")
    with open("/logs/verifier/breakdown.json", "w") as _f:
        _ff_json.dump({"output_contract_violations": violations}, _f, indent=2)
    raise SystemExit(0)


def load_artifact(path):
    if not path or not os.path.exists(path):
        return None
    if path.endswith(".json"):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:  # noqa: BLE001
            return None
    if path.endswith(".csv") or path.endswith(".tsv"):
        delim = "\t" if path.endswith(".tsv") else ","
        with open(path, newline="") as f:
            return list(csv.DictReader(f, delimiter=delim))
    with open(path) as f:
        return f.read()


def prepare(outputs_dir, spec):
    return {}


# === block: score_0 (check id='s_band_gap') ===
def score_0(artifact, step, ctx):
    if not all(k in artifact for k in ('band_gap_eV','is_indirect','vbm_kpoint','cbm_kpoint')):
        return 0.0
    gap = float(artifact['band_gap_eV'])
    target = step.get('hidden_gap_target', 3.114)
    tol = step.get('hidden_gap_tolerance', 0.2)
    diff = abs(gap - target)
    if diff <= tol:
        gap_score = 1.0
    elif diff <= 2*tol:
        gap_score = 0.5
    else:
        gap_score = 0.0
    is_indirect = bool(artifact['is_indirect'])
    indirect_score = 1.0 if is_indirect else 0.0
    vbm_k = str(artifact['vbm_kpoint']).strip()
    vbm_score = 1.0 if vbm_k == step.get('hidden_vbm_target','N') else 0.0
    cbm_k = str(artifact['cbm_kpoint']).strip()
    cbm_score = 1.0 if cbm_k == step.get('hidden_cbm_target','Gamma') else 0.0
    return 0.6*gap_score + 0.2*indirect_score + 0.1*vbm_score + 0.1*cbm_score


# === block: score_1 (check id='s_pdos') ===
def score_1(artifact, step, ctx):
    if not all(k in artifact for k in ('valence_band_dominant_orbitals','conduction_band_dominant_orbitals','bi_o_hybridization_energy_window')):
        return 0.0
    vb_list = [s.strip() for s in artifact['valence_band_dominant_orbitals']]
    cb_list = [s.strip() for s in artifact['conduction_band_dominant_orbitals']]
    target_vb = set(step.get('hidden_valence_orbitals', []))
    target_cb = set(step.get('hidden_conduction_orbitals', []))
    vb_score = 1.0 if target_vb.issubset(set(vb_list)) else 0.0
    cb_score = 1.0 if target_cb.issubset(set(cb_list)) else 0.0
    hybrid_window = str(artifact['bi_o_hybridization_energy_window']).strip().lower()
    target_hybrid = str(step.get('hidden_hybrid_window','0-4 eV')).strip().lower()
    hybrid_score = 1.0 if hybrid_window == target_hybrid else 0.0
    return 0.4*vb_score + 0.4*cb_score + 0.2*hybrid_score


# === block: score_2 (check id='s_dielectric') ===
def score_2(artifact, step, ctx):
    required = ['energies_eV','eps_xx','eps_yy','eps_zz','isotropic_below_4eV','anisotropic_above_4eV']
    if not all(k in artifact for k in required):
        return 0.0
    energies = artifact['energies_eV']
    eps_xx = artifact['eps_xx']
    eps_yy = artifact['eps_yy']
    eps_zz = artifact['eps_zz']
    if not (isinstance(energies, list) and isinstance(eps_xx, list) and isinstance(eps_yy, list) and isinstance(eps_zz, list)):
        return 0.0
    n = len(energies)
    if n < 50 or len(eps_xx) != n or len(eps_yy) != n or len(eps_zz) != n:
        return 0.0
    # basic validity score
    data_score = 0.2
    # recompute isotropy below 4 eV
    iso_max_rel_diff = 0.0
    for i in range(n):
        e = float(energies[i])
        if e > 4.0:
            break
        eps = [float(eps_xx[i]), float(eps_yy[i]), float(eps_zz[i])]
        avg = (eps[0]+eps[1]+eps[2])/3.0
        if avg == 0.0:
            continue
        max_diff = max(eps) - min(eps)
        rel_diff = max_diff / abs(avg)
        if rel_diff > iso_max_rel_diff:
            iso_max_rel_diff = rel_diff
    computed_iso = iso_max_rel_diff < 0.1
    agent_iso = bool(artifact['isotropic_below_4eV'])
    iso_score = 1.0 if computed_iso == agent_iso else 0.0
    # recompute anisotropy above 4 eV
    ani_max_rel_diff = 0.0
    found_above = False
    for i in range(n):
        e = float(energies[i])
        if e <= 4.0:
            continue
        found_above = True
        eps = [float(eps_xx[i]), float(eps_yy[i]), float(eps_zz[i])]
        avg = (eps[0]+eps[1]+eps[2])/3.0
        if avg == 0.0:
            continue
        max_diff = max(eps) - min(eps)
        rel_diff = max_diff / abs(avg)
        if rel_diff > ani_max_rel_diff:
            ani_max_rel_diff = rel_diff
    computed_ani = ani_max_rel_diff > 0.1 if found_above else True
    agent_ani = bool(artifact['anisotropic_above_4eV'])
    ani_score = 1.0 if computed_ani == agent_ani else 0.0
    return 0.2 + 0.4*iso_score + 0.4*ani_score


_SCORERS = {
    's_band_gap': score_0,
    's_pdos': score_1,
    's_dielectric': score_2,
}


def _step_id(step, index):
    sid = str(step.get("id", "")).strip()
    if sid:
        return sid
    output = str(step.get("output_file", "")).split("/")[-1].rsplit(".", 1)[0]
    kind = str(step.get("kind") or step.get("metric") or "score").strip()
    base = "_".join(part for part in (output, kind) if part).strip("_")
    return base or ("check_" + str(index))


def main():
    _ff_contract_gate()
    with open("/tests/grading_spec.json") as f:
        spec = json.load(f)
    outputs_dir = "/app/outputs"
    ctx = prepare(outputs_dir, spec)
    steps = spec.get("steps", spec.get("checks", [])) or []
    breakdown = {}
    total = 0.0
    for index, step in enumerate(steps):
        sid = _step_id(step, index)
        output_file = str(step.get("output_file", "")).split("/")[-1]
        weight = float(step.get("weight", 0.0))
        artifact = load_artifact(os.path.join(outputs_dir, output_file)) if output_file else None
        fn = _SCORERS.get(sid)
        if fn is None:
            score = 0.0
        else:
            try:
                score = float(fn(artifact, step, ctx))
            except Exception as exc:  # noqa: BLE001
                score = 0.0
                breakdown.setdefault("_errors", {})[sid] = repr(exc)
        score = max(0.0, min(1.0, score))
        breakdown[sid or output_file] = {"score": score, "weight": weight}
        total += score * weight
    os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as f:
        f.write(str(round(total, 6)))
    with open("/logs/verifier/breakdown.json", "w") as f:
        json.dump(breakdown, f, indent=2)


if __name__ == "__main__":
    main()
