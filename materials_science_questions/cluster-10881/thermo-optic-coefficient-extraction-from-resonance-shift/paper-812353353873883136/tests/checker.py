import os
import json
import csv

# === author imports / helpers ===
import math, json


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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    def finesse_from_R(R):
        if R <= 0 or R >= 1:
            return float('inf')
        F = 4*R/(1-R)**2
        return (math.pi/2) / math.asin(1/math.sqrt(F+2))

    tolerance = step.get("tolerance", 0.5)
    score_elements = []
    for row in artifact:
        if not isinstance(row, dict):
            continue
        try:
            R = float(row["R"])
        except (KeyError, ValueError):
            score_elements.append(0.0)
            continue
        expected = finesse_from_R(R)
        try:
            agent_val = float(row["theoretical_finesse"])
        except:
            agent_val = None
        if agent_val is None or math.isnan(agent_val) or math.isinf(agent_val):
            score_elements.append(0.0)
        else:
            err = abs(agent_val - expected)
            score_elements.append(1.0 if err <= tolerance else 0.0)
    if not score_elements:
        return 0.0
    return sum(score_elements)/len(score_elements)


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    measured_finesse_map = {
        (0.01, 0.9): 20,
        (0.24, 0.8): 10,
        (1.0, 0.8): 13,
        (10.0, 0.8): 6,
        (100.0, 0.7): 3
    }

    def finesse_from_R(R):
        if R <= 0 or R >= 1:
            return float('inf')
        F = 4*R/(1-R)**2
        return (math.pi/2) / math.asin(1/math.sqrt(F+2))

    def expected_effective_reflectance(L, R_nominal, measured_fe):
        lo, hi = 0.0, 1.0
        for _ in range(100):
            mid = (lo+hi)/2
            fe = finesse_from_R(mid)
            if fe > measured_fe:
                hi = mid
            else:
                lo = mid
        return (lo+hi)/2

    tolerance = step.get("tolerance", 0.02)
    score_elements = []
    for row in artifact:
        try:
            L = float(row["L"])
            R_nom = float(row["R_nominal"])
            key = (L, R_nom)
            if key not in measured_finesse_map:
                score_elements.append(0.0)
                continue
            measured_fe = measured_finesse_map[key]
            expected_Re = expected_effective_reflectance(L, R_nom, measured_fe)
            agent_Re = float(row["effective_reflectance"])
        except (KeyError, ValueError):
            score_elements.append(0.0)
            continue
        err = abs(agent_Re - expected_Re)
        score_elements.append(1.0 if err <= tolerance else 0.0)
    if not score_elements:
        return 0.0
    return sum(score_elements)/len(score_elements)


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    n = 1.46
    dn_dT = 1.1e-5
    p11 = 0.121
    p12 = 0.270
    nu = 0.17

    layers = [
        {"E": 730e8, "S": 0.012e-6, "alpha": 0.004e-4},
        {"E": 0.01e8, "S": 0.11e-6, "alpha": 2.5e-4},
        {"E": 5.5e8, "S": 0.52e-6, "alpha": 1e-4}
    ]

    def compute_beta(layers_subset):
        numerator = 0.0
        denominator = 0.0
        for l in layers_subset:
            numerator += l["alpha"] * l["E"] * l["S"]
            denominator += l["E"] * l["S"]
        return numerator / denominator

    def compute_S_phase(beta, alpha1):
        term1 = dn_dT / n
        coeff = (n**2 / 2) * ((p11 + p12)*nu - p12)
        term2 = coeff * (beta - alpha1)
        return term1 + term2 + beta

    alpha1 = layers[0]["alpha"]
    beta_jacketed = compute_beta(layers)
    beta_unjacketed = compute_beta([layers[0]])

    expected_jacketed = compute_S_phase(beta_jacketed, alpha1)
    expected_unjacketed = compute_S_phase(beta_unjacketed, alpha1)

    tol = step.get("tolerance", {})
    tol_j = tol.get("jacketed_S_phase", 5e-6)
    tol_u = tol.get("unjacketed_S_phase", 1e-6)

    score_j = 0.0
    score_u = 0.0
    if "jacketed_S_phase" in artifact:
        err = abs(artifact["jacketed_S_phase"] - expected_jacketed)
        if err <= tol_j:
            score_j = 1.0
    if "unjacketed_S_phase" in artifact:
        err = abs(artifact["unjacketed_S_phase"] - expected_unjacketed)
        if err <= tol_u:
            score_u = 1.0
    return (score_j + score_u) / 2.0


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
