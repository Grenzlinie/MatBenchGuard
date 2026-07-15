import os
import json
import csv

# === author imports / helpers ===
import numpy as np

# Conversion factor: (rad/s) to THz  (1 THz = 2*pi*1e12 rad/s??)
# Actually, angular frequency omega (rad/s) to f (THz): f = omega / (2*pi*1e12)
# Let's verify: 1 THz = 10^12 Hz => 2*pi*10^12 rad/s. So omega to THz: omega / (2*pi*1e12)
# The paper uses omega (rad/s) implicitly; the original code had CONV_THZ = 6579.68 which seems wrong.
# We'll define conversion from omega (a.u.)? Actually, the computation uses atomic units: length = bohr, energy = Hartree, mass = electron mass.
# The dynamical matrix units: [D] = energy/length^2; sqrt(D/M) gives omega in atomic units (1 a.u. = 4.13413e16 rad/s).
# 1 THz = 1e12 * 2*pi rad/s = 2*pi*1e12 rad/s. So 1 a.u. = 4.13413e16 / (2*pi*1e12) = 6579.68 THz. So CONV_THZ = 6579.68 is correct.
CONV_THZ = 6579.68

# Parameters for pure alkali metals (Z, Omega0 [bohr^3], rC [bohr], M_amu)
PURE_DATA = {
    'Li': {'Z': 1, 'Omega0': 143.8, 'rC': 0.7738, 'M_amu': 6.94},
    'Na': {'Z': 1, 'Omega0': 254.45, 'rC': 1.2182, 'M_amu': 22.99},
    'K':  {'Z': 1, 'Omega0': 482.5, 'rC': 1.4031, 'M_amu': 39.10},
    'Rb': {'Z': 1, 'Omega0': 587.5, 'rC': 1.7880, 'M_amu': 85.47},
    'Cs': {'Z': 1, 'Omega0': 747.0, 'rC': 1.9108, 'M_amu': 132.9}
}

M_E_PER_AMU = 1822.888  # electron mass in amu

def fermi_wavevector(Z, Omega0):
    return (3*np.pi**2 * Z / Omega0)**(1/3)

def alloy_params(matA, matB, x=0.5):
    pA = PURE_DATA[matA]
    pB = PURE_DATA[matB]
    Z     = (1-x)*pA['Z']     + x*pB['Z']
    Omega0= (1-x)*pA['Omega0']+ x*pB['Omega0']
    rC    = (1-x)*pA['rC']    + x*pB['rC']
    M_amu = (1-x)*pA['M_amu'] + x*pB['M_amu']
    kF    = (1-x)*fermi_wavevector(pA['Z'], pA['Omega0']) + x*fermi_wavevector(pB['Z'], pB['Omega0'])
    return {'Z': Z, 'Omega0': Omega0, 'rC': rC, 'M_amu': M_amu, 'kF': kF}

# All materials dict
MATERIALS = {}
for m in ['Li','Na','K','Rb','Cs']:
    p = PURE_DATA[m]
    kF = fermi_wavevector(p['Z'], p['Omega0'])
    MATERIALS[m] = {'Z': p['Z'], 'Omega0': p['Omega0'], 'rC': p['rC'], 'M_amu': p['M_amu'], 'kF': kF}
ALLOY_PAIRS = [('Na','Li'), ('Na','K'), ('Na','Rb'), ('Na','Cs')]
for A, B in ALLOY_PAIRS:
    name = f"Na0.5{A}0.5"
    MATERIALS[name] = alloy_params(A, B, x=0.5)

def generate_bcc_shells(a, max_shells=33):
    """Return list of (distance, (rx,ry,rz)) for up to max_shells nearest neighbours."""
    N = 5
    shells = {}
    for n1 in range(-N, N+1):
        for n2 in range(-N, N+1):
            for n3 in range(-N, N+1):
                x = a/2 * (-n1 + n2 + n3)
                y = a/2 * ( n1 - n2 + n3)
                z = a/2 * ( n1 + n2 - n3)
                dist = np.sqrt(x*x + y*y + z*z)
                if dist == 0:
                    continue
                if dist not in shells:
                    shells[dist] = (x, y, z)
    sorted_dists = sorted(shells.keys())
    return [(d, shells[d]) for d in sorted_dists[:max_shells]]

