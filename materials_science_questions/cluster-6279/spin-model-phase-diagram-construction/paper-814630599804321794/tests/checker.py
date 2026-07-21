import os
import json
import csv

# === author imports / helpers ===
import numpy as np

def solve_sigma_lambda(temp, h, J0, xi, D, K0, eta, zeta):
    """Self-consistent solver for sigma and lambda at given (T, h)."""
    sigma = 0.0
    lam = -2.0
    max_iter = 1000
    tol = 1e-12
    for it in range(max_iter):
        factor = 0.5 * K0 * (zeta - 1.0) * (sigma + lam)
        alpha1 = 0.5 * D - 2.0 * sigma * K0 - factor
        alpha2 = -D / 6.0 - (2.0 / 3.0) * lam * K0 - factor
        E1 = alpha1 + alpha2
        E0 = -2.0 * alpha2
        Em1 = -alpha1 + alpha2
        E = np.array([E1, E0, Em1])
        beta = 1.0 / max(temp, 1e-12)
        exp_vals = np.exp(-E * beta)
        Z = exp_vals.sum()
        if Z == 0.0:
            break
        prob = exp_vals / Z
        sigma_new = prob[0] - prob[2]  # Sz =1,0,-1
        lam_new = prob[0] + prob[2] - 2.0 * prob[1]  # Q0 =1,-2,1
        if abs(sigma_new - sigma) < tol and abs(lam_new - lam) < tol:
            sigma, lam = sigma_new, lam_new
            break
        sigma, lam = sigma_new, lam_new
    return sigma, lam

def omega1_0_condition(temp, h, eta, zeta, sigma, lam, J0, xi, D, K0):
    """Compute ω₁(0) from mean-field solution."""
    Delta = K0 * zeta - J0
    # Avoid division by zero (should be positive in QP1Z region)
    denom = Delta * (sigma + lam)
    if abs(denom) < 1e-15:
        return 1e6  # large value, unstable
    sin2chi = -h / denom
    # keep sin2chi in [-1,1]
    sin2chi = max(min(sin2chi, 1.0), -1.0)
    cos2chi = np.sqrt(max(0, 1.0 - sin2chi * sin2chi))
    s2 = sin2chi
    c2 = cos2chi
    s22 = s2 * s2
    c22 = c2 * c2
    sc = s2 * c2
    
    xiJ0 = xi * J0
    etaK0 = eta * K0
    diff_xiJ_etaK = xiJ0 - etaK0
    
    # A_k at k=0
    A0 = (h * s2 - D + (3.0*sigma - lam)*K0
          - (sigma + lam)*(J0 * s22 + zeta * K0 * c22)
          - (sigma - lam)*(xiJ0 + etaK0))
    # B_k at k=0
    B0 = (sigma - lam) * c2 * diff_xiJ_etaK
    # C_k at k=0
    C0 = h * c2 - (sigma + lam) * sc * (J0 - zeta * K0)
    # D_k at k=0
    D0 = (sigma - lam) * s2 * (-diff_xiJ_etaK)  # etaK0 - xiJ0
    # E_k = C_k
    E0 = C0
    # F_k at k=0
    F0 = 2.0 * sigma * s2 * (-diff_xiJ_etaK)
    # G_k at k=0
    G0 = (-h * s2 - D + (3.0*sigma - lam)*K0
          + (sigma + lam)*(J0 * s22 + zeta * K0 * c22)
          - 2.0 * sigma*(xiJ0 + etaK0))
    # H_k at k=0
    H0 = 2.0 * sigma * c2 * (-diff_xiJ_etaK)
    
    # L(0) = A0^2 - B0^2 + G0^2 - H0^2 + 2*C0*E0 - 2*D0*F0  but E0=C0
    L0 = A0*A0 - B0*B0 + G0*G0 - H0*H0 + 2.0*C0*C0 - 2.0*D0*F0
    # M(0) = determinant of the 4x4 matrix
    M0 = np.linalg.det(np.array([[A0, B0, C0, D0],
                                 [-B0, -A0, -D0, -C0],
                                 [C0, F0, G0, H0],
                                 [-F0, -C0, -H0, -G0]]))
    # ω₁(0) = sqrt(L0 + sqrt(L0^2 - 4*M0))  (real part)
    disc = max(0.0, L0*L0 - 4.0*M0)
    val = L0 + np.sqrt(disc)
    if val < 0:
        val = 0.0
    return np.sqrt(val)


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


