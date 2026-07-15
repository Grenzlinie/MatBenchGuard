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
    gold = spec['steps'][0]['hidden']['gold']
    energy_gold = spec['steps'][1]['hidden']['gold']
    energy_tols = spec['steps'][1]['hidden']['tolerances']
    density_tols = spec['steps'][0]['hidden']['tolerances']
    return {'density_gold': gold, 'density_tols': density_tols, 'energy_gold': energy_gold, 'energy_tols': energy_tols}


# === block: score_0 (check id='step_densities') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold = ctx['density_gold']
    tols = ctx['density_tols']
    alpha_ok = 'alpha_SrNCN' in artifact and isinstance(artifact['alpha_SrNCN'], dict)
    beta_ok = 'beta_SrNCN' in artifact and isinstance(artifact['beta_SrNCN'], dict)
    if not (alpha_ok and beta_ok):
        return 0.0
    a = artifact['alpha_SrNCN']
    b = artifact['beta_SrNCN']
    for k in ['density_g_per_cm3','unit_cell_volume_A3','formula_units_per_cell']:
        if k not in a or k not in b:
            return 0.0
    z_alpha_correct = a['formula_units_per_cell'] == gold['alpha_SrNCN']['formula_units_per_cell']
    z_beta_correct = b['formula_units_per_cell'] == gold['beta_SrNCN']['formula_units_per_cell']
    def density_score(d, ref):
        if ref == 0:
            return 0.0
        rel_err = abs(d - ref) / ref
        if rel_err <= tols['density_relative_tol']:
            return 1.0
        elif rel_err <= 0.05:
            return max(0.0, 1.0 - (rel_err - tols['density_relative_tol']) / (0.05 - tols['density_relative_tol']))
        else:
            return 0.0
    da = a['density_g_per_cm3']
    db = b['density_g_per_cm3']
    score_alpha_dens = density_score(da, gold['alpha_SrNCN']['density_g_per_cm3'])
    score_beta_dens = density_score(db, gold['beta_SrNCN']['density_g_per_cm3'])
    trend_correct = da > db
    total = (0.35 * score_alpha_dens +
             0.35 * score_beta_dens +
             0.15 * (1.0 if trend_correct else 0.0) +
             0.075 * (1.0 if z_alpha_correct else 0.0) +
             0.075 * (1.0 if z_beta_correct else 0.0))
    return min(1.0, max(0.0, total))


# === block: score_1 (check id='step_lattice_energies') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold = ctx['energy_gold']
    tols = ctx['energy_tols']
    required_keys = ['alpha_SrNCN', 'beta_SrNCN', 'energy_difference_beta_minus_alpha_eV_per_fu', 'more_stable_polymorph']
    for k in required_keys:
        if k not in artifact:
            return 0.0
    a = artifact['alpha_SrNCN']
    b = artifact['beta_SrNCN']
    if 'total_energy_per_fu_eV' not in a or 'total_energy_per_fu_Ry' not in a:
        return 0.0
    if 'total_energy_per_fu_eV' not in b or 'total_energy_per_fu_Ry' not in b:
        return 0.0
    e_a_ev = a['total_energy_per_fu_eV']
    e_b_ev = b['total_energy_per_fu_eV']
    e_diff_agent = artifact['energy_difference_beta_minus_alpha_eV_per_fu']
    more = artifact['more_stable_polymorph']
    sign_correct = e_b_ev < e_a_ev
    name_correct = isinstance(more, str) and more.lower().strip() == 'beta'
    diff_consistent = abs(e_diff_agent - (e_b_ev - e_a_ev)) <= tols['energy_difference_consistency_tol_eV']
    def energy_score(val, ref, abs_tol):
        if abs(val - ref) <= abs_tol:
            return 1.0
        excess = abs(val - ref) - abs_tol
        return max(0.0, 1.0 - excess / (4 * abs_tol))
    ev_tol = tols['energy_eV_abs_tol']
    score_alpha_ev = energy_score(e_a_ev, gold['alpha_SrNCN']['total_energy_per_fu_eV'], ev_tol)
    score_beta_ev = energy_score(e_b_ev, gold['beta_SrNCN']['total_energy_per_fu_eV'], ev_tol)
    e_a_ry = a.get('total_energy_per_fu_Ry')
    e_b_ry = b.get('total_energy_per_fu_Ry')
    ry_tol = tols['energy_Ry_abs_tol']
    score_alpha_ry = 0.0
    score_beta_ry = 0.0
    if e_a_ry is not None:
        score_alpha_ry = energy_score(e_a_ry, gold['alpha_SrNCN']['total_energy_per_fu_Ry'], ry_tol)
    if e_b_ry is not None:
        score_beta_ry = energy_score(e_b_ry, gold['beta_SrNCN']['total_energy_per_fu_Ry'], ry_tol)
    total = (0.4 * (1.0 if (sign_correct and name_correct) else 0.0) +
             0.2 * score_alpha_ev + 0.2 * score_beta_ev +
             0.1 * (1.0 if diff_consistent else 0.0) +
             0.05 * score_alpha_ry + 0.05 * score_beta_ry)
    return min(1.0, max(0.0, total))


_SCORERS = {
    'step_densities': score_0,
    'step_lattice_energies': score_1,
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
