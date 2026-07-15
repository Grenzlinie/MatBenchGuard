import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os


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
        'dipole_D': 3.739,
        'A_MHz': 74036.22,
        'B_MHz': 11440.35,
        'C_MHz': 9909.15,
        'harmonic_data': {
            1: (3803, 56),
            2: (3650, 51),
            3: (3021, 83),
            4: (1831, 337),
            5: (1632, 59),
            6: (1437, 4),
            7: (1295, 96),
            8: (1062, 4),
            9: (571, 11),
            10: (1060, 3),
            11: (656, 12),
            12: (186, 278)
        },
        'planarity_tol_deg': 0.01,
        'dipole_tol': 0.02,
        'rot_const_tol_frac': 0.005,
        'freq_tol': {
            'low': 20.0,
            'high': 10.0,
            'nh2_torsion': 25.0
        },
        'intensity_tol': {
            'rel_frac': 0.20,
            'abs_min': 10.0,
            'nh2_torsion_abs': 50.0
        }
    }
    return gold


# === block: score_0 (check id='check_planarity') ===
def score_0(artifact, step, ctx):
    # Parse the XYZ file and compute the Hc-N-C-O dihedral deviation from planarity
    lines = artifact.strip().splitlines()
    if len(lines) < 3:
        return 0.0
    nat = int(lines[0].strip())
    atoms = []
    for i, line in enumerate(lines[2:2+nat], start=2):
        parts = line.split()
        if len(parts) >= 4:
            sym = parts[0]
            x, y, z = map(float, parts[1:4])
            atoms.append((sym, (x, y, z)))

    # Find N, C, O
    n_coord = c_coord = o_coord = None
    for sym, coord in atoms:
        if sym == 'N': n_coord = coord
        elif sym == 'C': c_coord = coord
        elif sym == 'O': o_coord = coord
    if n_coord is None or c_coord is None or o_coord is None:
        return 0.0

    # Find Hs attached to N (distance < 1.2 Å)
    h_nitrogens = []
    for sym, coord in atoms:
        if sym == 'H':
            dx = coord[0]-n_coord[0]
            dy = coord[1]-n_coord[1]
            dz = coord[2]-n_coord[2]
            dist = math.sqrt(dx*dx+dy*dy+dz*dz)
            if dist < 1.2:
                h_nitrogens.append(coord)
    if len(h_nitrogens) != 2:
        return 0.0

    # Identify Hc (cis to O) as the one closer to O
    dist0 = math.sqrt((h_nitrogens[0][0]-o_coord[0])**2 + (h_nitrogens[0][1]-o_coord[1])**2 + (h_nitrogens[0][2]-o_coord[2])**2)
    dist1 = math.sqrt((h_nitrogens[1][0]-o_coord[0])**2 + (h_nitrogens[1][1]-o_coord[1])**2 + (h_nitrogens[1][2]-o_coord[2])**2)
    if dist0 < dist1:
        hc = h_nitrogens[0]
    else:
        hc = h_nitrogens[1]

    # Compute dihedral Hc-N-C-O
    # Vectors: b1 = N-Hc, b2 = C-N, b3 = O-C? Actually standard dihedral (p0,p1,p2,p3): angle between planes (p0,p1,p2) and (p1,p2,p3).
    # So p0=Hc, p1=N, p2=C, p3=O.
    p0 = hc
    p1 = n_coord
    p2 = c_coord
    p3 = o_coord

    def vec_sub(a, b):
        return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
    def cross(u, v):
        return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
    def dot(u, v):
        return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
    def norm(v):
        return math.sqrt(dot(v,v))

    v0 = vec_sub(p0, p1)  # Hc->N ? Actually p0-p1
    v1 = vec_sub(p2, p1)  # C-N
    v2 = vec_sub(p3, p2)  # O-C
    # Planes: (p0,p1,p2) normal n1 = cross(v0, v1)
    #          (p1,p2,p3) normal n2 = cross(v1, v2)
    n1 = cross(v0, v1)
    n2 = cross(v1, v2)
    # dihedral angle using atan2 formula: angle = atan2( dot(cross(n1,n2), v1)/|v1|, dot(n1,n2) )
    cross_n1n2 = cross(n1, n2)
    arg1 = dot(cross_n1n2, v1) / norm(v1)
    arg2 = dot(n1, n2)
    angle_rad = math.atan2(arg1, arg2)
    angle_deg = math.degrees(angle_rad)
    # Bring into [-180,180] and compute deviation from 0 or 180
    angle_deg = (angle_deg + 180) % 360 - 180  # now in [-180,180]
    dev = min(abs(angle_deg), 180 - abs(angle_deg))  # deviation from 0 or 180
    tol = ctx['planarity_tol_deg']
    if dev <= tol:
        return 1.0
    # partial credit: linear decay up to 5*tol
    score = max(0.0, 1.0 - (dev - tol) / (tol * 4))
    return score


