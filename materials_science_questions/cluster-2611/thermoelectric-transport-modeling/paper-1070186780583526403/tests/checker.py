import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys, importlib

def _ensure_package(pkg, import_name=None):
    if import_name is None:
        import_name = pkg
    try:
        importlib.import_module(import_name)
    except ImportError:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir",
             "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", pkg]
        )

_ensure_package('numpy')
_ensure_package('scipy', 'scipy.interpolate')

import numpy as np
from scipy.interpolate import CubicSpline
from collections import defaultdict


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


# === block: score_0 (check id='step_01_mu_T') ===
def score_0(artifact, step, ctx):
    import numpy as np

    artifact = list(artifact)  # list of dicts
    if not artifact:
        return 0.0

    # Extract columns
    keys = ['temperature (K)', 'mu_n0=-3e18 (eV)', 'mu_n0=1e18 (eV)', 'mu_n0=3e18 (eV)']
    for k in keys:
        if k not in artifact[0]:
            return 0.0
    temps = np.array([float(r[keys[0]]) for r in artifact])
    mu_hole = np.array([float(r[keys[1]]) for r in artifact])
    mu_e1   = np.array([float(r[keys[2]]) for r in artifact])
    mu_e3   = np.array([float(r[keys[3]]) for r in artifact])

    # sort by temperature
    idx = np.argsort(temps)
    temps = temps[idx]
    mu_hole = mu_hole[idx]
    mu_e1 = mu_e1[idx]
    mu_e3 = mu_e3[idx]

    # Helper to compute slope via least squares
    def slope(x, y):
        A = np.vstack([x, np.ones(len(x))]).T
        m, _ = np.linalg.lstsq(A, y, rcond=None)[0]
        return m

    m_h = slope(temps, mu_hole)
    m_e1 = slope(temps, mu_e1)
    m_e3 = slope(temps, mu_e3)

    score = 0.0
    # Trend: hole-doped should increase (μ rises toward mid-gap)
    if m_h > 0:
        score += 0.2
    # Electron-doped should decrease (μ drops toward mid-gap)
    if m_e1 < 0:
        score += 0.2
    if m_e3 < 0:
        score += 0.2

    # Convergence at high T: at max T, spread < 0.05 eV
    max_T = np.max(temps)
    idx_max = np.argmax(temps)
    mu_last = [mu_hole[idx_max], mu_e1[idx_max], mu_e3[idx_max]]
    if max(mu_last) - min(mu_last) < 0.05:
        score += 0.2

    # Ordering at low T: electron μ > hole μ at min T
    idx_min = np.argmin(temps)
    mu_first = [mu_hole[idx_min], mu_e1[idx_min], mu_e3[idx_min]]
    if mu_e1[idx_min] > mu_hole[idx_min] and mu_e3[idx_min] > mu_hole[idx_min]:
        score += 0.2

    return min(score, 1.0)


# === block: score_1 (check id='step_02_zero_field') ===
def score_1(artifact, step, ctx):
    import numpy as np
    from scipy.interpolate import CubicSpline

    artifact = list(artifact)
    if not artifact:
        return 0.0

    keys = ['temperature (K)', 'rho_n0=-3e18 (μΩ·cm)', 'rho_n0=1e18 (μΩ·cm)', 'rho_n0=3e18 (μΩ·cm)']
    for k in keys:
        if k not in artifact[0]:
            return 0.0

    temps = np.array([float(r[keys[0]]) for r in artifact])
    rho_hole = np.array([float(r[keys[1]]) for r in artifact])
    rho_e1   = np.array([float(r[keys[2]]) for r in artifact])
    rho_e3   = np.array([float(r[keys[3]]) for r in artifact])

    # sort by temperature
    idx = np.argsort(temps)
    temps = temps[idx]
    rho_hole = rho_hole[idx]
    rho_e1 = rho_e1[idx]
    rho_e3 = rho_e3[idx]

    def find_peak(T, R):
        # cubic spline to locate max precisely
        cs = CubicSpline(T, R, bc_type='natural')
        T_dense = np.linspace(T[0], T[-1], 1000)
        R_dense = cs(T_dense)
        ipeak = np.argmax(R_dense)
        return T_dense[ipeak], R_dense[ipeak]

    peaks = {}
    for name, col in [('hole', rho_hole), ('e1', rho_e1), ('e3', rho_e3)]:
        Tp, Rp = find_peak(temps, col)
        peaks[name] = (Tp, Rp)

    score = 0.0
    # Each doping must show a clear peak (Tp in [50,250] K, Rp > 1.2*avg of endpoints)
    for name, col in [('hole', rho_hole), ('e1', rho_e1), ('e3', rho_e3)]:
        Tp, Rp = peaks[name]
        avg = (col[0] + col[-1]) / 2.0
        if 50 <= Tp <= 250 and Rp > avg * 1.2:
            score += 0.15  # total 0.45 for three peaks
        # else missing peak gets zero

    # Ordering: Tp_e1 < Tp_e3 < Tp_hole (as claimed)
    Tp_e1 = peaks['e1'][0]
    Tp_e3 = peaks['e3'][0]
    Tp_hole = peaks['hole'][0]
    if Tp_e1 + 3 < Tp_e3 and Tp_e3 + 3 < Tp_hole:
        score += 0.55
    elif Tp_e1 < Tp_e3 and Tp_e3 < Tp_hole:  # strict ordering but small gap
        score += 0.3
    # else ordering broken, score remains

    return min(score, 1.0)


