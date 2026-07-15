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
    ctx = {}
    gold_tables = {}
    for step in spec.get('steps', []):
        params = step.get('params', {})
        if 'gold_table' in params:
            gold_tables[step['output_file']] = params['gold_table']
    ctx['gold_tables'] = gold_tables
    return ctx


# === block: score_0 (check id='interaction_energies') ===
def score_0(artifact, step, ctx):
    sys_names = ['His', 'Gly-His', 'Gly-His-Gly', 'Gly-Gly-His']
    agent_rows = {}
    for row in artifact:
        key = row.get('System', '').strip()
        if key in sys_names:
            agent_rows[key] = row
    if len(agent_rows) != 4:
        return 0.0

    energies = {}
    for sys_name in sys_names:
        row = agent_rows[sys_name]
        try:
            total = float(row['TotalEnergy_kcal_mol'])
            elec  = float(row['Elec_Energy_kcal_mol'])
            vdw   = float(row['vdW_Energy_kcal_mol'])
        except (ValueError, KeyError):
            return 0.0
        energies[sys_name] = (total, elec, vdw)

    check1 = 1.0 if energies['Gly-His'][0] < min(energies[s][0] for s in sys_names if s != 'Gly-His') else 0.0

    e_ghg = energies['Gly-His-Gly'][0]
    e_ggh = energies['Gly-Gly-His'][0]
    check2 = 1.0 if abs(e_ghg - e_ggh) <= 2.0 else 0.0

    check3 = 1.0
    for sys_name in sys_names:
        _, elec, vdw = energies[sys_name]
        if abs(elec) <= abs(vdw):
            check3 = 0.0
            break

    score = (check1 + check2 + check3) / 3.0
    return score


# === block: score_1 (check id='diffusion_coefficients') ===
def score_1(artifact, step, ctx):
    gold_table = ctx['gold_tables'].get(step['output_file'], {})
    tol_rel = step['params'].get('tol_rel', 0.25)
    sys_names = ['His', 'Gly-His', 'Gly-His-Gly', 'Gly-Gly-His']
    agent_rows = {}
    for row in artifact:
        key = row.get('System', '').strip()
        if key in sys_names:
            agent_rows[key] = row
    if len(agent_rows) != 4:
        return 0.0

    agent_dz = {}
    for sys_name in sys_names:
        row = agent_rows.get(sys_name)
        if row is None:
            return 0.0
        try:
            dz = float(row['D_z_cm2_s'])
        except (ValueError, KeyError):
            return 0.0
        agent_dz[sys_name] = dz

    per_scores = []
    for sys_name in sys_names:
        g = gold_table[sys_name]['D_z_cm2_s']
        a = agent_dz[sys_name]
        rel_err = abs(a - g) / (abs(g) + 1e-9)
        if rel_err <= tol_rel:
            s = 1.0
        else:
            s = max(0.0, 1.0 - (rel_err - tol_rel) / (1.0 - tol_rel))
        per_scores.append(s)
    avg_dz_score = sum(per_scores) / len(per_scores)

    ranking = sorted(agent_dz.items(), key=lambda x: x[1], reverse=True)
    order_score = 1.0 if ranking[0][0] == 'Gly-His' else 0.0
    return 0.8 * avg_dz_score + 0.2 * order_score


# === block: score_2 (check id='distance_shift_summary') ===
def score_2(artifact, step, ctx):
    gold_table = ctx['gold_tables'].get(step['output_file'], {})
    tol_abs = step['params'].get('tol_abs', 0.5)
    sys_names = ['His', 'Gly-His', 'Gly-His-Gly', 'Gly-Gly-His']
    agent_rows = {}
    for row in artifact:
        key = row.get('System', '').strip()
        if key in sys_names:
            agent_rows[key] = row
    if len(agent_rows) != 4:
        return 0.0

    per_scores = []
    for sys_name in sys_names:
        row = agent_rows.get(sys_name)
        if row is None:
            return 0.0
        try:
            agent_shift = float(row['Shift_Ang'])
        except (ValueError, KeyError):
            return 0.0
        gold_shift = gold_table[sys_name]['Shift_Ang']
        if abs(agent_shift - gold_shift) <= tol_abs:
            s = 1.0
        else:
            s = 0.0
        per_scores.append(s)
    return sum(per_scores) / len(per_scores)


_SCORERS = {
    'interaction_energies': score_0,
    'diffusion_coefficients': score_1,
    'distance_shift_summary': score_2,
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
