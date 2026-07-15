import os
import json
import csv

# === author imports / helpers ===
import sys, types, math, builtins

class _Array(list):
    def __ge__(self, other):
        return _Array(x >= other for x in self)
    def __le__(self, other):
        return _Array(x <= other for x in self)
    def __and__(self, other):
        if isinstance(other, _Array):
            return _Array(a and b for a,b in zip(self, other))
        raise TypeError
    def __bool__(self):
        return any(self)

class _NpModule(types.ModuleType):
    def __init__(self):
        super().__init__('numpy')
    def asarray(self, obj, dtype=None):
        if isinstance(obj, _Array):
            return obj
        return _Array(obj)
    def sum(self, arr, axis=None):
        if isinstance(arr, _Array):
            return builtins.sum(1 for x in arr if x)
        return builtins.sum(arr)
    def any(self, arr):
        if isinstance(arr, _Array):
            return builtins.any(arr)
        return builtins.any(arr)
    def std(self, arr):
        if isinstance(arr, _Array):
            vals = list(arr)
        else:
            vals = list(arr)
        n = len(vals)
        if n == 0:
            return 0.0
        mean = builtins.sum(vals)/n
        var = builtins.sum((v-mean)**2 for v in vals)/n
        return math.sqrt(var)

numpy = _NpModule()
sys.modules['numpy'] = numpy
import numpy as np


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
    import numpy as np

    ctx = {}
    for step in spec.get("steps", []):
        if step.get("id") == "struct_check":
            p = step.get("parameters", {})
            ctx["m1_short"] = p.get("m1_short_range", [2.35, 2.65])
            ctx["m1_long"] = p.get("m1_long_range", [3.0, 3.3])
            ctx["m1_peak_frac"] = p.get("m1_peak_min_fraction", 0.5)
            ctx["m1_angle"] = p.get("m1_angle_tol", [7.0, 8.5])
            ctx["m1_angle_frac"] = p.get("m1_angle_frac", 0.5)
            ctx["r_short_max"] = p.get("r_short_max", 2.65)
            ctx["r_long_min"] = p.get("r_long_min", 2.85)
            ctx["r_angle_min"] = p.get("r_angle_min", 1.0)
            ctx["r_std_min"] = p.get("r_std_min", 0.12)
            break
    return ctx


# === block: score_0 (check id='struct_check') ===
def score_0(artifact, step, ctx):
    import numpy as np

    def _score_m1(data, ctx):
        dists = np.asarray(data.get("distances", []), dtype=float)
        angles = np.asarray(data.get("angles", []), dtype=float)
        total = len(dists)
        if total == 0:
            return 0.0

        lo, hi = ctx["m1_short"]
        short = np.sum((dists >= lo) & (dists <= hi))
        lo, hi = ctx["m1_long"]
        long_ = np.sum((dists >= lo) & (dists <= hi))
        peak_frac = ctx["m1_peak_frac"]
        if short > 0 and long_ > 0:
            dist_score = min(1.0, (short + long_) / (peak_frac * total))
        else:
            dist_score = 0.0

        lo, hi = ctx["m1_angle"]
        angle_ok = np.sum((angles >= lo) & (angles <= hi))
        angle_score = min(1.0, angle_ok / (ctx["m1_angle_frac"] * total))
        return 0.5 * dist_score + 0.5 * angle_score

    def _score_r(data, ctx):
        dists = np.asarray(data.get("distances", []), dtype=float)
        angles = np.asarray(data.get("angles", []), dtype=float)
        if len(dists) == 0:
            return 0.0

        has_short = np.any(dists <= ctx["r_short_max"])
        has_long = np.any(dists >= ctx["r_long_min"])
        if has_short and has_long:
            dist_score = 1.0
        elif has_short or has_long:
            dist_score = 0.5
        else:
            dist_score = 0.0

        has_tilt = np.any([a > ctx["r_angle_min"] for a in angles])
        angle_score = 1.0 if has_tilt else 0.0

        std_dist = np.std(dists)
        std_score = 1.0 if std_dist > ctx["r_std_min"] else 0.0
        return (dist_score + angle_score + std_score) / 3.0

    m1_single_score = _score_m1(artifact.get("M1_single", {}), ctx)
    m1_ge03_score = _score_m1(artifact.get("M1_Ge03", {}), ctx)
    r_single_score = _score_r(artifact.get("R_single", {}), ctx)
    r_ge03_score = _score_r(artifact.get("R_Ge03", {}), ctx)
    score = (m1_single_score + m1_ge03_score + r_single_score + r_ge03_score) / 4.0
    return score


_SCORERS = {
    'struct_check': score_0,
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
