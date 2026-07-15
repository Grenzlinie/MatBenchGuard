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
    import os, csv
    outputs_dir = '/app/outputs'
    agent_eta = None
    hopfield_path = os.path.join(outputs_dir, 'hopfield_eta.csv')
    if os.path.exists(hopfield_path):
        with open(hopfield_path, newline='') as f:
            rows = list(csv.DictReader(f))
            if rows and 'eta_total_eV_Ang2' in rows[0]:
                try:
                    agent_eta = float(rows[0]['eta_total_eV_Ang2'])
                except:
                    pass
    return {'agent_eta': agent_eta}


# === block: score_0 (check id='eta_check') ===
def score_0(artifact, step, ctx):
    expected_cols = set(step.get('schema', {}).get('required_columns', []))
    expected_rows = step.get('schema', {}).get('expected_rows', 1)
    if not isinstance(artifact, list) or len(artifact) != expected_rows:
        return 0.0
    row = artifact[0]
    if not expected_cols.issubset(row.keys()):
        return 0.0
    try:
        eta_val = float(row['eta_total_eV_Ang2'])
    except:
        return 0.0
    gold = float(step['target'])
    tol_rel = float(step['tolerance_rel'])
    if abs(eta_val - gold) <= tol_rel * gold:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='tc_check') ===
def score_1(artifact, step, ctx):
    import math

    sub = step.get('sub_checks', {})
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    # Grid completeness
    omega_range = sub.get('grid_completeness', {}).get('omega_range', [1200, 1400, 50])
    mu_range = sub.get('grid_completeness', {}).get('mu_range', [0.09, 0.13, 0.01])
    w_grid = sub['grid_completeness']['weight']

    omega_vals = list(range(omega_range[0], omega_range[1]+1, omega_range[2]))
    mu_vals = []
    mu = mu_range[0]
    while mu <= mu_range[1] + 1e-9:
        mu_vals.append(round(mu, 10))
        mu += mu_range[2]

    expected = set()
    for o in omega_vals:
        for m in mu_vals:
            expected.add((float(o), float(m)))

    rows_by_key = {}
    for row in artifact:
        try:
            o = float(row['omega_K'])
            m = float(row['mu_star'])
            tc = float(row['Tc_K'])
        except:
            return 0.0
        key = (o, m)
        if key in rows_by_key:
            return 0.0
        rows_by_key[key] = tc

    if len(rows_by_key) != len(expected) or not expected.issubset(rows_by_key.keys()):
        score_grid = 0.0
    else:
        score_grid = 1.0

    # Monotonicity
    w_mono = sub['monotonicity']['weight']
    total_pairs = 0
    passed_pairs = 0
    # group by mu and check Tc decreasing with omega (physically correct trend)
    mu_to_omegas = {}
    for o, m in rows_by_key:
        mu_to_omegas.setdefault(m, []).append(o)
    for m, os in mu_to_omegas.items():
        os_sorted = sorted(os, key=lambda x: float(x))
        for i in range(len(os_sorted)-1):
            total_pairs += 1
            if rows_by_key[(os_sorted[i], m)] >= rows_by_key[(os_sorted[i+1], m)]:
                passed_pairs += 1
    # group by omega and check Tc decreasing with mu
    omega_to_mus = {}
    for o, m in rows_by_key:
        omega_to_mus.setdefault(o, []).append(m)
    for o, ms in omega_to_mus.items():
        ms_sorted = sorted(ms, key=lambda x: float(x))
        for i in range(len(ms_sorted)-1):
            total_pairs += 1
            if rows_by_key[(o, ms_sorted[i])] >= rows_by_key[(o, ms_sorted[i+1])]:
                passed_pairs += 1
    score_mono = passed_pairs / total_pairs if total_pairs > 0 else 0.0

    # Representative point
    w_rep = sub['representative_point']['weight']
    target_omega = float(sub['representative_point']['omega'])
    target_mu = float(sub['representative_point']['mu_star'])
    target_Tc = float(sub['representative_point']['target_Tc'])
    tol_abs = float(sub['representative_point']['tol_abs'])
    if (target_omega, target_mu) in rows_by_key:
        diff = abs(rows_by_key[(target_omega, target_mu)] - target_Tc)
        score_rep = 1.0 if diff <= tol_abs else 0.0
    else:
        score_rep = 0.0

    # Consistency recompute from agent's eta
    w_cons = sub['consistency_recompute']['weight']
    tol_cons = float(sub['consistency_recompute']['tolerance'])
    agent_eta = ctx.get('agent_eta')
    if agent_eta is None:
        score_cons = 0.0
    else:
        ha_eV = 27.2114
        bohr_ang = 0.529177
        m_u = 10.811
        m_e_u = 1822.888
        k_ha = 1.0 / 315775.0
        eta_au = agent_eta / ha_eV * (bohr_ang ** 2)
        m_au = m_u * m_e_u
        def recompute_Tc(omega, mu):
            omega_au = omega * k_ha
            lam = eta_au / (m_au * omega_au**2)
            denom = lam - mu * (1.0 + 0.62 * lam)
            if denom <= 0:
                return 0.0
            return (omega / 1.45) * math.exp(-1.04 * (1.0 + lam) / denom)
    
        ok = 0
        total = len(rows_by_key)
        for (o, m), tc_rep in rows_by_key.items():
            tc_recomp = recompute_Tc(o, m)
            if abs(tc_rep - tc_recomp) <= tol_cons:
                ok += 1
        score_cons = ok / total if total > 0 else 0.0

    # Weighted sum
    final = w_grid * score_grid + w_mono * score_mono + w_rep * score_rep + w_cons * score_cons
    return final


_SCORERS = {
    'eta_check': score_0,
    'tc_check': score_1,
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
