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


# === block: score_0 (check id='bare_surface_structure') ===
def score_0(artifact, step, ctx):
    def parse_xyz(content):
        lines = content.strip().splitlines()
        if len(lines) < 3:
            return None, None
        try:
            num_atoms = int(lines[0].strip())
        except:
            return None, None
        atoms = []
        for line in lines[2:]:
            if not line.strip():
                continue
            parts = line.split()
            if len(parts) < 4:
                return None, None
            elem = parts[0]
            try:
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
            except:
                return None, None
            atoms.append({'elem': elem, 'z': z})
        if len(atoms) < 2:
            return None, None
        return atoms, len(atoms)

    raw = artifact
    atoms, n = parse_xyz(raw)
    if atoms is None:
        return 0.0
    # basic shape: at least 8 atoms, parseable
    shape_ok = (n >= 8 and len(atoms) >= 8)
    # group atoms by z (cluster with tolerance 0.05 Å)
    atoms_sorted = sorted(atoms, key=lambda a: a['z'], reverse=True)
    layers = []
    for a in atoms_sorted:
        if not layers or abs(a['z'] - layers[-1]['z']) > 0.05:
            layers.append({'z': a['z'], 'elems': [a['elem']]})
        else:
            layers[-1]['elems'].append(a['elem'])
    # need at least two distinct layers
    if len(layers) < 2:
        return 0.0
    # top layer should be Al, second should be O
    top_al = next((l for l in layers if 'Al' in l['elems']), None)
    if top_al is None:
        # fallback: just take first two layers
        top_al = layers[0]
    # find the next layer that contains O
    next_o = None
    for l in layers:
        if l['z'] < top_al['z'] and 'O' in l['elems']:
            next_o = l
            break
    if next_o is None:
        return 0.0
    spacing = top_al['z'] - next_o['z']
    bulk = step.get('bulk_spacing', 0.84)
    if bulk <= 0:
        return 0.0
    contraction = (spacing - bulk) / bulk * 100.0
    gold = step.get('gold_contraction', -79.4)
    tol = step.get('tolerance_contraction', 10.0)
    diff = abs(contraction - gold)
    if diff <= tol:
        contraction_score = 1.0
    else:
        contraction_score = max(0.0, 1.0 - (diff - tol) / tol)
    shape_score = 1.0 if shape_ok else 0.0
    return 0.9 * contraction_score + 0.1 * shape_score


# === block: score_1 (check id='interface_structure') ===
def score_1(artifact, step, ctx):
    def parse_xyz(content):
        lines = content.strip().splitlines()
        if len(lines) < 3:
            return None, None
        try:
            num_atoms = int(lines[0].strip())
        except:
            return None, None
        atoms = []
        for line in lines[2:]:
            if not line.strip():
                continue
            parts = line.split()
            if len(parts) < 4:
                return None, None
            elem = parts[0]
            try:
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
            except:
                return None, None
            atoms.append({'elem': elem, 'x': x, 'y': y, 'z': z})
        if len(atoms) < 2:
            return None, None
        return atoms, len(atoms)

    raw = artifact
    atoms, n = parse_xyz(raw)
    if atoms is None:
        return 0.0
    shape_ok = (n >= 10 and len(atoms) >= 10)
    # surface Al: Al with highest z
    als = [a for a in atoms if a['elem'] == 'Al']
    if not als:
        return 0.0
    al_surf = max(als, key=lambda a: a['z'])
    # bridging O: O with z > al_surf.z, closest to al_surf
    os_above = [a for a in atoms if a['elem'] == 'O' and a['z'] > al_surf['z']]
    if not os_above:
        return 0.0
    def dist2(a,b):
        return (a['x']-b['x'])**2+(a['y']-b['y'])**2+(a['z']-b['z'])**2
    br_o = min(os_above, key=lambda a: dist2(a, al_surf))
    # Al-O distance
    d_al_o = math.sqrt(dist2(br_o, al_surf))
    gold_al_o = step.get('gold_al_o_distance', 1.76)
    tol_al_o = step.get('tolerance_al_o_distance', 0.15)
    diff_al_o = abs(d_al_o - gold_al_o)
    if diff_al_o <= tol_al_o:
        al_o_score = 1.0
    else:
        al_o_score = max(0.0, 1.0 - (diff_al_o - tol_al_o) / tol_al_o)
    # O-C average distance
    cs = [a for a in atoms if a['elem'] == 'C']
    if not cs:
        o_c_score = 0.0
    else:
        d_oc_avg = sum(math.sqrt(dist2(br_o, c)) for c in cs) / len(cs)
        gold_oc = step.get('gold_o_c_average_distance', 1.76)
        tol_oc = step.get('tolerance_o_c_average_distance', 0.15)
        diff_oc = abs(d_oc_avg - gold_oc)
        if diff_oc <= tol_oc:
            o_c_score = 1.0
        else:
            o_c_score = max(0.0, 1.0 - (diff_oc - tol_oc) / tol_oc)
    # first-layer contraction: spacing from surface Al to first O below it
    os_below = [a for a in atoms if a['elem'] == 'O' and a['z'] < al_surf['z']]
    if not os_below:
        contraction_score = 0.0
    else:
        o_below = max(os_below, key=lambda a: a['z'])
        spacing = al_surf['z'] - o_below['z']
        bulk = step.get('bulk_spacing', 0.84)
        contraction = (spacing - bulk) / bulk * 100.0
        gold_contr = step.get('gold_contraction', -35.3)
        tol_contr = step.get('tolerance_contraction', 10.0)
        diff_contr = abs(contraction - gold_contr)
        if diff_contr <= tol_contr:
            contraction_score = 1.0
        else:
            contraction_score = max(0.0, 1.0 - (diff_contr - tol_contr) / tol_contr)
    shape_score = 1.0 if shape_ok else 0.0
    return 0.35 * al_o_score + 0.35 * o_c_score + 0.2 * contraction_score + 0.1 * shape_score


# === block: score_2 (check id='adhesion_energy') ===
def score_2(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict):
        return 0.0
    required = ['interface_total_energy','graphene_total_energy','al2o3_slab_total_energy','supercell_area']
    shape_ok = all(k in data for k in required)
    if not shape_ok:
        return 0.0
    try:
        E_int = float(data['interface_total_energy'])
        E_gr = float(data['graphene_total_energy'])
        E_slab = float(data['al2o3_slab_total_energy'])
        area = float(data['supercell_area'])
    except (ValueError, TypeError):
        return 0.0
    if area <= 0:
        return 0.0
    # convert from eV/Å^2 to J/m^2: 1 eV = 1.602e-19 J, 1 Å^2 = 1e-20 m^2
    E_ad = (E_int - E_gr - E_slab) * 16.02 / area
    threshold = step.get('threshold_adhesion_jpm2', 1.10)
    if E_ad >= threshold:
        adhesion_score = 1.0
    else:
        adhesion_score = max(0.0, E_ad / threshold)
    return 0.9 * adhesion_score + 0.1 * 1.0   # shape_ok already ensured, so 1.0 for shape


_SCORERS = {
    'bare_surface_structure': score_0,
    'interface_structure': score_1,
    'adhesion_energy': score_2,
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
