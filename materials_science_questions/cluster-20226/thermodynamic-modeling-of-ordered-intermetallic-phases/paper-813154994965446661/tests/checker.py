import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve
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
        V = 1.0
        k = 1.0
        L = 0.1
        Tc = 0.8224 * V / k
        T_high = 0.9 * Tc
        T_low = 0.4 * Tc

        def solve_zeroth(V, T):
            exp1 = np.exp(-6.0 * V / (k * T))
            exp2 = np.exp(-2.0 * V / (k * T))
            def eqs(vars):
                b, g, h, r = vars
                b = max(b, 1e-15)
                g = max(g, 1e-15)
                h = max(h, 1e-15)
                r = max(0.0, min(1.0, r))
                a = b * g * exp1 / h
                c = b * h * exp2 / (g * exp1)
                d = b * h * h / (g * g * exp1)
                e = g**3 * exp1 / (h * h)
                f = g * g * exp2 / h
                # Eq. (2)
                eq2 = 4*a + 9*b + 6*c + d + 3*e + 6*f + 3*g - 1.0
                # Eq. (3)
                eq3 = a + 3*b + 3*c + d + e + 3*f + 3*g + h - 1.0
                # Eq. (4)
                eq4 = a + 2*b + c + e + 2*f + g - (1.0 - r) / 3.0
                # Order condition (Eq. (17) last)
                denom = max(r * (2.0 + r), 1e-30)
                ratio = max(c, 1e-30) / max(f, 1e-30)
                eq9 = ((1.0 - r)**2 / denom) * (ratio ** (4.0/3.0)) - 1.0
                return [eq2, eq3, eq4, eq9]

            if T >= Tc:
                init = [0.01, 0.1, 0.3, 0.001]  # b, g, h, r
            else:
                init = [0.001, 0.9, 0.001, 0.99]
            sol = fsolve(eqs, init, maxfev=2000, xtol=1e-12)
            b, g, h, r = sol
            b = max(b, 1e-15); g = max(g, 1e-15); h = max(h, 1e-15); r = max(0.0, min(1.0, r))
            a = b * g * exp1 / h
            c = b * h * exp2 / (g * exp1)
            d = b * h * h / (g * g * exp1)
            e = g**3 * exp1 / (h * h)
            f = g * g * exp2 / h
            return r, a, b, c, d, e, f, g, h

        def compute_k1k2(r, a, b, c, d, e, f, g, h, V, L, T):
            N = 1.0
            Lp = L
            # auxiliary coefficients from Eqs.(21)-(22)
            x1 = 4*a - 6*c - 2*d + 9*e + 12*f + 3*g
            x2 = 3*b + 4*c + d - 3*e - 4*f - g
            x3 = e + 2*f + g
            x4 = 2*c + d - 2*f - g
            y1 = a - 3*c - 2*d + 3*e + 6*f + 3*g
            y2 = b + 2*c + d - e - 2*f - g
            y3 = e + 3*f + 3*g + h
            y4 = c + d - f - g
            z1 = a - c + 3*e + 4*f + g
            z2 = -b - c - f - g
            z3 = b + c - e - f
            z4 = c - f
            z5 = f + g

            # common denominator
            den = 3*x3*(x1*y2 - x2*y1) + 3*z1*(x2*y3 - 3*x3*y2) + (x3 - 2*z3)*(x1*y3 - 3*x3*y1)
            if abs(den) < 1e-30:
                den = 1e-30
            inv_den = 1.0 / den

            # A
            num_A1 = 3*x3*y4 - x4*y3
            num_A2 = (x2*y3 - 3*x3*y2) * (
                -3*x3*(x1*y4 - x4*y1) + 3*z1*(3*x3*y4 - x4*y3) + (z4 - z5)*(x1*y3 - 3*x3*y1)
            ) * inv_den
            A = (num_A1 - num_A2) / max((x1*y3 - 3*x3*y1), 1e-30)

            # H
            num_H1 = -x1*y4 + x4*y1
            num_H2 = (x1*y2 - x2*y1) * (
                -3*x3*(x1*y4 - x4*y1) + 3*z1*(3*x3*y4 - x4*y3) + (z4 - z5)*(x1*y3 - 3*x3*y1)
            ) * inv_den
            H = (num_H1 - num_H2) / max((x1*y3 - 3*x3*y1), 1e-30)

            # B1
            B1 = -(27.0/2.0) * z4 / max(4.0*(1-r)*(2+r) + 27.0*z2, 1e-30)

            # B2
            term_B2_1 = -(x1*y3 - 3*x3*y1) * (x3*z5 - z3*(z4 + z5))
            term_B2_2 = z2 * (x3*(x1*y4 - x4*y1) - z1*(3*x3*y4 - x4*y3))
            term_B2_3 = -(z4 + 2*z5) * (x3*(x1*y2 - x2*y1) + z1*(x2*y3 - 3*x3*y2))
            num_B2 = term_B2_1 + term_B2_2 + term_B2_3
            B2 = num_B2 / max(z2 * den, 1e-30)

            # B3
            term_B3_1 = -(x1*y3 - 3*x3*y1) * (x3*z4 - 2*z3*z5)
            term_B3_2 = -2*z2 * (x3*(x1*y4 - x4*y1) - z1*(3*x3*y4 - x4*y3))
            term_B3_3 = (z4 + 2*z5) * (x3*(x1*y2 - x2*y1) + z1*(x2*y3 - 3*x3*y2))
            num_B3 = term_B3_1 + term_B3_2 + term_B3_3
            B3 = num_B3 / max(z2 * den, 1e-30)

            # C1, F1
            C1 = 0.5 - B1
            F1 = 0.5 + B1

            # D, E
            D = 1.0 - 2*A - B2 + B3
            E_coef = 3*A + B2 - B3 + H

            # G2
            G2 = 1.0 - A - B2 - H
            # G3
            G3 = 2*A - B3 + 2*H

            # k1 and k2 (Eq.24)
            k1 = 2.0 * (c*C1 + f*F1) * N * L * Lp / (k * T)
            k2 = 2.0 * (b*(3*B2 + B3) + d*D + e*E_coef + g*(3*G2 + G3)) * N * L * Lp / (k * T)
            return k1, k2

        r_h, a_h, b_h, c_h, d_h, e_h, f_h, g_h, h_h = solve_zeroth(V, T_high)
        k1_h, k2_h = compute_k1k2(r_h, a_h, b_h, c_h, d_h, e_h, f_h, g_h, h_h, V, L, T_high)
        r_l, a_l, b_l, c_l, d_l, e_l, f_l, g_l, h_l = solve_zeroth(V, T_low)
        k1_l, k2_l = compute_k1k2(r_l, a_l, b_l, c_l, d_l, e_l, f_l, g_l, h_l, V, L, T_low)

        ref = {
            'k1_highT': k1_h,
            'k2_highT': k2_h,
            'r_highT': r_h,
            'k1_lowT': k1_l,
            'k2_lowT': k2_l,
            'r_lowT': r_l
        }
        return dict(ref=ref)


