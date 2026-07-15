import os
import json
import csv

# === author imports / helpers ===
import csv, math

def has_decreasing_segment(points, dT_min, dT_max, min_width):
    """points: list of (dT, J) sorted by dT, filtered to dT_min..dT_max.
    Returns True if there exists a contiguous segment where J effectively
    decreases (allowing small upward noise) and the total dT span >= min_width.
    """
    if len(points) < 2:
        return False
    n = len(points)
    i = 0
    while i < n-1:
        start = i
        while i < n-1 and points[i+1][1] < points[i][1] + 1e-9:
            i += 1
        end = i
        if end > start:
            span = points[end][0] - points[start][0]
            # require a genuine net drop (more than a tiny epsilon)
            if span >= min_width and points[end][1] < points[start][1] - 1e-9:
                return True
        i += 1
    return False

def is_monotonic_non_decreasing(points, eps=1e-6):
    for i in range(1, len(points)):
        if points[i][1] < points[i-1][1] - eps:
            return False
    return True


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
    step = None
    for s in spec.get('steps', []):
        if s.get('id') == 'ndtc_check':
            step = s
            break
    case_checks = step.get('case_checks', []) if step else []
    return {'case_checks': case_checks}


# === block: score_0 (check id='ndtc_check') ===
def score_0(artifact, step, ctx):
    checks = ctx.get('case_checks', [])
    if not checks or not isinstance(artifact, list) or not artifact:
        return 0.0

    # Build mapping case -> [(dT, J), ...]
    data = {}
    for row in artifact:
        label = row.get('case', '').strip()
        if not label:
            continue
        try:
            dT = float(row['delta_T'])
            J = float(row['J'])
        except (KeyError, ValueError):
            continue
        data.setdefault(label, []).append((dT, J))

    passed = 0
    total = len(checks)

    for check in checks:
        label = check['label']
        ndtc_expected = check.get('ndtc_expected', None)
        points = data.get(label, [])
        if len(points) < 2:
            continue  # insufficient data => fail for this case
        points.sort(key=lambda x: x[0])

        if ndtc_expected is True:
            dT_min = check.get('delta_T_min', -float('inf'))
            dT_max = check.get('delta_T_max', float('inf'))
            min_width = check.get('min_decrease_width', 0)
            # filter to range
            filtered = [(d, j) for d, j in points if d >= dT_min and d <= dT_max]
            if has_decreasing_segment(filtered, dT_min, dT_max, min_width):
                passed += 1
        elif ndtc_expected is False:
            if is_monotonic_non_decreasing(points, eps=1e-6):
                passed += 1
        else:
            # no expectation? skip (should not happen)
            passed += 1

    return passed / total if total > 0 else 0.0


_SCORERS = {
    'ndtc_check': score_0,
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
