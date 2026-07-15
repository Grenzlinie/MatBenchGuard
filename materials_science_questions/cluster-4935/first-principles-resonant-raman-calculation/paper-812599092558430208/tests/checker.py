import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d
import json, csv, os, math

# ----------------------------------------------------------------------
# Model parameters (fixed in the task)
# ----------------------------------------------------------------------
OMEGA_O = 1.0
R = 0.15
OMEGA_V = OMEGA_O - R/2       # 0.925
OMEGA_C = OMEGA_O + R/2       # 1.075
DELTA = 2 * (R/2)             # 0.15
OMEGA10 = DELTA/10            # 0.015
GAMMA20 = DELTA/100           # 0.0015
GAMMA21 = DELTA/100
# omega20 for bound state
OMEGA20_BOUND = 0.95 * OMEGA_C   # 1.02125
# omega20 for spectra
OMEGA20_SPEC = 1.2 * OMEGA_C    # 1.29
# omega21 list
OMEGA21_LIST = [1.15*OMEGA_C, 1.05*OMEGA_C, OMEGA_C, OMEGA_O]   # [1.23625,1.12875,1.075,1.0]
FDMA_KAPPA = 0.001
DETUNING_GRID = np.linspace(-0.5, 0.5, 1001)

# ----------------------------------------------------------------------
# Atomic form factors
# ----------------------------------------------------------------------
def z_pbg(w):
    if OMEGA_V <= w <= OMEGA_C:
        return 0.0
    # outside gap
    arg = (w - OMEGA_V)*(w - OMEGA_C)
    arg = max(arg, 0.0)
    return abs(w - OMEGA_O) / np.sqrt(arg)

def z_fdm(w):
    if OMEGA_V <= w <= OMEGA_C:
        return 0.0
    num = w*w - 2*OMEGA_V*w + OMEGA_V*OMEGA_C
    den = (w - OMEGA_V)**2 + FDMA_KAPPA**2
    return num / den

# ----------------------------------------------------------------------
# Self-energy Σ_S′(ω) for the Stokes channel (Eq. 52a)
# We compute  γ21 * P ∫_{C∞} (z(w)-1)/(w - ω + ω21) dw
# to ensure convergence, using a small imaginary shift ε.
# ----------------------------------------------------------------------
EPS = 1e-6

def sigma_s_prime_pbg(omega, omega21):
    a = omega - omega21
    # Transformation for [0, OMEGA_V] to handle √ singularity at OMEGA_V
    def integrand_real1(w):
        zw = z_pbg(w)
        return (zw - 1.0) * (w - a) / ((w - a)**2 + EPS**2)
    # standard integration for upper branch
    def integrand_real2(w):
        zw = z_pbg(w)
        return (zw - 1.0) * (w - a) / ((w - a)**2 + EPS**2)

    # lower interval: integrate analytically with substitution u = sqrt(OMEGA_V - w)
    # Improve robustness: use quad on transformed domain or standard quad with points
    # We'll use a simple method: integrate from 0 to OMEGA_V using points at OMEGA_V
    I1, _ = quad(integrand_real1, 0, OMEGA_V, limit=200, epsabs=1e-14, epsrel=1e-8, points=[OMEGA_V])
    # upper interval: from OMEGA_C to inf, handle sqrt singularity at OMEGA_C
    I2, _ = quad(integrand_real2, OMEGA_C, np.inf, limit=200, epsabs=1e-14, epsrel=1e-8, points=[OMEGA_C])
    return GAMMA21 * (I1 + I2)

def sigma_s_prime_fdm(omega, omega21):
    a = omega - omega21
    def integrand_real(w):
        zw = z_fdm(w)
        return (zw - 1.0) * (w - a) / ((w - a)**2 + EPS**2)
    I1, _ = quad(integrand_real, 0, OMEGA_V, limit=200, epsabs=1e-14, epsrel=1e-8)
    I2, _ = quad(integrand_real, OMEGA_C, np.inf, limit=200, epsabs=1e-14, epsrel=1e-8)
    return GAMMA21 * (I1 + I2)

