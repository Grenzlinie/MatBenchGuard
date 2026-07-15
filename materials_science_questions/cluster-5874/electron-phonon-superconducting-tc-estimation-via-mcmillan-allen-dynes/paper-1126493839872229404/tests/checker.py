import os
import json
import csv

# === author imports / helpers ===
import math
import statistics

class _Numpy:
    @staticmethod
    def argsort(seq):
        return sorted(range(len(seq)), key=seq.__getitem__)

    @staticmethod
    def array(lst):
        return lst

    @staticmethod
    def polyfit(x, y, deg):
        if deg != 1:
            raise NotImplementedError("Only linear fit supported")
        n = len(x)
        sx = sum(x)
        sy = sum(y)
        sxx = sum(xi*xi for xi in x)
        sxy = sum(xi*yi for xi, yi in zip(x, y))
        denom = n*sxx - sx*sx
        if denom == 0:
            return 0.0, 0.0
        slope = (n*sxy - sx*sy) / denom
        intercept = (sy - slope*sx) / n
        return slope, intercept

    @staticmethod
    def mean(lst):
        return statistics.mean(lst)

np = _Numpy()


def find_peaks(signal, height=0.0):
    n = len(signal)
    peaks = []
    for i in range(1, n-1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1] and signal[i] >= height:
            peaks.append(i)
    return peaks, {}


class LinregressResult:
    __slots__ = ('slope', 'intercept', 'rvalue', 'pvalue', 'stderr')
    def __init__(self, slope, intercept, rvalue=0.0, pvalue=0.0, stderr=0.0):
        self.slope = slope
        self.intercept = intercept
        self.rvalue = rvalue
        self.pvalue = pvalue
        self.stderr = stderr


def linregress(x, y):
    n = len(x)
    if n < 2:
        return LinregressResult(0.0, 0.0)
    sx = sum(x)
    sy = sum(y)
    sxx = sum(xi*xi for xi in x)
    sxy = sum(xi*yi for xi, yi in zip(x, y))
    denom = n*sxx - sx*sx
    if denom == 0:
        return LinregressResult(0.0, 0.0)
    slope = (n*sxy - sx*sy) / denom
    intercept = (sy - slope*sx) / n
    return LinregressResult(slope, intercept)


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


# === block: score_0 (check id='check_specific_heat_upturn') ===
def score_0(artifact, step, ctx):
    if artifact is None or len(artifact) < 4:
        return 0.0
    T_vals = [float(row['T']) for row in artifact]
    CV_vals = [float(row['CV_T']) for row in artifact]
    T2_vals = [t**2 for t in T_vals]
    cfg = step.get('config', {})
    fit_thresh = cfg.get('fit_T2_threshold', 50.0)
    min_ratio = cfg.get('upturn_min_ratio', 1.3)
    lowest_frac = cfg.get('lowest_T2_fraction', 0.2)

    # Sort by T2
    idx_sorted = np.argsort(T2_vals)
    T2_sorted = np.array(T2_vals)[idx_sorted]
    CV_sorted = np.array(CV_vals)[idx_sorted]

    # Points for fitting: T2 > fit_thresh
    idx_fit = T2_sorted > fit_thresh
    if np.sum(idx_fit) < 3:
        return 0.0
    T2_fit = T2_sorted[idx_fit]
    CV_fit = CV_sorted[idx_fit]
    slope, intercept = np.polyfit(T2_fit, CV_fit, 1)

    # Lowest T2 points (fraction)
    low_limit = max(1, int(len(T2_sorted) * lowest_frac))
    lowest_T2 = T2_sorted[:low_limit]
    lowest_CV = CV_sorted[:low_limit]
    mean_low_T2 = np.mean(lowest_T2)
    predicted = intercept + slope * mean_low_T2
    mean_low_CV = np.mean(lowest_CV)
    if predicted <= 0:
        return 0.0
    ratio = mean_low_CV / predicted
    if ratio >= min_ratio:
        return 1.0
    else:
        return max(0.0, (ratio - 1.0) / (min_ratio - 1.0))


# === block: score_1 (check id='check_impurity_resonant_peaks') ===
def score_1(artifact, step, ctx):
    if artifact is None or len(artifact) < 10:
        return 0.0
    omega = np.array([float(row['omega']) for row in artifact])
    A_d = np.array([float(row['A_d']) for row in artifact])
    cfg = step.get('config', {})
    windows = cfg.get('peak_windows', [[-0.6, -0.4], [0.4, 0.6]])
    min_height = cfg.get('min_peak_height', 0.02)

    peaks, properties = find_peaks(A_d, height=min_height)
    peak_energies = omega[peaks]

    windows_found = 0
    for low, high in windows:
        if np.any((peak_energies >= low) & (peak_energies <= high)):
            windows_found += 1

    if len(windows) == 0:
        return 0.0
    score = windows_found / len(windows)
    return float(score)


# === block: score_2 (check id='check_thermal_conductivity_slope') ===
def score_2(artifact, step, ctx):
    if artifact is None or len(artifact) < 4:
        return 0.0
    T_vals = np.array([float(row['T']) for row in artifact])
    kappa_vals = np.array([float(row['kappa_f']) for row in artifact])
    positive = (T_vals > 0) & (kappa_vals > 0)
    if np.sum(positive) < 4:
        return 0.0
    logT = np.log10(T_vals[positive])
    logKappa = np.log10(kappa_vals[positive])
    slope, intercept, r_value, p_value, std_err = linregress(logT, logKappa)
    cfg = step.get('config', {})
    target = cfg.get('target_slope', -2.0)
    tol = cfg.get('slope_tolerance', 0.3)
    dev = abs(slope - target)
    if dev <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (dev - tol) / tol)


_SCORERS = {
    'check_specific_heat_upturn': score_0,
    'check_impurity_resonant_peaks': score_1,
    'check_thermal_conductivity_slope': score_2,
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
