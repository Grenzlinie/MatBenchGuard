import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ImportError:
    class _NumpyFallback:
        @staticmethod
        def polyfit(x, y, deg):
            # linear least squares (deg must be 1)
            if deg != 1:
                raise NotImplementedError("pure-python polyfit only supports deg=1")
            n = len(x)
            sx = sum(x)
            sy = sum(y)
            sx2 = sum(xi*xi for xi in x)
            sxy = sum(xi*yi for xi, yi in zip(x, y))
            slope = (n*sxy - sx*sy) / (n*sx2 - sx*sx)
            intercept = (sy - slope*sx) / n
            return slope, intercept
    np = _NumpyFallback()


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


# === block: score_0 (check id='step_band_gaps') ===
def score_0(artifact, step, ctx):
    pressures = [float(r['pressure']) for r in artifact]
    gaps = [float(r['Eg_gamma_gamma']) for r in artifact]
    slope, intercept = np.polyfit(pressures, gaps, 1)
    ref_slope = step['config']['slope_reference_meV_per_GPa'] / 1000.0
    tol_slope = step['config']['tolerance_meV_per_GPa'] / 1000.0
    diff = abs(slope - ref_slope)
    if diff <= tol_slope:
        slope_score = 1.0
    else:
        slope_score = max(0.0, 1.0 - (diff - tol_slope) / 0.01)
    ref_gaps = step['config']['gap_reference_0GPa']
    tol_gap = step['config']['gap_tolerance_eV']

    # 0 GPa absolute checks only for the two values the paper explicitly reports
    match_scores = []
    for col in ['Eg_gamma_gamma', 'Eg_L_Gamma']:
        val = None
        for row in artifact:
            if abs(float(row['pressure'])) < 1e-6:
                val = float(row[col])
                break
        if val is not None and abs(val - ref_gaps[col]) <= tol_gap:
            match_scores.append(1.0)
        else:
            match_scores.append(0.0)

    # Structural trend checks for the other two gaps (L-L, X-X): they must increase with pressure
    def _monotonic_increasing(artifact, col):
        sorted_rows = sorted(artifact, key=lambda r: float(r['pressure']))
        vals = [float(row[col]) for row in sorted_rows]
        return 1.0 if all(x < y for x, y in zip(vals, vals[1:])) else 0.0

    trend_scores = [
        _monotonic_increasing(artifact, 'Eg_L_L'),
        _monotonic_increasing(artifact, 'Eg_X_X')
    ]

    gap_score = (sum(match_scores) + sum(trend_scores)) / 4.0
    return 0.5 * slope_score + 0.5 * gap_score


# === block: score_1 (check id='step_optical') ===
def score_1(artifact, step, ctx):
    pressures = step['config']['pressures']
    peak_range = step['config']['peak_finding_range_eV']
    threshold = step['config']['absorption_edge_threshold']

    def find_first_peak_py(energy, eps2, peak_range):
        mask = [peak_range[0] <= e <= peak_range[1] for e in energy]
        if not any(mask):
            return None
        # collect (eps2_value, original_index) for masked region
        masked = [(eps2[i], i) for i, m in enumerate(mask) if m]
        if not masked:
            return None
        best = max(masked, key=lambda x: x[0])
        return energy[best[1]]

    def find_edge_py(energy, absorption, thresh):
        for i, ab in enumerate(absorption):
            if ab >= thresh:
                return energy[i]
        return None

    peaks = {}
    edges = {}
    for p in pressures:
        d = artifact[p]
        en = d['energy']   # list of floats
        ep2 = d['epsilon2']
        ab = d['absorption']
        peak_val = find_first_peak_py(en, ep2, peak_range)
        edge_val = find_edge_py(en, ab, threshold)
        if peak_val is None or edge_val is None:
            return 0.0
        peaks[p] = peak_val
        edges[p] = edge_val

    peak_vals = [peaks[str(p)] for p in pressures]
    edge_vals = [edges[str(p)] for p in pressures]
    peak_ok = all(peak_vals[i] < peak_vals[i+1] for i in range(len(peak_vals)-1))
    edge_ok = all(edge_vals[i] < edge_vals[i+1] for i in range(len(edge_vals)-1))
    score = 0.0
    if peak_ok:
        score += 0.5
    if edge_ok:
        score += 0.5
    return score


_SCORERS = {
    'step_band_gaps': score_0,
    'step_optical': score_1,
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
