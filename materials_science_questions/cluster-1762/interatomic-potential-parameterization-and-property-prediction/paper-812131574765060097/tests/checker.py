import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve
import json
import os


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
    def prepare(outputs_dir, spec):
        # --- constants in cgs units ---
        l = 2e-8  # 2 Å in cm
        e = 4.80320425e-10  # esu
        n_eff = 2.06
        ne = n_eff * e

        s = 9
        t = 6

        # overlap coefficients (cgs, from Eq.10)
        lam_OT = 15.6e-82
        lam_OO = 113.5e-82
        lam_BO = 99.0e-82
        lam_BB = 82.7e-82
        lam_BT = 12e-82
        lam_TT = 1.1e-82

        # van der Waals coefficients (cgs)
        mu_OT = 31.3e-60
        mu_OO = 135.0e-60
        mu_BO = 162.0e-60
        mu_BB = 239.0e-60
        mu_BT = 43e-60
        mu_TT = 10e-60

        # dipolar field sums
        p = 8.668
        q = 30.081

        # polarizabilities (from Anderson & Shockley)
        alpha_Ti = 0.0365/(4*np.pi) * (2*l)**3
        alpha_Ba = 0.382/(4*np.pi) * (2*l)**3
        alpha_O  = 0.470/(4*np.pi) * (2*l)**3

        # dipole coefficient a0'
        a0_prime = 0.1974 * ne**2 / (2 * alpha_Ti)
        sens = 7.30

        # helper: a and b functions (Eqs.22,23)
        def a_coeff(Da, Db1, Db2):
            val = (lam_OT * s*(s+1) * (l*(1+Da))**(-s-2)
                   - mu_OT * t*(t+1) * (l*(1+Da))**(-t-2)
                   - lam_OT * s * (l*(1+Db1))**(-s-2)
                   + mu_OT * t * (l*(1+Db1))**(-t-2)
                   - lam_OT * s * (l*(1+Db2))**(-s-2)
                   + mu_OT * t * (l*(1+Db2))**(-t-2)
                   + lam_BT * (4*s*(s-1)/3) * (np.sqrt(3)*l)**(-s-2)
                   - mu_BT * (4*t*(t-1)/3) * (np.sqrt(3)*l)**(-t-2))
            return val

        def b_coeff(Da, Db1, Db2):
            term_BT_s = (s*(s+2) - 2*s*(s+2)*(s+4)/3 + s*(s+2)*(s+4)*(s+6)/27) * (np.sqrt(3)*l)**(-s-4)
            term_BT_t = (t*(t+2) - 2*t*(t+2)*(t+4)/3 + t*(t+2)*(t+4)*(t+6)/27) * (np.sqrt(3)*l)**(-t-4)
            val = (lam_OT * s*(s+1)*(s+2)*(s+3)/12 * (l*(1+Da))**(-s-4)
                   - mu_OT * t*(t+1)*(t+2)*(t+3)/12 * (l*(1+Da))**(-t-4)
                   + lam_OT * s*(s+2)/4 * (l*(1+Db1))**(-s-4)
                   - mu_OT * t*(t+2)/4 * (l*(1+Db1))**(-t-4)
                   + lam_OT * s*(s+2)/4 * (l*(1+Db2))**(-s-4)
                   - mu_OT * t*(t+2)/4 * (l*(1+Db2))**(-t-4)
                   + lam_BT * term_BT_s - mu_BT * term_BT_t)
            return val

        # energy derivatives (Eqs.11,13)
        def dU1_dDa(Da, Db1, Db2):
            term = (-2*s*lam_OT * l**(-s) * (1 - (s+1)*Da)
                    + 2*t*mu_OT * l**(-t) * (1 - (t+1)*Da)
                    - s*(4*lam_OO + 4*lam_BO) * l**(-s) * 2**(-s/2) * (1 - s/2*Da - (s+2)/4*(Db1+Db2))
                    + t*(4*mu_OO + 4*mu_BO) * l**(-t) * 2**(-t/2) * (1 - t/2*Da - (t+2)/4*(Db1+Db2))
                    - 8*s*lam_BT * l**(-s) * 3**(-(s+2)/2) * (1 - (s-1)/3*Da - (s+2)/3*(Db1+Db2))
                    + 8*t*mu_BT * l**(-t) * 3**(-(t+2)/2) * (1 - (t-1)/3*Da - (t+2)/3*(Db1+Db2))
                    - s*(3*lam_OO + lam_BB + lam_TT) * (2*l)**(-s) * (1 - (s+1)*Da)
                    + t*(3*mu_OO + mu_BB + mu_TT) * (2*l)**(-t) * (1 - (t+1)*Da))
            return term

        def dU1_dDb(Db, Da, other_Db):
            # derivative w.r.t. one of the perpendicular directions
            term = (-2*s*lam_OT * l**(-s) * (1 - (s+1)*Db)
                    + 2*t*mu_OT * l**(-t) * (1 - (t+1)*Db)
                    - s*(4*lam_OO + 4*lam_BO) * l**(-s) * 2**(-s/2) * (1 - s/2*Db - (s+2)/4*(other_Db + Da))
                    + t*(4*mu_OO + 4*mu_BO) * l**(-t) * 2**(-t/2) * (1 - t/2*Db - (t+2)/4*(other_Db + Da))
                    - 8*s*lam_BT * l**(-s) * 3**(-(s+2)/2) * (1 - (s-1)/3*Db - (s+2)/3*(other_Db + Da))
                    + 8*t*mu_BT * l**(-t) * 3**(-(t+2)/2) * (1 - (t-1)/3*Db - (t+2)/3*(other_Db + Da))
                    - s*(3*lam_OO + lam_BB + lam_TT) * (2*l)**(-s) * (1 - (s+1)*Db)
                    + t*(3*mu_OO + mu_BB + mu_TT) * (2*l)**(-t) * (1 - (t+1)*Db))
            return term

        def dUC_dDa(Da):
            return (49.1 * e**2) / (6*l) * (1 - 2*Da)

        def dUC_dDb(Db):
            return (49.1 * e**2) / (6*l) * (1 - 2*Db)

        # finite-difference derivatives of a and b
        eps = 1e-8
        def da_dDa_fd(Da, Db):
            return (a_coeff(Da+eps, Db, Db) - a_coeff(Da-eps, Db, Db)) / (2*eps)
        def da_dDb_total_fd(Da, Db):
            return (a_coeff(Da, Db+eps, Db) + a_coeff(Da, Db, Db+eps) - a_coeff(Da, Db, Db) - a_coeff(Da, Db, Db)) / eps  # sum over Db1,Db2
        def db_dDa_fd(Da, Db):
            return (b_coeff(Da+eps, Db, Db) - b_coeff(Da-eps, Db, Db)) / (2*eps)
        def db_dDb_total_fd(Da, Db):
            return (b_coeff(Da, Db+eps, Db) + b_coeff(Da, Db, Db+eps) - b_coeff(Da, Db, Db) - b_coeff(Da, Db, Db)) / eps

        # equilibrium equations
        def eq_system(vars):
            Da, Db = vars
            # a and b at current point
            a_val = a_coeff(Da, Db, Db)
            b_val = b_coeff(Da, Db, Db)
            if b_val < 1e-20:
                b_val = 1e-20
            a_p = a0_prime * (1 - sens * Da)
            sum_a = a_p + a_val
            # derivatives of a'
            da_p_dDa = a0_prime * (-sens)
            # equilibrium for Da
            gA = (dU1_dDa(Da, Db, Db) + dUC_dDa(Da)
                  - sum_a/(2*b_val) * (da_p_dDa + da_dDa_fd(Da, Db))
                  + sum_a**2/(4*b_val**2) * db_dDa_fd(Da, Db))
            # equilibrium for Db
            dU1_dDb_sum = dU1_dDb(Db, Da, Db) + dU1_dDb(Db, Db, Da)
            dUC_dDb_sum = 2 * dUC_dDb(Db)
            gB = (dU1_dDb_sum + dUC_dDb_sum
                  - sum_a/(2*b_val) * da_dDb_total_fd(Da, Db)
                  + sum_a**2/(4*b_val**2) * db_dDb_total_fd(Da, Db))
            return [gA, gB]

        # initial guess from approximate results
        try:
            sol = fsolve(eq_system, [0.012, 0.005], maxfev=2000, xtol=1e-12)
            Da_sol, Db_sol = sol
            a_sol = a_coeff(Da_sol, Db_sol, Db_sol)
            b_sol = b_coeff(Da_sol, Db_sol, Db_sol)
            a_p_sol = a0_prime * (1 - sens * Da_sol)
            if a_p_sol + a_sol < 0:
                ti_sol = np.sqrt(-(a_p_sol + a_sol) / (2*b_sol))
            else:
                ti_sol = 0.0
        except Exception as e:
            # fallback: set zeros
            Da_sol, Db_sol, ti_sol = 0.0, 0.0, 0.0

        return {
            'gold_delta_a': Da_sol,
            'gold_delta_b': Db_sol,
            'gold_ti_shift': ti_sol,
            'tol_delta_a': 0.002,
            'tol_delta_b': 0.002,
            'tol_ti_shift': 0.01
        }


