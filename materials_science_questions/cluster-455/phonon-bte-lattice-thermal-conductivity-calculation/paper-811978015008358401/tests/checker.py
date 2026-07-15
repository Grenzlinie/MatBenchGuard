import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import quad
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
    kB = 1.380649e-23
    hbar = 1.054571817e-34
    Theta = 141.0
    alpha = 1.0
    Theta1, Theta2, Theta3, Theta4 = 57.0, 95.0, 145.0, 100.0
    VT1 = 1.98e5 * 1e-2   # cm/s -> m/s
    VT2 = 1.32e5 * 1e-2
    VL1 = 4.07e5 * 1e-2
    VL2 = 1.97e5 * 1e-2
    tauB_inv = 6.17e5
    Apt = 57e-44
    BT = 3.82e-5
    BL1 = 7.5e-22
    BL2 = 5e-18

    def safe_exp(x):
        if x > 100:
            return 1e30, 1e30
        ex = math.exp(x)
        return ex, ex - 1.0

    def m_T1(T):
        if T <= 0: return 0.0
        x = Theta2 / T
        ex, em1 = safe_exp(x)
        term1 = x / em1 if em1 != 0 else 0.0
        term2 = 0.5 * x
        term3 = math.log(1.0 + Theta/(alpha*T)) / math.log(T) if T > 1 else 0.0
        return term1 + term2 + term3

    def m_L1(T):
        if T <= 0: return 0.0
        x = Theta3 / T
        ex, em1 = safe_exp(x)
        term1 = x / em1 if em1 != 0 else 0.0
        term2 = 0.5 * x
        term3 = math.log(1.0 + Theta/(alpha*T)) / math.log(T) if T > 1 else 0.0
        return term1 + term2 + term3

    def m_L2(T):
        if T <= 0: return 0.0
        x = Theta3 / T
        ex, em1 = safe_exp(x)
        # 0.5 * x * exp(0.5*x) / (exp(x)-1)
        try:
            term1 = 0.5 * x * math.exp(0.5*x) / em1 if em1 != 0 else 0.0
        except OverflowError:
            term1 = 0.0
        term2 = 0.5
        term3 = math.log(1.0 + Theta/(alpha*T)) / math.log(T) if T > 1 else 0.0
        return term1 + term2 + term3

    def integrand_T(x, T, v, mT_val):
        omega = x * kB * T / hbar
        tau_pt_inv = Apt * (omega ** 4)
        tau_3ph_inv = BT * omega * (T ** mT_val) * math.exp(-Theta/(alpha*T))
        rate = tauB_inv + tau_pt_inv + tau_3ph_inv
        ex = math.exp(x)
        em1 = ex - 1.0
        I = (x**4) * ex / (em1**2) / rate
        return I / v

    def integrand_L(x, T, v, mL1_val, mL2_val):
        omega = x * kB * T / hbar
        tau_pt_inv = Apt * (omega ** 4)
        tau_3ph_inv = BL1 * (omega**2) * (T ** mL1_val) * math.exp(-Theta/(alpha*T)) + BL2 * (omega**2) * (T ** mL2_val) * math.exp(-Theta/(alpha*T))
        rate = tauB_inv + tau_pt_inv + tau_3ph_inv
        ex = math.exp(x)
        em1 = ex - 1.0
        I = (x**4) * ex / (em1**2) / rate
        return I / v

    def expected_conductivity(T):
        if T <= 0:
            return (0.0, 0.0, 0.0)
        mT1 = m_T1(T)
        mL1 = m_L1(T)
        mL2 = m_L2(T)
        prefactor_T = (2.0/3.0) * (kB/(2*np.pi**2)) * (kB*T/hbar)**3
        lim0 = Theta1 / T
        lim1 = Theta2 / T
        I_T1, _ = quad(integrand_T, 0, lim0, args=(T, VT1, mT1), limit=200)
        I_T2, _ = quad(integrand_T, lim0, lim1, args=(T, VT2, mT1), limit=200)
        K_T = prefactor_T * (I_T1 + I_T2)
        prefactor_L = (1.0/3.0) * (kB/(2*np.pi**2)) * (kB*T/hbar)**3
        lim2 = Theta4 / T
        lim3 = Theta3 / T
        I_L1, _ = quad(integrand_L, 0, lim2, args=(T, VL1, mL1, mL2), limit=200)
        I_L2, _ = quad(integrand_L, lim2, lim3, args=(T, VL2, mL1, mL2), limit=200)
        K_L = prefactor_L * (I_L1 + I_L2)
        K_total = K_T + K_L
        return (K_total, K_T, K_L)

    step = spec.get('steps', [{}])[0]
    points = step.get('points', [])
    expected = {}
    for T in points:
        expected[T] = expected_conductivity(T)
    return {'expected': expected, 'tolerance_rel': step.get('tolerance_rel', 0.15), 'trend_weight': step.get('trend_weight', 0.3)}


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    expected_dict = ctx['expected']
    tol_rel = ctx['tolerance_rel']
    trend_w = ctx['trend_weight']
    num_w = 1.0 - trend_w

    # artifact is list of dicts with string values
    rows_by_T = {}
    for row in artifact:
        try:
            T = float(row['T'])
            Kt = float(row['K_total'])
            Ktr = float(row['K_transverse'])
            Kl = float(row['K_longitudinal'])
            rows_by_T[T] = (Kt, Ktr, Kl)
        except (ValueError, KeyError):
            continue

    points = ctx['expected'].keys()
    numerical_scores = []
    trend_flags = []
    for T in points:
        if T not in rows_by_T:
            numerical_scores.append(0.0)
            continue
        Kt, Ktr, Kl = rows_by_T[T]
        exp_t, exp_tr, exp_l = expected_dict.get(T, (0,0,0))
        if exp_t == 0 and exp_tr == 0 and exp_l == 0:
            # cannot score, treat as missing
            numerical_scores.append(0.0)
            continue
        rel_errors = []
        if abs(exp_t) > 1e-12:
            rel_errors.append(abs(Kt - exp_t) / abs(exp_t))
        if abs(exp_tr) > 1e-12:
            rel_errors.append(abs(Ktr - exp_tr) / abs(exp_tr))
        if abs(exp_l) > 1e-12:
            rel_errors.append(abs(Kl - exp_l) / abs(exp_l))
        if not rel_errors:
            numerical_scores.append(1.0)
            continue
        max_rel_err = max(rel_errors)
        if max_rel_err <= tol_rel:
            score = 1.0
        elif max_rel_err >= 2 * tol_rel:
            score = 0.0
        else:
            score = (2*tol_rel - max_rel_err) / tol_rel
        numerical_scores.append(score)

        # trend check
        if T is not None:
            if T > 80 or T < 10:
                correct = (Ktr >= Kl)
            else:
                correct = (Kl >= Ktr)
            trend_flags.append(1.0 if correct else 0.0)

    if numerical_scores:
        avg_num = sum(numerical_scores) / len(numerical_scores)
    else:
        avg_num = 0.0
    if trend_flags:
        avg_trend = sum(trend_flags) / len(trend_flags)
    else:
        avg_trend = 0.0

    return num_w * avg_num + trend_w * avg_trend


_SCORERS = {
    'step_02': score_0,
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
