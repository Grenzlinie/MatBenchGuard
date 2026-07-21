import os
import json
import csv

# === author imports / helpers ===
import bisect
import math

class _Array(list):
    def __ne__(self, other):
        if isinstance(other, (int, float)):
            return [v != other for v in self]
        return [v != o for v, o in zip(self, other)]

class _NumpyEmu:
    @staticmethod
    def array(seq, dtype=None):
        return _Array(seq)

    @staticmethod
    def linspace(start, stop, num):
        if num <= 0:
            return []
        if num == 1:
            return [start]
        step = (stop - start) / (num - 1)
        return [start + i * step for i in range(num)]

    @staticmethod
    def interp(x, xp, fp, left=None, right=None):
        result = []
        for xi in x:
            idx = bisect.bisect_left(xp, xi)
            if idx == 0:
                y = fp[0]
            elif idx >= len(xp):
                y = fp[-1]
            else:
                x0, x1 = xp[idx-1], xp[idx]
                y0, y1 = fp[idx-1], fp[idx]
                if x1 == x0:
                    y = y0
                else:
                    y = y0 + (xi - x0) * (y1 - y0) / (x1 - x0)
            result.append(y)
        return result

    @staticmethod
    def sign(x):
        if isinstance(x, (int, float)):
            return 1 if x > 0 else -1 if x < 0 else 0
        return _Array(1 if v > 0 else -1 if v < 0 else 0 for v in x)

    @staticmethod
    def diff(x):
        if len(x) < 2:
            return _Array()
        return _Array(x[i+1] - x[i] for i in range(len(x)-1))

    @staticmethod
    def where(condition):
        if isinstance(condition, (bool, int)):
            return ([0],) if condition else ([],)
        indices = [i for i, v in enumerate(condition) if v]
        return (indices,)

    @staticmethod
    def max(seq):
        return max(seq)

    @staticmethod
    def min(seq):
        return min(seq)

    @staticmethod
    def mean(seq):
        if len(seq) == 0:
            return 0.0
        return sum(seq) / len(seq)

    @staticmethod
    def argmin(seq):
        return min(range(len(seq)), key=lambda i: seq[i])

    @staticmethod
    def argmax(seq):
        return max(range(len(seq)), key=lambda i: seq[i])

np = _NumpyEmu()

def find_peaks(x, prominence=0.0):
    if len(x) < 3:
        return [], {}
    peaks = []
    for i in range(1, len(x)-1):
        if x[i] > x[i-1] and x[i] > x[i+1]:
            if prominence > 0:
                base = min(x[i-1], x[i+1])
                if (x[i] - base) >= prominence:
                    peaks.append(i)
            else:
                peaks.append(i)
    return peaks, {}


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


# === block: score_0 (check id='results_check') ===
def score_0(artifact, step, ctx):
    def _find_intersection(T1, U1, T2, U2):
        t_min = max(np.min(T1), np.min(T2))
        t_max = min(np.max(T1), np.max(T2))
        if t_min >= t_max:
            return None
        t_grid = np.linspace(t_min, t_max, 1000)
        u1_interp = np.interp(t_grid, T1, U1)
        u2_interp = np.interp(t_grid, T2, U2)
        # _Array does not implement __sub__; use list comprehension for element-wise subtraction
        diff = [u1 - u2 for u1, u2 in zip(u1_interp, u2_interp)]
        signs = np.sign(diff)
        crossings = np.where(np.diff(signs) != 0)[0]
        if len(crossings) == 0:
            return None
        idx = crossings[0]
        t_cross = t_grid[idx] - diff[idx] * (t_grid[idx+1] - t_grid[idx]) / (diff[idx+1] - diff[idx])
        return t_cross

    def _get_U_data(rdata, sizes):
        U_data = rdata.get('U_data', {})
        out = {}
        for s in sizes:
            key = f'L{s}'
            d = U_data.get(key)
            if d and 'T' in d and 'U' in d:
                out[s] = (np.array(d['T'], dtype=float), np.array(d['U'], dtype=float))
        return out

    sub_weights = step.get('sub_weights', {})
    score = 0.0
    r02_T_N_avg = None
    r07_T_N_avg = None

    for r_key, T_range in [('r0.2', (1.65, 1.9)), ('r0.7', (2.3, 2.7))]:
        rdata = artifact.get(r_key)
        if not rdata:
            continue
        U_sizes = _get_U_data(rdata, [20, 80, 150])
        intersections = []
        for pair in [(20, 80), (20, 150), (80, 150)]:
            if pair[0] in U_sizes and pair[1] in U_sizes:
                T_cross = _find_intersection(U_sizes[pair[0]][0], U_sizes[pair[0]][1],
                                             U_sizes[pair[1]][0], U_sizes[pair[1]][1])
                if T_cross is not None:
                    intersections.append(T_cross)
        if len(intersections) >= 2:
            max_diff = max(intersections) - min(intersections)
            if max_diff <= step.get('intersection_tolerance', 0.02):
                wn = f'U_intersection_{r_key}'
                score += sub_weights.get(wn, 0.0)
                T_N_avg = float(np.mean(intersections))
                if r_key == 'r0.2':
                    r02_T_N_avg = T_N_avg
                else:
                    r07_T_N_avg = T_N_avg

    if r02_T_N_avg is not None and r07_T_N_avg is not None:
        r02_ok = 1.65 <= r02_T_N_avg <= 1.9
        r07_ok = 2.3 <= r07_T_N_avg <= 2.7
        trend_ok = (r07_T_N_avg > r02_T_N_avg)
        w = sub_weights.get('T_N_accuracy_trend', 0.0)
        if r02_ok and r07_ok:
            if trend_ok:
                score += w
            else:
                score += 0.5 * w
        else:
            if trend_ok:
                score += 0.3 * w
            else:
                score += 0.0

    for r_key in ['r0.2', 'r0.7']:
        rdata = artifact.get(r_key)
        if not rdata:
            continue
        V_data = rdata.get('V_data', {})
        L150 = V_data.get('L150')
        if L150 and 'T' in L150 and 'V' in L150:
            T_arr = np.array(L150['T'], dtype=float)
            V_arr = np.array(L150['V'], dtype=float)
            if len(T_arr) > 0:
                idx_min = np.argmin(T_arr)
                V_min = V_arr[idx_min]
                V_range = step.get('V_limit_range', [0.64, 0.68])
                if V_range[0] <= V_min <= V_range[1]:
                    score += sub_weights.get(f'V_limit_{r_key}', 0.0)

    for r_key in ['r0.2', 'r0.7']:
        rdata = artifact.get(r_key)
        if not rdata:
            continue
        hist = rdata.get('histogram')
        if hist and 'counts' in hist:
            counts = np.array(hist['counts'], dtype=int)
            if len(counts) > 0 and np.max(counts) > 0:
                peaks, _ = find_peaks(counts, prominence=0.01 * np.max(counts))
                if len(peaks) == 1:
                    score += sub_weights.get(f'histogram_{r_key}', 0.0)

    return min(score, 1.0)


_SCORERS = {
    'results_check': score_0,
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
