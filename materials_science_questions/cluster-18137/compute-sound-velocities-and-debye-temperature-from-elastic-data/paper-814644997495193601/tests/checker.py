import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import os, csv, math
from collections import defaultdict

try:
    from scipy.optimize import fsolve as _scipy_fsolve
    def _fsolve(f, x0, **kwargs):
        return _scipy_fsolve(f, x0, **kwargs)
except ImportError:
    # Fallback: simple bisection root‑finder for Debye‑temperature step.
    def _fsolve(f, x0, maxiter=100, tol=1e-8):
        a, b = 0.1, 2000.0           # Θ ∈ (0, 2000) K
        fa = f(a)
        fb = f(b)
        if fa * fb > 0:
            # No sign change: return x0 as best guess.
            return [x0]
        for _ in range(maxiter):
            c = (a + b) / 2.0
            fc = f(c)
            if abs(fc) < tol or (b - a) / 2.0 < tol:
                return [c]
            if fa * fc < 0:
                b, fb = c, fc
            else:
                a, fa = c, fc
        return [x0]

# Provide a global `fsolve` alias so existing scorer code works unchanged.
fsolve = _fsolve


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
    return {'outputs_dir': outputs_dir}


# === block: score_0 (check id='step1_dispersion') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact  # list of dicts
    if not artifact_rows:
        return 0.0
    qpoint_groups = defaultdict(list)
    for row in artifact_rows:
        qx = round(float(row['q_x']), 3)
        qz = round(float(row['q_z']), 3)
        qpoint_groups[(qx, qz)].append(float(row['frequency']))
    n_q = len(qpoint_groups)
    if n_q == 0:
        return 0.0
    ok = 0
    total_checks = 0
    for q, freqs in qpoint_groups.items():
        if len(freqs) != 18:
            continue
        if min(freqs) < -0.01:
            continue
        if abs(q[0]) < 1e-3 and abs(q[1]) < 1e-3:
            sorted_f = sorted(freqs)
            ok += 1.0 if sorted_f[2] < 0.2 else 0.5
        else:
            ok += 1.0
        total_checks += 1
    score = ok / total_checks if total_checks else 0.0
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='step2_dos') ===
def score_1(artifact, step, ctx):
    fre = np.array([float(r['frequency']) for r in artifact])
    dos = np.array([float(r['dos']) for r in artifact])
    if len(fre) < 2:
        return 0.0
    bin_width = fre[1] - fre[0]
    total = np.sum(dos) * bin_width
    integral_score = max(0.0, 1.0 - abs(total - 18.0) / 2.0)
    max_dos_freq = fre[np.argmax(dos)]
    peak_in_window1 = 7.0 <= max_dos_freq <= 9.5
    peak_in_window2 = 10.0 <= max_dos_freq <= 12.5
    peak_score = 1.0 if (peak_in_window1 or peak_in_window2) else 0.0
    score = 0.5 * integral_score + 0.5 * peak_score
    return max(0.0, min(1.0, score))


# === block: score_2 (check id='step3_cv') ===
def score_2(artifact, step, ctx):
    outputs_dir = ctx.get('outputs_dir', '/app/outputs')
    dos_path = os.path.join(outputs_dir, 'phonon_dos.csv')
    dos_artifact = None
    with open(dos_path, newline='') as f:
        dos_artifact = list(csv.DictReader(f))
    if not dos_artifact:
        return 0.0
    fre_dos = np.array([float(r['frequency']) for r in dos_artifact])
    dos_vals = np.array([float(r['dos']) for r in dos_artifact])
    h = 6.62607015e-34
    kB = 1.380649e-23
    NA = 6.02214076e23
    R = 8.314462618
    n_fu_per_cell = 2  # MoS2 formula units per primitive cell

    def compute_cv_at_T(T):
        nu = fre_dos * 1e12   # THz -> Hz
        x = h * nu / (kB * T)
        x_clip = np.clip(x, 0, 500)
        exp_x = np.exp(x_clip)
        term = np.where(x_clip < 1e-10, 0.0, (x_clip**2 * exp_x) / (exp_x - 1)**2)
        # integral over frequency in Hz
        integrand = dos_vals / 1e12 * term
        integ = np.trapz(integrand, nu)
        Cv_cell = kB * integ   # J/K per primitive cell
        Cv_mol = Cv_cell * NA / n_fu_per_cell   # J/(mol·K) per formula unit
        return Cv_mol

    T_agent = np.array([float(r['temperature']) for r in artifact])
    Cv_agent = np.array([float(r['Cv']) for r in artifact])
    Cv_ref = np.array([compute_cv_at_T(T) for T in T_agent])
    diff = np.abs(Cv_agent - Cv_ref)
    tol = 0.5  # J/(mol·K)
    pass_count = np.sum(diff <= tol)
    score = pass_count / len(diff) if len(diff) > 0 else 0.0
    return max(0.0, min(1.0, score))


# === block: score_3 (check id='step4_thetad') ===
def score_3(artifact, step, ctx):
    outputs_dir = ctx.get('outputs_dir', '/app/outputs')
    cv_path = os.path.join(outputs_dir, 'specific_heat.csv')
    cv_artifact = None
    with open(cv_path, newline='') as f:
        cv_artifact = list(csv.DictReader(f))
    if not cv_artifact:
        return 0.0
    R = 8.314462618

    def debye_cv(T, theta):
        if theta <= 0:
            return 0.0
        x_max = theta / T
        xs = np.linspace(0, x_max, 100)
        dx = xs[1] - xs[0]
        integrand = xs**4 * np.exp(xs) / (np.exp(xs)-1)**2
        integ = np.trapz(integrand, xs)
        return 9 * R * (T/theta)**3 * integ

    def theta_from_cv(Cv, T):
        if Cv <= 0:
            return 0.0
        def f(th):
            return debye_cv(T, th) - Cv
        guess = 200.0
        sol = fsolve(f, guess, maxfev=1000)
        return sol[0] if sol[0] > 0 else 0.0

    T_agent = np.array([float(r['temperature']) for r in artifact])
    theta_agent = np.array([float(r['Debye_temperature']) for r in artifact])
    # Match Cv values by same temperature
    T_cv = np.array([float(r['temperature']) for r in cv_artifact])
    Cv_cv = np.array([float(r['Cv']) for r in cv_artifact])
    theta_recomp = []
    for i, T in enumerate(T_agent):
        idx = np.argmin(np.abs(T_cv - T))
        Cv_val = Cv_cv[idx]
        theta_recomp.append(theta_from_cv(Cv_val, T))
    theta_recomp = np.array(theta_recomp)
    diff = np.abs(theta_agent - theta_recomp)
    tol = 10.0
    pass_count = np.sum(diff <= tol)
    score = pass_count / len(diff) if len(diff) > 0 else 0.0
    return max(0.0, min(1.0, score))


_SCORERS = {
    'step1_dispersion': score_0,
    'step2_dos': score_1,
    'step3_cv': score_2,
    'step4_thetad': score_3,
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
