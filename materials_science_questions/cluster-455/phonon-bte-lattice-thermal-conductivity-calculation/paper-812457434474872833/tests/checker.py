import os
import json
import csv

# === author imports / helpers ===
import statistics


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
    ctx = {"spec": os.environ.get("SPEC_PATH", "/tests/grading_spec.json")}
    return ctx


# === block: score_0 (check id='model_perf') ===
def score_0(artifact, step, ctx):
    data = artifact
    fields = step["params"]["fields"]
    ok = True
    for fname, limits in fields.items():
        val = data.get(fname)
        if val is None:
            ok = False; break
        if limits.get("min") is not None and val < limits["min"]:
            ok = False; break
        if limits.get("max") is not None and val > limits["max"]:
            ok = False; break
    if ok:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='predictions_white_mean') ===
def score_1(artifact, step, ctx):
    rows = artifact
    value_col = step["params"]["value_column"]
    comp_list = step["params"]["compositions"]
    target = step["params"]["target"]
    tol = step["params"]["tolerance_symmetric"]
    values = []
    for row in rows:
        if row.get("composition") in comp_list:
            val = row.get(value_col)
            if val is not None:
                values.append(float(val))
    if len(values) == 0:
        return 0.0
    mean_val = statistics.mean(values)
    if abs(mean_val - target) <= tol:
        return 1.0
    else:
        score = max(0.0, 1.0 - (abs(mean_val - target) - tol) / (2*tol))
        return score


# === block: score_2 (check id='predictions_grey_mean') ===
def score_2(artifact, step, ctx):
    rows = artifact
    value_col = step["params"]["value_column"]
    comp_list = step["params"]["compositions"]
    target = step["params"]["target"]
    tol = step["params"]["tolerance_symmetric"]
    values = []
    for row in rows:
        if row.get("composition") in comp_list:
            val = row.get(value_col)
            if val is not None:
                values.append(float(val))
    if len(values) == 0:
        return 0.0
    mean_val = statistics.mean(values)
    if abs(mean_val - target) <= tol:
        return 1.0
    else:
        score = max(0.0, 1.0 - (abs(mean_val - target) - tol) / (2*tol))
        return score


# === block: score_3 (check id='predictions_ba_lower_than_sr') ===
def score_3(artifact, step, ctx):
    rows = artifact
    phase_col = step["params"]["phase_field_column"]
    val_col = step["params"]["value_column"]
    group1 = step["params"]["group1"]
    group2 = step["params"]["group2"]
    vals1 = [float(row[val_col]) for row in rows if row.get(phase_col) == group1]
    vals2 = [float(row[val_col]) for row in rows if row.get(phase_col) == group2]
    if not vals1 or not vals2:
        return 0.0
    m1 = statistics.mean(vals1)
    m2 = statistics.mean(vals2)
    if m1 < m2:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'model_perf': score_0,
    'predictions_white_mean': score_1,
    'predictions_grey_mean': score_2,
    'predictions_ba_lower_than_sr': score_3,
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
