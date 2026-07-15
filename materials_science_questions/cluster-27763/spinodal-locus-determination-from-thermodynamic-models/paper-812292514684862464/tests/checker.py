import os
import json
import csv

# === author imports / helpers ===
import csv, math, numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import simpson

# ---------- Quasichemical EOS for 3D, λ=1 ----------
LAMBDA = 1.0

def x_from_T(T):
    return math.exp(-1.0/T)

def rho_from_r(r, x):
    # eq (46)
    lam2 = LAMBDA/2.0
    x_m_half = x**(-lam2)      # x^{-λ/2}
    x_p_half = x**(1+lam2)     # x^{1+λ/2}
    x_m1_half = x**(lam2 - 1)  # x^{λ/2-1}
    s_r = math.sqrt(r) if r>0 else 1e-6
    num = 1 + s_r*(2*x_m_half + x_p_half) + 3*r + x_m1_half * r**(1.5)
    den = (r**(-0.5))*x_m1_half + 4 + 2*s_r*(2*x_m_half + x_p_half) + 4*r + x_m1_half * r**(1.5)
    return num/den

def solve_r_for_rho(rho_target, T):
    x = x_from_T(T)
    def f(r):
        if r <= 0: r = 1e-12
        return rho_from_r(r, x) - rho_target
    try:
        # r typically positive; rho monotonic? try broad interval
        r_sol = brentq(f, 1e-10, 1e6, xtol=1e-12)
        return r_sol, x
    except:
        # fallback: scan
        best = (None, 1e9)
        for r in np.logspace(-10, 6, 1000):
            err = abs(rho_from_r(r, x) - rho_target)
            if err < best[1]:
                best = (r, err)
        return best[0], x

def pressure(r, rho, T, x):
    # eq (39) with λ=1: P* = (3T*/4) * ln( ( (1-ρ)^{5/3} * [...] ) / x^{-0.5} )
    lam2 = LAMBDA/2.0
    x_m_half = x**(-lam2)
    x_p_half = x**(1+lam2)
    x_m1_half = x**(lam2-1)
    s = math.sqrt(r) if r>0 else 0.0
    numerator = (1 - rho)**(5.0/3.0) * (x_m1_half + 3*s + r*(2*x_m_half + x_p_half) + r**(1.5))
    denominator = x_m1_half
    if numerator <= 0 or denominator <= 0:
        return float('inf')
    return (3*T/4) * math.log(numerator/denominator)

def chem_pot(r, rho, T):
    # eq (40) with λ=1: mu* = 3(λ-2)/2 + T* log( r^{3/2} ( (1-ρ)/ρ )^2 )
    if rho <= 0 or rho >= 1:
        return float('-inf')
    return 1.5*(LAMBDA-2) + T * math.log(r**(1.5) * ((1-rho)/rho)**2)

