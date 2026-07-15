import os
import json
import csv

# === author imports / helpers ===
def csv_float_compare(rows, expected_list, tolerance, value_keys):
    """
    rows: list of dict from csv.DictReader
    expected_list: list of dict with 'compound' and target values.
    tolerance: float
    value_keys: list of fields to compare (excluding 'compound')
    Returns score in [0,1]: fraction of expected compounds where all values are within tolerance.
    """
    if not rows or not expected_list:
        return 0.0
    row_dict = {}
    for r in rows:
        compound = (r.get('compound') or '').strip()
        if compound:
            row_dict[compound] = r
    total = len(expected_list)
    if total == 0:
        return 0.0
    passed = 0
    for exp in expected_list:
        compound = exp['compound']
        if compound not in row_dict:
            continue
        row = row_dict[compound]
        ok = True
        for key in value_keys:
            try:
                actual = float(row.get(key, float('nan')))
                target = float(exp[key])
            except (ValueError, TypeError):
                ok = False
                break
            if abs(actual - target) > tolerance + 1e-12:
                ok = False
                break
        if ok:
            passed += 1
    return passed / total


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


# === block: score_0 (check id='check_U') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts from csv.DictReader
    # step is the dict from grading_spec.steps (contains expected, tolerance)
    expected = step.get('expected', [])
    tolerance = float(step.get('tolerance', 0.05))
    value_keys = ['U_value']
    return csv_float_compare(artifact, expected, tolerance, value_keys)


# === block: score_1 (check id='check_lattice') ===
def score_1(artifact, step, ctx):
    expected = step.get('expected', [])
    tolerance = float(step.get('tolerance', 0.02))
    value_keys = ['a', 'c', 'volume']
    return csv_float_compare(artifact, expected, tolerance, value_keys)


# === block: score_2 (check id='check_magnetic') ===
def score_2(artifact, step, ctx):
    expected = step.get('expected', [])
    tolerance = float(step.get('tolerance', 0.1))
    value_keys = ['total_moment', 'RE1_moment', 'RE2_moment', 'Ge_moment']
    return csv_float_compare(artifact, expected, tolerance, value_keys)


_SCORERS = {
    'check_U': score_0,
    'check_lattice': score_1,
    'check_magnetic': score_2,
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
