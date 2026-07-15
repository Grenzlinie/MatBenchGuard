import os
import json
import csv

# === author imports / helpers ===
import json
import os
import math

def parse_xyz(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    natoms = int(lines[0].strip())
    atoms = []
    for line in lines[2:2+natoms]:
        parts = line.strip().split()
        if len(parts) >= 4:
            elem = parts[0]
            x = float(parts[1])
            y = float(parts[2])
            z = float(parts[3])
            atoms.append((elem, x, y, z))
    return atoms

def compute_coordination(atoms):
    radii = {'O':0.66, 'C':0.75, 'Si':1.11}
    ideal = {'O':2, 'C':4, 'Si':4}
    for a in atoms:
        et = a[0]
        if et not in radii:
            raise ValueError(f"Unknown element {et}")
    n = len(atoms)
    neighbors = [0]*n
    for i in range(n):
        ei = atoms[i][0]
        ri = radii[ei]
        xi, yi, zi = atoms[i][1], atoms[i][2], atoms[i][3]
        for j in range(i+1, n):
            ej = atoms[j][0]
            rj = radii[ej]
            dx = xi - atoms[j][1]
            dy = yi - atoms[j][2]
            dz = zi - atoms[j][3]
            d2 = dx*dx + dy*dy + dz*dz
            cutoff = 1.2 * (ri + rj)
            if d2 <= cutoff*cutoff:
                neighbors[i] += 1
                neighbors[j] += 1
    counts = {}
    for (elem, idel) in ideal.items():
        counts[elem] = {-2:0, -1:0, 0:0, 1:0, 2:0}
    for i, atom in enumerate(atoms):
        elem = atom[0]
        dev = neighbors[i] - ideal[elem]
        if dev < -2:
            dev = -2
        elif dev > 2:
            dev = 2
        counts[elem][dev] += 1
    return counts

def to_int_keys(d):
    if not isinstance(d, dict):
        return {}
    out = {}
    for k, v in d.items():
        try:
            key_int = int(k)
        except:
            key_int = k
        out[key_int] = v
    return out


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


# === block: score_0 (check id='xyz_66sph1_exists') ===
def score_0(artifact, step, ctx):
    path = os.path.join('/app/outputs', '66-sph-1_final.xyz')
    if not os.path.exists(path):
        return 0.0
    try:
        atoms = parse_xyz(path)
    except Exception:
        return 0.0
    with open(path) as f:
        lines = f.readlines()
    if len(lines) < 2 or '66-sph-1' not in lines[1]:
        return 0.0
    if len(lines) >= 2 and int(lines[0].strip()) != len(atoms):
        return 0.0
    return 1.0


# === block: score_1 (check id='xyz_66sup_exists') ===
def score_1(artifact, step, ctx):
    path = os.path.join('/app/outputs', '66-sup_final.xyz')
    if not os.path.exists(path):
        return 0.0
    try:
        atoms = parse_xyz(path)
    except Exception:
        return 0.0
    with open(path) as f:
        lines = f.readlines()
    if len(lines) < 2 or '66-sup' not in lines[1]:
        return 0.0
    if len(lines) >= 2 and int(lines[0].strip()) != len(atoms):
        return 0.0
    return 1.0


# === block: score_2 (check id='coordination_errors') ===
def score_2(artifact, step, ctx):
    if artifact is None:
        return 0.0
    if not isinstance(artifact, dict) or '66-sph-1' not in artifact or '66-sup' not in artifact:
        return 0.0
    for model in ['66-sph-1', '66-sup']:
        mod = artifact[model]
        if 'initial' not in mod or 'final' not in mod:
            return 0.0
    xyz_sph = os.path.join('/app/outputs', '66-sph-1_final.xyz')
    xyz_sup = os.path.join('/app/outputs', '66-sup_final.xyz')
    if not os.path.exists(xyz_sph) or not os.path.exists(xyz_sup):
        return 0.0
    try:
        atoms_sph = parse_xyz(xyz_sph)
        atoms_sup = parse_xyz(xyz_sup)
        final_sph = compute_coordination(atoms_sph)
        final_sup = compute_coordination(atoms_sup)
    except Exception:
        return 0.0
    agent_final_sph = artifact['66-sph-1']['final']
    agent_final_sup = artifact['66-sup']['final']
    elements = ['O','C','Si']
    deviations = [-2,-1,0,1,2]
    penal = 0
    for model, agent_data, rec_data in [('66-sph-1', agent_final_sph, final_sph), ('66-sup', agent_final_sup, final_sup)]:
        for el in elements:
            a_el = to_int_keys(agent_data.get(el, {}))
            for d in deviations:
                reported = a_el.get(d, 0)
                recomputed = rec_data.get(el, {}).get(d, 0)
                diff = abs(reported - recomputed)
                if diff > 1:
                    penal += 1
    consistency_score = max(0.0, 1.0 - 0.1 * penal)
    def total_under(coord_data):
        total = 0
        for el in elements:
            el_data = to_int_keys(coord_data.get(el, {}))
            total += el_data.get(-2, 0) + el_data.get(-1, 0)
        return total
    initial_sph = artifact['66-sph-1']['initial']
    initial_sup = artifact['66-sup']['initial']
    initial_under_sph = total_under(initial_sph)
    final_under_sph = total_under(final_sph)
    initial_under_sup = total_under(initial_sup)
    final_under_sup = total_under(final_sup)
    trend1_score = 1.0 if (final_under_sph < initial_under_sph and final_under_sup < initial_under_sup) else (0.5 if (final_under_sph < initial_under_sph or final_under_sup < initial_under_sup) else 0.0)
    def carbon_under(coord_data):
        return coord_data.get('C', {}).get(-1, 0) + coord_data.get('C', {}).get(-2, 0)
    c_under_sph = carbon_under(final_sph)
    c_under_sup = carbon_under(final_sup)
    if c_under_sup >= c_under_sph + 5:
        trend2_score = 1.0
    elif c_under_sup > c_under_sph:
        trend2_score = 0.5
    else:
        trend2_score = 0.0
    return 0.5*consistency_score + 0.3*trend1_score + 0.2*trend2_score


_SCORERS = {
    'xyz_66sph1_exists': score_0,
    'xyz_66sup_exists': score_1,
    'coordination_errors': score_2,
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
