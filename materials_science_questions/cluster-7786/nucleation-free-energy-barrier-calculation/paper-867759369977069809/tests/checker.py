import os
import json
import csv

# === author imports / helpers ===
import math, json, os


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
    p = step.get('params', {})
    eps_gs0 = p['epsilon_gs0']
    theta0g = p['theta0g']
    theta0m = p['theta0m']
    Delta_eps = p['Delta_eps']

    exp_theta_g2 = p['expected_theta_g2']
    theta_tol = p['theta_g2_tol']
    exp_H2 = p['expected_H2']
    H2_tol = p['H2_tol']
    exp_H1 = p['expected_H1']
    H1_tol = p['H1_tol']
    exp_exH2 = p['expected_expt_H2']
    exp_exH1 = p['expected_expt_H1']
    ex_tol = p['expt_tol']

    # Score sub-components
    scores = {}

    # Recompute theta_g2 from quadratic
    # Equation: a = eps_gs0, b = 3, c = 2 - eps_gs0 - Delta_eps
    c0 = 2 - eps_gs0 - Delta_eps
    disc = 9 - 4 * eps_gs0 * c0
    if disc < 0:
        disc = 0.0
    sqrt_disc = math.sqrt(disc)
    theta_g2_recomp = (-3 + sqrt_disc) / (2 * eps_gs0)   # original uses theta0g^3/(2eps_gs0) but theta0g=-1 gives same sign
    # The actual analytical formula includes theta0g^3/(2 eps_gs0); for theta0g=-1 this yields negative division
    # Re-evaluate with full formula: theta_g2 = (-3 + sqrt_disc) * (theta0g**3) / (2*eps_gs0)
    # For theta0g = -1, theta0g**3 = -1, so theta_g2 = -(-3+sqrt_disc)/(2*eps_gs0) = (3 - sqrt_disc)/(2*eps_gs0)?? We'll compute directly.
    # Let's test with our earlier derivation: a=eps_gs0, b=3, c=2-eps_gs0-Delta_eps. Roots: (-3 ± sqrt_disc) / (2*eps_gs0).
    # The paper's root is negative: (-3 + sqrt_disc) / (2*eps_gs0) yields approx -0.584. So we use that.
    theta_g2_calc = (-3 + sqrt_disc) / (2 * eps_gs0)

    if abs(artifact.get('theta_g2', None) - exp_theta_g2) <= theta_tol:
        scores['theta_g2'] = 1.0
    else:
        # partial credit based on distance
        dist = abs(artifact.get('theta_g2', 0) - exp_theta_g2)
        scores['theta_g2'] = max(0.0, 1.0 - dist / (5 * theta_tol))

    # H2/ΔHm (should be exactly Delta_eps)
    h2_val = artifact.get('H2_over_dHm_predicted', None)
    if h2_val is not None and abs(h2_val - exp_H2) <= H2_tol:
        scores['H2'] = 1.0
    else:
        scores['H2'] = 0.0

    # H1/ΔHm recompute: compute ε_ls(θ_g2) and ε_gs(θ_g2)
    theta_sq = theta_g2_calc ** 2
    theta0m_sq = theta0m ** 2
    theta0g_sq = theta0g ** 2
    eps_ls = eps_gs0 * (1 - theta_sq / theta0m_sq)   # note using same ε_ls0 as ε_gs0
    eps_gs = eps_gs0 * (1 - theta_sq / theta0g_sq)
    total_enthalpy_mag = abs(eps_ls - (eps_gs + Delta_eps))
    h1_expected = total_enthalpy_mag - Delta_eps

    h1_val = artifact.get('H1_over_dHm_predicted', None)
    if h1_val is not None and abs(h1_val - h1_expected) <= H1_tol:
        scores['H1'] = 1.0
    else:
        scores['H1'] = 0.0

    # Experimental means
    exp_h2 = artifact.get('experimental_mean_H2_over_dHm', None)
    exp_h1 = artifact.get('experimental_mean_H1_over_dHm', None)
    scores['expt'] = 0.0
    if exp_h2 is not None and exp_h1 is not None:
        if abs(exp_h2 - exp_exH2) <= ex_tol and abs(exp_h1 - exp_exH1) <= ex_tol:
            scores['expt'] = 1.0

    # Agreement statement (non-empty string)
    stmt = artifact.get('agreement_statement', None)
    scores['stmt'] = 1.0 if isinstance(stmt, str) and len(stmt.strip()) > 0 else 0.0

    # Weighted sum
    weights = {'theta_g2': 0.3, 'H2': 0.2, 'H1': 0.3, 'expt': 0.1, 'stmt': 0.1}
    total = sum(scores[k] * weights[k] for k in weights)
    return min(1.0, max(0.0, total))


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    p = step.get('params', {})
    exp_Sm = p['expected_S_m']
    exp_ratio = p['expected_S_Rg_over_S_m']
    Sm_tol = p['S_m_tol']
    ratio_tol = p['ratio_tol']
    S_Rg_tol = p['S_Rg_tol']

    Sm_val = artifact.get('S_m', None)
    ratio_val = artifact.get('S_Rg_over_S_m', None)
    S_Rg_val = artifact.get('S_Rg', None)

    # Basic existence
    if Sm_val is None or ratio_val is None or S_Rg_val is None:
        return 0.0

    # Check S_m
    if abs(Sm_val - exp_Sm) <= Sm_tol:
        sm_ok = 1.0
    else:
        sm_ok = 0.0

    # Check ratio
    if abs(ratio_val - exp_ratio) <= ratio_tol:
        ratio_ok = 1.0
    else:
        dist = abs(ratio_val - exp_ratio)
        ratio_ok = max(0.0, 1.0 - dist / (5 * ratio_tol))

    # Check S_Rg consistency with ratio and S_m: should be S_Rg = ratio * S_m
    if Sm_val != 0:
        expected_SRg = ratio_val * Sm_val
        if abs(S_Rg_val - expected_SRg) <= S_Rg_tol:
            srg_ok = 0.5
        else:
            srg_ok = 0.0
    else:
        srg_ok = 0.0

    # Also check absolute S_Rg against expected from gold ratio
    if abs(Sm_val - exp_Sm) <= Sm_tol:
        expected_abs_SRg = exp_ratio * exp_Sm
        if abs(S_Rg_val - expected_abs_SRg) <= 0.02:
            srg_ok = max(srg_ok, 0.3)

    # Weighted sum
    weights = {'sm': 0.2, 'ratio': 0.5, 'srg': 0.3}
    total = sm_ok * 0.2 + ratio_ok * 0.5 + srg_ok * 0.3
    return min(1.0, max(0.0, total))


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
