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


# === block: score_0 (check id='step-01-bandgap') ===
def score_0(artifact, step, ctx):
    artifact = artifact if isinstance(artifact, dict) else {}
    req_direct = step.get('required_direct', True)
    req_func = step.get('required_functional', 'HSE06')
    target = step.get('target_band_gap', None)
    tol = step.get('tolerance_band_gap', 0.1)
    direct_ok = isinstance(artifact.get('direct'), bool) and artifact.get('direct') == req_direct
    func_ok = artifact.get('functional') and artifact.get('functional').upper() == req_func.upper()
    gap_ok = False
    if target is not None:
        gap = artifact.get('band_gap')
        if isinstance(gap, (int, float)) and abs(gap - target) <= tol:
            gap_ok = True
    score = 0.0
    if direct_ok:
        score += 0.1
    if func_ok:
        score += 0.1
    if gap_ok:
        score += 0.8
    return score


# === block: score_1 (check id='step-02-effmass') ===
def score_1(artifact, step, ctx):
    artifact = artifact if isinstance(artifact, dict) else {}
    req_func = step.get('required_functional', 'LDA')
    target = step.get('target_effmass', None)
    tol = step.get('tolerance_effmass', 0.05)
    func_ok = artifact.get('functional') and artifact.get('functional').upper() == req_func.upper()
    mass_ok = False
    if target is not None:
        mass = artifact.get('effective_mass')
        if isinstance(mass, (int, float)) and abs(mass - target) <= tol:
            mass_ok = True
    score = 0.0
    if func_ok:
        score += 0.1
    if mass_ok:
        score += 0.9
    return score


# === block: score_2 (check id='step-03-bandedges') ===
def score_2(artifact, step, ctx):
    artifact = artifact if isinstance(artifact, dict) else {}
    w_cbm = 0.375
    w_vbm = 0.375
    w_her = 0.0625
    w_oer = 0.0625
    w_pH = 0.125
    score = 0.0
    cbm = artifact.get('CBM_vs_vacuum')
    vbm = artifact.get('VBM_vs_vacuum')
    her = artifact.get('HER_potential')
    oer = artifact.get('OER_potential')
    pH = artifact.get('pH')
    target_cbm = step.get('target_CBM', None)
    target_vbm = step.get('target_VBM', None)
    tol_cv = step.get('tolerance_CBM_VBM', 0.2)
    target_her = step.get('target_HER', None)
    target_oer = step.get('target_OER', None)
    tol_ho = step.get('tolerance_HER_OER', 0.1)
    req_pH = step.get('required_pH', 0)
    if isinstance(cbm, (int, float)) and isinstance(target_cbm, (int, float)) and abs(cbm - target_cbm) <= tol_cv:
        score += w_cbm
    if isinstance(vbm, (int, float)) and isinstance(target_vbm, (int, float)) and abs(vbm - target_vbm) <= tol_cv:
        score += w_vbm
    if isinstance(her, (int, float)) and isinstance(target_her, (int, float)) and abs(her - target_her) <= tol_ho:
        score += w_her
    if isinstance(oer, (int, float)) and isinstance(target_oer, (int, float)) and abs(oer - target_oer) <= tol_ho:
        score += w_oer
    if pH == req_pH:
        score += w_pH
    return min(score, 1.0)


# === block: score_3 (check id='step-04-polarization') ===
def score_3(artifact, step, ctx):
    artifact = artifact if isinstance(artifact, list) else []
    targets = step.get('targets', [])
    if not targets:
        return 0.0
    num = len(targets)
    score = 0.0
    for tgt in targets:
        struct_name = tgt.get('structure', '').lower()
        entry = None
        for item in artifact:
            if isinstance(item, dict) and item.get('structure', '').lower() == struct_name:
                entry = item
                break
        if entry is None:
            continue
        pol = entry.get('polarization')
        dir_val = entry.get('direction', '').lower()
        target_pol = tgt.get('polarization', None)
        tol = tgt.get('tolerance', 5e-13)
        target_dir = tgt.get('direction', '').lower()
        pol_ok = False
        if isinstance(pol, (int, float)) and isinstance(target_pol, (int, float)) and abs(pol - target_pol) <= tol:
            pol_ok = True
        dir_ok = (dir_val == target_dir)
        struct_score = 0.0
        if pol_ok:
            struct_score += 0.8
        if dir_ok:
            struct_score += 0.2
        score += struct_score / num
    return score


_SCORERS = {
    'step-01-bandgap': score_0,
    'step-02-effmass': score_1,
    'step-03-bandedges': score_2,
    'step-04-polarization': score_3,
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
