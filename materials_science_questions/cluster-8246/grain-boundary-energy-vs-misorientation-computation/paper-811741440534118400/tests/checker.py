import os
import json
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
    import os, csv
    chem_file = os.path.join(outputs_dir, "chemical_potential_coefficients.csv")
    ctx = {"chem_coeffs": None}
    if os.path.exists(chem_file):
        with open(chem_file, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            coeff_dict = {}
            for r in rows:
                coeff_dict[r['coefficient']] = float(r['value'])
            ctx["chem_coeffs"] = coeff_dict
    return ctx


# === block: score_0 (check id='adsorption') ===
def score_0(artifact, step, ctx):
    import re
    artifact_str = artifact
    lines = artifact_str.strip().split('\n')
    ads = None
    barr = None
    for l in lines:
        if 'adsorption_energy' in l:
            ads = float(re.findall(r'[-+]?\d*\.?\d+', l)[-1])
        if 'max_barrier' in l:
            barr = float(re.findall(r'[-+]?\d*\.?\d+', l)[-1])
    if ads is None or barr is None:
        return 0.0
    gold = step.get('gold', {})
    gold_ads = gold['adsorption_energy']
    gold_barr = gold['max_barrier']
    tol_ads = gold['tolerance_adsorption']
    tol_barr = gold['tolerance_barrier']
    def score_scalar(val, g, tol):
        diff = abs(val - g)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / tol)
    return 0.5 * score_scalar(ads, gold_ads, tol_ads) + 0.5 * score_scalar(barr, gold_barr, tol_barr)


# === block: score_1 (check id='chem_pot') ===
def score_1(artifact, step, ctx):
    rows = artifact
    gold = step.get('gold', {})
    reported = {}
    for r in rows:
        coeff_name = r.get('coefficient', '').strip()
        try:
            reported[coeff_name] = float(r['value'])
        except:
            continue
    gold_coeffs = {k: gold[k] for k in ['c0','c1','c2','c3','c4','c5','c6']}
    scores = []
    for c in ['c0','c1','c2','c3','c4','c5','c6']:
        gv = gold_coeffs[c]
        rv = reported.get(c, None)
        if rv is None:
            scores.append(0.0)
            continue
        if abs(gv) > 1.0:
            tol = 0.1 * abs(gv)
        else:
            tol = 0.5
        diff = abs(rv - gv)
        if diff <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tol) / (tol * 2)))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='isotherm') ===
def score_2(artifact, step, ctx):
    import math, json, os
    rows = artifact
    if not rows:
        return 0.0

    # Try to load the agent's own gas-phase reference; fallback to hidden gold if missing
    gas_phase_coeffs = None
    agent_gas_file = "/app/outputs/gas_phase_reference.json"
    if os.path.exists(agent_gas_file):
        try:
            with open(agent_gas_file) as f:
                g_ref = json.load(f)
            gas_phase_coeffs = (float(g_ref["c0"]), float(g_ref["c1"]), float(g_ref["c2"]))
        except Exception:
            pass

    if gas_phase_coeffs is None:
        gold = step.get('gold', {})
        if all(k in gold for k in ['gas_phase_c0', 'gas_phase_c1', 'gas_phase_c2']):
            gas_phase_coeffs = (float(gold['gas_phase_c0']), float(gold['gas_phase_c1']), float(gold['gas_phase_c2']))
        else:
            return 0.0

    gp_c0, gp_c1, gp_c2 = gas_phase_coeffs

    # Load agent's chemical potential coefficients from context (prepared from chem_pot artifact)
    chem = ctx.get('chem_coeffs', {})
    if not chem:
        return 0.0
    c0 = chem.get('c0'); c1 = chem.get('c1'); c2 = chem.get('c2'); c3 = chem.get('c3')
    c4 = chem.get('c4'); c5 = chem.get('c5'); c6 = chem.get('c6')
    if None in [c0, c1, c2, c3, c4, c5, c6]:
        return 0.0

    def mu_ads(theta, T):
        return c0 + c1*theta + c2*theta*theta + c3*theta*theta*theta + T*(c4*T + c5*theta + c6)

    def half_mu_gas(T):
        return gp_c0 + gp_c1*T + gp_c2*T*T

    R = 0.008314462618   # kJ/(mol·K)
    factor_tol = 1.000001  # self‑consistency check – very tight

    scores = []
    for row in rows:
        try:
            T = float(row.get('T(K)', ''))
            P_reported = float(row.get('P(bar)', ''))
            theta = float(row.get('theta', ''))
        except Exception:
            scores.append(0.0)
            continue
        if theta <= 0 or theta >= 1:
            scores.append(0.0)
            continue
        dG = mu_ads(theta, T) - half_mu_gas(T)
        K = math.exp(-dG/(R*T))
        denom = K*K*(1.0 - theta)*(1.0 - theta)
        if denom <= 0:
            scores.append(0.0)
            continue
        P_pred = theta*theta / denom
        if P_reported <= 0 or P_pred <= 0:
            scores.append(0.0)
            continue
        factor = max(P_reported/P_pred, P_pred/P_reported)
        if factor <= factor_tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (factor - factor_tol) / (factor_tol*2)))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='diffusion') ===
def score_3(artifact, step, ctx):
    import re
    artifact_str = artifact
    lines = artifact_str.strip().split('\n')
    e_bar = None; Q = None; D0 = None
    for l in lines:
        if 'electronic_barrier' in l:
            e_bar = float(re.findall(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', l)[-1])
        if 'activation_energy_Q' in l:
            Q = float(re.findall(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', l)[-1])
        if 'prefactor_D0' in l:
            D0 = float(re.findall(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', l)[-1])
    if None in (e_bar, Q, D0):
        return 0.0
    gold = step.get('gold', {})
    g_e = gold['electronic_barrier']
    g_Q = gold['Q']
    g_D0 = gold['D0']
    tol_e = gold['tol_barrier']
    tol_Q = gold['tol_Q']
    factor_D0 = gold['factor_D0']
    def score_abs(val, g, tol):
        diff = abs(val - g)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / tol)
    def score_factor(val, g, fac_tol):
        if g == 0:
            return 0.0
        ratio = val / g
        factor = max(ratio, 1.0/ratio)
        if factor <= fac_tol:
            return 1.0
        return max(0.0, 1.0 - (factor - fac_tol) / (fac_tol*2))
    s_e = score_abs(e_bar, g_e, tol_e)
    s_q = score_abs(Q, g_Q, tol_Q)
    s_d0 = score_factor(D0, g_D0, factor_D0)
    return (s_e + s_q + s_d0) / 3.0


_SCORERS = {
    'adsorption': score_0,
    'chem_pot': score_1,
    'isotherm': score_2,
    'diffusion': score_3,
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
