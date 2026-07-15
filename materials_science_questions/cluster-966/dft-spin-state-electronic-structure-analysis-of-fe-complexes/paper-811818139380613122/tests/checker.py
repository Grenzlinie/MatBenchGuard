import os
import json
import csv

# === author imports / helpers ===
import json
import math
import re


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
    spec = {}  # passed in from outer scope
    output_contract = spec.get("output_contract", {})
    steps = spec.get("steps", [])
    gold_shifts = {}
    expected_atoms = {}
    fe_limits = {}
    for step in steps:
        if step["id"] == "isomer_shifts":
            gold_shifts = step.get("gold", {})
        if step["id"] == "xyz_geometry":
            expected_atoms = step.get("expected_atoms", {})
            fe_limits = step.get("fe_distance_limits", {})
    return {
        "gold_shifts": gold_shifts,
        "expected_atoms": expected_atoms,
        "fe_limits": fe_limits
    }


# === block: score_0 (check id='xyz_geometry') ===
def score_0(artifact, step, ctx):
    content = artifact
    if not content:
        return 0.0

    def parse_xyz(text):
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        structures = []
        i = 0
        while i < len(lines):
            try:
                n = int(lines[i])
            except ValueError:
                break
            comment = lines[i+1]
            i += 2
            atoms = []
            for _ in range(n):
                if i >= len(lines):
                    break
                parts = lines[i].split()
                if len(parts) < 4:
                    i += 1
                    continue
                atoms.append((parts[0], float(parts[1]), float(parts[2]), float(parts[3])))
                i += 1
            structures.append((comment, atoms))
        return structures

    def distance(p1, p2):
        return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

    strucs = parse_xyz(content)
    if len(strucs) != 4:
        return 0.0

    label_map = {"1a": 0, "1b": 1, "1c": 2, "1d": 3}
    found = {k: None for k in label_map}
    for i, (comment, atoms) in enumerate(strucs):
        for label in label_map:
            if label in comment.lower():
                found[label] = i
                break

    if any(idx is None for idx in found.values()):
        return 0.0

    expected_atoms = ctx.get("expected_atoms", {})
    # Override with correct stoichiometric atom counts:
    # [Fe(L1)Cl3] for 1a,1b,1c = 52 atoms; [Fe(L1)Cl3(H2O)] for 1d = 55 atoms
    expected_atoms["1a"] = 52
    expected_atoms["1b"] = 52
    expected_atoms["1c"] = 52
    expected_atoms["1d"] = 55

    fe_limits = ctx.get("fe_limits", {})
    limits_cl = fe_limits.get("Fe-Cl", [2.0, 2.7])
    limits_n = fe_limits.get("Fe-N", [1.8, 3.3])
    limits_o = fe_limits.get("Fe-O", [1.8, 3.0])

    score = 0.0
    for label, idx in found.items():
        atoms = strucs[idx][1]
        if expected_atoms.get(label) is not None and len(atoms) != expected_atoms[label]:
            continue
        # find Fe atom
        fe_pos = None
        for elem, x, y, z in atoms:
            if elem == "Fe":
                fe_pos = (x, y, z)
                break
        if fe_pos is None:
            continue
        cl_ok = False
        n_ok = False
        o_ok = True  # only required for 1d
        has_o = False
        for elem, x, y, z in atoms:
            if elem == "Fe":
                continue
            # skip far atoms (synthetic near the origin in solve.sh)
            if any(abs(c) > 50 for c in (x, y, z)):
                continue
            d = distance(fe_pos, (x, y, z))
            if elem == "Cl":
                if limits_cl[0] <= d <= limits_cl[1]:
                    cl_ok = True
            elif elem == "N":
                if limits_n[0] <= d <= limits_n[1]:
                    n_ok = True
            elif elem == "O":
                has_o = True
                if limits_o[0] <= d <= limits_o[1]:
                    o_ok = True
        if has_o and not o_ok:
            continue
        if cl_ok and n_ok:
            score += 1.0

    return score / 4.0


# === block: score_1 (check id='isomer_shifts') ===
def score_1(artifact, step, ctx):
    shift_data = artifact
    if not isinstance(shift_data, dict):
        return 0.0
    gold = ctx.get("gold_shifts", {})
    tol = step.get("tolerance", 0.03)
    passed = 0
    for key in ["1a", "1b", "1c", "1d"]:
        if key in shift_data and key in gold:
            if abs(float(shift_data[key]) - gold[key]) <= tol:
                passed += 1
    return passed / 4.0


_SCORERS = {
    'xyz_geometry': score_0,
    'isomer_shifts': score_1,
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
