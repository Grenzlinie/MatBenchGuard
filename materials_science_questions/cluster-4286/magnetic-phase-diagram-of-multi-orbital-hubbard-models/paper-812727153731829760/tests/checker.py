import os
import json
import csv

# === author imports / helpers ===
import subprocess
import sys
import os
import json
import math

def _ensure_pkg(pkg_name, import_name=None):
    if import_name is None:
        import_name = pkg_name
    try:
        __import__(import_name)
    except ImportError:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir",
             "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", pkg_name]
        )

_ensure_pkg("numpy")
_ensure_pkg("scipy")

import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import bisect
import csv


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


# === block: score_0 (check id='step_1_flip_energy') ===
def score_0(artifact, step, ctx):
    import subprocess, sys
    try:
        import numpy as np
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir",
                               "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy"])
        import numpy as np
    try:
        from scipy.interpolate import interp1d
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir",
                               "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "scipy"])
        from scipy.interpolate import interp1d

    def compute_flip_bound(L, filling):
        N_sites_sub = L*L
        N_electrons = int(round(filling * N_sites_sub))
        H_free = np.zeros((N_sites_sub, N_sites_sub))
        for i in range(L):
            for j in range(L):
                idx = i*L + j
                for di, dj in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                    ni = (i+di) % L
                    nj = (j+dj) % L
                    nidx = ni*L + nj
                    H_free[idx, nidx] = 1.0
        e_free = np.linalg.eigvalsh(H_free)
        E_free = np.sum(np.sort(e_free)[:N_electrons])
        H_defect = H_free.copy()
        ci = L//2
        cj = L//2
        forbidden_idxs = []
        for di,dj in [(0,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
            ni = (ci+di)%L
            nj = (cj+dj)%L
            idx = ni*L + nj
            forbidden_idxs.append(idx)
        for idx in forbidden_idxs:
            H_defect[idx, idx] += 1e6
        e_defect = np.linalg.eigvalsh(H_defect)
        low_e = e_defect[e_defect < 1e5]
        low_e_sorted = np.sort(low_e)
        if len(low_e_sorted) < N_electrons-1:
            return None
        E_constrained = np.sum(low_e_sorted[:N_electrons-1])
        E_flip = -4.0 + E_constrained - E_free
        return E_flip

    agent_fillings = [float(r['filling']) for r in artifact]
    agent_E = [float(r['E_flip_lower_bound']) for r in artifact]
    if len(agent_fillings) < 2:
        return 0.0

    # --- recompute score (unchanged) ---
    interp = interp1d(agent_fillings, agent_E, kind='linear', fill_value='extrapolate')
    hidden_fillings = step.get('hidden_fillings', [0.15,0.22,0.28])
    L = step.get('lattice_size', 60)
    tolerance = step.get('tolerance', 0.1)
    scores = []
    for f in hidden_fillings:
        try:
            agent_val = float(interp(f))
            ref_val = compute_flip_bound(L, f)
            if ref_val is None:
                scores.append(0.0)
                continue
            err = abs(agent_val - ref_val)
            if err <= tolerance:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (err - tolerance)/tolerance))
        except Exception:
            scores.append(0.0)
    recompute_score = float(np.mean(scores)) if scores else 0.0

    # --- structural score (new) ---
    def _fill_val(f):
        return interp1d(agent_fillings, agent_E, kind='linear', fill_value='extrapolate')(f)

    structural_checks = []

    # 1. Monotonicity: values should be non-decreasing
    vals = np.array(agent_E)
    diffs = np.diff(vals)
    if len(diffs) == 0:
        structural_checks.append(0.0)
    else:
        if np.all(diffs >= -1e-8):
            structural_checks.append(1.0)
        else:
            structural_checks.append(0.0)

    # 2. Sign at low and high fillings: at 0.1, bound should be negative; at 0.35, positive
    try:
        v_low = _fill_val(0.1)
        v_high = _fill_val(0.35)
        if (v_low is not None and v_high is not None and v_low < 0.0 and v_high > 0.0):
            structural_checks.append(1.0)
        else:
            structural_checks.append(0.0)
    except Exception:
        structural_checks.append(0.0)

    # 3. Zero crossing fill between 0.2 and 0.3
    try:
        # find filling where interpolated E_flip crosses zero
        fvals = np.linspace(0.1, 0.35, 251)  # 0.001 step
        evals = np.array([_fill_val(f) for f in fvals])
        sign_changes = np.where(np.sign(evals[:-1]) != np.sign(evals[1:]))[0]
        if len(sign_changes) >= 1:
            idx = sign_changes[0]
            f1, f2 = fvals[idx], fvals[idx+1]
            e1, e2 = evals[idx], evals[idx+1]
            if abs(e2 - e1) > 1e-12:
                zero_fill = f1 - e1 * (f2 - f1) / (e2 - e1)
            else:
                zero_fill = (f1 + f2) / 2.0
            if 0.2 <= zero_fill <= 0.3:
                structural_checks.append(1.0)
            else:
                structural_checks.append(0.0)
        else:
            structural_checks.append(0.0)
    except Exception:
        structural_checks.append(0.0)

    structural_score = float(np.mean(structural_checks)) if structural_checks else 0.0

    # final score is average of recompute and structural
    final_score = (recompute_score + structural_score) / 2.0
    return float(min(1.0, max(0.0, final_score)))


