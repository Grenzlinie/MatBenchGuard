import os
import json
import csv

# === author imports / helpers ===
import math

try:
    import numpy as np
    from scipy.interpolate import CubicSpline
except ImportError:
    # ------------------------------------------------------------------------
    # Pure‑Python fallback for numpy + CubicSpline, sufficient for this checker.
    # ------------------------------------------------------------------------

    def _tridiag_solve(a, b, c, d):
        """Simple Thomas algorithm."""
        n = len(d)
        cp = list(c)
        dp = list(d)
        for i in range(1, n):
            w = a[i-1] / b[i-1]
            b[i] -= w * cp[i-1]
            dp[i] -= w * dp[i-1]
        x = [0.0] * n
        x[-1] = dp[-1] / b[-1]
        for i in range(n-2, -1, -1):
            x[i] = (dp[i] - cp[i] * x[i+1]) / b[i]
        return x

    class CubicSpline:
        """Natural cubic spline."""
        def __init__(self, x, y, bc_type='natural'):
            self.x = list(x)
            self.y = list(y)
            n = len(x)
            self.n = n
            h = [self.x[i+1] - self.x[i] for i in range(n-1)]
            b = [2.0 * (h[i] + h[i+1]) for i in range(n-2)]
            a = h[1:n-2]
            c = h[0:n-2]
            d = [6.0 * ((y[i+2] - y[i+1]) / h[i+1] - (y[i+1] - y[i]) / h[i]) for i in range(n-2)]
            # natural: m0 = m_{n-1} = 0
            if n == 2:
                self.m = [0.0, 0.0]
            else:
                m_inner = _tridiag_solve(a, b, c, d)
                self.m = [0.0] + m_inner + [0.0]
            self.h = h

        def __call__(self, xi):
            x = self.x
            y = self.y
            h = self.h
            m = self.m
            n = self.n
            # binary search
            if xi <= x[0]:
                i = 0
            elif xi >= x[-1]:
                i = n - 2
            else:
                lo, hi = 0, n-2
                while hi - lo > 1:
                    mid = (lo + hi) // 2
                    if x[mid] <= xi:
                        lo = mid
                    else:
                        hi = mid
                i = lo
            dx = xi - x[i]
            a = y[i]
            b = (y[i+1] - y[i]) / h[i] - (h[i] / 6.0) * (2.0 * m[i] + m[i+1])
            c = m[i] / 2.0
            d = (m[i+1] - m[i]) / (6.0 * h[i])
            return a + b * dx + c * dx * dx + d * dx * dx * dx

        def derivative(self, order):
            # return a simple finite-difference derivative for order=1,2
            if order == 1:
                def _der(xi):
                    h = 1e-5
                    return (self(xi + h) - self(xi - h)) / (2 * h)
                return _der
            elif order == 2:
                def _der2(xi):
                    h = 1e-5
                    return (self(xi + h) - 2 * self(xi) + self(xi - h)) / (h * h)
                return _der2
            raise ValueError

    def _eigvalsh_3x3(D):
        """Analytic eigenvalues of a 3x3 symmetric matrix (list of lists)."""
        a11, a12, a13 = D[0]
        a22, a23, a33 = D[1][1], D[1][2], D[2][2]
        # compute coefficients of char poly: λ^3 + c2 λ^2 + c1 λ + c0 = 0
        c2 = -(a11 + a22 + a33)
        c1 = a11*a22 + a11*a33 + a22*a33 - a12*a12 - a13*a13 - a23*a23
        c0 = -(a11*a22*a33 + 2*a12*a13*a23 - a11*a23*a23 - a22*a13*a13 - a33*a12*a12)
        # use trigonometric method
        p = c2*c2 / 9.0 - c1 / 3.0
        q = c2*c1 / 6.0 - c2*c2*c2 / 27.0 - c0 / 2.0
        if abs(p) < 1e-14:
            # one real
            r = (-q)**(1.0/3.0) if q < 0 else -q**(1.0/3.0)
            lam = [r - c2/3.0]*3
            return sorted(lam)
        disc = q*q - p*p*p
        if disc > 0:
            sqrt_disc = math.sqrt(disc)
            r1 = (-q + sqrt_disc)**(1.0/3.0)
            r2 = (-q - sqrt_disc)**(1.0/3.0)
            lam1 = r1 + r2 - c2/3.0
            return sorted([lam1, lam1, lam1])
        else:
            phi = math.acos(q / math.sqrt(p*p*p)) / 3.0
            sqrt_p = 2 * math.sqrt(p)
            lam1 = sqrt_p * math.cos(phi) - c2/3.0
            lam2 = sqrt_p * math.cos(phi - 2*math.pi/3) - c2/3.0
            lam3 = sqrt_p * math.cos(phi + 2*math.pi/3) - c2/3.0
            return sorted([lam1, lam2, lam3])

    class _NpFallback:
        """Provide a minimal numpy‑like interface."""
        def __init__(self):
            self.pi = math.pi
            self.linalg = self

        def array(self, obj, dtype=None):
            return list(obj)

        def zeros(self, shape, dtype=None):
            if isinstance(shape, int):
                return [0.0] * shape
            return [self.zeros(shape[1:]) for _ in range(shape[0])]

        def eye(self, n):
            return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

        def outer(self, a, b):
            return [[ai * bj for bj in b] for ai in a]

        def dot(self, a, b):
            if isinstance(a[0], (list, tuple)):
                # matrix-vector
                return [sum(ai_j * bj for ai_j, bj in zip(ai, b)) for ai in a]
            # vector-vector
            return sum(ai * bi for ai, bi in zip(a, b))

        def cos(self, x):
            return math.cos(x)

        def sqrt(self, x):
            return math.sqrt(x)

        def maximum(self, a, b):
            if isinstance(a, (list, tuple)):
                return [[max(ai, b) if isinstance(ai, (int,float)) else self.maximum(ai, b) for ai in row] for row in a]
            return max(a, b)

        def mean(self, arr):
            return sum(arr) / len(arr)

        def abs(self, x):
            return abs(x)

        def asarray(self, x):
            return list(x)

        def eigvalsh(self, D):
            return _eigvalsh_3x3(D)

    np = _NpFallback()