# === block: score_2 (check id='step_03_hall') ===
def score_2(artifact, step, ctx):
    import numpy as np

    artifact = list(artifact)
    if not artifact:
        return 0.0

    required = ['B (T)', 'temperature (K)', 'rho_yx_n0=-3e18 (μΩ·cm)', 'rho_yx_n0=1e18 (μΩ·cm)', 'rho_yx_n0=3e18 (μΩ·cm)']
    for k in required:
        if k not in artifact[0]:
            return 0.0

    # organize by doping
    from collections import defaultdict

    def extract_rho(doping_key):
        temps = sorted(set(float(r['temperature (K)']) for r in artifact))
        result = {}
        for T in temps:
            rows = [r for r in artifact if abs(float(r['temperature (K)']) - T) < 1e-6]
            rows.sort(key=lambda r: float(r['B (T)']))
            B_vals = [float(r['B (T)']) for r in rows]
            R_vals = [float(r[doping_key]) for r in rows]
            result[T] = (B_vals, R_vals)
        return result

    hole_data = extract_rho('rho_yx_n0=-3e18 (μΩ·cm)')
    e1_data = extract_rho('rho_yx_n0=1e18 (μΩ·cm)')
    e3_data = extract_rho('rho_yx_n0=3e18 (μΩ·cm)')

    def has_sign_reversal(B, R):
        if R[0] * R[-1] < 0:
            return True
        for i in range(len(R)-1):
            if R[i] * R[i+1] <= 0:
                return True
        return False

    def any_sign_reversal(data_dict):
        for T, (B, R) in data_dict.items():
            if 50 <= T <= 200:
                if has_sign_reversal(B, R):
                    return True
        return False

    e1_rev = any_sign_reversal(e1_data)
    e3_rev = any_sign_reversal(e3_data)
    hole_rev = any_sign_reversal(hole_data)

    score = 0.0
    if e1_rev:
        score += 0.4
    if e3_rev:
        score += 0.4
    if not hole_rev:
        score += 0.2

    return min(score, 1.0)


# === block: score_3 (check id='step_04_mr') ===
def score_3(artifact, step, ctx):
    import numpy as np

    artifact = list(artifact)
    if not artifact:
        return 0.0

    required = ['B (T)', 'temperature (K)', 'MR_n0=-3e18 (dimensionless)', 'MR_n0=1e18 (dimensionless)', 'MR_n0=3e18 (dimensionless)']
    for k in required:
        if k not in artifact[0]:
            return 0.0

    def extract_mr(doping_key):
        temps = sorted(set(float(r['temperature (K)']) for r in artifact))
        result = {}
        for T in temps:
            rows = [r for r in artifact if abs(float(r['temperature (K)']) - T) < 1e-6]
            rows.sort(key=lambda r: float(r['B (T)']))
            B_vals = [float(r['B (T)']) for r in rows]
            R_vals = [float(r[doping_key]) for r in rows]
            result[T] = (B_vals, R_vals)
        return result

    hole_data = extract_mr('MR_n0=-3e18 (dimensionless)')
    e1_data = extract_mr('MR_n0=1e18 (dimensionless)')
    e3_data = extract_mr('MR_n0=3e18 (dimensionless)')

    def monotonic_at_T(data_dict, target_T=275):
        temps = sorted(data_dict.keys())
        # find closest T
        closest = min(temps, key=lambda x: abs(x - target_T))
        B, R = data_dict[closest]
        diffs = np.diff(R)
        if np.all(diffs >= -1e-6) and R[-1] > R[0] * 1.01:
            return True
        return False

    score = 0.0
    if monotonic_at_T(hole_data):
        score += 1/3
    if monotonic_at_T(e1_data):
        score += 1/3
    if monotonic_at_T(e3_data):
        score += 1/3

    return score


_SCORERS = {
    'step_01_mu_T': score_0,
    'step_02_zero_field': score_1,
    'step_03_hall': score_2,
    'step_04_mr': score_3,
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
