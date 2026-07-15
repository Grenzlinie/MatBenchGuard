import os
import json
import csv

# === author imports / helpers ===
import csv, math, os

def linreg_slope(xs, ys):
    n = len(xs)
    if n == 0:
        return 0.0
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_xx = sum(x*x for x in xs)
    sum_xy = sum(x*y for x,y in zip(xs,ys))
    denom = n*sum_xx - sum_x*sum_x
    if abs(denom) < 1e-12:
        return 0.0
    return (n*sum_xy - sum_x*sum_y) / denom


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


# === block: score_0 (check id='trend_check') ===
def score_0(artifact, step, ctx):
    def score_trend(artifact, step, ctx):
        intra_params = ["l1","l2","l3","l4","w1","w2","w3","w4"]
        required = intra_params + ["theta1","theta2","stress"]
        if not artifact or not all(col in artifact[0] for col in required):
            return 0.0
        stresses = []
        theta1_vals = []
        theta2_vals = []
        intra_vals = {p: [] for p in intra_params}
        for row in artifact:
            try:
                s = row["stress"]
                t1 = row["theta1"]
                t2 = row["theta2"]
                if s is None or t1 is None or t2 is None:
                    continue
                s = float(s)
                t1 = float(t1)
                t2 = float(t2)
                vals = {p: row[p] for p in intra_params}
                if any(v is None for v in vals.values()):
                    continue
                vals = {p: float(v) for p, v in vals.items()}
                stresses.append(s)
                theta1_vals.append(t1)
                theta2_vals.append(t2)
                for p in intra_params:
                    intra_vals[p].append(vals[p])
            except (ValueError, TypeError, KeyError):
                continue
        min_rows = step.get("min_rows", 5)
        if len(stresses) < min_rows:
            return 0.0
        slope_theta1 = linreg_slope(stresses, theta1_vals)
        slope_theta2 = linreg_slope(stresses, theta2_vals)
        if slope_theta1 <= 0 or slope_theta2 <= 0:
            return 0.0
        intra_slopes = [abs(linreg_slope(stresses, intra_vals[p])) for p in intra_params]
        max_intra = max(intra_slopes) if intra_slopes else 1e-12
        if max_intra < 1e-12:
            return 1.0
        ratio1 = slope_theta1 / max_intra
        ratio2 = slope_theta2 / max_intra
        min_ratio = min(ratio1, ratio2)
        threshold = step.get("threshold_ratio", 5.0)
        score = max(0.0, min(1.0, (min_ratio - 1) / (threshold - 1)))
        return score


_SCORERS = {
    'trend_check': score_0,
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