# ----------------------------------------------------------------------
# sigma_S double prime (Eq. 52b)
# ----------------------------------------------------------------------
def sigma_s_double_prime(z_func, omega):
    w_s = omega - OMEGA10
    return 0.5 * GAMMA21 * z_func(w_s)

# ----------------------------------------------------------------------
# Reference Rayleigh cross-section (Eq. 53) for given ω21 and medium
# ----------------------------------------------------------------------
def reference_spectrum(omega21, medium, omega_grid):
    if medium == 'pbg':
        zf = z_pbg
        sigma_prime_fn = sigma_s_prime_pbg
    else:
        zf = z_fdm
        sigma_prime_fn = sigma_s_prime_fdm

    ref = []
    for omega in omega_grid:
        z_w = zf(omega)
        if z_w == 0.0:
            # inside gap, sigma_R = 0
            ref.append(0.0)
        else:
            sp = sigma_prime_fn(omega, omega21)
            sdp = sigma_s_double_prime(zf, omega)
            den = (OMEGA20_SPEC - omega - sp)**2 + (GAMMA20 + 2*sdp)**2 / 4.0
            val = z_w**2 / den
            ref.append(val)
    return np.array(ref)

# ----------------------------------------------------------------------
# Scoring helper for a single ω21
# ----------------------------------------------------------------------
def score_one_spectrum(agent_detunings, agent_sig, omega21, ref_grid, ref_sig):
    if len(agent_detunings) < 5:
        return 0.0
    # interpolate agent onto reference detuning grid
    try:
        interp = interp1d(np.asarray(agent_detunings), np.asarray(agent_sig), kind='linear', bounds_error=False, fill_value=0.0)
        ag = interp(ref_grid)
    except Exception:
        return 0.0
    # optimal scaling factor
    mask = ref_sig > 1e-30
    if not np.any(mask):
        ref_norm = 0.0
        return 0.0
    # avoid zero scaling
    if np.sum(ag**2) < 1e-30:
        return 0.0
    k = np.sum(ref_sig[mask] * ag[mask]) / np.sum(ag[mask]**2)
    scaled = k * ag
    # relative L2 error
    err = np.sqrt(np.sum((scaled[mask] - ref_sig[mask])**2))
    ref_l2 = np.sqrt(np.sum(ref_sig[mask]**2))
    if ref_l2 < 1e-30:
        return 0.0
    rel_err = err / ref_l2
    # threshold_or_better: 1.0 if rel_err <= tol, linearly fall to 0 at rel_err = 3*tol
    tol = 0.15
    if rel_err <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (rel_err - tol) / (2*tol))


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
    params = {
        'omega21_list': OMEGA21_LIST,
        'eigen_tol_abs': 0.01,
        'ref_pbg': {},
        'ref_fdm': {},
        'detuning_grid': DETUNING_GRID
    }

    # ----------------------------------------------------------------------
    # Robust self-energy implementations (local copies to avoid global defects)
    # ----------------------------------------------------------------------
    EPS_LOCAL = 1e-6

    def _sigma_s_prime_pbg(omega, omega21):
        a = omega - omega21
        # lower branch [0, OMEGA_V] – finite interval, points is allowed
        def f1(w):
            zw = z_pbg(w)
            return (zw - 1.0) * (w - a) / ((w - a)**2 + EPS_LOCAL**2)
        I1, _ = quad(f1, 0, OMEGA_V, limit=200, epsabs=1e-14, epsrel=1e-8, points=[OMEGA_V])
        # upper branch [OMEGA_C, inf) – no points argument to avoid ValueError
        def f2(w):
            zw = z_pbg(w)
            return (zw - 1.0) * (w - a) / ((w - a)**2 + EPS_LOCAL**2)
        I2, _ = quad(f2, OMEGA_C, np.inf, limit=200, epsabs=1e-14, epsrel=1e-8)
        return GAMMA21 * (I1 + I2)

    def _sigma_s_prime_fdm(omega, omega21):
        a = omega - omega21
        def f(w):
            zw = z_fdm(w)
            return (zw - 1.0) * (w - a) / ((w - a)**2 + EPS_LOCAL**2)
        I1, _ = quad(f, 0, OMEGA_V, limit=200, epsabs=1e-14, epsrel=1e-8)
        I2, _ = quad(f, OMEGA_C, np.inf, limit=200, epsabs=1e-14, epsrel=1e-8)
        return GAMMA21 * (I1 + I2)

    def _sigma_s_double_prime(z_func, omega):
        w_s = omega - OMEGA10
        return 0.5 * GAMMA21 * z_func(w_s)

    def _reference_spectrum(omega21, medium, omega_grid):
        if medium == 'pbg':
            zf = z_pbg
            sigma_prime_fn = _sigma_s_prime_pbg
        else:
            zf = z_fdm
            sigma_prime_fn = _sigma_s_prime_fdm
        ref = []
        for omega in omega_grid:
            z_w = zf(omega)
            if z_w == 0.0:
                ref.append(0.0)
            else:
                sp = sigma_prime_fn(omega, omega21)
                sdp = _sigma_s_double_prime(zf, omega)
                den = (OMEGA20_SPEC - omega - sp)**2 + (GAMMA20 + 2*sdp)**2 / 4.0
                val = z_w**2 / den
                ref.append(val)
        return np.array(ref)

    # ----------------------------------------------------------------------
    # Compute reference spectra
    # ----------------------------------------------------------------------
    for w21 in OMEGA21_LIST:
        params['ref_pbg'][w21] = _reference_spectrum(w21, 'pbg', DETUNING_GRID)
        params['ref_fdm'][w21] = _reference_spectrum(w21, 'fdm', DETUNING_GRID)
    return params


