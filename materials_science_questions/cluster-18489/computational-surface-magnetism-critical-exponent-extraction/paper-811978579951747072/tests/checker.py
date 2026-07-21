import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve
import math

# energy parameters (reduced units)
v_AA_s = 0.7
v_BB_s = 0.9
v_AB_s = 1.4
w_s = 1.2
v_AA_prime = 0.8
v_BB_prime = 1.0
v_AB_prime = 1.7
w_prime = 1.6
v_AA = 0.4
v_BB = 0.8
v_AB = 1.1
w = 1.0

def _f1_eq(csA, mu, tau):
    if mu == 0.0:
        return 0.0
    arg = (1.0+mu)/(1.0-mu)
    if arg <= 0:
        return 1e9
    return tau * np.log(arg) - 4.0 * csA**2 * mu

def _f2_eq(csA, cA, tau):
    ratio = csA * (1.0 - cA) / ((1.0 - csA) * cA)
    if ratio <= 0:
        return 1e9
    log_term = np.log(ratio)
    term1 = 4.0 * (v_AA - v_BB + (1.0 - 2.0*cA) * w)
    term2 = -2.0 * (v_AA_s - v_BB_s + (1.0 - 2.0*csA) * w_s)
    term3 = -(v_AA_prime - v_BB_prime + (1.0 - 2.0*cA) * w_prime)
    return tau * log_term + term1 + term2 + term3

def solve_csA_tau(cA, mu):
    """Solve for csA, tau given cA and fixed mu."""
    def eqs(vars):
        csA, tau = vars
        if csA <= 0.0 or csA >= 1.0 or tau <= 0.0:
            return [1e9, 1e9]
        f1 = _f1_eq(csA, mu, tau)
        f2 = _f2_eq(csA, cA, tau)
        return [f1, f2]
    guess_csA = min(max(cA * 1.2, 0.01), 0.99)
    guess_tau = 0.5
    try:
        sol = fsolve(eqs, [guess_csA, guess_tau], maxfev=1000, xtol=1e-8)
        csA_sol, tau_sol = sol[0], sol[1]
        if np.isnan(csA_sol) or np.isnan(tau_sol):
            return (np.nan, np.nan)
        return (csA_sol, tau_sol)
    except Exception:
        return (np.nan, np.nan)

def solve_csA_mu(cA, tau):
    """Solve for csA, mu given cA and fixed tau."""
    def eqs(vars):
        csA, mu = vars
        if csA <= 0.0 or csA >= 1.0 or mu <= 0.0 or mu >= 1.0:
            return [1e9, 1e9]
        f1 = _f1_eq(csA, mu, tau)
        f2 = _f2_eq(csA, cA, tau)
        return [f1, f2]
    guess_csA = min(max(cA * 1.2, 0.01), 0.99)
    if tau < 1.0:
        guess_mu = 0.8
    else:
        guess_mu = 0.1
    try:
        sol = fsolve(eqs, [guess_csA, guess_mu], maxfev=1000, xtol=1e-8)
        csA_sol, mu_sol = sol[0], sol[1]
        if np.isnan(csA_sol) or np.isnan(mu_sol):
            return (np.nan, np.nan)
        return (csA_sol, mu_sol)
    except Exception:
        return (np.nan, np.nan)

def has_first_order_jump(mu_seq, tau_seq):
    """Return True if mu drops abruptly (discontinuity) as tau increases."""
    # find where mu transitions from >0.3 to <0.1 with a large drop
    for i in range(len(tau_seq)-1):
        if mu_seq[i] > 0.3 and mu_seq[i+1] < 0.1:
            if mu_seq[i] - mu_seq[i+1] > 0.3:
                return True
    return False


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
    return {'tolerance': 0.05, 'jump_threshold': 0.3}


# === block: score_0 (check id='step_fig1') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact  # list of dict from csv
    cA_vals = [float(r['cA']) for r in artifact_rows]
    mu_vals = [0.0, 0.5, 1.0]
    col_map = {0.0: 'csA_mu0', 0.5: 'csA_mu0p5', 1.0: 'csA_mu1'}
    total = 0
    pass_count = 0
    for mu in mu_vals:
        col = col_map[mu]
        for i, cA in enumerate(cA_vals):
            agent_val = float(artifact_rows[i].get(col, np.nan))
            if np.isnan(agent_val):
                continue
            ref_csA, _ = solve_csA_tau(cA, mu)
            if np.isnan(ref_csA):
                continue
            if abs(agent_val - ref_csA) <= ctx['tolerance']:
                pass_count += 1
            total += 1
    if total == 0:
        return 0.0
    return pass_count / total


# === block: score_1 (check id='step_fig2') ===
def score_1(artifact, step, ctx):
    artifact_rows = artifact
    mu_vals = [float(r['mu']) for r in artifact_rows]
    cA_vals = [0.001, 0.01, 0.05, 0.1]
    col_map = {0.001: 'csA_cA0p001', 0.01: 'csA_cA0p01', 0.05: 'csA_cA0p05', 0.1: 'csA_cA0p1'}
    total = 0
    pass_count = 0
    for cA in cA_vals:
        col = col_map[cA]
        for i, mu in enumerate(mu_vals):
            agent_val = float(artifact_rows[i].get(col, np.nan))
            if np.isnan(agent_val):
                continue
            ref_csA, _ = solve_csA_tau(cA, mu)
            if np.isnan(ref_csA):
                continue
            if abs(agent_val - ref_csA) <= ctx['tolerance']:
                pass_count += 1
            total += 1
    if total == 0:
        return 0.0
    return pass_count / total


# === block: score_2 (check id='step_fig3') ===
def score_2(artifact, step, ctx):
    artifact_rows = artifact
    tau_vals = [float(r['tau']) for r in artifact_rows]
    cA_vals = [0.01, 0.05, 0.1]
    col_map = {0.01: 'mu_cA0p01', 0.05: 'mu_cA0p05', 0.1: 'mu_cA0p1'}
    total = 0
    pass_count = 0
    jump_flags = []
    for cA in cA_vals:
        col = col_map[cA]
        mu_agent = []
        mu_ref = []
        for i, tau in enumerate(tau_vals):
            agent_val = float(artifact_rows[i].get(col, np.nan))
            if np.isnan(agent_val):
                continue
            mu_agent.append(agent_val)
            _, ref_mu = solve_csA_mu(cA, tau)
            mu_ref.append(ref_mu if not np.isnan(ref_mu) else np.nan)
            if not np.isnan(ref_mu) and abs(agent_val - ref_mu) <= ctx['tolerance']:
                pass_count += 1
            total += 1
        # check jump on agent's mu values (use only non-nan)
        valid_mu = [m for m in mu_agent if not np.isnan(m)]
        valid_tau = [tau_vals[i] for i in range(len(tau_vals)) if not np.isnan(artifact_rows[i].get(col, np.nan))]
        if valid_mu:
            # sort by tau to detect jump
            sorted_pairs = sorted(zip(valid_tau, valid_mu), key=lambda x: x[0])
            sorted_tau, sorted_mu = zip(*sorted_pairs)
            if has_first_order_jump(sorted_mu, sorted_tau):
                jump_flags.append(1.0)
            else:
                jump_flags.append(0.0)
        else:
            jump_flags.append(0.0)
    pointwise_score = pass_count / total if total > 0 else 0.0
    jump_score = sum(jump_flags) / len(jump_flags) if jump_flags else 0.0
    return 0.7 * pointwise_score + 0.3 * jump_score


_SCORERS = {
    'step_fig1': score_0,
    'step_fig2': score_1,
    'step_fig3': score_2,
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
