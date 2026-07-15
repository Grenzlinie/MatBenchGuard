import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os
import json

def compute_SR(alpha, w_t, t_2rho, n, mu, R, theta_deg):
    theta = math.radians(theta_deg)
    factor_a = ((1+R)/math.sqrt(1+2*R)) * t_2rho
    term1 = (1/(1+n)) * (factor_a)**(1+n)
    factor_c = w_t / math.cos(theta) - (t_2rho**(-1) + 1) * math.tan(theta)
    factor_d = math.tan(theta) * t_2rho + (math.tan(theta) + 2*mu) * (1 - math.cos(theta) + mu * math.sin(theta) * t_2rho) / (math.cos(theta) + mu * math.sin(theta))
    term2 = alpha * (n/math.e)**n * factor_c * factor_d
    sr = (t_2rho)**(-2) * (term1 - term2)
    return sr

def compute_alpha_c(R, n, w_t, t_2rho, mu, theta_deg):
    theta = math.radians(theta_deg)
    factor_a = ((1+R)/math.sqrt(1+2*R)) * t_2rho
    term1 = (factor_a)**(1+n) / (1+n)
    term2 = (n/math.e)**(-n)
    denom1 = w_t / math.cos(theta) - (t_2rho**(-1) + 1) * math.tan(theta)
    denom2 = (math.tan(theta) + 2*mu) * (1 - math.cos(theta) + mu * math.sin(theta) * t_2rho) / (math.cos(theta) + mu * math.sin(theta)) + math.tan(theta) * t_2rho
    alpha_c = term1 * term2 * (1.0/denom1) * (1.0/denom2)
    return alpha_c

def compute_lower_limit(w_t, theta_deg):
    theta = math.radians(theta_deg)
    return math.sin(theta) / (w_t - math.sin(theta))


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
    expected_counts = {
        "sr_data.csv": 4 * 5 * 5 * 3 * 4 * 4 * 21,   # 100800
        "alpha_c_data.csv": 4 * 5 * 5 * 3 * 4 * 4,    # 4800
        "lower_limit_data.csv": 7 * 7,                 # 49
    }
    return {"expected_counts": expected_counts}


# === block: score_0 (check id='sr_data') ===
def score_0(artifact, step, ctx):
    expected_total = ctx["expected_counts"].get("sr_data.csv")
    if expected_total is None:
        return 0.0
    rel_tol = float(step["params"]["relative_tol"])
    abs_tol = float(step["params"]["absolute_tol"])
    correct = 0
    for row in artifact:
        try:
            alpha = float(row["alpha"])
            w_t = float(row["w_t"])
            t_2rho = float(row["t_2rho"])
            n = float(row["n"])
            mu = float(row["mu"])
            R = float(row["R"])
            theta = float(row["theta"])
            sr_val = float(row["SR"])
        except (KeyError, ValueError, TypeError):
            continue
        expected = compute_SR(alpha, w_t, t_2rho, n, mu, R, theta)
        tol = abs_tol + rel_tol * abs(expected)
        if abs(sr_val - expected) <= tol:
            correct += 1
    score = min(correct / expected_total, 1.0)
    return score


# === block: score_1 (check id='alpha_c_data') ===
def score_1(artifact, step, ctx):
    expected_total = ctx["expected_counts"].get("alpha_c_data.csv")
    if expected_total is None:
        return 0.0
    rel_tol = float(step["params"]["relative_tol"])
    abs_tol = float(step["params"]["absolute_tol"])
    correct = 0
    for row in artifact:
        try:
            R = float(row["R"])
            n = float(row["n"])
            w_t = float(row["w_t"])
            t_2rho = float(row["t_2rho"])
            mu = float(row["mu"])
            theta = float(row["theta"])
            alpha_c_val = float(row["alpha_c"])
        except (KeyError, ValueError, TypeError):
            continue
        expected = compute_alpha_c(R, n, w_t, t_2rho, mu, theta)
        tol = abs_tol + rel_tol * abs(expected)
        if abs(alpha_c_val - expected) <= tol:
            correct += 1
    score = min(correct / expected_total, 1.0)
    return score


# === block: score_2 (check id='lower_limit_data') ===
def score_2(artifact, step, ctx):
    expected_total = ctx["expected_counts"].get("lower_limit_data.csv")
    if expected_total is None:
        return 0.0
    rel_tol = float(step["params"]["relative_tol"])
    abs_tol = float(step["params"]["absolute_tol"])
    correct = 0
    for row in artifact:
        try:
            w_t = float(row["w_t"])
            theta = float(row["theta"])
            lower_limit = float(row["lower_limit"])
        except (KeyError, ValueError, TypeError):
            continue
        expected = compute_lower_limit(w_t, theta)
        tol = abs_tol + rel_tol * abs(expected)
        if abs(lower_limit - expected) <= tol:
            correct += 1
    score = min(correct / expected_total, 1.0)
    return score


_SCORERS = {
    'sr_data': score_0,
    'alpha_c_data': score_1,
    'lower_limit_data': score_2,
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
