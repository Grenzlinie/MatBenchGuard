import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='compute_effective_debye') ===
def score_0(artifact, step, ctx):
    artifact = artifact
    a_KBr = 6.600
    a_KI = 7.066
    M_KBr = 119.002
    M_KI = 166.0028
    N_A = 6.02214076e23
    tD_KBr = 172.0
    tD_KI = 132.0
    # expected phase compositions and volume fractions (for reference, not scored)
    xs = artifact.get('phase_compositions', [])
    vol_fracs = artifact.get('volume_fractions', [])
    if len(xs) != 3 or len(vol_fracs) != 3:
        return 0.0
    lats = artifact.get('phase_lattice_constants_A', [])
    dens = artifact.get('phase_densities_g_per_cc', [])
    thetas = artifact.get('phase_theta_D_K', [])
    rep_eff = artifact.get('theta_D_effective_K')
    if None in (lats, dens, thetas, rep_eff) or len(lats)!=3 or len(dens)!=3 or len(thetas)!=3:
        return 0.0
    # recompute lattice constants
    comp_lats = []
    comp_dens = []
    comp_thetas = []
    for x in xs:
        a = x*a_KBr + (1-x)*a_KI
        comp_lats.append(a)
        M = x*M_KBr + (1-x)*M_KI
        dens_val = (M * 4) / (N_A * (a**3) * 1e-24)
        comp_dens.append(dens_val)
        inv2 = x/(tD_KBr**2) + (1-x)/(tD_KI**2)
        theta = 1.0 / math.sqrt(inv2)
        comp_thetas.append(theta)
    # sub-scores
    score_lat = 1.0
    for r, c in zip(lats, comp_lats):
        if abs(r-c) > 1e-8:
            score_lat = 0.0
            break
    score_dens = 1.0
    for r, c in zip(dens, comp_dens):
        if abs(r-c) > 1e-4:
            score_dens = 0.0
            break
    score_theta = 1.0
    for r, c in zip(thetas, comp_thetas):
        if abs(r-c) > 0.5:
            score_theta = 0.0
            break
    # recompute effective theta
    rho_eff = sum(w * d for w, d in zip(vol_fracs, dens))
    sum_hc = sum(w * d / (t**3) for w, d, t in zip(vol_fracs, dens, thetas))
    if sum_hc > 0:
        comp_eff = (rho_eff / sum_hc) ** (1.0/3.0)
    else:
        comp_eff = 0.0
    score_int_cons = 1.0 if abs(rep_eff - comp_eff) < 0.5 else 0.0
    score_gold = 1.0 if abs(comp_eff - 150.0) <= 5.0 else 0.0
    # weights
    w_lat = 0.1
    w_dens = 0.1
    w_theta = 0.1
    w_int = 0.1
    w_gold = 0.6
    total = w_lat*score_lat + w_dens*score_dens + w_theta*score_theta + w_int*score_int_cons + w_gold*score_gold
    return total


_SCORERS = {
    'compute_effective_debye': score_0,
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
