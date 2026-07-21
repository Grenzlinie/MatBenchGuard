import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math
import csv
import json
import io

# ----------------- material constants (Table 1) -----------------
C44_CdS = 1.49e10          # N/m^2
rho_CdS = 4824.0            # kg/m^3
e15_CdS = -0.21              # C/m^2
eps11_CdS = 7.99e-11         # F/m

C44_ZnO = 4.25e10
rho_ZnO = 5676.0
e15_ZnO = -0.59
eps11_ZnO = 7.38e-11

# derived quantities
Ct_CdS = math.sqrt(C44_CdS / rho_CdS)   # m/s

# layer geometry: equal thicknesses h = h'  => D = 2h+2h' = 4h, so h = D/4
# we set D = 1.0 for dimensionless computation
D = 1.0
h = D / 4.0   # half-thickness of each layer

# ---------- helper: compute alpha for a medium ----------
def alpha(omega, C44, rho, e15, eps11, k_par):
    """alpha = sqrt(k_par^2 - rho*omega^2 / (C44*(1 + e15^2/(eps11*C44))))"""
    factor = C44 * (1.0 + e15**2 / (eps11 * C44))
    arg = k_par**2 - rho * omega**2 / factor
    # for decaying waves, arg can be negative; we handle sqrt of complex with real part for analysis
    # in transfer matrix we need cosh/sinh of alpha*h, so we compute alpha as complex sqrt
    return np.sqrt(arg + 0j)

# ---------- transfer matrix T (4x4) from appendix ----------
def transfer_matrix(omega, k_par):
    # parameters for CdS (medium A) and ZnO (A')
    # use negative e15 as given
    # compute alpha for each
    a1 = alpha(omega, C44_CdS, rho_CdS, e15_CdS, eps11_CdS, k_par)
    a2 = alpha(omega, C44_ZnO, rho_ZnO, e15_ZnO, eps11_ZnO, k_par)
    a = a1
    ap = a2
    k = k_par
    # shorthand for material constants
    C44 = C44_CdS
    e15 = e15_CdS
    eps11 = eps11_CdS
    C44p = C44_ZnO
    e15p = e15_ZnO
    eps11p = eps11_ZnO

    # hyperbolic functions
    S1 = np.sinh(k * h)
    C1 = np.cosh(k * h)
    S1p = np.sinh(k * h)          # same thickness
    C1p = np.cosh(k * h)
    Sh1 = np.sinh(2 * k * h)
    Ch1 = np.cosh(2 * k * h)
    Sh1p = np.sinh(2 * k * h)
    Ch1p = np.cosh(2 * k * h)
    S2 = np.sinh(a * h)
    C2 = np.cosh(a * h)
    S2p = np.sinh(ap * h)
    C2p = np.cosh(ap * h)
    Sh2 = np.sinh(2 * a * h)
    Ch2 = np.cosh(2 * a * h)
    Sh2p = np.sinh(2 * ap * h)
    Ch2p = np.cosh(2 * ap * h)

    # intermediate quantities (appendix)
    B = (e15/eps11) - (e15p/eps11p)
    C = k * (eps11 * e15p - eps11p * e15) / (eps11p * ap * (C44p + e15p**2 / eps11p))
    Cp = k * (eps11 * e15p - eps11p * e15) / (eps11 * a * (C44 + e15**2 / eps11))
    F = a * (C44 + e15**2 / eps11) / (ap * (C44p + e15p**2 / eps11p))
    Fp = 1.0 / F
    E = eps11 / eps11p
    Ep = 1.0 / E

    # matrix elements (use np.complex for sqrt of a, but results should be real for the determinant)
    t11 = Ch1 * Ch1p + 0.5 * (E + Ep) * Sh1 * Sh1p + 0.5 * B * C * Sh1 * Sh2p
    t12 = B * (Ch1p - Ch2p) * C1 * C2 + B * (Ep * C2 * S1 * Sh1p - F * C1 * S2 * Sh2p)
    t13 = -Sh1 * Ch1p - (E * C1**2 + Ep * S1**2) * Sh1p - B * C * C1**2 * Sh2p
    t14 = B * (Ch2p - Ch1p) * C1 * S2 - B * Ep * Sh1p * S1 * S2 + B * F * C1 * C2 * Sh2p

    t21 = Cp * C1 * S2 * Sh1p - C * S1 * C2 * Sh2p + (E * Cp * Ch1p - C * Fp * Ch2p) * S1 * S2
    t22 = Ch2 * Ch2p + 0.5 * (F + Fp) * Sh2 * Sh2p + 0.5 * B * Cp * Sh1p * Sh2
    t23 = C * C1 * C2 * Sh2p - Cp * S1 * S2 * Sh1p + (C * Fp * Ch2p - Cp * E * Ch1p) * C1 * S2
    t24 = -Ch2p * Sh2 - (Fp * S2**2 + F * C2**2) * Sh2p - B * Cp * Sh1p * S2**2

    t31 = -Ch1p * Sh1 - B * C * Sh2p * S1**2 - (Ep * C1**2 + E * S1**2) * Sh1p
    t32 = B * (Ch2p - Ch1p) * S1 * C2 - B * Ep * C1 * C2 * Sh1p + B * F * S1 * S2 * Sh2p
    t33 = t11
    t34 = B * (Ch1p - Ch2p) * S1 * S2 + B * (Ep * C1 * S2 * Sh1p - F * S1 * C2 * Sh2p)

    t41 = C * S1 * S2 * Sh2p - Cp * C1 * C2 * Sh1p + (C * Fp * Ch2p - Cp * E * Ch1p) * C2 * S1
    t42 = -Ch2p * Sh2 - B * Cp * Sh1p * C2**2 - (Fp * C2**2 + F * S2**2) * Sh2p
    t43 = Cp * S1 * C2 * Sh1p - C * C1 * S2 * Sh2p + (E * Cp * Ch1p - C * Fp * Ch2p) * C1 * C2
    t44 = t22

    T = np.array([[t11, t12, t13, t14],
                  [t21, t22, t23, t24],
                  [t31, t32, t33, t34],
                  [t41, t42, t43, t44]])
    return T.real.astype(np.float64)  # physical eigenvalues are real; we expect real matrix

