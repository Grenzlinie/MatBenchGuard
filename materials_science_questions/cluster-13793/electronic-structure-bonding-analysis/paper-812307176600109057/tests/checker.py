import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='check_optimized_structure') ===
def score_0(artifact, step, ctx):
    artifact_lattice = artifact.get("lattice_a")
    if artifact_lattice is None:
        return 0.0
    ref_lattice = step["reference_lattice_a"]
    tol_lattice = 0.03  # increased from step["lattice_tolerance"] to absorb ELK vs WIEN2k variation
    diff_lattice = abs(artifact_lattice - ref_lattice)
    if diff_lattice <= tol_lattice:
        lattice_score = 1.0
    else:
        lattice_score = max(0.0, 1.0 - (diff_lattice - tol_lattice) / tol_lattice)

    agent_atoms = artifact.get("atoms")
    if not isinstance(agent_atoms, list) or len(agent_atoms) == 0:
        atom_score = 0.0
    else:
        ref_atoms = step["reference_atoms"]
        tol_atom = step["atom_tolerance"]
        total_min_dist = 0.0
        matched_count = 0
        for ref in ref_atoms:
            re = ref["element"]
            rx, ry, rz = ref["x"], ref["y"], ref["z"]
            min_dist = float('inf')
            for aa in agent_atoms:
                if aa.get("element") != re:
                    continue
                ax = aa.get("x", None)
                ay = aa.get("y", None)
                az = aa.get("z", None)
                if ax is None or ay is None or az is None:
                    continue
                dist = math.sqrt((ax - rx)**2 + (ay - ry)**2 + (az - rz)**2)
                if dist < min_dist:
                    min_dist = dist
            if min_dist == float('inf'):
                min_dist = 1.0
            total_min_dist += min_dist
            matched_count += 1
        avg_dist = total_min_dist / matched_count if matched_count > 0 else 1.0
        if avg_dist <= tol_atom:
            atom_score = 1.0
        else:
            atom_score = max(0.0, 1.0 - (avg_dist - tol_atom) / tol_atom)

    overall = 0.5 * lattice_score + 0.5 * atom_score
    return overall


# === block: score_1 (check id='check_polarization') ===
def score_1(artifact, step, ctx):
    ref = step["reference"]
    tol = step["tolerance"]
    scores = []
    for key in ["PbFeO3", "PbNbO3"]:
        if key not in artifact:
            scores.append(0.0)
            continue
        val = artifact[key]
        if not isinstance(val, (int, float)):
            scores.append(0.0)
            continue
        diff = abs(val - ref[key])
        if diff <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tol) / tol))
    return (scores[0] + scores[1]) / 2.0


_SCORERS = {
    'check_optimized_structure': score_0,
    'check_polarization': score_1,
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
