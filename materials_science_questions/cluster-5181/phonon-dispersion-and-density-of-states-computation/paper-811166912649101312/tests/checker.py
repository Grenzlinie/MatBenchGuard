import os
import json
import csv

# === author imports / helpers ===
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
    import os, json
    outputs_dir = '/app/outputs'
    data = {}
    mapping = {
        'BaNi2P2_results.json': 'ni',
        'BaIr2P2_results.json': 'ir',
        'BaRh2P2_results.json': 'rh'
    }
    for fname, key in mapping.items():
        path = os.path.join(outputs_dir, fname)
        with open(path) as f:
            data[key] = json.load(f)
    return {'all_data': data, 'lambda_ni': None, 'Tc_ni': None, 'lambda_ir': None, 'Tc_ir': None, 'lambda_rh': None, 'Tc_rh': None}


# === block: score_0 (check id='extract_ni') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    if artifact is None or 'N_EF' not in artifact or 'alpha2F' not in artifact:
        return 0.0
    N_EF = artifact['N_EF']
    alpha2F = artifact['alpha2F']
    if not isinstance(N_EF, (int, float)) or not isinstance(alpha2F, list) or len(alpha2F) == 0:
        return 0.0
    freqs = []
    vals = []
    for pair in alpha2F:
        if len(pair) != 2:
            continue
        f, v = pair
        if f <= 0:
            continue
        freqs.append(f)
        vals.append(v)
    if len(freqs) < 2:
        return 0.0
    # sort by frequency
    zipped = sorted(zip(freqs, vals), key=lambda x: x[0])
    freqs, vals = zip(*zipped) if zipped else ([], [])
    freqs = list(freqs)
    vals = list(vals)
    n = len(freqs)
    lambda_val = 0.0
    omega_ln_int = 0.0
    for i in range(n - 1):
        dw = freqs[i+1] - freqs[i]
        lam_avg = 0.5 * (vals[i]/freqs[i] + vals[i+1]/freqs[i+1])
        lambda_val += lam_avg * dw
        ln_avg = 0.5 * (vals[i] * math.log(freqs[i]) / freqs[i] + vals[i+1] * math.log(freqs[i+1]) / freqs[i+1])
        omega_ln_int += ln_avg * dw
    lambda_val *= 2.0
    if lambda_val <= 0:
        return 0.0
    omega_ln_meV = math.exp((2.0/lambda_val) * omega_ln_int)
    omega_ln_K = omega_ln_meV * 11.6045
    mu_star = 0.13
    denom = lambda_val - mu_star * (1.0 + 0.62 * lambda_val)
    if denom <= 0:
        Tc = 0.0
    else:
        Tc = (omega_ln_K / 1.2) * math.exp(-1.04 * (1.0 + lambda_val) / denom)
    kB = 8.617333262145e-5
    kB2 = kB * kB
    pi = math.pi
    gamma_cell = (pi * pi / 3.0) * kB2 * N_EF * (1.0 + lambda_val)  # eV/K^2 per formula unit
    gamma_out = gamma_cell * 6.02214076e23 * 1.602176634e-16  # mJ/(mol K^2)

    ctx['lambda_ni'] = lambda_val
    ctx['Tc_ni'] = Tc

    gold_lambda = gold['lambda']
    gold_omega_ln = gold['omega_ln']
    gold_Tc = gold['Tc']
    gold_gamma = gold['gamma']
    tols = {'lambda': 0.20, 'omega_ln': 0.15, 'Tc': 0.20, 'gamma': 0.15}

    def score_q(val, gld, tol):
        if gld == 0:
            return 1.0 if abs(val) < 1e-12 else 0.0
        rel = abs(val - gld) / abs(gld)
        if rel <= tol:
            return 1.0
        return max(0.0, 1.0 - (rel - tol) / (2 * tol))

    s_lam = score_q(lambda_val, gold_lambda, tols['lambda'])
    s_om  = score_q(omega_ln_K, gold_omega_ln, tols['omega_ln'])
    s_tc  = score_q(Tc, gold_Tc, tols['Tc'])
    s_gam = score_q(gamma_out, gold_gamma, tols['gamma'])
    return 0.4 * s_tc + 0.2 * s_lam + 0.2 * s_om + 0.2 * s_gam


