import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os
import math
import statistics as _stat

# Pure-Python ndarray-like helper
class _Arr:
    def __init__(self, data, _shape=None):
        if isinstance(data, _Arr):
            self._data = data._data[:]
            self._shape = data._shape
        else:
            self._data = [float(x) for x in data]
            self._shape = _shape if _shape is not None else (len(self._data),)
    def __len__(self):
        return len(self._data)
    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return _Arr(self._data[idx])
        if isinstance(idx, (list, _Arr)):
            return _Arr([self._data[i] for i in idx])
        return self._data[idx]
    def __sub__(self, other):
        if isinstance(other, _Arr):
            return _Arr([a-b for a,b in zip(self._data, other._data)])
        return _Arr([x-other for x in self._data])
    def __add__(self, other):
        if isinstance(other, _Arr):
            return _Arr([a+b for a,b in zip(self._data, other._data)])
        return _Arr([x+other for x in self._data])
    def __mul__(self, other):
        if isinstance(other, _Arr):
            return _Arr([a*b for a,b in zip(self._data, other._data)])
        return _Arr([x*other for x in self._data])
    def __truediv__(self, other):
        if isinstance(other, _Arr):
            return _Arr([a/b for a,b in zip(self._data, other._data)])
        return _Arr([x/other for x in self._data])
    def __neg__(self):
        return _Arr([-x for x in self._data])
    def __ge__(self, other):
        o = other._data if isinstance(other, _Arr) else [other]*len(self)
        return _Arr([1.0 if a>=b else 0.0 for a,b in zip(self._data, o)])
    def __iter__(self):
        return iter(self._data)
    @property
    def shape(self):
        return self._shape

def _np_array(data):
    if isinstance(data, _Arr):
        return _Arr(data)
    return _Arr(data)

def _np_ones_like(arr):
    return _Arr([1.0]*len(arr._data))

def _np_mean(arr):
    if len(arr._data)==0:
        return 0.0
    return math.fsum(arr._data)/len(arr._data)

def _np_clip(arr, a_min, a_max):
    if isinstance(arr, _Arr):
        return _Arr([min(max(x,a_min),a_max) for x in arr._data])
    return min(max(arr,a_min),a_max)

def _np_log(arr):
    if isinstance(arr, _Arr):
        return _Arr([math.log(x) for x in arr._data])
    return math.log(arr)

def _np_argsort(arr):
    seq = arr._data if isinstance(arr, _Arr) else list(arr)
    idxs = list(range(len(seq)))
    idxs.sort(key=lambda i: seq[i])
    return idxs

def _np_column_stack(tup):
    a,b = tup
    n = len(a._data)
    flat = []
    for i in range(n):
        flat.append(a._data[i])
        flat.append(b._data[i])
    arr = _Arr(flat)
    arr._shape = (n,2)
    return arr

def _np_lstsq(A, b_vec, rcond=None):
    # A (n,2), b (n,)
    a0 = [A._data[i*2] for i in range(A._shape[0])]
    a1 = [A._data[i*2+1] for i in range(A._shape[0])]
    bd = b_vec._data if isinstance(b_vec, _Arr) else list(b_vec)
    s00 = math.fsum([x*x for x in a0])
    s01 = math.fsum([x*y for x,y in zip(a0,a1)])
    s11 = math.fsum([y*y for y in a1])
    det = s00*s11 - s01*s01
    if det==0:
        raise ValueError('singular matrix')
    d0 = math.fsum([x*y for x,y in zip(a0,bd)])
    d1 = math.fsum([x*y for x,y in zip(a1,bd)])
    x0 = (s11*d0 - s01*d1)/det
    x1 = (s00*d1 - s01*d0)/det
    # residuals
    resid = math.fsum([(bd[i] - (x0*a0[i]+x1*a1[i]))**2 for i in range(len(bd))])
    return (_Arr([x0,x1]), resid, 2, _Arr([0.0,0.0]))

try:
    import numpy as np
except ImportError:
    class _FakeNumpy:
        array = staticmethod(_np_array)
        ones_like = staticmethod(_np_ones_like)
        mean = staticmethod(_np_mean)
        clip = staticmethod(_np_clip)
        log = staticmethod(_np_log)
        argsort = staticmethod(_np_argsort)
        column_stack = staticmethod(_np_column_stack)
        class linalg:
            @staticmethod
            def lstsq(a, b, rcond=None):
                return _np_lstsq(a, b, rcond)
    np = _FakeNumpy()


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


# === block: score_0 (check id='compute_width_without') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 2:
            return 0.0
        times = np.array([float(r['time']) for r in artifact])
        widths = np.array([float(r['surface_width']) for r in artifact])
        idx = np.argsort(times)
        times = times[idx]
        widths = widths[idx]
        # Monotonicity (allow tiny noise)
        dw = widths[1:] - widths[:-1]
        monotonic_score = np.clip(np.mean(dw >= -1e-6), 0.0, 1.0)
        # Exponent fit for t > 100
        mask = times > 100
        if np.sum(mask) < 5:
            exponent_score = 0.0
        else:
            log_t = np.log(times[mask])
            log_w = np.log(widths[mask])
            A = np.column_stack([log_t, np.ones_like(log_t)])
            beta, _ = np.linalg.lstsq(A, log_w, rcond=None)[0]
            target = step.get('target_beta', 0.5)
            tol = step.get('tolerance', 0.1)
            dev = abs(beta - target)
            if dev <= tol:
                exponent_score = 1.0
            else:
                exponent_score = max(0.0, 1.0 - (dev - tol) / 0.2)
        w_exp = 0.8
        w_mon = 0.2
        return float(w_exp * exponent_score + w_mon * monotonic_score)


# === block: score_1 (check id='compute_width_with') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 2:
            return 0.0
        times = np.array([float(r['time']) for r in artifact])
        widths = np.array([float(r['surface_width']) for r in artifact])
        idx = np.argsort(times)
        times = times[idx]
        widths = widths[idx]
        # Monotonicity
        dw = widths[1:] - widths[:-1]
        monotonic_score = np.clip(np.mean(dw >= -1e-6), 0.0, 1.0)
        # Exponent fit for t > 100
        mask = times > 100
        if np.sum(mask) < 5:
            exponent_score = 0.0
        else:
            log_t = np.log(times[mask])
            log_w = np.log(widths[mask])
            A = np.column_stack([log_t, np.ones_like(log_t)])
            beta, _ = np.linalg.lstsq(A, log_w, rcond=None)[0]
            target = step.get('target_beta', 0.333333)
            tol = step.get('tolerance', 0.1)
            dev = abs(beta - target)
            if dev <= tol:
                exponent_score = 1.0
            else:
                exponent_score = max(0.0, 1.0 - (dev - tol) / 0.2)
        # Coarsening: derivative (dWidth/dt) should be decreasing
        dtimes = times[1:] - times[:-1]
        dwidths = widths[1:] - widths[:-1]
        deriv = dwidths / (dtimes + 1e-12)
        if len(deriv) >= 2 and deriv[-1] < deriv[0] * 0.95:
            coarsening_score = 1.0
        else:
            coarsening_score = 0.0
        w_exp = 0.7
        w_mon = 0.1
        w_coarse = 0.2
        return float(w_exp * exponent_score + w_mon * monotonic_score + w_coarse * coarsening_score)


_SCORERS = {
    'compute_width_without': score_0,
    'compute_width_with': score_1,
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
