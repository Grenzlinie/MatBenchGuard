import os
import json
import csv

# === author imports / helpers ===
import numpy as np

def linear_sum_assignment(cost_matrix):
    # 4x4 brute-force min-cost assignment for 4 bands
    n = cost_matrix.shape[0]
    if n != 4:
        raise ValueError("Expected 4x4 cost matrix for band matching")
    perm = [0,1,2,3]
    best = float('inf')
    best_perm = perm[:]
    for a in range(n):
        for b in range(n):
            if b == a: continue
            for c in range(n):
                if c == a or c == b: continue
                d = 0+1+2+3 - a - b - c
                val = cost_matrix[0,a] + cost_matrix[1,b] + cost_matrix[2,c] + cost_matrix[3,d]
                if val < best:
                    best = val
                    best_perm = [a,b,c,d]
    return np.arange(n), np.array(best_perm)


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
    ctx = {}
    vF_si = 5.8e5  # m/s
    hbar_eVs = 6.582119569e-16  # eV·s
    vF_eV_Ang = vF_si * hbar_eVs * 1e10  # ~3.818 eV·Å

    ctx['params'] = {
        'sb': {
            'mstar': -0.2,
            'alphaR': 0.5,
            't': 0.05,
            'delta': 0.05,
            'vF': vF_eV_Ang
        },
        'bi': {
            'mstar': -0.12,
            'alphaR': 0.2,
            't': 0.1,
            'delta': 0.4,
            'vF': vF_eV_Ang
        }
    }
    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import numpy as np
    from scipy.optimize import linear_sum_assignment

    params = step['parameters']
    expected_zero = params['expected_zero_crossings']
    expected_below = params['expected_below_crossings']
    tol_zero = params['energy_tolerance_zero']
    tol_below = params['energy_tolerance_below']
    mat = params['material']
    mat_params = ctx['params'][mat]

    rows = artifact
    if len(rows) < 10:
        return 0.0

    try:
        ks = np.array([float(r['k']) for r in rows])
        energies = np.array([[float(r['E1']), float(r['E2']), float(r['E3']), float(r['E4'])] for r in rows])
    except Exception:
        return 0.0

    sort_idx = np.argsort(ks)
    ks = ks[sort_idx]
    energies = energies[sort_idx]

    def build_H(k, mp):
        vF = mp['vF']
        mstar_inv = 1.0 / (2.0 * mp['mstar'])
        delta = mp['delta']
        alphaR = mp['alphaR']
        t = mp['t']
        sx = np.array([[0,1],[1,0]], dtype=complex)
        sy = np.array([[0,-1j],[1j,0]], dtype=complex)
        sz = np.array([[1,0],[0,-1]], dtype=complex)
        I2 = np.eye(2)
        kx = k
        ky = 0.0
        H_TI = vF * (kx * sy - ky * sx)
        k2 = kx*kx + ky*ky
        H_BI = (mstar_inv * k2 + delta) * I2 + alphaR * (ky * sx + kx * sy)
        T = t * sz
        H = np.zeros((4,4), dtype=complex)
        H[0:2, 0:2] = H_TI
        H[0:2, 2:4] = T
        H[2:4, 0:2] = T.conj().T
        H[2:4, 2:4] = H_BI
        return H

    # recompute sorted eigenvalues at every k
    n_k = len(ks)
    n_bands = 4
    raw_evals = np.zeros((n_k, n_bands))
    for i, k in enumerate(ks):
        H = build_H(k, mat_params)
        raw_evals[i] = np.sort(np.linalg.eigh(H)[0])

    # Verify that the agent's eigenvalues match the recomputed ones within a small tolerance.
    # If not, the agent likely did not genuinely diagonalize the Hamiltonian.
    AGENT_CONSISTENCY_TOL = 1e-5  # eV
    for i in range(n_k):
        # sort the agent's energies for that row in case they are provided in arbitrary order
        agent_row_sorted = np.sort(energies[i])
        if not np.allclose(agent_row_sorted, raw_evals[i], atol=AGENT_CONSISTENCY_TOL):
            return 0.0

    # track band indices across k by min-cost matching (permutation that minimizes squared distance)
    bands = np.empty((n_bands, n_k))
    bands[:, 0] = raw_evals[0]
    prev = raw_evals[0]
    for i in range(1, n_k):
        current = raw_evals[i]
        cost = (prev.reshape(-1, 1) - current.reshape(1, -1)) ** 2
        row_ind, col_ind = linear_sum_assignment(cost)
        bands[:, i] = current[col_ind]
        prev = bands[:, i]

    # detect crossings between tracked bands
    crossings = []
    for i in range(n_bands):
        for j in range(i+1, n_bands):
            diff = bands[j] - bands[i]
            for k_idx in range(n_k - 1):
                d1 = diff[k_idx]
                d2 = diff[k_idx+1]
                if d1 * d2 > 0:
                    continue
                # crossing
                k1, k2 = ks[k_idx], ks[k_idx+1]
                e_i1 = bands[i, k_idx]
                e_i2 = bands[i, k_idx+1]
                e_j1 = bands[j, k_idx]
                e_j2 = bands[j, k_idx+1]
                # linear interpolation: solve e_i(k) = e_j(k)
                denom = (e_i2 - e_i1) - (e_j2 - e_j1)
                if abs(denom) < 1e-12:
                    continue
                t = (e_j1 - e_i1) / denom
                k_cross = k1 + t * (k2 - k1)
                k_cross = max(k1, min(k2, k_cross))
                e_cross_i = e_i1 + (k_cross - k1) * (e_i2 - e_i1) / (k2 - k1)
                e_cross_j = e_j1 + (k_cross - k1) * (e_j2 - e_j1) / (k2 - k1)
                E_cross = 0.5 * (e_cross_i + e_cross_j)
                crossing_point = (k_cross, E_cross)
                if not any(abs(c[0] - k_cross) < 1e-6 for c in crossings):
                    crossings.append(crossing_point)

    # classify crossings
    zero_cross = [c for c in crossings if abs(c[1]) < tol_zero]
    below_cross = [c for c in crossings if c[1] < -tol_below]

    score = 0.0
    if len(zero_cross) >= expected_zero:
        score += 0.5
    if len(below_cross) >= expected_below:
        score += 0.5
    return min(score, 1.0)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    import numpy as np
    from scipy.optimize import linear_sum_assignment

    params = step['parameters']
    expected_zero = params['expected_zero_crossings']
    expected_below = params['expected_below_crossings']
    tol_zero = params['energy_tolerance_zero']
    tol_below = params['energy_tolerance_below']
    mat = params['material']
    mat_params = ctx['params'][mat]

    rows = artifact
    if len(rows) < 10:
        return 0.0

    try:
        ks = np.array([float(r['k']) for r in rows])
        energies = np.array([[float(r['E1']), float(r['E2']), float(r['E3']), float(r['E4'])] for r in rows])
    except Exception:
        return 0.0

    sort_idx = np.argsort(ks)
    ks = ks[sort_idx]

    def build_H(k, mp):
        vF = mp['vF']
        mstar_inv = 1.0 / (2.0 * mp['mstar'])
        delta = mp['delta']
        alphaR = mp['alphaR']
        t = mp['t']
        sx = np.array([[0,1],[1,0]], dtype=complex)
        sy = np.array([[0,-1j],[1j,0]], dtype=complex)
        sz = np.array([[1,0],[0,-1]], dtype=complex)
        I2 = np.eye(2)
        kx = k
        ky = 0.0
        H_TI = vF * (kx * sy - ky * sx)
        k2 = kx*kx + ky*ky
        H_BI = (mstar_inv * k2 + delta) * I2 + alphaR * (ky * sx + kx * sy)
        T = t * sz
        H = np.zeros((4,4), dtype=complex)
        H[0:2, 0:2] = H_TI
        H[0:2, 2:4] = T
        H[2:4, 0:2] = T.conj().T
        H[2:4, 2:4] = H_BI
        return H

    n_k = len(ks)
    n_bands = 4
    raw_evals = np.zeros((n_k, n_bands))
    for i, k in enumerate(ks):
        H = build_H(k, mat_params)
        raw_evals[i] = np.sort(np.linalg.eigh(H)[0])

    # track band indices across k by min-cost permutation
    bands = np.empty((n_bands, n_k))
    bands[:, 0] = raw_evals[0]
    prev = raw_evals[0]
    for i in range(1, n_k):
        current = raw_evals[i]
        cost = (prev.reshape(-1, 1) - current.reshape(1, -1)) ** 2
        row_ind, col_ind = linear_sum_assignment(cost)
        bands[:, i] = current[col_ind]
        prev = bands[:, i]

    # detect crossings between tracked bands
    crossings = []
    for i in range(n_bands):
        for j in range(i+1, n_bands):
            diff = bands[j] - bands[i]
            for k_idx in range(n_k - 1):
                d1 = diff[k_idx]
                d2 = diff[k_idx+1]
                if d1 * d2 > 0:
                    continue
                k1, k2 = ks[k_idx], ks[k_idx+1]
                e_i1 = bands[i, k_idx]
                e_i2 = bands[i, k_idx+1]
                e_j1 = bands[j, k_idx]
                e_j2 = bands[j, k_idx+1]
                denom = (e_i2 - e_i1) - (e_j2 - e_j1)
                if abs(denom) < 1e-12:
                    continue
                t_int = (e_j1 - e_i1) / denom
                k_cross = k1 + t_int * (k2 - k1)
                k_cross = max(k1, min(k2, k_cross))
                e_cross_i = e_i1 + (k_cross - k1) * (e_i2 - e_i1) / (k2 - k1)
                e_cross_j = e_j1 + (k_cross - k1) * (e_j2 - e_j1) / (k2 - k1)
                E_cross = 0.5 * (e_cross_i + e_cross_j)
                if not any(abs(c[0] - k_cross) < 1e-6 for c in crossings):
                    crossings.append((k_cross, E_cross))

    # classify crossings
    zero_cross = [c for c in crossings if abs(c[1]) < tol_zero]
    below_cross = [c for c in crossings if c[1] < -tol_below]

    score = 0.0
    if len(zero_cross) >= expected_zero:
        score += 0.3
    if len(below_cross) >= expected_below:
        score += 0.3
    if len(below_cross) >= 2:
        es = sorted([c[1] for c in below_cross])
        if es[0] < es[1] < 0:
            score += 0.4
    return min(score, 1.0)


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
