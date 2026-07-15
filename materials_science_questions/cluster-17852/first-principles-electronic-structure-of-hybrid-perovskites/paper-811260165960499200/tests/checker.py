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


# === block: score_0 (check id='pol_electron_values') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerance_abs']
    orientations = ['100', '110', '111']
    passed = 0
    try:
        for o in orientations:
            if o not in artifact or 'electron' not in artifact[o]:
                continue
            if abs(artifact[o]['electron'] - gold[o]) <= tol:
                passed += 1
    except Exception:
        return 0.0
    return passed / len(orientations)


# === block: score_1 (check id='pol_hole_values') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerance_abs']
    orientations = ['100', '110', '111']
    passed = 0
    try:
        for o in orientations:
            if o not in artifact or 'hole' not in artifact[o]:
                continue
            if abs(artifact[o]['hole'] - gold[o]) <= tol:
                passed += 1
    except Exception:
        return 0.0
    return passed / len(orientations)


# === block: score_2 (check id='pol_ordering') ===
def score_2(artifact, step, ctx):
    try:
        e100 = artifact['100']['electron']
        e110 = artifact['110']['electron']
        e111 = artifact['111']['electron']
        h100 = artifact['100']['hole']
        h110 = artifact['110']['hole']
        h111 = artifact['111']['hole']
        elec_ok = e110 > e111 > e100
        hole_ok = h110 > h111 > h100
        score = 0.0
        if elec_ok:
            score += 0.5
        if hole_ok:
            score += 0.5
        return score
    except Exception:
        return 0.0


# === block: score_3 (check id='dielectric_values') ===
def score_3(artifact, step, ctx):
    gold = step['gold']
    tol_rel = step['tolerance_rel']
    orientations = ['100', '110', '111']
    passed = 0
    try:
        for o in orientations:
            if o not in artifact or 'avg_diagonal' not in artifact[o]:
                continue
            agent_val = artifact[o]['avg_diagonal']
            gold_val = gold[o]
            if gold_val == 0:
                if abs(agent_val) <= tol_rel:
                    passed += 1
            else:
                if abs(agent_val - gold_val) / abs(gold_val) <= tol_rel:
                    passed += 1
    except Exception:
        return 0.0
    return passed / len(orientations)


# === block: score_4 (check id='rotor_values') ===
def score_4(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerance_abs']
    keys = ['CH3ND3', 'CD3NH3', 'CD3ND3']
    passed = 0
    try:
        for k in keys:
            if k not in artifact:
                continue
            if abs(artifact[k] - gold[k]) <= tol:
                passed += 1
    except Exception:
        return 0.0
    return passed / len(keys)


_SCORERS = {
    'pol_electron_values': score_0,
    'pol_hole_values': score_1,
    'pol_ordering': score_2,
    'dielectric_values': score_3,
    'rotor_values': score_4,
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
