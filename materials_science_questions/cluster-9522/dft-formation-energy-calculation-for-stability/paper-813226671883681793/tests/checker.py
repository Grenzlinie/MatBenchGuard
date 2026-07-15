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
    return {}


# === block: score_0 (check id='formation_enthalpies_check') ===
def score_0(artifact, step, ctx):
    import json, math
    entries = artifact
    compounds_info = {
        'Ge3Ti5': {'x': 0.375, 'gold_dH': -66.477},
        'Ge4Ti5': {'x': 4.0/9.0, 'gold_dH': -65.684},
        'Ge5Ti6': {'x': 5.0/11.0, 'gold_dH': -63.419},
        'Ge2Ti': {'x': 2.0/3.0, 'gold_dH': -39.179}
    }
    lattice_gold = {
        'Ge3Ti5': {'a': 7.578, 'b': 7.578, 'c': 5.215},
        'Ge4Ti5': {'a': 6.682, 'b': 12.855, 'c': 6.782},
        'Ge5Ti6': {'a': 16.979, 'b': 7.969, 'c': 5.228},
        'Ge2Ti': {'a': 8.645, 'b': 5.076, 'c': 8.825}
    }
    tol_dH = 3.0
    tol_lattice_relative = 0.02
    tol_ic = 0.01
    eV_to_kJ = 96.485
    data = {e['compound']: e for e in entries}
    if 'Ge A4' not in data or 'Ti A3' not in data:
        return 0.0
    E_Ge_per_atom = data['Ge A4']['total_energy_per_cell_eV'] / data['Ge A4']['natoms']
    E_Ti_per_atom = data['Ti A3']['total_energy_per_cell_eV'] / data['Ti A3']['natoms']
    max_ic_diff = 0.0
    for comp, info in compounds_info.items():
        if comp not in data:
            return 0.0
        entry = data[comp]
        E_comp_per_atom = entry['total_energy_per_cell_eV'] / entry['natoms']
        x_Ge = info['x']
        dH_recomp = (E_comp_per_atom - x_Ge * E_Ge_per_atom - (1-x_Ge) * E_Ti_per_atom) * eV_to_kJ
        diff = abs(dH_recomp - entry['formation_enthalpy_kJ_mol_atom'])
        if diff > max_ic_diff:
            max_ic_diff = diff
    ic_score = 1.0 if max_ic_diff <= tol_ic else 0.0
    dH_scores = []
    for comp, info in compounds_info.items():
        dH_agent = data[comp]['formation_enthalpy_kJ_mol_atom']
        diff = abs(dH_agent - info['gold_dH'])
        if diff <= tol_dH:
            dH_scores.append(1.0)
        elif diff <= 10.0:
            dH_scores.append(1.0 - (diff - tol_dH) / (10.0 - tol_dH))
        else:
            dH_scores.append(0.0)
    enthalpy_score = sum(dH_scores) / len(dH_scores) if dH_scores else 0.0
    lat_scores = []
    for comp, gold_lat in lattice_gold.items():
        if comp not in data:
            return 0.0
        lat = data[comp]['lattice_parameters']
        for axis in ['a', 'b', 'c']:
            agent_val = lat[axis]
            gold_val = gold_lat[axis]
            rel_err = abs(agent_val - gold_val) / gold_val
            lat_scores.append(1.0 if rel_err <= tol_lattice_relative else 0.0)
    lattice_score = sum(lat_scores) / len(lat_scores) if lat_scores else 0.0
    w_ic, w_enthalpy, w_lattice = 0.1, 0.6, 0.3
    return w_ic * ic_score + w_enthalpy * enthalpy_score + w_lattice * lattice_score


# === block: score_1 (check id='convex_hull_check') ===
def score_1(artifact, step, ctx):
    import json
    on_hull = artifact.get('on_hull', [])
    ge4ti5_on_hull = artifact.get('ge4ti5_on_hull', False)
    with open('/app/outputs/formation_enthalpies.json') as f:
        formation_data = json.load(f)
    entries = {e['compound']: e for e in formation_data}
    compounds = ['Ge3Ti5', 'Ge4Ti5', 'Ge5Ti6', 'Ge2Ti']
    x_map = {'Ge3Ti5': 0.375, 'Ge4Ti5': 4.0/9.0, 'Ge5Ti6': 5.0/11.0, 'Ge2Ti': 2.0/3.0}
    points = []
    for comp in compounds:
        if comp not in entries:
            return 0.0
        x = x_map[comp]
        dH = entries[comp]['formation_enthalpy_kJ_mol_atom']
        points.append((x, dH, comp))
    points.sort(key=lambda p: p[0])
    hull_indices = []
    for i, p in enumerate(points):
        while len(hull_indices) >= 2:
            p1 = points[hull_indices[-2]]
            p2 = points[hull_indices[-1]]
            dx1, dy1 = p2[0] - p1[0], p2[1] - p1[1]
            dx2, dy2 = p[0] - p2[0], p[1] - p2[1]
            cross = dx1 * dy2 - dy1 * dx2
            if cross <= 0:
                hull_indices.pop()
            else:
                break
        hull_indices.append(i)
    hull_comps = set(points[i][2] for i in hull_indices)
    agent_hull_set = set(on_hull)
    if agent_hull_set == hull_comps and ge4ti5_on_hull == ('Ge4Ti5' in hull_comps):
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'formation_enthalpies_check': score_0,
    'convex_hull_check': score_1,
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