# === block: score_1 (check id='extract_ir') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    if artifact is None or 'N_EF' not in artifact or 'alpha2F' not in artifact:
        return 0.0
    N_EF = artifact['N_EF']
    alpha2F = artifact['alpha2F']
    if not isinstance(N_EF, (int, float)) or not isinstance(alpha2F, list) or len(alpha2F) == 0:
        return 0.0
    freqs = []
    vals = []
    for pair in alpha2F:
        if len(pair) != 2:
            continue
        f, v = pair
        if f <= 0:
            continue
        freqs.append(f)
        vals.append(v)
    if len(freqs) < 2:
        return 0.0
    zipped = sorted(zip(freqs, vals), key=lambda x: x[0])
    freqs, vals = zip(*zipped) if zipped else ([], [])
    freqs = list(freqs)
    vals = list(vals)
    n = len(freqs)
    lambda_val = 0.0
    omega_ln_int = 0.0
    for i in range(n - 1):
        dw = freqs[i+1] - freqs[i]
        lam_avg = 0.5 * (vals[i]/freqs[i] + vals[i+1]/freqs[i+1])
        lambda_val += lam_avg * dw
        ln_avg = 0.5 * (vals[i] * math.log(freqs[i]) / freqs[i] + vals[i+1] * math.log(freqs[i+1]) / freqs[i+1])
        omega_ln_int += ln_avg * dw
    lambda_val *= 2.0
    if lambda_val <= 0:
        return 0.0
    omega_ln_meV = math.exp((2.0/lambda_val) * omega_ln_int)
    omega_ln_K = omega_ln_meV * 11.6045
    mu_star = 0.13
    denom = lambda_val - mu_star * (1.0 + 0.62 * lambda_val)
    if denom <= 0:
        Tc = 0.0
    else:
        Tc = (omega_ln_K / 1.2) * math.exp(-1.04 * (1.0 + lambda_val) / denom)
    kB = 8.617333262145e-5
    kB2 = kB * kB
    pi = math.pi
    gamma_cell = (pi * pi / 3.0) * kB2 * N_EF * (1.0 + lambda_val)
    gamma_out = gamma_cell * 6.02214076e23 * 1.602176634e-16

    ctx['lambda_ir'] = lambda_val
    ctx['Tc_ir'] = Tc

    gold_lambda = gold['lambda']
    gold_omega_ln = gold['omega_ln']
    gold_Tc = gold['Tc']
    gold_gamma = gold['gamma']
    tols = {'lambda': 0.20, 'omega_ln': 0.15, 'Tc': 0.20, 'gamma': 0.15}

    def score_q(val, gld, tol):
        if gld == 0:
            return 1.0 if abs(val) < 1e-12 else 0.0
        rel = abs(val - gld) / abs(gld)
        if rel <= tol:
            return 1.0
        return max(0.0, 1.0 - (rel - tol) / (2 * tol))

    s_lam = score_q(lambda_val, gold_lambda, tols['lambda'])
    s_om  = score_q(omega_ln_K, gold_omega_ln, tols['omega_ln'])
    s_tc  = score_q(Tc, gold_Tc, tols['Tc'])
    s_gam = score_q(gamma_out, gold_gamma, tols['gamma'])
    return 0.4 * s_tc + 0.2 * s_lam + 0.2 * s_om + 0.2 * s_gam


