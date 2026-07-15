import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='step_geometry') ===
def score_0(artifact, step, ctx):
    def parse_xyz(text):
        lines = text.strip().splitlines()
        i = 0
        mols = []
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue
            try:
                nat = int(line)
            except ValueError:
                i += 1
                continue
            comment = lines[i+1].strip() if i+1 < len(lines) else ''
            atoms = []
            for j in range(nat):
                if i+2+j >= len(lines):
                    break
                parts = lines[i+2+j].split()
                if len(parts) >= 4:
                    elem = parts[0]
                    x = float(parts[1])
                    y = float(parts[2])
                    z = float(parts[3])
                    atoms.append((elem, (x, y, z)))
            if len(atoms) == nat:
                mols.append(atoms)
            i += 2 + nat
        return mols

    def torsion(p0, p1, p2, p3):
        b1 = (p1[0]-p0[0], p1[1]-p0[1], p1[2]-p0[2])
        b2 = (p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2])
        b3 = (p3[0]-p2[0], p3[1]-p2[1], p3[2]-p2[2])
        n1 = (b1[1]*b2[2] - b1[2]*b2[1], b1[2]*b2[0] - b1[0]*b2[2], b1[0]*b2[1] - b1[1]*b2[0])
        n2 = (b2[1]*b3[2] - b2[2]*b3[1], b2[2]*b3[0] - b2[0]*b3[2], b2[0]*b3[1] - b2[1]*b3[0])
        n1_norm = math.hypot(*n1)
        n2_norm = math.hypot(*n2)
        if n1_norm < 1e-12 or n2_norm < 1e-12:
            return 0.0
        n1 = (n1[0]/n1_norm, n1[1]/n1_norm, n1[2]/n1_norm)
        n2 = (n2[0]/n2_norm, n2[1]/n2_norm, n2[2]/n2_norm)
        cos_phi = n1[0]*n2[0] + n1[1]*n2[1] + n1[2]*n2[2]
        cos_phi = max(-1.0, min(1.0, cos_phi))
        phi = math.acos(cos_phi)
        cross = (n1[1]*n2[2] - n1[2]*n2[1], n1[2]*n2[0] - n1[0]*n2[2], n1[0]*n2[1] - n1[1]*n2[0])
        sign = 1 if (b2[0]*cross[0] + b2[1]*cross[1] + b2[2]*cross[2]) >= 0 else -1
        return sign * math.degrees(phi)

    mols = parse_xyz(artifact)
    if not mols:
        return 0.0
    within = 0
    for atoms in mols:
        s_idxs = [i for i, a in enumerate(atoms) if a[0] == 'S']
        if len(s_idxs) != 2:
            continue
        s1 = atoms[s_idxs[0]][1]
        s2 = atoms[s_idxs[1]][1]
        # nearest carbon to each sulfur
        c1_cands = [(i, math.hypot(atoms[i][1][0]-s1[0], atoms[i][1][1]-s1[1], atoms[i][1][2]-s1[2]))
                    for i, a in enumerate(atoms) if a[0] == 'C' and i != s_idxs[0] and math.hypot(atoms[i][1][0]-s1[0], atoms[i][1][1]-s1[1], atoms[i][1][2]-s1[2]) < 2.5]
        c2_cands = [(i, math.hypot(atoms[i][1][0]-s2[0], atoms[i][1][1]-s2[1], atoms[i][1][2]-s2[2]))
                    for i, a in enumerate(atoms) if a[0] == 'C' and i != s_idxs[1] and math.hypot(atoms[i][1][0]-s2[0], atoms[i][1][1]-s2[1], atoms[i][1][2]-s2[2]) < 2.5]
        if not c1_cands or not c2_cands:
            continue
        c1_idx = min(c1_cands, key=lambda x: x[1])[0]
        c2_idx = min(c2_cands, key=lambda x: x[1])[0]
        phi = torsion(atoms[c1_idx][1], s1, s2, atoms[c2_idx][1])
        delta = abs(abs(phi) - 90.0)
        if delta <= 5.0:
            within += 1
    return within / 6.0


# === block: score_1 (check id='step_orbitals') ===
def score_1(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict):
        return 0.0
    if 'H_DPDS' not in data or 'NO2_DPDS' not in data:
        return 0.0

    def sum_dict(d):
        return sum(d.values())

    def check_sum(d, tol=0.01):
        s = sum_dict(d)
        return abs(s - 1.0) <= tol

    hdpds = data['H_DPDS']
    nodpds = data['NO2_DPDS']

    # HOMO S fraction for H-DPDS
    homo_h = hdpds.get('HOMO_composition', {})
    s_frac = sum(v for k, v in homo_h.items() if k.startswith('S'))
    score_sfrac = min(1.0, s_frac / 0.5)

    # LUMO energy for NO2-DPDS
    lum_e = nodpds.get('LUMO_energy')
    if lum_e is None:
        score_lume = 0.0
    else:
        deviation = abs(lum_e - (-10.5))
        score_lume = max(0.0, 1.0 - deviation / 0.5)

    # Composition sums (4 checks)
    checks = [
        check_sum(hdpds.get('HOMO_composition', {})),
        check_sum(hdpds.get('LUMO_composition', {})),
        check_sum(nodpds.get('HOMO_composition', {})),
        check_sum(nodpds.get('LUMO_composition', {}))
    ]
    score_sum = sum(checks) / 4.0

    # LUMO N+O fraction for NO2-DPDS (paper notes strong nitro contribution)
    lumo_nodp = nodpds.get('LUMO_composition', {})
    no_frac = sum(v for k, v in lumo_nodp.items() if k.startswith('N') or k.startswith('O'))
    score_nofrac = min(1.0, no_frac / 0.5)

    return 0.3 * score_sfrac + 0.3 * score_lume + 0.2 * score_sum + 0.2 * score_nofrac


_SCORERS = {
    'step_geometry': score_0,
    'step_orbitals': score_1,
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