# ---------- compute cos(k1D) eigenvalues from 2x2 block of (T+T^{-1})/2 ----------
def cos_eigenvalues(omega, k_par):
    T = transfer_matrix(omega, k_par)
    try:
        Ti = np.linalg.inv(T)
    except np.linalg.LinAlgError:
        # singular matrix -> return None
        return None
    S = 0.5 * (T + Ti)
    block = S[:2, :2]
    evals = np.linalg.eigvals(block)
    return np.real(evals)

# ---------- check if bulk wave propagates (any eigenvalue within [-1,1]) ----------
def in_band(omega, k_par):
    evs = cos_eigenvalues(omega, k_par)
    if evs is None:
        return False
    return np.any(np.abs(evs) <= 1.0)

# ---------- find band edges for a given k_par D (kD) by scanning omega ----------
def get_band_edges(kD, omega_min=0.0, omega_max=5.0, n_grid=20000):
    k_par = kD / D  # D=1
    omegas = np.linspace(omega_min, omega_max, n_grid)
    inband = np.zeros(n_grid, dtype=bool)
    for i, om in enumerate(omegas):
        inband[i] = in_band(om, k_par)
    edges = []
    # find rising/falling edges
    changes = np.diff(inband.astype(int))
    start_idx = np.where(changes == 1)[0] + 1
    end_idx = np.where(changes == -1)[0]
    # refine edges with bisection
    def refine(fun, lo, hi):
        # bisection to find omega where in_band toggles
        for _ in range(30):
            mid = (lo + hi) / 2
            if fun(mid) == fun(lo):
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    
    # collect intervals
    if len(start_idx) > 0 and len(end_idx) > 0:
        for s, e in zip(start_idx, end_idx):
            if s < e:
                lo = omegas[s-1] if s>0 else omega_min
                hi = omegas[e]
                # refine lower edge
                lower = refine(lambda om: in_band(om, k_par), lo, omegas[s])
                upper = refine(lambda om: in_band(om, k_par), omegas[e-1], hi)
                edges.append((lower, upper))
    # also handle first interval if in band at omega_min
    if inband[0]:
        # band starts below omega_min; discard
        pass
    # sort by lower frequency
    edges.sort(key=lambda x: x[0])
    return edges  # list of (lower, upper) in dimensionless Omega (actually Omega = omega*D/(2π Ct_CdS)? we are working in ω, will convert later)

# For output, we need dimensionless Omega: Ω = ω*D/(2π*Ct_CdS)
def to_Omega(omega):
    return omega * D / (2 * math.pi * Ct_CdS)

# ---------- surface wave eigenvector selection for decays ----------
def select_decaying_eigenvectors(T, kD):
    """Return the eigenvectors (columns of V) corresponding to eigenvalues with |lambda|<1"""
    vals, vecs = np.linalg.eig(T)
    # choose those with |vals| < 1
    mask = np.abs(vals) < 1.0
    chosen_vals = vals[mask]
    chosen_vecs = vecs[:, mask]
    # sort by decreasing magnitude (optional)
    return chosen_vecs, chosen_vals

