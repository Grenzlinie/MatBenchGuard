import os
import json
import csv

# === author imports / helpers ===
import json
import os
import csv
import sys
import math
from collections import defaultdict

THK = 2.0  # nm

def truncated_exp(x, lam):
    try:
        norm = 1.0 - math.exp(-THK / lam)
        return (1.0 / lam) * math.exp(-x / lam) / norm
    except (ZeroDivisionError, OverflowError):
        return 0.0

def fit_lambda(depths):
    """Fit depths (nm) to truncated exponential, return lambda in nm."""
    if len(depths) == 0:
        return None
    nbins = 20
    bin_edges = [THK * i / nbins for i in range(nbins+1)]
    hist = [0]*nbins
    for d in depths:
        for i in range(nbins):
            if bin_edges[i] <= d < bin_edges[i+1]:
                hist[i] += 1
                break
    total = sum(hist)
    if total == 0:
        return None
    mean_d = sum(depths) / len(depths)
    # Solve mean = lambda - THK * exp(-THK/lambda) / (1 - exp(-THK/lambda))
    lo = 1e-6
    hi = 10.0
    for _ in range(50):
        mid = (lo + hi) / 2
        try:
            en = math.exp(-THK / mid)
            mean_mid = mid - THK * en / (1 - en)
        except (OverflowError, ZeroDivisionError):
            mean_mid = mid
        if mean_mid < mean_d:
            lo = mid
        else:
            hi = mid
    lam = (lo + hi) / 2
    return lam

class _np:
    @staticmethod
    def mean(a):
        return sum(a) / len(a) if a else 0.0
    @staticmethod
    def std(a, ddof=0):
        if len(a) < 2:
            return 0.0
        m = sum(a) / len(a)
        var = sum((x-m)**2 for x in a) / (len(a) - ddof)
        return math.sqrt(var)
    @staticmethod
    def histogram(a, bins=10, range=None):
        if range is None:
            min_a = min(a) if a else 0
            max_a = max(a) if a else 1
        else:
            min_a, max_a = range
        bin_edges = [min_a + i*(max_a - min_a)/bins for i in range(bins+1)]
        hist = [0]*bins
        for x in a:
            for i in range(bins):
                if bin_edges[i] <= x < bin_edges[i+1]:
                    hist[i] += 1
                    break
        return hist, bin_edges
np = _np()

def spearmanr(x, y):
    """Return (correlation, pvalue) using rank correlation."""
    n = len(x)
    if n < 2:
        return (0.0, 1.0)
    def rankdata(v):
        sorted_v = sorted(enumerate(v), key=lambda t: t[1])
        ranks = [0]*n
        i = 0
        while i < n:
            j = i
            while j < n and sorted_v[j][1] == sorted_v[i][1]:
                j += 1
            avg_rank = (i + j - 1) / 2 + 1  # 1-indexed
            for k in range(i, j):
                ranks[sorted_v[k][0]] = avg_rank
            i = j
        return ranks
    rx = rankdata(x)
    ry = rankdata(y)
    mean_rx = sum(rx)/n
    mean_ry = sum(ry)/n
    num = sum((rx[i]-mean_rx)*(ry[i]-mean_ry) for i in range(n))
    den = math.sqrt(sum((rx[i]-mean_rx)**2 for i in range(n)) * sum((ry[i]-mean_ry)**2 for i in range(n)))
    if den == 0:
        return (0.0, 1.0)
    rho = num / den
    return (rho, None)


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


# === block: score_0 (check id='raw_ensemble_check') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) == 0:
        return 0.0
    cond_counts = defaultdict(int)
    for rec in data:
        cond_counts[rec.get('condition_id', -999)] += 1
    for cnt in cond_counts.values():
        if cnt != 100:
            return 0.0
    for rec in data:
        if len(rec.get('ov_depth_positions', [])) != rec.get('ov_count', -1):
            return 0.0
    return 1.0


