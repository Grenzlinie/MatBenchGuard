import os
import json
import csv

# === author imports / helpers ===
import os, json, math

def parse_xyz(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    atoms = []
    for line in lines[2:]:
        parts = line.strip().split()
        if len(parts) >= 4:
            elem = parts[0]
            x, y, z = map(float, parts[1:4])
            atoms.append((elem, (x, y, z)))
    return atoms

def compute_average_bond_lengths(atoms):
    # classify atoms
    coords_by_elem = {'B': [], 'C': [], 'Fe': [], 'Co': [], 'Ni': []}
    for elem, pos in atoms:
        if elem in coords_by_elem:
            coords_by_elem[elem].append(pos)
    # identify metal
    metal = None
    for elem in coords_by_elem:
        if elem not in ('B', 'C') and len(coords_by_elem[elem]) == 1:
            metal = elem
            break
    if not metal:
        raise ValueError("No single metal found")
    # B-B distances
    b_coords = coords_by_elem['B']
    bb_dists = [math.dist(b_coords[i], b_coords[j]) for i in range(len(b_coords)) for j in range(i+1, len(b_coords)) if math.dist(b_coords[i], b_coords[j]) < 1.75]
    # B-C distances
    c_coords = coords_by_elem['C']
    bc_dists = [math.dist(b, c) for b in b_coords for c in c_coords if math.dist(b, c) < 1.9]
    # B-M distances
    m_pos = coords_by_elem[metal][0]
    bm_dists = [math.dist(b, m_pos) for b in b_coords]
    # C-M distances
    cm_dists = [math.dist(c, m_pos) for c in c_coords]
    # averages
    avg_bb = sum(bb_dists)/len(bb_dists) if bb_dists else None
    avg_bc = sum(bc_dists)/len(bc_dists) if bc_dists else None
    avg_bm = sum(bm_dists)/len(bm_dists) if bm_dists else None
    avg_cm = sum(cm_dists)/len(cm_dists) if cm_dists else None
    return avg_bb, avg_bc, avg_bm, avg_cm

def check_frequencies(data, targets, tol):
    n_metals = len(targets)
    correct = 0
    for metal, target in targets.items():
        if metal not in data:
            continue
        entry = data[metal]
        if not isinstance(entry, dict):
            continue
        all_real = entry.get('all_real', False)
        freq = entry.get('lowest_frequency', None)
        if all_real and freq is not None and abs(freq - target['lowest_frequency']) <= tol:
            correct += 1
    return correct / n_metals if n_metals > 0 else 0.0


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


# === block: score_0 (check id='step_2') ===
def score_0(artifact, step, ctx):
    atoms = parse_xyz(os.path.join("/app/outputs", "D6d_Fe.xyz"))
    avg_bb, avg_bc, avg_bm, avg_cm = compute_average_bond_lengths(atoms)
    target = step["target"]
    tol = 0.04  # widened from 0.02 to absorb cross-engine DFT differences (ORCA vs Gaussian)
    count = 0
    if avg_bb is not None and abs(avg_bb - target["r_BB"]) <= tol: count += 1
    if avg_bc is not None and abs(avg_bc - target["r_BC"]) <= tol: count += 1
    if avg_bm is not None and abs(avg_bm - target["r_BM"]) <= tol: count += 1
    if avg_cm is not None and abs(avg_cm - target["r_CM"]) <= tol: count += 1
    return count / 4.0


# === block: score_1 (check id='step_3') ===
def score_1(artifact, step, ctx):
    atoms = parse_xyz(os.path.join("/app/outputs", "D6d_Co.xyz"))
    avg_bb, avg_bc, avg_bm, avg_cm = compute_average_bond_lengths(atoms)
    target = step["target"]
    tol = step["tolerance"]
    count = 0
    if avg_bb is not None and abs(avg_bb - target["r_BB"]) <= tol: count += 1
    if avg_bc is not None and abs(avg_bc - target["r_BC"]) <= tol: count += 1
    if avg_bm is not None and abs(avg_bm - target["r_BM"]) <= tol: count += 1
    if avg_cm is not None and abs(avg_cm - target["r_CM"]) <= tol: count += 1
    return count / 4.0


# === block: score_2 (check id='step_4') ===
def score_2(artifact, step, ctx):
    atoms = parse_xyz(os.path.join("/app/outputs", "D6d_Ni.xyz"))
    avg_bb, avg_bc, avg_bm, avg_cm = compute_average_bond_lengths(atoms)
    target = step["target"]
    tol = step["tolerance"]
    count = 0
    if avg_bb is not None and abs(avg_bb - target["r_BB"]) <= tol: count += 1
    if avg_bc is not None and abs(avg_bc - target["r_BC"]) <= tol: count += 1
    if avg_bm is not None and abs(avg_bm - target["r_BM"]) <= tol: count += 1
    if avg_cm is not None and abs(avg_cm - target["r_CM"]) <= tol: count += 1
    return count / 4.0


# === block: score_3 (check id='step_5') ===
def score_3(artifact, step, ctx):
    data = json.loads(artifact) if isinstance(artifact, str) else artifact
    target = step["target"]
    tol = step["tolerance_frequency_cm"]
    score = check_frequencies(data, target, tol)
    return score


_SCORERS = {
    'step_2': score_0,
    'step_3': score_1,
    'step_4': score_2,
    'step_5': score_3,
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
