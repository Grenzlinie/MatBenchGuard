import os
import json
import csv

# === author imports / helpers ===
import json

def get_nested(d, path):
    keys = path.split('.')
    for k in keys:
        d = d[k]
    return d


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


# === block: score_0 (check id='check_1wm_total_binding') ===
def score_0(artifact, step, ctx):
    val = get_nested(artifact, step['field_path'])
    target = step['target']
    if target == 0:
        return 1.0 if abs(val) <= 0.1 else 0.0
    rel_err = abs(val - target) / abs(target)
    return 1.0 if rel_err <= 0.3 else 0.0


# === block: score_1 (check id='check_1wm_avg_binding') ===
def score_1(artifact, step, ctx):
    val = get_nested(artifact, step['field_path'])
    return 1.0 if abs(val - step['target']) <= step['tolerance_abs'] else 0.0


# === block: score_2 (check id='check_1wm_o_zn_dist') ===
def score_2(artifact, step, ctx):
    val = get_nested(artifact, step['field_path'])
    return 1.0 if abs(val - step['target']) <= step['tolerance_abs'] else 0.0


# === block: score_3 (check id='check_1wm_h_o_dist') ===
def score_3(artifact, step, ctx):
    val = get_nested(artifact, step['field_path'])
    return 1.0 if abs(val - step['target']) <= step['tolerance_abs'] else 0.0


# === block: score_4 (check id='check_1wm_charge') ===
def score_4(artifact, step, ctx):
    val = get_nested(artifact, step['field_path'])
    return 1.0 if abs(val - step['target']) <= step['tolerance_abs'] else 0.0


# === block: score_5 (check id='check_4wm_avg_binding') ===
def score_5(artifact, step, ctx):
    val = get_nested(artifact, step['field_path'])
    return 1.0 if abs(val - step['target']) <= step['tolerance_abs'] else 0.0


# === block: score_6 (check id='check_4wm_total_binding') ===
def score_6(artifact, step, ctx):
    val = get_nested(artifact, step['field_path'])
    return 1.0 if abs(val - step['target']) <= step['tolerance_abs'] else 0.0


# === block: score_7 (check id='check_10wm_avg_binding') ===
def score_7(artifact, step, ctx):
    val = get_nested(artifact, step['field_path'])
    return 1.0 if abs(val - step['target']) <= step['tolerance_abs'] else 0.0


# === block: score_8 (check id='check_10wm_total_binding') ===
def score_8(artifact, step, ctx):
    val = get_nested(artifact, step['field_path'])
    return 1.0 if abs(val - step['target']) <= step['tolerance_abs'] else 0.0


# === block: score_9 (check id='check_coverage_indep') ===
def score_9(artifact, step, ctx):
    avg1 = artifact['1_WM']['avg_binding_energy_eV']
    avg4 = artifact['4_WM']['avg_binding_energy_eV']
    avg10 = artifact['10_WM']['avg_binding_energy_eV']
    max_diff = max(abs(avg1-avg4), abs(avg1-avg10), abs(avg4-avg10))
    return 1.0 if max_diff <= 0.02 else 0.0


_SCORERS = {
    'check_1wm_total_binding': score_0,
    'check_1wm_avg_binding': score_1,
    'check_1wm_o_zn_dist': score_2,
    'check_1wm_h_o_dist': score_3,
    'check_1wm_charge': score_4,
    'check_4wm_avg_binding': score_5,
    'check_4wm_total_binding': score_6,
    'check_10wm_avg_binding': score_7,
    'check_10wm_total_binding': score_8,
    'check_coverage_indep': score_9,
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
