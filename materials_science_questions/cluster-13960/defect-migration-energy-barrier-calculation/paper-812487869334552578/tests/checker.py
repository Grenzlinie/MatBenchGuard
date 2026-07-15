import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ImportError:
    import math

    class CorrResult:
        def __init__(self, r):
            self._r = r
        def __getitem__(self, key):
            if isinstance(key, tuple):
                i, j = key
                if (i == 0 and j == 0) or (i == 1 and j == 1):
                    return 1.0
                if (i == 0 and j == 1) or (i == 1 and j == 0):
                    return self._r
                raise IndexError
            if key == 0:
                return [1.0, self._r]
            if key == 1:
                return [self._r, 1.0]
            raise IndexError

    class FallbackNp:
        def corrcoef(self, x, y):
            n = len(x)
            sum_x = sum(x)
            sum_y = sum(y)
            sum_xy = sum(xi*yi for xi, yi in zip(x, y))
            sum_x2 = sum(xi*xi for xi in x)
            sum_y2 = sum(yi*yi for yi in y)
            numerator = n * sum_xy - sum_x * sum_y
            denom = math.sqrt((n * sum_x2 - sum_x*sum_x) * (n * sum_y2 - sum_y*sum_y))
            r = numerator / denom if denom != 0 else 0.0
            return CorrResult(r)
        def std(self, vals):
            n = len(vals)
            if n == 0:
                return float('nan')
            mean = sum(vals) / n
            variance = sum((v - mean) ** 2 for v in vals) / n
            return math.sqrt(variance)
        def isnan(self, x):
            try:
                return math.isnan(x)
            except Exception:
                return x != x
    np = FallbackNp()


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


# === block: score_0 (check id='dE_vs_de_correlation') ===
def score_0(artifact, step, ctx):
    x = [float(row['de_per_O']) for row in artifact]
    y = [float(row['dE_V']) for row in artifact]
    if len(x) < 3 or np.std(x) < 1e-12 or np.std(y) < 1e-12:
        return 0.0
    r = np.corrcoef(x, y)[0, 1]
    if np.isnan(r):
        return 0.0
    expected_sign = step.get('expected_sign', 'positive')
    if expected_sign == 'positive' and r < 0:
        return 0.0
    elif expected_sign == 'negative' and r > 0:
        return 0.0
    threshold = step.get('threshold', 0.9)
    if abs(r) >= threshold:
        return 1.0
    score = abs(r) / threshold
    return min(score, 1.0)


# === block: score_1 (check id='barriers_vs_de_correlation') ===
def score_1(artifact, step, ctx):
    x = [float(row['de_per_O']) for row in artifact]
    y = [float(row['barrier_eV']) for row in artifact]
    if len(x) < 3 or np.std(x) < 1e-12 or np.std(y) < 1e-12:
        return 0.0
    r = np.corrcoef(x, y)[0, 1]
    if np.isnan(r):
        return 0.0
    expected_sign = step.get('expected_sign', 'negative')
    if expected_sign == 'positive' and r < 0:
        return 0.0
    elif expected_sign == 'negative' and r > 0:
        return 0.0
    threshold = step.get('threshold', 0.9)
    if abs(r) >= threshold:
        return 1.0
    score = abs(r) / threshold
    return min(score, 1.0)


_SCORERS = {
    'dE_vs_de_correlation': score_0,
    'barriers_vs_de_correlation': score_1,
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
