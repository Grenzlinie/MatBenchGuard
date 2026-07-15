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
        """Extract gold and tolerances for numeric_compare steps."""
        golds = {}
        for step in spec["steps"]:
            if step["kind"] == "numeric_compare":
                golds[step["id"]] = {
                    "gold": step["gold"],
                    "tolerances": step.get("tolerances"),
                    "tolerance": step.get("tolerance")
                }
        return {"golds": golds}


# === block: score_0 (check id='magnetic_properties') ===
def score_0(artifact, step, ctx):
        step_id = step["id"]
        gold_data = ctx["golds"][step_id]["gold"]
        tolerances = ctx["golds"][step_id]["tolerances"]
        if not isinstance(artifact, dict):
            return 0.0
        fields = ["magnetic_moment_muB", "mae_meV"]
        sub = []
        for fld in fields:
            if fld not in artifact:
                sub.append(0.0)
                continue
            diff = abs(artifact[fld] - gold_data[fld])
            tol = tolerances.get(fld, 0)
            sub.append(1.0 if diff <= tol else 0.0)
        return sum(sub) / len(sub)


# === block: score_1 (check id='exchange_parameters') ===
def score_1(artifact, step, ctx):
        step_id = step["id"]
        gold_data = ctx["golds"][step_id]["gold"]
        tolerances = ctx["golds"][step_id]["tolerances"]
        if not isinstance(artifact, dict):
            return 0.0
        fields = ["J1_meV", "J2_meV", "J3_meV"]
        sub = []
        for fld in fields:
            if fld not in artifact:
                sub.append(0.0)
                continue
            diff = abs(artifact[fld] - gold_data[fld])
            tol = tolerances.get(fld, 0)
            sub.append(1.0 if diff <= tol else 0.0)
        return sum(sub) / len(sub)


# === block: score_2 (check id='curie_temperature') ===
def score_2(artifact, step, ctx):
        step_id = step["id"]
        gold_val = ctx["golds"][step_id]["gold"]
        tol = ctx["golds"][step_id]["tolerance"]
        if isinstance(artifact, str):
            try:
                val = float(artifact.strip().splitlines()[0])
            except (ValueError, IndexError):
                return 0.0
            diff = abs(val - gold_val)
            return 1.0 if diff <= tol else 0.0
        return 0.0


# === block: score_3 (check id='topological_properties') ===
def score_3(artifact, step, ctx):
        step_id = step["id"]
        gold_data = ctx["golds"][step_id]["gold"]
        tolerances = ctx["golds"][step_id]["tolerances"]
        if not isinstance(artifact, dict):
            return 0.0
        fields = ["soc_band_gap_meV", "chern_number"]
        sub = []
        for fld in fields:
            if fld not in artifact:
                sub.append(0.0)
                continue
            diff = abs(artifact[fld] - gold_data[fld])
            tol = tolerances.get(fld, 0)
            sub.append(1.0 if diff <= tol else 0.0)
        return sum(sub) / len(sub)


_SCORERS = {
    'magnetic_properties': score_0,
    'exchange_parameters': score_1,
    'curie_temperature': score_2,
    'topological_properties': score_3,
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
