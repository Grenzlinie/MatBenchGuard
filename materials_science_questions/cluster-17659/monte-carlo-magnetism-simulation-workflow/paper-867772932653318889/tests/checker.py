import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from collections import defaultdict


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


# === block: score_0 (check id='xi_over_l_data') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0

    L_to_points = defaultdict(list)
    for row in artifact:
        try:
            L = int(row['L'])
            h = float(row['h'])
            xioL = float(row['xi_over_L'])
            L_to_points[L].append((h, xioL))
        except (ValueError, KeyError):
            continue

    pairs = [(8, 16), (12, 24), (16, 32)]
    gold = step.get('gold_h_star', {})
    tol = step.get('h_star_tol', 0.02)
    max_tol = step.get('h_star_max_tol', 0.04)

    scores = []
    for L1, L2 in pairs:
        if L1 not in L_to_points or L2 not in L_to_points:
            scores.append(0.0)
            continue
        pts1 = sorted(L_to_points[L1], key=lambda x: x[0])
        pts2 = sorted(L_to_points[L2], key=lambda x: x[0])
        h1 = np.array([p[0] for p in pts1])
        y1 = np.array([p[1] for p in pts1])
        h2 = np.array([p[0] for p in pts2])
        y2 = np.array([p[1] for p in pts2])

        # Find the h where the interpolated difference changes sign
        h_min = max(h1[0], h2[0])
        h_max = min(h1[-1], h2[-1])
        if h_min >= h_max:
            scores.append(0.0)
            continue
        common_h = np.linspace(h_min, h_max, 200)
        interp1 = np.interp(common_h, h1, y1, left=np.nan, right=np.nan)
        interp2 = np.interp(common_h, h2, y2, left=np.nan, right=np.nan)
        d = interp1 - interp2
        idx = np.where(np.diff(np.sign(d)))[0]
        if len(idx) == 0:
            scores.append(0.0)
            continue
        crossing_h = common_h[idx[0]]
        gold_val = gold.get(str(L1), None)
        if gold_val is None:
            scores.append(1.0)  # no gold to compare, just crossing existence
        else:
            err = abs(crossing_h - gold_val)
            if err <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (err - tol) / (max_tol - tol)))

    return float(np.mean(scores)) if scores else 0.0


# === block: score_1 (check id='barrier_data') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0

    gold_barriers = step.get('gold_barriers', {})
    tol = step.get('barrier_tol', 0.002)
    max_tol = step.get('barrier_max_tol', 0.005)
    gold_theta = step.get('gold_theta', 1.469)
    theta_tol = step.get('theta_tol', 0.03)

    L_agent = artifact.get('L', [])
    Delta = artifact.get('Delta_F_over_N', [])
    if not L_agent or not Delta:
        return 0.0

    barrier_scores = []
    for L_val, D_val in zip(L_agent, Delta):
        if L_val in gold_barriers:
            err = abs(D_val - gold_barriers[L_val])
            if err <= tol:
                barrier_scores.append(1.0)
            else:
                barrier_scores.append(max(0.0, 1.0 - (err - tol) / (max_tol - tol)))
        else:
            barrier_scores.append(0.0)

    barrier_score = np.mean(barrier_scores) if barrier_scores else 0.0

    theta_agent = artifact.get('theta_estimate', None)
    if theta_agent is not None:
        theta_err = abs(theta_agent - gold_theta)
        theta_score = 1.0 if theta_err <= theta_tol else max(0.0, 1.0 - theta_err / theta_tol)
    else:
        theta_score = 0.0

    # Combined: barriers 70%, theta 30%
    return barrier_score * 0.7 + theta_score * 0.3


# === block: score_2 (check id='critical_exponents') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0

    # The paper's Table I lists nu_h = 7.090(9) for L=12, which is a typo.
    # The corrected value used as gold is 0.709.

    def score_array(agent_vals, gold_vals, tol, max_tol):
        if len(agent_vals) != len(gold_vals):
            return 0.0
        scores = []
        for a, g in zip(agent_vals, gold_vals):
            err = abs(a - g)
            if err <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (err - tol) / (max_tol - tol)))
        return np.mean(scores) if scores else 0.0

    def score_single(val, gold, tol):
        if val is None:
            return 0.0
        err = abs(val - gold)
        return 1.0 if err <= tol else max(0.0, 1.0 - err / tol)

    beta_agent = artifact.get('beta_over_nu', [])
    nu_h_agent = artifact.get('nu_h', [])
    nu_T_agent = artifact.get('nu_T', [])

    gold_beta = step.get('gold_beta_over_nu', [])
    gold_nu_h = step.get('gold_nu_h', [])
    gold_nu_T = step.get('gold_nu_T', [])

    if not (beta_agent and nu_h_agent and nu_T_agent and gold_beta and gold_nu_h and gold_nu_T):
        return 0.0

    per_size = (score_array(beta_agent, gold_beta, step['tol_beta'], step['max_tol_beta']) +
                score_array(nu_h_agent, gold_nu_h, step['tol_nu_h'], step['max_tol_nu_h']) +
                score_array(nu_T_agent, gold_nu_T, step['tol_nu_T'], step['max_tol_nu_T'])) / 3.0

    final_scores = []
    for key, gold_key, tol_key in [
        ('final_beta_over_nu', 'gold_final_beta_over_nu', 'tol_final_beta'),
        ('final_nu_h', 'gold_final_nu_h', 'tol_final_nu_h'),
        ('final_nu_T', 'gold_final_nu_T', 'tol_final_nu_T'),
        ('final_theta', 'gold_final_theta', 'tol_final_theta')
    ]:
        val = artifact.get(key, None)
        gold_val = step.get(gold_key, None)
        tol_val = step.get(tol_key, 0.1)
        if gold_val is not None:
            final_scores.append(score_single(val, gold_val, tol_val))
        else:
            final_scores.append(0.0)

    final_score = np.mean(final_scores) if final_scores else 0.0

    return per_size * 0.6 + final_score * 0.4


_SCORERS = {
    'xi_over_l_data': score_0,
    'barrier_data': score_1,
    'critical_exponents': score_2,
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
