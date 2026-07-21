import os
import json
import csv

# === author imports / helpers ===
import math

class ndarray:
    def __init__(self, data):
        if isinstance(data, ndarray):
            self.data = data.data
        elif isinstance(data, (list, tuple)):
            self.data = [float(x) if not isinstance(x, float) else x for x in data]
        else:
            try:
                self.data = [float(data)]
            except TypeError:
                self.data = [float(x) for x in data]
    def __iter__(self):
        return iter(self.data)
    def __len__(self):
        return len(self.data)
    def __getitem__(self, i):
        return self.data[i]
    def __setitem__(self, i, v):
        self.data[i] = v
    def __sub__(self, other):
        if isinstance(other, ndarray):
            return ndarray([a - b for a, b in zip(self.data, other.data)])
        return ndarray([a - other for a in self.data])
    def __rsub__(self, other):
        return ndarray([other - a for a in self.data])
    def __truediv__(self, other):
        if isinstance(other, ndarray):
            return ndarray([a / b for a, b in zip(self.data, other.data)])
        return ndarray([a / other for a in self.data])
    def __rtruediv__(self, other):
        return ndarray([other / a for a in self.data])
    def __mul__(self, other):
        if isinstance(other, ndarray):
            return ndarray([a * b for a, b in zip(self.data, other.data)])
        return ndarray([a * other for a in self.data])
    def __rmul__(self, other):
        return ndarray([other * a for a in self.data])
    def __abs__(self):
        return ndarray([abs(a) for a in self.data])
    def __pow__(self, power):
        return ndarray([a ** power for a in self.data])

class _Np:
    @staticmethod
    def sqrt(x):
        if isinstance(x, ndarray):
            return ndarray([math.sqrt(v) for v in x.data])
        return math.sqrt(x)
    @staticmethod
    def maximum(a, b):
        a_arr = ndarray(a) if not isinstance(a, ndarray) else a
        b_arr = ndarray(b) if not isinstance(b, ndarray) else b
        return ndarray([max(aa, bb) for aa, bb in zip(a_arr.data, b_arr.data)])
    @staticmethod
    def clip(a, a_min, a_max):
        if isinstance(a, ndarray):
            return ndarray([max(a_min, min(a_max, v)) for v in a.data])
        return max(a_min, min(a_max, a))
    @staticmethod
    def log(x):
        if isinstance(x, ndarray):
            return ndarray([math.log(v) for v in x.data])
        return math.log(x)
    @staticmethod
    def exp(x):
        if isinstance(x, ndarray):
            return ndarray([math.exp(v) for v in x.data])
        return math.exp(x)
    @staticmethod
    def arctan(x):
        if isinstance(x, ndarray):
            return ndarray([math.atan(v) for v in x.data])
        return math.atan(x)
    @staticmethod
    def abs(x):
        if isinstance(x, ndarray):
            return abs(x)
        return abs(x)
    @staticmethod
    def array(lst):
        return ndarray(lst)
    @staticmethod
    def linspace(start, stop, num):
        if num <= 1:
            return ndarray([stop])
        step = (stop - start) / (num - 1)
        return ndarray([start + i * step for i in range(num)])
    @staticmethod
    def logspace(start, stop, num, base=10.0):
        return ndarray([base ** v for v in _Np.linspace(start, stop, num).data])
    @staticmethod
    def argmax(arr):
        if isinstance(arr, ndarray):
            data = arr.data
        else:
            data = list(arr)
        return max(range(len(data)), key=lambda i: data[i])
    @staticmethod
    def mean(arr):
        if isinstance(arr, ndarray):
            data = arr.data
        else:
            data = list(arr)
        if not data:
            return 0.0
        return sum(data) / len(data)
    @staticmethod
    def sum(arr):
        if isinstance(arr, ndarray):
            data = arr.data
        else:
            data = list(arr)
        return sum(data)

try:
    import numpy as np
