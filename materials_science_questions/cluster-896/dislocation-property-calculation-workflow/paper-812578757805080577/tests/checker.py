import os
import json
import csv

# === author imports / helpers ===
import os
import sys
import subprocess

def _ensure_numpy():
    try:
        import numpy as np
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir",
                               "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
        import numpy as np
    return np

np = _ensure_numpy()


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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import numpy as np
    rows = artifact
    radii = np.array([float(r['radius']) for r in rows])
    mean_r = np.mean(radii)
    score_radius = 1.0 if abs(mean_r - 1.0) <= step['gold']['radius_tol'] else max(0.0, 1.0 - abs(mean_r - 1.0) / 0.1)
    # orientation spread: compute std of each component
    r1 = np.array([float(r['r1']) for r in rows])
    r2 = np.array([float(r['r2']) for r in rows])
    r3 = np.array([float(r['r3']) for r in rows])
    std1 = np.std(r1)
    std2 = np.std(r2)
    std3 = np.std(r3)
    avg_std = (std1 + std2 + std3) / 3.0
    target_sigma = step['gold']['sigma_target']
    sigma_tol = step['gold']['sigma_tol']
    if abs(avg_std - target_sigma) <= sigma_tol:
        score_sigma = 1.0
    else:
        score_sigma = max(0.0, 1.0 - abs(avg_std - target_sigma) / (2*sigma_tol))
    return 0.5 * score_radius + 0.5 * score_sigma


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    import numpy as np
    rows = artifact
    t = np.array([float(r['t']) for r in rows])
    X = np.array([float(r['X']) for r in rows])
    rho = np.array([float(r['rho_rx']) for r in rows])
    meanR = np.array([float(r['mean_R_rx']) for r in rows])

    def interp_at(tvec, yvec, t_target):
        # linear interpolation, assumes tvec sorted
        if t_target <= tvec[0]:
            return yvec[0]
        if t_target >= tvec[-1]:
            return yvec[-1]
        idx = np.searchsorted(tvec, t_target, side='right') - 1
        idx2 = min(idx+1, len(tvec)-1)
        if idx2 == idx:
            return yvec[idx]
        frac = (t_target - tvec[idx]) / (tvec[idx2] - tvec[idx])
        return yvec[idx] * (1-frac) + yvec[idx2] * frac

    # t50: find time when X crosses 0.5
    if X[0] >= 0.5:
        t50 = t[0]
    elif X[-1] <= 0.5:
        t50 = t[-1]
    else:
        cross_idx = np.where(X >= 0.5)[0][0]
        if cross_idx == 0:
            t50 = t[0]
        else:
            t0 = t[cross_idx-1]
            t1 = t[cross_idx]
            x0 = X[cross_idx-1]
            x1 = X[cross_idx]
            t50 = t0 + (0.5 - x0) / (x1 - x0) * (t1 - t0)

    gold = step['gold']
    gold_t50 = gold['t50']
    upper = gold_t50 * gold['t50_upper_multiplier']
    if t50 <= upper:
        score_t50 = 1.0
    else:
        score_t50 = max(0.0, 1.0 - (t50 - upper) / (0.1*gold_t50))

    # rho_rx at t=0.2
    rho_at_02 = interp_at(t, rho, 0.2)
    gold_rho = gold['rho_rx_at_02']
    lower_rho = gold_rho * gold['rho_rx_lower_multiplier']
    if rho_at_02 >= lower_rho:
        score_rho = 1.0
    else:
        score_rho = max(0.0, 1.0 - (lower_rho - rho_at_02) / (0.5*gold_rho))

    # mean_R_rx at t=0.2
    meanR_at_02 = interp_at(t, meanR, 0.2)
    gold_meanR = gold['mean_R_at_02']
    lower_meanR = gold_meanR * gold['mean_R_lower_multiplier']
    if meanR_at_02 >= lower_meanR:
        score_meanR = 1.0
    else:
        score_meanR = max(0.0, 1.0 - (lower_meanR - meanR_at_02) / (0.5*gold_meanR))

    return (score_t50 + score_rho + score_meanR) / 3.0


# === block: score_2 (check id='step_04') ===
def score_2(artifact, step, ctx):
    import numpy as np
    data = artifact
    bin_edges = np.array(data['bin_edges'])
    rec_frac = np.array(data['recrystallized_area_fraction'])
    if len(rec_frac) == 0:
        return 0.0
    # find mode
    peak_idx = np.argmax(rec_frac)
    # bin center
    center = (bin_edges[peak_idx] + bin_edges[peak_idx+1]) / 2.0
    gold = step['gold']
    mode_gold = gold['mode']
    tol = gold['tolerance']
    if abs(center - mode_gold) <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - abs(center - mode_gold) / (3*tol))


# === block: score_3 (check id='step_05') ===
def score_3(artifact, step, ctx):
    import numpy as np
    rows = artifact
    t_vec = np.array([float(r['t']) for r in rows])
    m1 = np.array([float(r['mean_theta']) for r in rows])
    m2 = np.array([float(r['sqrt_second_moment']) for r in rows])

    def interp_at(tvec, yvec, t_target):
        if t_target <= tvec[0]:
            return yvec[0]
        if t_target >= tvec[-1]:
            return yvec[-1]
        idx = np.searchsorted(tvec, t_target, side='right') - 1
        idx2 = min(idx+1, len(tvec)-1)
        if idx2 == idx:
            return yvec[idx]
        frac = (t_target - tvec[idx]) / (tvec[idx2] - tvec[idx])
        return yvec[idx] * (1-frac) + yvec[idx2] * frac

    gold = step['gold']
    t_points = gold['t_points']
    mean_gold = gold['mean_theta_gold']
    sqrt_gold = gold['sqrt_second_moment_gold']
    tol = gold['tolerance']

    scores = []
    for i, tp in enumerate(t_points):
        agent_mean = interp_at(t_vec, m1, tp)
        agent_sqrt = interp_at(t_vec, m2, tp)
        # mean_theta check
        diff1 = abs(agent_mean - mean_gold[i])
        if diff1 <= tol:
            sc1 = 1.0
        else:
            sc1 = max(0.0, 1.0 - diff1 / (2*tol))
        # sqrt_second_moment check
        diff2 = abs(agent_sqrt - sqrt_gold[i])
        if diff2 <= tol:
            sc2 = 1.0
        else:
            sc2 = max(0.0, 1.0 - diff2 / (2*tol))
        scores.append(0.5 * sc1 + 0.5 * sc2)
    return np.mean(scores)


_SCORERS = {
    'step_01': score_0,
    'step_03': score_1,
    'step_04': score_2,
    'step_05': score_3,
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
