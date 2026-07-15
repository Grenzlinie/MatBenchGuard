import os
import json
import csv

# === author imports / helpers ===
import math

def compute_slope(rows):
    freqs = []
    powers = []
    for r in rows:
        try:
            freqs.append(float(r['frequency']))
            powers.append(float(r['power']))
        except (KeyError, ValueError):
            continue
    if len(freqs) < 5:
        return None
    # sort by frequency
    paired = sorted(zip(freqs, powers), key=lambda x: x[0])
    freqs = [p[0] for p in paired]
    powers = [p[1] for p in paired]
    # filter positive
    filtered = [(f, p) for f, p in zip(freqs, powers) if f > 0 and p > 0]
    if len(filtered) < 5:
        return None
    freqs = [f for f, p in filtered]
    powers = [p for f, p in filtered]
    # compute 1st percentile of frequencies
    sorted_f = sorted(freqs)
    p1_idx = max(1, int(0.01 * len(sorted_f)))
    threshold = sorted_f[p1_idx - 1] if p1_idx <= len(sorted_f) else sorted_f[0]
    indices = [i for i, f in enumerate(freqs) if f > threshold]
    if len(indices) < 5:
        return None
    log_f = [math.log10(freqs[i]) for i in indices]
    log_p = [math.log10(powers[i]) for i in indices]
    n = len(log_f)
    sum_x = sum(log_f)
    sum_y = sum(log_p)
    sum_xy = sum(x * y for x, y in zip(log_f, log_p))
    sum_x2 = sum(x * x for x in log_f)
    denom = n * sum_x2 - sum_x * sum_x
    if denom == 0:
        return None
    return (n * sum_xy - sum_x * sum_y) / denom


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


# === block: score_0 (check id='xe55_slope') ===
def score_0(artifact, step, ctx):
    slope = compute_slope(artifact)
    if slope is None:
        return 0.0
    low, high = step.get("target_range", [-1.2, -0.8])
    return 1.0 if low <= slope <= high else 0.0


# === block: score_1 (check id='ar_slope') ===
def score_1(artifact, step, ctx):
    slope = compute_slope(artifact)
    if slope is None:
        return 0.0
    low, high = step.get("target_range", [-0.2, 0.2])
    return 1.0 if low <= slope <= high else 0.0


# === block: score_2 (check id='xe_arxe_slope') ===
def score_2(artifact, step, ctx):
    slope = compute_slope(artifact)
    if slope is None:
        return 0.0
    low, high = step.get("target_range", [-1.2, -0.8])
    return 1.0 if low <= slope <= high else 0.0


_SCORERS = {
    'xe55_slope': score_0,
    'ar_slope': score_1,
    'xe_arxe_slope': score_2,
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
