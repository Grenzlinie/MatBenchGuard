import os
import json
import csv

# === author imports / helpers ===
import csv
import math

# Lightweight NumPy-compatible replacements for common operations (no external dependency)
# ============================================================================
class NumpyArray(list):
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return NumpyArray(x * other for x in self)
        return NotImplemented
    def __rmul__(self, other):
        return self.__mul__(other)
    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return NumpyArray(x ** other for x in self)
        return NotImplemented

class _MockNumpy:
    @staticmethod
    def array(data, dtype=None):
        return NumpyArray(data)
    @staticmethod
    def polyfit(x, y, deg):
        # only deg=1 is used
        x_vals = list(x)
        y_vals = list(y)
        n = len(x_vals)
        if n == 0:
            return [0.0, 0.0]
        sum_x = sum(x_vals)
        sum_y = sum(y_vals)
        sum_xy = sum(xi * yi for xi, yi in zip(x_vals, y_vals))
        sum_x2 = sum(xi * xi for xi in x_vals)
        denom = n * sum_x2 - sum_x * sum_x
        if denom == 0:
            slope = 0.0
        else:
            slope = (n * sum_xy - sum_x * sum_y) / denom
        intercept = (sum_y - slope * sum_x) / n
        return [slope, intercept]
    @staticmethod
    def corrcoef(x, y):
        x_vals = list(x)
        y_vals = list(y)
        n = len(x_vals)
        if n == 0:
            return [[1.0, 0.0], [0.0, 1.0]]
        mean_x = sum(x_vals) / n
        mean_y = sum(y_vals) / n
        if n > 1:
            cov = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x_vals, y_vals)) / (n - 1)
            std_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x_vals) / (n - 1))
            std_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y_vals) / (n - 1))
        else:
            cov = 0.0
            std_x = 1.0
            std_y = 1.0
        if std_x == 0 or std_y == 0:
            corr = 0.0
        else:
            corr = cov / (std_x * std_y)
        return [[1.0, corr], [corr, 1.0]]

np = _MockNumpy()


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
    spec_gold = spec.get('gold_data', {})
    step = spec['steps'][0]
    return {
        'gold_data': spec_gold,
        'tol_rel': float(step.get('tolerance_slope_rel', 0.01)),
        'tol_abs_min': float(step.get('tolerance_abs_min', 1e9)),
        'r2_threshold': float(step.get('r2_threshold', 0.95)),
        'co_slope_threshold': float(step.get('co_slope_threshold', 5e10))
    }


# === block: score_0 (check id='step_linear_fit') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    samples = ['sample_1_Fe', 'sample_2_Fe', 'Co']
    rows = {}
    for row in artifact:
        sid = row.get('sample_id', '').strip()
        if sid:
            rows[sid] = row
    gold_data = ctx['gold_data']
    tol_rel = ctx['tol_rel']
    tol_abs_min = ctx['tol_abs_min']
    r2_thr = ctx['r2_threshold']
    co_slope_thr = ctx['co_slope_threshold']
    # Compute gold regression parameters
    gold = {}
    for sid, data in gold_data.items():
        P = np.array(data['P'], dtype=float)
        n_10p18 = np.array(data['n_10p18'], dtype=float)
        n_cm3 = n_10p18 * 1e18
        n23 = n_cm3 ** (2/3)  # cm^{-2}
        coeffs = np.polyfit(P, n23, 1)
        slope_gold = coeffs[0]
        intercept_gold = coeffs[1]
        # Compute R² manually to avoid tuple-indexing on list-of-lists from the mock corrcoef
        y_fit = [coeffs[0]*px + coeffs[1] for px in data['P']]
        y_mean = sum(n23) / len(n23)
        ss_res = sum((yi - yf)**2 for yi, yf in zip(n23, y_fit))
        ss_tot = sum((yi - y_mean)**2 for yi in n23)
        corr = 1.0 - ss_res / ss_tot if ss_tot != 0 else 0.0
        gold[sid] = (slope_gold, intercept_gold, corr)

    def check_val(agent_val, gold_val):
        max_diff = max(tol_abs_min, abs(gold_val) * tol_rel)
        return 1.0 if abs(agent_val - gold_val) <= max_diff else 0.0

    per_sample = {}
    for sid in samples:
        row = rows.get(sid)
        if row is None:
            per_sample[sid] = 0.0
            continue
        try:
            agent_s = float(row.get('slope', '0'))
            agent_i = float(row.get('intercept', '0'))
            agent_r2 = float(row.get('r_squared', '0'))
        except (ValueError, TypeError):
            per_sample[sid] = 0.0
            continue
        if sid == 'Co':
            per_sample[sid] = 1.0 if abs(agent_s) < co_slope_thr else 0.0
        else:
            gs, gi, gr2 = gold[sid]
            score_s = check_val(agent_s, gs)
            score_i = check_val(agent_i, gi)
            # R²: full credit if >= threshold, otherwise proportional
            if agent_r2 >= r2_thr:
                score_r2 = 1.0
            else:
                score_r2 = max(0.0, agent_r2 / r2_thr) if r2_thr > 0 else 0.0
            per_sample[sid] = 0.6 * score_s + 0.3 * score_i + 0.1 * score_r2

    final = (per_sample['sample_1_Fe'] + per_sample['sample_2_Fe'] + per_sample['Co']) / 3.0
    return float(final)


_SCORERS = {
    'step_linear_fit': score_0,
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
