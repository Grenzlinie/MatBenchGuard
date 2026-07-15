import os
import json
import csv

# === author imports / helpers ===
import csv, json, bisect, math


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


# === block: score_0 (check id='nucleation_kinetics_check') ===
def score_0(artifact, step, ctx):
    import csv, bisect, math

    # Read CSV artifact: list of dicts with 'time', 'arrangement', 'number_density'
    rows = artifact  # artifact is passed as list of dicts
    if not rows:
        return 0.0

    time_ref = step.get('params', {}).get('time_ref', 1e6)
    density_ref = step.get('params', {}).get('density_ref', 1e21)
    factor = step.get('params', {}).get('factor_random_regular', 10)
    speedup = step.get('params', {}).get('speedup_factor', 10000)

    # Group by arrangement
    from collections import defaultdict
    arr_data = defaultdict(list)
    for r in rows:
        try:
            t = float(r['time'])
            d = float(r['number_density'])
            arr = r['arrangement'].strip()
            arr_data[arr].append((t, d))
        except:
            pass

    # Helper: sort and get value at a given time by linear interpolation
    def get_value_at(series, t_target):
        if not series:
            return None
        series.sort()
        if t_target <= series[0][0]:
            return series[0][1]
        if t_target >= series[-1][0]:
            return series[-1][1]
        idx = bisect.bisect_left([p[0] for p in series], t_target)
        if idx == 0:
            return series[0][1]
        t_prev, d_prev = series[idx-1]
        t_next, d_next = series[idx]
        if t_next == t_prev:
            return d_prev
        frac = (t_target - t_prev) / (t_next - t_prev)
        return d_prev + frac * (d_next - d_prev)

    # Helper: first time where density >= threshold
    def get_reach_time(series, threshold):
        series.sort()
        for t, d in series:
            if d >= threshold:
                return t
        return None

    # Check monotonic non-decreasing
    def is_non_decreasing(series):
        series.sort()
        prev = -1.0
        for _, d in series:
            if d < prev - 1e-12:
                return False
            prev = d
        return True

    sub_scores = []
    weights = []

    for arr_name in ['random', 'regular', 'homogeneous']:
        if arr_name in arr_data:
            series = arr_data[arr_name]
            if is_non_decreasing(series):
                sub_scores.append(1.0)
            else:
                sub_scores.append(0.0)
            weights.append(0.03333 * 0)  # weight for monotonicity? We'll allocate a small weight
        else:
            sub_scores.append(0.0)
            weights.append(0.0)

    # Actually weight: we give monotonicity total weight 0.1, equally divided among existing arrangements. We'll compute dynamic.
    arr_present = [a for a in ['random','regular','homogeneous'] if a in arr_data]
    if not arr_present:
        return 0.0
    mono_weight_dynamic = 0.1 / max(1, len(arr_present))
    mono_score = 0.0
    for a in arr_present:
        mono_score += (1.0 if is_non_decreasing(arr_data[a]) else 0.0) * mono_weight_dynamic

    # Condition 1: random density at t=1e6 vs regular/homogeneous
    score_ratio = 0.0
    if 'random' in arr_data:
        d_random = get_value_at(arr_data['random'], time_ref)
        if d_random is not None and d_random > 0:
            max_other = 0.0
            for other in ['regular','homogeneous']:
                if other in arr_data:
                    d_other = get_value_at(arr_data[other], time_ref)
                    if d_other is not None:
                        max_other = max(max_other, d_other)
            if max_other > 0:
                ratio = d_random / max_other
                score_ratio = min(1.0, ratio / factor)  # linear scaling: full if ratio >= factor
            else:
                score_ratio = 1.0  # no other arrangement has density, so random clearly bigger
        else:
            score_ratio = 0.0
    else:
        score_ratio = 0.0

    # Condition 2: speed-up in reaching density_ref
    score_speedup = 0.0
    if 'random' in arr_data:
        t_random = get_reach_time(arr_data['random'], density_ref)
        if t_random is not None:
            t_regular = get_reach_time(arr_data.get('regular', []), density_ref)
            if t_regular is None:
                # regular never reaches, so random is infinitely faster => full credit
                score_speedup = 1.0
            elif t_regular <= 0:
                score_speedup = 0.0  # can't evaluate
            else:
                actual_speedup = t_regular / t_random
                score_speedup = min(1.0, actual_speedup / speedup)
        else:
            score_speedup = 0.0
    else:
        score_speedup = 0.0

    total_weight = 0.0
    total_score = 0.0

    # mono weight 0.1, ratio weight 0.4, speedup weight 0.5
    total_score += mono_score
    mono_weight = 0.1
    total_weight += mono_weight

    ratio_weight = 0.4
    total_score += score_ratio * ratio_weight
    total_weight += ratio_weight

    speedup_weight = 0.5
    total_score += score_speedup * speedup_weight
    total_weight += speedup_weight

    if total_weight == 0:
        return 0.0
    return total_score / total_weight


_SCORERS = {
    'nucleation_kinetics_check': score_0,
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
