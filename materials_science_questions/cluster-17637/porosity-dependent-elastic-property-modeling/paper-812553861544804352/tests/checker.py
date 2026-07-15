import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='degraded_properties') ===
def score_0(artifact, step, ctx):
    ages_gold = step['gold_ages']
    em_gold = step['gold_Em']
    ft_gold = step['gold_ft']
    rel_em = step['tolerance_rel_Em']
    abs_ft = step['tolerance_abs_ft']
    lookup = {age: (em, ft) for age, em, ft in zip(ages_gold, em_gold, ft_gold)}
    total_cells = 0
    ok_cells = 0
    for row in artifact:
        try:
            age = int(row['age'])
            em_agent = float(row['E_m'])
            ft_agent = float(row['f_t'])
        except (ValueError, KeyError):
            continue
        if age in lookup:
            em_ref, ft_ref = lookup[age]
            if abs(em_agent - em_ref) <= rel_em * abs(em_ref):
                ok_cells += 1
            total_cells += 1
            if abs(ft_agent - ft_ref) <= abs_ft:
                ok_cells += 1
            total_cells += 1
    if total_cells == 0:
        return 0.0
    return ok_cells / total_cells


# === block: score_1 (check id='response_summary') ===
def score_1(artifact, step, ctx):
    gold_data = step['gold']
    tolerances = step['tolerances']
    numeric_w = step['numeric_weight_in_scorer']
    trend_w = step['trend_weight_in_scorer']
    gold_dict = {}
    for g in gold_data:
        key = (g['earthquake'], g['motion_type'], int(g['age']))
        gold_dict[key] = g
    agent_rows = []
    for row in artifact:
        try:
            r = {}
            r['earthquake'] = row['earthquake'].strip()
            r['motion_type'] = row['motion_type'].strip()
            r['age'] = int(row['age'])
            r['disp'] = float(row['max_crest_displacement'])
            r['sigma_heel'] = float(row['max_major_principal_stress_heel'])
            r['sigma_neck'] = float(row['max_minor_principal_stress_neck'])
            r['p_max'] = float(row['max_hydrodynamic_pressure'])
            agent_rows.append(r)
        except (ValueError, KeyError):
            continue
    agent_dict = {}
    for r in agent_rows:
        key = (r['earthquake'], r['motion_type'], r['age'])
        agent_dict[key] = r
    numeric_cols = ['disp', 'sigma_heel', 'sigma_neck', 'p_max']
    col_tol = {
        'disp': tolerances['max_crest_displacement'],
        'sigma_heel': tolerances['max_major_principal_stress_heel'],
        'sigma_neck': tolerances['max_minor_principal_stress_neck'],
        'p_max': tolerances['max_hydrodynamic_pressure'],
    }
    gold_field_map = {
        'disp': 'max_crest_displacement',
        'sigma_heel': 'max_major_principal_stress_heel',
        'sigma_neck': 'max_minor_principal_stress_neck',
        'p_max': 'max_hydrodynamic_pressure',
    }
    row_scores = []
    for key in gold_dict:
        gold = gold_dict[key]
        if key not in agent_dict:
            row_scores.append(0.0)
            continue
        agent = agent_dict[key]
        cell_ok = 0.0
        for col in numeric_cols:
            agent_val = agent[col]
            gold_val = gold[gold_field_map[col]]
            tol = col_tol[col]
            abs_tol = max(tol['rel'] * abs(gold_val), tol['abs'])
            if abs(agent_val - gold_val) <= abs_tol:
                cell_ok += 1.0
        row_scores.append(cell_ok / len(numeric_cols))
    numeric_score = sum(row_scores) / len(row_scores) if row_scores else 0.0
    trend_checks = []
    events = set(g['earthquake'] for g in gold_data)
    motions = set(g['motion_type'] for g in gold_data)
    for eq in events:
        for mt in motions:
            k1 = (eq, mt, 1)
            k75 = (eq, mt, 75)
            if k1 in agent_dict and k75 in agent_dict:
                trend_checks.append(agent_dict[k75]['disp'] > agent_dict[k1]['disp'])
    for eq in events:
        for mt in motions:
            k1 = (eq, mt, 1)
            k75 = (eq, mt, 75)
            if k1 in agent_dict and k75 in agent_dict:
                trend_checks.append(agent_dict[k75]['sigma_heel'] < agent_dict[k1]['sigma_heel'])
    for eq in events:
        for age in [1, 75]:
            k_nf = (eq, 'NF', age)
            k_ff = (eq, 'FF', age)
            if k_nf in agent_dict and k_ff in agent_dict:
                trend_checks.append(agent_dict[k_nf]['disp'] > agent_dict[k_ff]['disp'])
                trend_checks.append(agent_dict[k_nf]['sigma_heel'] > agent_dict[k_ff]['sigma_heel'])
    trend_score = sum(trend_checks) / len(trend_checks) if trend_checks else 0.0
    return numeric_w * numeric_score + trend_w * trend_score


_SCORERS = {
    'degraded_properties': score_0,
    'response_summary': score_1,
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