# === block: score_2 (check id='extract_rh') ===
def score_2(artifact, step, ctx):
    gold = step['gold']
    if artifact is None or 'N_EF' not in artifact or 'alpha2F' not in artifact:
        return 0.0
    N_EF = artifact['N_EF']
    alpha2F = artifact['alpha2F']
    if not isinstance(N_EF, (int, float)) or not isinstance(alpha2F, list) or len(alpha2F) == 0:
        return 0.0
    freqs = []
    vals = []
    for pair in alpha2F:
        if len(pair) != 2:
            continue
        f, v = pair
        if f <= 0:
            continue
        freqs.append(f)
        vals.append(v)
    if len(freqs) < 2:
        return 0.0
    zipped = sorted(zip(freqs, vals), key=lambda x: x[0])
    freqs, vals = zip(*zipped) if zipped else ([], [])
    freqs = list(freqs)
    vals = list(vals)
    n = len(freqs)
    lambda_val = 0.0
    omega_ln_int = 0.0
    for i in range(n - 1):
        dw = freqs[i+1] - freqs[i]
        lam_avg = 0.5 * (vals[i]/freqs[i] + vals[i+1]/freqs[i+1])
        lambda_val += lam_avg * dw
        ln_avg = 0.5 * (vals[i] * math.log(freqs[i]) / freqs[i] + vals[i+1] * math.log(freqs[i+1]) / freqs[i+1])
        omega_ln_int += ln_avg * dw
    lambda_val *= 2.0
    if lambda_val <= 0:
        return 0.0
    omega_ln_meV = math.exp((2.0/lambda_val) * omega_ln_int)
    omega_ln_K = omega_ln_meV * 11.6045
    mu_star = 0.13
    denom = lambda_val - mu_star * (1.0 + 0.62 * lambda_val)
    if denom <= 0:
        Tc = 0.0
    else:
        Tc = (omega_ln_K / 1.2) * math.exp(-1.04 * (1.0 + lambda_val) / denom)
    kB = 8.617333262145e-5
    kB2 = kB * kB
    pi = math.pi
    gamma_cell = (pi * pi / 3.0) * kB2 * N_EF * (1.0 + lambda_val)
    gamma_out = gamma_cell * 6.02214076e23 * 1.602176634e-16

    ctx['lambda_rh'] = lambda_val
    ctx['Tc_rh'] = Tc

    gold_lambda = gold['lambda']
    gold_omega_ln = gold['omega_ln']
    gold_Tc = gold['Tc']
    gold_gamma = gold['gamma']
    tols = {'lambda': 0.20, 'omega_ln': 0.15, 'Tc': 0.20, 'gamma': 0.15}

    def score_q(val, gld, tol):
        if gld == 0:
            return 1.0 if abs(val) < 1e-12 else 0.0
        rel = abs(val - gld) / abs(gld)
        if rel <= tol:
            return 1.0
        return max(0.0, 1.0 - (rel - tol) / (2 * tol))

    s_lam = score_q(lambda_val, gold_lambda, tols['lambda'])
    s_om  = score_q(omega_ln_K, gold_omega_ln, tols['omega_ln'])
    s_tc  = score_q(Tc, gold_Tc, tols['Tc'])
    s_gam = score_q(gamma_out, gold_gamma, tols['gamma'])
    return 0.4 * s_tc + 0.2 * s_lam + 0.2 * s_om + 0.2 * s_gam


# === block: score_3 (check id='order_check') ===
def score_3(artifact, step, ctx):
    lam_ni = ctx.get('lambda_ni')
    lam_ir = ctx.get('lambda_ir')
    lam_rh = ctx.get('lambda_rh')
    Tc_ni = ctx.get('Tc_ni')
    Tc_ir = ctx.get('Tc_ir')
    Tc_rh = ctx.get('Tc_rh')
    if None in (lam_ni, lam_ir, lam_rh, Tc_ni, Tc_ir, Tc_rh):
        return 0.0
    order_lam = (lam_ni > lam_ir > lam_rh)
    order_Tc  = (Tc_ni > Tc_ir > Tc_rh)
    return 1.0 if (order_lam and order_Tc) else 0.0


_SCORERS = {
    'extract_ni': score_0,
    'extract_ir': score_1,
    'extract_rh': score_2,
    'order_check': score_3,
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
