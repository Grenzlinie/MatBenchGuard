import os
import json
import csv

# === author imports / helpers ===
import os
from math import sqrt


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
    ambient_path = os.path.join(outputs_dir, "ambient_properties.csv")
    ambient = load_artifact(ambient_path)
    ambient_dict = {}
    if ambient is not None:
        for row in ambient:
            prop = row.get("property", "").strip()
            val_str = row.get("value", "")
            try:
                val = float(val_str)
                ambient_dict[prop] = val
            except:
                pass
    cp = ambient_dict.get("specific_heat_CP_J_per_mol_K", None)
    return {"ambient_cp": cp}


# === block: score_0 (check id='ambient_properties') ===
def score_0(artifact, step, ctx):
    gold = step.get("properties", {})
    score = 0.0
    count = 0
    for row in artifact:
        prop = row.get("property", "").strip()
        val_str = row.get("value", "")
        try:
            val = float(val_str)
        except:
            continue
        if prop in gold:
            g = gold[prop]["gold"]
            tol = gold[prop]["tolerance"]
            if abs(val - g) <= tol:
                score += 1.0
            count += 1
    if count > 0:
        return score / count
    else:
        return 0.0


# === block: score_1 (check id='pressure_dependence') ===
def score_1(artifact, step, ctx):
    checks = step.get("checks", {})
    if not artifact or len(artifact) < 3:
        return 0.0

    pressures = []
    kt = []
    cp = []
    for row in artifact:
        try:
            p = float(row["pressure_GPa"])
            k = float(row["bulk_modulus_Kt_GPa"])
            c = float(row["specific_heat_CP_J_per_mol_K"])
        except:
            continue
        pressures.append(p)
        kt.append(k)
        cp.append(c)

    def linear_fit(x, y):
        n = len(x)
        if n < 2:
            return None, None
        mean_x = sum(x)/n
        mean_y = sum(y)/n
        num = sum((xi-mean_x)*(yi-mean_y) for xi,yi in zip(x,y))
        den = sum((xi-mean_x)**2 for xi in x)
        if den == 0:
            return None, None
        slope = num/den
        intercept = mean_y - slope*mean_x
        ss_res = sum((yi - (slope*xi+intercept))**2 for xi,yi in zip(x,y))
        ss_tot = sum((yi-mean_y)**2 for yi in y)
        r2 = 1 - ss_res/ss_tot if ss_tot != 0 else 1.0
        return slope, max(0.0, min(1.0, r2))

    slope_kt, r2_kt = linear_fit(pressures, kt)
    slope_cp, r2_cp = linear_fit(pressures, cp)

    score_kt = 0.0
    if slope_kt is not None and r2_kt is not None:
        slope_ok = checks["bulk_modulus_slope_range"][0] <= slope_kt <= checks["bulk_modulus_slope_range"][1]
        r2_ok = r2_kt >= checks["bulk_modulus_r2_min"]
        if slope_ok and r2_ok:
            score_kt = 1.0

    score_cp = 0.0
    if slope_cp is not None and r2_cp is not None:
        slope_sign_ok = (checks["cp_slope_sign"] == "negative" and slope_cp < 0) or (checks["cp_slope_sign"] == "positive" and slope_cp > 0)
        mag_ok = checks["cp_slope_magnitude_range"][0] <= abs(slope_cp) <= checks["cp_slope_magnitude_range"][1]
        r2_ok = r2_cp >= checks["cp_r2_min"]
        if slope_sign_ok and mag_ok and r2_ok:
            score_cp = 1.0

    ambient_cp = ctx.get("ambient_cp", None)
    consistency = 0.0
    if ambient_cp is not None and cp:
        cp0 = cp[0] if cp else None
        if cp0 is not None and abs(cp0 - ambient_cp) <= checks["cp_cross_tolerance"]:
            consistency = 1.0

    total = 0.4*score_kt + 0.4*score_cp + 0.2*consistency
    return total


_SCORERS = {
    'ambient_properties': score_0,
    'pressure_dependence': score_1,
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
