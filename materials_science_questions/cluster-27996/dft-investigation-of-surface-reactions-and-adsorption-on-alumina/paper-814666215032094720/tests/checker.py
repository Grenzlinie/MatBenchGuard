import os
import json
import csv

# === author imports / helpers ===
import math
from typing import Dict, Any


def parse_xyz_lines(xyz_str):
    """Return list of (element, x, y, z) from xyz string (may include header lines)."""
    atoms = []
    lines = xyz_str.strip().splitlines()
    # Skip comment line if present; first line often number of atoms
    # We'll just parse lines that start with element symbol
    for line in lines:
        parts = line.split()
        if len(parts) >= 4:
            elem = parts[0]
            try:
                x = float(parts[1])
                y = float(parts[2])
                z = float(parts[3])
                if elem in ('H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr'):
                    atoms.append((elem, x, y, z))
            except ValueError:
                continue
    return atoms


def distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


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


# === block: score_0 (check id='step_dft_validation') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        xyz = artifact.get('coordinates_xyz')
        if not isinstance(xyz, str) or not xyz.strip():
            return 0.0
        atoms = parse_xyz_lines(xyz)
        # collect Al and P, O
        p_atoms = [a for a in atoms if a[0] == 'P']
        if not p_atoms:
            return 0.0
        p_pos = p_atoms[0][1:]
        o_atoms = [a for a in atoms if a[0] == 'O']
        al_atoms = [a for a in atoms if a[0] == 'Al']
        # PO3 oxygens: O atoms within 1.8 Å of P
        po_oxygens = []
        for o in o_atoms:
            d = distance(p_pos, o[1:])
            if d < 1.8:
                po_oxygens.append(o)
        if len(po_oxygens) < 2:
            return 0.0  # insufficient PO3 oxygens
        bond_count = 0
        for o in po_oxygens:
            o_pos = o[1:]
            # find nearest Al
            if not al_atoms:
                return 0.0
            min_dist = min((distance(o_pos, a[1:]) for a in al_atoms), default=10.0)
            if 1.8 <= min_dist <= 2.2:
                bond_count += 1
        # exactly two bonds expected
        if bond_count == 2:
            return 1.0
        elif bond_count == 1:
            return 0.5  # partial credit
        else:
            return 0.0


# === block: score_1 (check id='step_qmmm_hbond') ===
def score_1(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        xyz = artifact.get('coordinates_xyz', '')
        if not isinstance(xyz, str) or not xyz.strip():
            return 0.0
        atoms = parse_xyz_lines(xyz)
        # find P and OPA oxygens
        p_atoms = [a for a in atoms if a[0] == 'P']
        if not p_atoms:
            return 0.0
        p_pos = p_atoms[0][1:]
        o_atoms = [a for a in atoms if a[0] == 'O']
        # PO3 oxygens
        opa_oxygens = []
        for o in o_atoms:
            if distance(p_pos, o[1:]) < 1.8:
                opa_oxygens.append(o)
        # find Al atoms and OH hydrogens
        al_atoms = [a for a in atoms if a[0] == 'Al']
        # hydroxyl O atoms: O bonded to Al (distance < 2.1)
        oh_oxygens = []
        for o in o_atoms:
            o_pos = o[1:]
            for al in al_atoms:
                d = distance(o_pos, al[1:])
                if d < 2.1:
                    oh_oxygens.append(o)
                    break
        # hydroxyl H atoms: H bonded to those O (distance < 1.2)
        h_atoms = [a for a in atoms if a[0] == 'H']
        oh_hydrogens = []
        for h in h_atoms:
            h_pos = h[1:]
            for o in oh_oxygens:
                if distance(h_pos, o[1:]) < 1.2:
                    oh_hydrogens.append(h)
                    break
        if not opa_oxygens or not oh_hydrogens:
            return 0.0
        # compute min O···H distance
        min_dist = 10.0
        for o in opa_oxygens:
            for h in oh_hydrogens:
                d = distance(o[1:], h[1:])
                if d < min_dist:
                    min_dist = d
        target = step.get('target_value', 2.07)
        tol = step.get('tolerance_abs', 0.1)
        diff = abs(min_dist - target)
        if diff <= tol:
            return 1.0
        # linear decay up to 2*tol
        decay = (diff - tol) / tol
        if decay >= 1.0:
            return 0.0
        return 1.0 - decay


_SCORERS = {
    'step_dft_validation': score_0,
    'step_qmmm_hbond': score_1,
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
