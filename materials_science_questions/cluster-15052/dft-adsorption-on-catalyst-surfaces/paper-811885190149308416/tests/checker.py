import os
import json
import csv

# === author imports / helpers ===
import os, json, math, io

def check_numeric(value, target, tol):
    if value is None:
        return 0.0
    return 1.0 if abs(value - target) <= tol else 0.0

def extract_json_value(data, path):
    if data is None:
        return None
    parts = path.split('.')
    val = data
    for p in parts:
        if not isinstance(val, dict) or p not in val:
            return None
        val = val[p]
    return val

def parse_xyz(text):
    lines = text.strip().splitlines()
    if not lines:
        return None
    try:
        n_atoms = int(lines[0].strip())
    except:
        return None
    if n_atoms < 1:
        return None
    atoms = []
    for line in lines[2:2+n_atoms]:
        parts = line.strip().split()
        if len(parts) < 4:
            return None
        sym, x, y, z = parts[0], float(parts[1]), float(parts[2]), float(parts[3])
        atoms.append((sym, (x, y, z)))
    return n_atoms, atoms


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
    ads_path = os.path.join(outputs_dir, "adsorption_results.json")
    ads_data = None
    if os.path.exists(ads_path):
        with open(ads_path) as f:
            ads_data = json.load(f)
    return {"adsorption_data": ads_data}


# === block: score_0 (check id='check_redox_eads') ===
def score_0(artifact, step, ctx):
    val = extract_json_value(ctx.get("adsorption_data"), step["field_path"])
    return check_numeric(val, step["target"], step["tolerance_abs"])


# === block: score_1 (check id='check_redox_co_bond') ===
def score_1(artifact, step, ctx):
    val = extract_json_value(ctx.get("adsorption_data"), step["field_path"])
    return check_numeric(val, step["target"], step["tolerance_abs"])


# === block: score_2 (check id='check_redox_bader_before') ===
def score_2(artifact, step, ctx):
    val = extract_json_value(ctx.get("adsorption_data"), step["field_path"])
    return check_numeric(val, step["target"], step["tolerance_abs"])


# === block: score_3 (check id='check_redox_bader_after') ===
def score_3(artifact, step, ctx):
    val = extract_json_value(ctx.get("adsorption_data"), step["field_path"])
    return check_numeric(val, step["target"], step["tolerance_abs"])


# === block: score_4 (check id='check_bulk_eads') ===
def score_4(artifact, step, ctx):
    val = extract_json_value(ctx.get("adsorption_data"), step["field_path"])
    return check_numeric(val, step["target"], step["tolerance_abs"])


# === block: score_5 (check id='check_bulk_co_bond') ===
def score_5(artifact, step, ctx):
    val = extract_json_value(ctx.get("adsorption_data"), step["field_path"])
    return check_numeric(val, step["target"], step["tolerance_abs"])


# === block: score_6 (check id='check_bulk_bader_before') ===
def score_6(artifact, step, ctx):
    val = extract_json_value(ctx.get("adsorption_data"), step["field_path"])
    return check_numeric(val, step["target"], step["tolerance_abs"])


# === block: score_7 (check id='check_bulk_bader_after') ===
def score_7(artifact, step, ctx):
    val = extract_json_value(ctx.get("adsorption_data"), step["field_path"])
    return check_numeric(val, step["target"], step["tolerance_abs"])


# === block: score_8 (check id='check_gas_co_bond') ===
def score_8(artifact, step, ctx):
    val = extract_json_value(ctx.get("adsorption_data"), step["field_path"])
    return check_numeric(val, step["target"], step["tolerance_abs"])


# === block: score_9 (check id='check_xyz_redox') ===
def score_9(artifact, step, ctx):
    parsed = parse_xyz(artifact)
    if parsed is None:
        return 0.0
    n_atoms, atoms_list = parsed
    if n_atoms < step.get("min_atoms", 1):
        return 0.0
    ads = ctx.get("adsorption_data")
    expected = extract_json_value(ads, step["json_path"])
    if expected is None:
        return 0.0
    c_pos = None
    o_positions = []
    for sym, pos in atoms_list:
        if sym == 'C':
            if c_pos is not None:
                return 0.0
            c_pos = pos
        elif sym == 'O':
            o_positions.append(pos)
    if c_pos is None or not o_positions:
        return 0.0
    min_dist = min(math.sqrt((c_pos[0]-p[0])**2 + (c_pos[1]-p[1])**2 + (c_pos[2]-p[2])**2) for p in o_positions)
    tol = step.get("tolerance_abs", 0.01)
    return 1.0 if abs(min_dist - expected) <= tol else 0.0


# === block: score_10 (check id='check_xyz_bulk') ===
def score_10(artifact, step, ctx):
    parsed = parse_xyz(artifact)
    if parsed is None:
        return 0.0
    n_atoms, atoms_list = parsed
    if n_atoms < step.get("min_atoms", 1):
        return 0.0
    ads = ctx.get("adsorption_data")
    expected = extract_json_value(ads, step["json_path"])
    if expected is None:
        return 0.0
    c_pos = None
    o_positions = []
    for sym, pos in atoms_list:
        if sym == 'C':
            if c_pos is not None:
                return 0.0
            c_pos = pos
        elif sym == 'O':
            o_positions.append(pos)
    if c_pos is None or not o_positions:
        return 0.0
    min_dist = min(math.sqrt((c_pos[0]-p[0])**2 + (c_pos[1]-p[1])**2 + (c_pos[2]-p[2])**2) for p in o_positions)
    tol = step.get("tolerance_abs", 0.01)
    return 1.0 if abs(min_dist - expected) <= tol else 0.0


_SCORERS = {
    'check_redox_eads': score_0,
    'check_redox_co_bond': score_1,
    'check_redox_bader_before': score_2,
    'check_redox_bader_after': score_3,
    'check_bulk_eads': score_4,
    'check_bulk_co_bond': score_5,
    'check_bulk_bader_before': score_6,
    'check_bulk_bader_after': score_7,
    'check_gas_co_bond': score_8,
    'check_xyz_redox': score_9,
    'check_xyz_bulk': score_10,
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
