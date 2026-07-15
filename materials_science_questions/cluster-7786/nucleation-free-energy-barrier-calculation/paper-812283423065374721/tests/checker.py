import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import os
import re


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
    steps = spec.get('steps', [])
    step1 = [s for s in steps if s['id'] == 'step_1_surface_energies'][0]
    step2 = [s for s in steps if s['id'] == 'step_2_vapor_pressure'][0]
    step3 = [s for s in steps if s['id'] == 'step_3_critical_dimensions'][0]
    ctx = {
        'gold_surface': step1['hidden']['gold_table'],
        'rel_tol_surf': step1['hidden']['relative_tolerance'],
        'abs_tol_surf': step1['hidden']['absolute_tolerance_meV_per_sqA'],
        'expected_p_eq': step2['hidden']['expected_value_Torr'],
        'p_factor': step2['hidden']['factor_tolerance'],
        'beam_pressures': step3['hidden']['beam_pressures'],
        'sigma_meV': step3['hidden']['adhesion_energy_sigma_meV_per_sqA'],
        'uc': step3['hidden']['unit_cell'],
        'rel_tol_crit': step3['hidden']['relative_tolerance'],
    }
    return ctx


# === block: score_0 (check id='step_1_surface_energies') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts
    if not rows:
        return 0.0
    gold = ctx['gold_surface']
    rel_tol = ctx['rel_tol_surf']
    abs_tol = ctx['abs_tol_surf']
    passed = 0
    total = 0
    for gr in gold:
        cutoff_match = round(gr['cutoff'], 2)
        face = gr['face']
        gold_val = gr['gamma']
        agent_val = None
        for row in rows:
            c = float(row.get('cutoff', 0))
            f = row.get('face', '').strip()
            if abs(c - cutoff_match) < 0.01 and f == face:
                agent_val = float(row.get('surface_energy'))
                break
        if agent_val is None:
            continue
        total += 1
        err = abs(agent_val - gold_val)
        tol = max(rel_tol * abs(gold_val), abs_tol)
        if err <= tol:
            passed += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_1 (check id='step_2_vapor_pressure') ===
def score_1(artifact, step, ctx):
    text = artifact  # string
    m = re.search(r'p_eq\s*=\s*([\d\.eE+\-]+)', text)
    if not m:
        return 0.0
    p_eq = float(m.group(1))
    expected = ctx['expected_p_eq']
    factor = ctx['p_factor']
    ratio = max(p_eq / expected, expected / p_eq) if expected != 0 else 0.0
    return 1.0 if ratio <= factor else 0.0


# === block: score_2 (check id='step_3_critical_dimensions') ===
def score_2(artifact, step, ctx):
    rows = artifact  # list of dicts
    if not rows:
        return 0.0
    # load surface energies and vapor pressure
    se_path = os.path.join('/app/outputs', 'surface_energies.csv')
    vp_path = os.path.join('/app/outputs', 'vapor_pressure_298K.txt')
    if not os.path.exists(se_path) or not os.path.exists(vp_path):
        return 0.0
    with open(se_path, newline='') as f:
        se_reader = csv.DictReader(f)
        se_data = list(se_reader)
    # get gamma at cutoff 19.9
    gamma = {}
    for row in se_data:
        if abs(float(row.get('cutoff', 0)) - 19.9) < 0.01:
            gamma[row['face'].strip()] = float(row['surface_energy'])
    if not {'001','100','110','010'}.issubset(gamma.keys()):
        return 0.0
    # vapor pressure
    with open(vp_path) as f:
        vp_text = f.read()
    m = re.search(r'p_eq\s*=\s*([\d\.eE+\-]+)', vp_text)
    if not m:
        return 0.0
    p_eq_Torr = float(m.group(1))
    # constants
    kB_eV_per_K = 8.617333262145e-5
    T_C = 298.0
    uc = ctx['uc']
    a = uc['a_A']
    b = uc['b_A']
    c = uc['c_A']
    Z = uc['Z']
    sigma_meV = ctx['sigma_meV']
    rel_tol = ctx['rel_tol_crit']
    beam_pressures = ctx['beam_pressures']
    bp_dict = {bp['source_temp_C']: bp['p_C_Torr'] for bp in beam_pressures}
    # convert surface energies from meV/Å² to eV/Å²
    g001_eV = gamma['001'] / 1000.0
    g100_eV = gamma['100'] / 1000.0
    g110_eV = gamma['110'] / 1000.0
    g010_eV = gamma['010'] / 1000.0
    sigma_eV = sigma_meV / 1000.0
    sqrt_a2_b2 = math.sqrt(a*a + b*b)
    passed = 0
    for row in rows:
        temp = int(row.get('source_temp_C'))
        p_C = bp_dict.get(temp)
        if p_C is None:
            continue
        # supersaturation
        delta_mu = kB_eV_per_K * T_C * math.log(p_C / p_eq_Torr) if p_eq_Torr > 0 else 0.0
        # critical dimensions
        if delta_mu <= 0:
            continue
        denom = Z * delta_mu
        n_a = (4.0 * c * (g110_eV * sqrt_a2_b2 - a * g010_eV)) / denom if denom != 0 else 0.0
        n_b = (4.0 * c * (g110_eV * sqrt_a2_b2 - b * g100_eV)) / denom
        n_c = (2.0 * a * b * (2.0 * g001_eV - sigma_eV)) / denom
        n_d = (-2.0 * c * (g110_eV * sqrt_a2_b2 - a * g010_eV - b * g100_eV)) / denom
        # compare agent numbers
        try:
            agent_na = float(row.get('n_a_star'))
            agent_nb = float(row.get('n_b_star'))
            agent_nc = float(row.get('n_c_star'))
            agent_nd = float(row.get('n_d_star'))
            agent_dmu = float(row.get('supersaturation_eV'))
        except (ValueError, TypeError):
            continue
        pairs = [(agent_na, n_a), (agent_nb, n_b), (agent_nc, n_c), (agent_nd, n_d), (agent_dmu, delta_mu)]
        ok = True
        for rep, comp in pairs:
            if abs(comp) < 1e-12 and abs(rep) < 1e-12:
                continue
            rel_diff = abs(rep - comp) / max(abs(comp), 1e-12)
            if rel_diff > rel_tol:
                ok = False
                break
        if ok:
            passed += 1
    if len(rows) == 0:
        return 0.0
    return passed / len(rows)


_SCORERS = {
    'step_1_surface_energies': score_0,
    'step_2_vapor_pressure': score_1,
    'step_3_critical_dimensions': score_2,
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
