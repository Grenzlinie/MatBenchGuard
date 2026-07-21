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


# === block: score_0 (check id='pt_cim_dq') ===
def score_0(artifact, step, ctx):
    # scorer body for pt_cim_dq
    model = step['gold']['model']
    field = step['gold']['field']
    gold_val = step['gold']['value']
    rel_tol = step['gold']['rel_tol']
    abs_tol = step['gold']['abs_tol']
    for entry in artifact:
        if entry.get('model') == model:
            val = entry.get(field)
            if val is None:
                return 0.0
            diff = abs(val - gold_val)
            threshold = max(rel_tol * abs(gold_val), abs_tol)
            if diff <= threshold:
                return 1.0
            else:
                # linear decay: reaches 0 when diff == 2*threshold
                return max(0.0, 1.0 - (diff - threshold) / threshold)
    return 0.0


# === block: score_1 (check id='pt_cim_np') ===
def score_1(artifact, step, ctx):
    # scorer body for pt_cim_np
    model = step['gold']['model']
    field = step['gold']['field']
    gold_val = step['gold']['value']
    rel_tol = step['gold']['rel_tol']
    abs_tol = step['gold']['abs_tol']
    for entry in artifact:
        if entry.get('model') == model:
            val = entry.get(field)
            if val is None:
                return 0.0
            diff = abs(val - gold_val)
            threshold = max(rel_tol * abs(gold_val), abs_tol)
            if diff <= threshold:
                return 1.0
            else:
                return max(0.0, 1.0 - (diff - threshold) / threshold)
    return 0.0


# === block: score_2 (check id='dv_cim_dq') ===
def score_2(artifact, step, ctx):
    # scorer body for dv_cim_dq
    model = step['gold']['model']
    field = step['gold']['field']
    gold_val = step['gold']['value']
    abs_tol = step['gold']['abs_tol']
    for entry in artifact:
        if entry.get('model') == model:
            val = entry.get(field)
            if val is None:
                return 0.0
            diff = abs(val - gold_val)
            if diff <= abs_tol:
                return 1.0
            else:
                # linear decay to 0 at 4*abs_tol
                return max(0.0, 1.0 - (diff - abs_tol) / (3 * abs_tol))
    return 0.0


# === block: score_3 (check id='dv_cim_np') ===
def score_3(artifact, step, ctx):
    # scorer body for dv_cim_np
    model = step['gold']['model']
    field = step['gold']['field']
    gold_val = step['gold']['value']
    abs_tol = step['gold']['abs_tol']
    for entry in artifact:
        if entry.get('model') == model:
            val = entry.get(field)
            if val is None:
                return 0.0
            diff = abs(val - gold_val)
            if diff <= abs_tol:
                return 1.0
            else:
                return max(0.0, 1.0 - (diff - abs_tol) / (3 * abs_tol))
    return 0.0


# === block: score_4 (check id='struct_pt_order') ===
def score_4(artifact, step, ctx):
    # scorer body for struct_pt_order
    pt_dq = None
    pt_np = None
    for entry in artifact:
        if entry.get('model') == 'CIM-DQ':
            pt_dq = entry.get('Pt_GPa')
        elif entry.get('model') == 'CIM no polarization':
            pt_np = entry.get('Pt_GPa')
    if pt_dq is None or pt_np is None:
        return 0.0
    diff = pt_dq - pt_np
    if diff >= 50:
        return 1.0
    elif diff > 0:
        return diff / 50.0
    else:
        return 0.0


# === block: score_5 (check id='struct_dv_order') ===
def score_5(artifact, step, ctx):
    # scorer body for struct_dv_order
    dv_dq = None
    dv_np = None
    for entry in artifact:
        if entry.get('model') == 'CIM-DQ':
            dv_dq = entry.get('delta_V_percent')
        elif entry.get('model') == 'CIM no polarization':
            dv_np = entry.get('delta_V_percent')
    if dv_dq is None or dv_np is None:
        return 0.0
    if abs(dv_dq) < abs(dv_np):
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'pt_cim_dq': score_0,
    'pt_cim_np': score_1,
    'dv_cim_dq': score_2,
    'dv_cim_np': score_3,
    'struct_pt_order': score_4,
    'struct_dv_order': score_5,
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
