import os
import json
import csv


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


# === block: score_0 (check id='results_check') ===
def score_0(artifact, step, ctx):
    criteria = step.get('criteria', {})
    try:
        d = artifact
        # imaginary frequency
        imf = bool(d.get('H2SiOO_planar_imaginary_freq'))
        # spin populations
        si_spin = float(d['H2SiOO_CASSCF_spins']['Si'])
        ot_spin = float(d['H2SiOO_CASSCF_spins']['O_terminal'])
        c_spin = float(d['H2COO_CASSCF_spins']['C'])
        oc_spin = float(d['H2COO_CASSCF_spins']['O_terminal'])
        # orbital overlaps
        Si_gvb = d['H2SiOO_GVB_overlaps']
        C_gvb  = d['H2COO_GVB_overlaps']
        S_pi_Si = float(Si_gvb['S_pi'])
        S_Si_Oa = float(Si_gvb['S_Si_Oa'])
        S_Oa_Ob_Si = float(Si_gvb['S_Oa_Ob'])
        S_pi_C = float(C_gvb['S_pi'])
        S_C_Oa = float(C_gvb['S_C_Oa'])
        S_Oa_Ob_C = float(C_gvb['S_Oa_Ob'])
        # energies
        E_h2sioo = float(d['H2SiOO_MP2_energy_hartree'])
        E_ts = float(d['H2SiOO_TS_energy_hartree'])
        E_sila = float(d['H2SiOO_siladioxirane_energy_hartree'])
        # compute derived
        barrier_ha = E_ts - E_h2sioo
        exo_ha = E_sila - E_h2sioo
        # thresholds
        barrier_max = criteria.get('barrier_max_ha', 0.05)
        exo_max = criteria.get('exothermicity_max_ha', -0.04)
        sigma_min = criteria.get('overlap_sigma_min', 0.65)
        pi_Si_max = criteria.get('overlap_pi_Si_max', 0.4)
        pi_C_min = criteria.get('overlap_pi_C_min', 0.3)
        spin_Si_min = criteria.get('spin_Si_min', 0.5)
        spin_O_Si_min = criteria.get('spin_O_Si_min', 0.5)
        spin_C_max = criteria.get('spin_C_max', 0.5)
        spin_O_C_max = criteria.get('spin_O_C_max', 0.5)
        # sub-scores (5 groups, each 0.2)
        s1 = 1.0 if imf == criteria.get('imaginary_freq_expected', True) else 0.0
        s2 = 1.0 if (abs(barrier_ha) < barrier_max and exo_ha < exo_max) else 0.0
        s3 = 1.0 if (S_Si_Oa > sigma_min and S_Oa_Ob_Si > sigma_min and S_C_Oa > sigma_min and S_Oa_Ob_C > sigma_min) else 0.0
        s4 = 1.0 if (S_pi_Si < pi_Si_max and S_pi_C > pi_C_min and S_pi_Si < S_pi_C) else 0.0
        s5 = 1.0 if (si_spin > spin_Si_min and ot_spin > spin_O_Si_min and c_spin < spin_C_max and oc_spin < spin_O_C_max and si_spin > c_spin and ot_spin > oc_spin) else 0.0
        total = (s1 + s2 + s3 + s4 + s5) / 5.0
        return total
    except Exception:
        return 0.0


_SCORERS = {
    'results_check': score_0,
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
