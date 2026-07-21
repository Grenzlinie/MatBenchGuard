import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve

def bulk_magnetization(T):
    if T <= 0:
        return 1.0
    if T >= 12.0:
        return 0.0
    def f(x):
        return x - (24.0 / T) * np.tanh(x)
    # initial guess
    guess = 1.0
    try:
        sol = fsolve(f, guess, maxfev=200)
        x = sol[0]
    except Exception:
        x = 0.0
    return np.tanh(x)

def solve_layer_magnetizations(T, J00=1.645, J01=-1.282, J11=1.0, Jb=1.0):
    Z0 = 6
    Z1 = 3
    eta_bulk = bulk_magnetization(T)
    # use auxiliary variables x_i = arctanh(eta_i) to avoid domain errors
    def eqs(vars):
        x0, x1, x2, x3 = vars
        e0 = np.tanh(x0)
        e1 = np.tanh(x1)
        e2 = np.tanh(x2)
        e3 = np.tanh(x3)
        eq0 = x0 - (Z0 * J00 * e0 + Z1 * J01 * e1) / T
        eq1 = x1 - (Z1 * J01 * e0 + Z0 * J11 * e1 + Z1 * Jb * e2) / T
        eq2 = x2 - (Z1 * Jb * e1 + Z0 * Jb * e2 + Z1 * Jb * e3) / T
        eq3 = x3 - (Z1 * Jb * e2 + Z0 * Jb * e3 + Z1 * Jb * eta_bulk) / T
        return [eq0, eq1, eq2, eq3]
    # initial guess: start from bulk value (arctanh(eta_bulk) if |eta_bulk|<1 else 5.0)
    if abs(eta_bulk) < 0.999:
        x_init = np.arctanh(eta_bulk)
    else:
        x_init = 5.0
    guess = np.array([x_init]*4)
    try:
        sol = fsolve(eqs, guess, maxfev=1000, xtol=1e-12)
    except Exception:
        sol = guess
    return [np.tanh(sol[i]) for i in range(4)]

def compute_T_CS_from_abc(a, b, c):
    coeffs = [b, -(1 - c**2 + 2*a*b + b**2), 2*a*(a*b - c**2)*(a+2*b), -a**2 - (a*b - c)**2]
    roots = np.roots(coeffs)
    real_roots = roots[np.isreal(roots)].real
    tcs_vals = [(r + 2)/4 for r in real_roots]
    if len(tcs_vals) == 0:
        return 1.0
    return max(tcs_vals)


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


# === block: score_0 (check id='critical_classify') ===
def score_0(artifact, step, ctx):
        correct = 0
        total = 0
        for row in artifact:
            try:
                x = float(row["J00_div_J"])
                y = float(row["J11_div_J"])
                z = float(row["J01_div_J"])
            except (ValueError, KeyError):
                continue
            lhs = 6 * (2 - x) * (1 - 2 * y / 3)
            rhs = z * z
            expected = 1 if lhs < rhs else 0
            if int(row["is_critical"]) == expected:
                correct += 1
            total += 1
        if total == 0:
            return 0.0
        return correct / total


# === block: score_1 (check id='tcs_cubic') ===
def score_1(artifact, step, ctx):
        tol = step.get("tolerance", 1e-5)
        total_err = 0.0
        count = 0
        for row in artifact:
            try:
                a = float(row["a"])
                b = float(row["b"])
                c = float(row["c"])
                agent_tcs = float(row["T_CS_div_T_C"])
            except (ValueError, KeyError):
                continue
            ref_tcs = compute_T_CS_from_abc(a, b, c)
            if abs(ref_tcs) < 1e-9:
                ref_tcs = 1e-9
            rel_err = abs(agent_tcs - ref_tcs) / abs(ref_tcs)
            total_err += min(rel_err / tol, 1.0)
            count += 1
        if count == 0:
            return 0.0
        score = 1.0 - total_err / count
        return max(0.0, score)


