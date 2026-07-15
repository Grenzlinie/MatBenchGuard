import os
import json
import csv

# === author imports / helpers ===
import math
try:
    from scipy.optimize import brentq
except ImportError:
    def brentq(f, a, b, args=(), maxiter=200):
        fa = f(a, *args)
        fb = f(b, *args)
        if fa * fb >= 0:
            raise ValueError("f(a) and f(b) must have opposite signs")
        for _ in range(maxiter):
            c = (a + b) / 2
            fc = f(c, *args)
            if fc == 0:
                return c
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
        return (a + b) / 2


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


# === block: score_0 (check id='step_mode2') ===
def score_0(artifact, step, ctx):
    MIN_ROWS = 120
    if len(artifact) < MIN_ROWS:
        return 0.0
    tol_atol = 1e-12
    tol_rtol = 1e-10
    correct = 0
    eps = 1e6
    total = len(artifact)
    for row in artifact:
        try:
            n = float(row['n'])
            param = float(row['parameter_R_over_epsilon_d'])
            sigma = float(row['sigma_Pa'])
            if n <= 0:
                continue
            exp_val = eps * (( (n+1)*param / n ) ** (n/(n+1)))
            err = abs(sigma - exp_val)
            threshold = tol_atol + tol_rtol * max(abs(sigma), abs(exp_val))
            if err <= threshold:
                correct += 1
        except (ValueError, KeyError):
            continue
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='step_tension') ===
def score_1(artifact, step, ctx):
    MIN_ROWS = 10
    if len(artifact) < MIN_ROWS:
        return 0.0
    tol_atol = 1e-12
    tol_rtol = 1e-10
    correct = 0
    eps = 1e6
    total = len(artifact)
    def f(lambda_x, n, param):
        return (lambda_x - 1.0)**(n+1) / math.sqrt(lambda_x) - (n+1)*param
    for row in artifact:
        try:
            n = float(row['n'])
            param = float(row['parameter_R_over_2kc_epsilon'])
            sigma = float(row['sigma_Pa'])
            if n <= 0 or param <= 0:
                continue
            # Find upper bound for root
            lo = 1.0
            hi = 2.0
            while f(hi, n, param) <= 0:
                hi *= 2
                if hi > 1e12:
                    break
            if f(hi, n, param) <= 0:
                continue  # no root found
            lambda_sol = brentq(f, lo, hi, args=(n, param), maxiter=200)
            exp_val = eps * (lambda_sol - 1.0)**n
            err = abs(sigma - exp_val)
            threshold = tol_atol + tol_rtol * max(abs(sigma), abs(exp_val))
            if err <= threshold:
                correct += 1
        except (ValueError, KeyError):
            continue
    return correct / total if total > 0 else 0.0


_SCORERS = {
    'step_mode2': score_0,
    'step_tension': score_1,
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
