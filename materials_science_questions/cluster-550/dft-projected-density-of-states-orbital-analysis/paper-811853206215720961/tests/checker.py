import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ImportError:
    np = None
try:
    from scipy import stats
except ImportError:
    import math
    from collections import namedtuple
    LinregressResult = namedtuple('LinregressResult', ['slope', 'intercept', 'rvalue', 'pvalue', 'stderr'])
    def linregress(x, y):
        n = len(x)
        if n != len(y) or n < 2:
            raise ValueError
        sumx = sum(x)
        sumy = sum(y)
        sumx2 = sum(xi*xi for xi in x)
        sumxy = sum(xi*yi for xi, yi in zip(x, y))
        denom = n*sumx2 - sumx*sumx
        if denom == 0:
            slope = 0.0
            intercept = sumy / n
        else:
            slope = (n*sumxy - sumx*sumy) / denom
            intercept = (sumy - slope*sumx) / n
        meanx = sumx / n
        meany = sumy / n
        ssx = sum((xi-meanx)**2 for xi in x)
        ssy = sum((yi-meany)**2 for yi in y)
        ssxy = sum((xi-meanx)*(yi-meany) for xi, yi in zip(x, y))
        if ssx == 0 or ssy == 0:
            rvalue = 0.0
        else:
            rvalue = ssxy / math.sqrt(ssx * ssy)
        return LinregressResult(slope, intercept, rvalue, float('nan'), float('nan'))
    class FakeStats:
        linregress = staticmethod(linregress)
    stats = FakeStats()


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


# === block: score_0 (check id='s1') ===
def score_0(artifact, step, ctx):
    try:
        val = float(artifact.strip().split('\n')[0].strip())
    except:
        return 0.0
    gold = step.get('gold', 6.7)
    tol = step.get('tolerance', 0.3)
    if abs(val - gold) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='s4') ===
def score_1(artifact, step, ctx):
    min_rows = step.get('min_rows', 4)
    if len(artifact) < min_rows:
        return 0.0
    try:
        U_vals = [float(row['U']) for row in artifact]
        vb_vals = [float(row['delta_VB']) for row in artifact]
        cb_vals = [float(row['delta_CB']) for row in artifact]
    except (ValueError, KeyError):
        return 0.0

    pos_w = step.get('positivity_weight', 0.2)
    all_positive = all(v > 0 for v in vb_vals) and all(c > 0 for c in cb_vals)
    score_pos = pos_w if all_positive else 0.0

    slope_vb_w = step.get('slope_vb_weight', 0.2)
    r2_vb_w = step.get('r2_vb_weight', 0.2)
    if len(U_vals) >= 3:
        reg_vb = stats.linregress(U_vals, vb_vals)
        slope_vb = reg_vb.slope
        r2_vb = reg_vb.rvalue**2
    else:
        slope_vb = 0.0
        r2_vb = 0.0
    score_slope_vb = slope_vb_w if slope_vb < 0 else 0.0
    score_r2_vb = r2_vb_w if r2_vb > 0.7 else 0.0

    slope_cb_w = step.get('slope_cb_weight', 0.2)
    r2_cb_w = step.get('r2_cb_weight', 0.2)
    if len(U_vals) >= 3:
        reg_cb = stats.linregress(U_vals, cb_vals)
        slope_cb = reg_cb.slope
        r2_cb = reg_cb.rvalue**2
    else:
        slope_cb = 0.0
        r2_cb = 0.0
    score_slope_cb = slope_cb_w if slope_cb > 0 else 0.0
    score_r2_cb = r2_cb_w if r2_cb > 0.7 else 0.0

    total = score_pos + score_slope_vb + score_r2_vb + score_slope_cb + score_r2_cb
    return min(total, 1.0)


_SCORERS = {
    's1': score_0,
    's4': score_1,
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
