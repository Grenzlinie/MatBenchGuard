import os
import json
import csv

# === author imports / helpers ===
import json, os


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


# === block: score_0 (check id='step_06') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    required = [
        "pristine_strength_nanoindentation_GPa",
        "pristine_strength_tension_GPa",
        "gb_strength_nanoindentation_GPa",
        "gb_strength_tension_GPa",
        "gb_nucleation_deflection_nm",
        "gb_failure_deflection_nm"
    ]
    for k in required:
        if k not in artifact or not isinstance(artifact[k], (int, float)):
            return 0.0

    # Gold values from grading spec to stay aligned with declared reference
    gold_all = step.get("gold", {})
    gold_strengths = {
        "pristine_strength_nanoindentation_GPa": gold_all.get("pristine_strength_nanoindentation_GPa", 105.0),
        "pristine_strength_tension_GPa": gold_all.get("pristine_strength_tension_GPa", 120.0),
        "gb_strength_nanoindentation_GPa": gold_all.get("gb_strength_nanoindentation_GPa", 90.0),
        "gb_strength_tension_GPa": gold_all.get("gb_strength_tension_GPa", 70.0)
    }
    gold_deflections = {
        "gb_nucleation_deflection_nm": gold_all.get("gb_nucleation_deflection_nm", 3.54),
        "gb_failure_deflection_nm": gold_all.get("gb_failure_deflection_nm", 4.6)
    }

    tol_strength_rel = step.get("tolerances", {}).get("strength_relative", 0.10)
    tol_deflection_abs = step.get("tolerances", {}).get("deflection_abs_nm", 0.5)

    def score_strength(val, gold):
        if gold == 0:
            return 0.0
        err = abs(val - gold) / gold
        if err <= tol_strength_rel:
            return 1.0
        else:
            return max(0.0, 1.0 - (err - tol_strength_rel) / tol_strength_rel)

    def score_deflection(val, gold):
        err = abs(val - gold)
        if err <= tol_deflection_abs:
            return 1.0
        else:
            return max(0.0, 1.0 - (err - tol_deflection_abs) / tol_deflection_abs)

    scores = []
    for k in gold_strengths:
        scores.append(score_strength(artifact[k], gold_strengths[k]))
    for k in gold_deflections:
        scores.append(score_deflection(artifact[k], gold_deflections[k]))

    base = sum(scores) / len(scores)
    penalty = 0.0
    if not (artifact["gb_failure_deflection_nm"] > artifact["gb_nucleation_deflection_nm"]):
        penalty += 0.2
    if not (artifact["pristine_strength_nanoindentation_GPa"] < artifact["pristine_strength_tension_GPa"]):
        penalty += 0.2
    final = max(0.0, base - penalty)
    return min(1.0, final)


_SCORERS = {
    'step_06': score_0,
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
