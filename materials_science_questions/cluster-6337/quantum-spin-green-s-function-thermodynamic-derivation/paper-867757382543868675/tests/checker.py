import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import solve_ivp

def compute_coeffs(alpha, D, mu=0.9, tau=1.0):
    xi = 1 / (1 + alpha**2)
    A1 = (- D**2 * tau * (6 * mu**2 * alpha**2 - 1) * xi**4
          + 2 * mu**2 * alpha * D * tau * xi**3
          - D * (mu**2 * alpha**2 - 2) * xi**2
          + mu**2 * alpha * xi)
    A2 = (0.5 * mu * alpha * D**2 * tau * (11 - 3 * mu**2 * alpha**2) * xi**4
          + mu * D * tau * (mu**2 * alpha**2 - 1) * xi**3
          + 3 * mu * D * alpha * xi**2
          - mu * xi)
    A3 = (D**2 * tau * (3 * mu**2 * alpha**2 + 1) * xi**4
          - 4 * mu**2 * alpha * D * tau * xi**3
          + 2 * D * xi**2)
    return A1, A2, A3

def compute_tau_c(alpha, D, mu=0.9):
    num = mu**2 * (alpha**3 - D * alpha**2 + alpha) + 2 * D
    den = 2 * D * mu**2 * (alpha**3 - 3 * D * alpha**2 + alpha) + D**2
    if den == 0:
        return np.nan
    return - num * (1 + alpha**2)**2 / den

def compute_C12_gold(mu, alpha, D, tau, s_vals, C0=1.0):
    A1, A2, A3 = compute_coeffs(alpha, D, mu, tau)
    G = np.array([[-A1,  A2,  0],
                  [-A2, -A1,  0],
                  [ 0,   0, -A3]])
    xi = 1 / (1 + alpha**2)
    # Linear coefficient L_{i,j,k}: Λ_{ij} = Σ_k L_{i,j,k} ψ_k
    L = np.zeros((3, 3, 3))
    L[0,0,2] = xi * alpha * mu
    L[0,1,2] = xi
    L[0,2,0] = -xi * alpha * mu
    L[0,2,1] = -xi
    L[1,0,2] = -xi
    L[1,1,2] = xi * alpha * mu
    L[1,2,0] = xi
    L[1,2,1] = -xi * alpha * mu
    L[2,0,1] = xi
    L[2,1,0] = -xi
    # T_{i,j,a,b} = Σ_k L_{i,k,a} * L_{j,k,b}
    T = np.zeros((3, 3, 3, 3))
    for i in range(3):
        for j in range(3):
            for a in range(3):
                for b in range(3):
                    s = 0.0
                    for k in range(3):
                        s += L[i,k,a] * L[j,k,b]
                    T[i,j,a,b] = s
    def rhs(s, y):
        C = np.reshape(y, (3, 3))
        dC1 = G @ C
        factor = D * np.exp(-s / tau)
        dC2 = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                sum_ab = 0.0
                for a in range(3):
                    for b in range(3):
                        sum_ab += T[i,j,a,b] * C[a,b]
                dC2[i,j] = factor * sum_ab
        dC = dC1 + dC2
        return dC.flatten()
    C0_mat = np.ones((3, 3)) * C0
    y0 = C0_mat.flatten()
    sol = solve_ivp(rhs, [0.0, s_vals[-1] + 1e-9], y0,
                    t_eval=s_vals, method='DOP853',
                    atol=1e-10, rtol=1e-10)
    # C12 corresponds to row=0, col=1, flatten index 1
    C12 = sol.y[1, :]
    return s_vals, C12


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


# === block: score_0 (check id='stability_coeffs') ===
def score_0(artifact, step, ctx):
    tolerance_atol = 1e-8
    tolerance_rtol = 1e-5
    total_rows = len(artifact)
    if total_rows == 0:
        return 0.0
    passed = 0
    for row in artifact:
        try:
            alpha = float(row['alpha'])
            D = float(row['D'])
        except (KeyError, ValueError):
            continue
        A1_exp, A2_exp, A3_exp = compute_coeffs(alpha, D, mu=0.9, tau=1.0)
        tau_c_exp = compute_tau_c(alpha, D, mu=0.9)
        ok = True
        for field, exp_val in [('A1', A1_exp), ('A2', A2_exp), ('A3', A3_exp)]:
            try:
                agent_val = float(row[field])
            except (KeyError, ValueError):
                ok = False
                break
            if not (np.isfinite(agent_val) and np.isfinite(exp_val)):
                ok = False
                break
            diff = abs(agent_val - exp_val)
            if diff > tolerance_atol + tolerance_rtol * abs(exp_val):
                ok = False
                break
        if ok:
            try:
                agent_tau = row.get('tau_c', '')
                if agent_tau == '':
                    agent_tau_val = np.nan
                else:
                    agent_tau_val = float(agent_tau)
            except (ValueError, KeyError):
                agent_tau_val = np.nan
            if np.isnan(agent_tau_val) and np.isnan(tau_c_exp):
                pass
            elif np.isnan(agent_tau_val) or np.isnan(tau_c_exp):
                ok = False
            else:
                if abs(agent_tau_val - tau_c_exp) > tolerance_atol + tolerance_rtol * abs(tau_c_exp):
                    ok = False
        if ok:
            passed += 1
    return passed / total_rows


# === block: score_1 (check id='correlation_C12') ===
def score_1(artifact, step, ctx):
    try:
        s_vals = np.array([float(row['s']) for row in artifact])
        C12_agent = np.array([float(row['C12']) for row in artifact])
    except (KeyError, ValueError):
        return 0.0
    if len(s_vals) < 10:
        return 0.0
    mu = 0.9
    alpha = 0.005
    D = 0.1
    tau = 1.0
    s_gold, C12_gold = compute_C12_gold(mu, alpha, D, tau, s_vals, C0=1.0)
    rtol = 1e-4
    atol = 1e-6
    diff = np.abs(C12_agent - C12_gold)
    passed = np.sum(diff <= atol + rtol * np.abs(C12_gold))
    return passed / len(s_vals)


_SCORERS = {
    'stability_coeffs': score_0,
    'correlation_C12': score_1,
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
