import os
import json
import csv

# === author imports / helpers ===
import math
import json

def parse_cif_content(content):
    """Parse a CIF text and return a dict with bond distances for NN, BN1, BN2."""
    lines = content.splitlines()
    cell = {'a': None, 'b': None, 'c': None, 'alpha': 90.0, 'beta': 90.0, 'gamma': 90.0}
    atoms = []
    mode = None
    keys = []
    for line in lines:
        line = line.strip()
        if line.startswith('_'):
            if 'cell_length_a' in line:
                cell['a'] = float(line.split()[1])
            elif 'cell_length_b' in line:
                cell['b'] = float(line.split()[1])
            elif 'cell_length_c' in line:
                cell['c'] = float(line.split()[1])
            elif 'cell_angle_alpha' in line:
                cell['alpha'] = float(line.split()[1])
            elif 'cell_angle_beta' in line:
                cell['beta'] = float(line.split()[1])
            elif 'cell_angle_gamma' in line:
                cell['gamma'] = float(line.split()[1])
            elif '_atom_site_label' in line:
                keys.append('label')
            elif '_atom_site_fract_x' in line:
                keys.append('x')
            elif '_atom_site_fract_y' in line:
                keys.append('y')
            elif '_atom_site_fract_z' in line:
                keys.append('z')
        elif line.startswith('loop_') or line.startswith('loop_'):
            mode = 'atom_site'
            keys = []
        elif mode == 'atom_site' and line and line[0].isprintable() and not line.startswith('_'):
            parts = line.split()
            if len(parts) >= len(keys):
                atom = {}
                for i, key in enumerate(keys):
                    if key == 'label':
                        atom['label'] = parts[i]
                    elif key == 'x':
                        atom['x'] = float(parts[i])
                    elif key == 'y':
                        atom['y'] = float(parts[i])
                    elif key == 'z':
                        atom['z'] = float(parts[i])
                atoms.append(atom)
        else:
            pass
    if None in [cell['a'], cell['b'], cell['c']]:
        raise ValueError('Missing cell parameters')
    a = cell['a']
    b = cell['b']
    c = cell['c']
    # Build Cartesian coordinates
    cart_atoms = []
    for atom in atoms:
        x_c = a * atom['x']
        y_c = b * atom['y']
        z_c = c * atom['z']
        cart_atoms.append({'label': atom['label'], 'x': x_c, 'y': y_c, 'z': z_c})
    def min_dist_between(g1, g2):
        min_d = None
        for a1 in g1:
            for a2 in g2:
                if a1 == a2:
                    continue
                dx = a2['x'] - a1['x']
                dy = a2['y'] - a1['y']
                dz = a2['z'] - a1['z']
                dx -= round(dx / a) * a
                dy -= round(dy / a) * a
                dz -= round(dz / c) * c
                d = math.sqrt(dx*dx + dy*dy + dz*dz)
                if min_d is None or d < min_d:
                    min_d = d
        return min_d
    n1_atoms = [a for a in cart_atoms if 'N1' in a['label']]
    b_atoms = [a for a in cart_atoms if a['label'] == 'B']
    n2_atoms = [a for a in cart_atoms if 'N2' in a['label']]
    if not n1_atoms or not b_atoms or not n2_atoms:
        raise ValueError('Missing required atom labels (B, N1, N2)')
    nn = min_dist_between(n1_atoms, n1_atoms)
    bn1 = min_dist_between(b_atoms, n1_atoms)
    bn2 = min_dist_between(b_atoms, n2_atoms)
    return {'NN': nn, 'BN1': bn1, 'BN2': bn2}


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


# === block: score_0 (check id='check_structure') ===
def score_0(artifact, step, ctx):
    import math
    artifact_text = artifact if isinstance(artifact, str) else ''
    if not artifact_text:
        return 0.0
    try:
        bonds = parse_cif_content(artifact_text)
    except Exception:
        return 0.0
    gold = step['gold']
    tol = step['tolerance_relative']
    total = 0
    for key in ['NN', 'BN1', 'BN2']:
        if key in bonds and key in gold:
            if abs(bonds[key] - gold[key]) <= tol * gold[key]:
                total += 1
    return total / 3.0


# === block: score_1 (check id='check_properties') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold = step['gold']
    tolerances = step['tolerances']
    field_weights = step['field_weights']
    is_metallic_expected = step.get('is_metallic_expected', True)
    band_gap_max = step.get('band_gap_max', 0.1)
    score = 0.0
    # elastic constants
    for f in ['c11','c12','c13','c33','c44','c66']:
        if f in artifact and f in gold:
            if abs(artifact[f] - gold[f]) <= tolerances['elastic'] * abs(gold[f]):
                score += field_weights.get(f, 0.0)
    # moduli
    for f in ['bulk_modulus', 'shear_modulus']:
        if f in artifact and f in gold:
            if abs(artifact[f] - gold[f]) <= tolerances['moduli'] * abs(gold[f]):
                score += field_weights.get(f, 0.0)
    # g_over_b_ratio
    f = 'g_over_b_ratio'
    if f in artifact and f in gold:
        if abs(artifact[f] - gold[f]) <= tolerances['gb_ratio_abs']:
            score += field_weights.get(f, 0.0)
    # energy density
    f = 'energy_density_kJ_g'
    if f in artifact and f in gold:
        if abs(artifact[f] - gold[f]) <= tolerances['energy_density'] * abs(gold[f]):
            score += field_weights.get(f, 0.0)
    # is_metallic
    f = 'is_metallic'
    if f in artifact:
        if bool(artifact[f]) == is_metallic_expected:
            score += field_weights.get(f, 0.0)
    # band_gap
    f = 'band_gap_eV'
    if f in artifact:
        if artifact[f] <= band_gap_max:
            score += field_weights.get(f, 0.0)
    return min(max(score, 0.0), 1.0)


_SCORERS = {
    'check_structure': score_0,
    'check_properties': score_1,
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
