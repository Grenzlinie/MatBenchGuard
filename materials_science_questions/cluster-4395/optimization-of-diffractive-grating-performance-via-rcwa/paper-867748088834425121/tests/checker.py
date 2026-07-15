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
    # No shared preparation needed beyond the step configs already available
    # Each scorer receives its own step dict with thresholds inline
    return {}


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    # Structural audit for reflectivity_contour.csv
    # artifact is a list of dicts with keys: h2_over_Lambda, normalized_frequency, reflectivity
    if not artifact or not isinstance(artifact, list) or len(artifact) < step.get('min_rows', 50):
        return 0.0
    r_vals = []
    for row in artifact:
        try:
            r = float(row.get('reflectivity', -999))
            r_vals.append(r)
        except (ValueError, TypeError):
            pass
    if not r_vals:
        return 0.0
    # Check reflectivity values are mostly in [0, 1] (allow tiny float overshoot)
    r_range = step.get('range_checks', {}).get('reflectivity', [0.0, 1.0])
    r_lo, r_hi = r_range[0] - 0.01, r_range[1] + 0.01
    in_range_frac = sum(1 for r in r_vals if r_lo <= r <= r_hi) / len(r_vals)
    if in_range_frac < 0.9:
        return 0.3
    # Check data is not degenerate (all same reflectivity)
    if max(r_vals) - min(r_vals) < 0.001:
        return 0.5
    return 1.0


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
    # Recompute fractional bandwidth with R>0.99 from reflectivity_spectrum.csv
    cfg = step.get('recompute_config', {})
    f_col = cfg.get('frequency_column', 'normalized_frequency')
    r_col = cfg.get('reflectivity_column', 'reflectivity')
    r_thresh = cfg.get('reflectivity_threshold', 0.99)
    freqs = []
    refs = []
    for row in artifact:
        try:
            f = float(row.get(f_col, None))
            r = float(row.get(r_col, None))
            freqs.append(f)
            refs.append(r)
        except (ValueError, TypeError):
            pass
    if not freqs:
        return 0.0
    # Sort by frequency
    pairs = sorted(zip(freqs, refs), key=lambda x: x[0])
    freqs = [p[0] for p in pairs]
    refs = [p[1] for p in pairs]
    # Find contiguous intervals where R > threshold
    intervals = []
    in_band = False
    band_start = None
    prev_f = None
    for f, r in zip(freqs, refs):
        if r > r_thresh:
            if not in_band:
                band_start = f
                in_band = True
        else:
            if in_band and band_start is not None and prev_f is not None:
                intervals.append((band_start, prev_f))
                in_band = False
                band_start = None
        prev_f = f
    if in_band and band_start is not None and prev_f is not None:
        intervals.append((band_start, prev_f))
    if not intervals:
        return 0.0
    # Find largest interval by frequency span, compute fractional bandwidth
    largest = max(intervals, key=lambda x: x[1] - x[0])
    f_min, f_max = largest
    f_center = (f_min + f_max) / 2.0
    bandwidth = (f_max - f_min) / f_center if f_center > 0 else 0.0
    target = step.get('target_threshold', 0.30)
    floor_val = step.get('floor_threshold', 0.10)
    if bandwidth >= target:
        return 1.0
    elif bandwidth <= floor_val:
        return 0.0
    else:
        return (bandwidth - floor_val) / (target - floor_val)


# === block: score_2 (check id='step3') ===
def score_2(artifact, step, ctx):
    # Recompute angular range with R>0.99 from angle_scan.csv
    cfg = step.get('recompute_config', {})
    a_col = cfg.get('angle_column', 'angle_deg')
    r_col = cfg.get('reflectivity_column', 'reflectivity')
    r_thresh = cfg.get('reflectivity_threshold', 0.99)
    angles = []
    refs = []
    for row in artifact:
        try:
            a = float(row.get(a_col, None))
            r = float(row.get(r_col, None))
            angles.append(a)
            refs.append(r)
        except (ValueError, TypeError):
            pass
    if not angles:
        return 0.0
    # Sort by angle
    pairs = sorted(zip(angles, refs), key=lambda x: x[0])
    angles = [p[0] for p in pairs]
    refs = [p[1] for p in pairs]
    # Find contiguous intervals where R > threshold
    intervals = []
    in_band = False
    band_start = None
    prev_a = None
    for a, r in zip(angles, refs):
        if r > r_thresh:
            if not in_band:
                band_start = a
                in_band = True
        else:
            if in_band and band_start is not None and prev_a is not None:
                intervals.append((band_start, prev_a))
                in_band = False
                band_start = None
        prev_a = a
    if in_band and band_start is not None and prev_a is not None:
        intervals.append((band_start, prev_a))
    if not intervals:
        return 0.0
    # Find largest contiguous angular span
    largest_span = max(a_end - a_start for a_start, a_end in intervals)
    target = step.get('target_threshold', 40)
    floor_val = step.get('floor_threshold', 10)
    if largest_span >= target:
        return 1.0
    elif largest_span <= floor_val:
        return 0.0
    else:
        return (largest_span - floor_val) / (target - floor_val)


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
    'step3': score_2,
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
