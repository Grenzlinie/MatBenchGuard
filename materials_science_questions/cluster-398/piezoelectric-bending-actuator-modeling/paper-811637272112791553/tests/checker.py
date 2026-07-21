import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
    from scipy.signal import find_peaks
except ImportError:
    import sys
    import builtins

    # Minimal fallback for numpy array-like behaviour
    class _NDArray(list):
        def __getitem__(self, idx):
            if isinstance(idx, (int, slice)):
                return super().__getitem__(idx)
            return _NDArray([self[i] for i in idx])
        def __abs__(self):
            return _NDArray([abs(v) for v in self])
        def __le__(self, other):
            return [v <= other for v in self]
        def __sub__(self, other):
            return _NDArray([v - other for v in self])
        def __truediv__(self, other):
            return _NDArray([v / other for v in self])

    def _array(data, dtype=None):
        if isinstance(data, list):
            return _NDArray(data)
        return _NDArray(list(data))

    def _where(cond):
        return [i for i, c in enumerate(cond) if c]

    def _abs(x):
        if isinstance(x, _NDArray):
            return _NDArray([abs(v) for v in x])
        return abs(x)

    def _argmin(x):
        return min(range(len(x)), key=lambda i: x[i])

    _np = type(sys)("np")
    _np.array = _array
    _np.where = _where
    _np.abs = _abs
    _np.argmin = _argmin
    np = _np

    def find_peaks(x, prominence=None, height=None, width=None):
        # Simple local maxima detector
        if len(x) < 3:
            return [], {}
        peaks = []
        for i in range(1, len(x)-1):
            if x[i] > x[i-1] and x[i] > x[i+1]:
                peaks.append(i)
        prominences = []
        for idx in peaks:
            left_base = x[idx]
            for j in range(idx-1, -1, -1):
                if x[j] < x[idx]:
                    left_base = x[j]
                    break
            else:
                left_base = min(x[:idx]) if idx > 0 else x[0]
            right_base = x[idx]
            for j in range(idx+1, len(x)):
                if x[j] < x[idx]:
                    right_base = x[j]
                    break
            else:
                right_base = min(x[idx:]) if idx < len(x)-1 else x[-1]
            prominences.append(x[idx] - max(left_base, right_base))
        return peaks, {"prominences": prominences}


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


# === block: score_0 (check id='check_bumps') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 100:
        return 0.0
    try:
        omega = np.array([float(row['omega_over_Omega_n']) for row in artifact])
        current = np.array([float(row['relative_current']) for row in artifact])
    except (KeyError, ValueError):
        return 0.0
    if len(omega) != len(current) or len(omega) < 100:
        return 0.0

    peaks, props = find_peaks(current, prominence=(None, None))
    if len(peaks) == 0:
        return 0.0
    peak_omegas = omega[peaks]
    prominences = props['prominences']
    expected = [1.0, 2.0, 3.0, 4.0]
    tol = 0.05
    found = 0
    for exp in expected:
        matches = np.where(np.abs(peak_omegas - exp) <= tol)[0]
        if len(matches) > 0:
            idx = matches[np.argmin(np.abs(peak_omegas[matches] - exp))]
            prom = prominences[idx]
            peak_val = current[peaks][idx]
            if peak_val > 0 and prom / peak_val >= 0.1:
                found += 1
    return found / 4.0


_SCORERS = {
    'check_bumps': score_0,
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
