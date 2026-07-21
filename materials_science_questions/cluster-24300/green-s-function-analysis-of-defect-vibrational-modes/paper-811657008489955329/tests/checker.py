import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import root
import sys


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
    output_dir = '/app/outputs'
    params_list = [
        {'alpha': 0.5, 'epsilon': 0.5, 'a': 1.0, 'c': 4.0},
        {'alpha': 0.0, 'epsilon': 1.0, 'a': 1.0, 'c': 4.0}
    ]
    Ns = [1, 2, 5, 10, 20, 50]

    def k0(omega, c):
        # complex wave number with branch cut consistent with paper (principal branch)
        return np.sqrt(omega**2 - c**2)

    def green(x, omega, c):
        k = k0(omega, c)
        return np.exp(1j * k * abs(x)) / (2j * k) if abs(k) > 1e-15 else 0.0

    def build_matrices(alpha, epsilon, a, c, N, omega):
        k = k0(omega, c)
        x = (np.arange(N) + 0.5) * a
        # compute d_j
        d = c**2 * epsilon - omega**2 * alpha
        # matrix A
        A = 2j * k * np.eye(N) - d * np.exp(1j * k * np.abs(x[:, None] - x[None, :]))
        # RHS g
        g = np.exp(1j * k * np.abs(x))
        return A, g, x

    def kappa_plus(alpha, epsilon, a, c, N, omega):
        """Compute transmission coefficient κ⁺ for given omega (real)."""
        A, g, x = build_matrices(alpha, epsilon, a, c, N, omega)
        try:
            w = np.linalg.solve(A, g)
        except np.linalg.LinAlgError:
            return 0.0
        x_plus = x[-1] + 1.0
        k = k0(omega, c)
        g_plus = green(x_plus, omega, c)
        # compute w(x_plus)
        w_plus = g_plus
        for j in range(N):
            f_j = w[j] * (c**2 * epsilon - omega**2 * alpha)
            w_plus += f_j * green(x_plus - x[j], omega, c)
        return abs(w_plus / g_plus)**2 if abs(g_plus) > 1e-15 else 0.0

    def det_A(alpha, epsilon, a, c, N, omega):
        """Determinant of A for complex omega."""
        k = k0(omega, c)
        x = (np.arange(N) + 0.5) * a
        d = c**2 * epsilon - omega**2 * alpha
        A = 2j * k * np.eye(N) - d * np.exp(1j * k * np.abs(x[:, None] - x[None, :]))
        return np.linalg.det(A)

    def find_poles(alpha, epsilon, a, c, N, real_range):
        """Find poles (roots of det A) in lower half-plane within real_range."""
        poles = []
        # coarse grid of initial guesses
        re_vals = np.arange(real_range[0], real_range[1] + 0.5, 0.5)
        im_vals = np.arange(-5, 0.1, 0.5)
        initial_guesses = []
        for re in re_vals:
            for im in im_vals:
                omega0 = re + 1j*im
                # quick check: if det is small, add as candidate
                try:
                    if abs(det_A(alpha, epsilon, a, c, N, omega0)) < 1000.0:
                        initial_guesses.append(omega0)
                except:
                    pass
        # cluster nearby guesses (average)
        if not initial_guesses:
            return []
        # simple clustering: use threshold distance 1.0
        clusters = []
        for guess in initial_guesses:
            matched = False
            for cl in clusters:
                if np.linalg.norm(guess - cl['center']) < 1.0:
                    cl['points'].append(guess)
                    matched = True
                    break
            if not matched:
                clusters.append({'points': [guess]})
        for cl in clusters:
            cl['center'] = np.mean(cl['points'])
        # refine each cluster center with root-finding
        for cl in clusters:
            omega0 = cl['center']
            def f(vars):
                omega = vars[0] + 1j*vars[1]
                d = det_A(alpha, epsilon, a, c, N, omega)
                return [d.real, d.imag]
            try:
                sol = root(f, [omega0.real, omega0.imag], method='hybr', tol=1e-6)
                if sol.success:
                    omega_root = sol.x[0] + 1j*sol.x[1]
                    # filter out spurious roots far from real axis or outside range
                    if real_range[0] <= omega_root.real <= real_range[1] and omega_root.imag <= 0:
                        poles.append(omega_root)
            except:
                pass
        # deduplicate: keep only one pole per tight threshold
        unique_poles = []
        for p in poles:
            if not any(np.abs(p - up) < 1e-3 for up in unique_poles):
                unique_poles.append(p)
        return unique_poles

    ctx = {
        'output_dir': output_dir,
        'params_list': params_list,
        'Ns': Ns,
        'k0': k0,
        'green': green,
        'build_matrices': build_matrices,
        'kappa_plus': kappa_plus,
        'det_A': det_A,
        'find_poles': find_poles
    }


