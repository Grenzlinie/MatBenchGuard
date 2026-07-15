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
        gold_curve = []
        for step in spec.get('steps', []):
            if step.get('output_file') == 'single_asperity_mastercurve.csv':
                pts = step.get('gold_curve_points', [])
                gold_curve = [(p['X_over_dX'], p['k_local_over_K_cl']) for p in pts]
                break
        return {'gold_curve': sorted(gold_curve)}


# === block: score_0 (check id='step_01_mastercurve') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, list) or len(artifact) < 20:
            return 0.0
        xs = []
        ys = []
        for row in artifact:
            try:
                x = float(row['X_over_dX'])
                y = float(row['k_local_over_K_cl'])
            except (KeyError, ValueError):
                return 0.0
            xs.append(x)
            ys.append(y)
        # sort by X
        coords = sorted(zip(xs, ys))
        xs = [c[0] for c in coords]
        ys = [c[1] for c in coords]
        # monotonic decreasing
        mono = 1.0
        for i in range(1, len(ys)):
            if ys[i] > ys[i-1] + 1e-12:
                mono = 0.0
                break
        # interpolate at gold X and compute closeness
        tol = float(step.get('tolerance_relative', 0.1))
        gold_curve = ctx.get('gold_curve', [])
        if not gold_curve:
            return mono  # no gold, only structure
        point_scores = []
        def _interp(x_val, xs, ys):
            n = len(xs)
            if x_val <= xs[0]:
                return ys[0]
            if x_val >= xs[-1]:
                return ys[-1]
            # binary search segment
            lo, hi = 0, n-1
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if xs[mid] <= x_val:
                    lo = mid
                else:
                    hi = mid
            # linear interpolate
            t = (x_val - xs[lo]) / (xs[hi] - xs[lo])
            return ys[lo] + t * (ys[hi] - ys[lo])
        for gx, gy in gold_curve:
            interp_y = _interp(gx, xs, ys)
            rel_err = abs(interp_y - gy) / gy if gy != 0 else abs(interp_y - gy)
            if rel_err <= tol:
                ps = 1.0
            else:
                ps = max(0.0, 1.0 - (rel_err - tol) / (1.0 - tol))
            point_scores.append(ps)
        closeness = sum(point_scores) / len(point_scores) if point_scores else 0.0
        # combine: 10% monotonic, 90% closeness
        return 0.1 * mono + 0.9 * closeness


# === block: score_1 (check id='step_02_multiple') ===
def score_1(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        gold_ew = float(step.get('gold_equal_widths', 0.98))
        gold_ee = float(step.get('gold_equal_effectiveness', 0.97))
        tol = float(step.get('tolerance_abs', 0.05))
        def score_one(value, gold):
            try:
                val = float(value)
            except (ValueError, TypeError):
                return 0.0
            diff = abs(val - gold)
            if diff <= tol:
                return 1.0
            return max(0.0, 1.0 - (diff - tol) / (2 * tol))
        s1 = score_one(artifact.get('equal_widths'), gold_ew)
        s2 = score_one(artifact.get('equal_effectiveness'), gold_ee)
        return 0.5 * s1 + 0.5 * s2


_SCORERS = {
    'step_01_mastercurve': score_0,
    'step_02_multiple': score_1,
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
