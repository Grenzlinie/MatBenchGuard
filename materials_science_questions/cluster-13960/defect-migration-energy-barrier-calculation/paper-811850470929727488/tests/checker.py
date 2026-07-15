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


# === block: score_0 (check id='potential_parameters') ===
def score_0(artifact, step, ctx):
    expected = step.get('expected', {})
    short_range_exp = expected.get('short_range', [])
    shell_exp = expected.get('shell', [])
    short_range = artifact.get('short_range', [])
    shell = artifact.get('shell', [])

    def find_match(items, key_field, exp):
        for it in items:
            if it.get(key_field) == exp.get(key_field):
                return it
        return None

    tol_A_rel = 0.01
    tol_C_rel = 0.01
    tol_rho_abs = 0.005

    score_short = 0.0
    for exp in short_range_exp:
        match = find_match(short_range, "interaction", exp)
        if match is None:
            continue
        A_ok = abs(match.get("A", 0) - exp["A"]) / abs(exp["A"]) <= tol_A_rel if exp["A"] != 0 else match.get("A", 0) == 0.0
        rho_ok = abs(match.get("rho", 0) - exp["rho"]) <= tol_rho_abs
        C_ok = abs(match.get("C", 0) - exp["C"]) / abs(exp["C"]) <= tol_C_rel if exp["C"] != 0 else match.get("C", 0) == 0.0
        if A_ok and rho_ok and C_ok:
            score_short += 1.0

    score_shell = 0.0
    for exp in shell_exp:
        match = find_match(shell, "species", exp)
        if match is None:
            continue
        Y_ok = abs(match.get("Y", 0) - exp["Y"]) / abs(exp["Y"]) <= 0.01 if exp["Y"] != 0 else match.get("Y", 0) == 0.0
        k_ok = abs(match.get("k", 0) - exp["k"]) / abs(exp["k"]) <= 0.01 if exp["k"] != 0 else match.get("k", 0) == 0.0
        if Y_ok and k_ok:
            score_shell += 1.0

    total_short = len(short_range_exp)
    total_shell = len(shell_exp)
    if total_short + total_shell == 0:
        return 1.0
    weight_short = total_short / (total_short + total_shell)
    weight_shell = total_shell / (total_short + total_shell)
    sc = (score_short / total_short if total_short else 1.0) * weight_short + (score_shell / total_shell if total_shell else 1.0) * weight_shell
    return sc


# === block: score_1 (check id='perfect_crystal') ===
def score_1(artifact, step, ctx):
    expected = step.get('expected', {})
    def abs_check(val, exp, tol):
        return abs(val - exp) <= tol

    lattice_energy_ok = 1.0 if abs_check(artifact.get('lattice_energy', 0), expected['lattice_energy'], 0.1) else 0.0

    uc = artifact.get('unit_cell', {})
    exp_uc = expected['unit_cell']
    a_ok = 1.0 if abs_check(uc.get('a', 0), exp_uc['a'], 0.01) else 0.0
    b_ok = 1.0 if abs_check(uc.get('b', 0), exp_uc['b'], 0.01) else 0.0
    c_ok = 1.0 if abs_check(uc.get('c', 0), exp_uc['c'], 0.01) else 0.0
    uc_score = (a_ok + b_ok + c_ok) / 3.0

    distances = artifact.get('interatomic_distances', [])
    exp_dist = expected.get('interatomic_distances', [])
    dist_count = len(exp_dist)
    dist_hits = 0
    for ed in exp_dist:
        pair = ed['pair']
        target = ed['distance']
        match = next((d for d in distances if d.get('pair') == pair), None)
        if match and abs_check(match.get('distance', 0), target, 0.01):
            dist_hits += 1
    dist_score = dist_hits / dist_count if dist_count else 1.0

    static_ok = 1.0 if abs_check(artifact.get('static_dielectric', 0), expected['static_dielectric'], 0.05) else 0.0
    hf_ok = 1.0 if abs_check(artifact.get('high_frequency_dielectric', 0), expected['high_frequency_dielectric'], 0.05) else 0.0
    dens_ok = 1.0 if abs_check(artifact.get('density', 0), expected['density'], 0.01) else 0.0

    total = lattice_energy_ok + uc_score + dist_score + static_ok + hf_ok + dens_ok
    return total / 6.0


# === block: score_2 (check id='intrinsic_defect_energies') ===
def score_2(artifact, step, ctx):
    expected = step.get('expected', {})
    isolated_exp = expected.get('isolated', [])
    frenkel_exp = expected.get('frenkel', [])
    schottky_exp = expected.get('schottky', [])
    isolated = artifact.get('isolated', [])
    frenkel = artifact.get('frenkel', [])
    schottky = artifact.get('schottky', [])

    def match_energy_list(exp_list, act_list, item_key, energy_key):
        hits = 0
        for exp in exp_list:
            match = next((x for x in act_list if x.get(item_key) == exp[item_key]), None)
            if match and abs(match.get(energy_key, 0) - exp[energy_key]) <= 0.1:
                hits += 1
        return hits

    hits_isolated = match_energy_list(isolated_exp, isolated, 'defect', 'energy')
    hits_frenkel = match_energy_list(frenkel_exp, frenkel, 'type', 'energy_per_defect')
    hits_schottky = match_energy_list(schottky_exp, schottky, 'type', 'energy_per_defect')
    total_items = len(isolated_exp) + len(frenkel_exp) + len(schottky_exp)
    if total_items == 0:
        return 0.0
    score = (hits_isolated + hits_frenkel + hits_schottky) / total_items
    return score


# === block: score_3 (check id='redox_energies') ===
def score_3(artifact, step, ctx):
    expected = step.get('expected', {})
    electronic_expected = expected.get('electronic_defects', {})
    redox_expected = expected.get('redox', {})
    electronic = artifact.get('electronic_defects', {})
    redox = artifact.get('redox', {})

    def check_field(act, exp, tol):
        return abs(act - exp) <= tol

    fields_elec = ['hole_formation', 'electron_formation', 'hole_defect_energy', 'electron_defect_energy']
    fields_redox = ['oxidation_vacancy_filling', 'oxidation_interstitial_oxygen', 'reduction']
    total_fields = len(fields_elec) + len(fields_redox)
    hits = 0
    for f in fields_elec:
        if f in electronic and check_field(electronic[f], electronic_expected[f], 0.1):
            hits += 1
    for f in fields_redox:
        if f in redox and check_field(redox[f], redox_expected[f], 0.1):
            hits += 1
    return hits / total_fields if total_fields else 0.0


# === block: score_4 (check id='migration_barriers') ===
def score_4(artifact, step, ctx):
    expected = step.get('expected', {})
    pathways_exp = expected.get('pathways', [])
    pathways = artifact.get('pathways', [])
    hits = 0
    for exp in pathways_exp:
        match = next((p for p in pathways if p.get('jump_path') == exp['jump_path']), None)
        if match and abs(match.get('activation_energy', 0) - exp['activation_energy']) <= 0.05:
            hits += 1
    total = len(pathways_exp)
    return hits / total if total else 0.0


_SCORERS = {
    'potential_parameters': score_0,
    'perfect_crystal': score_1,
    'intrinsic_defect_energies': score_2,
    'redox_energies': score_3,
    'migration_barriers': score_4,
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