# === block: score_2 (check id='mag_profile') ===
def score_2(artifact, step, ctx):
        hidden_temps = step.get("hidden_temperatures", [])
        tol = step.get("tolerance", 0.001)
        if not hidden_temps:
            return 0.0
        T_vals = []
        eta0_vals = []
        eta1_vals = []
        eta2_vals = []
        eta_avg3_vals = []
        eta_avg_surf_vals = []
        for row in artifact:
            try:
                T_vals.append(float(row["T_div_T_C"]))
                eta0_vals.append(float(row["eta_0"]))
                eta1_vals.append(float(row["eta_1"]))
                eta2_vals.append(float(row["eta_2"]))
                eta_avg3_vals.append(float(row["eta_avg_3layers"]))
                eta_avg_surf_vals.append(float(row["eta_avg_surface_layer_model"]))
            except:
                continue
        if len(T_vals) == 0:
            return 0.0
        T_vals = np.array(T_vals)
        eta0_arr = np.array(eta0_vals)
        eta1_arr = np.array(eta1_vals)
        eta2_arr = np.array(eta2_vals)
        eta_avg3_arr = np.array(eta_avg3_vals)
        eta_avg_surf_arr = np.array(eta_avg_surf_vals)
        order = np.argsort(T_vals)
        T_vals = T_vals[order]
        eta0_arr = eta0_arr[order]
        eta1_arr = eta1_arr[order]
        eta2_arr = eta2_arr[order]
        eta_avg3_arr = eta_avg3_arr[order]
        eta_avg_surf_arr = eta_avg_surf_arr[order]
        eta_errors = []
        for T_div in hidden_temps:
            T_actual = T_div * 12.0
            try:
                eta0_ref, eta1_ref, eta2_ref, _ = solve_layer_magnetizations(T_actual)
            except:
                continue
            eta0_agent = float(np.interp(T_div, T_vals, eta0_arr))
            eta1_agent = float(np.interp(T_div, T_vals, eta1_arr))
            eta2_agent = float(np.interp(T_div, T_vals, eta2_arr))
            errors = [
                abs(eta0_agent - eta0_ref),
                abs(eta1_agent - eta1_ref),
                abs(eta2_agent - eta2_ref)
            ]
            max_err = max(errors)
            if max_err <= tol:
                eta_errors.append(0.0)
            else:
                eta_errors.append(min(max_err / tol, 1.0))
        if len(eta_errors) == 0:
            eta_score = 0.0
        else:
            eta_score = 1.0 - np.mean(eta_errors)
        avg_errors = []
        for T_div in hidden_temps:
            T_actual = T_div * 12.0
            eta0_agent = float(np.interp(T_div, T_vals, eta0_arr))
            eta1_agent = float(np.interp(T_div, T_vals, eta1_arr))
            eta2_agent = float(np.interp(T_div, T_vals, eta2_arr))
            agent_avg3 = float(np.interp(T_div, T_vals, eta_avg3_arr))
            agent_avg_surf = float(np.interp(T_div, T_vals, eta_avg_surf_arr))
            expected_avg3 = eta0_agent + eta1_agent + eta2_agent
            eta_bulk = bulk_magnetization(T_actual)
            expected_avg_surf = eta0_agent + 2 * eta_bulk
            err_avg3 = abs(agent_avg3 - expected_avg3)
            err_avg_surf = abs(agent_avg_surf - expected_avg_surf)
            avg_errors.append(max(err_avg3, err_avg_surf))
        if len(avg_errors) == 0:
            avg_score = 0.0
        else:
            avg_tol = 1e-4
            avg_score = max(0.0, 1.0 - np.mean(avg_errors) / avg_tol)
        final_score = 0.8 * eta_score + 0.2 * avg_score
        return max(0.0, min(1.0, final_score))


_SCORERS = {
    'critical_classify': score_0,
    'tcs_cubic': score_1,
    'mag_profile': score_2,
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