# === block: score_0 (check id='poles_check') ===
def score_0(artifact, step, ctx):
    params_list = step['parameters']['param_sets']
    Ns = step['parameters']['Ns']
    tol = step['parameters']['tolerance']
    real_range = step['parameters']['real_range']

    def k0(omega, c):
        return np.sqrt(omega**2 - c**2)

    def det_A(alpha, epsilon, a, c, N, omega):
        k = k0(omega, c)
        x = (np.arange(N) + 0.5) * a
        d = c**2 * epsilon - omega**2 * alpha
        A = 2j * k * np.eye(N) - d * np.exp(1j * k * np.abs(x[:, None] - x[None, :]))
        return np.linalg.det(A)

    def find_poles(alpha, epsilon, a, c, N, real_range):
        poles = []
        # coarse grid of initial guesses
        re_vals = np.arange(real_range[0], real_range[1] + 0.5, 0.5)
        im_vals = np.arange(-5, 0.1, 0.5)
        initial_guesses = []
        for re in re_vals:
            for im in im_vals:
                omega0 = re + 1j*im
                try:
                    if abs(det_A(alpha, epsilon, a, c, N, omega0)) < 1000.0:
                        initial_guesses.append(omega0)
                except:
                    pass
        if not initial_guesses:
            return []
        # cluster nearby guesses (threshold distance 1.0)
        clusters = []
        for guess in initial_guesses:
            matched = False
            for cl in clusters:
                if np.linalg.norm(guess - cl['center']) < 1.0:
                    cl['points'].append(guess)
                    matched = True
                    break
            if not matched:
                clusters.append({'points': [guess]})
        for cl in clusters:
            cl['center'] = np.mean(cl['points'])
        # refine each cluster center with root-finding
        for cl in clusters:
            omega0 = cl['center']
            def f(vars):
                omega = vars[0] + 1j*vars[1]
                d = det_A(alpha, epsilon, a, c, N, omega)
                return [d.real, d.imag]
            try:
                sol = root(f, [omega0.real, omega0.imag], method='hybr', tol=1e-6)
                if sol.success:
                    omega_root = sol.x[0] + 1j*sol.x[1]
                    if real_range[0] <= omega_root.real <= real_range[1] and omega_root.imag <= 0:
                        poles.append(omega_root)
            except:
                pass
        # deduplicate
        unique_poles = []
        for p in poles:
            if not any(np.abs(p - up) < 1e-3 for up in unique_poles):
                unique_poles.append(p)
        return unique_poles

    scores = []
    for params in params_list:
        for N in Ns:
            # build reference poles
            ref_poles = find_poles(params['alpha'], params['epsilon'], params['a'], params['c'], N, real_range)
            if not ref_poles:
                scores.append(1.0)
                continue
            # collect agent poles for this config
            agent_poles = []
            for row in artifact:
                try:
                    if (int(row['N']) == N and
                        abs(float(row['alpha']) - params['alpha']) < 1e-6 and
                        abs(float(row['epsilon']) - params['epsilon']) < 1e-6 and
                        abs(float(row['a']) - params['a']) < 1e-6 and
                        abs(float(row['c']) - params['c']) < 1e-6):
                        re = float(row['real_part'])
                        im = float(row['imag_part'])
                        if real_range[0] <= re <= real_range[1] and im <= 0:
                            agent_poles.append(re + 1j*im)
                except:
                    continue
            matched = 0
            for ref in ref_poles:
                if agent_poles:
                    dists = [abs(ref - ap) for ap in agent_poles]
                    if min(dists) <= tol:
                        matched += 1
            score = matched / len(ref_poles)
            scores.append(score)
    # overall score = mean over all configs
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='transmission_check') ===
def score_1(artifact, step, ctx):
    artifact = artifact  # list of dicts
    params_list = ctx['params_list']
    Ns = ctx['Ns']
    kappa_plus = ctx['kappa_plus']
    mae_threshold = step['parameters']['mae_threshold']

    errors = []
    count = 0
    for row in artifact:
        try:
            N = int(row['N'])
            omega = float(row['omega'])
            agent_kappa = float(row['kappa_plus'])
            # find matching param set
            matched_params = None
            for p in params_list:
                if abs(float(row.get('alpha', p['alpha'])) - p['alpha']) < 1e-6 and \
                   abs(float(row.get('epsilon', p['epsilon'])) - p['epsilon']) < 1e-6 and \
                   abs(float(row.get('a', p['a'])) - p['a']) < 1e-6 and \
                   abs(float(row.get('c', p['c'])) - p['c']) < 1e-6:
                    matched_params = p
                    break
            if matched_params is None:
                continue
            ref_kappa = kappa_plus(matched_params['alpha'], matched_params['epsilon'],
                                  matched_params['a'], matched_params['c'], N, omega)
            errors.append(abs(agent_kappa - ref_kappa))
            count += 1
        except:
            continue
    if count == 0:
        return 0.0
    mae = sum(errors) / count
    score = max(0.0, 1.0 - mae / mae_threshold)
    return score


