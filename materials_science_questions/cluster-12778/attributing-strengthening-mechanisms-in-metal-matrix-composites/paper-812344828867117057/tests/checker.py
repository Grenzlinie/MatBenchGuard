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


# === block: score_0 (check id='recompute_ratio_Al2O3') ===
def score_0(artifact, step, ctx):
    score = 0.0
    try:
        angle1 = float(artifact.get('wetting_angle_Al2O3'))
        angle2 = float(artifact.get('wetting_angle_NiAl2O3'))
        ratio1 = float(artifact.get('nucleation_work_ratio_Al2O3'))
        ratio2 = float(artifact.get('nucleation_work_ratio_NiAl2O3'))
        reduction = float(artifact.get('reduction_percent'))
    except (TypeError, ValueError):
        return 0.0

    rad1 = math.radians(angle1)
    rad2 = math.radians(angle2)
    expected_ratio1 = (2 - 3*math.cos(rad1) + math.cos(rad1)**3) / 4
    expected_ratio2 = (2 - 3*math.cos(rad2) + math.cos(rad2)**3) / 4
    if expected_ratio1 == 0:
        return 0.0
    expected_reduction = (expected_ratio1 - expected_ratio2) / expected_ratio1 * 100

    tol = step.get('tolerance', 1e-6)
    if (abs(ratio1 - expected_ratio1) <= tol and
        abs(ratio2 - expected_ratio2) <= tol and
        abs(reduction - expected_reduction) <= tol):
        score = 1.0
    return score


# === block: score_1 (check id='recompute_ratio_NiAl2O3') ===
def score_1(artifact, step, ctx):
    score = 0.0
    angle = artifact.get(step['angle_field'])
    if angle is not None:
        angle_rad = math.radians(float(angle))
        ratio = (2 - 3*math.cos(angle_rad) + math.cos(angle_rad)**3) / 4
        diff = abs(ratio - step['target'])
        score = 1.0 if diff <= step['tolerance'] else 0.0
    return score


# === block: score_2 (check id='recompute_reduction') ===
def score_2(artifact, step, ctx):
    score = 0.0
    angle1 = artifact.get('wetting_angle_Al2O3')
    angle2 = artifact.get('wetting_angle_NiAl2O3')
    if angle1 is not None and angle2 is not None:
        r1 = (2 - 3*math.cos(math.radians(float(angle1))) + math.cos(math.radians(float(angle1)))**3) / 4
        r2 = (2 - 3*math.cos(math.radians(float(angle2))) + math.cos(math.radians(float(angle2)))**3) / 4
        reduction = (r1 - r2) / r1 * 100
        diff = abs(reduction - step['target'])
        score = 1.0 if diff <= step['tolerance'] else 0.0
    return score


_SCORERS = {
    'recompute_ratio_Al2O3': score_0,
    'recompute_ratio_NiAl2O3': score_1,
    'recompute_reduction': score_2,
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