# === block: score_1 (check id='check_molecular_params') ===
def score_1(artifact, step, ctx):
    # Read TSV, compare dipole and rotational constants
    reader = csv.DictReader(artifact.splitlines(), delimiter='\t')
    if reader.fieldnames is None or 'property' not in reader.fieldnames or 'value' not in reader.fieldnames:
        return 0.0
    props = {}
    for row in reader:
        prop = row['property'].strip()
        try:
            val = float(row['value'].strip())
        except:
            continue
        props[prop] = val

    # Define expected and tolerances
    expected = {
        'dipole_moment_D': ctx['dipole_D'],
        'A_MHz': ctx['A_MHz'],
        'B_MHz': ctx['B_MHz'],
        'C_MHz': ctx['C_MHz']
    }
    # For dipole, absolute tolerance; for rot const, relative tolerance
    scores = []
    for prop, gold in expected.items():
        if prop not in props:
            scores.append(0.0)
            continue
        agent_val = props[prop]
        if prop == 'dipole_moment_D':
            tol = ctx['dipole_tol']
            error = abs(agent_val - gold)
            if error <= tol:
                s = 1.0
            else:
                s = max(0.0, 1.0 - (error - tol) / (tol * 2))
        else:  # rotational constants
            tol_frac = ctx['rot_const_tol_frac']
            rel = abs(agent_val - gold) / gold
            if rel <= tol_frac:
                s = 1.0
            else:
                s = max(0.0, 1.0 - (rel - tol_frac) / (tol_frac * 2))
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='check_harmonic_data') ===
def score_2(artifact, step, ctx):
    # Read harmonic data TSV, build list of (wavenumber, intensity) pairs
    reader = csv.DictReader(artifact.splitlines(), delimiter='\t')
    if reader.fieldnames is None or 'wavenumber_cm1' not in reader.fieldnames or 'intensity_km_mol' not in reader.fieldnames:
        return 0.0
    agent_pairs = []
    for row in reader:
        try:
            wavenum = float(row['wavenumber_cm1'].strip())
            intensity = float(row['intensity_km_mol'].strip())
            agent_pairs.append((wavenum, intensity))
        except Exception:
            continue
    if len(agent_pairs) != 12:
        return 0.0

    # Sort both agent and gold by increasing wavenumber
    agent_sorted = sorted(agent_pairs, key=lambda x: x[0])
    gold_items = ctx['harmonic_data'].items()  # (index, (wave, int))
    gold_pairs = sorted([(wave, intens) for _, (wave, intens) in gold_items], key=lambda x: x[0])

    mode_scores = []
    for (agent_wave, agent_int), (gold_wave, gold_int) in zip(agent_sorted, gold_pairs):
        # wavenumber tolerance
        if abs(gold_wave - 186.0) < 0.01:   # NH2 torsion
            wave_tol = ctx['freq_tol']['nh2_torsion']
        elif gold_wave > 1000:
            wave_tol = ctx['freq_tol']['high']
        else:
            wave_tol = ctx['freq_tol']['low']
        wave_error = abs(agent_wave - gold_wave)
        if wave_error <= wave_tol:
            wave_score = 1.0
        else:
            wave_score = max(0.0, 1.0 - (wave_error - wave_tol) / wave_tol)

        # intensity tolerance
        if abs(gold_wave - 186.0) < 0.01:
            int_tol = ctx['intensity_tol']['nh2_torsion_abs']
        else:
            int_tol = max(ctx['intensity_tol']['rel_frac'] * gold_int, ctx['intensity_tol']['abs_min'])
        int_error = abs(agent_int - gold_int)
        if int_error <= int_tol:
            int_score = 1.0
        else:
            int_score = max(0.0, 1.0 - (int_error - int_tol) / int_tol)

        mode_score = (wave_score + int_score) / 2.0
        mode_scores.append(mode_score)

    return sum(mode_scores) / len(mode_scores) if mode_scores else 0.0


_SCORERS = {
    'check_planarity': score_0,
    'check_molecular_params': score_1,
    'check_harmonic_data': score_2,
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