# --- Vectorized screening and pseudopotential functions (handles scalar or array q) ---
def _safe_trapz(y, x):
    """Trapezoidal integration, robust to numpy version."""
    # np.trapezoid is available in numpy >=2.0, np.trapz deprecated.
    if hasattr(np, 'trapezoid'):
        return np.trapezoid(y, x)
    try:
        return np.trapz(y, x)
    except AttributeError:
        # manual fallback
        dx = np.diff(x)
        yavg = (y[:-1] + y[1:]) / 2.0
        return np.sum(yavg * dx)

def epsilon_H(q, kF):
    """Static Hartree dielectric function (Lindhard). Works for scalar or 1D array q."""
    q = np.asarray(q, dtype=float)
    scalar = q.ndim == 0
    if scalar:
        q = q.reshape(1)
    eps = np.empty_like(q)
    kTF2 = 4 * kF / np.pi
    for i in range(len(q)):
        qi = q[i]
        if qi == 0.0:
            eps[i] = 1e16
            continue
        eta = qi / (2 * kF)
        if eta < 1e-8:
            u = 0.5
        else:
            u = 0.5 + (1 - eta**2) / (4*eta) * np.log(np.abs((1+eta)/(1-eta)))
        eps[i] = 1.0 + kTF2 * u / (qi**2)
    if scalar:
        return eps[0]
    return eps

def f_IU(q, kF):
    """Simplified Ichimaru-Utsumi local field correction (inline in grading spec)."""
    q = np.asarray(q, dtype=float)
    return q**2 / (2 * (q**2 + kF**2))

def V_Gajjar(q, Z, Omega0, rC):
    """Gajjar empty-core pseudopotential. Works for scalar or array q."""
    q = np.asarray(q, dtype=float)
    q_safe = np.where(q == 0, 1e-12, q)  # avoid division by zero
    qrC = q_safe * rC
    term = np.cos(qrC) - (qrC**2) / (1 + qrC**2)
    V = (-8 * np.pi * Z / (Omega0 * q_safe**2)) * term
    # exact q=0 gives 0 limit
    V = np.where(q == 0, 0.0, V)
    return V

def F_q(q_vals, mat, screening):
    """Energy wave-number characteristic F(q)."""
    Z = mat['Z']
    Omega0 = mat['Omega0']
    rC = mat['rC']
    kF = mat['kF']
    V = V_Gajjar(q_vals, Z, Omega0, rC)
    eps = epsilon_H(q_vals, kF)
    if screening == 'IU':
        f = f_IU(q_vals, kF)
    else:
        f = np.zeros_like(q_vals)
    denominator = 1 + (eps - 1) * (1 - f)
    F = (Omega0 * q_vals**2 / (8 * np.pi)) * (eps - 1) / denominator
    return F

def compute_tangential_radial_force_constants(mat, shells, screening):
    Z = mat['Z']
    Omega0 = mat['Omega0']
    kF = mat['kF']
    qmax = 40 * kF
    Nq = 3000
    q_grid = np.linspace(1e-8, qmax, Nq)
    F_vals = F_q(q_grid, mat, screening)
    Kt_list = []
    Kr_list = []
    for r, _ in shells:
        qr = q_grid * r
        sin_qr = np.sin(qr)
        cos_qr = np.cos(qr)
        # Integrand for Kt
        term_t = cos_qr - sin_qr / qr
        integrand_t = F_vals * q_grid**2 * term_t
        I_t = _safe_trapz(integrand_t, q_grid)
        Kt = -Z**2 / (r**3) + (Omega0 / (np.pi**2 * r**2)) * I_t
        # Integrand for Kr
        term_r = (2*sin_qr/qr) - 2*cos_qr - qr*sin_qr
        integrand_r = F_vals * q_grid**2 * term_r
        I_r = _safe_trapz(integrand_r, q_grid)
        Kr = 2*Z**2/(r**3) + (Omega0 / (np.pi**2 * r**2)) * I_r
        Kt_list.append(Kt)
        Kr_list.append(Kr)
    return np.array(Kt_list), np.array(Kr_list)

