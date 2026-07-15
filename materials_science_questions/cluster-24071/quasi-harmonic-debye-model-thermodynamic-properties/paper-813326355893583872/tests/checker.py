import os
import json
import csv

# === author imports / helpers ===
from math import log10


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
    return {"ref": spec["reference_data"]}


# === block: score_0 (check id='thermo_numeric') ===
def score_0(artifact, step, ctx):
    import csv, math

    rows = artifact
    step_cfg = step
    ref_data = ctx["ref"]
    tol_cfg = step_cfg["tolerances"]

    total = 0
    passed = 0

    def get_expected(method, condition, T, P, prop):
        mref = ref_data.get(method)
        if not mref:
            return None
        sweep = mref.get(condition)
        if not sweep:
            return None
        if prop == "bulk_modulus_K_GPa":
            coeffs = sweep.get("K_coeffs")
            if not coeffs: return None
            return coeffs[0] + coeffs[1]*P + coeffs[2]*P*P
        elif prop == "K_prime":
            coeffs = sweep.get("K_prime_coeffs")
            if not coeffs: return None
            return coeffs[0] + coeffs[1]*P
        elif prop == "K_double_prime":
            val = sweep.get("K_double_prime")
            if val is None: return None
            return val
        elif prop == "thermal_expansivity_alpha_1e6_K":
            if condition == "temperature_sweep":
                points = sweep.get("alpha_points")
                if not points: return None
                if T <= points[0][0]:
                    return points[0][1]
                for i in range(len(points)-1):
                    if T <= points[i+1][0]:
                        t1, a1 = points[i]
                        t2, a2 = points[i+1]
                        return a1 + (a2 - a1) * (T - t1) / (t2 - t1)
                return points[-1][1]
            else:
                return None
        return None

    for row in rows:
        method = row.get("method","").strip()
        T_str = row.get("temperature_K","").strip()
        P_str = row.get("pressure_GPa","").strip()
        if not T_str or not P_str:
            continue
        T = float(T_str)
        P = float(P_str)
        condition = None
        if abs(T - 300.0) < 0.5:
            condition = "pressure_sweep"
        elif abs(P) < 0.5:
            condition = "temperature_sweep"
        else:
            continue
        for prop in ["bulk_modulus_K_GPa","K_prime","K_double_prime","thermal_expansivity_alpha_1e6_K"]:
            expected = get_expected(method, condition, T, P, prop)
            if expected is None:
                continue
            val_str = row.get(prop, "").strip()
            if val_str == "":
                total += 1
                continue
            try:
                val = float(val_str)
            except:
                total += 1
                continue
            total += 1
            tol_info = tol_cfg.get(prop)
            if not tol_info:
                passed += 1
                continue
            if tol_info["type"] == "absolute":
                if abs(val - expected) <= tol_info["value"]:
                    passed += 1
            else:
                if abs(expected) < 1e-12:
                    if abs(val) < 1e-12:
                        passed += 1
                else:
                    if abs((val - expected) / expected) <= tol_info["value"]:
                        passed += 1

    if total == 0:
        return 0.0
    return min(1.0, passed / total)


# === block: score_1 (check id='low_t_slope') ===
def score_1(artifact, step, ctx):
    import math

    rows = artifact
    step_cfg = step
    spec = step_cfg.get("structural_spec", {})
    method_req = spec.get("method", "QHD")
    T_max = spec.get("temperature_max", 500)
    expected_slope = spec.get("expected_slope", 3.0)
    tol = spec.get("slope_tolerance", 0.5)

    logT_vals = []
    logA_vals = []

    for row in rows:
        if row.get("method","").strip() != method_req:
            continue
        T_str = row.get("temperature_K","").strip()
        P_str = row.get("pressure_GPa","").strip()
        alpha_str = row.get("thermal_expansivity_alpha_1e6_K","").strip()
        if not T_str or not P_str or not alpha_str:
            continue
        T = float(T_str)
        P = float(P_str)
        if T <= 0 or T >= T_max:
            continue
        if abs(P) > 0.5:
            continue
        alpha = float(alpha_str)
        if alpha <= 0:
            continue
        logT_vals.append(math.log10(T))
        logA_vals.append(math.log10(alpha))

    n = len(logT_vals)
    if n < 2:
        return 0.0

    sum_x = sum(logT_vals)
    sum_y = sum(logA_vals)
    sum_xy = sum(x*y for x,y in zip(logT_vals, logA_vals))
    sum_xx = sum(x*x for x in logT_vals)

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    if abs(slope - expected_slope) <= tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'thermo_numeric': score_0,
    'low_t_slope': score_1,
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
