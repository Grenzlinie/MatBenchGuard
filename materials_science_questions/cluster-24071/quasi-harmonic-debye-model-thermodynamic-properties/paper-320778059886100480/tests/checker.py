import os
import json
import csv

# === author imports / helpers ===
import math
from scipy.integrate import quad

def D(x):
    if x == 0.0:
        return 1.0
    integral, _ = quad(lambda y: y**3 / (math.exp(y) - 1), 0, x, limit=100)
    return 3.0 * integral / (x**3)

def Cv_debye(mu, L, T, Theta_D, R):
    Theta = Theta_D * (1.0 + L)
    x = Theta / T
    Dx = D(x)
    term1 = 4.0 * Dx - 3.0 * x / (math.exp(x) - 1.0)
    factor = 1.0 - L / (4.0 * (L + 1.0)) * (3.0 - L / (L + 1.0))
    return (3.0 * R / mu) * term1 * factor

def S_debye(mu, L, T, Theta_D, R):
    Theta = Theta_D * (1.0 + L)
    x = Theta / T
    Dx = D(x)
    factor = 1.0 - 3.0 * L / (8.0 * (1.0 + L))
    S = (R / mu) * (4.0 * Dx * factor - 3.0 * math.log(1.0 - math.exp(-x)))
    return S

def ideal_gas_S(mu, v, T, m, g_a, R):
    h = 6.62607015e-34
    k = 1.380649e-23
    term = h**3 / ((2.0 * math.pi * m * k * T)**1.5 * g_a * m * v)
    return (R / mu) * (2.5 - math.log(term))


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
    path = os.path.join(outputs_dir, 'verification_results.json')
    with open(path, 'r') as f:
        data = json.load(f)

    # infer R from the solid limit expected_Cv = 3*R/mu
    solid = data.get('solid_limit', {})
    mu_s = solid.get('mu', 1.0)
    expected_Cv_s = solid.get('expected_Cv', 0.0)
    if expected_Cv_s != 0.0:
        R_agent = expected_Cv_s * mu_s / 3.0
    else:
        gas = data.get('gas_limit', {})
        mu_g = gas.get('mu', 1.0)
        expected_Cv_g = gas.get('expected_Cv', 0.0)
        if expected_Cv_g != 0.0:
            R_agent = expected_Cv_g * mu_g * 2.0 / 3.0   # because expected = 3R/(2mu)
        else:
            R_agent = 8.314462618

    return {'R_agent': R_agent}


# === block: score_0 (check id='step_verify_limits') ===
def score_0(artifact, step, ctx):
    R = 8.314462618

    # ---- solid_limit ----
    solid = artifact.get('solid_limit', {})
    mu_s = solid.get('mu')
    L_s = solid.get('L')
    T_s = solid.get('T')
    Theta_D_s = solid.get('Theta_D')
    computed_Cv_s = solid.get('computed_Cv')
    expected_Cv_s = solid.get('expected_Cv')
    rel_err_s = solid.get('relative_error')

    if None in (mu_s, L_s, T_s, Theta_D_s, computed_Cv_s, expected_Cv_s, rel_err_s):
        solid_score = 0.0
    else:
        expected_s_true = 3.0 * R / mu_s
        if abs(expected_Cv_s - expected_s_true) > 1e-6 * abs(expected_s_true):
            solid_score = 0.0
        else:
            try:
                Cv_model_s = Cv_debye(mu_s, L_s, T_s, Theta_D_s, R)
            except Exception:
                Cv_model_s = None
            if Cv_model_s is not None and abs(Cv_model_s - computed_Cv_s) > 1e-4 * (abs(computed_Cv_s) + 1e-12):
                solid_score = 0.0
            else:
                actual_rel = abs(computed_Cv_s - expected_s_true) / abs(expected_s_true)
                if actual_rel > 0.01:
                    solid_score = 0.0
                elif abs(rel_err_s - actual_rel) > 1e-6:
                    solid_score = 0.0
                else:
                    solid_score = 1.0

    # ---- gas_limit ----
    gas = artifact.get('gas_limit', {})
    mu_g = gas.get('mu')
    L_g = gas.get('L')
    T_g = gas.get('T')
    Theta_D_g = gas.get('Theta_D')
    computed_Cv_g = gas.get('computed_Cv')
    expected_Cv_g = gas.get('expected_Cv')
    rel_err_g = gas.get('relative_error')

    if None in (mu_g, L_g, T_g, Theta_D_g, computed_Cv_g, expected_Cv_g, rel_err_g):
        gas_score = 0.0
    else:
        expected_g_true = 3.0 * R / (2.0 * mu_g)
        if abs(expected_Cv_g - expected_g_true) > 1e-6 * abs(expected_g_true):
            gas_score = 0.0
        else:
            try:
                Cv_model_g = Cv_debye(mu_g, L_g, T_g, Theta_D_g, R)
            except Exception:
                Cv_model_g = None
            if Cv_model_g is not None and abs(Cv_model_g - computed_Cv_g) > 1e-4 * (abs(computed_Cv_g) + 1e-12):
                gas_score = 0.0
            else:
                actual_rel = abs(computed_Cv_g - expected_g_true) / abs(expected_g_true)
                if actual_rel > 0.01:
                    gas_score = 0.0
                elif abs(rel_err_g - actual_rel) > 1e-6:
                    gas_score = 0.0
                else:
                    gas_score = 1.0

    # ---- entropy_check ----
    ent = artifact.get('entropy_check', {})
    L_e = ent.get('L')
    T_e = ent.get('T')
    v_e = ent.get('v')
    mu_e = ent.get('mu')
    m_e = ent.get('m')
    g_a_e = ent.get('g_a')
    computed_S = ent.get('computed_S')
    ideal_S = ent.get('ideal_gas_S')
    rel_err_e = ent.get('relative_error')

    if None in (L_e, T_e, v_e, mu_e, m_e, g_a_e, computed_S, ideal_S, rel_err_e):
        entropy_score = 0.0
    else:
        recomputed_ideal = ideal_gas_S(mu_e, v_e, T_e, m_e, g_a_e, R)
        if abs(ideal_S - recomputed_ideal) > 1e-6 * abs(recomputed_ideal):
            entropy_score = 0.0
        else:
            actual_rel = abs(computed_S - recomputed_ideal) / abs(recomputed_ideal)
            if actual_rel > 0.01:
                entropy_score = 0.0
            elif abs(rel_err_e - actual_rel) > 1e-6:
                entropy_score = 0.0
            else:
                entropy_score = 1.0

    w_solid = 0.4
    w_gas   = 0.4
    w_ent   = 0.2
    total = w_solid * solid_score + w_gas * gas_score + w_ent * entropy_score
    return total


_SCORERS = {
    'step_verify_limits': score_0,
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