# Conversion factor: 1 eV/Å^2/amu -> (rad/s)^2 multiplier, then -> THz
FREQ_CONV = 15.63


def _build_splines(params):
    """Build cubic splines for Z(r) and F(ρ) from the parameter dict."""
    p = params
    Z_spline = CubicSpline(p['Z_r_knots'], p['Z_vals'],
                           bc_type=((1, p['Z_left_deriv']), (1, p['Z_right_deriv'])))
    F_spline = CubicSpline(p['F_rho_knots'], p['F_vals'], bc_type='natural')
    return Z_spline, F_spline


def _compute_V_func(Z_spline):
    """Return functions giving V(R)=14.4*Z^2/R (eV) and its derivatives."""
    def V(r):
        return 14.4 * (Z_spline(r)**2) / r
    def Vprime(r):
        h = 1e-5
        return (V(r+h) - V(r-h)) / (2*h)
    def Vprime2(r):
        h = 1e-5
        return (V(r+h) - 2*V(r) + V(r-h)) / (h**2)
    return Vprime, Vprime2


def _first_neighbor_vecs(a0):
    """12 first-neighbor vectors in fcc (Cartesian, units a0)."""
    vecs = []
    for sx in (-1,1):
        for sy in (-1,1):
            vecs.append(np.array([sx*0.5, sy*0.5, 0.0]) * a0)
            vecs.append(np.array([sx*0.5, 0.0, sy*0.5]) * a0)
            vecs.append(np.array([0.0, sx*0.5, sy*0.5]) * a0)
    return vecs


def _third_neighbor_vecs(a0):
    """24 third-neighbor vectors (1, 1/2, 1/2)a0 with permutations and signs."""
    vecs = []
    bases = [np.array([1.0, 0.5, 0.5]),
             np.array([0.5, 1.0, 0.5]),
             np.array([0.5, 0.5, 1.0])]
    for b in bases:
        for s1 in (-1,1):
            for s2 in (-1,1):
                for s3 in (-1,1):
                    v = np.array([s1*b[0], s2*b[1], s3*b[2]]) * a0
                    vecs.append(v)
    return vecs