def dynamical_matrix(q_vec, shells, Kt, Kr):
    D = np.zeros((3,3), dtype=complex)
    for idx, (dist, rv) in enumerate(shells):
        r = dist
        rx, ry, rz = rv
        r_vec = np.array([rx, ry, rz])
        phase = np.exp(1j * np.dot(q_vec, r_vec))
        factor = (1 - phase)
        kt = Kt[idx]
        kr = Kr[idx]
        for alpha in range(3):
            for beta in range(3):
                D[alpha, beta] += factor * (kt + (r_vec[alpha]*r_vec[beta])/(r*r) * (kr - kt))
    return D

def compute_frequencies(mat, direction_label, q_red_array, screening='H'):
    Z = mat['Z']
    Omega0 = mat['Omega0']
    a = (2*Omega0)**(1/3)
    M = mat['M_amu'] * M_E_PER_AMU
    shells = generate_bcc_shells(a, max_shells=33)
    Kt_vals, Kr_vals = compute_tangential_radial_force_constants(mat, shells, screening)
    if direction_label == '100':
        q_dir = np.array([1.0, 0.0, 0.0])
    elif direction_label == '110':
        q_dir = np.array([1.0, 1.0, 0.0]) / np.sqrt(2)
    elif direction_label == '111':
        q_dir = np.array([1.0, 1.0, 1.0]) / np.sqrt(3)
    else:
        raise ValueError("Invalid direction")
    freq_L, freq_T1, freq_T2 = [], [], []
    for q_red in q_red_array:
        q = q_red * (2*np.pi/a) * q_dir
        D = dynamical_matrix(q, shells, Kt_vals, Kr_vals)
        eigvals = np.sort(np.linalg.eigvalsh(D.real))
        omega = np.sqrt(np.maximum(eigvals, 0.0) / M)
        freq_THz = omega * CONV_THZ
        freq_L.append(freq_THz[2])
        freq_T1.append(freq_THz[1])
        freq_T2.append(freq_THz[0])
    return np.array(freq_L), np.array(freq_T1), np.array(freq_T2)


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
        # step parameters
        steps = spec.get('steps', [])
        step_params = steps[0].get('parameters', {}) if steps else {}
        pure_mape_full = step_params.get('pure_mape_full_credit', 0.01)
        pure_mape_zero = step_params.get('pure_mape_zero_credit', 0.05)
        alloy_mape_full = step_params.get('alloy_mape_full_credit', 0.03)
        alloy_mape_zero = step_params.get('alloy_mape_zero_credit', 0.10)
        # Precompute Hartree reference phonon frequencies on a uniform grid
        ref_data = {}
        q_grid_uniform = np.linspace(0, 1, 100)
        directions = ['100', '110', '111']
        for mat_name, matd in MATERIALS.items():
            ref_data[mat_name] = {}
            for d in directions:
                L, T1, T2 = compute_frequencies(matd, d, q_grid_uniform, screening='H')
                ref_data[mat_name][d] = {'q': q_grid_uniform.copy(), 'L': L, 'T1': T1, 'T2': T2}
        return {
            'ref_data': ref_data,
            'pure_mape_full': pure_mape_full,
            'pure_mape_zero': pure_mape_zero,
            'alloy_mape_full': alloy_mape_full,
            'alloy_mape_zero': alloy_mape_zero
        }