# === block: score_0 (check id='s2_result') ===
def score_0(artifact, step, ctx):
            V = 1.0
            kB = 1.0
            L = 0.1
            Tc = 0.8224 * V / kB
            T_high = 0.9 * Tc
            T_low = 0.4 * Tc
            N = 1.0

            # Robust zeroth‑order solver (matches solve.sh, avoids fsolve warnings)
            def solve_zeroth(T):
                exp1 = np.exp(-6.0 * V / (kB * T))
                exp2 = np.exp(-2.0 * V / (kB * T))
                def eqs(vars):
                    b, g, h, r = vars
                    b = np.clip(b, 1e-15, None)
                    g = np.clip(g, 1e-15, None)
                    h = np.clip(h, 1e-15, None)
                    r = np.clip(r, 0.0, 1.0)
                    a = b * g * exp1 / h
                    c = b * h * exp2 / (g * exp1)
                    d = b * h * h / (g * g * exp1)
                    e = g**3 * exp1 / (h * h)
                    f = g * g * exp2 / h
                    # Eq. (2)
                    eq2 = 4*a + 9*b + 6*c + d + 3*e + 6*f + 3*g - 1.0
                    # Eq. (3)
                    eq3 = a + 3*b + 3*c + d + e + 3*f + 3*g + h - 1.0
                    # Eq. (4)
                    eq4 = a + 2*b + c + e + 2*f + g - (1.0 - r) / 3.0
                    # Order condition (Eq. (17) last) – log form
                    lpart = np.log((1.0 - r)**2 / (r * (2.0 + r))) - (4.0/3.0) * np.log(f / c)
                    return [eq2, eq3, eq4, lpart]

                if T >= Tc:
                    init = [0.01, 0.1, 0.3, 0.001]  # b, g, h, r
                else:
                    init = [0.001, 0.9, 0.001, 0.99]
                sol = fsolve(eqs, init, maxfev=2000, xtol=1e-12)
                b, g, h, r = sol
                b = max(b, 1e-15)
                g = max(g, 1e-15)
                h = max(h, 1e-15)
                r = max(0.0, min(1.0, r))
                a = b * g * exp1 / h
                c = b * h * exp2 / (g * exp1)
                d = b * h * h / (g * g * exp1)
                e = g**3 * exp1 / (h * h)
                f = g * g * exp2 / h
                return dict(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, r=r)

            # Compute anisotropy constants (Eqs. 21‑22 and 24)
            def compute_k1k2(sol, T):
                a = sol['a']; b = sol['b']; c = sol['c']; d = sol['d']
                e = sol['e']; f = sol['f']; g = sol['g']; h = sol['h']; r = sol['r']
                x1 = 4*a - 6*c - 2*d + 9*e + 12*f + 3*g
                x2 = 3*b + 4*c + d - 3*e - 4*f - g
                x3 = e + 2*f + g
                x4 = 2*c + d - 2*f - g
                y1 = a - 3*c - 2*d + 3*e + 6*f + 3*g
                y2 = b + 2*c + d - e - 2*f - g
                y3 = e + 3*f + 3*g + h
                y4 = c + d - f - g
                z1 = a - c + 3*e + 4*f + g
                z2 = -b - c - f - g
                z3 = b + c - e - f
                z4 = c - f
                z5 = f + g
                denA = 3*x3*(x1*y2 - x2*y1) + 3*z1*(x2*y3 - 3*x3*y2) + (x3 - 2*z3)*(x1*y3 - 3*x3*y1)
                if abs(denA) < 1e-30:
                    denA = 1e-30
                numA = -3*x3*(x1*y4 - x4*y1) + 3*z1*(3*x3*y4 - x4*y3) + (z4 - z5)*(x1*y3 - 3*x3*y1)
                A = (3*x3*y4 - x4*y3 - (x2*y3 - 3*x3*y2) * numA / denA) / max(x1*y3 - 3*x3*y1, 1e-30)
                B1 = -(27.0/2.0) * z4 / max(4.0*(1.0-r)*(2.0+r) + 27.0*z2, 1e-30)
                denB = z2 * denA
                if abs(denB) < 1e-30:
                    denB = 1e-30
                numB2_1 = -(x1*y3 - 3*x3*y1)*(x3*z5 - z3*(z4+z5))
                numB2_2 = z2*(x3*(x1*y4 - x4*y1) - z1*(3*x3*y4 - x4*y3))
                numB2_3 = -(z4+2*z5)*(x3*(x1*y2 - x2*y1) + z1*(x2*y3 - 3*x3*y2))
                B2 = (numB2_1 + numB2_2 + numB2_3) / denB
                numB3_1 = -(x1*y3 - 3*x3*y1)*(x3*z4 - 2*z3*z5)
                numB3_2 = -2*z2*(x3*(x1*y4 - x4*y1) - z1*(3*x3*y4 - x4*y3))
                numB3_3 = -(z4+2*z5)*(x3*(x1*y2 - x2*y1) + z1*(x2*y3 - 3*x3*y2))
                B3 = (numB3_1 + numB3_2 + numB3_3) / denB
                H = ( -x1*y4 + x4*y1 - (x1*y2 - x2*y1) * numA / denA ) / max(x1*y3 - 3*x3*y1, 1e-30)
                C1 = 0.5 - B1
                F1 = 0.5 + B1
                D_coef = 1.0 - 2*A - B2 + B3
                E_coef = 3*A + B2 - B3 + H
                G2 = 1.0 - A - B2 - H
                G3 = 2*A - B3 + 2*H
                k1 = 2.0 * (c*C1 + f*F1) * N * L * L / (kB * T)
                k2 = 2.0 * (b*(3*B2 + B3) + d*D_coef + e*E_coef + g*(3*G2 + G3)) * N * L * L / (kB * T)
                return k1, k2, r

            # Compute reference values
            sol_high = solve_zeroth(T_high)
            k1_h, k2_h, r_h = compute_k1k2(sol_high, T_high)
            sol_low = solve_zeroth(T_low)
            k1_l, k2_l, r_l = compute_k1k2(sol_low, T_low)
            ref = {
                'k1_highT': k1_h,
                'k2_highT': k2_h,
                'r_highT': r_h,
                'k1_lowT': k1_l,
                'k2_lowT': k2_l,
                'r_lowT': r_l
            }

            # Compare artifact fields to reference
            fields = ['k1_highT', 'k2_highT', 'r_highT', 'k1_lowT', 'k2_lowT', 'r_lowT']
            scores = []
            for f in fields:
                val = artifact.get(f)
                if val is None or not isinstance(val, (int, float)):
                    scores.append(0.0)
                    continue
                ref_val = ref[f]
                # tolerance: absolute 1e-6, relative 1e-4 (approved plan)
                tol = max(1e-6, 1e-4 * abs(ref_val))
                err = abs(val - ref_val)
                if err <= tol:
                    scores.append(1.0)
                else:
                    # linear decay: full credit within tol, 0 at 11*tol (10*tol excess)
                    excess = err - tol
                    factor = excess / (10.0 * tol)
                    scores.append(max(0.0, 1.0 - factor))
            return float(np.mean(scores)) if scores else 0.0


_SCORERS = {
    's2_result': score_0,
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
