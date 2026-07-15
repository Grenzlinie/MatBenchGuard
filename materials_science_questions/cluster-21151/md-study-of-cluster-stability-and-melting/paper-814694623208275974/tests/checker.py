import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import re


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


# === block: score_0 (check id='pdf_peaks') ===
def score_0(artifact, step, ctx):
    r = np.array([float(row['r']) for row in artifact])
    # we only need 300 K columns here
    co_300 = np.array([float(row['Co_B_g_300K']) for row in artifact])
    b_300 = np.array([float(row['B_B_g_300K']) for row in artifact])
    config = step.get('config', {})
    gold_peaks = config.get('gold_peaks', {})
    tol = config.get('tolerance_abs', 0.05)

    def score_peak(r_vals, g_vals, r_range, target):
        mask = (r_vals >= r_range[0]) & (r_vals <= r_range[1])
        if not np.any(mask):
            return 0.0
        idx_max = np.argmax(g_vals[mask])
        r_peak = r_vals[mask][idx_max]
        dif = abs(r_peak - target)
        if dif <= tol:
            return 1.0
        elif dif <= 2*tol:
            return 1.0 - (dif - tol) / tol
        else:
            return 0.0

    scores = []
    scores.append(score_peak(r, co_300, [1.5, 2.3], gold_peaks.get('Co_B_first', 1.98)))
    scores.append(score_peak(r, b_300, [1.5, 2.2], gold_peaks.get('B_B_first', 1.85)))
    scores.append(score_peak(r, b_300, [2.4, 3.5], gold_peaks.get('B_B_second', 2.9)))
    return float(np.mean(scores))


# === block: score_1 (check id='pdf_trend') ===
def score_1(artifact, step, ctx):
    r = np.array([float(row['r']) for row in artifact])
    # identify high‑T columns
    keys = artifact[0].keys()
    def get_highT_col(pattern, keys):
        for k in keys:
            if k.startswith(pattern) and k != pattern+'_300K':
                return k
        raise ValueError(f'no high‑T column for pattern {pattern}')
    co_high_key = get_highT_col('Co_B_g', keys)
    b_high_key = get_highT_col('B_B_g', keys)
    co_300 = np.array([float(row['Co_B_g_300K']) for row in artifact])
    b_300 = np.array([float(row['B_B_g_300K']) for row in artifact])
    co_high = np.array([float(row[co_high_key]) for row in artifact])
    b_high = np.array([float(row[b_high_key]) for row in artifact])

    # define windows
    windows = {
        'Co_B_first': (1.5, 2.3),
        'B_B_first': (1.5, 2.2),
        'B_B_second': (2.4, 3.5)
    }
    def max_in_window(r, g, win):
        mask = (r >= win[0]) & (r <= win[1])
        if not np.any(mask):
            return 0.0
        return np.max(g[mask])

    count = 0
    if max_in_window(r, co_high, windows['Co_B_first']) < max_in_window(r, co_300, windows['Co_B_first']):
        count += 1
    if max_in_window(r, b_high, windows['B_B_first']) < max_in_window(r, b_300, windows['B_B_first']):
        count += 1
    if max_in_window(r, b_high, windows['B_B_second']) < max_in_window(r, b_300, windows['B_B_second']):
        count += 1
    return count / 3.0


# === block: score_2 (check id='bond_angle_trend') ===
def score_2(artifact, step, ctx):
    angle = np.array([float(row['angle_degrees']) for row in artifact])
    # identify high‑T column
    keys = artifact[0].keys()
    def get_highT_col(keys):
        for k in keys:
            if k.startswith('probability_') and k != 'probability_300K':
                return k
        raise ValueError('no high‑T column for probability')
    high_key = get_highT_col(keys)
    prob_300 = np.array([float(row['probability_300K']) for row in artifact])
    prob_high = np.array([float(row[high_key]) for row in artifact])
    # Find peak near 90 deg in window 80-100
    mask = (angle >= 80) & (angle <= 100)
    if not np.any(mask):
        return 0.0
    max_300 = np.max(prob_300[mask])
    max_high = np.max(prob_high[mask])
    if max_high < max_300:
        return 1.0
    else:
        return 0.0


# === block: score_3 (check id='voronoi_fractions') ===
def score_3(artifact, step, ctx):
    # artifact is a dict
    def get_val(key):
        for k in artifact.keys():
            if k.startswith('Frank_Kasper_fraction_'):
                if k.endswith('_300K'):
                    if key == '300':
                        return float(artifact[k])
                elif k.endswith('_highT'):
                    if key == 'high':
                        # highT key does not encode a numeric temperature; return None for T
                        return float(artifact[k]), None
                else:
                    # parse temperature
                    parts = k.split('_')
                    try:
                        temp_str = parts[-1]
                        if temp_str.endswith('K'):
                            T = int(temp_str[:-1])
                            if key == 'high':
                                return float(artifact[k]), T
                    except:
                        pass
        raise ValueError('cannot find the expected keys')

    frac_300 = get_val('300')
    frac_high, T_high = get_val('high')  # high returns tuple

    config = step.get('config', {})
    gold_frac_300K = config.get('gold_frac_300K', 0.50)
    tol_300 = config.get('tolerance_abs_300K', 0.05)

    def score_300(fv):
        dif = abs(fv - gold_frac_300K)
        if dif <= tol_300:
            return 1.0
        elif dif <= 2*tol_300:
            return 1.0 - (dif - tol_300) / tol_300
        else:
            return 0.0

    s1 = score_300(frac_300)

    # trend: frac_high < frac_300 - 0.10
    if frac_high < frac_300 - 0.10:
        s2 = 1.0
    elif frac_high < frac_300:
        s2 = 0.5
    else:
        s2 = 0.0

    # consistency with temperature: linear interpolation 0.5 at 300 K, 0.35 at 1600 K
    if T_high:
        expected = 0.5 - (T_high - 300.0) / 1300.0 * 0.15
        dif3 = abs(frac_high - expected)
        if dif3 <= 0.05:
            s3 = 1.0
        elif dif3 <= 0.10:
            s3 = 1.0 - (dif3 - 0.05) / 0.05
        else:
            s3 = 0.0
    else:
        # fallback range check
        if 0.25 <= frac_high <= 0.45:
            s3 = 1.0
        elif 0.20 <= frac_high <= 0.50:
            s3 = 0.5
        else:
            s3 = 0.0

    return 0.4 * s1 + 0.3 * s2 + 0.3 * s3


_SCORERS = {
    'pdf_peaks': score_0,
    'pdf_trend': score_1,
    'bond_angle_trend': score_2,
    'voronoi_fractions': score_3,
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
