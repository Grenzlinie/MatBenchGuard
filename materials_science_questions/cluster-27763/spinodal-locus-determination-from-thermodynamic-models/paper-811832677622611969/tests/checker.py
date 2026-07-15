import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve

PARAM_SETS = {
    "p1": {"label": "Lambda=350, eta_c=-0.05, eta_cc=0.04", "Lambda": 350.0, "eta_c": -0.05, "eta_cc": 0.04},
    "p2": {"label": "Lambda=100, eta_c=-0.05, eta_cc=0.04", "Lambda": 100.0, "eta_c": -0.05, "eta_cc": 0.04},
    "p3": {"label": "Lambda=100, eta_c=-0.03, eta_cc=0", "Lambda": 100.0, "eta_c": -0.03, "eta_cc": 0.0},
    "p4": {"label": "Lambda=100, eta_c=-0.01, eta_cc=-0.04", "Lambda": 100.0, "eta_c": -0.01, "eta_cc": -0.04},
}

def get_params(param_set_str):
    s = str(param_set_str)
    if "Lambda=350" in s or "Λ=350" in s or "Lambda = 350" in s:
        return PARAM_SETS["p1"]
    if "Lambda=100" in s or "Λ=100" in s or "Lambda = 100" in s:
        if "eta_c=-0.05" in s or "η_c=-0.05" in s:
            return PARAM_SETS["p2"]
        if "eta_c=-0.03" in s or "η_c=-0.03" in s:
            return PARAM_SETS["p3"]
        if "eta_c=-0.01" in s or "η_c=-0.01" in s:
            return PARAM_SETS["p4"]
    raise ValueError("Unknown param_set: " + s)

def epsilon(c, eta_c, eta_cc):
    return eta_c * c + 0.5 * eta_cc * c**2

def d_epsilon(c, eta_c, eta_cc):
    return eta_c + eta_cc * c

def phi(t, c, Pi, params):
    Lam = params["Lambda"]
    ec = epsilon(c, params["eta_c"], params["eta_cc"])
    return t * (c * np.log(c) + (1-c) * np.log(1-c)) + 2*c*(1-c) - 4.5 * Pi**2 + 3 * np.sqrt(Lam) * ec * Pi

def dphi_dc(t, c, Pi, params):
    Lam = params["Lambda"]
    dec = d_epsilon(c, params["eta_c"], params["eta_cc"])
    return t * np.log(c/(1-c)) + 2*(1-2*c) + 3 * np.sqrt(Lam) * dec * Pi

def dphi_dPi(t, c, Pi, params):
    Lam = params["Lambda"]
    ec = epsilon(c, params["eta_c"], params["eta_cc"])
    return -9 * Pi + 3 * np.sqrt(Lam) * ec

def grand_omega(t, c, Pi, params):
    return phi(t, c, Pi, params) - c * dphi_dc(t, c, Pi, params) - Pi * dphi_dPi(t, c, Pi, params)

def equations_alpha(x, t, P_o, params):
    c_a, c_b, P_b = x[0], x[1], x[2]
    eq1 = dphi_dc(t, c_a, P_o, params) - dphi_dc(t, c_b, P_b, params)
    eq2 = dphi_dPi(t, c_a, P_o, params) - dphi_dPi(t, c_b, P_b, params)
    eq3 = grand_omega(t, c_a, P_o, params) - grand_omega(t, c_b, P_b, params)
    return [eq1, eq2, eq3]

def solve_alpha_boundary(t, P_o, params):
    guess = [0.3, 0.7, P_o]
    sol = fsolve(lambda x: equations_alpha(x, t, P_o, params), guess, xtol=1e-8, maxfev=1000)
    c_a, c_b, P_b = sol
    return c_a, c_b, P_o, P_b

def equations_beta(x, t, P_o, params):
    c_a, c_b, P_a = x[0], x[1], x[2]
    eq1 = dphi_dc(t, c_a, P_a, params) - dphi_dc(t, c_b, P_o, params)
    eq2 = dphi_dPi(t, c_a, P_a, params) - dphi_dPi(t, c_b, P_o, params)
    eq3 = grand_omega(t, c_a, P_a, params) - grand_omega(t, c_b, P_o, params)
    return [eq1, eq2, eq3]

def solve_beta_boundary(t, P_o, params):
    guess = [0.3, 0.7, P_o]
    sol = fsolve(lambda x: equations_beta(x, t, P_o, params), guess, xtol=1e-8, maxfev=1000)
    c_a, c_b, P_a = sol
    return c_a, c_b, P_a, P_o

def spinodal_residual(t, c, Pi, params):
    Lam = params["Lambda"]
    dec = d_epsilon(c, params["eta_c"], params["eta_cc"])
    rhs = c*(1-c) * (4.0 - Lam * dec**2 - 3.0 * params["eta_cc"] * np.sqrt(Lam) * Pi)
    return t - rhs

def find_spinodal_roots(t, Pi, params):
    roots = set()
    for guess in [0.2, 0.5, 0.8]:
        try:
            sol = fsolve(lambda c: spinodal_residual(t, float(c), Pi, params), guess, xtol=1e-8)
            root = sol[0]
            if 0.001 < root < 0.999 and not any(np.abs(root - r) < 1e-4 for r in roots):
                roots.add(root)
        except:
            pass
    return sorted(roots)

