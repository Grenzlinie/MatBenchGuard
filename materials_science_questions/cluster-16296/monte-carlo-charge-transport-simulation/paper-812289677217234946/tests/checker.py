import os
import json
import csv

# === author imports / helpers ===
import math
import bisect

class _Array:
    def __init__(self, data):
        self.data = list(data)
    def __len__(self):
        return len(self.data)
    def __iter__(self):
        return iter(self.data)
    def __getitem__(self, idx):
        if isinstance(idx, _Array) and idx.data and isinstance(idx.data[0], bool):
            return _Array([x for x, b in zip(self.data, idx.data) if b])
        return self.data[idx]
    def __setitem__(self, idx, val):
        self.data[idx] = val
    def __neg__(self):
        return _Array([-a for a in self.data])
    def __abs__(self):
        return _Array([abs(a) for a in self.data])
    def __add__(self, other):
        if isinstance(other, _Array):
            return _Array([a + b for a, b in zip(self.data, other.data)])
        return _Array([a + other for a in self.data])
    def __radd__(self, other):
        return self + other
    def __sub__(self, other):
        if isinstance(other, _Array):
            return _Array([a - b for a, b in zip(self.data, other.data)])
        return _Array([a - other for a in self.data])
    def __rsub__(self, other):
        return _Array([other - a for a in self.data])
    def __mul__(self, other):
        if isinstance(other, _Array):
            return _Array([a * b for a, b in zip(self.data, other.data)])
        return _Array([a * other for a in self.data])
    def __rmul__(self, other):
        return self * other
    def __truediv__(self, other):
        if isinstance(other, _Array):
            return _Array([a / b for a, b in zip(self.data, other.data)])
        return _Array([a / other for a in self.data])
    def __pow__(self, exp):
        return _Array([a ** exp for a in self.data])
    def __ge__(self, other):
        if isinstance(other, _Array):
            return _Array([a >= b for a, b in zip(self.data, other.data)])
        return _Array([a >= other for a in self.data])
    def __le__(self, other):
        if isinstance(other, _Array):
            return _Array([a <= b for a, b in zip(self.data, other.data)])
        return _Array([a <= other for a in self.data])
    def __gt__(self, other):
        if isinstance(other, _Array):
            return _Array([a > b for a, b in zip(self.data, other.data)])
        return _Array([a > other for a in self.data])
    def __lt__(self, other):
        if isinstance(other, _Array):
            return _Array([a < b for a, b in zip(self.data, other.data)])
        return _Array([a < other for a in self.data])
    def __and__(self, other):
        return _Array([a and b for a, b in zip(self.data, other.data)])
    def min(self):
        return min(self.data)
    def max(self):
        return max(self.data)
    def mean(self):
        return sum(self.data) / len(self.data)
    def __repr__(self):
        return f'_Array({self.data})'

class _numpy:
    def array(self, obj, dtype=None):
        return _Array(obj)
    def arange(self, start, stop=None, step=None):
        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1
        return _Array([start + i*step for i in range(int(math.ceil((stop - start)/step)))])
    def zeros_like(self, arr):
        return _Array([0.0] * len(arr.data))
    def mean(self, arr):
        return sum(arr.data) / len(arr.data)
    def abs(self, arr):
        return _Array([abs(x) for x in arr.data])
    def exp(self, arr):
        return _Array([math.exp(x) for x in arr.data])
    def min(self, arr):
        return min(arr.data)
    def max(self, arr):
        return max(arr.data)
np = _numpy()

def _pearsonr(x, y):
    n = len(x.data)
    if n < 2:
        return 0.0, 1.0
    mx = sum(x.data) / n
    my = sum(y.data) / n
    cov = sum((xi - mx)*(yi - my) for xi, yi in zip(x.data, y.data)) / (n - 1)
    sx = math.sqrt(sum((xi - mx)**2 for xi in x.data) / (n - 1))
    sy = math.sqrt(sum((yi - my)**2 for yi in y.data) / (n - 1))
    if sx == 0 or sy == 0:
        return 0.0, 1.0
    return cov / (sx * sy), 1.0
pearsonr = _pearsonr

