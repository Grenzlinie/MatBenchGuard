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


# === block: score_0 (check id='energy_components') ===
def score_0(artifact, step, ctx):
    target = step["target"]
    rel_tol = step.get("rel_tolerance", 0.02)
    if not isinstance(artifact, dict):
        return 0.0
    scores = []
    for struct in ("sc", "fcc", "bcc"):
        if struct not in artifact:
            return 0.0
        expected = target[struct]
        for field in ("E_M_alpha_rs", "E2", "E3_I_over_alpha_rs", "E3_II_over_alpha_rs", "E3_III_over_alpha_rs"):
            val = artifact[struct].get(field)
            gold = expected.get(field)
            if val is None or gold is None:
                scores.append(0.0)
                continue
            diff = abs(val - gold)
            denom = max(abs(gold), 1e-12)
            rel_err = diff / denom
            if rel_err <= rel_tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (rel_err - rel_tol) / rel_tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='elastic_constants') ===
def score_1(artifact, step, ctx):
    target = step["target"]
    rel_tol = step.get("rel_tolerance", 0.02)
    if not isinstance(artifact, dict):
        return 0.0
    scores = []
    fields = ("A_M", "A2", "A3_I", "A3_II", "A3_III", "B_M", "B2", "B3_I", "B3_II", "B3_III")
    for struct in ("sc", "fcc", "bcc"):
        if struct not in artifact:
            return 0.0
        expected = target[struct]
        for field in fields:
            val = artifact[struct].get(field)
            gold = expected.get(field)
            if val is None or gold is None:
                scores.append(0.0)
                continue
            diff = abs(val - gold)
            denom = max(abs(gold), 1e-12)
            rel_err = diff / denom
            if rel_err <= rel_tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (rel_err - rel_tol) / rel_tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='crossing_pressure') ===
def score_2(artifact, step, ctx):
    target = step["target"]["P_c_a_u"]
    abs_tol = step.get("abs_tolerance", 0.01)
    val = artifact.get("P_c_a_u")
    if val is None:
        return 0.0
    diff = abs(val - target)
    if diff <= abs_tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - abs_tol) / abs_tol)


# === block: score_3 (check id='pt_energy') ===
def score_3(artifact, step, ctx):
    threshold = step.get("threshold", -1.098)
    val = artifact.get("E_pt_Ry")
    if val is None:
        return 0.0
    if val <= threshold:
        return 1.0
    else:
        excess = val - threshold
        return max(0.0, 1.0 - excess / 0.01)


_SCORERS = {
    'energy_components': score_0,
    'elastic_constants': score_1,
    'crossing_pressure': score_2,
    'pt_energy': score_3,
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
