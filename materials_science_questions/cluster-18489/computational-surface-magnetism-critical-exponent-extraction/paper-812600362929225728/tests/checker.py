import os
import json
import csv

# === author imports / helpers ===
import csv, math, os, json
from collections import defaultdict

def moving_average(y, window=3):
    if len(y) < window:
        return y
    half = window // 2
    smoothed = []
    for i in range(len(y)):
        start = max(0, i - half)
        end = min(len(y), i + half + 1)
        smoothed.append(sum(y[start:end]) / (end - start))
    return smoothed

def detect_peak(T, C_total, search_range, smooth_window=3):
    # extract data within search range
    indices = [i for i, t in enumerate(T) if search_range[0] <= t <= search_range[1]]
    if len(indices) < 5:
        return None
    T_sub = [T[i] for i in indices]
    C_sub = [C_total[i] for i in indices]
    C_smooth = moving_average(C_sub, smooth_window)
    # find global maximum in smooth data
    max_idx_local = max(range(len(C_smooth)), key=lambda i: C_smooth[i])
    max_temp = T_sub[max_idx_local]
    max_val = C_smooth[max_idx_local]
    # FWHM on smooth data
    half_max = max_val * 0.5
    left = None
    for i in range(max_idx_local, -1, -1):
        if C_smooth[i] <= half_max:
            if i == max_idx_local:
                left = T_sub[i]
            else:
                # linear interpolation between i and i+1
                t1 = T_sub[i]
                t2 = T_sub[i+1]
                c1 = C_smooth[i]
                c2 = C_smooth[i+1]
                if c2 == c1:
                    left = t1
                else:
                    left = t1 + (half_max - c1) * (t2 - t1) / (c2 - c1)
            break
    right = None
    for i in range(max_idx_local, len(C_smooth)):
        if C_smooth[i] <= half_max:
            if i == max_idx_local:
                right = T_sub[i]
            else:
                t1 = T_sub[i-1]
                t2 = T_sub[i]
                c1 = C_smooth[i-1]
                c2 = C_smooth[i]
                if c2 == c1:
                    right = t2
                else:
                    right = t1 + (half_max - c1) * (t2 - t1) / (c2 - c1)
            break
    if left is None or right is None:
        return None
    fwhm = right - left
    return max_temp, max_val, max(fwhm, 0.0)

def detect_compensation(T, m_vals, search_range, smooth_window=3):
    indices = [i for i, t in enumerate(T) if search_range[0] <= t <= search_range[1]]
    if len(indices) < 5:
        return None
    T_sub = [T[i] for i in indices]
    m_sub = [m_vals[i] for i in indices]
    m_smooth = moving_average(m_sub, smooth_window)
    # find minimum absolute value
    min_i = min(range(len(m_smooth)), key=lambda i: abs(m_smooth[i]))
    return T_sub[min_i]


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


# === block: score_0 (check id='check_high_t_peak_scaling') ===
def score_0(artifact, step, ctx):
    params = step.get('params', {})
    conditions = params.get('conditions', [])
    peak_range = params.get('peak_search_range', [900, 1000])
    loc_tol = params.get('location_tolerance', 30)
    expected_low = params.get('expected_location_low', 930)
    expected_high = params.get('expected_location_high', 990)
    height_thresh = params.get('height_increase_threshold', 1.0)
    width_thresh = params.get('width_decrease_threshold', 1.0)
    # Group artifact
    groups = defaultdict(list)
    for row in artifact:
        key = (int(row['L']), int(row['P']), row['boundary'])
        groups[key].append((float(row['T']), float(row['C']), float(row['m'])))
    peaks = {}
    for cond in conditions:
        key = (cond['L'], cond['P'], cond['boundary'])
        if key not in groups:
            return 0.0
        data = groups[key]
        data.sort(key=lambda x: x[0])
        T_vals = [d[0] for d in data]
        C_vals = [d[1] for d in data]
        peak = detect_peak(T_vals, C_vals, peak_range, smooth_window=3)
        if peak is None:
            return 0.0
        peaks[key] = peak
    p6 = peaks[(6,4,'free')]
    p24 = peaks[(24,4,'free')]
    loc6, h6, w6 = p6
    loc24, h24, w24 = p24
    # Location check
    if not (expected_low <= loc6 <= expected_high and expected_low <= loc24 <= expected_high):
        return 0.0
    # Height scaling
    ratio_h = h24 / h6 if h6 > 0 else 0.0
    score_h = 1.0 if ratio_h >= height_thresh else max(0.0, 1.0 - (height_thresh - ratio_h) * 2.0)
    # Width scaling
    ratio_w = w24 / w6 if w6 > 0 else float('inf')
    score_w = 1.0 if ratio_w <= width_thresh else max(0.0, 1.0 - (ratio_w - width_thresh) * 2.0)
    return 0.5 * score_h + 0.5 * score_w


# === block: score_1 (check id='check_low_t_peak_unchanged') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    conditions = params.get('conditions', [])
    peak_range = params.get('peak_search_range', [150, 350])
    expected_low = params.get('expected_location_low', 190)
    expected_high = params.get('expected_location_high', 250)
    max_height_diff = params.get('max_height_relative_diff', 0.20)
    groups = defaultdict(list)
    for row in artifact:
        key = (int(row['L']), int(row['P']), row['boundary'])
        groups[key].append((float(row['T']), float(row['C']), float(row['m'])))
    peaks = {}
    for cond in conditions:
        key = (cond['L'], cond['P'], cond['boundary'])
        if key not in groups:
            return 0.0
        data = groups[key]
        data.sort(key=lambda x: x[0])
        T_vals = [d[0] for d in data]
        C_vals = [d[1] for d in data]
        peak = detect_peak(T_vals, C_vals, peak_range, smooth_window=3)
        if peak is None:
            return 0.0
        peaks[key] = peak
    p6 = peaks[(6,4,'free')]
    p24 = peaks[(24,4,'free')]
    loc6, h6, _ = p6
    loc24, h24, _ = p24
    # Location within tolerance
    if not (expected_low <= loc6 <= expected_high and expected_low <= loc24 <= expected_high):
        return 0.0
    # Height relative difference
    rel_diff = abs(h24 - h6) / h6 if h6 > 0 else 1.0
    score = 1.0 if rel_diff <= max_height_diff else max(0.0, 1.0 - (rel_diff - max_height_diff) * 5.0)
    return score


# === block: score_2 (check id='check_compensation_points') ===
def score_2(artifact, step, ctx):
    params = step.get('params', {})
    conditions = params.get('conditions', [])
    search_range = params.get('search_range', [300, 700])
    groups = defaultdict(list)
    for row in artifact:
        key = (int(row['L']), int(row['P']), row['boundary'])
        groups[key].append((float(row['T']), float(row['C']), float(row['m'])))
    scores = []
    for cond in conditions:
        key = (cond['L'], cond['P'], cond['boundary'])
        expected = cond['expected_comp']
        tol = cond['tolerance']
        if key not in groups:
            scores.append(0.0)
            continue
        data = groups[key]
        data.sort(key=lambda x: x[0])
        T_vals = [d[0] for d in data]
        M_vals = [d[2] for d in data]
        comp_temp = detect_compensation(T_vals, M_vals, search_range, smooth_window=3)
        if comp_temp is None:
            scores.append(0.0)
            continue
        error = abs(comp_temp - expected)
        if error <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (error - tol) / tol))
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'check_high_t_peak_scaling': score_0,
    'check_low_t_peak_unchanged': score_1,
    'check_compensation_points': score_2,
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
