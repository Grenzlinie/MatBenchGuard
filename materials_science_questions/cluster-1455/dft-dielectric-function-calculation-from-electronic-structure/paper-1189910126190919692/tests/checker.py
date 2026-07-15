import os
import json
import csv

# === author imports / helpers ===
import math, cmath


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
    spec_json = spec
    gold_pristine = spec_json.get('gold_epsilon_pristine', {'epsilon_x':6.7,'epsilon_y':6.5,'epsilon_z':4.5})
    gold_sn = spec_json.get('gold_epsilon_Sn', {'epsilon_x':13.3,'epsilon_y':13.2,'epsilon_z':4.8})
    tol_pristine = spec_json.get('tol_pristine', 0.20)
    tol_sn = spec_json.get('tol_Sn', 0.30)
    lorentz = spec_json.get('lorentz_params', {'omega_TO': 822, 'omega_LO': 972, 'gamma': 5})
    thickness_nm = spec_json.get('flake_thickness_nm', 120)
    eps_sub = spec_json.get('substrate_epsilon', 11.7)
    eps_air = 1.0
    return {
        'gold_pristine': gold_pristine,
        'gold_sn': gold_sn,
        'tol_pristine': tol_pristine,
        'tol_sn': tol_sn,
        'lorentz': lorentz,
        'thickness_nm': thickness_nm,
        'eps_sub': eps_sub,
        'eps_air': eps_air
    }


# === block: score_0 (check id='step_03') ===
def score_0(artifact, step, ctx):
    required_fields = ['pristine','Sn_intercalated','dispersion_shift','analytical_dispersion_pristine','analytical_dispersion_Sn']
    if not all(k in artifact for k in required_fields):
        return 0.0
    pristine = artifact['pristine']
    sn = artifact['Sn_intercalated']
    if not all(k in pristine for k in ['epsilon_x','epsilon_y','epsilon_z']):
        return 0.0
    if not all(k in sn for k in ['epsilon_x','epsilon_y','epsilon_z']):
        return 0.0
    shape_score = 1.0

    # Dielectric constant comparison
    gold_pristine = ctx['gold_pristine']
    gold_sn = ctx['gold_sn']
    tol_pristine = ctx['tol_pristine']
    tol_sn = ctx['tol_sn']

    def epsilon_score(val, gold, tol):
        rel_err = abs(val-gold)/abs(gold) if gold != 0 else abs(val-gold)
        if rel_err <= tol:
            return 1.0
        elif rel_err <= 2*tol:
            return 0.5
        else:
            return 0.0

    eps_pristine_score = sum(epsilon_score(pristine[k], gold_pristine[k], tol_pristine) for k in ['epsilon_x','epsilon_y','epsilon_z']) / 3.0
    eps_sn_score = sum(epsilon_score(sn[k], gold_sn[k], tol_sn) for k in ['epsilon_x','epsilon_y','epsilon_z']) / 3.0

    # Analytical dispersion self-consistency (recompute from epsilon_inf)
    L = ctx['lorentz']
    d_nm = ctx['thickness_nm']
    eps_sub = ctx['eps_sub']
    eps_air = ctx['eps_air']

    def epsilon_x(freq_cm, eps_inf_x):
        omega_TO2 = L['omega_TO']**2
        omega_LO2 = L['omega_LO']**2
        gamma = L['gamma']
        omega = freq_cm
        denom = omega_TO2 - omega**2 - 1j*gamma*omega
        if abs(denom) < 1e-30:
            denom = 1e-30
        return eps_inf_x * (1 + (omega_LO2 - omega_TO2) / denom)

    def compute_k(freq_cm, eps_inf_x, eps_inf_z):
        eps_x = epsilon_x(freq_cm, eps_inf_x)
        eps_z = eps_inf_z
        # rho = i*sqrt(eps_z/eps_x)
        rho = 1j * cmath.sqrt(eps_z / eps_x)
        k0 = 2 * math.pi * freq_cm * 1e-4  # um^-1
        d_um = d_nm * 1e-3  # 0.12 um
        arg1 = eps_air * rho / eps_z
        arg2 = eps_sub * rho / eps_z
        q = (rho / (k0 * d_um)) * (cmath.atan(arg1) + cmath.atan(arg2))
        k = q * k0
        return k.real

    disp_pristine = artifact.get('analytical_dispersion_pristine', [])
    disp_sn = artifact.get('analytical_dispersion_Sn', [])
    if not disp_pristine or not disp_sn:
        return shape_score * 0.1  # minimal credit

    max_err_pristine = 0.0
    for point in disp_pristine:
        freq = point['frequency_cm-1']
        k_sub = point['wavevector_um-1']
        k_calc = compute_k(freq, pristine['epsilon_x'], pristine['epsilon_z'])
        if abs(k_calc) > 1e-12:
            err = abs(k_sub - k_calc) / abs(k_calc)
            if err > max_err_pristine:
                max_err_pristine = err

    max_err_sn = 0.0
    for point in disp_sn:
        freq = point['frequency_cm-1']
        k_sub = point['wavevector_um-1']
        k_calc = compute_k(freq, sn['epsilon_x'], sn['epsilon_z'])
        if abs(k_calc) > 1e-12:
            err = abs(k_sub - k_calc) / abs(k_calc)
            if err > max_err_sn:
                max_err_sn = err

    overall_err = max(max_err_pristine, max_err_sn)
    if overall_err <= 0.05:
        disp_score = 1.0
    elif overall_err <= 0.15:
        disp_score = 0.5
    else:
        disp_score = 0.0

    # Shift consistency
    k_pristine_860 = compute_k(860, pristine['epsilon_x'], pristine['epsilon_z'])
    k_sn_860 = compute_k(860, sn['epsilon_x'], sn['epsilon_z'])
    if abs(k_pristine_860) < 1e-12:
        k_pristine_860 = 1e-12
    our_shift = (k_pristine_860 - k_sn_860) / k_pristine_860
    reported_shift = artifact['dispersion_shift']
    shift_err = abs(reported_shift - our_shift) / max(abs(our_shift), 0.01)
    if reported_shift <= 0:
        shift_score = 0.0
    elif shift_err <= 0.05:
        shift_score = 1.0
    elif shift_err <= 0.2:
        shift_score = 0.5
    else:
        shift_score = 0.0

    # Weighted combination
    final_score = 0.1*shape_score + 0.2*eps_pristine_score + 0.2*eps_sn_score + 0.3*disp_score + 0.2*shift_score
    return min(1.0, max(0.0, final_score))


_SCORERS = {
    'step_03': score_0,
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
