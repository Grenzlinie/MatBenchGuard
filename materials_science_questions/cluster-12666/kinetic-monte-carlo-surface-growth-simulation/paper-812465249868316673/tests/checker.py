import os
import json
import csv

# === author imports / helpers ===
import math, json


import os as _ff_os
import json as _ff_json





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


# === block: score_0 (check id='shape_2x1_sym') ===
def score_0(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    if len(lines) < 3: return 0.0
    try:
        natoms = int(lines[0].strip())
    except:
        return 0.0
    if natoms != 720: return 0.0
    nlines = len(lines)
    if nlines < natoms + 2: return 0.0
    for line in lines[2:2+natoms]:
        parts = line.split()
        if len(parts) < 4 or parts[0] != 'C':
            return 0.0
    return 1.0


# === block: score_1 (check id='dimer_bond_2x1_sym') ===
def score_1(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    if len(lines) < 3: return 0.0
    try:
        natoms = int(lines[0].strip())
    except:
        return 0.0
    if natoms != 720: return 0.0
    top_atoms = []
    coords = []
    for line in lines[2:]:
        parts = line.split()
        if len(parts) < 4 or parts[0] != 'C':
            continue
        x, y, z = map(float, parts[1:4])
        coords.append((x, y, z))
    if len(coords) != 720: return 0.0
    zs = [c[2] for c in coords]
    max_z = max(zs)
    threshold = max_z - 0.5
    top_indices = [i for i, c in enumerate(coords) if c[2] > threshold]
    if len(top_indices) != 36: return 0.0
    dists = []
    for i in range(len(top_indices)):
        for j in range(i+1, len(top_indices)):
            idx1, idx2 = top_indices[i], top_indices[j]
            dx = coords[idx1][0] - coords[idx2][0]
            dy = coords[idx1][1] - coords[idx2][1]
            dz = coords[idx1][2] - coords[idx2][2]
            d = math.sqrt(dx*dx + dy*dy + dz*dz)
            if d < 2.0:
                dists.append(d)
    if not dists: return 0.0
    avg = sum(dists) / len(dists)
    target = step['target']
    tol = step['tolerance']
    diff = abs(avg - target)
    return 1.0 if diff <= tol else 0.0


# === block: score_2 (check id='shape_2x1a_asym') ===
def score_2(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    if len(lines) < 3: return 0.0
    try:
        natoms = int(lines[0].strip())
    except:
        return 0.0
    if natoms != 720: return 0.0
    nlines = len(lines)
    if nlines < natoms + 2: return 0.0
    for line in lines[2:2+natoms]:
        parts = line.split()
        if len(parts) < 4 or parts[0] != 'C':
            return 0.0
    return 1.0


# === block: score_3 (check id='dimer_bond_2x1a_asym') ===
def score_3(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    if len(lines) < 3: return 0.0
    try:
        natoms = int(lines[0].strip())
    except:
        return 0.0
    if natoms != 720: return 0.0
    top_atoms = []
    coords = []
    for line in lines[2:]:
        parts = line.split()
        if len(parts) < 4 or parts[0] != 'C':
            continue
        x, y, z = map(float, parts[1:4])
        coords.append((x, y, z))
    if len(coords) != 720: return 0.0
    zs = [c[2] for c in coords]
    max_z = max(zs)
    threshold = max_z - 0.5
    top_indices = [i for i, c in enumerate(coords) if c[2] > threshold]
    if len(top_indices) != 36: return 0.0
    dists = []
    for i in range(len(top_indices)):
        for j in range(i+1, len(top_indices)):
            idx1, idx2 = top_indices[i], top_indices[j]
            dx = coords[idx1][0] - coords[idx2][0]
            dy = coords[idx1][1] - coords[idx2][1]
            dz = coords[idx1][2] - coords[idx2][2]
            d = math.sqrt(dx*dx + dy*dy + dz*dz)
            if d < 2.0:
                dists.append(d)
    if not dists: return 0.0
    avg = sum(dists) / len(dists)
    target = step['target']
    tol = step['tolerance']
    diff = abs(avg - target)
    return 1.0 if diff <= tol else 0.0


# === block: score_4 (check id='shape_1x1_relaxed') ===
def score_4(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    if len(lines) < 3: return 0.0
    try:
        natoms = int(lines[0].strip())
    except:
        return 0.0
    if natoms != 720: return 0.0
    nlines = len(lines)
    if nlines < natoms + 2: return 0.0
    for line in lines[2:2+natoms]:
        parts = line.split()
        if len(parts) < 4 or parts[0] != 'C':
            return 0.0
    return 1.0


# === block: score_5 (check id='energy_gains_results') ===
def score_5(artifact, step, ctx):
    targets = step['targets']
    def _check(val, gold, tol):
        return 1.0 if abs(val - gold) <= tol else 0.0

    val_1x1 = artifact.get('energy_gain_1x1_per_surface_atom', None)
    val_2x1 = artifact.get('energy_gain_2x1_per_dimer', None)
    val_2x1a = artifact.get('energy_gain_2x1a_per_dimer', None)
    if val_1x1 is None or val_2x1 is None or val_2x1a is None:
        return 0.0

    s1 = _check(val_1x1, targets['energy_gain_1x1_per_surface_atom']['gold'],
               targets['energy_gain_1x1_per_surface_atom']['tolerance'])
    s2 = _check(val_2x1, targets['energy_gain_2x1_per_dimer']['gold'],
               targets['energy_gain_2x1_per_dimer']['tolerance'])
    s3 = _check(val_2x1a, targets['energy_gain_2x1a_per_dimer']['gold'],
               targets['energy_gain_2x1a_per_dimer']['tolerance'])

    # internal consistency checks
    try:
        e_bulk = artifact['energy_bulk_terminated']
        e_1x1 = artifact['energy_1x1_relaxed']
        e_2x1 = artifact['energy_2x1_sym']
        e_2x1a = artifact['energy_2x1a_asym']
    except KeyError:
        return 0.0

    c1 = 1.0 if abs((e_1x1 - e_bulk) / 36.0 - val_1x1) <= 0.02 else 0.0
    c2 = 1.0 if abs((e_2x1 - e_1x1) / 18.0 - val_2x1) <= 0.02 else 0.0
    c3 = 1.0 if abs((e_2x1a - e_1x1) / 18.0 - val_2x1a) <= 0.02 else 0.0

    gain_score = (s1 + s2 + s3) / 3.0
    cons_score = (c1 + c2 + c3) / 3.0
    return 0.85 * gain_score + 0.15 * cons_score


_SCORERS = {
    'shape_2x1_sym': score_0,
    'dimer_bond_2x1_sym': score_1,
    'shape_2x1a_asym': score_2,
    'dimer_bond_2x1a_asym': score_3,
    'shape_1x1_relaxed': score_4,
    'energy_gains_results': score_5,
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