# ---------- surface determinant for CdS non-metallized (3x3) ----------
def surface_det_nonmetal(omega, kD):
    k_par = kD / D
    T = transfer_matrix(omega, k_par)
    vecs, vals = select_decaying_eigenvectors(T, kD)
    if vecs.shape[1] < 2:
        return 1e10  # no decaying solution
    # we need eigenvectors corresponding to two retained eigenvalues (as in paper)
    # here we take all decaying eigenvectors; in practice we need exactly 2.
    # For simplicity, if we have >2, pick two with smallest |val|? But the paper states exactly two have Im(k1)>0.
    # We'll assume that after selection we have exactly 2; if not, return large.
    if vecs.shape[1] != 2:
        return 1e10
    # The two eigenvectors are columns. For each r=1,2, compute coefficients P_n1, P_n2, Q_n1, Q_n2 from vecs.
    # Then evaluate D_1r, D_2r, D_3r from eq (2.19).
    h_s = h  # surface layer thickness same as bulk
    eps0 = 8.854187817e-12  # vacuum permittivity
    eps11 = eps11_CdS
    e15 = e15_CdS
    C44 = C44_CdS
    a = alpha(omega, C44_CdS, rho_CdS, e15_CdS, eps11_CdS, k_par)
    # evaluate functions
    def D1(P1,P2,Q1,Q2):
        sh1 = np.sinh(k_par * h_s)
        ch1 = np.cosh(k_par * h_s)
        sa = np.sinh(a * h_s)
        ca = np.cosh(a * h_s)
        return e15 * k_par * (P1 * sh1 + Q1 * ch1) + a * (C44 + e15**2/eps11) * (P2 * sa + Q2 * ca)
    def D2(P1,P2,Q1,Q2):
        sh1 = np.sinh(k_par * h_s)
        ch1 = np.cosh(k_par * h_s)
        return eps11 * k_par * (P1 * sh1 + Q1 * ch1)
    def D3(P1,P2,Q1,Q2):
        ch1 = np.cosh(k_par * h_s)
        sh1 = np.sinh(k_par * h_s)
        ca = np.cosh(a * h_s)
        sa = np.sinh(a * h_s)
        return P1 * ch1 + Q1 * sh1 + (e15/eps11) * (P2 * ca + Q2 * sa)

    mat = np.zeros((3,3), dtype=np.complex128)
    for r in range(2):
        P1 = vecs[0, r]
        P2 = vecs[1, r]
        Q1 = vecs[2, r]
        Q2 = vecs[3, r]
        mat[0, r] = D1(P1,P2,Q1,Q2)
        mat[1, r] = D2(P1,P2,Q1,Q2)
        mat[2, r] = D3(P1,P2,Q1,Q2)
    mat[0,2] = 0.0
    mat[1,2] = eps0 * k_par * np.exp(-k_par * h_s)
    mat[2,2] = -np.exp(-k_par * h_s)
    det = np.linalg.det(mat)
    return np.abs(det)

# ---------- surface determinant for metallized surface (2x2) ----------
def surface_det_metal(omega, kD, top_is_CdS=True):
    k_par = kD / D
    T = transfer_matrix(omega, k_par)
    vecs, vals = select_decaying_eigenvectors(T, kD)
    if vecs.shape[1] < 2:
        return 1e10
    if vecs.shape[1] != 2:
        return 1e10
    h_s = h
    if top_is_CdS:
        eps11 = eps11_CdS
        e15 = e15_CdS
        C44 = C44_CdS
        a = alpha(omega, C44_CdS, rho_CdS, e15_CdS, eps11_CdS, k_par)
    else:
        eps11 = eps11_ZnO
        e15 = e15_ZnO
        C44 = C44_ZnO
        a = alpha(omega, C44_ZnO, rho_ZnO, e15_ZnO, eps11_ZnO, k_par)
    
    def D1(P1,P2,Q1,Q2):
        sh1 = np.sinh(k_par * h_s)
        ch1 = np.cosh(k_par * h_s)
        sa = np.sinh(a * h_s)
        ca = np.cosh(a * h_s)
        return e15 * k_par * (P1 * sh1 + Q1 * ch1) + a * (C44 + e15**2/eps11) * (P2 * sa + Q2 * ca)
    def D2(P1,P2,Q1,Q2):
        sh1 = np.sinh(k_par * h_s)
        ch1 = np.cosh(k_par * h_s)
        return eps11 * k_par * (P1 * sh1 + Q1 * ch1)

    mat = np.zeros((2,2), dtype=np.complex128)
    for r in range(2):
        P1 = vecs[0, r]
        P2 = vecs[1, r]
        Q1 = vecs[2, r]
        Q2 = vecs[3, r]
        mat[0, r] = D1(P1,P2,Q1,Q2)
        mat[1, r] = D2(P1,P2,Q1,Q2)
    det = np.linalg.det(mat)
    return np.abs(det)

