import os
import json
import csv

# === author imports / helpers ===
import os, json, csv


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
    gap = None
    pristine_path = os.path.join(outputs_dir, "pristine_cbm.json")
    if os.path.exists(pristine_path):
        with open(pristine_path) as f:
            data = json.load(f)
            if "cb_minus_vbm" in data:
                gap = float(data["cb_minus_vbm"])

    ef_data = []
    ef_path = os.path.join(outputs_dir, "ef_vs_vbm_table.csv")
    if os.path.exists(ef_path):
        with open(ef_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ef_data.append(row)

    return {"cb_minus_vbm": gap, "ef_data": ef_data}


# === block: score_0 (check id='pristine_gap_sanity') ===
def score_0(artifact, step, ctx):
    cb = artifact.get("cb_minus_vbm")
    if not isinstance(cb, (int, float)):
        return 0.0
    if not (step.get("min_val", 1.3) <= cb <= step.get("max_val", 2.1)):
        return 0.0
    ef = ctx.get("ef_data")
    if not ef or len(ef) < 12:
        return 0.0
    return 1.0


# === block: score_1 (check id='s5_7_2na_above_cbm') ===
def score_1(artifact, step, ctx):
    cb = ctx.get("cb_minus_vbm")
    if cb is None:
        return 0.0
    tol = step.get("tolerance_eV", 0.0)
    target_defect = step["target_defect"]
    target_na = int(step["target_na_count"])
    for row in artifact:
        if row.get("defect_type") == target_defect and int(row.get("Na_count")) == target_na:
            ef_val = float(row.get("EF_minus_VBM"))
            if ef_val >= cb - tol:
                return 1.0
            else:
                return 0.0
    return 0.0


# === block: score_2 (check id='others_below_cbm') ===
def score_2(artifact, step, ctx):
    cb = ctx.get("cb_minus_vbm")
    if cb is None:
        return 0.0
    tol = step.get("tolerance_eV", 0.0)
    target_defect = step.get("exclude_defect", "S5|7")
    target_na = step.get("exclude_na_count", 2)
    for row in artifact:
        if row.get("defect_type") == target_defect and int(row.get("Na_count")) == target_na:
            continue
        ef_val = float(row.get("EF_minus_VBM"))
        if not (ef_val < cb + tol):
            return 0.0
    return 1.0


# === block: score_3 (check id='ef_monotonicity') ===
def score_3(artifact, step, ctx):
    groups = {}
    for row in artifact:
        d = row.get("defect_type")
        if d is None:
            continue
        groups.setdefault(d, []).append((int(row.get("Na_count")), float(row.get("EF_minus_VBM"))))
    tol = step.get("tolerance_eV", 0.0)
    for d, points in groups.items():
        points.sort(key=lambda x: x[0])
        for i in range(len(points)-1):
            if points[i+1][1] < points[i][1] - tol:
                return 0.0
    return 1.0


_SCORERS = {
    'pristine_gap_sanity': score_0,
    's5_7_2na_above_cbm': score_1,
    'others_below_cbm': score_2,
    'ef_monotonicity': score_3,
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
