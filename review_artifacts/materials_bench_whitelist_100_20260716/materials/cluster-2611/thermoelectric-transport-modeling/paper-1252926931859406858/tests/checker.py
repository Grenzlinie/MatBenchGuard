import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='sawtooth_structural') ===
def score_0(artifact, step, ctx):
    rows = artifact
    params = step.get('params', {})
    sigma_thresh = params.get('sigma_max_at_flatband', 0.01)
    S_thresh = params.get('S_min_abs_at_flatband', 1.0)
    zT_range = params.get('zT_peak_Vg_range', [-0.2, -0.1])
    gamma_vals = set(float(row['Gamma']) for row in rows)
    if len(gamma_vals) < 2:
        return 0.0

    def find_closest(gamma_target):
        best_row = None
        best_dist = float('inf')
        for row in rows:
            if float(row['Gamma']) != gamma_target:
                continue
            dist = abs(float(row['Vg']))
            if dist < best_dist:
                best_dist = dist
                best_row = row
        return best_row

    def find_zt_peak(gamma_target):
        max_zT = -float('inf')
        max_vg = None
        for row in rows:
            if float(row['Gamma']) != gamma_target:
                continue
            z = float(row['zT'])
            if z > max_zT:
                max_zT = z
                max_vg = float(row['Vg'])
        return max_vg

    checks_passed = 0
    total_checks = 0
    for gamma in [5.0, 50.0]:
        row0 = find_closest(gamma)
        if row0 is None:
            continue
        sigma = float(row0['sigma'])
        S = float(row0['S'])
        total_checks += 1
        if sigma <= sigma_thresh:
            checks_passed += 1
        total_checks += 1
        if abs(S) >= S_thresh:
            checks_passed += 1
        vg_peak = find_zt_peak(gamma)
        total_checks += 1
        if vg_peak is not None and zT_range[0] <= vg_peak <= zT_range[1]:
            checks_passed += 1
    if total_checks == 0:
        return 0.0
    return checks_passed / total_checks


# === block: score_1 (check id='diamond_structural') ===
def score_1(artifact, step, ctx):
    rows = artifact
    params = step.get('params', {})
    sigma_min = params.get('sigma_min_at_flatband', 0.1)
    zT_range = params.get('zT_peak_Vg_range', [-0.2, -0.1])
    gamma_vals = set(float(row['Gamma']) for row in rows)
    if len(gamma_vals) < 2:
        return 0.0

    def find_closest(gamma_target):
        best_row = None
        best_dist = float('inf')
        for row in rows:
            if float(row['Gamma']) != gamma_target:
                continue
            dist = abs(float(row['Vg']))
            if dist < best_dist:
                best_dist = dist
                best_row = row
        return best_row

    def find_zt_peak(gamma_target):
        max_zT = -float('inf')
        max_vg = None
        for row in rows:
            if float(row['Gamma']) != gamma_target:
                continue
            z = float(row['zT'])
            if z > max_zT:
                max_zT = z
                max_vg = float(row['Vg'])
        return max_vg

    checks_passed = 0
    total_checks = 0
    for gamma in [5.0, 50.0]:
        row0 = find_closest(gamma)
        if row0 is None:
            continue
        sigma = float(row0['sigma'])
        total_checks += 1
        if sigma >= sigma_min:
            checks_passed += 1
        vg_peak = find_zt_peak(gamma)
        total_checks += 1
        if vg_peak is not None and zT_range[0] <= vg_peak <= zT_range[1]:
            checks_passed += 1
    if total_checks == 0:
        return 0.0
    return checks_passed / total_checks


_SCORERS = {
    'sawtooth_structural': score_0,
    'diamond_structural': score_1,
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