# === block: score_0 (check id='phonon_dispersion_scoring') ===
def score_0(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        required_materials = list(MATERIALS.keys())
        required_dirs = ['100','110','111']
        required_screenings = ['H','IU']
        # minimum 50 points per material/direction/screening
        counts = {}
        for row in rows:
            key = (row['material'], row['direction'], row['screening'])
            counts[key] = counts.get(key, 0) + 1
        for mat in required_materials:
            for d in required_dirs:
                for scr in required_screenings:
                    if counts.get((mat, d, scr), 0) < 50:
                        return 0.0
        ref_data = ctx['ref_data']
        pure_mape_full = ctx['pure_mape_full']
        pure_mape_zero = ctx['pure_mape_zero']
        alloy_mape_full = ctx['alloy_mape_full']
        alloy_mape_zero = ctx['alloy_mape_zero']
        h_rows = [r for r in rows if r['screening'] == 'H']
        iu_rows = [r for r in rows if r['screening'] == 'IU']
        # MAPE for Hartree rows
        pure_ape_sum = 0.0
        pure_count = 0
        alloy_ape_sum = 0.0
        alloy_count = 0
        for r in h_rows:
            mat = r['material']
            direc = r['direction']
            q_red = float(r['q_reduced'])
            branch = r['branch']
            freq = float(r['frequency'])
            if mat not in ref_data or direc not in ref_data[mat]:
                return 0.0
            ref = ref_data[mat][direc]
            q_ref = ref['q']
            if branch == 'L':
                ref_vals = ref['L']
            elif branch == 'T1':
                ref_vals = ref['T1']
            else:
                ref_vals = ref['T2']
            ref_freq = np.interp(q_red, q_ref, ref_vals)
            if ref_freq == 0:
                continue
            ape = abs(freq - ref_freq) / ref_freq
            if mat in ['Li','Na','K','Rb','Cs']:
                pure_ape_sum += ape
                pure_count += 1
            else:
                alloy_ape_sum += ape
                alloy_count += 1
        if pure_count > 0:
            pure_mape = pure_ape_sum / pure_count
        else:
            pure_mape = 0.0
            pure_count = 1
        if alloy_count > 0:
            alloy_mape = alloy_ape_sum / alloy_count
        else:
            alloy_mape = 0.0
            alloy_count = 1
        if pure_mape <= pure_mape_full:
            score_pure = 1.0
        elif pure_mape >= pure_mape_zero:
            score_pure = 0.0
        else:
            score_pure = 1.0 - (pure_mape - pure_mape_full) / (pure_mape_zero - pure_mape_full)
        if alloy_mape <= alloy_mape_full:
            score_alloy = 1.0
        elif alloy_mape >= alloy_mape_zero:
            score_alloy = 0.0
        else:
            score_alloy = 1.0 - (alloy_mape - alloy_mape_full) / (alloy_mape_zero - alloy_mape_full)
        total_h = pure_count + alloy_count
        if total_h > 0:
            mape_score = (pure_count * score_pure + alloy_count * score_alloy) / total_h
        else:
            mape_score = 0.0
        # IU structural check: longitudinal branch suppression
        h_L_dict = {}
        for r in h_rows:
            if r['branch'] == 'L':
                key = (r['material'], r['direction'], float(r['q_reduced']))
                h_L_dict[key] = float(r['frequency'])
        iu_compliant = 0
        iu_total = 0
        for r in iu_rows:
            if r['branch'] == 'L':
                key = (r['material'], r['direction'], float(r['q_reduced']))
                freq_iu = float(r['frequency'])
                if key in h_L_dict:
                    freq_h = h_L_dict[key]
                    iu_total += 1
                    if freq_iu <= 1.02 * freq_h:
                        iu_compliant += 1
        iu_score = iu_compliant / iu_total if iu_total > 0 else 0.0
        weight_mape = 0.8
        weight_iu = 0.2
        final = weight_mape * mape_score + weight_iu * iu_score
        return float(final)


_SCORERS = {
    'phonon_dispersion_scoring': score_0,
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
