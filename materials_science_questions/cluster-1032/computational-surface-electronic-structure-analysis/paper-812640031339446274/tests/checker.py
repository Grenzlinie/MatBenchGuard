import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.special import jv
from scipy.optimize import brentq
from scipy.integrate import quad
import cmath
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
        m0 = -0.169
        m1 = 3.353
        m2 = 29.375
        A = 2.513
        B = 1.836
        R0_nm = 1.49
        R_list_nm = [r*R0_nm for r in [2,4,6,8,10]]
        R_list_ang = [r*10 for r in R_list_nm]  # nm -> Å

        def kappas(E):
            term1 = -(m0/m2 + A**2/(2*m2**2))
            inner = cmath.sqrt(A**4/(4*m2**4) + E**2/(m2**2) + A**2*m0/(m2**3))
            kp = cmath.sqrt(term1 + inner)
            km = cmath.sqrt(term1 - inner)
            return kp, km

        def Delta(k, E):
            return m2 * k**2 + m0 - E

        def Tj(z, j):
            return jv(j+0.5, z) / jv(j-0.5, z)

        def f1(E, j, R):
            kp, km = kappas(E)
            Dp = Delta(kp, E)
            Dm = Delta(km, E)
            lhs = (kp * Dm) / (km * Dp)
            rhs = Tj(kp*R, j) / Tj(km*R, j)
            return np.real(lhs - rhs)

        def solve_energy(j, R, sign=1):
            # scan for the lowest-energy root with desired sign
            E_grid = np.linspace(-0.8, 0.8, 4001)
            vals = np.array([f1(e, j, R) for e in E_grid])
            # extract indices where sign changes
            idx = np.where(np.diff(np.sign(vals)))[0]
            cand = None
            for i in idx:
                e1, e2 = E_grid[i], E_grid[i+1]
                try:
                    root = brentq(f1, e1, e2, args=(j,R), xtol=1e-12, maxiter=100)
                    if sign == 0 or np.sign(root) == sign:
                        # prefer smallest absolute value among candidates
                        if cand is None or abs(root) < abs(cand):
                            cand = root
                except Exception:
                    pass
            if cand is None:
                raise ValueError(f"No root found for j={j}, R={R}")
            return cand

        def get_Phis(j, E, R):
            kp, km = kappas(E)
            Dp = Delta(kp, E)
            Dm = Delta(km, E)
            # boundary condition: α_+ J_{j+1/2}(kp*R) + α_- J_{j+1/2}(km*R) = 0
            ratio = jv(j+0.5, kp*R) / jv(j+0.5, km*R)
            alpha_m = -ratio
            # radial functions (unnormalized)
            def Phi1(r):
                t1 = (1j * A * kp / Dp) * jv(j-0.5, kp*r)
                t2 = alpha_m * (1j * A * km / Dm) * jv(j-0.5, km*r)
                return t1 + t2
            def Phi2(r):
                return 0.0+0j
            def Phi3(r):
                return 0.0+0j
            def Phi4(r):
                t1 = jv(j+0.5, kp*r)
                t2 = alpha_m * jv(j+0.5, km*r)
                return t1 + t2
            return Phi1, Phi2, Phi3, Phi4

        def norm_radial(Phi1, Phi2, Phi3, Phi4, R):
            integrand = lambda r: r * (np.abs(Phi1(r))**2 + np.abs(Phi2(r))**2 + np.abs(Phi3(r))**2 + np.abs(Phi4(r))**2)
            val, _ = quad(integrand, 0, R, limit=200)
            return val

        # 1. eigenenergies
        ref_energies = {}
        for R_nm, R_ang in zip(R_list_nm, R_list_ang):
            for j_val in [0.5, 1.5]:
                key = (j_val, round(R_nm, 10))
                try:
                    E = solve_energy(j_val, R_ang, sign=1)
                    ref_energies[key] = abs(E)
                except Exception as e:
                    print(f"WARN energy failed j={j_val} R={R_nm}: {e}")
                    ref_energies[key] = None

        # 2. overlap integrals S14, S23
        ref_overlap = {}
        for R_nm, R_ang in zip(R_list_nm, R_list_ang):
            key = round(R_nm, 10)
            try:
                E_pos = solve_energy(0.5, R_ang, sign=1)
                E_neg = solve_energy(-0.5, R_ang, sign=-1)
                Phi1_pos, Phi2_pos, Phi3_pos, Phi4_pos = get_Phis(0.5, E_pos, R_ang)
                Phi1_neg, Phi2_neg, Phi3_neg, Phi4_neg = get_Phis(-0.5, E_neg, R_ang)
                N_pos = norm_radial(Phi1_pos, Phi2_pos, Phi3_pos, Phi4_pos, R_ang)
                N_neg = norm_radial(Phi1_neg, Phi2_neg, Phi3_neg, Phi4_neg, R_ang)
                # unnormalized overlap S14
                integrand_S14 = lambda r: r * np.real(np.conj(Phi1_pos(r)) * Phi4_neg(r))
                S14_un, _ = quad(integrand_S14, 0, R_ang, limit=200)
                S14 = S14_un / np.sqrt(N_pos * N_neg)
                S23 = 0.0
                ref_overlap[key] = (S14, S23)
            except Exception as e:
                print(f"WARN overlap failed R={R_nm}: {e}")
                ref_overlap[key] = None

        ctx = {
            'ref_energies': ref_energies,
            'ref_overlap': ref_overlap
        }
        return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
        ref = ctx.get('ref_energies', {})
        if not artifact or not ref:
            return 0.0
        tol = step.get('tolerance', 0.01)
        rows = list(artifact)
        total = 0
        good = 0
        for row in rows:
            try:
                j_val = float(row.get('j', 0))
                R_nm = float(row.get('R', 0))
                key = (j_val, round(R_nm, 10))
                if key in ref:
                    ref_e = ref[key]
                    if ref_e is None:
                        continue
                    sub_e = float(row.get('energy', 0))
                    if abs(sub_e - ref_e) <= tol:
                        good += 1
                    total += 1
            except Exception:
                continue
        score = good / total if total else 0.0
        return score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
        ref = ctx.get('ref_overlap', {})
        if not artifact or not ref:
            return 0.0
        tol = step.get('tolerance', 0.01)
        rows = list(artifact)
        total = 0
        good = 0
        for row in rows:
            try:
                R_nm = float(row.get('R', 0))
                key = round(R_nm, 10)
                if key in ref:
                    ref_vals = ref[key]
                    if ref_vals is None:
                        continue
                    s14_ref, s23_ref = ref_vals
                    s14_sub = float(row.get('S_14', 0))
                    s23_sub = float(row.get('S_23', 0))
                    if abs(s14_sub - s14_ref) <= tol and abs(s23_sub - s23_ref) <= tol:
                        good += 1
                    total += 1
            except Exception:
                continue
        score = good / total if total else 0.0
        return score


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
