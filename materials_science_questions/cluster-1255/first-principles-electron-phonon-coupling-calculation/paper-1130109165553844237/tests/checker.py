import os
import json
import csv

# === author imports / helpers ===
import math
import os
import csv


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
    csv_path = os.path.join('/app/outputs', 'results.csv')
    data = {}
    if os.path.exists(csv_path):
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            if set(['parameter','value','unit']).issubset(reader.fieldnames or []):
                for row in reader:
                    try:
                        data[row['parameter'].strip()] = float(row['value'])
                    except (ValueError, KeyError):
                        pass
    return {
        'data': data,
        'epsilon_F_eV': 0.1,
        'tau_ps': 0.1,
        'B_T': 1.0,
        'rho_I': 3.03e3,
        'mu_B': 9.274009994e-24,
        'hbar': 1.054571817e-34,
        'e_charge': 1.602176634e-19,
        'm_e': 9.10938356e-31,
    }


# === block: score_0 (check id='results_shape') ===
def score_0(artifact, step, ctx):
    data = ctx.get('data', {})
    required = step.get('required_parameter_names', [])
    if all(p in data for p in required):
        return 1.0
    return 0.0


# === block: score_1 (check id='eu_frequency_check') ===
def score_1(artifact, step, ctx):
    data = ctx['data']
    val = data.get('Eu_mode_frequency')
    if val is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_abs']
    diff = abs(val - target)
    out_factor = step.get('out_of_range_factor', 2.0)
    max_tol = tol * out_factor
    if diff <= tol:
        return 1.0
    elif diff >= max_tol:
        return 0.0
    else:
        return 1.0 - (diff - tol) / (max_tol - tol)


# === block: score_2 (check id='beta_over_a_check') ===
def score_2(artifact, step, ctx):
    data = ctx['data']
    val = data.get('beta_over_a')
    if val is None:
        return 0.0
    target = step['target']
    tol_rel = step['tolerance_rel']
    tol = abs(target) * tol_rel
    diff = abs(val - target)
    out_factor = step.get('out_of_range_factor', 2.0)
    max_tol = tol * out_factor
    if diff <= tol:
        return 1.0
    elif diff >= max_tol:
        return 0.0
    else:
        return 1.0 - (diff - tol) / (max_tol - tol)


# === block: score_3 (check id='v_F_check') ===
def score_3(artifact, step, ctx):
    data = ctx['data']
    val = data.get('v_F')
    if val is None:
        return 0.0
    target = step['target']
    tol_rel = step['tolerance_rel']
    tol = abs(target) * tol_rel
    diff = abs(val - target)
    out_factor = step.get('out_of_range_factor', 2.0)
    max_tol = tol * out_factor
    if diff <= tol:
        return 1.0
    elif diff >= max_tol:
        return 0.0
    else:
        return 1.0 - (diff - tol) / (max_tol - tol)


# === block: score_4 (check id='eta_H_consistency') ===
def score_4(artifact, step, ctx):
    data = ctx['data']
    v_F = data.get('v_F')
    if v_F is None:
        return 0.0
    epsilon_F = ctx['epsilon_F_eV'] * ctx['e_charge']
    hbar = ctx['hbar']
    tau = ctx['tau_ps'] * 1e-12
    B = ctx['B_T']
    e = ctx['e_charge']
    n_e = epsilon_F**3 / (3 * math.pi**2 * (hbar * v_F)**3)
    m_star = epsilon_F / (v_F**2)
    omega_c = e * B / m_star
    nu_H = (v_F**2 / 2.0) * (omega_c * tau**2) / (1 + 4 * omega_c**2 * tau**2)
    eta_H_recomputed = n_e * m_star * nu_H
    reported = data.get('eta_H')
    if reported is None or reported == 0.0:
        return 0.0
    diff = abs(reported - eta_H_recomputed) / abs(reported)
    tol_rel = step.get('tolerance_rel', 0.05)
    if diff <= tol_rel:
        return 1.0
    return 0.0


# === block: score_5 (check id='mu_ph_self_consistency') ===
def score_5(artifact, step, ctx):
    data = ctx['data']
    beta_over_a = data.get('beta_over_a')
    v_F = data.get('v_F')
    eta_H = data.get('eta_H')
    if not all([beta_over_a, v_F, eta_H]):
        return 0.0
    beta_a_SI = beta_over_a * 1e10  # 1/Å -> 1/m
    hbar = ctx['hbar']
    rho_I = ctx['rho_I']
    B = ctx['B_T']
    mu_ph_SI = (hbar * (beta_a_SI)**2 / rho_I) * (eta_H / B)
    mu_B = ctx['mu_B']
    mu_ph_recomputed = mu_ph_SI / mu_B
    reported = data.get('mu_ph')
    if reported is None or abs(reported) < 1e-12:
        return 0.0
    diff = abs(reported - mu_ph_recomputed) / abs(reported)
    tol_rel = step.get('tolerance_rel', 0.05)
    if diff <= tol_rel:
        return 1.0
    return 0.0


# === block: score_6 (check id='mu_ph_gold_compare') ===
def score_6(artifact, step, ctx):
    data = ctx['data']
    val = data.get('mu_ph')
    if val is None:
        return 0.0
    target = step['target']
    tol = step['tolerance_abs']
    diff = abs(val - target)
    out_factor = step.get('out_of_range_factor', 2.0)
    max_tol = tol * out_factor
    if diff <= tol:
        return 1.0
    elif diff >= max_tol:
        return 0.0
    else:
        return 1.0 - (diff - tol) / (max_tol - tol)


# === block: score_7 (check id='omega_consistency') ===
def score_7(artifact, step, ctx):
    data = ctx['data']
    omega0_THz = data.get('Eu_mode_frequency')
    beta_over_a = data.get('beta_over_a')
    eta_H = data.get('eta_H')
    if not all([omega0_THz, beta_over_a, eta_H]):
        return 0.0
    beta_a_SI = beta_over_a * 1e10
    rho_I = ctx['rho_I']
    delta_omega_rad = eta_H * (beta_a_SI)**2 / (2 * rho_I)
    delta_f_THz = delta_omega_rad / (2 * math.pi * 1e12)
    f0 = omega0_THz
    f_plus_recomputed = math.sqrt(f0**2 + delta_f_THz**2) + delta_f_THz
    f_minus_recomputed = math.sqrt(f0**2 + delta_f_THz**2) - delta_f_THz
    omega_plus = data.get('omega_plus')
    omega_minus = data.get('omega_minus')
    tol_rel = step.get('tolerance_rel', 0.02)
    ok_plus = False
    ok_minus = False
    if omega_plus is not None:
        ok_plus = abs(omega_plus - f_plus_recomputed) / max(abs(omega_plus), 1e-12) <= tol_rel
    if omega_minus is not None:
        ok_minus = abs(omega_minus - f_minus_recomputed) / max(abs(omega_minus), 1e-12) <= tol_rel
    if ok_plus and ok_minus:
        return 1.0
    return 0.0


_SCORERS = {
    'results_shape': score_0,
    'eu_frequency_check': score_1,
    'beta_over_a_check': score_2,
    'v_F_check': score_3,
    'eta_H_consistency': score_4,
    'mu_ph_self_consistency': score_5,
    'mu_ph_gold_compare': score_6,
    'omega_consistency': score_7,
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
