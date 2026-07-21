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


# === block: score_0 (check id='check_surface_vs_L') ===
def score_0(artifact, step, ctx):
    rubric = step.get("rubric", {})
    data = artifact
    rows_by_L = {int(row["L"]): row for row in data}
    # mandatory crossing: E_surface must be above HH1 at L=2 and below at L=3
    if not (2 in rows_by_L and 3 in rows_by_L):
        return 0.0
    if float(rows_by_L[2]["E_surface"]) <= float(rows_by_L[2]["E_HH1"]) or float(rows_by_L[3]["E_surface"]) >= float(rows_by_L[3]["E_HH1"]):
        return 0.0
    score = 0.0
    if all(l in rows_by_L for l in [2,3,4,5,6]):
        score += rubric["rows_complete"]["weight"]
    if all(float(row["t_decay"]) < 1.0 for row in data):
        score += rubric["t_decay_less_than_one"]["weight"]
    vals = [float(rows_by_L[l]["E_surface"]) for l in [2,3,4,5,6]]
    if all(vals[i] <= vals[i-1] + 1e-3 for i in range(1, len(vals))):
        score += rubric["E_surface_non_increasing"]["weight"]
    if float(rows_by_L[2]["E_surface"]) > float(rows_by_L[2]["E_HH1"]):
        score += rubric["crossing_L2_above"]["weight"]
    if float(rows_by_L[3]["E_surface"]) < float(rows_by_L[3]["E_HH1"]):
        score += rubric["crossing_L3_below"]["weight"]
    if all(rubric["E_surface_range"]["min"] <= float(row["E_surface"]) <= rubric["E_surface_range"]["max"] for row in data):
        score += rubric["E_surface_range"]["weight"]
    if all(rubric["E_HH1_range"]["min"] <= float(row["E_HH1"]) <= rubric["E_HH1_range"]["max"] for row in data):
        score += rubric["E_HH1_range"]["weight"]
    return min(1.0, score)


# === block: score_1 (check id='check_dispersion_Q') ===
def score_1(artifact, step, ctx):
    rubric = step.get("rubric", {})
    data = artifact
    rows_by_Q = {round(float(row["Q"]), 2): row for row in data}
    expected_Q = [round(i*0.1, 1) for i in range(11)]
    score = 0.0
    if all(q in rows_by_Q for q in expected_Q):
        score += rubric["Q_complete"]["weight"]
    if all(rubric["E_surface_plausible"]["min"] <= float(row["E_surface"]) <= rubric["E_surface_plausible"]["max"] for row in data):
        score += rubric["E_surface_plausible"]["weight"]
    q0_val = float(rows_by_Q[0.0]["E_surface"])
    if rubric["Q0_range"]["min"] <= q0_val <= rubric["Q0_range"]["max"]:
        score += rubric["Q0_range"]["weight"]
    q1_val = float(rows_by_Q[1.0]["E_surface"])
    if rubric["Q1_range"]["min"] <= q1_val <= rubric["Q1_range"]["max"]:
        score += rubric["Q1_range"]["weight"]
    return min(1.0, score)


_SCORERS = {
    'check_surface_vs_L': score_0,
    'check_dispersion_Q': score_1,
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