# === block: score_0 (check id='step5_solve_deformation') ===
def score_0(artifact, step, ctx):
        # safe conversion helper
        def _to_float(v):
            try:
                return float(v)
            except (TypeError, ValueError):
                return None
        if not isinstance(artifact, dict):
            return 0.0
        da = _to_float(artifact.get('delta_a'))
        db = _to_float(artifact.get('delta_b'))
        ts = _to_float(artifact.get('ti_shift'))
        if da is None or db is None or ts is None:
            return 0.0
        gold_da = _to_float(ctx.get('gold_delta_a'))
        gold_db = _to_float(ctx.get('gold_delta_b'))
        gold_ts = _to_float(ctx.get('gold_ti_shift'))
        tol_da = _to_float(ctx.get('tol_delta_a'))
        tol_db = _to_float(ctx.get('tol_delta_b'))
        tol_ts = _to_float(ctx.get('tol_ti_shift'))
        if any(v is None for v in (gold_da, gold_db, gold_ts, tol_da, tol_db, tol_ts)):
            return 0.0
        da_ok = abs(da - gold_da) <= tol_da
        db_ok = abs(db - gold_db) <= tol_db
        ts_ok = abs(ts - gold_ts) <= tol_ts
        return 1.0 if (da_ok and db_ok and ts_ok) else 0.0


_SCORERS = {
    'step5_solve_deformation': score_0,
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
