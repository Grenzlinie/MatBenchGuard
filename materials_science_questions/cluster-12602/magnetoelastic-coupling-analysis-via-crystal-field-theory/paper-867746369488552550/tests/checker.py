import os
import json
import csv

# === author imports / helpers ===
import numpy as np

def quad(func, a, b, limit=200):
    n = max(limit, 500)
    x = np.linspace(a, b, n)
    y = func(x)
    dx = (b - a) / (n - 1)
    val = np.sum((y[:-1] + y[1:]) * 0.5) * dx
    return val, 0.0

def solve(A, b):
    return np.linalg.solve(A, b)


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


# === block: score_0 (check id='check_a_tau') ===
def score_0(artifact, step, ctx):
        a = 85e-6
        chi = 13.1
        h0 = 300e-6
        rho0 = 1.5e-3
        n = 1e10/(2*np.pi)
        mu = 1
        R = 2e-3
        mu0 = 4e-7*np.pi
        H = 1.0
        tol_rel = step.get('tolerance_relative', 1e-5)
        tol_abs = step.get('tolerance_absolute', 1e-12)
        n_rows = len(artifact)
        ok = 0
        for row in artifact:
            q0h0 = float(row['q0h0'])
            q0 = q0h0 / h0
            S = np.sin(q0h0/2)
            D = np.sqrt(h0**2 + 4*rho0**2 * S**2)
            numA = 4*rho0**4 * S**4 - 10*h0**2*rho0**2 * S**2 + h0**4
            A_exp = -8*np.pi*n*a**6 * (chi/(chi+3))**2 * numA / (mu * D) * mu0 * H**2
            tau_exp = -96*np.pi*n*a**6 * (chi/(chi+3))**2 * h0 * rho0**2 * (h0**2 - rho0**2 * S**2) * np.sin(q0h0) / (mu * R**2 * D) * mu0 * H**2
            if np.isclose(float(row['A']), A_exp, rtol=tol_rel, atol=tol_abs) and np.isclose(float(row['tau']), tau_exp, rtol=tol_rel, atol=tol_abs):
                ok += 1
        return ok / n_rows