def check_critical(t_c, c_c, P_o_c, params):
    if params["eta_cc"] == 0.0:
        ok_c = np.abs(c_c - 0.5) < 0.02
        t_expected = 1 - params["Lambda"] * params["eta_c"]**2 / 4.0
        ok_t = np.abs(t_c - t_expected) < 0.02
        return ok_c and ok_t
    else:
        res1 = np.abs(spinodal_residual(t_c, c_c, P_o_c, params))
        Lam = params["Lambda"]
        dec = d_epsilon(c_c, params["eta_c"], params["eta_cc"])
        rhs_t = (c_c*(1-c_c))**2 / (1 - 2*c_c) * 3 * Lam * params["eta_cc"] * dec
        res2 = np.abs(t_c - rhs_t)
        return res1 < 0.005 and res2 < 0.005


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


# === block: score_0 (check id='phase_boundary_data') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list):
            return 0.0
        tol_comp = 0.01
        tol_P = 0.01
        tol_z = 0.01
        total_rows = 0
        correct_rows = 0
        for row in artifact:
            try:
                param_str = str(row.get("param_set", "")).strip()
                slice_type = str(row.get("slice_type", "")).strip()
                t = float(row["t"])
                P_o = float(row["P_o"])
                c_alpha = float(row["c_alpha"])
                c_beta = float(row["c_beta"])
                P_alpha = float(row["P_alpha"])
                P_beta = float(row["P_beta"])
                z = float(row["z"])
            except (KeyError, ValueError):
                continue
            total_rows += 1
            # Validate slice conditions
            if slice_type == "t_c":
                if abs(P_o - 0.1) > 0.01:
                    continue
                fixed_Pi = 0.1
            elif slice_type == "c_P":
                if abs(t - 0.8) > 0.01:
                    continue
                fixed_t = 0.8
            else:
                continue
            try:
                params = get_params(param_str)
            except:
                continue
            # Determine boundary by z value
            if abs(z) < tol_z:
                # alpha boundary
                try:
                    if slice_type == "t_c":
                        c_a_exp, c_b_exp, P_a_exp, P_b_exp = solve_alpha_boundary(t, fixed_Pi, params)
                    else:
                        c_a_exp, c_b_exp, P_a_exp, P_b_exp = solve_alpha_boundary(fixed_t, P_o, params)
                    if (abs(c_alpha - c_a_exp) <= tol_comp and
                        abs(c_beta - c_b_exp) <= tol_comp and
                        abs(P_alpha - P_a_exp) <= tol_P and
                        abs(P_beta - P_b_exp) <= tol_P):
                        correct_rows += 1
                except:
                    pass
            elif abs(z - 1.0) < tol_z:
                # beta boundary
                try:
                    if slice_type == "t_c":
                        c_a_exp, c_b_exp, P_a_exp, P_b_exp = solve_beta_boundary(t, fixed_Pi, params)
                    else:
                        c_a_exp, c_b_exp, P_a_exp, P_b_exp = solve_beta_boundary(fixed_t, P_o, params)
                    if (abs(c_alpha - c_a_exp) <= tol_comp and
                        abs(c_beta - c_b_exp) <= tol_comp and
                        abs(P_alpha - P_a_exp) <= tol_P and
                        abs(P_beta - P_b_exp) <= tol_P):
                        correct_rows += 1
                except:
                    pass
            # else z not near 0 or 1; ignore as it may not be a boundary row
        if total_rows == 0:
            return 0.0
        return correct_rows / total_rows


# === block: score_1 (check id='spinodal_data') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list):
            return 0.0
        tol_c = 0.01
        total_rows = 0
        correct_rows = 0
        for row in artifact:
            try:
                param_str = str(row.get("param_set", "")).strip()
                slice_type = str(row.get("slice_type", "")).strip()
                t = float(row["t"])
                P_o = float(row["P_o"])
                c_sp_raw = float(row["c_spinodal"])
            except:
                continue
            total_rows += 1
            try:
                params = get_params(param_str)
            except:
                continue
            if slice_type == "t_c":
                if abs(P_o - 0.1) > 0.01:
                    continue
                Pi_fixed = 0.1
                t_val = t
            elif slice_type == "c_P":
                if abs(t - 0.8) > 0.01:
                    continue
                t_val = 0.8
                Pi_fixed = P_o
            else:
                continue
            try:
                roots = find_spinodal_roots(t_val, Pi_fixed, params)
            except:
                roots = []
            matched = any(abs(c_sp_raw - r) <= tol_c for r in roots)
            if matched:
                correct_rows += 1
        if total_rows == 0:
            return 0.0
        return correct_rows / total_rows


# === block: score_2 (check id='critical_points') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list):
            return 0.0
        total = 0
        correct = 0
        for row in artifact:
            try:
                param_str = str(row.get("param_set", "")).strip()
                t_c = float(row["t_c"])
                c_c = float(row["c_c"])
                P_o_c = float(row["P_o_c"])
            except:
                continue
            try:
                params = get_params(param_str)
            except:
                continue
            if check_critical(t_c, c_c, P_o_c, params):
                correct += 1
            total += 1
        if total == 0:
            return 0.0
        return correct / total


_SCORERS = {
    'phase_boundary_data': score_0,
    'spinodal_data': score_1,
    'critical_points': score_2,
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
