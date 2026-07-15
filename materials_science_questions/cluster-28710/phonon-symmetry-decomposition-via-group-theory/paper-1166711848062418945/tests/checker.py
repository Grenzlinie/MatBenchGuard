import os
import json
import csv

# === author imports / helpers ===
import json
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
    gold_exciton_irreps = {}
    for step in spec.get("steps", []):
        if step["id"] == "classify_excitons":
            gold_exciton_irreps = step.get("gold_state_labels", {})
            break
    gold_blocks = {}
    block_tolerance = 0.10
    for step in spec.get("steps", []):
        if step["id"] == "block_diag":
            gold_blocks = step.get("gold_blocks", {})
            block_tolerance = step.get("tolerance", 0.10)
            break
    gold_selection_rules = {}
    for step in spec.get("steps", []):
        if step["id"] == "selection_rules":
            gold_selection_rules = step.get("gold_rules", {})
            break
    return {
        "gold_exciton_irreps": gold_exciton_irreps,
        "gold_blocks": gold_blocks,
        "block_tolerance": block_tolerance,
        "gold_selection_rules": gold_selection_rules
    }


# === block: score_0 (check id='classify_excitons') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold_points = ctx.get("gold_exciton_irreps", {})
    if not gold_points:
        return 1.0
    point_states = {}
    for row in artifact:
        pt = row.get("symmetry_point")
        si = row.get("state_index")
        lbl = row.get("irrep_label")
        if pt is None or si is None or lbl is None:
            continue
        try:
            si = str(int(si))  # normalize to string
        except:
            continue
        point_states.setdefault(pt, {})[si] = lbl
    good = 0
    total = len(gold_points)
    for pt, expected in gold_points.items():
        states = point_states.get(pt, {})
        match = True
        for s in ["1","2","3","4","5","6","7","8"]:
            if states.get(s) != expected.get(s):
                match = False
                break
        if match:
            good += 1
    return good / total if total > 0 else 1.0


# === block: score_1 (check id='block_diag') ===
def score_1(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = ctx.get("gold_blocks", {})
    tol = ctx.get("block_tolerance", 0.10)
    if not gold:
        return 1.0
    total_irreps = 0
    matched = 0
    for point_key in gold:
        if point_key not in artifact:
            continue
        gold_point = gold[point_key]
        art_point = artifact[point_key]
        for irr, expected in gold_point.items():
            actual = art_point.get(irr)
            total_irreps += 1
            if actual is not None and isinstance(actual, (int, float)):
                if abs(actual - expected) <= tol * expected:
                    matched += 1
    if total_irreps == 0:
        return 1.0
    return matched / total_irreps


# === block: score_2 (check id='selection_rules') ===
def score_2(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold = ctx.get("gold_selection_rules", {})
    if not gold:
        return 1.0
    if json.dumps(artifact, sort_keys=True) == json.dumps(gold, sort_keys=True):
        return 1.0
    return 0.0


_SCORERS = {
    'classify_excitons': score_0,
    'block_diag': score_1,
    'selection_rules': score_2,
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
