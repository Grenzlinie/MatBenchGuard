import os
import json
import csv

# === author imports / helpers ===
from collections import defaultdict
import math

class np:
    @staticmethod
    def array(lst, dtype=None):
        return list(lst)
    @staticmethod
    def median(data):
        n = len(data)
        s = sorted(data)
        if n % 2 == 1:
            return s[n//2]
        return (s[n//2-1] + s[n//2]) / 2.0
    @staticmethod
    def linspace(start, stop, num):
        if num == 1:
            return [stop]
        step = (stop - start) / (num - 1)
        return [start + i * step for i in range(num)]
    @staticmethod
    def argmin(arr):
        return min(range(len(arr)), key=lambda i: arr[i])
    @staticmethod
    def mean(arr):
        return sum(arr) / len(arr)
    @staticmethod
    def polyfit(x, y, deg):
        n = len(x)
        X = [[sum(xi**(i+j) for xi in x) for j in range(deg+1)] for i in range(deg+1)]
        Y = [sum(yi * (xi**i) for xi, yi in zip(x, y)) for i in range(deg+1)]
        A = X
        b = Y
        size = len(A)
        for i in range(size):
            pivot = A[i][i]
            for j in range(i+1, size):
                factor = A[j][i] / pivot
                b[j] -= factor * b[i]
                for k in range(i, size):
                    A[j][k] -= factor * A[i][k]
        coeffs = [0] * size
        for i in range(size-1, -1, -1):
            s = b[i]
            for j in range(i+1, size):
                s -= A[i][j] * coeffs[j]
            coeffs[i] = s / A[i][i]
        return coeffs[::-1]
    @staticmethod
    def poly1d(coeffs):
        class Poly:
            def __init__(self, c):
                self.c = c
            def __call__(self, x):
                res = 0.0
                for co in self.c:
                    res = res * x + co
                return res
        return Poly(coeffs)
    @staticmethod
    def polyder(poly, m=1):
        c = poly.c[:]
        for _ in range(m):
            if not c:
                return np.poly1d([0])
            n = len(c) - 1
            c = [(n - i) * c[i] for i in range(n)]
        return np.poly1d(c)
    @staticmethod
    def roots(coeffs):
        # return empty list to trigger the V_scan fallback in the scorer
        return []


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
    return {
        'gold': spec.get('gold', {}),
        'evv_tol_rel': 0.15
    }


# === block: score_0 (check id='evv_check') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    for row in artifact:
        if not all(k in row for k in ('phase','volume_ang3','total_energy_eV')):
            return 0.0
    phases_data = defaultdict(list)
    for row in artifact:
        try:
            vol = float(row['volume_ang3'])
            ener = float(row['total_energy_eV'])
            phases_data[row['phase']].append((vol, ener))
        except:
            continue
    required_phases = {'alpha','beta','cubic','pseudocubic','graphitic'}
    if set(phases_data.keys()) != required_phases:
        return 0.0
    def fit_phase(vols, energies):
        coeffs = np.polyfit(vols, energies, 4)
        poly = np.poly1d(coeffs)
        deriv = np.polyder(poly, 1)
        deriv2 = np.polyder(poly, 2)
        roots = np.roots(deriv)
        V_median = np.median(vols)
        real_roots = [r.real for r in roots if abs(r.imag) < 1e-9]
        if not real_roots:
            V_scan = np.linspace(min(vols), max(vols), 1000)
            E_scan = poly(V_scan)
            idx = np.argmin(E_scan)
            V0 = V_scan[idx]
        else:
            V0 = min(real_roots, key=lambda v: abs(v - V_median))
        E0 = poly(V0)
        d2E = deriv2(V0)
        B0_GPa = V0 * d2E * 160.2177
        return E0, V0, B0_GPa
    fitted = {}
    for ph, points in phases_data.items():
        vols, eners = zip(*sorted(points, key=lambda x: x[0]))
        vols = np.array(vols, dtype=float)
        eners = np.array(eners, dtype=float)
        E0, V0, B0 = fit_phase(vols, eners)
        fitted[ph] = {'E0': E0, 'V0': V0, 'B0': B0}
    ctx['fitted'] = fitted
    energies = {ph: fitted[ph]['E0'] for ph in required_phases}
    pairs = [('pseudocubic','alpha'), ('alpha','graphitic'), ('graphitic','beta'), ('beta','cubic')]
    correct = 0
    for low, high in pairs:
        if energies[low] < energies[high]:
            correct += 1
    order_score = correct / len(pairs)
    phases_with_B0 = ['alpha','beta','cubic','pseudocubic']
    B0_vals = {ph: fitted[ph]['B0'] for ph in phases_with_B0}
    pseudo_B0 = fitted['pseudocubic']['B0']
    max_other = max(B0_vals[ph] for ph in phases_with_B0 if ph != 'pseudocubic')
    highest = 1.0 if pseudo_B0 > max_other else 0.0
    target = 230.0
    tol_rel = ctx.get('evv_tol_rel', 0.15)
    if abs(pseudo_B0 - target) <= tol_rel * target:
        range_ok = 1.0
    else:
        range_ok = 0.0
    bulk_score = (highest + range_ok) / 2.0
    return 0.5 * order_score + 0.5 * bulk_score


# === block: score_1 (check id='properties_check') ===
def score_1(artifact, step, ctx):
    if 'fitted' not in ctx:
        return 0.0
    if not artifact:
        return 0.0
    for row in artifact:
        if not all(k in row for k in ('phase','equilibrium_energy_eV','equilibrium_volume_ang3','bulk_modulus_GPa')):
            return 0.0
    fitted = ctx['fitted']
    phases = ['alpha','beta','cubic','pseudocubic','graphitic']
    scores = []
    for row in artifact:
        ph = row['phase']
        if ph not in fitted:
            continue
        ref = fitted[ph]
        try:
            e_agent = float(row['equilibrium_energy_eV'])
            v_agent = float(row['equilibrium_volume_ang3'])
            b_agent = float(row['bulk_modulus_GPa'])
        except:
            continue
        e_ok = abs(e_agent - ref['E0']) <= 0.01 * abs(ref['E0']) if abs(ref['E0']) > 1e-6 else True
        v_ok = abs(v_agent - ref['V0']) <= 0.05 * ref['V0']
        b_ok = abs(b_agent - ref['B0']) <= 0.10 * abs(ref['B0']) if abs(ref['B0']) > 1e-6 else True
        phase_score = (e_ok + v_ok + b_ok) / 3.0
        scores.append(phase_score)
    if not scores:
        return 0.0
    return float(np.mean(scores))


_SCORERS = {
    'evv_check': score_0,
    'properties_check': score_1,
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
