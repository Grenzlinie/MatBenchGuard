import os
import json
import csv

# === author imports / helpers ===
import json, csv, math


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
    k = 1.380649e-23
    T0 = 300.0
    N_A = 6.02214076e23
    mol_mass = 18.015e-3
    M = mol_mass / N_A
    L0_mol = 43.8e3
    L0 = L0_mol / N_A
    omega = L0 / (k * T0) - 1.0
    Ps = 3.6e3
    D = 0.25e-4
    alpha_c = 0.04
    alpha_t = 1.0
    lam = 0.026
    rho = 997.0
    sigma = 0.071

    a = (alpha_t * lam * T0) / (D * Ps * omega * (omega + 1.0))
    ws = alpha_c * Ps / math.sqrt(2.0 * math.pi * M * k * T0)
    b = (alpha_t * lam) / (k * ws * omega * (omega + 1.0) * (a + 1.0))
    b_nm = b * 1e9
    tau = (b ** 2) * rho * k * (omega + 1.0) / (alpha_t * lam * M)
    tau_us = tau * 1e6
    v_mu = M / rho
    R_sigma = 2.0 * sigma * v_mu / (k * T0)
    beta = R_sigma / (b * omega * (a + 1.0))

    expected_params = {'a': a, 'b': b_nm, 'tau': tau_us, 'beta': beta}

    denom_z_inf = omega * (a + 1.0)
    expected_z_inf = {
        0.9: (1.0 - 0.9) / denom_z_inf,
        0.99: (1.0 - 0.99) / denom_z_inf
    }

    f0_lifetime = 0.5
    phi0 = (1.0 - f0_lifetime) / denom_z_inf

    def lifetime_theta(R_phys_m):
        R_dim = R_phys_m / b
        tmp = R_dim**2 + 2*R_dim*(1 - beta + 2*phi0) + (1 + beta)**2
        z = 0.5 * (math.sqrt(max(tmp, 0.0)) - R_dim - 1.0 + beta)
        if z == phi0 or abs(phi0 - z) < 1e-30:
            return 0.0
        inner1 = phi0 * (2*phi0*z**2 - z*(3*phi0**2 + 1) + 2*phi0*(phi0**2 + phi0 + 1))
        inner2 = beta * (phi0*(phi0**2 + 4*phi0 + 3) - 2*z*(phi0 + 1))
        first = 0.5 * (z - beta) / (phi0**2 * (phi0 - z)**2) * (inner1 - inner2)
        term_log1 = (phi0 + 1)*(phi0**2 + beta)*(phi0 - beta) / (phi0**3)
        if (phi0 - beta) != 0 and (phi0 - z) != 0:
            log1 = math.log((phi0 - beta)/(phi0 - z))
        else:
            log1 = 0.0
        second = - term_log1 * log1
        term_log2 = beta*(beta*(phi0 + 1) - phi0) / (phi0**3)
        if beta != 0 and z != 0:
            log2 = math.log(beta / z)
        else:
            log2 = 0.0
        third = - term_log2 * log2
        theta_dim = first + second + third
        return theta_dim * tau

    return {
        'expected_params': expected_params,
        'expected_z_inf': expected_z_inf,
        'lifetime_func': lifetime_theta,
        'tolerance_step3': 0.05
    }


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    fields = step.get('fields', ['a','b','tau','beta'])
    tol = step.get('tolerance_relative', 0.02)
    expected = ctx['expected_params']
    count = 0
    for f in fields:
        if f in artifact and f in expected:
            v = float(artifact[f])
            e = float(expected[f])
            ok = False
            if abs(e) < 1e-12:
                if abs(v) < 1e-12:
                    ok = True
            else:
                if abs(v - e) / abs(e) <= tol:
                    ok = True
            if ok:
                count += 1
    return count / len(fields) if fields else 0.0


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list):
        return 0.0
    tol = step.get('tolerance_relative', 0.02)
    expected = ctx['expected_z_inf']
    found = {}
    for row in artifact:
        try:
            f0_val = float(row['f0'])
            z_val = float(row['z_inf'])
            found[f0_val] = z_val
        except (ValueError, KeyError):
            continue
    ok = 0
    for f0, exp in expected.items():
        if f0 in found:
            v = found[f0]
            if abs(exp) < 1e-12:
                if abs(v) < 1e-12:
                    ok += 1
            else:
                if abs(v - exp) / abs(exp) <= tol:
                    ok += 1
    return ok / len(expected) if expected else 0.0


# === block: score_2 (check id='step3') ===
def score_2(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list):
        return 0.0
    tol = step.get('tolerance_relative', 0.05)
    lifetime_func = ctx['lifetime_func']
    max_rel_err = 0.0
    for row in artifact:
        try:
            R_um = float(row['R_initial_um'])
            t_agent = float(row['lifetime_s'])
        except (ValueError, KeyError):
            continue
        R_m = R_um * 1e-6
        t_expected = lifetime_func(R_m)
        if t_expected < 1e-12 and t_agent < 1e-12:
            rel_err = 0.0
        elif t_expected < 1e-12:
            rel_err = 1.0
        else:
            rel_err = abs(t_agent - t_expected) / abs(t_expected)
        if rel_err > max_rel_err:
            max_rel_err = rel_err
    if max_rel_err <= tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
    'step3': score_2,
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