except ImportError:
    np = _Np()


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
    def prepare(outputs_dir, spec):
        step = spec['steps'][0]
        params = step['params']
        eps = params['epsilon']
        eta2 = params['eta2']
        rho = params['rho']
        c = params['c']
        mu = params['mu']
        Nc = params['Nc']
        Delta_J = params['Delta_J']
        xi_J = params['xi_J']
        omega = params['omega']
        T0 = params['T0_illum']
        q = 1.602176634e-19
        kB = 1.380649e-23
        E_c_J = -0.68 * Delta_J
        prefactor = 0.7 * omega * np.sqrt(rho / c) * eta2 / Delta_J
        def alpha_T(sigma):
            sigma = np.maximum(sigma, 1e-30)
            A = q * mu * Nc
            ratio = sigma / A
            ratio = np.clip(ratio, 1e-30, 1 - 1e-12)
            T = (xi_J - E_c_J) / (kB * np.log(ratio))
            T = np.clip(T, 1e-3, 1e4)
            tau = eps / sigma
            exp_arg = 2.1 * Delta_J / (kB * T)
            exp_arg = np.clip(exp_arg, -100, 100)
            exp_term = np.exp(exp_arg)
            arg = (omega * tau * exp_term) / (1 + (omega * tau)**2 * exp_term)
            alpha = prefactor * (kB * T) * np.arctan(arg)
            return alpha
        def alpha_I(sigma):
            sigma = np.maximum(sigma, 1e-30)
            tau = eps / sigma
            exp_arg = 2.1 * Delta_J / (kB * T0)
            exp_term = np.exp(exp_arg)
            arg = (omega * tau * exp_term) / (1 + (omega * tau)**2 * exp_term)
            alpha = prefactor * (kB * T0) * np.arctan(arg)
            return alpha
        return {'params': params, 'alpha_T': alpha_T, 'alpha_I': alpha_I}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        try:
            curves = artifact['curves']
            tm = artifact['temperature_maximum']
            im = artifact['illumination_maximum']
            ver = artifact['verification']
        except KeyError:
            return 0.0
        params = ctx['params']
        eps = params['epsilon']
        omega = params['omega']
        expected_homo = eps * omega
        # 1. Curve match
        curve_scores = []
        for sc in curves:
            scenario = sc['scenario']
            sigma_a = np.array(sc['sigma'])
            alpha_a = np.array(sc['alpha'])
            if scenario == 'temperature':
                expected = ctx['alpha_T'](sigma_a)
            else:
                expected = ctx['alpha_I'](sigma_a)
            denom = np.maximum(np.abs(expected), 1e-12)
            rel_err = np.abs(alpha_a - expected) / denom
            mean_rel = np.mean(rel_err)
            if mean_rel <= 1e-6:
                c_score = 1.0
            else:
                c_score = max(0.0, 1.0 - (mean_rel - 1e-6) / (1e-3 - 1e-6))
            curve_scores.append(c_score)
        curve_score = 0.5*curve_scores[0] + 0.5*curve_scores[1] if len(curve_scores)==2 else 0.0
        # 2. Peak match
        q = 1.602176634e-19
        kB = 1.380649e-23
        mu = params['mu']
        Nc = params['Nc']
        Delta_J = params['Delta_J']
        xi_J = params['xi_J']
        E_c_J = -0.68*Delta_J
        A = q * mu * Nc
        T_grid = np.linspace(300, 900, 2000)
        sigma_T_arr = A * np.exp((xi_J - E_c_J) / (kB * T_grid))
        alpha_T_arr = ctx['alpha_T'](sigma_T_arr)
        idx_T = np.argmax(alpha_T_arr)
        sigma_T_ref = sigma_T_arr[idx_T]
        alpha_T_ref = alpha_T_arr[idx_T]
        sigma_I_arr = np.logspace(-7, -1, 2000)
        alpha_I_arr = ctx['alpha_I'](sigma_I_arr)
        idx_I = np.argmax(alpha_I_arr)
        sigma_I_ref = sigma_I_arr[idx_I]
        alpha_I_ref = alpha_I_arr[idx_I]
        def peak_score(val, ref, rel_tol=0.01):
            eps = 1e-20
            rel = abs(val - ref) / max(eps, abs(ref))
            if rel <= rel_tol:
                return 1.0
            else:
                return max(0.0, 1.0 - (rel - rel_tol) / (rel_tol*10))
        sigma_T_sc = peak_score(tm.get('sigma_T', 0), sigma_T_ref)
        alpha_T_sc = peak_score(tm.get('alpha_T', 0), alpha_T_ref)
        sigma_I_sc = peak_score(im.get('sigma_I', 0), sigma_I_ref)
        alpha_I_sc = peak_score(im.get('alpha_I', 0), alpha_I_ref)
        peak_sc = 0.25*(sigma_T_sc+alpha_T_sc+sigma_I_sc+alpha_I_sc)
        # 3. Booleans
        expected_gt = bool(sigma_T_ref > sigma_I_ref)
        expected_neq = bool(abs(sigma_T_ref - expected_homo)/max(1e-20, expected_homo) > 0.01)
        bool_sc = 0.0
        if ver.get('sigma_T_gt_sigma_I') == expected_gt:
            bool_sc += 0.5
        if ver.get('sigma_T_not_equal_homogeneous') == expected_neq:
            bool_sc += 0.5
        total = 0.5*curve_score + 0.3*peak_sc + 0.2*bool_sc
        return total


_SCORERS = {
    'step_01': score_0,
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