# ---------- compute surface velocity ----------
def compute_surface_velocity(kD, termination, boundary):
    """
    termination: 'CdS' or 'ZnO'
    boundary: 'nonmetal' or 'metal'
    returns dimensionless velocity v / Ct_CdS, or NaN if no solution.
    """
    # first get first band edge (lower_edge)
    edges = get_band_edges(kD)
    if len(edges) == 0:
        return float('nan')
    omega_max = edges[0][0]  # start of first band
    k_par = kD / D
    
    def det_fun(om):
        if termination == 'CdS':
            T = transfer_matrix(om, k_par)
            if boundary == 'nonmetal':
                return surface_det_nonmetal(om, kD)
            else:
                return surface_det_metal(om, kD, top_is_CdS=True)
        else:  # ZnO
            if boundary == 'metal':
                return surface_det_metal(om, kD, top_is_CdS=False)
            else:
                return float('nan')  # not required
    
    # search omega from 0.0 to omega_max for root
    omega_try = np.linspace(1e-9, omega_max, 5000)
    dets = np.array([det_fun(om) for om in omega_try])
    # find where det crosses zero (sign change)
    idx = np.where(np.diff(np.sign(dets)))[0]
    if len(idx) == 0:
        return float('nan')
    # take first crossing
    i = idx[0]
    lo = omega_try[i]
    hi = omega_try[i+1]
    for _ in range(30):
        mid = (lo+hi)/2
        if det_fun(mid)*det_fun(lo) > 0:
            lo = mid
        else:
            hi = mid
    omega_root = (lo+hi)/2
    # velocity = omega / k_par
    velocity = omega_root / k_par
    velocity_dimless = velocity / Ct_CdS
    return velocity_dimless

# ---------- effective constants ----------
def compute_effective_constants():
    x = 0.5  # equal thickness
    # compute for each layer: C55 (which is same as C44), e15, eps11
    def D(C44, e15, eps11):
        return C44 * eps11 + e15**2
    # averages of C55/D, eps11/D, e15/D
    val_CdS = (C44_CdS, e15_CdS, eps11_CdS)
    val_ZnO = (C44_ZnO, e15_ZnO, eps11_ZnO)
    def avg(f):
        return x * f(*val_CdS) + (1-x) * f(*val_ZnO)
    A1 = avg(lambda C44, e15, eps11: C44 / D(C44, e15, eps11))
    A2 = avg(lambda C44, e15, eps11: eps11 / D(C44, e15, eps11))
    A3 = avg(lambda C44, e15, eps11: e15 / D(C44, e15, eps11))
    D_eff = 1.0 / (A1 * A2 + A3**2)
    C44_eff = A1 * D_eff
    eps11_eff = A2 * D_eff
    e15_eff = A3 * D_eff
    return C44_eff, e15_eff, eps11_eff


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


# === block: score_0 (check id='bulk_band_scoring') ===
def score_0(artifact, step, ctx):
    import csv, io
    def score(artifact, step, ctx):
        # artifact is list of dicts from CSV
        if not artifact or len(artifact) < 2:
            return 0.0
        required = ['k_parallel_D','band1_lower','band1_upper','band2_lower','band2_upper']
        for field in required:
            if field not in artifact[0]:
                return 0.0
        rel_tol = step.get('tolerance_rel', 1e-4)
        ok = 0
        total = 0
        for row in artifact:
            try:
                kD = float(row['k_parallel_D'])
                b1l = float(row['band1_lower'])
                b1u = float(row['band1_upper'])
                b2l = float(row['band2_lower'])
                b2u = float(row['band2_upper'])
            except (ValueError, TypeError):
                continue
            # compute ground truth edges
            edges = get_band_edges(kD)
            if len(edges) < 2:
                # cannot compare; skip? treat as mismatch
                continue
            # first band
            ref_b1l = edges[0][0]
            ref_b1u = edges[0][1]
            ref_b2l = edges[1][0]
            ref_b2u = edges[1][1]
            # compare with relative tolerance
            def rel_diff(a,b):
                denom = max(abs(a), abs(b), 1e-12)
                return abs(a-b)/denom
            if (rel_diff(b1l, ref_b1l) <= rel_tol and
                rel_diff(b1u, ref_b1u) <= rel_tol and
                rel_diff(b2l, ref_b2l) <= rel_tol and
                rel_diff(b2u, ref_b2u) <= rel_tol):
                ok += 1
            total += 1
        if total == 0:
            return 0.0
        return ok / total
    return score(artifact, step, ctx)


