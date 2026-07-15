import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ImportError:
    import math

    class _Array(list):
        def max(self):
            return max(self)
        def sum(self):
            return sum(self)

    class _np:
        @staticmethod
        def array(iterable):
            return _Array(iterable)

        @staticmethod
        def log(values):
            return _Array(math.log(v) for v in values)

        @staticmethod
        def polyfit(x, y, deg):
            if deg != 1:
                raise NotImplementedError
            n = len(x)
            sx = sum(x)
            sy = sum(y)
            sxx = sum(v * v for v in x)
            sxy = sum(vx * vy for vx, vy in zip(x, y))
            denom = n * sxx - sx * sx
            if denom == 0:
                return [0.0, 0.0]
            slope = (n * sxy - sx * sy) / denom
            intercept = (sy - slope * sx) / n
            return [slope, intercept]

        @staticmethod
        def ones_like(arr, dtype=None):
            n = len(arr)
            if dtype == bool:
                return _Array([True] * n)
            return _Array([1.0] * n)

        @staticmethod
        def abs(values):
            if isinstance(values, _Array):
                return _Array(abs(v) for v in values)
            return abs(values)

    np = _np()


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
    import os
    import csv
    import math


    def _fit_beta(csv_path):
        if not os.path.exists(csv_path):
            return None
        times = []
        velocities = []
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            if 'time' not in reader.fieldnames or 'velocity' not in reader.fieldnames:
                return None
            for row in reader:
                try:
                    t = float(row['time'])
                    v = float(row['velocity'])
                    times.append(t)
                    velocities.append(v)
                except (ValueError, KeyError):
                    continue
        if len(times) < 10:
            return None
        max_t = max(times)
        threshold = 0.3 * max_t
        mask = [t > threshold for t in times]
        if sum(mask) < 5:
            mask = [True] * len(times)
        filtered_times = [t for i, t in enumerate(times) if mask[i]]
        filtered_vels = [v for i, v in enumerate(velocities) if mask[i]]
        if len(filtered_times) < 2:
            return None
        log_t = [math.log(t) for t in filtered_times]
        log_v = [math.log(v) for v in filtered_vels]
        n = len(log_t)
        sx = sum(log_t)
        sy = sum(log_v)
        sxx = sum(x * x for x in log_t)
        sxy = sum(x * y for x, y in zip(log_t, log_v))
        denom = n * sxx - sx * sx
        if denom == 0:
            return None
        slope = (n * sxy - sx * sy) / denom
        return -slope


    ctx = {}
    ctx['beta_high_comp'] = _fit_beta('/app/outputs/velocity_highT.csv')
    ctx['beta_low_comp'] = _fit_beta('/app/outputs/velocity_lowT.csv')
    return ctx


# === block: score_0 (check id='beta_highT_recompute') ===
def score_0(artifact, step, ctx):
    comp = ctx.get('beta_high_comp')
    if comp is None:
        return 0.0
    target = step.get('target')
    tol = step.get('tolerance_abs', 0.05)
    return 1.0 if abs(comp - target) <= tol else 0.0


# === block: score_1 (check id='beta_lowT_recompute') ===
def score_1(artifact, step, ctx):
    comp = ctx.get('beta_low_comp')
    if comp is None:
        return 0.0
    target = step.get('target')
    tol = step.get('tolerance_abs', 0.05)
    return 1.0 if abs(comp - target) <= tol else 0.0


# === block: score_2 (check id='beta_json_consistency') ===
def score_2(artifact, step, ctx):
    if artifact is None:
        return 0.0
    b_high = artifact.get('beta_highT')
    b_low = artifact.get('beta_lowT')
    if b_high is None or b_low is None:
        return 0.0
    target_high = step.get('target_highT')
    target_low = step.get('target_lowT')
    tol = step.get('tolerance_abs', 0.05)
    score = 0.0
    if abs(b_high - target_high) <= tol:
        score += 0.5
    if abs(b_low - target_low) <= tol:
        score += 0.5
    return score


_SCORERS = {
    'beta_highT_recompute': score_0,
    'beta_lowT_recompute': score_1,
    'beta_json_consistency': score_2,
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
