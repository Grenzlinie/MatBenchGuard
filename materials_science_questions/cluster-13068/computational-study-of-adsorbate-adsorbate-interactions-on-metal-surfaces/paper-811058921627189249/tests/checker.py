import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import root_scalar


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
    # Reference order parameter is computed from the analytic theory (Eq. 8 of the paper),
    # using the theoretical inflection point V22/V22_max ≈ 0.183.
    # The agent never sees this implementation, so the reference remains hidden.
    theory_threshold = 0.183  # inflection point from the paper's theory curve

    def langevin(z):
        if z == 0.0:
            return 0.0
        return (np.exp(z) + np.exp(-z)) / (np.exp(z) - np.exp(-z)) - 1.0 / z

    def solve_order(c):
        if c > -3.0:
            return 0.0
        f = lambda m: m - langevin(c * m)
        try:
            sol = root_scalar(f, bracket=[1e-8, 1.0], method='brentq')
            return sol.root
        except ValueError:
            return 0.0

    # Normalisation constant: order parameter at maximum coupling strength (x=1)
    m_max = solve_order(-3.0 / theory_threshold)  # c at x=1

    artifact_path = os.path.join(outputs_dir, 'order_parameter.csv')
    if not os.path.exists(artifact_path):
        return {'x': np.array([]), 'y_sim': np.array([]), 'y_ref': np.array([])}

    with open(artifact_path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    x_vals = []
    y_sim_vals = []
    for row in rows:
        try:
            x_vals.append(float(row['V22_relative_strength']))
            y_sim_vals.append(float(row['order_parameter_sim']))
        except (KeyError, ValueError):
            continue

    x = np.array(x_vals)
    y_sim = np.array(y_sim_vals)

    # Generate hidden reference values at exactly the same V22_relative_strength values
    y_ref = np.zeros_like(x)
    for i, xi in enumerate(x):
        c = -3.0 * xi / theory_threshold
        m = solve_order(c)
        y_ref[i] = m / m_max if m_max > 0 else 0.0

    return {'x': x, 'y_sim': y_sim, 'y_ref': y_ref}


# === block: score_0 (check id='inflection') ===
def score_0(artifact, step, ctx):
    x, y_sim = ctx['x'], ctx['y_sim']
    if len(x) < 3 or np.all(y_sim == y_sim[0]):
        return 0.0

    # compute numerical derivative and find maximum
    dy = np.gradient(y_sim, x)
    idx = int(np.argmax(dy))
    inflection = float(x[idx])

    target = float(step['target'])
    tolerance = float(step['tolerance'])
    score = max(0.0, 1.0 - abs(inflection - target) / tolerance)
    return float(score)


# === block: score_1 (check id='l2') ===
def score_1(artifact, step, ctx):
    y_sim = ctx['y_sim']
    y_ref = ctx['y_ref']
    if len(y_sim) == 0 or len(y_ref) == 0 or len(y_sim) != len(y_ref):
        return 0.0

    # compute root-mean-square L2 distance
    l2 = np.sqrt(np.mean((y_sim - y_ref) ** 2))
    tolerance_l2 = float(step['tolerance_l2'])
    score = max(0.0, 1.0 - l2 / tolerance_l2)
    return float(score)


_SCORERS = {
    'inflection': score_0,
    'l2': score_1,
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