# === block: score_1 (check id='surface_velocity_scoring') ===
def score_1(artifact, step, ctx):
    import csv, io
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 1:
            return 0.0
        required = ['k_parallel_D','velocity_CdS_nonmetal','velocity_CdS_metal','velocity_ZnO_metal']
        for f in required:
            if f not in artifact[0]:
                return 0.0
        rel_tol = step.get('tolerance_rel', 1e-4)
        ok = 0
        total = 0
        for row in artifact:
            try:
                kD = float(row['k_parallel_D'])
            except:
                continue
            # compute reference velocities
            ref_cds_metal = compute_surface_velocity(kD, 'CdS', 'metal')
            ref_cds_non = compute_surface_velocity(kD, 'CdS', 'nonmetal')
            ref_zno_metal = compute_surface_velocity(kD, 'ZnO', 'metal')
            # for each column, if agent value is NaN, skip; if reference is NaN, agent must also be NaN
            def check(agent_val, ref_val):
                if agent_val is None:
                    return False
                try:
                    av = float(agent_val)
                except:
                    return False
                if math.isnan(ref_val):
                    return math.isnan(av)
                denom = max(abs(av), abs(ref_val), 1e-12)
                return abs(av - ref_val) / denom <= rel_tol
        
            match = True
            for col, ref in [('velocity_CdS_nonmetal', ref_cds_non),
                             ('velocity_CdS_metal', ref_cds_metal),
                             ('velocity_ZnO_metal', ref_zno_metal)]:
                av = row.get(col)
                if not check(av, ref):
                    match = False
                    break
            if match:
                ok += 1
            total += 1
        if total == 0:
            return 0.0
        return ok / total
    return score(artifact, step, ctx)


# === block: score_2 (check id='effective_constants_scoring') ===
def score_2(artifact, step, ctx):
    import json

    def score(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        required = ['C44_eff','e15_eff','epsilon11_eff']
        for f in required:
            if f not in artifact:
                return 0.0
        abs_tol = step.get('tolerance_abs', {})
        # Compute reference effective constants as per instruction Step 3
        x = 0.5
        C44_eff_raw = x * C44_CdS + (1.0 - x) * C44_ZnO
        # 𝒟' for each material
        D_CdS = C44_CdS * eps11_CdS + e15_CdS ** 2
        D_ZnO = C44_ZnO * eps11_ZnO + e15_ZnO ** 2
        A = x * (e15_CdS / D_CdS) + (1 - x) * (e15_ZnO / D_ZnO)
        B = x * (eps11_CdS / D_CdS) + (1 - x) * (eps11_ZnO / D_ZnO)
        C_avg = x * (C44_CdS / D_CdS) + (1 - x) * (C44_ZnO / D_ZnO)
        D_eff = C44_eff_raw / C_avg
        e15_ref = A * D_eff
        eps11_ref_raw = B * D_eff   # F/m

        # Convert to expected units: C44_eff in 10^10 N/m², e15 in C/m², eps11 in 10⁻¹¹ F/m
        C44_ref = C44_eff_raw * 1e-10
        eps11_ref = eps11_ref_raw * 1e11

        try:
            C44_agent = float(artifact['C44_eff'])
            e15_agent = float(artifact['e15_eff'])
            eps11_agent = float(artifact['epsilon11_eff'])
        except Exception:
            return 0.0
        tol_C44 = abs_tol.get('C44_eff', 1e-3)
        tol_e15 = abs_tol.get('e15_eff', 1e-3)
        tol_eps11 = abs_tol.get('epsilon11_eff', 1e-3)
        ok = 0
        if abs(C44_agent - C44_ref) <= tol_C44:
            ok += 1
        if abs(e15_agent - e15_ref) <= tol_e15:
            ok += 1
        if abs(eps11_agent - eps11_ref) <= tol_eps11:
            ok += 1
        return ok / 3.0


_SCORERS = {
    'bulk_band_scoring': score_0,
    'surface_velocity_scoring': score_1,
    'effective_constants_scoring': score_2,
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