def compute_EOS(rho, T):
    r, x = solve_r_for_rho(rho, T)
    P = pressure(r, rho, T, x)
    mu = chem_pot(r, rho, T)
    return P, mu


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
    # Generate reference curves for λ=1
    # ΔT = 0.002; 
    T_max = 1.25
    T_step = 0.002
    Ts = np.arange(T_step, T_max + T_step/2, T_step)

    # --- Spinodal reference ---
    spinodal_points = []  # (T, P)
    for T in Ts:
        x = x_from_T(T)
        # dP/drho = 0 => find rho where derivative sign changes
        # Scan rho grid and find where P'(rho) changes sign
        rho_grid = np.linspace(0.005, 0.995, 300)
        P_vals = []
        for rho in rho_grid:
            try:
                P, _ = compute_EOS(rho, T)
                P_vals.append(P)
            except:
                P_vals.append(np.nan)
        P_arr = np.array(P_vals)
        # compute numeric derivative
        dP = np.diff(P_arr) / (rho_grid[1]-rho_grid[0])
        # find sign changes (0 crossing)
        signs = np.sign(dP)
        change_idx = np.where(np.diff(signs))[0]
        for idx in change_idx:
            rho_spin = (rho_grid[idx] + rho_grid[idx+1]) / 2.0
            try:
                P_spin, _ = compute_EOS(rho_spin, T)
                spinodal_points.append((T, P_spin))
            except:
                pass
    # filter only stable range (remove noise)
    if spinodal_points:
        spinodal_arr = np.array(spinodal_points)
        # sort by P
        spinodal_arr = spinodal_arr[spinodal_arr[:,1].argsort()]
    else:
        spinodal_arr = np.array([[0,0]])

    # --- Binodal via equal-area Maxwell construction ---
    binodal_points = []
    for T in Ts:
        # Determine if coexistence exists (rough estimate: check for van der Waals loop)
        rho_fine = np.linspace(0.001, 0.999, 500)
        Ps = []
        for rho in rho_fine:
            try:
                Pr, _ = compute_EOS(rho, T)
                Ps.append(Pr)
            except:
                Ps.append(np.nan)
        P_arr = np.array(Ps)
        # check if there is a region with negative slope
        dPd = np.diff(P_arr) / 0.002
        if np.any(dPd < -1e-6):  # loop exists
            # define function to integrate area difference
            def area_diff(P_eq):
                # find two crossing densities: left (<0.5) and right (>0.5) where P(rho)=P_eq
                left_idx = np.where((P_arr - P_eq) >= 0)[0]
                right_idx = np.where((P_arr - P_eq) <= 0)[0]
                if len(left_idx)==0 or len(right_idx)==0:
                    return 1e9
                rho_left = rho_fine[left_idx[0]]
                rho_right = rho_fine[right_idx[-1]]
                # integrate P(rho)-P_eq from rho_left to rho_right using fine grid
                mask = (rho_fine >= rho_left) & (rho_fine <= rho_right)
                rho_mask = rho_fine[mask]
                P_mask = P_arr[mask]
                if len(rho_mask)<2:
                    return 1e9
                integrand = P_mask - P_eq
                return simpson(integrand, rho_mask)
            # find P range: min and max of P in stable regions
            P_min = max(P_arr[np.where(rho_fine<0.5) and np.isfinite(P_arr)].min(), 0.0)
            P_max = P_arr[np.where(rho_fine>0.5) and np.isfinite(P_arr)].max()
            if P_max > P_min:
                try:
                    P_eq = brentq(area_diff, P_min*1.01, P_max*0.99, xtol=1e-6)
                    # get the two densities
                    left_idx = np.argmin(np.abs(P_arr - P_eq))
                    rho_left = rho_fine[left_idx]
                    # find right crossing by scanning from 0.5 up
                    for i in range(left_idx+1, len(rho_fine)):
                        if (P_arr[i-1] - P_eq) * (P_arr[i] - P_eq) < 0:
                            rho_right = (rho_fine[i-1]+rho_fine[i])/2.0
                            break
                    else:
                        continue
                    binodal_points.append((T, P_eq))
                except:
                    pass

    if binodal_points:
        binodal_arr = np.array(binodal_points)
        binodal_arr = binodal_arr[binodal_arr[:,0].argsort()]
    else:
        binodal_arr = np.array([[0,0]])

    # --- Density maxima locus ---
    P_range = np.linspace(0.02, 0.25, 100)
    density_maxima = []
    for P_val in P_range:
        # find T where d(rho)/dT = 0 at constant P
        def rho_at_T_given_P(T, P):
            # need to solve for rho such that pressure equals P
            # we can invert P(rho,T)
            def f(rho):
                try:
                    Pr, _ = compute_EOS(rho, T)
                    return Pr - P
                except:
                    return 1e9
            try:
                rho_sol = brentq(f, 0.005, 0.995, xtol=1e-8)
                return rho_sol
            except:
                return None
        # scan T to find maximum rho
        Ts_tmp = np.linspace(0.02, 1.2, 200)
        rhos = []
        valid_T = []
        for Tt in Ts_tmp:
            rho = rho_at_T_given_P(Tt, P_val)
            if rho is not None:
                rhos.append(rho)
                valid_T.append(Tt)
        if len(rhos) < 3:
            continue
        rhos = np.array(rhos)
        Ts_tmp2 = np.array(valid_T)
        # find peaks (local maxima)
        # compute derivative
        d_rho_dT = np.gradient(rhos, Ts_tmp2)
        # look for sign change positive->negative
        sign = np.sign(d_rho_dT)
        for i in range(1, len(sign)-1):
            if sign[i] >= 0 and sign[i+1] <= 0:
                T_peak = (Ts_tmp2[i] + Ts_tmp2[i+1])/2.0
                rho_peak = (rhos[i] + rhos[i+1])/2.0
                P_star = P_val
                density_maxima.append((T_peak, P_star, rho_peak))
                break

    if density_maxima:
        dmax_arr = np.array(density_maxima)
    else:
        dmax_arr = np.array([[0,0,0]])

    ctx = {
        'ref_binodal': binodal_arr,
        'ref_spinodal': spinodal_arr,
        'ref_dmax': dmax_arr
    }
    return ctx


