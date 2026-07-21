import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import quad
import math

# Parameters (hidden gold = the analytical formulas)
BETA = 0.8
L = 0.244
A0 = 1.0
PREFAC = (BETA * L / A0) ** 2
VAA = -0.019
EPSILON_A = 0.102
EPSILON_F = 0.3

# Helper functions
def Lambda(omega):
    Omega = omega
    denominator = (1 + Omega) ** 2
    num = (VAA - Omega) ** 2
    pref = PREFAC * num / denominator
    real_part = 3 + Omega
    if Omega < 0:
        real_part -= 2.0 / math.sqrt(-Omega)
    return pref * real_part

def Delta(omega):
    Omega = omega
    if Omega <= 0:
        return 0.0
    denominator = (1 + Omega) ** 2
    num = (VAA - Omega) ** 2
    return PREFAC * num * 2.0 / (math.sqrt(Omega) * denominator)

def phase_shift(omega):
    delta = Delta(omega)
    lam = Lambda(omega)
    denom = omega - EPSILON_A - lam
    return math.atan2(delta, denom)

def Sigma_ab(d, omega):
    abs_d = abs(d)
    Omega = omega
    denom = (1 + Omega) ** 2
    real_term = (2 + (1 + abs_d) * (1 + Omega)) / denom * math.exp(-abs_d)
    if Omega <= 0:
        return PREFAC * real_term
    else:
        # Fix: multiply by -2j instead of -2.0 to match Eq. 43 (-i * 2 * exp(...))
        imag_term = -2.0j * np.exp(1j * abs_d * math.sqrt(Omega)) / (math.sqrt(Omega) * denom)
        return PREFAC * (real_term + imag_term)

def integrand(omega, d):
    Sigma_a = Lambda(omega) - 1j*Delta(omega)
    denom = omega - EPSILON_A - Sigma_a
    Sigma_ab_val = Sigma_ab(d, omega)
    arg = 1 - (Sigma_ab_val**2) / (denom**2)
    return -(2 / math.pi) * np.imag(np.log(arg))


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


# === block: score_0 (check id='step_01_sigma') ===
def score_0(artifact, step, ctx):
    import csv, os
    path = os.path.join('/app/outputs', step.get('output_file', 'step_01_sigma.csv'))
    try:
        with open(path, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception:
        return 0.0
    if len(rows) != 6:
        return 0.0
    passed = 0
    for row in rows:
        if len(row) < 3:
            continue
        try:
            Omega = float(row[0].strip())
            Lambda_agent = float(row[1].strip())
            Delta_agent = float(row[2].strip())
            Lambda_exp = Lambda(Omega)
            Delta_exp = Delta(Omega)
            tol_L = max(step['tolerance']['rel'] * max(abs(Lambda_exp), 1e-10), step['tolerance']['abs_min'])
            tol_D = max(step['tolerance']['rel'] * max(abs(Delta_exp), 1e-10), step['tolerance']['abs_min'])
            ok_L = abs(Lambda_agent - Lambda_exp) <= tol_L
            ok_D = abs(Delta_agent - Delta_exp) <= tol_D
            if ok_L and ok_D:
                passed += 1
        except Exception:
            continue
    return passed / len(rows)


# === block: score_1 (check id='step_02_phase_shift') ===
def score_1(artifact, step, ctx):
    # Read text, compare single float
    if artifact is None:
        return 0.0
    try:
        val = float(artifact.strip())
        expected = phase_shift(EPSILON_F)
        tol = max(step['tolerance']['rel'] * max(abs(expected), 1e-10), step['tolerance']['abs_min'])
        if abs(val - expected) <= tol:
            return 1.0
        else:
            return 0.0
    except Exception:
        return 0.0


# === block: score_2 (check id='step_03_interaction_energy') ===
def score_2(artifact, step, ctx):
    # Read CSV, compare each row
    import csv
    if artifact is None:
        return 0.0
    passed = 0
    total = 0
    for row in artifact:
        try:
            d = float(row['d'])
            Wab_agent = float(row['W_ab'])
            # Compute expected W_ab via integration
            result, _ = quad(integrand, -10.0, EPSILON_F, args=(d,), limit=200, epsabs=1e-8, epsrel=1e-4, points=[0.0])
            expected = result
            tol = max(step['tolerance']['rel'] * max(abs(expected), 1e-8), step['tolerance']['abs_min'])
            if abs(Wab_agent - expected) <= tol:
                passed += 1
            total += 1
        except Exception:
            continue
    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'step_01_sigma': score_0,
    'step_02_phase_shift': score_1,
    'step_03_interaction_energy': score_2,
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