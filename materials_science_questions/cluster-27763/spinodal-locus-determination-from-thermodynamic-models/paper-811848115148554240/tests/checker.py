import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, os


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
    steps = spec.get("steps", [])
    expected = {}
    tolerances = {}
    for step in steps:
        if step["id"] == "step_elementary":
            expected = step.get("expected", {})
            tolerances = step.get("tolerances", {})
            break
    return {"expected": expected, "tolerances": tolerances}


# === block: score_0 (check id='step_elementary') ===
def score_0(artifact, step, ctx):
    expected = ctx["expected"]
    tolerances = ctx["tolerances"]
    n_map = {"B20":2,"B11":2,"B02":2,"B30":3,"B21":3,"B12":3,"B03":3,"B40":4,"B31":4,"B22":4,"B13":4,"B04":4}
    tol_n2 = tolerances.get("n2", 0.02)
    tol_n3 = tolerances.get("n3", 0.03)
    tol_n4 = tolerances.get("n4", 0.05)
    eps = 1e-10
    total = 0
    passed = 0
    for temp in ["0.7","1.0","1.15","1.31"]:
        exp_temp = expected.get(temp, {})
        agent_temp = artifact.get(temp, {})
        for coeff in n_map:
            total += 1
            gold = exp_temp.get(coeff, {}).get("value")
            if gold is None:
                continue
            agent_val = agent_temp.get(coeff, {}).get("value")
            if agent_val is None:
                continue
            denom = max(abs(gold), eps)
            rel_err = abs(agent_val - gold) / denom
            n_val = n_map[coeff]
            tol = tol_n2 if n_val == 2 else tol_n3 if n_val == 3 else tol_n4
            if rel_err <= tol:
                passed += 1
    return passed / total if total > 0 else 0.0


# === block: score_1 (check id='step_spinodal') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) < 10:
        return 0.0
    coeff_file = "/app/outputs/elementary_coefficients.json"
    if not os.path.exists(coeff_file):
        return 0.0
    with open(coeff_file) as f:
        coeff_data = json.load(f)
    T = 1.15
    T_key = "1.15"
    B = coeff_data.get(T_key)
    if not B:
        return 0.0
    try:
        B20 = B["B20"]["value"]
        B11 = B["B11"]["value"]
        B02 = B["B02"]["value"]
        B30 = B["B30"]["value"]
        B21 = B["B21"]["value"]
        B12 = B["B12"]["value"]
        B03 = B["B03"]["value"]
        B40 = B["B40"]["value"]
        B31 = B["B31"]["value"]
        B22 = B["B22"]["value"]
        B13 = B["B13"]["value"]
        B04 = B["B04"]["value"]
    except (KeyError, TypeError):
        return 0.0

    def _B2(y):
        return y*y*B20 + 2*y*(1-y)*B11 + (1-y)*(1-y)*B02

    def _B3(y):
        return y**3*B30 + 3*y*y*(1-y)*B21 + 3*y*(1-y)**2*B12 + (1-y)**3*B03

    def _B4(y):
        return y**4*B40 + 4*y**3*(1-y)*B31 + 6*y*y*(1-y)**2*B22 + 4*y*(1-y)**3*B13 + (1-y)**4*B04

    def _P(rho, y):
        return rho * T * (1 + _B2(y)*rho + _B3(y)*rho*rho + _B4(y)*rho**3)

    def _mu1(rho, y):
        if y*rho <= 0:
            return 0.0
        return math.log(y*rho) + 2*rho*(y*B20 + (1-y)*B11) \
               + 1.5*rho*rho*(y*y*B30 + 2*y*(1-y)*B21 + (1-y)*(1-y)*B12) \
               + (4.0/3.0)*rho**3*(y**3*B40 + 3*y*y*(1-y)*B31 + 3*y*(1-y)**2*B22 + (1-y)**3*B13)

    def _dP_drho(rho, y, h=1e-6):
        return (_P(rho+h, y) - _P(rho-h, y)) / (2*h)

    def _dP_dy(rho, y, h=1e-6):
        return (_P(rho, y+h) - _P(rho, y-h)) / (2*h)

    def _dmu1_dy(rho, y, h=1e-6):
        return (_mu1(rho, y+h) - _mu1(rho, y-h)) / (2*h)

    def _stability(rho, y):
        return _dP_drho(rho, y) * (_dmu1_dy(rho, y) - _dP_dy(rho, y)/rho) \
               - (1-y)/(rho*rho) * _dP_dy(rho, y)**2

    max_residual = step.get("max_residual", 1e-6)
    good = 0
    total_points = 0
    for row in artifact:
        try:
            rho = float(row["rho"])
            y1 = float(row["y1"])
        except (ValueError, KeyError):
            continue
        if not (0.001 <= rho <= 0.5 and 0.001 <= y1 <= 0.999):
            continue
        total_points += 1
        if abs(_stability(rho, y1)) <= max_residual:
            good += 1
    if total_points < 10:
        return 0.0
    return good / total_points


_SCORERS = {
    'step_elementary': score_0,
    'step_spinodal': score_1,
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
