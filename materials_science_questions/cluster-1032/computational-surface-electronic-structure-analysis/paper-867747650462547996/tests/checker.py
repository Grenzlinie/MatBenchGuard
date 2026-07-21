import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.special import j0, y0, j1, y1
from scipy.optimize import root_scalar
from scipy.integrate import trapezoid as trapz


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


# === block: score_0 (check id='ldos_decay') ===
def score_0(artifact, step, ctx):
    omega = -0.7
    Unz = 1.0
    a0 = 0.01
    R = np.array([float(row['R']) for row in artifact])
    rho_agent = np.array([float(row['rho']) for row in artifact])
    f0_a0 = -np.sign(omega) * j0(abs(omega)*a0) - 1j * y0(abs(omega)*a0)
    g0 = 1j * omega / 4.0 * f0_a0
    B = Unz * omega**2 / (16*np.pi * (1 - Unz**2 * g0**2))
    rho_exp = []
    for r in R:
        f0_r = -np.sign(omega) * j0(abs(omega)*r) - 1j * y0(abs(omega)*r)
        f1_r = -1j * j1(abs(omega)*r) + np.sign(omega) * y1(abs(omega)*r)
        mod = 2 * Unz * np.imag(B * (f0_r**2 - f1_r**2))
        rho_exp.append(abs(omega)/4 + mod)
    rho_exp = np.array(rho_exp)
    rel_err = np.abs(rho_agent - rho_exp) / (np.abs(rho_exp) + 1e-12)
    value_score = np.mean(rel_err < 1e-8)
    delta_rho = rho_agent - abs(omega)/4
    valid = (delta_rho != 0) & (R > 0)
    if np.sum(valid) < 5:
        exp_score = 0.0
    else:
        logR = np.log(R[valid])
        log_d = np.log(np.abs(delta_rho[valid]) + 1e-12)
        coeffs = np.polyfit(logR, log_d, 1)
        slope = coeffs[0]
        exp_score = 1.0 if (-2.05 < slope < -1.95) else 0.0
    score = 0.5 * value_score + 0.5 * exp_score
    return score


# === block: score_1 (check id='spin_parity') ===
def score_1(artifact, step, ctx):
    omegas = np.array([float(row['omega']) for row in artifact])
    sx_agent = np.array([float(row['s_x']) for row in artifact])
    sy_agent = np.array([float(row['s_y']) for row in artifact])
    sz_agent = np.array([float(row['s_z']) for row in artifact])
    R = 0.5
    theta_R = 0.0
    Unz = 1.0
    a0 = 0.01
    N = len(omegas)
    sx_exp = np.zeros(N)
    sy_exp = np.zeros(N)
    sz_exp = np.zeros(N)
    for i, omega in enumerate(omegas):
        f0_a0 = -np.sign(omega) * j0(abs(omega)*a0) - 1j * y0(abs(omega)*a0)
        g0 = 1j * omega / 4.0 * f0_a0
        B = Unz * omega**2 / (16*np.pi * (1 - Unz**2 * g0**2))
        f0_R = -np.sign(omega) * j0(abs(omega)*R) - 1j * y0(abs(omega)*R)
        f1_R = -1j * j1(abs(omega)*R) + np.sign(omega) * y1(abs(omega)*R)
        s_z = np.imag(B * (f0_R**2 + f1_R**2))
        s_x = np.imag(B * (-2j * f0_R * f1_R * np.cos(theta_R)))
        s_y = np.imag(B * (-2j * f0_R * f1_R * np.sin(theta_R)))
        sz_exp[i] = s_z
        sx_exp[i] = s_x
        sy_exp[i] = s_y
    max_rel = np.maximum.reduce([np.abs(sx_agent - sx_exp) / (np.abs(sx_exp)+1e-12),
                                  np.abs(sy_agent - sy_exp) / (np.abs(sy_exp)+1e-12),
                                  np.abs(sz_agent - sz_exp) / (np.abs(sz_exp)+1e-12)])
    value_fraction = np.mean(max_rel < 1e-8)
    pos_mask = omegas > 0
    neg_mask = omegas < 0
    parity_ok = True
    for idx in np.where(pos_mask)[0]:
        w_pos = omegas[idx]
        diffs = np.abs(omegas[neg_mask] + w_pos)
        best_neg = np.argmin(diffs)
        neg_idx_global = np.where(neg_mask)[0][best_neg]
        if np.abs(sz_agent[idx] + sz_agent[neg_idx_global]) > 1e-10:
            parity_ok = False
        if np.abs(sx_agent[idx] - sx_agent[neg_idx_global]) > 1e-10:
            parity_ok = False
        if np.abs(sy_agent[idx] - sy_agent[neg_idx_global]) > 1e-10:
            parity_ok = False
    neg_idx = np.where(neg_mask)[0]
    sum_rule_ok = True
    if len(neg_idx) > 0:
        integral_x = np.abs(trapz(sx_agent[neg_idx], omegas[neg_idx]))
        integral_y = np.abs(trapz(sy_agent[neg_idx], omegas[neg_idx]))
        sum_rule_ok = (integral_x < 1e-10) and (integral_y < 1e-10)
    score = value_fraction * 0.5 + (1.0 if parity_ok else 0.0) * 0.25 + (1.0 if sum_rule_ok else 0.0) * 0.25
    return score


# === block: score_2 (check id='rkky_decay') ===
def score_2(artifact, step, ctx):
    R = np.array([float(row['R']) for row in artifact])
    chi_agent = np.array([float(row['chi_zz']) for row in artifact])
    chi_exp = -1.0 / (8 * np.pi * R**3)
    rel_err = np.abs(chi_agent - chi_exp) / (np.abs(chi_exp) + 1e-12)
    value_score = np.mean(rel_err < 1e-10)
    sign_ok = np.all(chi_agent < 0)
    valid = chi_agent < 0
    if np.sum(valid) < 5:
        exp_score = 0.0
    else:
        logR = np.log(R[valid])
        log_abs_chi = np.log(np.abs(chi_agent[valid]) + 1e-12)
        coeffs = np.polyfit(logR, log_abs_chi, 1)
        slope = coeffs[0]
        exp_score = 1.0 if (-3.05 < slope < -2.95) else 0.0
    score = value_score * 0.4 + (1.0 if sign_ok else 0.0) * 0.3 + exp_score * 0.3
    return score


# === block: score_3 (check id='resonance_energy') ===
def score_3(artifact, step, ctx):
    omega_agent = float(artifact.strip())
    U_nz = 1.0
    a0 = 0.01
    def f(om):
        if om <= 0:
            om = 1e-12
        f0_a0 = -np.sign(om) * j0(abs(om)*a0) - 1j * y0(abs(om)*a0)
        g0 = 1j * om / 4.0 * f0_a0
        return abs(U_nz * g0) - 1.0
    try:
        res = root_scalar(f, bracket=[1e-4, 1.0], method='brentq')
        omega_expected = res.root
        rel_diff = abs(omega_agent - omega_expected) / (abs(omega_expected) + 1e-12)
        return 1.0 if rel_diff < 1e-6 else 0.0
    except Exception:
        return 0.0


_SCORERS = {
    'ldos_decay': score_0,
    'spin_parity': score_1,
    'rkky_decay': score_2,
    'resonance_energy': score_3,
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