# === block: score_0 (check id='bound_state_result') ===
def score_0(artifact, step, ctx):
    # Check PBG bound state: expect exists, eigenvalue near 1.02
    # FDM: no bound state
    art = artifact  # dict
    score_pbg = 0.0
    if art.get('pbg_bound_state_exists') is True:
        eig = art.get('pbg_eigenvalue')
        if eig is not None and isinstance(eig, (int, float)):
            if abs(eig - 1.02) <= ctx['eigen_tol_abs']:
                score_pbg = 1.0
            else:
                score_pbg = max(0.0, 1.0 - 2*abs(eig-1.02)/ctx['eigen_tol_abs'])
        else:
            score_pbg = 0.3  # correct flag but no value
    else:
        # agent says no PBG bound state: 0
        pass

    score_fdm = 1.0 if (art.get('fdm_bound_state_exists') is False) else 0.0

    return 0.5*score_pbg + 0.5*score_fdm


# === block: score_1 (check id='rayleigh_spectrum_pbg') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    # group by omega21
    grouped = {}
    for row in artifact:
        try:
            det = float(row['omega_minus_omega20'])
            w21 = float(row['omega21'])
            sig = float(row['sigma_R'])
            grouped.setdefault(w21, ([], []))[0].append(det)
            grouped[w21][0].append(sig)
        except:
            continue
    ref = ctx['ref_pbg']
    det_grid = ctx['detuning_grid']
    scores = []
    for w21 in OMEGA21_LIST:
        if w21 in grouped:
            dets, sigs = grouped[w21]
            s = score_one_spectrum(dets, sigs, w21, det_grid, ref[w21])
            scores.append(s)
        else:
            scores.append(0.0)
    return float(np.mean(scores))


# === block: score_2 (check id='rayleigh_spectrum_fdm') ===
def score_2(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    grouped = {}
    for row in artifact:
        try:
            det = float(row['omega_minus_omega20'])
            w21 = float(row['omega21'])
            sig = float(row['sigma_R'])
            grouped.setdefault(w21, ([], []))[0].append(det)
            grouped[w21][0].append(sig)
        except:
            continue
    ref = ctx['ref_fdm']
    det_grid = ctx['detuning_grid']
    scores = []
    for w21 in OMEGA21_LIST:
        if w21 in grouped:
            dets, sigs = grouped[w21]
            s = score_one_spectrum(dets, sigs, w21, det_grid, ref[w21])
            scores.append(s)
        else:
            scores.append(0.0)
    return float(np.mean(scores))


_SCORERS = {
    'bound_state_result': score_0,
    'rayleigh_spectrum_pbg': score_1,
    'rayleigh_spectrum_fdm': score_2,
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
