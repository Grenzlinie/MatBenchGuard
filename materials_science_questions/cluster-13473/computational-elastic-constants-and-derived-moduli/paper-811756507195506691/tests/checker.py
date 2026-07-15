import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from math import pi, sqrt, sin, cos


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
    mu0 = 4.0e-7 * pi
    R = 1.25e-6
    Vp = (4.0/3.0) * pi * R**3
    mue = 1.0
    mup = 1000.0
    beta = (mup - mue) / (mup + 2.0 * mue)
    Ms = 1.7e6
    phi = 0.11

    eps = 1e-6

    def compute_f_array(b, gamma, l_max=200):
        """Return f[l] = sum_g(l,b,gamma) for l=1..l_max."""
        f = np.zeros(l_max+1)
        for l in range(1, l_max+1):
            # ranges for class A chains
            if b % 2 == 1:
                a_range = np.arange(-(b-1)//2, (b-1)//2 + 1)
            else:
                # even b: range [-(b/2-1), (b/2-1)] inclusive
                a_range = np.arange(-(b//2 - 1), b//2)
            if l % 2 == 1:
                a3_range = np.arange(-(l-1)//2, (l-1)//2 + 1)
            else:
                a3_range = np.arange(-(l//2 - 1), l//2)
            sum_g = 0.0
            for A1 in a_range:
                for A2 in a_range:
                    for A3 in a3_range:
                        if A1 == 0 and A2 == 0 and A3 == 0:
                            continue
                        x = sqrt(6) * A1 * R + 2 * A3 * R * sin(gamma)
                        y = sqrt(6) * A2 * R
                        z_val = 2 * A3 * R * cos(gamma)
                        r2 = x*x + y*y + z_val*z_val
                        denom = 4 * pi * mu0 * (r2**2.5)
                        num = 2 * z_val**2 - x*x - y*y
                        sum_g += num / denom
            # class B chains
            if b % 2 == 1:
                b1_range = [i for i in range(-(b-1)//2, (b-1)//2 + 1) if i != 0]
            else:
                b1_range = [i for i in range(-(b//2), b//2 + 1) if i != 0]
            if l % 2 == 1:
                b3_range = [i for i in range(-(l-1)//2, (l-1)//2 + 1) if i != 0]
            else:
                b3_range = [i for i in range(-(l//2), l//2 + 1) if i != 0]
            for B1 in b1_range:
                for B2 in b1_range:
                    for B3 in b3_range:
                        x = (sqrt(6)/2) * (2*B1 - 1) * R + 2 * (B3 - 1) * R * sin(gamma)
                        y = (sqrt(6)/2) * (2*B2 - 1) * R
                        z_val = 2 * (B3 - 1) * R * cos(gamma)
                        r2 = x*x + y*y + z_val*z_val
                        denom = 4 * pi * mu0 * (r2**2.5)
                        num = 2 * z_val**2 - x*x - y*y
                        sum_g += num / denom
            f[l] = sum_g
        return f

    def solve_pz(l, f_val, H0):
        """Iteratively solve for dipole moment p_z."""
        p = 0.0
        for _ in range(200):
            H_loc = H0 + f_val * p
            p_new = (3 * mue * mu0 * beta * Vp * H_loc) / (1 + 3 * mue * beta * H_loc / Ms)
            if abs(p_new - p) < 1e-20:
                return p_new
            p = p_new
        return p

    def compute_delta_G(L, sigma, b, H0, gamma):
        """Compute field‑induced shear modulus ΔG (Pa) for given parameters.
        L: mean column length, sigma: standard deviation, b: column width,
        H0: external field in A/m, gamma: shear strain."""
        l_max = 2 * int(round(L))
        shifts = [-2*eps, -eps, 0.0, eps, 2*eps]
        f_arrays = []
        for sh in shifts:
            g = gamma + sh
            f_arrays.append(compute_f_array(b, g, l_max))

        def J_for_f_array(f_arr):
            l_vals = np.arange(1, l_max+1)
            exponent = -((l_vals - L)**2) / (2 * sigma**2)
            exp_weights = np.exp(exponent)
            S = np.sum(l_vals * exp_weights)
            factor = phi / (Vp * (b**2 + (b-1)**2) * S)
            n_l_over_V = factor * exp_weights
            J = 0.0
            for i, li in enumerate(l_vals):
                f_l = f_arr[li]
                try:
                    pz = solve_pz(li, f_l, H0)
                except:
                    pz = 0.0
                n_part = b**2 * li + (b-1)**2 * (li-1)
                J += n_part * pz * n_l_over_V[i]
            return J

        J_2m, J_m, J_0, J_p, J_2p = [J_for_f_array(fa) for fa in f_arrays]
        chi_2m = J_2m / (mu0 * H0)
        chi_m  = J_m  / (mu0 * H0)
        chi_0  = J_0  / (mu0 * H0)
        chi_p  = J_p  / (mu0 * H0)
        chi_2p = J_2p / (mu0 * H0)

        dchi_m  = (chi_0 - chi_2m) / (2*eps)
        dchi_0  = (chi_p - chi_m)  / (2*eps)
        dchi_p  = (chi_2p - chi_0) / (2*eps)

        tau_m = -0.5 * mu0 * (H0 / (1 + chi_m))**2 * dchi_m
        tau_0 = -0.5 * mu0 * (H0 / (1 + chi_0))**2 * dchi_0
        tau_p = -0.5 * mu0 * (H0 / (1 + chi_p))**2 * dchi_p

        Delta_G = (tau_p - tau_m) / (2*eps)
        return Delta_G

    return {'compute_delta_G': compute_delta_G}


# === block: score_0 (check id='value_match') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact
    compute_delta_G = ctx['compute_delta_G']
    MU = 1e6  # conversion between MPa <-> Pa, MA/m <-> A/m
    rows = artifact_rows
    scores = []
    for row in rows:
        try:
            L = int(row['L'])
            sigma = int(row['sigma'])
            b_val = int(row['b'])
            H0_MA = float(row['H0'])
            gamma = float(row['gamma'])
            agent_DG = float(row['Delta_G'])
            H0 = H0_MA * MU
            expected_DG = compute_delta_G(L, sigma, b_val, H0, gamma)  # Pa
            agent_DG_Pa = agent_DG * MU
            diff = abs(agent_DG_Pa - expected_DG)
            if expected_DG < 0.2 * MU:
                tol = 0.02 * MU
            else:
                tol = 0.05 * expected_DG
            if diff <= tol:
                row_score = 1.0
            else:
                row_score = max(0.0, 1.0 - (diff - tol) / (0.5 * expected_DG))
            scores.append(row_score)
        except Exception as e:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='trend_check') ===
def score_1(artifact, step, ctx):
    rows = artifact

    def rows_match(L=None, sigma=None, b=None, H0=None, gamma=None):
        res = []
        for r in rows:
            try:
                if L is not None and int(r['L']) != L: continue
                if sigma is not None and int(r['sigma']) != sigma: continue
                if b is not None and int(r['b']) != b: continue
                if H0 is not None and abs(float(r['H0']) - H0) > 1e-6: continue
                if gamma is not None and abs(float(r['gamma']) - gamma) > 1e-6: continue
                res.append(r)
            except:
                pass
        return res

    total = 0
    passed = 0

    # L sweep for σ=3,6,9
    for sig in [3,6,9]:
        subset = rows_match(sigma=sig, b=2, H0=1.0, gamma=0.003)
        subset.sort(key=lambda r: int(r['L']))
        dgv = [float(r['Delta_G']) for r in subset]
        for i in range(len(dgv)-1):
            total += 1
            if dgv[i+1] >= dgv[i] - 0.01:
                passed += 1

    # b experimental pairs
    pairs = [(10,2),(20,3),(30,4),(40,5)]
    subset = []
    for Lv, bv in pairs:
        r = rows_match(L=Lv, sigma=9, b=bv, H0=1.0, gamma=0.003)
        if r:
            subset.append(r[0])
    subset.sort(key=lambda r: int(r['b']))
    dgv = [float(r['Delta_G']) for r in subset]
    for i in range(len(dgv)-1):
        total += 1
        if dgv[i] >= dgv[i+1] - 0.01:
            passed += 1

    # b continuous L=30
    subset = rows_match(L=30, sigma=9, H0=1.0, gamma=0.003)
    subset.sort(key=lambda r: int(r['b']))
    dgv = [float(r['Delta_G']) for r in subset]
    for i in range(len(dgv)-1):
        total += 1
        if dgv[i] >= dgv[i+1] - 0.01:
            passed += 1

    # H0 sweep
    for gam in [0.001, 0.003, 0.005]:
        subset = rows_match(L=30, sigma=3, b=2, gamma=gam)
        subset.sort(key=lambda r: float(r['H0']))
        dgv = [float(r['Delta_G']) for r in subset]
        for i in range(len(dgv)-1):
            total += 1
            if dgv[i+1] >= dgv[i] - 0.01:
                passed += 1

    # gamma dependence
    for h0 in [x/10.0 for x in range(1,11)]:
        subset = rows_match(L=30, sigma=3, b=2, H0=h0)
        subset.sort(key=lambda r: float(r['gamma']))
        dgv = [float(r['Delta_G']) for r in subset]
        for i in range(len(dgv)-1):
            total += 1
            if dgv[i] >= dgv[i+1] - 0.01:
                passed += 1

    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'value_match': score_0,
    'trend_check': score_1,
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
