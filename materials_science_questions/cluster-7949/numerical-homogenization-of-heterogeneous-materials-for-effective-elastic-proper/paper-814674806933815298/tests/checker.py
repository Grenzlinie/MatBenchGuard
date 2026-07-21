import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, math


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


# === block: score_0 (check id='fixed_ratios_check_exp1') ===
def score_0(artifact, step, ctx):
    target = step.get('target')
    tolerance = step.get('tolerance', 1.0)
    field = step.get('field')
    value = artifact.get(field)
    if value is None:
        return 0.0
    error = abs(value - target)
    score = max(0.0, 1.0 - error / tolerance)
    return score


# === block: score_1 (check id='fixed_ratios_check_exp2') ===
def score_1(artifact, step, ctx):
    target = step.get('target')
    tolerance = step.get('tolerance', 1.0)
    field = step.get('field')
    value = artifact.get(field)
    if value is None:
        return 0.0
    error = abs(value - target)
    score = max(0.0, 1.0 - error / tolerance)
    return score


# === block: score_2 (check id='residual_curves_check') ===
def score_2(artifact, step, ctx):
    rows = sorted(artifact, key=lambda r: float(r['temperature']))
    temps = [float(r['temperature']) for r in rows]
    exp1 = [float(r['exp1_ratio']) for r in rows]
    exp2 = [float(r['exp2_ratio']) for r in rows]

    def find_idx(temps, target, tol=0.1):
        for i, t in enumerate(temps):
            if abs(t - target) <= tol:
                return i
        return None

    idx0 = find_idx(temps, 0.0)
    idx50 = find_idx(temps, 50.0)

    sub_weights = [0.25, 0.25, 0.25, 0.25]
    sub_scores = [0.0, 0.0, 0.0, 0.0]

    # 1. initial 100%
    if idx0 is not None:
        if 98.0 <= exp1[idx0] <= 102.0 and 98.0 <= exp2[idx0] <= 102.0:
            sub_scores[0] = 1.0

    # 2. monotonic non-increasing
    def is_monotonic_non_increasing(vals):
        for i in range(1, len(vals)):
            if vals[i] > vals[i-1] + 1e-9:
                return False
        return True

    if is_monotonic_non_increasing(exp1) and is_monotonic_non_increasing(exp2):
        sub_scores[1] = 1.0

    # 3. crossover: exp1 > exp2 for T < 40
    crossover_pass = True
    for t, v1, v2 in zip(temps, exp1, exp2):
        if t < 40.0 and v1 <= v2 + 1e-9:
            crossover_pass = False
            break
    if crossover_pass:
        sub_scores[2] = 1.0

    # 4. final recovery: both < 5% at T=50
    if idx50 is not None:
        if exp1[idx50] < 5.0 and exp2[idx50] < 5.0:
            sub_scores[3] = 1.0

    score = sum(s * w for s, w in zip(sub_scores, sub_weights)) / sum(sub_weights)
    return score


_SCORERS = {
    'fixed_ratios_check_exp1': score_0,
    'fixed_ratios_check_exp2': score_1,
    'residual_curves_check': score_2,
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
