import os
import json
import csv

# === author imports / helpers ===
try:
    import numpy as np
except ImportError:
    import math

    class _Array:
        __slots__ = ('data',)
        def __init__(self, data):
            if isinstance(data, (int, float)):
                self.data = [float(data)]
            else:
                self.data = list(data)
        def __iter__(self):
            return iter(self.data)
        def __len__(self):
            return len(self.data)
        def __getitem__(self, i):
            if isinstance(i, _Array):
                # boolean indexing
                return _Array([self.data[j] for j, v in enumerate(i.data) if v])
            if isinstance(i, list) and all(isinstance(x, bool) for x in i):
                return _Array([self.data[j] for j, v in enumerate(i) if v])
            if isinstance(i, slice):
                return _Array(self.data[i])
            return self.data[i]
        def __lt__(self, other):
            if isinstance(other, _Array):
                return _Array([self.data[j] < other.data[j] for j in range(len(self.data))])
            return _Array([x < other for x in self.data])
        def __le__(self, other):
            if isinstance(other, _Array):
                return _Array([self.data[j] <= other.data[j] for j in range(len(self.data))])
            return _Array([x <= other for x in self.data])
        def __gt__(self, other):
            if isinstance(other, _Array):
                return _Array([self.data[j] > other.data[j] for j in range(len(self.data))])
            return _Array([x > other for x in self.data])
        def __ge__(self, other):
            if isinstance(other, _Array):
                return _Array([self.data[j] >= other.data[j] for j in range(len(self.data))])
            return _Array([x >= other for x in self.data])
        def __eq__(self, other):
            if isinstance(other, _Array):
                return _Array([self.data[j] == other.data[j] for j in range(len(self.data))])
            return _Array([x == other for x in self.data])
        def __ne__(self, other):
            if isinstance(other, _Array):
                return _Array([self.data[j] != other.data[j] for j in range(len(self.data))])
            return _Array([x != other for x in self.data])
        def __sub__(self, other):
            if isinstance(other, _Array):
                return _Array([self.data[j] - other.data[j] for j in range(len(self.data))])
            return _Array([x - other for x in self.data])
        def __rsub__(self, other):
            return _Array([other - x for x in self.data])
        def __truediv__(self, other):
            if isinstance(other, _Array):
                return _Array([self.data[j] / other.data[j] for j in range(len(self.data))])
            return _Array([x / other for x in self.data])
        def __abs__(self):
            return _Array([abs(x) for x in self.data])
        def __and__(self, other):
            if isinstance(other, _Array):
                return _Array([self.data[j] and other.data[j] for j in range(len(self.data))])
            return _Array([x and other for x in self.data])
        def __or__(self, other):
            if isinstance(other, _Array):
                return _Array([self.data[j] or other.data[j] for j in range(len(self.data))])
            return _Array([x or other for x in self.data])
        def mean(self):
            if not self.data:
                return 0.0
            # treat booleans as 0/1 for mean computation
            vals = [1 if v is True else v for v in self.data]
            return sum(vals) / len(vals)

    class _NumpyFallback:
        def array(self, data, dtype=None):
            return _Array(data)
        def mean(self, data):
            if isinstance(data, _Array):
                return data.mean()
            if not data:
                return 0.0
            vals = [1 if v is True else v for v in data]
            return sum(vals) / len(vals)
        def abs(self, data):
            return abs(data)
        def all(self, data):
            if isinstance(data, _Array):
                return all(data.data)
            return all(data)
        def any(self, data):
            if isinstance(data, _Array):
                return any(data.data)
            return any(data)
        def corrcoef(self, x, y):
            if isinstance(x, _Array):
                x = x.data
            if isinstance(y, _Array):
                y = y.data
            n = len(x)
            if n < 2:
                return [[1.0, 0.0], [0.0, 1.0]]
            mx = sum(x) / n
            my = sum(y) / n
            cov = sum((x[i]-mx)*(y[i]-my) for i in range(n)) / n
            sx = math.sqrt(sum((xi-mx)**2 for xi in x) / n)
            sy = math.sqrt(sum((yi-my)**2 for yi in y) / n)
            if sx == 0 or sy == 0:
                r = 0.0
            else:
                r = cov / (sx * sy)
            return [[1.0, r], [r, 1.0]]
        def clip(self, a, a_min, a_max):
            try:
                iter(a)
                if isinstance(a, _Array):
                    return _Array([max(a_min, min(x, a_max)) for x in a.data])
                return [max(a_min, min(x, a_max)) for x in a]
            except TypeError:
                return max(a_min, min(a, a_max))
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


# === block: score_0 (check id='scored_best_ann_results') ===
def score_0(artifact, step, ctx):
    import csv

    # Read artifact
    rows = artifact  # artifact is already a list of dicts from the shape gate
    if not rows:
        return 0.0

    sigma = np.array([float(r['sigma_0']) for r in rows])
    val_loss = np.array([float(r['validation_loss']) for r in rows])
    pred_A = np.array([float(r['predicted_A_sigma']) for r in rows])

    N = len(sigma)
    if N != 1000:
        return 0.0

    # Check 1: all predicted_A_sigma < 120°
    fraction_under_120 = np.mean(pred_A < 120.0)
    score_1 = fraction_under_120  # fraction in [0,1]

    # Check 2: amplitude accuracy relative to expected |180 - sigma_0|
    expected_A = np.abs(180.0 - sigma)
    rel_err = np.abs(pred_A - expected_A) / expected_A
    mean_rel_err = np.mean(rel_err)
    # Score: full if mean_rel_err <= 0.10, linear decay to 0 at 0.30
    score_2 = max(0.0, 1.0 - (mean_rel_err - 0.10) / 0.20)

    # Check 3: correlation between validation_loss and |sigma_0 - 180|
    dist_from_centre = np.abs(sigma - 180.0)
    # Use [0][1] indexing to be safe with both numpy and list-of-lists fallback
    rho = np.corrcoef(dist_from_centre, val_loss)[0][1] if len(val_loss) > 1 else 0.0
    # Score 1 if rho > 0.3, 0 otherwise
    score_3 = 1.0 if rho > 0.3 else 0.0

    # Check 4: edges mean loss > centre mean loss (edges: dist > 120°, centre: dist < 60°)
    edge_mask = dist_from_centre > 120.0
    centre_mask = dist_from_centre < 60.0
    edge_mean = val_loss[edge_mask].mean() if np.any(edge_mask) else 0.0
    centre_mean = val_loss[centre_mask].mean() if np.any(centre_mask) else 0.0
    score_4 = 1.0 if edge_mean > centre_mean else 0.0

    # Check 5: loss in reasonable range (0,0.2]
    valid_loss = np.all((val_loss > 0) & (val_loss <= 0.2))
    score_5 = 1.0 if valid_loss else 0.0

    # Combine sub-scores
    final = 0.3 * score_1 + 0.4 * score_2 + 0.15 * score_3 + 0.1 * score_4 + 0.05 * score_5
    return float(np.clip(final, 0.0, 1.0))


_SCORERS = {
    'scored_best_ann_results': score_0,
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
