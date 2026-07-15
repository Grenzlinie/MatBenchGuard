import os
import json
import csv

# === author imports / helpers ===
import math
import json
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
    return {}


# === block: score_0 (check id='step1_triplet_opt') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if artifact is None:
            return 0.0
        lines = artifact.strip().split('\n')
        # skip first line (atom count), second line (comment)
        atom_lines = [l.strip() for l in lines[2:] if l.strip()]
        if len(atom_lines) != 58:
            return 0.0
        atoms = []
        for line in atom_lines:
            parts = line.split()
            if len(parts) >= 4:
                sym = parts[0]
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                atoms.append((sym, (x, y, z)))
            else:
                return 0.0
        fe_coords = None
        for sym, coord in atoms:
            if sym == 'Fe':
                fe_coords = coord
                break
        if fe_coords is None:
            return 0.0
        o_coords = None
        for sym, coord in atoms:
            if sym == 'O':
                o_coords = coord
                break
        if o_coords is None:
            return 0.0
        min_dist = float('inf')
        n_coord = None
        for sym, coord in atoms:
            if sym == 'N':
                dx = coord[0]-o_coords[0]
                dy = coord[1]-o_coords[1]
                dz = coord[2]-o_coords[2]
                d = math.sqrt(dx*dx + dy*dy + dz*dz)
                if d < min_dist:
                    min_dist = d
                    n_coord = coord
        if n_coord is None:
            return 0.0
        v1x = fe_coords[0]-n_coord[0]
        v1y = fe_coords[1]-n_coord[1]
        v1z = fe_coords[2]-n_coord[2]
        v2x = o_coords[0]-n_coord[0]
        v2y = o_coords[1]-n_coord[1]
        v2z = o_coords[2]-n_coord[2]
        dot = v1x*v2x + v1y*v2y + v1z*v2z
        norm1 = math.sqrt(v1x*v1x + v1y*v1y + v1z*v1z)
        norm2 = math.sqrt(v2x*v2x + v2y*v2y + v2z*v2z)
        if norm1 == 0.0 or norm2 == 0.0:
            return 0.0
        cos_angle = dot / (norm1 * norm2)
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_deg = math.degrees(math.acos(cos_angle))
        lo, hi = step.get('target_angle_range', [130, 170])
        if lo <= angle_deg <= hi:
            return 1.0
        return 0.0


# === block: score_1 (check id='step2_singlet_opt') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if artifact is None:
            return 0.0
        lines = artifact.strip().split('\n')
        atom_lines = [l.strip() for l in lines[2:] if l.strip()]
        if len(atom_lines) != 58:
            return 0.0
        atoms = []
        for line in atom_lines:
            parts = line.split()
            if len(parts) >= 4:
                sym = parts[0]
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                atoms.append((sym, (x, y, z)))
            else:
                return 0.0
        fe_coords = None
        for sym, coord in atoms:
            if sym == 'Fe':
                fe_coords = coord
                break
        if fe_coords is None:
            return 0.0
        o_coords = None
        for sym, coord in atoms:
            if sym == 'O':
                o_coords = coord
                break
        if o_coords is None:
            return 0.0
        min_dist = float('inf')
        n_coord = None
        for sym, coord in atoms:
            if sym == 'N':
                dx = coord[0]-o_coords[0]
                dy = coord[1]-o_coords[1]
                dz = coord[2]-o_coords[2]
                d = math.sqrt(dx*dx + dy*dy + dz*dz)
                if d < min_dist:
                    min_dist = d
                    n_coord = coord
        if n_coord is None:
            return 0.0
        v1x = fe_coords[0]-n_coord[0]
        v1y = fe_coords[1]-n_coord[1]
        v1z = fe_coords[2]-n_coord[2]
        v2x = o_coords[0]-n_coord[0]
        v2y = o_coords[1]-n_coord[1]
        v2z = o_coords[2]-n_coord[2]
        dot = v1x*v2x + v1y*v2y + v1z*v2z
        norm1 = math.sqrt(v1x*v1x + v1y*v1y + v1z*v1z)
        norm2 = math.sqrt(v2x*v2x + v2y*v2y + v2z*v2z)
        if norm1 == 0.0 or norm2 == 0.0:
            return 0.0
        cos_angle = dot / (norm1 * norm2)
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_deg = math.degrees(math.acos(cos_angle))
        lo, hi = step.get('target_angle_range', [110, 140])
        if lo <= angle_deg <= hi:
            return 1.0
        return 0.0


# === block: score_2 (check id='step3_results') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if artifact is None:
            return 0.0
        v_no = artifact.get("v_no_triplet_cm-1")
        rel_energy = artifact.get("relative_energy_kcal_per_mol")
        if v_no is None or rel_energy is None:
            return 0.0
        target_v = step.get("target_v_no", 1643)
        tol_v = step.get("tolerance_v_no", 50)
        target_e = step.get("target_rel_energy", 11.8)
        tol_e = step.get("tolerance_rel_energy", 2.0)
        v_ok = abs(v_no - target_v) <= tol_v
        e_ok = abs(rel_energy - target_e) <= tol_e
        if v_ok and e_ok:
            return 1.0
        return 0.0


_SCORERS = {
    'step1_triplet_opt': score_0,
    'step2_singlet_opt': score_1,
    'step3_results': score_2,
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
