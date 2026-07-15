import os
import json
import csv

# === author imports / helpers ===
import csv, os, json
import math

try:
    import numpy as np
except ImportError:
    class _NpArray(list):
        def __lt__(self, other):
            if isinstance(other, (int, float)):
                return [float(item) < other for item in self]
            return NotImplemented
        def __mul__(self, other):
            if isinstance(other, (int, float)):
                return _NpArray([item * other for item in self])
            return NotImplemented
        def __rmul__(self, other):
            if isinstance(other, (int, float)):
                return _NpArray([other * item for item in self])
            return NotImplemented
        def __add__(self, other):
            if isinstance(other, (int, float)):
                return _NpArray([item + other for item in self])
            return NotImplemented
        def __radd__(self, other):
            if isinstance(other, (int, float)):
                return _NpArray([other + item for item in self])
            return NotImplemented
        def __sub__(self, other):
            if isinstance(other, (int, float)):
                return _NpArray([item - other for item in self])
            return NotImplemented
        def __rsub__(self, other):
            if isinstance(other, (int, float)):
                return _NpArray([other - item for item in self])
            return NotImplemented
        def __truediv__(self, other):
            if isinstance(other, (int, float)):
                return _NpArray([item / other for item in self])
            return NotImplemented
        def __rtruediv__(self, other):
            if isinstance(other, (int, float)):
                return _NpArray([other / item for item in self])
            return NotImplemented
        def __getitem__(self, index):
            if isinstance(index, list) and all(isinstance(x, bool) for x in index):
                return _NpArray([self[i] for i, v in enumerate(index) if v])
            return super().__getitem__(index)
    def _where(cond, x, y):
        if isinstance(x, (list, _NpArray)):
            x_vals = list(x)
        else:
            x_vals = [x] * len(cond)
        if isinstance(y, (list, _NpArray)):
            y_vals = list(y)
        else:
            y_vals = [y] * len(cond)
        return _NpArray([x_vals[i] if cond[i] else y_vals[i] for i in range(len(cond))])
    def _power(arr, exp):
        return _NpArray([math.pow(v, exp) for v in arr])
    def _maximum(arr, val):
        return _NpArray([max(v, val) for v in arr])
    def _mean(arr):
        vals = list(arr)
        return sum(vals) / len(vals) if vals else 0.0
    class _np:
        @staticmethod
        def array(x, dtype=None):
            return _NpArray(list(x))
        where = _where
        power = _power
        maximum = _maximum
        mean = _mean
    np = _np()

try:
    from scipy.optimize import curve_fit
except ImportError:
    curve_fit = None


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


# === block: score_0 (check id='densification_threshold') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        expected = float(step.get('expected_p_crit', 8.0))
        tol_abs = float(step.get('abs_tol', 2.5))
        resid_tol = float(step.get('resid_tol', 0.005))

        cycles = {}
        for row in artifact:
            cid = int(row['cycle_id'])
            if cid not in cycles:
                cycles[cid] = {'load': [], 'unload': []}
            phase = row['loading_phase'].strip().lower()
            if phase not in ('load', 'unload'):
                continue
            cycles[cid][phase].append(row)

        threshold = None
        for cid, data in cycles.items():
            if not data['load'] or not data['unload']:
                continue
            p_max = max(float(r['pressure']) for r in data['load'])
            best_unload = min(data['unload'], key=lambda r: float(r['pressure']))
            final_vol = float(best_unload['volume_norm'])
            residual = 1.0 - final_vol
            if residual > resid_tol:
                if threshold is None or p_max < threshold:
                    threshold = p_max

        if threshold is None:
            return 0.0
        diff = abs(threshold - expected)
        if diff <= tol_abs:
            return 1.0
        max_diff = 3.0 * tol_abs
        if diff >= max_diff:
            return 0.0
        return 1.0 - (diff - tol_abs) / (max_diff - tol_abs)


# === block: score_1 (check id='critical_state_line') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if curve_fit is None:
            return 0.0
        min_points = int(step.get('min_points', 6))
        if len(artifact) < min_points:
            return 0.0

        p_vals, qc_vals = [], []
        for row in artifact:
            try:
                p = float(row['confining_pressure'])
                qc = float(row['critical_shear_stress_qc'])
            except (ValueError, KeyError):
                continue
            p_vals.append(p)
            qc_vals.append(qc)

        if len(p_vals) < min_points:
            return 0.0

        p_arr = np.array(p_vals)
        q_arr = np.array(qc_vals)

        def model(x, p1, qt, pt, B, beta):
            return np.where(x < p1,
                            qt * (p1 - x) / (p1 - pt),
                            B * np.power(np.maximum(x, 1e-9), beta))

        p0 = [10.0, 7.0, -8.0, 1.2, 0.5]
        bounds = ([1.0, 1.0, -15.0, 0.1, 0.1],
                  [20.0, 15.0, -1.0, 5.0, 1.0])
        try:
            popt, _ = curve_fit(model, p_arr, q_arr, p0=p0, bounds=bounds, maxfev=20000)
        except Exception:
            return 0.0

        expected = {
            'p1': float(step.get('expected_p1', 12.337)),
            'qt': float(step.get('expected_qt', 7.402)),
            'pt': float(step.get('expected_pt', -8.5)),
            'B': float(step.get('expected_B', 1.168)),
            'beta': float(step.get('expected_beta', 0.5))
        }
        tolerances = step.get('tolerances', {})
        if not tolerances:
            return 0.0
        tol = {
            'p1': float(tolerances.get('p1_abs', 3.0)),
            'qt': float(tolerances.get('qt_abs', 2.0)),
            'pt': float(tolerances.get('pt_abs', 2.0)),
            'B': float(tolerances.get('B_abs', 0.3)),
            'beta': float(tolerances.get('beta_abs', 0.1))
        }
        params_order = ['p1', 'qt', 'pt', 'B', 'beta']
        fitted = dict(zip(params_order, popt))

        scores = []
        for key in params_order:
            diff = abs(fitted[key] - expected[key])
            s = max(0.0, 1.0 - diff / tol[key])
            scores.append(s)
        return float(np.mean(scores))


_SCORERS = {
    'densification_threshold': score_0,
    'critical_state_line': score_1,
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
