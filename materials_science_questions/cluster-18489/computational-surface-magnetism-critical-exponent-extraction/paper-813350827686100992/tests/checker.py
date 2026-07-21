import os
import json
import csv

# === author imports / helpers ===
import math

# --- numpy fallback ---
class np:
    class _Array:
        def __init__(self, data):
            self._data = [float(x) for x in data]
        def __repr__(self):
            return repr(self._data)
        def __len__(self):
            return len(self._data)
        def __getitem__(self, idx):
            return self._data[idx]
        def __iter__(self):
            return iter(self._data)
        def __truediv__(self, other):
            if isinstance(other, (int, float)):
                return np._Array([x / other for x in self._data])
            return NotImplemented
        def __rtruediv__(self, other):
            if isinstance(other, (int, float)):
                return np._Array([other / x for x in self._data])
            return NotImplemented
        def __sub__(self, other):
            if isinstance(other, (int, float)):
                return np._Array([x - other for x in self._data])
            return NotImplemented
        def __rsub__(self, other):
            if isinstance(other, (int, float)):
                return np._Array([other - x for x in self._data])
            return NotImplemented
        def __add__(self, other):
            if isinstance(other, (int, float)):
                return np._Array([x + other for x in self._data])
            return NotImplemented
        def __radd__(self, other):
            return self.__add__(other)
        def __mul__(self, other):
            if isinstance(other, (int, float)):
                return np._Array([x * other for x in self._data])
            return NotImplemented
        def __rmul__(self, other):
            return self.__mul__(other)
        def __neg__(self):
            return np._Array([-x for x in self._data])
        def __le__(self, other):
            if isinstance(other, (int, float)):
                return [x <= other for x in self._data]
            return NotImplemented
        def __lt__(self, other):
            if isinstance(other, (int, float)):
                return [x < other for x in self._data]
            return NotImplemented

    @staticmethod
    def array(iterable, dtype=None):
        return np._Array(iterable)

    @staticmethod
    def log(arr):
        if isinstance(arr, np._Array):
            return np._Array([math.log(x) for x in arr._data])
        return np._Array([math.log(x) for x in arr])

    @staticmethod
    def exp(val):
        if isinstance(val, np._Array):
            return np._Array([math.exp(x) for x in val._data])
        return math.exp(val)

    @staticmethod
    def any(iterable):
        return any(iterable)

# --- linregress fallback ---
try:
    from scipy.stats import linregress
except ImportError:
    def linregress(x, y):
        n = len(x)
        if n < 2:
            raise ValueError
        sumx = sum(x)
        sumy = sum(y)
        sumxy = sum(xi*yi for xi, yi in zip(x, y))
        sumx2 = sum(xi*xi for xi in x)
        denom = n * sumx2 - sumx * sumx
        if denom == 0:
            slope = 0.0
            intercept = sumy / n
        else:
            slope = (n * sumxy - sumx * sumy) / denom
            intercept = (sumy - slope * sumx) / n
        # Return an object with the attributes used by the scorer body
        return type('', (object,), {
            'slope': slope,
            'intercept': intercept,
            'r_value': 0.0,
            'p_value': 0.0,
            'std_err': 0.0
        })()


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
        'Tc_inf': 0.221654,
        'nu_inv': 1.5625,
        'gold_a': 0.98,
        'tol_a': 0.2,
        'tol_slope': 0.2,
        'gold_B': 1.57,
        'tol_B': 0.15,
        'gold_Cplus': 1.058,
        'tol_Cplus': 0.15
    }


# === block: score_0 (check id='extract_tc') ===
def score_0(artifact, step, ctx):
    if artifact is None or len(artifact) == 0:
        return 0.0
    try:
        Ns = np.array([float(row['N']) for row in artifact])
        Tcs = np.array([float(row['Tc']) for row in artifact])
    except (KeyError, ValueError):
        return 0.0
    Tc_inf = ctx['Tc_inf']
    nu_inv = ctx['nu_inv']
    delta = 1.0 - Tcs / Tc_inf
    if np.any(delta <= 0) or len(Ns) < 3:
        return 0.0
    log_delta = np.log(delta)
    log_N = np.log(Ns)
    slope, intercept, r_value, p_value, std_err = linregress(log_N, log_delta)
    a_fit = np.exp(intercept)
    slope_score = 1.0 if abs(slope + nu_inv) <= ctx['tol_slope'] else max(0.0, 1.0 - (abs(slope + nu_inv) - ctx['tol_slope']) / 0.2)
    a_score = 1.0 if abs(a_fit - ctx['gold_a']) <= ctx['tol_a'] else max(0.0, 1.0 - (abs(a_fit - ctx['gold_a']) - ctx['tol_a']) / ctx['tol_a'])
    return 0.3 * slope_score + 0.7 * a_score


# === block: score_1 (check id='fit_a') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict) or 'a' not in artifact:
        return 0.0
    a = float(artifact['a'])
    if abs(a - ctx['gold_a']) <= ctx['tol_a']:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='scaling_amps') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict) or 'B' not in artifact or 'Cplus' not in artifact:
        return 0.0
    B = float(artifact['B'])
    Cp = float(artifact['Cplus'])
    b_score = 1.0 if abs(B - ctx['gold_B']) <= ctx['tol_B'] else 0.0
    c_score = 1.0 if abs(Cp - ctx['gold_Cplus']) <= ctx['tol_Cplus'] else 0.0
    return (b_score + c_score) / 2.0


_SCORERS = {
    'extract_tc': score_0,
    'fit_a': score_1,
    'scaling_amps': score_2,
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
