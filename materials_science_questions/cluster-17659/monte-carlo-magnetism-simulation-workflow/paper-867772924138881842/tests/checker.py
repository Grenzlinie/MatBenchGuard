import os
import json
import csv

# === author imports / helpers ===
import sys
import math
import csv
import os

# Provide dummy numpy and scipy.special to avoid ModuleNotFoundError
class _FakeNumpy:
    sqrt = staticmethod(math.sqrt)
    @staticmethod
    def arange(start, stop, step):
        values = []
        v = start
        if step > 0:
            while v <= stop + 1e-12:
                values.append(v)
                v += step
        else:
            while v >= stop - 1e-12:
                values.append(v)
                v += step
        return values

sys.modules['numpy'] = _FakeNumpy()

class _FakeScipySpecial:
    erf = staticmethod(math.erf)

sys.modules['scipy.special'] = _FakeScipySpecial()


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
    import numpy as np
    from scipy.special import erf
    from math import sqrt

    # Gaussian CDF for N(0,1)
    def phi(x):
        return 0.5 * (1.0 + erf(x / sqrt(2)))

    def p_n(n, h, J=1.0):
        # p_n(h) = 1 - Phi(2(1-n)J - h)
        arg = 2*(1-n)*J - h
        return 1.0 - phi(arg)

    def P_star(h, J=1.0):
        p0 = p_n(0, h, J)
        p1 = p_n(1, h, J)
        denom = 1.0 - (p1 - p0)
        if denom == 0:
            return 0.0
        return p0 / denom

    def main_magnetization(h, J=1.0):
        P = P_star(h, J)
        p0 = p_n(0, h, J)
        p1 = p_n(1, h, J)
        p2 = p_n(2, h, J)
        prob_up = P*P*p2 + 2*P*(1-P)*p1 + (1-P)*(1-P)*p0
        m = 2*prob_up - 1
        return m

    def return_magnetization(h_rev_start, h_prime, J=1.0):
        h = h_rev_start
        P = P_star(h, J)
        p2h = p_n(2, h, J)
        p1h = p_n(1, h, J)
        p0h = p_n(0, h, J)
        p2hp = p_n(2, h_prime, J)
        p1hp = p_n(1, h_prime, J)
        p0hp = p_n(0, h_prime, J)
        prob_up_h = P*P*p2h + 2*P*(1-P)*p1h + (1-P)*(1-P)*p0h
        # f(h)
        f = (1 - p2h)*P + (1 - p1h)*(1 - P)
        denom = 1.0 - (p1h - p1hp)
        if denom == 0:
            return 2*prob_up_h - 1  # no change
        q_a = f / denom
        q_b = (p2h - p2hp)*P / denom
        q_sum = q_a + q_b
        q_r2 = P*P * (p2h - p2hp)
        q_r1 = 2 * P * q_sum * (p1h - p1hp)
        q_r0 = q_sum * q_sum * (p0h - p0hp)
        prob_up_prime = prob_up_h - q_r2 - q_r1 - q_r0
        m_prime = 2*prob_up_prime - 1
        return m_prime

    # Precompute main loop gold
    main_h = np.arange(-5.0, 5.01, 0.1)
    main_gold = {}
    for h in main_h:
        m = main_magnetization(h, J=1.0)
        main_gold[round(h, 7)] = m

    # Precompute return loop gold
    rev_start = 1.0
    ret_h = np.arange(1.0, -1.01, -0.05)
    return_gold = {}
    for h in ret_h:
        m = return_magnetization(rev_start, h, J=1.0)
        return_gold[round(h, 7)] = m

    ctx = {
        'main_gold': main_gold,
        'return_gold': return_gold,
        'rtol': 1e-6,
        'atol': 1e-9
    }
    return ctx


# === block: score_0 (check id='step_1') ===
def score_0(artifact, step, ctx):
    import csv

    rtol = ctx['rtol']
    atol = ctx['atol']
    gold = ctx['main_gold']

    if not isinstance(artifact, list):
        return 0.0
    if len(artifact) == 0:
        return 0.0

    required = {'h', 'm'}
    if not required.issubset(artifact[0].keys()):
        return 0.0

    count = 0
    matched = 0
    for row in artifact:
        try:
            h = float(row['h'])
            m = float(row['m'])
        except (ValueError, TypeError):
            return 0.0
        h_key = round(h, 7)
        if h_key in gold:
            gm = gold[h_key]
            if abs(m - gm) <= atol + rtol * abs(gm):
                matched += 1
            count += 1
        else:
            # unknown h value -> treat as mismatch
            count += 1

    if count == 0:
        return 0.0
    return matched / count


# === block: score_1 (check id='step_2') ===
def score_1(artifact, step, ctx):
    import csv

    rtol = ctx['rtol']
    atol = ctx['atol']
    gold = ctx['return_gold']

    if not isinstance(artifact, list):
        return 0.0
    if len(artifact) == 0:
        return 0.0

    required = {'h_prime', 'm_prime'}
    if not required.issubset(artifact[0].keys()):
        return 0.0

    count = 0
    matched = 0
    for row in artifact:
        try:
            h = float(row['h_prime'])
            m = float(row['m_prime'])
        except (ValueError, TypeError):
            return 0.0
        h_key = round(h, 7)
        if h_key in gold:
            gm = gold[h_key]
            if abs(m - gm) <= atol + rtol * abs(gm):
                matched += 1
            count += 1
        else:
            count += 1

    if count == 0:
        return 0.0
    return matched / count


_SCORERS = {
    'step_1': score_0,
    'step_2': score_1,
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
