import os
import json
import csv

# === author imports / helpers ===
import csv
import os
from typing import List, Tuple

def find_high_intervals(wavelengths, reflectivities, threshold=0.995):
    intervals = []
    start = None
    for wl, r in zip(wavelengths, reflectivities):
        if r > threshold:
            if start is None:
                start = wl
        else:
            if start is not None:
                intervals.append((start, wl))
                start = None
    if start is not None:
        intervals.append((start, wavelengths[-1]))
    return intervals

def band_intersection_coverage(agent_intervals, expected_band):
    """
    Return fraction of [expected_band] wavelength width where agent has reflectivity > threshold.
    agent_intervals: list of (start, end) in µm
    """
    a0, a1 = expected_band
    total_band_width = a1 - a0
    if total_band_width <= 0:
        return 0.0
    covered = 0.0
    for start, end in agent_intervals:
        # clip to expected band
        c0 = max(start, a0)
        c1 = min(end, a1)
        if c1 > c0:
            covered += c1 - c0
    return min(1.0, covered / total_band_width)

def intervals_overlap_width(intervals1, intervals2):
    """Return total width of intersection of two sets of intervals."""
    # simple O(n*m) fine for small intervals
    width = 0.0
    for s1, e1 in intervals1:
        for s2, e2 in intervals2:
            start = max(s1, s2)
            end = min(e1, e2)
            if end > start:
                width += end - start
    return width


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


# === block: score_0 (check id='step_tm') ===
def score_0(artifact, step, ctx):
    import csv, os
    threshold = float(step.get('reflectivity_threshold', 0.995))
    expected_band = step.get('expected_band', [0.705, 0.875])
    # convert dict list to arrays
    wavelengths = []
    reflectivities = []
    for row in artifact:
        wl = float(row['wavelength'])
        r = float(row['reflectivity'])
        wavelengths.append(wl)
        reflectivities.append(r)
    intervals = find_high_intervals(wavelengths, reflectivities, threshold)
    coverage = band_intersection_coverage(intervals, expected_band)
    return coverage


# === block: score_1 (check id='step_te') ===
def score_1(artifact, step, ctx):
    import csv, os
    threshold = float(step.get('reflectivity_threshold', 0.995))
    expected_te_bands = step.get('expected_te_bands', [[0.749,0.794],[0.831,0.944]])
    expected_overlap_width = float(step.get('expected_overlap_width_um', 0.089))
    # parse TE artifact
    wavelengths = []
    reflectivities = []
    for row in artifact:
        wl = float(row['wavelength'])
        r = float(row['reflectivity'])
        wavelengths.append(wl)
        reflectivities.append(r)
    te_intervals = find_high_intervals(wavelengths, reflectivities, threshold)
    # TE band coverage: sum over expected bands
    total_expected_width = sum(band[1]-band[0] for band in expected_te_bands)
    if total_expected_width <= 0:
        te_coverage = 0.0
    else:
        covered = 0.0
        for band in expected_te_bands:
            for start, end in te_intervals:
                c0 = max(start, band[0])
                c1 = min(end, band[1])
                if c1 > c0:
                    covered += c1 - c0
        te_coverage = min(1.0, covered / total_expected_width)

    # load TM file for overlap computation
    tm_path = os.path.join('/app/outputs', 'tm_reflectivity.csv')
    tm_intervals = []
    if os.path.exists(tm_path):
        with open(tm_path, newline='') as f:
            reader = csv.DictReader(f)
            tm_wls = []
            tm_refs = []
            for row in reader:
                tm_wls.append(float(row['wavelength']))
                tm_refs.append(float(row['reflectivity']))
            tm_intervals = find_high_intervals(tm_wls, tm_refs, threshold)

    overlap_width = intervals_overlap_width(te_intervals, tm_intervals)
    overlap_fraction = min(1.0, overlap_width / expected_overlap_width) if expected_overlap_width > 0 else 0.0

    # equal weight to TE bands and overlap
    score = (te_coverage + overlap_fraction) / 2.0
    return max(0.0, min(1.0, score))


_SCORERS = {
    'step_tm': score_0,
    'step_te': score_1,
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
