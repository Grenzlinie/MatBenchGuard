import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    import math

    RTOL = step.get("tolerance_relative", 1e-6)
    ATOL = step.get("tolerance_absolute", 1e-12)
    columns = step["columns"]
    params = step["params"]
    theta_D = params["theta_D"]
    eps_c_d3 = params["eps_c_d3"]
    eps_c_d2 = params["eps_c_d2"]

    def is_close(a, b):
        return abs(a - b) <= ATOL + RTOL * max(abs(a), abs(b))

    def compute_P(T, d, f, eps_c):
        # Eqn (10) of the paper
        sinh_term = 2.0 * math.sinh(theta_D / (2.0 * T))
        P = 0.108 * (T ** 2.5) / f * (sinh_term ** d) * math.exp(-11600.0 * eps_c / T)
        return P

    # Map column name -> (d, f)
    col_map = {
        "P_d3_f1e-3": (3, 1e-3, eps_c_d3),
        "P_d3_f1e-4": (3, 1e-4, eps_c_d3),
        "P_d2_f1e-3": (2, 1e-3, eps_c_d2),
        "P_d2_f1e-4": (2, 1e-4, eps_c_d2),
    }

    rows = artifact
    if not rows:
        return 0.0
    ok = 0
    for row in rows:
        T = float(row["T"])
        row_ok = True
        for col in columns:
            d, f, eps_c = col_map[col]
            expected = compute_P(T, d, f, eps_c)
            actual = float(row[col])
            if not is_close(actual, expected):
                row_ok = False
                break
        if row_ok:
            ok += 1
    return ok / len(rows)


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    import math

    RTOL = step.get("tolerance_relative", 1e-6)
    ATOL = step.get("tolerance_absolute", 1e-12)
    columns = step["columns"]
    params = step["params"]
    theta_D = params["theta_D"]
    eps_c_d3 = params["eps_c_d3"]
    eps_c_d2 = params["eps_c_d2"]
    eps_a = params["eps_a"]
    k_perp = params["k_perp"]
    k_par = params["k_par"]

    def is_close(a, b):
        return abs(a - b) <= ATOL + RTOL * max(abs(a), abs(b))

    def compute_Z1_over_q1(T, d, eps_c):
        # Eqn (15)
        factor = 2.0 * math.exp(-11600.0 * (eps_c - eps_a) / T)
        sinh_D = 2.0 * math.sinh(theta_D / (2.0 * T))
        factor *= (sinh_D ** d)
        factor *= (2.0 * math.sinh(0.719 * k_perp / T)) ** (-1)
        factor *= (2.0 * math.sinh(0.719 * k_par / T)) ** (-2)
        return factor

    def compute_theta(T, d, f, eps_c):
        # Eqns (14) and (15)
        Z1_over_q1 = compute_Z1_over_q1(T, d, eps_c)
        X = 41.1 * ((1.0 - f) / f) * Z1_over_q1
        theta = X / (1.0 + X)
        return theta

    # Map column name -> (d, f, eps_c)
    col_map = {
        "theta_d3_f0.01":  (3, 0.01, eps_c_d3),
        "theta_d3_f0.005": (3, 0.005, eps_c_d3),
        "theta_d2_f0.01":  (2, 0.01, eps_c_d2),
        "theta_d2_f0.005": (2, 0.005, eps_c_d2),
    }

    rows = artifact
    if not rows:
        return 0.0
    ok = 0
    for row in rows:
        T = float(row["T"])
        row_ok = True
        for col in columns:
            d, f, eps_c = col_map[col]
            expected = compute_theta(T, d, f, eps_c)
            actual = float(row[col])
            if not is_close(actual, expected):
                row_ok = False
                break
        if row_ok:
            ok += 1
    return ok / len(rows)


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
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