# === block: score_1 (check id='trends_check') ===
def score_1(artifact, step, ctx):
    raw = artifact
    if not isinstance(raw, list) or len(raw) == 0:
        return 0.0
    csv_path = '/app/outputs/ov_statistics.csv'
    if not os.path.exists(csv_path):
        return 0.0
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        csv_rows = list(reader)
    # build param map: condition_id -> (pO2, T_G_form, WF)
    cond_params = {}
    for row in csv_rows:
        cid = int(row['condition_id'])
        cond_params[cid] = (float(row['pO2']), float(row['T_G_form']), float(row['WF']))

    # group raw by condition_id
    cond_raw = defaultdict(list)
    for rec in raw:
        cond_raw[rec['condition_id']].append(rec)

    # compute per-condition statistics
    cond_stats = {}
    for cid, samples in cond_raw.items():
        counts = [s['ov_count'] for s in samples]
        depths = []
        for s in samples:
            depths.extend(s.get('ov_depth_positions', []))
        mean_cnt = np.mean(counts)
        std_cnt = np.std(counts, ddof=1)
        lam = fit_lambda(depths)
        cond_stats[cid] = (mean_cnt, lam)

    # sweep configs
    sweep_po2_params = step.get('sweep_config', {}).get('pO2_sweep_params', {})
    sweep_T_params = step.get('sweep_config', {}).get('T_sweep_params', {})
    sweep_WF_params = step.get('sweep_config', {}).get('WF_sweep_params', {})

    T_fix = sweep_po2_params.get('T_G_form', 1300)
    WF_fix = sweep_po2_params.get('WF', 4.7)
    po2_fix = sweep_T_params.get('pO2', 5e-8)

    # pO2 sweep conditions: T=T_fix, WF=WF_fix
    pO2_vals = []
    pO2_means = []
    for cid, (mean_cnt, lam) in cond_stats.items():
        if cid not in cond_params: continue
        po2, T, WF = cond_params[cid]
        if abs(T - T_fix) < 1e-6 and abs(WF - WF_fix) < 1e-6:
            pO2_vals.append(po2)
            pO2_means.append(mean_cnt)

    # T sweep: pO2=pO2_fix, WF=WF_fix
    T_means = {}
    for cid, (mean_cnt, lam) in cond_stats.items():
        if cid not in cond_params: continue
        po2, T, WF = cond_params[cid]
        if abs(po2 - po2_fix) < 1e-6 and abs(WF - WF_fix) < 1e-6:
            T_means[T] = mean_cnt

    # WF sweep: pO2=pO2_fix, T=T_fix
    WF_vals = []
    WF_means = []
    for cid, (mean_cnt, lam) in cond_stats.items():
        if cid not in cond_params: continue
        po2, T, WF = cond_params[cid]
        if abs(po2 - po2_fix) < 1e-6 and abs(T - T_fix) < 1e-6:
            WF_vals.append(WF)
            WF_means.append(mean_cnt)

    # lambda vs mean count
    lambdas = []
    means_for_lambda = []
    for cid, (mean_cnt, lam) in cond_stats.items():
        if lam is not None:
            lambdas.append(lam)
            means_for_lambda.append(mean_cnt)

    checks = []
    # 1. pO2 monotonic: mean count should decrease as pO2 increases (negative correlation)
    if len(pO2_vals) >= 3:
        rho, _ = spearmanr(pO2_vals, pO2_means)
        checks.append(rho < -0.5)
    else:
        checks.append(False)
    # 2. T monotonic: count at T=1300 > count at T=750
    if 1300 in T_means and 750 in T_means:
        checks.append(T_means[1300] > T_means[750])
    else:
        checks.append(False)
    # 3. WF monotonic: count should increase with WF (positive correlation)
    if len(WF_vals) >= 3:
        rho, _ = spearmanr(WF_vals, WF_means)
        checks.append(rho > 0.5)
    else:
        checks.append(False)
    # 4. lambda vs count: negative correlation
    if len(lambdas) >= 5:
        rho, _ = spearmanr(means_for_lambda, lambdas)
        checks.append(rho < -0.3)
    else:
        checks.append(False)

    # score: all trends must hold; partial credit not used here because weight is already distributed.
    score = 1.0 if all(checks) else 0.0
    return score


