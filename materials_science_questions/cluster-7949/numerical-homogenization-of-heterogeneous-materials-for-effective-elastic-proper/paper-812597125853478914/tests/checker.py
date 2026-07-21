import os
import json
import csv

# === author imports / helpers ===
import csv, sys, math, os


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


# === block: score_0 (check id='step03_copper_stress') ===
def score_0(artifact, step, ctx):
    rows = artifact
    ref = step['reference_data']
    ref_pts = ref['points']
    rel_tol = ref['rel_tol']
    max_rel = ref['max_score_rel']
    strains = []
    stresses = []
    for r in rows:
        s = float(r['strain'])
        e = float(r['equivalent_stress'])
        strains.append(abs(s))
        stresses.append(e)
    if len(strains) < 10:
        return 0.0
    user_x = sorted(strains)
    user_y = [stresses[strains.index(x)] for x in user_x]
    def interp(x, xs, ys):
        if x <= xs[0]:
            return ys[0]
        if x >= xs[-1]:
            return ys[-1]
        for i in range(len(xs)-1):
            if xs[i] <= x <= xs[i+1]:
                t = (x - xs[i]) / (xs[i+1] - xs[i])
                return ys[i] + t * (ys[i+1] - ys[i])
    errs = []
    for xp, yp in ref_pts:
        y_hat = interp(xp, user_x, user_y)
        if abs(yp) > 1e-12:
            errs.append(abs(y_hat - yp) / abs(yp))
        else:
            errs.append(abs(y_hat))
    if not errs:
        return 0.0
    max_err = max(errs)
    if max_err <= rel_tol:
        return 1.0
    if max_err >= max_rel:
        return 0.0
    return (max_rel - max_err) / (max_rel - rel_tol)


# === block: score_1 (check id='step04_copper_strain_ratio') ===
def score_1(artifact, step, ctx):
    rows = artifact
    ref = step['reference_data']
    ref_pts = ref['points']
    abs_tol = ref['abs_tol']
    max_abs = ref['max_score_abs']
    strains = []
    ratios = []
    for r in rows:
        s = float(r['strain'])
        v = float(r['transverse_strain_ratio'])
        strains.append(abs(s))
        ratios.append(v)
    user_x = sorted(strains)
    user_y = [ratios[strains.index(x)] for x in user_x]
    def interp(x, xs, ys):
        if x <= xs[0]: return ys[0]
        if x >= xs[-1]: return ys[-1]
        for i in range(len(xs)-1):
            if xs[i] <= x <= xs[i+1]:
                t = (x - xs[i]) / (xs[i+1] - xs[i])
                return ys[i] + t * (ys[i+1] - ys[i])
    errs = []
    for xp, yp in ref_pts:
        y_hat = interp(xp, user_x, user_y)
        errs.append(abs(y_hat - yp))
    max_err = max(errs)
    if max_err <= abs_tol:
        return 1.0
    if max_err >= max_abs:
        return 0.0
    return (max_abs - max_err) / (max_abs - abs_tol)


# === block: score_2 (check id='step05_ss_lattice_avg') ===
def score_2(artifact, step, ctx):
    ref_rows = step['reference_data']['ref_rows']
    rel_tol = step['reference_data']['rel_tol']
    max_rel = step['reference_data']['max_score_rel']
    errs = []
    for ref_row in ref_rows:
        family = ref_row['family']
        direction = ref_row['direction']
        target = ref_row['lattice_strain']
        found = None
        for row in artifact:
            if row['family'] == family and row['direction'] == direction:
                found = float(row['lattice_strain'])
                break
        if found is None:
            errs.append(1.0)
        else:
            if abs(target) > 1e-12:
                errs.append(abs(found - target) / abs(target))
            else:
                errs.append(abs(found))
    max_err = max(errs)
    if max_err <= rel_tol:
        return 1.0
    if max_err >= max_rel:
        return 0.0
    return (max_rel - max_err) / (max_rel - rel_tol)


# === block: score_3 (check id='step06_ss_lattice_std') ===
def score_3(artifact, step, ctx):
    ref_rows = step['reference_data']['ref_rows']
    rel_tol = step['reference_data']['rel_tol']
    max_rel = step['reference_data']['max_score_rel']
    errs = []
    for ref_row in ref_rows:
        family = ref_row['family']
        direction = ref_row['direction']
        target = ref_row['std_lattice_strain']
        found = None
        for row in artifact:
            if row['family'] == family and row['direction'] == direction:
                found = float(row['std_lattice_strain'])
                break
        if found is None:
            errs.append(1.0)
        else:
            if abs(target) > 1e-12:
                errs.append(abs(found - target) / abs(target))
            else:
                errs.append(abs(found))
    max_err = max(errs)
    if max_err <= rel_tol:
        return 1.0
    if max_err >= max_rel:
        return 0.0
    return (max_rel - max_err) / (max_rel - rel_tol)


_SCORERS = {
    'step03_copper_stress': score_0,
    'step04_copper_strain_ratio': score_1,
    'step05_ss_lattice_avg': score_2,
    'step06_ss_lattice_std': score_3,
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
