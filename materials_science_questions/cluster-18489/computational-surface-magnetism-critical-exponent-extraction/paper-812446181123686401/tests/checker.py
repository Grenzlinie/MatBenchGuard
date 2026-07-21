import os
import json
import csv

# === author imports / helpers ===
import csv, json
from collections import defaultdict

# Pure-Python fallback for numpy functionality needed by the scorer.
class _NumpyFallback:
    @staticmethod
    def array(seq):
        return list(seq)
    @staticmethod
    def diff(arr):
        return [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    @staticmethod
    def min(arr):
        return min(arr) if arr else float('inf')
    @staticmethod
    def max(arr):
        return max(arr) if arr else -float('inf')
    @staticmethod
    def interp(x, xp, fp):
        # 1-D linear interpolation; assumes xp sorted monotonically.
        if not xp or not fp:
            raise ValueError('empty xp/fp')
        if x <= xp[0]:
            return fp[0]
        if x >= xp[-1]:
            return fp[-1]
        for i in range(len(xp)-1):
            if xp[i] <= x <= xp[i+1]:
                t = (x - xp[i]) / (xp[i+1] - xp[i])
                return fp[i] + t * (fp[i+1] - fp[i])
        # fallback (should not reach)
        return fp[-1]

np = _NumpyFallback()


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


# === block: score_0 (check id='phase_boundary') ===
def score_0(artifact, step, ctx):
    params = step.get('params', {})
    js_values = params.get('J_s_prime_values', [2.0, 1.0, 0.0, -1.0])
    critical_targets = params.get('critical_delta_targets', {})
    req_min_pts = params.get('req_min_points', 20)
    eps = 1e-4

    if not artifact:
        return 0.0

    groups = defaultdict(list)
    for row in artifact:
        try:
            js = float(row['J_s_prime_over_J'])
            ds = float(row['delta_s'])
            tc = float(row['T_c_over_T_cb'])
        except (KeyError, ValueError):
            continue
        groups[js].append((ds, tc))

    total_score = 0.0
    for js in js_values:
        curve = groups.get(js, [])
        if len(curve) < req_min_pts:
            continue
        curve.sort(key=lambda x: x[0])
        deltas = np.array([p[0] for p in curve])
        tcs = np.array([p[1] for p in curve])
    
        # monotonic sub-score
        diffs = np.diff(tcs)
        if len(diffs) > 0 and np.min(diffs) >= -eps:
            total_score += 0.05
    
        # critical delta sub-score
        critical_sub = 0.0
        if np.min(tcs) <= 1.0 <= np.max(tcs):
            try:
                critical_ds = np.interp(1.0, tcs, deltas)
            except Exception:
                critical_ds = None
            if critical_ds is not None:
                target = critical_targets.get(str(js), {})
                if js == 0.0:
                    lo = target.get('min', 0.95)
                    hi = target.get('max', 1.05)
                    if lo <= critical_ds <= hi:
                        critical_sub = 0.2
                elif js in (1.0, 2.0):
                    max_val = target.get('max', 0.94)
                    if critical_ds <= max_val:
                        critical_sub = 0.2
                elif js == -1.0:
                    min_val = target.get('min', 1.06)
                    if critical_ds >= min_val:
                        critical_sub = 0.2
        total_score += critical_sub

    return min(1.0, total_score)


_SCORERS = {
    'phase_boundary': score_0,
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
