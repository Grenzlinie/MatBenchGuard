import os
import json
import csv

# === author imports / helpers ===
import json
import os

class _NumpyShim:
    @staticmethod
    def array(seq, dtype=None):
        return list(seq)

    @staticmethod
    def polyfit(x, y, deg):
        if deg != 1:
            raise NotImplementedError
        n = len(x)
        if n == 0:
            return [0.0, 0.0]
        sumx = sum(x)
        sumy = sum(y)
        sumxy = sum(xi * yi for xi, yi in zip(x, y))
        sumxx = sum(xi * xi for xi in x)
        denom = n * sumxx - sumx * sumx
        if denom == 0:
            return [0.0, sumy / n]
        slope = (n * sumxy - sumx * sumy) / denom
        intercept = (sumy - slope * sumx) / n
        return [slope, intercept]

    @staticmethod
    def corrcoef(x, y):
        n = len(x)
        if n < 2:
            return [[1.0, 0.0], [0.0, 1.0]]
        meanx = sum(x) / n
        meany = sum(y) / n
        cov = sum((xi - meanx) * (yi - meany) for xi, yi in zip(x, y))
        varx = sum((xi - meanx) ** 2 for xi in x)
        vary = sum((yi - meany) ** 2 for yi in y)
        if varx == 0 or vary == 0:
            r = 0.0
        else:
            r = cov / (varx * vary) ** 0.5
        return [[1.0, r], [r, 1.0]]

    @staticmethod
    def sum(arr):
        return sum(arr)

    @staticmethod
    def mean(arr):
        return sum(arr) / len(arr) if arr else 0.0

    def __getattr__(self, name):
        raise AttributeError(f"numpy shim does not implement {name}")

np = _NumpyShim()


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


# === block: score_0 (check id='density_check') ===
def score_0(artifact, step, ctx):
    score = 0.0
    ref_values = step.get("ref_values", [])
    if not ref_values:
        return 1.0
    tol = step.get("tolerance_abs", 0.05)
    matched = 0
    artifact_by_eps = {}
    for row in artifact:
        try:
            eps = float(row["epsilon_norm"])
            density = float(row["density_g_cm3"])
            artifact_by_eps[eps] = density
        except:
            pass
    for ref in ref_values:
        eps = float(ref["epsilon_norm"])
        ref_density = float(ref["density_g_cm3"])
        if eps in artifact_by_eps:
            if abs(artifact_by_eps[eps] - ref_density) <= tol:
                matched += 1
    score = matched / len(ref_values)
    return score


# === block: score_1 (check id='modulus_recompute_and_linear') ===
def score_1(artifact, step, ctx):
    # Recompute moduli from tensile_data.json
    tensile_path = "/app/outputs/" + step.get("tensile_data_file", "tensile_data.json")
    if not os.path.exists(tensile_path):
        return 0.0
    with open(tensile_path) as f:
        tensile_data = json.load(f)
    if not isinstance(tensile_data, list):
        return 0.0
    # Group by epsilon_norm, recompute slope
    direction_slopes = {}
    for entry in tensile_data:
        try:
            eps = float(entry["epsilon_norm"])
            direction = str(entry["direction"]).strip()
            strain = np.array(entry["strain"], dtype=float)
            stress = np.array(entry["stress"], dtype=float)
            # fit linear to strain <= 0.02
            mask = strain <= 0.02
            if np.sum(mask) < 2:
                continue
            coeffs = np.polyfit(strain[mask], stress[mask], 1)
            slope = coeffs[0]
            direction_slopes.setdefault(eps, []).append(slope)
        except:
            continue
    # Compute mean slope per epsilon_norm
    recomputed = {}
    for eps, slopes in direction_slopes.items():
        recomputed[eps] = np.mean(slopes)
    # Pointwise accuracy
    ref_moduli = step.get("ref_moduli", [])
    rel_tol = step.get("relative_tolerance", 0.20)
    pointwise_score = 0.0
    count = 0
    for ref in ref_moduli:
        eps = float(ref["epsilon_norm"])
        ref_val = float(ref["young_modulus_GPa"])
        if eps in recomputed:
            val = recomputed[eps]
            if abs(val - ref_val) / max(1e-9, abs(ref_val)) <= rel_tol:
                pointwise_score += 1.0
            count += 1
    if count > 0:
        pointwise_score /= count
    else:
        pointwise_score = 0.0
    # Linearity (R² and slope)
    eps_values = [float(ref["epsilon_norm"]) for ref in ref_moduli]
    moduli = [recomputed.get(eps, 0.0) for eps in eps_values]
    linearity_score = 0.0
    if len(eps_values) >= 2:
        eps_arr = np.array(eps_values)
        mod_arr = np.array(moduli)
        coeffs = np.polyfit(eps_arr, mod_arr, 1)
        slope = coeffs[0]
        # R²
        corr = np.corrcoef(eps_arr, mod_arr)[0,1]
        r_squared = corr**2
        r2_threshold = step.get("r2_threshold", 0.95)
        score_r2 = 1.0 if r_squared >= r2_threshold else 0.0
        slope_gold = step.get("slope_gold", 2.0)
        slope_factor = step.get("slope_factor", 2.0)
        low = slope_gold / slope_factor
        high = slope_gold * slope_factor
        score_slope = 1.0 if low <= slope <= high else 0.0
        linearity_score = 0.5 * score_r2 + 0.5 * score_slope
    else:
        linearity_score = 0.0
    # Combine weights
    pw = step.get("pointwise_weight", 0.7)
    lw = step.get("linearity_weight", 0.3)
    total = pw * pointwise_score + lw * linearity_score
    return total


_SCORERS = {
    'density_check': score_0,
    'modulus_recompute_and_linear': score_1,
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
