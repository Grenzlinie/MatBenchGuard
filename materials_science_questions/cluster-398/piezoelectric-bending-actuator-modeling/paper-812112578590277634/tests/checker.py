import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='voltage_table') ===
def score_0(artifact, step, ctx):
    import math
    import numpy as np
    from scipy.integrate import solve_ivp
    from scipy.optimize import brentq

    def compute_u_stat_ode(eta, Q, a, b, gamma):
        """
        Numerical steady-state voltage solver matching the instruction's ODE model.
        Solves u_p'' + (1/Q) u_p' + u_p = F(tau) - gamma  for u_stat > 0,
        with F(tau) = eta^2 cos(eta*tau) + (eta/Q) sin(eta*tau).
        Normalization: alpha=1, Cp=1, hat_x_p=1.
        """
        nu_sq = max(1e-12, 1.0 - 1.0 / (4.0 * Q * Q))
        nu = math.sqrt(nu_sq)
        delta_tau = b * (2.0 * math.pi / nu)
        tau_close = (a - b / 2.0) * (2.0 * math.pi / nu)

        # Open-circuit voltage change (eq. 3 in instruction, normalized)
        delta_u_open = math.cos((2.0 * a - b) * math.pi * eta) + math.cos((2.0 * a + b) * math.pi * eta)

        # Initial derivative at switch closure: u_p'(0) = eta * sin(eta * tau_close)
        up_init_deriv = eta * math.sin(eta * tau_close)

        def rhs(tau, y):
            up, up_prime = y
            F = eta * eta * math.cos(eta * tau) + (eta / Q) * math.sin(eta * tau)
            return [up_prime, -up_prime / Q - up + F - gamma]

        def objective(u_guess):
            u0 = max(u_guess, 0.0)
            sol = solve_ivp(rhs, [0.0, delta_tau], [u0, up_init_deriv],
                            method='RK45', rtol=1e-9, atol=1e-12)
            up_final = sol.y[0, -1]
            return abs(up_final) - u0 + delta_u_open

        # Find bracket and solve for root
        f0 = objective(0.0)
        if abs(f0) < 1e-12:
            return 0.0
        for upper in [5.0, 10.0, 20.0, 50.0, 100.0, 200.0]:
            fu = objective(upper)
            if f0 * fu <= 0.0:
                return brentq(objective, 0.0, upper, xtol=1e-10, rtol=1e-10)
        return 0.0


    # ---- Scoring ----
    table = artifact.get('voltage_table', [])
    if not table:
        return 0.0

    TOL = 1e-4
    correct = 0
    for entry in table:
        eta = float(entry.get('eta', 0))
        Q_val = float(entry.get('Q', 0))
        a_val = float(entry.get('a', 0))
        b_val = float(entry.get('b', 0))
        gamma_val = float(entry.get('gamma', 0))
        agent_u = float(entry.get('u_stat', 0))

        gold_u = compute_u_stat_ode(eta, Q_val, a_val, b_val, gamma_val)
        if abs(agent_u - gold_u) <= TOL:
            correct += 1

    return correct / len(table)


# === block: score_1 (check id='optimal_law') ===
def score_1(artifact, step, ctx):
    import math
    alpha = 1.0
    Cp = 1.0
    hat_x_p = 1.0
    eta = 0.5
    Q = 10.0
    gamma = 0.0

    def compute_u_stat(eta, Q, a, b, gamma, alpha, Cp, hat_x_p):
        nu = math.sqrt(max(0, 1 - 1/(4*Q*Q)))
        term1 = math.cos(math.pi * eta / 2)
        exp_term = math.exp(-math.pi / (2 * Q * nu))
        term2 = (1 + exp_term) * math.sin(math.pi * eta / (2 * nu)) * nu * eta / math.pi
        A = 2 * alpha / Cp * (term1 + term2) / (1 - exp_term) * hat_x_p
        B = (1 + exp_term) / (1 - exp_term) * gamma * hat_x_p
        return A + B

    nu = math.sqrt(max(0, 1 - 1/(4*Q*Q)))
    expected_b = 1/(2*nu)
    gold_peak = compute_u_stat(eta, Q, 0, expected_b, gamma, alpha, Cp, hat_x_p)
    opt = artifact.get('optimal_law', {})
    a_opt = float(opt.get('a_opt', 0))
    b_opt = float(opt.get('b_opt', 0))
    peak_voltage = float(opt.get('peak_voltage', 0))

    a_ok = abs(a_opt - 0) <= 0.01
    b_ok = abs(b_opt - expected_b) <= 0.01
    peak_ok = abs(peak_voltage - gold_peak) / max(1.0, abs(gold_peak)) <= 1e-5
    return (a_ok + b_ok + peak_ok) / 3.0


# === block: score_2 (check id='equivalence') ===
def score_2(artifact, step, ctx):
    alpha = 1.0
    Cp = 1.0
    equiv = artifact.get('equivalence', {})
    gamma = float(equiv.get('gamma', 0))
    alpha_eff = float(equiv.get('alpha_eff', 0))
    alpha_plus = alpha + Cp * gamma
    rel_err = abs(alpha_eff - alpha_plus) / max(1.0, abs(alpha_eff))
    if rel_err <= 1e-5:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'voltage_table': score_0,
    'optimal_law': score_1,
    'equivalence': score_2,
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