def interp1d(x, y, kind='linear', bounds_error=False, fill_value='extrapolate'):
    xs = x.data if isinstance(x, _Array) else list(x)
    ys = y.data if isinstance(y, _Array) else list(y)
    def interpolate(xq):
        if isinstance(xq, _Array):
            return _Array([interpolate(xi) for xi in xq.data])
        xi = xq
        if xi < xs[0]:
            if fill_value == 'extrapolate':
                return ys[0] + (ys[1]-ys[0])/(xs[1]-xs[0])*(xi - xs[0])
            else:
                return fill_value
        if xi > xs[-1]:
            if fill_value == 'extrapolate':
                return ys[-1] + (ys[-1]-ys[-2])/(xs[-1]-xs[-2])*(xi - xs[-1])
            else:
                return fill_value
        i = bisect.bisect_left(xs, xi)
        if i == 0:
            return ys[0]
        if i == len(xs):
            return ys[-1]
        x0, x1 = xs[i-1], xs[i]
        y0, y1 = ys[i-1], ys[i]
        return y0 + (xi - x0) * (y1 - y0) / (x1 - x0)
    return interpolate


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
        for step in spec.get('steps', []):
            if step.get('id') == 'derivative':
                p = step['gold_params']
                e_min, e_max, step_size = p['e_min'], p['e_max'], p['step']
                energy = np.arange(e_min, e_max + step_size/2, step_size)
                d2 = (p['amp_gamma'] * np.exp(-((energy - p['mu_gamma'])**2) / (2 * p['sigma_gamma']**2)) +
                      p['amp_L'] * np.exp(-((energy - p['mu_L'])**2) / (2 * p['sigma_L']**2)))
                return {'gold_energy': energy, 'gold_d2': d2, 'step': step}
        raise ValueError('gold curve step not found')


# === block: score_0 (check id='derivative') ===
def score_0(artifact, step, ctx):
        # Guard against a missing or malformed context (e.g., prepare returned None)
        if not isinstance(ctx, dict) or 'gold_energy' not in ctx or 'gold_d2' not in ctx:
            return 0.0

        # Robust parsing with sorting
        energies_raw = []
        vals_raw = []
        for row in artifact:
            try:
                e = float(row.get('energy_eV', None) or '')
                d = float(row.get('d2_alpha', None) or '')
            except (ValueError, TypeError):
                continue
            energies_raw.append(e)
            vals_raw.append(d)
        if len(energies_raw) < 5:
            return 0.0

        sorted_pairs = sorted(zip(energies_raw, vals_raw), key=lambda p: p[0])
        energies = [p[0] for p in sorted_pairs]
        d2_vals = [p[1] for p in sorted_pairs]
        agent_energy = np.array(energies)
        agent_d2 = np.array(d2_vals)

        agent_e_min, agent_e_max = agent_energy.min(), agent_energy.max()
        gold_energy = ctx['gold_energy']
        gold_d2 = ctx['gold_d2']
        gold_e_min, gold_e_max = gold_energy[0], gold_energy[-1]
        common_min = max(agent_e_min, gold_e_min)
        common_max = min(agent_e_max, gold_e_max)
        if common_max <= common_min:
            return 0.0
        overlap_mask = (gold_energy >= common_min) & (gold_energy <= common_max)
        gold_overlap = gold_d2[overlap_mask]
        interp = interp1d(agent_energy, agent_d2, kind='linear', bounds_error=False, fill_value='extrapolate')
        agent_overlap = interp(gold_energy[overlap_mask])

        def minmax(arr):
            amin, amax = arr.min(), arr.max()
            if amax - amin < 1e-12:
                return np.zeros_like(arr)
            return (arr - amin) / (amax - amin)

        gold_norm = minmax(gold_overlap)
        agent_norm = minmax(agent_overlap)
        if len(gold_norm) < 5:
            return 0.0

        r, _ = pearsonr(gold_norm, agent_norm)
        mae = np.mean(np.abs(gold_norm - agent_norm))

        corr_threshold = 0.95
        if r >= corr_threshold:
            corr_score = 1.0
        else:
            corr_score = max(0.0, (r - 0.5) / (corr_threshold - 0.5))

        mae_threshold = 0.05
        if mae <= mae_threshold:
            mae_score = 1.0
        else:
            mae_score = max(0.0, 1.0 - (mae - mae_threshold) / 0.2)

        final_score = (corr_score + mae_score) / 2.0
        return min(1.0, max(0.0, final_score))


_SCORERS = {
    'derivative': score_0,
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
