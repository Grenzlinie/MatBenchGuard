import os
import json
import csv

# === author imports / helpers ===
import math


def find_atoms(geometry, symbol):
    return [i for i, a in enumerate(geometry) if a['symbol'] == symbol]


def distance(p1, p2):
    return math.sqrt(sum((p1[k] - p2[k]) ** 2 for k in ['x', 'y', 'z']))


def analyze_fe_bonds(geometry):
    """Identify diketonate ligands in the truncated Fe complex.
    Returns (C-O_avg, C-C_avg) or raises if identification fails."""
    fe_idx = find_atoms(geometry, 'Fe')
    if len(fe_idx) != 1:
        raise ValueError('Expected one Fe atom')
    fe = fe_idx[0]
    # find O atoms within bonding distance of Fe
    oxygens = []
    for i, a in enumerate(geometry):
        if a['symbol'] == 'O' and distance(geometry[fe], a) < 2.5:
            oxygens.append(i)
    if len(oxygens) != 6:
        raise ValueError('Expected 6 O atoms bound to Fe, found {}'.format(len(oxygens)))
    # for each O, find nearest C (C-O bond ~1.2-1.5 Å)
    o_c_pairs = []
    for o_idx in oxygens:
        c_candidates = []
        for i, a in enumerate(geometry):
            if a['symbol'] == 'C':
                d = distance(geometry[o_idx], a)
                if 1.15 < d < 1.55:
                    c_candidates.append((i, d))
        if not c_candidates:
            raise ValueError(f'O {o_idx} has no nearby C')
        c_candidates.sort(key=lambda x: x[1])
        o_c_pairs.append((o_idx, c_candidates[0][0]))
    # group into three ligands: O-Fe-O triplets
    # use O-O distance within same ligand (< 3.5 Å) and O-Fe-O angle rough
    ligands = []
    used_o = set()
    for i in range(len(o_c_pairs)):
        if i in used_o:
            continue
        for j in range(i + 1, len(o_c_pairs)):
            if j in used_o:
                continue
            o1 = o_c_pairs[i][0]
            o2 = o_c_pairs[j][0]
            d_oo = distance(geometry[o1], geometry[o2])
            if 2.5 < d_oo < 3.6:
                ligands.append((o_c_pairs[i], o_c_pairs[j]))
                used_o.add(i)
                used_o.add(j)
                break
    if len(ligands) != 3:
        raise ValueError(f'Could not identify 3 diketonate ligands, got {len(ligands)}')
    # compute C-C and C-O distances
    cc_values = []
    co_values = []
    for (o1, c1), (o2, c2) in ligands:
        d_cc = distance(geometry[c1], geometry[c2])
        cc_values.append(d_cc)
        co_values.append(distance(geometry[o1], geometry[c1]))
        co_values.append(distance(geometry[o2], geometry[c2]))
    C_O_avg = sum(co_values) / len(co_values)
    C_C_avg = sum(cc_values) / len(cc_values)
    return C_O_avg, C_C_avg


def analyze_ni_bonds(geometry):
    """Identify diketonate ligand in Ni complex.
    Returns (C-O_avg, C-C) or raises."""
    ni_idx = find_atoms(geometry, 'Ni')
    if len(ni_idx) != 1:
        raise ValueError('Expected one Ni atom')
    ni = ni_idx[0]
    oxygens = []
    for i, a in enumerate(geometry):
        if a['symbol'] == 'O' and distance(geometry[ni], a) < 2.4:
            oxygens.append(i)
    if len(oxygens) != 2:
        raise ValueError('Expected 2 O atoms bound to Ni, found {}'.format(len(oxygens)))
    # find attached C
    o_c_pairs = []
    for o_idx in oxygens:
        best = None
        best_dist = float('inf')
        for i, a in enumerate(geometry):
            if a['symbol'] == 'C':
                d = distance(geometry[o_idx], a)
                if 1.15 < d < 1.55 and d < best_dist:
                    best_dist = d
                    best = i
        if best is None:
            raise ValueError(f'O {o_idx} has no bonded C')
        o_c_pairs.append((o_idx, best))
    c1 = o_c_pairs[0][1]
    c2 = o_c_pairs[1][1]
    C_C = distance(geometry[c1], geometry[c2])
    co1 = distance(geometry[o_c_pairs[0][0]], geometry[c1])
    co2 = distance(geometry[o_c_pairs[1][0]], geometry[c2])
    C_O_avg = (co1 + co2) / 2.0
    return C_O_avg, C_C


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
    gold = {
        'fe': {
            'C-O_avg': spec['steps'][0]['target']['C-O_avg'],
            'C-C': spec['steps'][0]['target']['C-C'],
            'tolerance': spec['steps'][0]['tolerance_abs']
        },
        'ni': {
            'C-O_avg': spec['steps'][1]['target']['C-O_avg'],
            'C-C': spec['steps'][1]['target']['C-C'],
            'tolerance': spec['steps'][1]['tolerance_abs']
        }
    }
    return gold