# === block: score_0 (check id='phase_diagram') ===
def score_0(artifact, step, ctx):
        ref_binodal = ctx.get('ref_binodal', np.array([[0,0]]))
        ref_spinodal = ctx.get('ref_spinodal', np.array([[0,0]]))
        tol_full = 0.01   # RMS full credit threshold
        rows = artifact
        if not rows:
            return 0.0
        binodal_pts = []
        spinodal_pts = []
        for r in rows:
            ctype = (r.get('curve_type') or '').strip()
            try:
                T_val = r.get('T_star')
                P_val = r.get('P_star')
                T = float(T_val) if T_val is not None else None
                P = float(P_val) if P_val is not None else None
                if T is None or P is None:
                    continue
            except (ValueError, TypeError):
                continue
            if ctype == 'binodal':
                binodal_pts.append([T, P])
            elif ctype == 'spinodal':
                spinodal_pts.append([T, P])
        def curve_rms(agent_pts, ref_pts):
            if len(agent_pts) == 0 or len(ref_pts) == 0:
                return 999.0
            agent_arr = np.array(agent_pts)
            ref_arr = np.array(ref_pts)
            if ref_arr.ndim == 1:
                ref_arr = ref_arr.reshape(-1, 1)
            if ref_arr.shape[1] < 2:
                return 999.0
            dists = []
            for i in range(ref_arr.shape[0]):
                p_ref = ref_arr[i, :2]
                sq_dists = np.sum((agent_arr - p_ref)**2, axis=1)
                min_d = np.sqrt(np.min(sq_dists))
                dists.append(min_d)
            return np.sqrt(np.mean(np.array(dists)**2))
        rms_bin = curve_rms(binodal_pts, ref_binodal[:, :2] if ref_binodal.ndim >= 2 else ref_binodal)
        rms_spin = curve_rms(spinodal_pts, ref_spinodal[:, :2] if ref_spinodal.ndim >= 2 else ref_spinodal)
        def rms_score(rms, tol):
            if rms <= tol:
                return 1.0
            else:
                return max(0.0, 1.0 - (rms - tol) / (0.1 - tol))
        s_bin = rms_score(rms_bin, tol_full)
        s_spin = rms_score(rms_spin, tol_full)
        return 0.5 * s_bin + 0.5 * s_spin


# === block: score_1 (check id='density_maxima') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref_dmax = ctx['ref_dmax']
        tol_full = 0.02
        rows = artifact
        if not rows:
            return 0.0
        agent_pts = []
        for r in rows:
            try:
                T = float(r['T_star'])
                P = float(r['P_star'])
                rho = float(r['rho'])
            except:
                continue
            if 0 < rho < 1:
                agent_pts.append([T, P])
        if len(agent_pts) == 0 or len(ref_dmax) == 0:
            return 0.0
        agent_arr = np.array(agent_pts)
        ref_arr = ref_dmax[:, :2]  # T,P
        dists = []
        for p_ref in ref_arr:
            sq_dists = np.sum((agent_arr - p_ref)**2, axis=1)
            min_d = np.sqrt(np.min(sq_dists))
            dists.append(min_d)
        rms = np.sqrt(np.mean(np.array(dists)**2))
        # additional structural check: density maxima P* range 0.1 < P* < 0.2
        in_range = np.all((agent_arr[:,1] > 0.05) & (agent_arr[:,1] < 0.25))
        struct_ok = 1.0 if in_range else 0.5
        if rms <= tol_full:
            rms_score = 1.0
        else:
            rms_score = max(0.0, 1.0 - (rms - tol_full) / (0.1 - tol_full))
        # combine: 90% rms, 10% structural
        return 0.9 * rms_score + 0.1 * struct_ok


_SCORERS = {
    'phase_diagram': score_0,
    'density_maxima': score_1,
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
