import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    steps = spec.get("steps", [])
    ctx = {"gold": {}, "tol": {}, "trends": {}, "snap_params": {}}
    for step in steps:
        if step["id"] == "sim_report":
            ctx["gold"] = step.get("gold", {})
            ctx["tol"] = step.get("tolerances", {})
            ctx["trends"] = step.get("trends", {})
        elif step["id"] == "snapshots":
            ctx["snap_params"] = step
    return ctx


# === block: score_0 (check id='sim_report') ===
def score_0(artifact, step, ctx):
    rows = artifact
    gold = ctx["gold"]
    tol = ctx["tol"]
    trends = ctx["trends"]
    frac_gold = gold["fraction"]
    mass_gold = gold["mass_loss"]
    tol_frac = tol["fraction"]
    tol_mass = tol["mass_loss"]
    vals = {}
    for row in rows:
        angle = int(row["angle_deg"])
        vals[angle] = {
            "frac": float(row["fraction_highly_stressed_200fs"]),
            "mass": float(row["mass_loss_percent"]),
        }
    frac_scores = []
    for a in [0,45,90]:
        if a in vals:
            diff = abs(vals[a]["frac"] - float(frac_gold[str(a)]))
            if diff <= tol_frac:
                frac_scores.append(1.0)
            elif diff <= 2*tol_frac:
                frac_scores.append(0.5)
            else:
                frac_scores.append(0.0)
        else:
            frac_scores.append(0.0)
    frac_avg = sum(frac_scores)/3.0 if frac_scores else 0.0
    mass_scores = []
    for a in [0,45,90]:
        if a in vals:
            diff = abs(vals[a]["mass"] - float(mass_gold[str(a)]))
            if diff <= tol_mass:
                mass_scores.append(1.0)
            elif diff <= 2*tol_mass:
                mass_scores.append(0.5)
            else:
                mass_scores.append(0.0)
        else:
            mass_scores.append(0.0)
    mass_avg = sum(mass_scores)/3.0 if mass_scores else 0.0
    trend_frac = 1.0 if all(a in vals for a in [0,45,90]) and vals[0]["frac"] > vals[45]["frac"] > vals[90]["frac"] else 0.0
    trend_mass = 1.0 if all(a in vals for a in [0,45,90]) and vals[90]["mass"] > vals[45]["mass"] > vals[0]["mass"] else 0.0
    score = 0.4*frac_avg + 0.4*mass_avg + 0.1*trend_frac + 0.1*trend_mass
    return min(score, 1.0)


# === block: score_1 (check id='snapshots') ===
def score_1(artifact, step, ctx):
    text = artifact.strip()
    lines = text.splitlines()
    i = 0
    frames = 0
    atom_counts_ok = True
    min_atoms = ctx["snap_params"].get("min_atom_count", 500)
    expected_frames = ctx["snap_params"].get("expected_frames", 3)
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        try:
            n_atoms = int(line)
        except:
            i += 1
            continue
        if i+1 >= len(lines):
            break
        # skip comment
        i += 2
        atom_count = 0
        while atom_count < n_atoms and i < len(lines):
            if lines[i].strip():
                atom_count += 1
            i += 1
        if n_atoms < min_atoms:
            atom_counts_ok = False
        frames += 1
    frames_ok = frames >= expected_frames
    score = 0.0
    if frames_ok:
        score += 0.5
    if atom_counts_ok and frames_ok:
        score += 0.5
    return min(score, 1.0)


_SCORERS = {
    'sim_report': score_0,
    'snapshots': score_1,
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