# === block: score_2 (check id='csv_consistency') ===
def score_2(artifact, step, ctx):
    csv_rows = artifact
    if not isinstance(csv_rows, list) or len(csv_rows) == 0:
        return 0.0
    raw_path = '/app/outputs/ov_per_sample.json'
    if not os.path.exists(raw_path):
        return 0.0
    with open(raw_path) as f:
        raw = json.load(f)

    cond_raw = defaultdict(list)
    for rec in raw:
        cond_raw[int(rec['condition_id'])].append(rec)

    # recompute per-condition
    recomputed = {}
    for cid, samples in cond_raw.items():
        counts = [s['ov_count'] for s in samples]
        depths = []
        for s in samples:
            depths.extend(s.get('ov_depth_positions', []))
        mean_cnt = np.mean(counts)
        std_cnt = np.std(counts, ddof=1)
        lam = fit_lambda(depths)
        recomputed[cid] = (mean_cnt, std_cnt, lam)

    # compare against CSV
    ratios_mean = []
    ratios_std = []
    lambda_ok = True
    for row in csv_rows:
        cid = int(row['condition_id'])
        if cid not in recomputed:
            continue
        mean_cnt_rec, std_cnt_rec, lam_rec = recomputed[cid]
        try:
            mean_N_OV = float(row['mean_N_OV'])
            std_N_OV = float(row['std_N_OV'])
            lam_csv = float(row['lambda'])
        except (ValueError, KeyError):
            return 0.0
        if mean_cnt_rec > 0:
            ratios_mean.append(mean_N_OV / mean_cnt_rec)
        if std_cnt_rec > 0:
            ratios_std.append(std_N_OV / std_cnt_rec)
        if lam_rec is not None and lam_csv is not None:
            if abs(lam_rec - lam_csv) > 0.01:
                lambda_ok = False

    # check ratio constancy (small CV)
    def cv(arr):
        if len(arr) == 0:
            return None
        return np.std(arr) / np.mean(arr)

    mean_ratio_cv = cv(ratios_mean)
    std_ratio_cv = cv(ratios_std)

    if mean_ratio_cv is not None and mean_ratio_cv < 0.01 and std_ratio_cv is not None and std_ratio_cv < 0.03 and lambda_ok:
        return 1.0
    else:
        return 0.0


# === block: score_3 (check id='absolute_range_check') ===
def score_3(artifact, step, ctx):
    csv_rows = artifact
    if not isinstance(csv_rows, list):
        return 0.0
    target = step.get('target_condition', {})
    pO2_target = target.get('pO2', 5e-8)
    T_target = target.get('T_G_form', 1300)
    WF_target = target.get('WF', 4.7)
    N_min = step.get('N_OV_min', 2e13)
    N_max = step.get('N_OV_max', 3.9e14)
    for row in csv_rows:
        try:
            po2 = float(row['pO2'])
            T = float(row['T_G_form'])
            WF = float(row['WF'])
            mean_N = float(row['mean_N_OV'])
        except (ValueError, KeyError):
            continue
        if abs(po2 - pO2_target) < 1e-12 and abs(T - T_target) < 1 and abs(WF - WF_target) < 0.01:
            if N_min <= mean_N <= N_max:
                return 1.0
            else:
                return 0.0
    return 0.0


_SCORERS = {
    'raw_ensemble_check': score_0,
    'trends_check': score_1,
    'csv_consistency': score_2,
    'absolute_range_check': score_3,
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