# === block: score_0 (check id='fe_bond_lengths') ===
def score_0(artifact, step, ctx):
    geom = artifact.get('geometry')
    if not geom:
        return 0.0
    try:
        c_o_comp, c_c_comp = analyze_fe_bonds(geom)
    except Exception as e:
        return 0.0
    target_co = ctx['fe']['C-O_avg']
    target_cc = ctx['fe']['C-C']
    tol = ctx['fe']['tolerance']
    err_co = abs(c_o_comp - target_co)
    err_cc = abs(c_c_comp - target_cc)
    max_err = max(err_co, err_cc)
    if max_err <= tol:
        return 1.0
    else:
        # linear decay to 0 at 5*tol
        score = max(0.0, 1.0 - (max_err - tol) / (4 * tol))
        return round(score, 4)


# === block: score_1 (check id='ni_bond_lengths') ===
def score_1(artifact, step, ctx):
    geom = artifact.get('geometry')
    if not geom:
        return 0.0
    try:
        c_o_comp, c_c_comp = analyze_ni_bonds(geom)
    except Exception as e:
        return 0.0
    target_co = ctx['ni']['C-O_avg']
    target_cc = ctx['ni']['C-C']
    tol = ctx['ni']['tolerance']
    err_co = abs(c_o_comp - target_co)
    err_cc = abs(c_c_comp - target_cc)
    max_err = max(err_co, err_cc)
    if max_err <= tol:
        return 1.0
    else:
        score = max(0.0, 1.0 - (max_err - tol) / (4 * tol))
        return round(score, 4)


# === block: score_2 (check id='fe_spin_consistency') ===
def score_2(artifact, step, ctx):
    fe = artifact.get('mulliken_spin_fe')
    ligands = artifact.get('mulliken_spin_ligands')
    if fe is None or ligands is None or len(ligands) != 3:
        return 0.0
    spin_sum = fe + sum(ligands)
    expected = step['expected_sum']
    tol = step['sum_tolerance']
    # sum deviation score
    if abs(spin_sum - expected) <= tol:
        sum_score = 1.0
    else:
        sum_score = max(0.0, 1.0 - (abs(spin_sum - expected) - tol) / tol)
    # sign checks: Fe positive, each ligand negative
    sign_ok = fe > step['fe_positive_min'] and all(l < step['ligand_negative_max'] for l in ligands)
    sign_score = 0.3 if sign_ok else 0.0
    return round(sum_score * 0.7 + sign_score, 4)


# === block: score_3 (check id='ni_spin_consistency') ===
def score_3(artifact, step, ctx):
    ni = artifact.get('mulliken_spin_ni')
    ligand = artifact.get('mulliken_spin_ligand')
    if ni is None or ligand is None:
        return 0.0
    spin_sum = ni + ligand
    expected = step['expected_sum']
    tol = step['sum_tolerance']
    if abs(spin_sum - expected) <= tol:
        sum_score = 1.0
    else:
        sum_score = max(0.0, 1.0 - (abs(spin_sum - expected) - tol) / tol)
    sign_ok = ni > step['metal_positive_min'] and ligand < step['ligand_negative_max']
    sign_score = 0.3 if sign_ok else 0.0
    return round(sum_score * 0.7 + sign_score, 4)


# === block: score_4 (check id='fe_orbital_counts') ===
def score_4(artifact, step, ctx):
    alpha = artifact.get('num_alpha_singly_occupied')
    beta = artifact.get('num_beta_singly_occupied')
    if alpha == step['alpha'] and beta == step['beta']:
        return 1.0
    return 0.0


# === block: score_5 (check id='ni_orbital_counts') ===
def score_5(artifact, step, ctx):
    alpha = artifact.get('num_alpha_singly_occupied')
    beta = artifact.get('num_beta_singly_occupied')
    if alpha == step['alpha'] and beta == step['beta']:
        return 1.0
    return 0.0


_SCORERS = {
    'fe_bond_lengths': score_0,
    'ni_bond_lengths': score_1,
    'fe_spin_consistency': score_2,
    'ni_spin_consistency': score_3,
    'fe_orbital_counts': score_4,
    'ni_orbital_counts': score_5,
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
