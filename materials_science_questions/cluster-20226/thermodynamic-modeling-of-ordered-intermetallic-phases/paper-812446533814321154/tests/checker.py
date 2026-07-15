import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.interpolate import UnivariateSpline


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
    gold = {}
    for step in spec.get('steps', []):
        if step['id'] == 'step_tc':
            gold['tc'] = {float(k): v for k, v in step.get('gold_tc', {}).items()}
            gold['tc_theta_list'] = step.get('theta_list', [])
            gold['tc_tol'] = float(step.get('tolerance_abs_K', 5))
        elif step['id'] == 'step_intensity':
            gold['intensity'] = {float(k): v for k, v in step.get('gold_I', {}).items()}
            gold['T_target'] = step.get('T_target', 150)
            gold['tol_rel'] = float(step.get('tolerance_rel', 0.001))
            gold['tol_abs'] = float(step.get('tolerance_abs_floor', 0.0001))
    return gold


# === block: score_0 (check id='step_tc') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold_tc = ctx.get('tc', {})
    gold_tol = ctx.get('tc_tol', 5)
    theta_set = ctx.get('tc_theta_list', [])

    # group by theta and sort by T
    groups = {}
    for row in artifact:
        try:
            th = float(row['theta'])
            t = float(row['T'])
            i = float(row['I'])
        except (ValueError, KeyError):
            continue
        groups.setdefault(th, []).append((t, i))

    # pre-compute max intensity per theta (used for flat-curve detection)
    max_I = {}
    for th, points in groups.items():
        if points:
            max_I[th] = max(i for _, i in points)
        else:
            max_I[th] = 0.0

    FLAT_I_THRESH = 1e-3  # threshold below which the curve is considered flat (no ordering)

    computed_tc = {}
    for th, points in groups.items():
        if len(points) < 5:
            continue
        points.sort()
        ts, is_ = zip(*points)
        ts = np.array(ts)
        is_ = np.array(is_)
        # Fit cubic spline
        try:
            spl = UnivariateSpline(ts, is_, s=0, k=3)
            d2 = spl.derivative(2)
            # find zero crossing of second derivative within [min(T)+5, max(T)-5]
            t_min = float(np.min(ts) + 5)
            t_max = float(np.max(ts) - 5)
            if t_max <= t_min:
                continue
            t_range = np.linspace(t_min, t_max, 200)
            d2_vals = d2(t_range)
            crossings = []
            for j in range(len(d2_vals)-1):
                if d2_vals[j] == 0:
                    crossings.append(t_range[j])
                elif d2_vals[j] * d2_vals[j+1] < 0:
                    # linear interpolation for zero
                    t0 = t_range[j]
                    t1 = t_range[j+1]
                    f0 = d2_vals[j]
                    f1 = d2_vals[j+1]
                    tc = t0 - f0 * (t1 - t0) / (f1 - f0)
                    crossings.append(tc)
            if not crossings:
                continue
            # choose the crossing closest to the mid of the range
            mid = (t_min + t_max) / 2
            best_tc = min(crossings, key=lambda x: abs(x - mid))
            computed_tc[th] = best_tc
        except Exception:
            continue

    scores = []
    for th in theta_set:
        if th not in gold_tc:
            continue
        if th not in computed_tc:
            # No Tc extracted; if gold expects Tc=0 and the intensity curve is essentially flat, accept as correct
            if gold_tc[th] == 0.0 and max_I.get(th, 0.0) < FLAT_I_THRESH:
                scores.append(1.0)
            else:
                scores.append(0.0)
            continue
        diff = abs(computed_tc[th] - gold_tc[th])
        if diff <= gold_tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_intensity') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold_I = ctx.get('intensity', {})
    T_target = ctx.get('T_target', 150)
    tol_rel = ctx.get('tol_rel', 0.001)
    tol_abs = ctx.get('tol_abs', 0.0001)

    # extract rows where T equals T_target (closest)
    candidate = None
    min_diff = None
    for row in artifact:
        try:
            t = float(row['T'])
            th = float(row['theta'])
            i = float(row['I'])
        except (ValueError, KeyError):
            continue
        diff = abs(t - T_target)
        if min_diff is None or diff < min_diff:
            min_diff = diff
            candidate = {}
        if diff != min_diff:
            continue
        candidate[th] = i

    if not candidate:
        return 0.0

    scores = []
    for th_str, gold_val in gold_I.items():
        th = float(th_str)
        if th not in candidate:
            scores.append(0.0)
            continue
        val = candidate[th]
        thresh = max(tol_abs, tol_rel * abs(gold_val))
        if abs(val - gold_val) <= thresh:
            scores.append(1.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step_tc': score_0,
    'step_intensity': score_1,
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