# === block: score_0 (check id='step_order_params') ===
def score_0(artifact, step, ctx):
    PARAMS = {'J0': 1.0, 'xi': 1.0, 'D': 1.2, 'K0': 1.25, 'eta': 2.0, 'zeta': 3.0}
    tol = step.get('tolerance_abs', 0.01)
    max_dev = step.get('max_deviation_for_zero_score', 0.1)
    rows = artifact
    if not rows:
        return 0.0
    errors = []
    for row in rows:
        try:
            h_val = float(row['field'])
            T_val = float(row['temperature'])
            sigma, lam = solve_sigma_lambda(T_val, h_val, **PARAMS)
            Delta = PARAMS['K0'] * PARAMS['zeta'] - PARAMS['J0']
            Sz_expected = h_val / (2.0 * Delta)
            Q0_expected = (3.0 * sigma - lam) / 2.0
            if Delta <= 0:
                Q2_expected = 0.0
            else:
                radicand = (Delta * (sigma + lam))**2 - h_val**2
                if radicand < 0:
                    Q2_expected = 0.0
                else:
                    Q2_expected = -np.sqrt(radicand) / (2.0 * Delta)
            S_z_reported = float(row['S_z'])
            Q0_reported = float(row['Q0'])
            Q2_reported = float(row['Q2'])
            # max of three absolute differences
            err = max(abs(Sz_expected - S_z_reported),
                      abs(Q0_expected - Q0_reported),
                      abs(Q2_expected - Q2_reported))
            errors.append(err)
        except Exception:
            errors.append(1e6)
    if not errors:
        return 0.0
    max_err = max(errors)
    if max_err <= tol:
        return 1.0
    score = max(0.0, 1.0 - (max_err - tol) / (max_dev - tol))
    return float(min(score, 1.0))


# === block: score_1 (check id='step_phase_boundary') ===
def score_1(artifact, step, ctx):
    PARAMS = {'J0': 1.0, 'xi': 1.0, 'D': 1.2, 'K0': 1.25, 'eta': 2.0, 'zeta': 3.0}
    tol = step.get('tolerance_abs', 0.02)
    rows = artifact
    if not rows:
        return 0.0
    passed = 0
    for row in rows:
        try:
            h_val = float(row['field'])
            T_val = float(row['critical_temperature'])
            sigma, lam = solve_sigma_lambda(T_val, h_val, **PARAMS)
            Delta = PARAMS['K0'] * PARAMS['zeta'] - PARAMS['J0']
            if Delta <= 0:
                Q2 = 0.0
            else:
                radicand = (Delta * (sigma + lam))**2 - h_val**2
                if radicand < 0:
                    Q2 = 0.0
                else:
                    Q2 = -np.sqrt(radicand) / (2.0 * Delta)
            if abs(Q2) <= tol:
                passed += 1
        except Exception:
            pass
    return float(passed) / max(len(rows), 1)


# === block: score_2 (check id='step_critical_anisotropy') ===
def score_2(artifact, step, ctx):
    PARAMS_BASE = {'J0': 1.0, 'xi': 1.0, 'D': 1.2, 'K0': 1.25}
    tol = step.get('tolerance_abs', 0.02)
    rows = artifact
    if not rows:
        return 0.0
    passed = 0
    for row in rows:
        try:
            eta = float(row['eta'])
            zeta = float(row['zeta'])
            h_val = float(row['field'])
            T_star = float(row['critical_temperature'])
            sigma, lam = solve_sigma_lambda(T_star, h_val,
                                            J0=PARAMS_BASE['J0'],
                                            xi=PARAMS_BASE['xi'],
                                            D=PARAMS_BASE['D'],
                                            K0=PARAMS_BASE['K0'],
                                            eta=eta, zeta=zeta)
            omega = omega1_0_condition(T_star, h_val, eta, zeta, sigma, lam,
                                       **PARAMS_BASE)
            if omega <= tol:
                passed += 1
        except Exception:
            pass
    return float(passed) / max(len(rows), 1)


_SCORERS = {
    'step_order_params': score_0,
    'step_phase_boundary': score_1,
    'step_critical_anisotropy': score_2,
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