# === block: score_1 (check id='check_macro_params') ===
def score_1(artifact, step, ctx):
        a = 85e-6
        chi = 13.1
        h0 = 300e-6
        rho0 = 1.5e-3
        n = 1e10/(2*np.pi)
        mu = 1
        R = 2e-3
        mu0 = 4e-7*np.pi
        H = 1.0
        tol_rel = step.get('tolerance_relative', 1e-4)
        tol_abs = step.get('tolerance_absolute', 1e-10)
        n_rows = len(artifact)
        ok = 0
        for row in artifact:
            q0h0 = float(row['q0h0'])
            q0 = q0h0 / h0
            if abs(q0) < 1e-12:
                q0 = 1e-12 if q0>=0 else -1e-12
            S = np.sin(q0*h0/2)
            D = np.sqrt(h0**2 + 4*rho0**2 * S**2)
            term = q0*R - np.arctan(q0*R)
            cosq = np.cos(q0*h0)
            sinq = np.sin(q0*h0)
            # alpha_parallel
            num_par = mu0 * (chi+3)**2 * term * D
            den1 = 4*np.pi*n*chi*a**3 * term * ((chi+3)*D + 4*chi*a**3*(h0**2 - rho0**2 + rho0**2*cosq))
            den2 = 3*chi*a**3*rho0*h0*sinq * ((q0*R)**2 - np.log(1+(q0*R)**2))
            apar = num_par / (den1 + den2)
            # alpha_perp
            den_perp = 4*np.pi*n*chi*a**3 * term * ((chi+3)*D + 4*chi*a**3*(h0**2 - rho0**2 + rho0**2*cosq)) - 3*chi*a**3*rho0*h0*sinq*np.log(1+(q0*R)**2)
            aperp = mu0 * (chi+3)**2 * term * D / den_perp
            # mesoscopic coefficients
            A_meso = 24*np.pi*n*a**6 * (chi/(chi+3))**2 * mu0 * (4*rho0**4*S**4 - 10*h0**2*rho0**2*S**2 + h0**4) / D
            tau_meso = 48*np.pi*n*a**6 * (chi/(chi+3))**2 * mu0 * h0*rho0**2 * (h0**2 - rho0**2*S**2) * sinq / D
            M_A_meso = 36*np.pi*n*a**6 * (chi/(chi+3))**2 * h0*rho0 * (8*rho0**2*S**2 - 3*h0**2) / D * sinq
            M_tau_meso = 12*np.pi*n*a**6 * (chi/(chi+3))**2 * h0**2*rho0 * (2*h0**2*cosq - rho0**2*(9*np.sin(q0*h0/2)+np.sin(3*q0*h0/2))) / D
            # integrals for macroscopic energy A-term, tau-term, M_phi A-term, tau-term
            # define integrands
            def int_fA_basis(r, coeff):
                if coeff==0:
                    return ( (apar-aperp)/(apar*aperp) * 3*q0**2*r**2/(1+q0**2*r**2)**2 ) * r
                elif coeff==1:
                    return - (1/(apar**2)) * (1 - 0.5*q0**2*r**2) / (1+q0**2*r**2)**2 * r
                elif coeff==3:
                    return ( - ((aperp**2 - apar**2)/(apar**2*aperp**2)) * (1-0.5*q0**2*r**2)/(1+q0**2*r**2)**2 - (1/aperp**2)*(1-0.5*q0**2*r**2)/(1+q0**2*r**2) ) * r
                elif coeff==4:
                    t1 = - (2*(aperp-apar)/(apar**2*aperp)) * (1-0.5*q0**2*r**2)/(1+q0**2*r**2)**2
                    t2 = - (2/(apar*aperp)) / (1+q0**2*r**2)
                    return (t1 + t2) * r
                elif coeff==6:
                    t1 = - ((aperp-apar)**2/(apar**2*aperp**2))*(1-0.5*q0**2*r**2)/(1+q0**2*r**2)**2
                    t2 = - 2*(apar*(aperp-apar))/(apar**2*aperp**2) / (1+q0**2*r**2)
                    t3 = - 1/aperp**2
                    return (t1 + t2 + t3) * r
                else:
                    return 0.0
            def int_ftau_basis(r, coeff):
                if coeff==0:
                    return ( (apar-aperp)/(apar*aperp) * q0**2*r**2/(1+q0**2*r**2)**2 ) * r
                elif coeff==1:
                    return 0.5/apar**2 * q0**2*r**2/(1+q0**2*r**2)**2 * r
                elif coeff==3:
                    return (0.5*(aperp**2-apar**2)/(apar**2*aperp**2) * q0**2*r**2/(1+q0**2*r**2)**2 + 0.5/aperp**2 * q0**2*r**2/(1+q0**2*r**2)) * r
                elif coeff==4:
                    return ( (aperp-apar)/(apar**2*aperp) * q0**2*r**2/(1+q0**2*r**2)**2 + 0.5/(apar*aperp) * q0**2*r**2/(1+q0**2*r**2) ) * r
                elif coeff==6:
                    return ( 0.5*(aperp-apar)**2/(apar**2*aperp**2) * q0**2*r**2/(1+q0**2*r**2)**2 + 0.5*apar*(aperp-apar)/(apar**2*aperp**2) * q0**2*r**2/(1+q0**2*r**2) ) * r
                else:
                    return 0.0
            def int_mA_basis(r, coeff):
                if coeff==0:
                    return ( (apar-aperp)/(apar*aperp) * 1.5 * q0*r * (1 - q0**2*r**2) / (1+q0**2*r**2)**2 ) * r
                elif coeff==1:
                    return (1/apar**2) * q0*r * (1 - 0.5*q0**2*r**2) / (1+q0**2*r**2)**2 * r
                elif coeff==3:
                    return ( (aperp**2-apar**2)/(apar**2*aperp**2) * q0*r * (1-0.5*q0**2*r**2)/(1+q0**2*r**2)**2 ) * r
                elif coeff==4:
                    t1 = (2*aperp*(aperp-apar)/(apar**2*aperp**2)) * q0*r * (1-0.5*q0**2*r**2)/(1+q0**2*r**2)**2
                    t2 = 0.5/(apar*aperp) * q0*r/(1+q0**2*r**2)
                    return (t1 + t2) * r
                elif coeff==6:
                    t1 = ( (aperp-apar)**2/(apar**2*aperp**2) ) * q0*r * (1-0.5*q0**2*r**2)/(1+q0**2*r**2)**2
                    t2 = 0.5/(apar*aperp) * q0*r/(1+q0**2*r**2)
                    t3 = -0.5/aperp**2 * q0*r/(1+q0**2*r**2)
                    return (t1 + t2 + t3) * r
                else:
                    return 0.0
            def int_mt_basis(r, coeff):
                if coeff==0:
                    return ( (aperp-apar)/(apar*aperp) * q0*r * (1 - q0**2*r**2) / (1+q0**2*r**2)**2 ) * r
                elif coeff==1:
                    return (1/apar**2) * q0**3 * r**3 / (1+q0**2*r**2)**2 * r
                elif coeff==3:
                    return ( (aperp**2-apar**2)/(apar**2*aperp**2) * q0**3 * r**3 / (1+q0**2*r**2)**2 ) * r
                elif coeff==4:
                    t1 = (2*aperp*(aperp-apar)/(apar**2*aperp**2))*q0**3*r**3/(1+q0**2*r**2)**2
                    t2 = 0.5/(apar*aperp) * q0*r
                    return (t1 + t2)*r
                elif coeff==6:
                    t1 = ((aperp-apar)**2/(apar**2*aperp**2))*q0**3*r**3/(1+q0**2*r**2)**2
                    t2 = 0.5/(apar*aperp) * q0*r
                    return (t1 + t2)*r
                else:
                    return 0.0
            # integrate basis functions
            coeffs_basis = [0,1,3,4,6]
            # energy A term
            IA = {c: quad(lambda r, c=c: int_fA_basis(r,c), 0, R, limit=200)[0] for c in coeffs_basis}
            # energy tau term
            Itau = {c: quad(lambda r, c=c: int_ftau_basis(r,c), 0, R, limit=200)[0] for c in coeffs_basis}
            # M_phi A term
            ImA = {c: quad(lambda r, c=c: int_mA_basis(r,c), 0, R, limit=200)[0] for c in coeffs_basis}
            # M_phi tau term
            Imt = {c: quad(lambda r, c=c: int_mt_basis(r,c), 0, R, limit=200)[0] for c in coeffs_basis}
            # build linear system: A_mat * [z1,z3,z4,z6] = b_vec
            # equation 1: energy A: (mu0**2 / R**2) * (IA[0] + sum_i IA_i * z_i) = A_meso
            #   => sum_i IA_i * z_i = (A_meso * R**2 / mu0**2) - IA[0]
            R_sq = R**2
            fac = R_sq / mu0**2
            b1 = A_meso * fac - IA[0]
            A1 = [IA[1], IA[3], IA[4], IA[6]]
            # equation 2: energy tau: - (mu0**2 / R**2) * (1/q0) * (Itau[0] + sum_i Itau_i * z_i) = tau_meso
            #   => sum_i Itau_i * z_i = -(tau_meso * fac_neg) - Itau[0], where fac_neg = -R_sq/q0/mu0**2? Actually tau_meso = - mu0**2 * (2/R**2) * (1/q0) * sum ... so sum_i Itau_i z_i = - (tau_meso * R**2 * q0 / mu0**2) - Itau[0]
            fac2 = -R_sq * q0 / mu0**2
            b2 = tau_meso * fac2 - Itau[0]
            A2 = [Itau[1], Itau[3], Itau[4], Itau[6]]
            # equation 3: M_phi A: (2/R**2) * mu0 * (ImA[0] + sum ... ) = M_A_meso
            #   => sum_i ImA_i z_i = (M_A_meso * 0.5 * R**2 / mu0) - ImA[0]
            fac3 = 0.5 * R_sq / mu0
            b3 = M_A_meso * fac3 - ImA[0]
            A3 = [ImA[1], ImA[3], ImA[4], ImA[6]]
            # equation 4: M_phi tau: (2/R**2) * mu0 * (1/q0) * (Imt[0] + sum ... ) = M_tau_meso
            #   => sum_i Imt_i z_i = (M_tau_meso * 0.5 * R**2 * q0 / mu0) - Imt[0]
            fac4 = 0.5 * R_sq * q0 / mu0
            b4 = M_tau_meso * fac4 - Imt[0]
            A4 = [Imt[1], Imt[3], Imt[4], Imt[6]]
            A_mat = np.array([A1, A2, A3, A4])
            b_vec = np.array([b1, b2, b3, b4])
            sol = solve(A_mat, b_vec)
            z1_sol, z3_sol, z4_sol, z6_sol = sol
            # compare with agent's row
            row_ok = True
            for key, val in zip(['alpha_parallel','alpha_perp','zeta1','zeta3','zeta4','zeta6'],
                               [apar, aperp, z1_sol, z3_sol, z4_sol, z6_sol]):
                if not np.isclose(float(row[key]), val, rtol=tol_rel, atol=tol_abs):
                    row_ok = False
                    break
            if row_ok:
                ok += 1
        return ok / n_rows


_SCORERS = {
    'check_a_tau': score_0,
    'check_macro_params': score_1,
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
