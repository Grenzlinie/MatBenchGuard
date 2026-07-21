import os
import json
import csv

# === author imports / helpers ===
import numpy as np

def _argrelextrema(data, comparator, order=1):
    """Mimic scipy.signal.argrelextrema for 1D arrays.
    Returns a tuple (indices,) so that caller can unpack [0]."""
    data = np.asarray(data)
    if data.size < 3:
        return (np.array([]),)
    n = len(data)
    indices = []
    for i in range(1, n - 1):
        if comparator(data[i], data[i - 1]) and comparator(data[i], data[i + 1]):
            indices.append(i)
    return (np.array(indices),)

argrelextrema = _argrelextrema


def curve_fit(f, xdata, ydata, p0=None, maxfev=None):
    """Replacement for scipy.optimize.curve_fit for the specific exponential
    decay model y = A * exp(-k * t).  Uses log‑transform and linear least‑squares."""
    x = np.asarray(xdata, dtype=float)
    y = np.asarray(ydata, dtype=float)
    mask = y > 0
    if not np.any(mask):
        return np.array([1.0, 0.0]), np.zeros((2, 2))
    x = x[mask]
    logy = np.log(y[mask])
    A_mat = np.column_stack((np.ones_like(x), x))
    try:
        coeffs, residuals, rank, s = np.linalg.lstsq(A_mat, logy, rcond=None)
    except np.linalg.LinAlgError:
        return np.array([1.0, 0.0]), np.zeros((2, 2))
    b0, b1 = coeffs
    A = np.exp(b0)
    k = -b1
    pcov = np.zeros((2, 2))
    if len(residuals) > 0 and rank == 2:
        dof = len(x) - 2
        if dof > 0:
            var = residuals[0] / dof
            try:
                XtX_inv = np.linalg.inv(A_mat.T @ A_mat)
                pcov = var * XtX_inv
            except np.linalg.LinAlgError:
                pass
    return np.array([A, k]), pcov


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


# === block: score_0 (check id='check_magnetization_oscillation') ===
def score_0(artifact, step, ctx):
    times = np.array([float(r['time']) for r in artifact])
    vals = np.array([float(r['magnetization']) for r in artifact])
    last_rows = step.get('params', {}).get('last_rows', 100)
    mean_thresh = step.get('params', {}).get('mean_threshold', 0.1)
    transient_frac = step.get('params', {}).get('transient_fraction', 0.1)
    mean_val = np.mean(vals[-last_rows:])
    mean_ok = 1.0 if abs(mean_val) < mean_thresh else 0.0
    N = len(vals)
    start_idx = int(transient_frac * N)
    local_min = argrelextrema(vals, np.less_equal)[0]
    local_max = argrelextrema(vals, np.greater_equal)[0]
    osc_ok = 0.0
    for mn in local_min:
        if mn >= start_idx:
            for mx in local_max:
                if mx > mn:
                    osc_ok = 1.0
                    break
            if osc_ok:
                break
    score = 0.5 * mean_ok + 0.5 * osc_ok
    return score


# === block: score_1 (check id='check_fluctuation_scaling') ===
def score_1(artifact, step, ctx):
    Ls = np.array([float(r['L']) for r in artifact])
    stds = np.array([float(r['std_magnetization']) for r in artifact])
    logL = np.log(Ls)
    logS = np.log(stds)
    coeffs = np.polyfit(logL, logS, 1)
    slope = coeffs[0]
    residuals = logS - (coeffs[0]*logL + coeffs[1])
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((logS - np.mean(logS))**2)
    r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 1e-12 else 0.0
    slope_range = step.get('params', {}).get('slope_range', [-1.2, -0.8])
    r2_thresh = step.get('params', {}).get('r2_threshold', 0.8)
    slope_ok = slope_range[0] <= slope <= slope_range[1]
    r2_ok = r2 > r2_thresh
    score = 1.0 if (slope_ok and r2_ok) else 0.0
    return score


# === block: score_2 (check id='check_irreversible_decay') ===
def score_2(artifact, step, ctx):
    t_all = np.array([float(r['time']) for r in artifact])
    f_all = np.array([float(r['fraction_buyers']) for r in artifact])
    n_discard = step.get('params', {}).get('discard_first', 100)
    if len(t_all) <= n_discard:
        return 0.0
    t = t_all[n_discard:]
    f = f_all[n_discard:]
    def exp_model(t, A, k):
        return A * np.exp(-k * t)
    try:
        popt, _ = curve_fit(exp_model, t, f, p0=(1.0, 0.01), maxfev=10000)
        A, k = popt
        f_pred = exp_model(t, A, k)
        ss_res = np.sum((f - f_pred)**2)
        ss_tot = np.sum((f - np.mean(f))**2)
        r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 1e-12 else 0.0
        r2_thresh = step.get('params', {}).get('r2_threshold', 0.8)
        min_k = step.get('params', {}).get('min_k', 1e-10)
        score = 1.0 if (k > min_k and r2 > r2_thresh) else 0.0
    except:
        score = 0.0
    return score


_SCORERS = {
    'check_magnetization_oscillation': score_0,
    'check_fluctuation_scaling': score_1,
    'check_irreversible_decay': score_2,
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
