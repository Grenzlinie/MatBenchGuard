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


# === block: score_0 (check id='step_01_tc') ===
def score_0(artifact, step, ctx):
    target = step['target']
    tol = step.get('tolerance', 0.01)
    if not isinstance(artifact, dict) or 'Tc' not in artifact:
        return 0.0
    val = artifact['Tc']
    if not isinstance(val, (int, float)):
        return 0.0
    err = abs(val - target)
    if err <= tol:
        return 1.0
    max_err = 0.5
    excess = max(0.0, err - tol)
    return max(0.0, 1.0 - excess / max_err)


# === block: score_1 (check id='step_01_n1') ===
def score_1(artifact, step, ctx):
    arr = artifact.get('n1_vs_temperature')
    if not isinstance(arr, list) or len(arr) < 4:
        return 0.0
    temps = []
    n1s = []
    for item in arr:
        if not isinstance(item, dict):
            continue
        t = item.get('temperature')
        n = item.get('n1')
        if t is not None and n is not None:
            try:
                temps.append(float(t))
                n1s.append(float(n))
            except (ValueError, TypeError):
                pass
    if len(temps) < 4:
        return 0.0
    low_thresh = 2.5
    high_thresh = 4.0
    low_points = [(t, n) for t, n in zip(temps, n1s) if t <= low_thresh]
    high_points = [(t, n) for t, n in zip(temps, n1s) if t >= high_thresh]
    cond_low = any(n >= 0.9 for t, n in low_points)
    cond_high = any(n <= 0.2 for t, n in high_points)
    near_tc = [n for t, n in zip(temps, n1s) if 3.3 <= t <= 3.6]
    cond_transition = any(0.3 <= n <= 0.9 for n in near_tc)
    score = 0.0
    if cond_low:
        score += 0.33
    if cond_high:
        score += 0.33
    if cond_transition:
        score += 0.33
    return min(1.0, score)


# === block: score_2 (check id='step_02') ===
def score_2(artifact, step, ctx):
    thresh = step.get('threshold', 0.8)
    if not isinstance(artifact, dict) or 'n1_at_T0' not in artifact:
        return 0.0
    val = artifact['n1_at_T0']
    if not isinstance(val, (int, float)):
        return 0.0
    return 1.0 if float(val) >= thresh else 0.0


_SCORERS = {
    'step_01_tc': score_0,
    'step_01_n1': score_1,
    'step_02': score_2,
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
