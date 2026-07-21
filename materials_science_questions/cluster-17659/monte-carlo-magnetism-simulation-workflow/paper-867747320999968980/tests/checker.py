import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import i0e, i1e


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
    # Load submitted CSV (already passed shape gate)
    rows = [r for r in artifact if r['n'] and r['T'] and r['q0'] is not None and r['q1'] is not None]
    if not rows:
        return 0.0

    # Parameters
    Btilde = 1.0
    Jtilde = 3.0
    beta_T = lambda T: 1.0 / T

    # Helper to compute log of I0(x), I1(x) using scaled versions to avoid overflow
    def log_i0(x):
        if x < 1e-12:
            return 0.0
        val = i0e(x)  # i0e(x) = exp(-x)*I0(x)
        return x + math.log(val)

    def log_i1(x):
        if x < 1e-12:
            return -np.inf
        val = i1e(x)
        return x + math.log(val)

    # Compute rhs of the equations for given q0,q1,T,n
    def rhs(q0, q1, T, n):
        beta = 1.0 / T
        # Avoid non-physical values
        q0 = max(0.0, min(q0, 0.999))
        q1 = max(q0, min(q1, 0.999))  # constraint q0 <= q1
        Xi_sq = max(0.0, 0.5*(Jtilde + Btilde)*q1 - 0.5*Btilde*q0)
        Xi = beta * math.sqrt(Xi_sq)
        inner_factor = beta * math.sqrt(0.5 * Btilde * q0) if q0 > 0.0 else 0.0

        # integration weight
        def p_weight(x):
            return x * math.exp(-0.5 * x * x)

        # outer integrand for q0: (num/den)^2 * p_weight(x)
        def outer_q0(x):
            if Xi < 1e-12:
                return 0.0
            # Inner integrals over z
            def num_f(z):
                ln_i1_xi = log_i1(z * Xi)
                ln_i1_arg2 = log_i1(z * inner_factor * x / Xi) if inner_factor > 0 and Xi > 0 else -np.inf
                log_num = ln_i1_xi + ln_i1_arg2
                log_denom = n * log_i0(z * Xi) + log_i0(z * inner_factor * x / Xi)
                ratio = math.exp(log_num - log_denom)
                return ratio * z * math.exp(-0.5 * z * z)
            denom_f = lambda z: (i0e(z * Xi) ** n * i0e(z * inner_factor * x / Xi)) * math.exp(z * Xi * n + z * inner_factor * x / Xi - 0.5 * z * z) * z # using logs is safer
            # We'll use log methods to avoid overflow
            inner_num, _ = quad(num_f, 0, 30, limit=100)
            inner_den, _ = quad(lambda z: math.exp(n * log_i0(z * Xi) + log_i0(z * inner_factor * x / Xi) - 0.5 * z * z) * z, 0, 30, limit=100)
            if inner_den > 0:
                val = (inner_num / inner_den) ** 2
            else:
                val = 0.0
            return val * p_weight(x)

        # outer integrand for q1: num/den
        def outer_q1(x):
            if Xi < 1e-12:
                return 0.0
            def num_f(z):
                ln_i1_xi = log_i1(z * Xi)
                ln_i1_arg2 = log_i1(z * inner_factor * x / Xi) if inner_factor > 0 else -np.inf
                if ln_i1_xi < -500 or ln_i1_arg2 < -500:
                    return 0.0
                log_num = ln_i1_xi + ln_i1_arg2
                log_denom = n * log_i0(z * Xi) + log_i0(z * inner_factor * x / Xi)
                return math.exp(log_num - log_denom - 0.5 * z * z) * z
            inner_num, _ = quad(num_f, 0, 30, limit=100)
            inner_den, _ = quad(lambda z: math.exp(n * log_i0(z * Xi) + log_i0(z * inner_factor * x / Xi) - 0.5 * z * z) * z, 0, 30, limit=100)
            if inner_den > 0:
                return (inner_num / inner_den) * p_weight(x)
            else:
                return 0.0

        q0_rhs, _ = quad(outer_q0, 0, 20, limit=100)
        q1_rhs, _ = quad(outer_q1, 0, 20, limit=100)
        return q0_rhs, q1_rhs

    # Compute errors
    errors = []
    for row in rows:
        try:
            n = float(row['n'])
            T = float(row['T'])
            q0 = float(row['q0'])
            q1 = float(row['q1'])
            q0_rhs, q1_rhs = rhs(q0, q1, T, n)
            err = max(abs(q0 - q0_rhs), abs(q1 - q1_rhs))
            errors.append(err)
        except Exception:
            errors.append(1.0)  # penalize bad row

    if not errors:
        return 0.0
    avg_err = sum(errors) / len(errors)
    # Score: full credit if avg_err <= 0.005, linearly drop to 0 at avg_err >= 0.05
    score = max(0.0, 1.0 - (avg_err - 0.005) / 0.045)
    return score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    # Agent artifact for step_02 (transition temps)
    trans = []
    if artifact is None:
        return 0.0
    for row in artifact:
        n = row.get('n')
        if n is None:
            continue
        n = float(n)
        t1 = row.get('T_P_SG1')
        t2 = row.get('T_SG1_SG2')
        trans.append((n, t1.strip() if isinstance(t1, str) else t1, t2.strip() if isinstance(t2, str) else t2))
    if not trans:
        return 0.0

    # Load step_01 data from /app/outputs/step_01_order_parameters.csv
    import os, csv
    step01_path = os.path.join('/app/outputs', 'step_01_order_parameters.csv')
    if not os.path.exists(step01_path):
        return 0.0
    with open(step01_path, newline='') as f:
        reader = csv.DictReader(f)
        raw = [r for r in reader]
    # Build curves per n
    data = {}
    for r in raw:
        try:
            n = float(r['n'])
            T = float(r['T'])
            q0 = float(r['q0'])
            q1 = float(r['q1'])
        except:
            continue
        data.setdefault(n, []).append((T, q0, q1))

    # Derive expected transition temps
    def find_transition(curves, field_index, threshold=0.005):
        if not curves:
            return None
        sorted_pts = sorted(curves, key=lambda x: x[0])
        for i in range(len(sorted_pts)):
            T, q0, q1 = sorted_pts[i]
            val = q0 if field_index == 0 else q1
            if val > threshold:
                # linear interpolation with previous point
                if i == 0:
                    return T
                T0, _, val0 = sorted_pts[i-1]
                val0 = val0 if field_index == 0 else val0
                if val0 > threshold:
                    return T0
                # interpolate
                slope = (val - val0) / (T - T0)
                if slope > 0:
                    return T0 + (threshold - val0) / slope
                else:
                    return T
        return None

    score_sum = 0.0
    count = 0.0
    for n, t1, t2 in trans:
        n = float(n)
        curves = data.get(n, [])
        if not curves:
            continue
        expected_t1 = find_transition(curves, 1, threshold=0.005)  # q1
        expected_t2 = find_transition(curves, 0, threshold=0.005)  # q0
        # If expected_t2 is None, it means SG1->SG2 never occurs; t2 should be empty
        score_t1 = 0.0
        score_t2 = 0.0
        if t1 is not None and t1 != '':
            if expected_t1 is not None and abs(float(t1) - expected_t1) <= 0.05:
                score_t1 = 1.0
        else:
            if expected_t1 is None:
                score_t1 = 1.0
        if t2 is not None and t2 != '':
            if expected_t2 is not None and abs(float(t2) - expected_t2) <= 0.05:
                score_t2 = 1.0
        else:
            if expected_t2 is None:
                score_t2 = 1.0
        score_sum += (score_t1 + score_t2) / 2.0
        count += 1.0
    if count == 0:
        return 0.0
    return score_sum / count


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
