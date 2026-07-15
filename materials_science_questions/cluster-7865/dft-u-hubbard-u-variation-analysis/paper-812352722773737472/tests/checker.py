import os
import json
import csv


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


# === block: score_0 (check id='check_relax') ===
def score_0(artifact, step, ctx):
    u = artifact.get('u')
    v = artifact.get('v')
    if u is None or v is None:
        return 0.0
    tol = step['tolerance']
    gold_u = step['gold_u']
    gold_v = step['gold_v']
    score_u = 1.0 if abs(u - gold_u) <= tol else 0.0
    score_v = 1.0 if abs(v - gold_v) <= tol else 0.0
    return (score_u + score_v) / 2.0


# === block: score_1 (check id='check_charges') ===
def score_1(artifact, step, ctx):
    gold = step['gold_dict']
    rel_tol = step['relative_tolerance']
    min_abs = step.get('min_absolute_tolerance', 0.01)
    atoms = ['Hf1', 'Hf2', 'Co']
    orbitals = ['s', 'p', 'd', 'f']
    total_score = 0.0
    count = 0
    for atom in atoms:
        atom_data = artifact.get(atom, {})
        for orb in orbitals:
            val = atom_data.get(orb)
            if val is None:
                continue
            gold_val = gold[atom][orb]
            delta = abs(val - gold_val)
            threshold = max(rel_tol * abs(gold_val), min_abs)
            total_score += 1.0 if delta <= threshold else 0.0
            count += 1
    if count == 0:
        return 0.0
    return total_score / count


# === block: score_2 (check id='check_efg') ===
def score_2(artifact, step, ctx):
    c16 = artifact.get('16c', {})
    f48 = artifact.get('48f', {})
    if not isinstance(c16, dict) or not isinstance(f48, dict):
        return 0.0
    v16 = c16.get('V_ZZ')
    v48 = f48.get('V_ZZ')
    eta16 = c16.get('eta')
    eta48 = f48.get('eta')
    if None in (v16, v48, eta16, eta48):
        return 0.0
    gold = step['gold_efg']
    rel_tol_v = step['relative_tolerance_V']
    abs_tol_eta = step['absolute_tolerance_eta']
    # V_ZZ 16c
    gv16 = gold['16c']['V_ZZ']
    sign_match = (v16 * gv16) >= 0
    if not sign_match:
        score_v16 = 0.0
    else:
        delta = abs(v16 - gv16)
        score_v16 = 1.0 if delta <= rel_tol_v * abs(gv16) else 0.0
    # V_ZZ 48f
    gv48 = gold['48f']['V_ZZ']
    sign_match = (v48 * gv48) >= 0
    if not sign_match:
        score_v48 = 0.0
    else:
        delta = abs(v48 - gv48)
        score_v48 = 1.0 if delta <= rel_tol_v * abs(gv48) else 0.0
    # eta 16c
    score_eta16 = 1.0 if abs(eta16 - gold['16c']['eta']) <= abs_tol_eta else 0.0
    # eta 48f
    score_eta48 = 1.0 if abs(eta48 - gold['48f']['eta']) <= abs_tol_eta else 0.0
    # structural check: V_ZZ magnitude at 48f >= 10 * |V_ZZ| at 16c
    if abs(v48) >= 10 * abs(v16):
        score_struct = 1.0
    else:
        score_struct = 0.0
    w_v16 = 0.25
    w_v48 = 0.25
    w_eta16 = 0.15
    w_eta48 = 0.15
    w_struct = 0.2
    return w_v16*score_v16 + w_v48*score_v48 + w_eta16*score_eta16 + w_eta48*score_eta48 + w_struct*score_struct


_SCORERS = {
    'check_relax': score_0,
    'check_charges': score_1,
    'check_efg': score_2,
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