# === block: score_2 (check id='band_edges_check') ===
def score_2(artifact, step, ctx):
    output_dir = ctx['output_dir']
    params_list = ctx['params_list']
    edge_tol = step['parameters']['edge_tolerance']

    # load transmission data (if available) for inferring transmission bands
    trans_path = os.path.join(output_dir, 'transmission_coefficient_N.csv')
    trans_data = None
    if os.path.exists(trans_path):
        with open(trans_path) as f:
            trans_data = list(csv.DictReader(f))

    def compute_bloch_bands(alpha, epsilon, a, c, omega_min, omega_max, step=0.001):
        """Return list of (lower, upper) pass bands from Bloch-Floquet inequality."""
        bands = []
        prev_val = None
        prev_omega = None
        in_band = False
        for omega in np.arange(omega_min, omega_max + step, step):
            k = ctx['k0'](omega, c)
            d = c**2 * epsilon - omega**2 * alpha
            val = abs(np.cos(a*k) + (d * a / k) * np.sin(a*k))
            if val < 1:
                if not in_band:
                    start = omega
                    in_band = True
            else:
                if in_band:
                    bands.append((start, omega - step))
                    in_band = False
        if in_band:
            bands.append((start, omega_max))
        return bands

    def compute_transmission_bands(alpha, epsilon, a, c, trans_data):
        """Use agent's κ⁺ for N=50 with threshold 0.5 to find bands."""
        rows = []
        for r in trans_data:
            try:
                N = int(r['N'])
                if N != 50:
                    continue
                if abs(float(r.get('alpha', 0)) - alpha) < 1e-6 and \
                   abs(float(r.get('epsilon', 0)) - epsilon) < 1e-6 and \
                   abs(float(r.get('a', 0)) - a) < 1e-6 and \
                   abs(float(r.get('c', 0)) - c) < 1e-6:
                    rows.append((float(r['omega']), float(r['kappa_plus'])))
            except:
                continue
        if not rows:
            return []
        rows.sort(key=lambda x: x[0])
        bands = []
        in_band = False
        start = None
        for om, kp in rows:
            if kp > 0.5:
                if not in_band:
                    start = om
                    in_band = True
            else:
                if in_band:
                    bands.append((start, om))
                    in_band = False
        if in_band:
            bands.append((start, rows[-1][0]))
        return bands

    def match_intervals(ref_intervals, agent_intervals, tol):
        matched = 0
        for ref in ref_intervals:
            for ag in agent_intervals:
                if abs(ref[0] - ag[0]) <= tol and abs(ref[1] - ag[1]) <= tol:
                    matched += 1
                    break
        return matched

    scores = []
    for params in params_list:
        c = params['c']
        a = params['a']
        alpha = params['alpha']
        epsilon = params['epsilon']
        omega_max = 5 * c
        # Bloch-Floquet reference
        ref_bloch = compute_bloch_bands(alpha, epsilon, a, c, c, omega_max)
        # agent reported Bloch-Floquet bands
        agent_bloch = []
        for row in artifact:
            try:
                if row['band_type'].strip().lower() == 'bloch-floquet' and row['method'].strip().lower() == 'inequality':
                    if abs(float(row.get('alpha', 0)) - alpha) < 1e-6 and \
                       abs(float(row.get('epsilon', 0)) - epsilon) < 1e-6:
                        lo = float(row['lower_edge'])
                        up = float(row['upper_edge'])
                        agent_bloch.append((lo, up))
            except:
                continue
        if ref_bloch:
            mat = match_intervals(ref_bloch, agent_bloch, edge_tol)
            scores.append(mat / len(ref_bloch))
        else:
            scores.append(1.0)  # no bands, pass

        # Transmission bands
        agent_trans = []
        for row in artifact:
            try:
                if row['band_type'].strip().lower() == 'transmission' and row['method'].strip().lower() == 'kappa_plus':
                    if abs(float(row.get('alpha', 0)) - alpha) < 1e-6 and \
                       abs(float(row.get('epsilon', 0)) - epsilon) < 1e-6:
                        lo = float(row['lower_edge'])
                        up = float(row['upper_edge'])
                        agent_trans.append((lo, up))
            except:
                continue
        if trans_data:
            ref_trans = compute_transmission_bands(alpha, epsilon, a, c, trans_data)
        else:
            ref_trans = []
        if ref_trans:
            mat = match_intervals(ref_trans, agent_trans, edge_tol)
            scores.append(mat / len(ref_trans))
        else:
            scores.append(1.0)

    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'poles_check': score_0,
    'transmission_check': score_1,
    'band_edges_check': score_2,
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
