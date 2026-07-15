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


# === block: score_0 (check id='check_csv_sanity') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    final_rows = {}
    for row in artifact:
        thick = int(row.get('thickness_nm', 0))
        mcs = int(row.get('MCS', 0))
        if thick not in final_rows or mcs > int(final_rows[thick]['MCS']):
            final_rows[thick] = row
    min_mcs = 1000
    sum_min, sum_max = 0.9, 1.1
    for thick in (100, 500, 800):
        if thick not in final_rows:
            return 0.0
        row = final_rows[thick]
        if int(row.get('MCS', 0)) < min_mcs:
            return 0.0
        total = (float(row.get('fraction_111', 0)) + float(row.get('fraction_001', 0)) +
                 float(row.get('fraction_511', 0)) + float(row.get('fraction_101', 0)))
        if total < sum_min or total > sum_max:
            return 0.0
    return 1.0


# === block: score_1 (check id='check_final_json') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    thick_req = {
        '100nm': {'check_fields': [('fraction_111', 0.4)], 'sum_range': (0.9, 1.1)},
        '500nm': {'check_fields': [('fraction_511', 0.1), ('fraction_111', 0.1)], 'sum_range': (0.9, 1.1)},
        '800nm': {'check_fields': [('fraction_001', 0.4)], 'sum_range': (0.9, 1.1)}
    }
    passed = 0
    total = 0
    for key, req in thick_req.items():
        if key not in artifact:
            return 0.0
        data = artifact[key]
        frac_sum = sum(float(data.get(f, 0)) for f in ['fraction_111', 'fraction_001', 'fraction_511', 'fraction_101'])
        low, high = req['sum_range']
        total += 1
        if low <= frac_sum <= high:
            passed += 1
        for field, min_val in req['check_fields']:
            total += 1
            if float(data.get(field, 0)) > min_val:
                passed += 1
    return passed / total if total > 0 else 0.0


_SCORERS = {
    'check_csv_sanity': score_0,
    'check_final_json': score_1,
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