def compute_phonon_reference(metal, direction, q_reduced, metal_params):
    """Return sorted phonon frequencies (THz) for a given metal, direction, q_reduced."""
    p = metal_params
    a0 = p['a0']
    mass_u = p['mass']
    Z_spline, F_spline = _build_splines(p)
    Vprime_func, Vprime2_func = _compute_V_func(Z_spline)

    if direction == '[100]':
        q_vec = np.array([q_reduced * 2 * math.pi / a0, 0.0, 0.0])
    elif direction == '[110]':
        q_vec = np.array([1.0, 1.0, 0.0]) / math.sqrt(2) * (2 * math.pi / a0 * q_reduced)
    elif direction == '[111]':
        q_vec = np.array([1.0, 1.0, 1.0]) / math.sqrt(3) * (2 * math.pi / a0 * q_reduced)
    else:
        raise ValueError(f'Unknown direction {direction}')

    R1 = a0 / math.sqrt(2)
    Z1 = Z_spline(R1)
    rho_eq = 12 * Z1
    F_prime = F_spline.derivative(1)(rho_eq)
    F_prime2 = F_spline.derivative(2)(rho_eq)

    Z1_prime = Z_spline.derivative(1)(R1)
    Z1_prime2 = Z_spline.derivative(2)(R1)

    D = np.zeros((3, 3), dtype=np.float64)

    first_vecs = _first_neighbor_vecs(a0)
    for Rvec in first_vecs:
        R = math.sqrt(Rvec[0]**2 + Rvec[1]**2 + Rvec[2]**2)
        Rhat = [Rvec[0]/R, Rvec[1]/R, Rvec[2]/R]
        outer_r = np.outer(Rhat, Rhat)
        Vprime = Vprime_func(R)
        Vprime2 = Vprime2_func(R)
        Zp = Z_spline.derivative(1)(R)
        Zp2 = Z_spline.derivative(2)(R)
        pair = [[- (Vprime2 - Vprime/R) * outer_r[i][j] for j in range(3)] for i in range(3)]
        I = [[1.0 if i==j else 0.0 for j in range(3)] for i in range(3)]
        pair = [[pair[i][j] - (Vprime/R) * I[i][j] for j in range(3)] for i in range(3)]
        embed = [[- (F_prime * Zp2 + F_prime2 * Zp**2) * outer_r[i][j] - (F_prime * Zp / R) * I[i][j] for j in range(3)] for i in range(3)]
        phi = [[pair[i][j] + embed[i][j] for j in range(3)] for i in range(3)]
        phase = math.cos(q_vec[0]*Rvec[0] + q_vec[1]*Rvec[1] + q_vec[2]*Rvec[2])
        D = [[D[i][j] + phi[i][j] * (1.0 - phase) for j in range(3)] for i in range(3)]

    phi3_prime = p['phi3_prime']
    phi3_prime2 = p['phi3_prime2']
    third_vecs = _third_neighbor_vecs(a0)
    for Rvec in third_vecs:
        R = math.sqrt(Rvec[0]**2 + Rvec[1]**2 + Rvec[2]**2)
        Rhat = [Rvec[0]/R, Rvec[1]/R, Rvec[2]/R]
        outer_r = np.outer(Rhat, Rhat)
        phi3 = [[- (phi3_prime2 - phi3_prime/R) * outer_r[i][j] - (phi3_prime/R) * (1.0 if i==j else 0.0) for j in range(3)] for i in range(3)]
        phase = math.cos(q_vec[0]*Rvec[0] + q_vec[1]*Rvec[1] + q_vec[2]*Rvec[2])
        D = [[D[i][j] + phi3[i][j] * (1.0 - phase) for j in range(3)] for i in range(3)]

    eigvals = np.linalg.eigvalsh(D)
    omega2 = [max(e, 0.0) for e in eigvals]
    omega2 = [e / mass_u for e in omega2]
    freq = [math.sqrt(e) * FREQ_CONV for e in omega2]
    freq.sort()
    return freq


def compute_mape(rows, metal_params):
    groups = {}
    for row in rows:
        metal = row['metal']
        direction = row['direction']
        q = float(row['q_reduced'])
        freq_val = float(row['frequency_THz'])
        key = (metal, direction, q)
        if key not in groups:
            groups[key] = []
        groups[key].append(freq_val)

    errors = []
    for (metal, direction, q), freqs in groups.items():
        if metal not in metal_params:
            return 1.0
        ref = compute_phonon_reference(metal, direction, q, metal_params[metal])
        agent_sorted = sorted(freqs)
        if len(ref) != len(agent_sorted):
            errors.extend([1.0] * max(len(ref), len(agent_sorted)))
            continue
        for a, r in zip(agent_sorted, ref):
            if r > 1e-6:
                errors.append(abs(a - r) / r)
    if not errors:
        return 0.0
    return np.mean(errors)


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
    # Build metal parameter contexts from grading_spec hidden_parameters
    hidden = spec.get('hidden_parameters', {})
    ctx = {}
    for metal, p in hidden.items():
        ctx[metal] = {
            'a0': float(p['a0']),
            'rho_bar': float(p['rho_bar']),
            'mass': float(p['mass']),
            'Z_r_knots': np.array(p['Z_r_knots'], dtype=float),
            'Z_vals': np.array(p['Z_vals'], dtype=float),
            'Z_left_deriv': float(p.get('Z_left_deriv', 0.0)),
            'Z_right_deriv': float(p.get('Z_right_deriv', 0.0)),
            'F_rho_knots': np.array(p['F_rho_knots'], dtype=float),
            'F_vals': np.array(p['F_vals'], dtype=float),
            'F_left_deriv': float(p.get('F_left_deriv', 0.0)),
            'F_right_deriv': float(p.get('F_right_deriv', 0.0)),
            'phi3_prime': float(p['phi3_prime']),
            'phi3_prime2': float(p['phi3_prime2']),
        }
    return ctx


# === block: score_0 (check id='scored_phonon') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts from CSV; ctx has per-metal params
    map_err = compute_mape(artifact, ctx)
    target = float(step.get('target_value', 0.05))
    max_decay = float(step.get('max_score_decay_to_zero_value', 0.20))
    if map_err <= target:
        score_val = 1.0
    else:
        score_val = max(0.0, 1.0 - (map_err - target) / (max_decay - target))
    return score_val


_SCORERS = {
    'scored_phonon': score_0,
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