# === block: score_1 (check id='step_2_critical_filling') ===
def score_1(artifact, step, ctx):
    n_c = float(artifact.get('n_c', 999))
    method = str(artifact.get('method', ''))
    max_n_c = step.get('max_n_c', 0.265)
    score = 0.0
    if n_c <= max_n_c:
        score += 0.8
    if method and 'interpolat' in method.lower():
        score += 0.2
    elif method:
        score += 0.1
    return min(1.0, score)


# === block: score_2 (check id='step_3_bcs_gap') ===
def score_2(artifact, step, ctx):
    def solve_bcs_for_filling(filling, tprime_sign=1):
        # Determine symmetry
        if tprime_sign > 0:
            sym = 1 if filling > 0.5 else -1  # 1: s-wave, -1: d-wave
        else:
            sym = -1 if filling > 0.5 else 1
        Nk = 200
        kx = np.linspace(0, np.pi, Nk, endpoint=False)
        ky = np.linspace(0, 2*np.pi, Nk, endpoint=False)
        KX, KY = np.meshgrid(kx, ky)
        eps = 4.0 * np.cos(KX) * np.cos(KY)
        # find mu from band filling in non-interacting limit
        def f(mu):
            return np.mean(eps < mu) - filling
        mu = bisect(f, -4.1, 4.1, xtol=1e-4)
        # compute V0 for small delta values
        deltas = np.array([1e-4, 2e-4, 4e-4])
        V0s = []
        for delta in deltas:
            chi = np.cos(KX) + sym * np.cos(KY)
            integrand = chi**2 / np.sqrt((eps - mu)**2 + delta**2 * chi**2)
            # V0^{-1} = 0.25 * mean(integrand)
            V0_inv = 0.25 * np.mean(integrand)
            if V0_inv <= 0:
                return None, None
            V0s.append(1.0 / V0_inv)
        V0s = np.array(V0s)
        log_delta = np.log(deltas)
        inv_V0 = 1.0 / V0s
        A = np.vstack([inv_V0, np.ones_like(inv_V0)]).T
        slope, intercept = np.linalg.lstsq(A, log_delta, rcond=None)[0]
        g0 = -1.0 / slope
        omega = np.exp(intercept) / 2.0
        return omega, g0

    agent_fillings = [float(r['filling']) for r in artifact]
    agent_omega = [float(r['omega_over_tprime']) for r in artifact]
    agent_g0 = [float(r['g0']) for r in artifact]
    agent_map = {}
    for i, f in enumerate(agent_fillings):
        if f not in agent_map:
            agent_map[f] = (agent_omega[i], agent_g0[i])

    hidden_fillings = step.get('hidden_fillings', [0.25,0.55,0.75])
    rel_tol = step.get('relative_tolerance', 0.15)
    scores = []
    for fill in hidden_fillings:
        if fill not in agent_map:
            scores.append(0.0)
            continue
        agent_omega_val, agent_g0_val = agent_map[fill]
        try:
            omega_ref, g0_ref = solve_bcs_for_filling(fill, tprime_sign=1)
            if omega_ref is None:
                scores.append(0.0)
                continue
            err_omega = abs(agent_omega_val - omega_ref) / max(abs(omega_ref), 1e-12)
            err_g0 = abs(agent_g0_val - g0_ref) / max(abs(g0_ref), 1e-12)
            score_omega = 1.0 if err_omega <= rel_tol else max(0.0, 1.0 - (err_omega - rel_tol)/rel_tol)
            score_g0 = 1.0 if err_g0 <= rel_tol else max(0.0, 1.0 - (err_g0 - rel_tol)/rel_tol)
            scores.append((score_omega + score_g0) / 2.0)
        except Exception:
            scores.append(0.0)
    return float(np.mean(scores)) if scores else 0.0


# === block: score_3 (check id='step_4_symmetry') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, str):
        return 0.0
    lines = artifact.strip().split('\n')
    expected = {}
    for fill in np.arange(0.1, 0.91, 0.05):
        fill = round(fill, 2)
        if fill < 0.5:
            expected[(fill, '+')] = 'd-wave'
            expected[(fill, '-')] = 's-wave'
        else:
            expected[(fill, '+')] = 's-wave'
            expected[(fill, '-')] = 'd-wave'
    actual = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            parts = [p.strip() for p in line.split(',')]
            fill_val = float(parts[0].split('=')[1].strip())
            sign_part = parts[1].strip()
            if "t'>" in sign_part:
                sign = '+'
            elif "t'<" in sign_part:
                sign = '-'
            else:
                sign = '+'
            sym = parts[2].split('>')[1].strip()
            actual[(fill_val, sign)] = sym
        except Exception:
            continue
    if not expected:
        return 0.0
    correct = 0
    for key, exp_sym in expected.items():
        if key in actual and actual[key] == exp_sym:
            correct += 1
    return round(correct / len(expected), 4)


_SCORERS = {
    'step_1_flip_energy': score_0,
    'step_2_critical_filling': score_1,
    'step_3_bcs_gap': score_2,
    'step_4_symmetry': score_3,
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
