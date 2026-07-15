import os
import json
import csv

# === author imports / helpers ===
import math, json


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


# === block: score_0 (check id='clean_structure') ===
def score_0(artifact, step, ctx):
    lines = artifact.strip().split('\n')
    natoms = int(lines[0])
    symbols = []
    coords = []
    for line in lines[2:2+natoms]:
        parts = line.split()
        if len(parts) < 4: continue
        sym = parts[0]
        x,y,z = float(parts[1]), float(parts[2]), float(parts[3])
        symbols.append(sym)
        coords.append((x,y,z))
    al_indices = [i for i,s in enumerate(symbols) if s.strip() == 'Al']
    if not al_indices: return 0.0
    al_i_idx = max(al_indices, key=lambda i: coords[i][2])
    al_i = coords[al_i_idx]
    o_neighbors = []
    for i in range(len(coords)):
        if symbols[i].strip() == 'O':
            dx = coords[i][0]-al_i[0]
            dy = coords[i][1]-al_i[1]
            dz = coords[i][2]-al_i[2]
            d = math.sqrt(dx*dx+dy*dy+dz*dz)
            if d < 2.2:
                o_neighbors.append((i, d, coords[i]))
    o_neighbors.sort(key=lambda x: x[1])
    o_OI = o_neighbors[:3]
    if len(o_OI) < 3:
        return 0.0
    mean_o_z = sum(o[2][2] for o in o_OI)/3.0
    d_spacing = al_i[2] - mean_o_z
    avg_bond = sum(o[1] for o in o_OI)/3.0
    cfg = step.get('config', {})
    def score_val(val, target, tol):
        if abs(val - target) <= tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (abs(val-target)-tol)/tol)
    scores = []
    scores.append(score_val(d_spacing, cfg['d_spacing']['target'], cfg['d_spacing']['tol']))
    scores.append(score_val(avg_bond, cfg['bond_length']['target'], cfg['bond_length']['tol']))
    return sum(scores)/len(scores)


# === block: score_1 (check id='clean_energies') ===
def score_1(artifact, step, ctx):
    a = artifact
    unrelax_e = a.get('unrelaxed_total_energy')
    relax_e = a.get('relaxed_total_energy')
    unrelax_lumo = a.get('unrelaxed_LUMO_energy')
    relax_lumo = a.get('relaxed_LUMO_energy')
    area = a.get('surface_area_A2')
    if any(v is None for v in [unrelax_e, relax_e, unrelax_lumo, relax_lumo, area]):
        return 0.0
    delta_e = relax_e - unrelax_e
    kcal = delta_e * 627.5095
    jpm2 = kcal * 4184.0 / (area * 1e-20) if area > 0 else 0.0
    lumo_shift = relax_lumo - unrelax_lumo
    cfg = step.get('config', {})
    def score_val(val, target, tol):
        if abs(val - target) <= tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (abs(val-target)-tol)/tol)
    scores = []
    scores.append(score_val(kcal, cfg['relaxation_kcal']['target'], cfg['relaxation_kcal']['tol']))
    scores.append(score_val(jpm2, cfg['relaxation_Jpm2']['target'], cfg['relaxation_Jpm2']['tol']))
    scores.append(score_val(lumo_shift, cfg['LUMO_shift']['target'], cfg['LUMO_shift']['tol']))
    return sum(scores)/len(scores)


# === block: score_2 (check id='co_structure') ===
def score_2(artifact, step, ctx):
    lines = artifact.strip().split('\n')
    natoms = int(lines[0])
    symbols = []
    coords = []
    for line in lines[2:2+natoms]:
        parts = line.split()
        if len(parts) < 4: continue
        sym = parts[0]
        x,y,z = float(parts[1]), float(parts[2]), float(parts[3])
        symbols.append(sym)
        coords.append((x,y,z))
    c_atoms = [i for i,s in enumerate(symbols) if s.strip() == 'C']
    o_atoms = [i for i,s in enumerate(symbols) if s.strip() == 'O']
    if not c_atoms or not o_atoms:
        return 0.0
    c_idx = c_atoms[0]  # assume only one C
    c_coord = coords[c_idx]
    min_d = None
    for o_idx in o_atoms:
        dx = coords[o_idx][0]-c_coord[0]
        dy = coords[o_idx][1]-c_coord[1]
        dz = coords[o_idx][2]-c_coord[2]
        d = math.sqrt(dx*dx+dy*dy+dz*dz)
        if min_d is None or d < min_d:
            min_d = d
    cfg = step.get('config', {}).get('C_O_bond_length', {})
    target = cfg.get('target', 1.134)
    tol = cfg.get('tol', 0.02)
    if abs(min_d - target) <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (abs(min_d-target)-tol)/tol)


# === block: score_3 (check id='ads_enthalpy') ===
def score_3(artifact, step, ctx):
    a = artifact
    val = a.get('adsorption_enthalpy_kcal_per_mol')
    if val is None:
        return 0.0
    cfg = step.get('config', {}).get('enthalpy', {})
    target = cfg.get('target', -13.36)
    tol = cfg.get('tol', 2.0)
    diff = abs(val - target)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol)/tol)


# === block: score_4 (check id='ads_frequency') ===
def score_4(artifact, step, ctx):
    a = artifact
    val = a.get('C_O_stretching_frequency_cm-1')
    if val is None:
        return 0.0
    cfg = step.get('config', {}).get('frequency', {})
    target = cfg.get('target', 2158)
    tol = cfg.get('tol', 20.0)
    diff = abs(val - target)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol)/tol)


_SCORERS = {
    'clean_structure': score_0,
    'clean_energies': score_1,
    'co_structure': score_2,
    'ads_enthalpy': score_3,
    'ads_frequency': score_4,
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
