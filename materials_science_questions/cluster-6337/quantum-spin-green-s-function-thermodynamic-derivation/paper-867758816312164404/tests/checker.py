import os
import json
import csv

# === author imports / helpers ===
import sympy as sp
import math
import random


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
    # no shared state needed
    return {}


# === block: score_0 (check id='expr_check') ===
def score_0(artifact, step, ctx):
    KEYS = step.get('keys', [])
    tolerance = step.get('tolerance', 1e-5)
    num_points = step.get('num_test_points', 20)

    if not isinstance(artifact, dict):
        return 0.0

    beta, G, b, t, S = sp.symbols('beta G b t S', positive=True, real=True)
    d_sym = 2*S + 1
    locals_dict = {'beta': beta, 'G': G, 'b': b, 't': t, 'S': S, 'd': d_sym}

    # gold numeric helpers
    def gold_f_sum(S_val, sin_bt):
        n_max = int(2*S_val)
        total = 0.0
        for n in range(0, n_max+1):
            term = math.comb(n_max, n) * (-1)**n * (sin_bt**(2*n)) * (math.factorial2(2*n) / math.factorial2(2*n+1))
            total += term
        return total

    def gold_value(key, beta_val, G_val, b_val, t_val, S_val):
        d_val = 2*S_val + 1
        if b_val * t_val == 0:
            g_val = 1.0
        else:
            g_val = math.sin(d_val * b_val * t_val) / (d_val * math.sin(b_val * t_val))
        sin_bt = math.sin(b_val * t_val)
        if key == 'mutual_information':
            return (beta_val**2 * G_val**2) / (3 * math.log(2)) * S_val*(S_val+1) * (1 - g_val**2)
        elif key in ('classical_correlation_S_half', 'quantum_correlation_S_half'):
            return (beta_val**2 * G_val**2 * sin_bt**2) / (8 * math.log(2))
        elif key == 'classical_correlation_S_general':
            f_sum = gold_f_sum(S_val, sin_bt)
            return (beta_val**2 * G_val**2) / (6 * math.log(2)) * (
                S_val*(S_val+1)*(f_sum - g_val**2) + S_val**2 * (1 - g_val**2)
            )
        elif key == 'quantum_correlation_S_general':
            f_sum = gold_f_sum(S_val, sin_bt)
            return (beta_val**2 * G_val**2) / (6 * math.log(2)) * (
                S_val*(S_val+1)*(1 - f_sum) + S_val * (1 - g_val**2)
            )
        elif key == 'quantum_fraction':
            return 1.0 / (S_val + 1.0)
        else:
            raise ValueError(f'Unknown key {key}')

    # generate random test points
    random.seed(42)
    test_params = []
    for _ in range(num_points):
        S_val = random.choice([0.5, 1, 1.5, 2, 2.5, 3])
        beta_val = 1e-5
        G_val = random.uniform(0.1, 1.0)
        b_val = random.uniform(0.1, 10.0)
        t_val = random.uniform(1e-6, 0.1)
        test_params.append((beta_val, G_val, b_val, t_val, S_val))

    passed = 0
    for key in KEYS:
        if key not in artifact:
            continue
        expr_str = str(artifact[key])
        try:
            expr = sp.sympify(expr_str, locals=locals_dict)
        except Exception:
            continue
        ok = True
        for beta_val, G_val, b_val, t_val, S_val in test_params:
            subs_dict = {
                beta: beta_val,
                G: G_val,
                b: b_val,
                t: t_val,
                S: S_val,
                d_sym: 2*S_val+1
            }
            try:
                agent_val = float(expr.evalf(subs=subs_dict))
            except Exception:
                ok = False
                break
            gold_val = gold_value(key, beta_val, G_val, b_val, t_val, S_val)
            if gold_val == 0.0:
                if abs(agent_val) > 1e-12:
                    ok = False
                    break
            else:
                rel_err = abs(agent_val - gold_val) / abs(gold_val)
                if rel_err > tolerance:
                    ok = False
                    break
        if ok:
            passed += 1

    score = passed / len(KEYS) if KEYS else 0.0
    return score


_SCORERS = {
    'expr_check': score_0,
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
