import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='voltage_curve_check') ===
def score_0(artifact, step, ctx):
    targets = step
    avg_target = targets["avg_voltage_target"]
    avg_tol = targets["avg_voltage_tol"]
    step33_target = targets["step33_target"]
    step50_target = targets["step50_target"]
    step_tol = targets["step_tol"]

    lines = artifact.strip().splitlines()
    if len(lines) < 2:
        return 0.0
    header = lines[0].strip().split()
    x_idx = 0 if header[0].lower().startswith('x') else None
    v_idx = 1 if (len(header) > 1 and header[1].lower().startswith('v')) else None
    if x_idx is None or v_idx is None:
        x_idx, v_idx = 0, 1

    data = []
    for line in lines[1:]:
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        try:
            x = float(parts[x_idx])
            v = float(parts[v_idx])
            data.append((x, v))
        except Exception:
            continue
    if len(data) < 2:
        return 0.0

    data.sort(key=lambda p: p[0])
    xs = [d[0] for d in data]
    vs = [d[1] for d in data]

    def interp(x, xs, vs):
        if x <= xs[0]:
            return vs[0]
        if x >= xs[-1]:
            return vs[-1]
        for i in range(len(xs) - 1):
            if xs[i] <= x <= xs[i+1]:
                t = (x - xs[i]) / (xs[i+1] - xs[i])
                return vs[i] + t * (vs[i+1] - vs[i])
        return vs[-1]

    def trapz(xs, vs):
        area = 0.0
        for i in range(len(xs) - 1):
            area += (xs[i+1] - xs[i]) * (vs[i] + vs[i+1]) * 0.5
        return area

    avg_v = trapz(xs, vs) / (xs[-1] - xs[0])
    v32 = interp(0.32, xs, vs)
    v33 = interp(0.33, xs, vs)
    v49 = interp(0.49, xs, vs)
    v50 = interp(0.50, xs, vs)
    step33 = v32 - v33
    step50 = v49 - v50

    score_avg = 1.0 if abs(avg_v - avg_target) <= avg_tol else 0.0
    score_33 = 1.0 if abs(step33 - step33_target) <= step_tol else 0.0
    score_50 = 1.0 if abs(step50 - step50_target) <= step_tol else 0.0

    check_score = (0.3 * score_avg + 0.15 * score_33 + 0.15 * score_50) / 0.6
    return float(check_score)


# === block: score_1 (check id='migration_barriers_check') ===
def score_1(artifact, step, ctx):
    targets = step["barrier_targets"]
    tol = step["barrier_tol"]

    lines = artifact.strip().splitlines()
    cases = {}
    for line in lines[1:]:
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        case_name = parts[0].strip()
        try:
            barrier = float(parts[1])
            cases[case_name] = barrier
        except Exception:
            continue

    n_correct = 0
    for case_name, ref in targets.items():
        if case_name in cases and abs(cases[case_name] - ref) <= tol:
            n_correct += 1
    return n_correct / len(targets)


_SCORERS = {
    'voltage_curve_check': score_0,
    'migration_barriers_check': score_1,
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
