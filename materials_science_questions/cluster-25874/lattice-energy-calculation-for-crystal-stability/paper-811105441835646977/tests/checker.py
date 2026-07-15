import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import os

def compute_mape(rows, exp_col='experimental_Tm', pred_col='predicted_Tm'):
    errors = []
    for r in rows:
        exp = float(r[exp_col])
        pred = float(r[pred_col])
        if exp == 0:
            continue
        errors.append(abs(pred - exp) / exp * 100.0)
    if not errors:
        return None
    return sum(errors) / len(errors)

def mape_score(mape, target, tol_abs, decay_abs_range):
    # monotonic: lower mape -> higher score
    if mape is None:
        return 0.0
    max_acceptable = target + tol_abs
    if mape <= max_acceptable:
        return 1.0
    # linear decay from max_acceptable to max_acceptable + decay_abs_range
    if decay_abs_range <= 0:
        return 0.0
    return max(0.0, 1.0 - (mape - max_acceptable) / decay_abs_range)


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
    return {
        'expected_validation_names': [
            'THP:SAC',
            'CAF:4F3NAN',
            'INA:ADA',
            'INA:4HBA',
            'INA:GTA',
            'NA:GTA'
        ]
    }


# === block: score_0 (check id='check_split_integrity') ===
def score_0(artifact, step, ctx):
    rows = artifact  # artifact is a list of dicts from csv
    if rows is None or not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    expected = set(ctx['expected_validation_names'])
    validation_rows = [r for r in rows if str(r.get('split', '')).strip().lower() == 'validation']
    training_rows = [r for r in rows if str(r.get('split', '')).strip().lower() == 'training']
    actual_val_names = set(r.get('cocrystal_name', '').strip() for r in validation_rows)
    if actual_val_names != expected:
        return 0.0
    if len(validation_rows) != 6:
        return 0.0
    if len(training_rows) != 55:
        return 0.0
    # check no overlap and all rows accounted for
    if (len(validation_rows) + len(training_rows)) != len(rows):
        return 0.0
    return 1.0


# === block: score_1 (check id='check_train_mape') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if rows is None:
        return 0.0
    split = step.get('split_filter', 'training')
    filtered = [r for r in rows if str(r.get('split', '')).strip().lower() == split]
    mape = compute_mape(filtered)
    return mape_score(mape, step['target_value'], step['tolerance_abs'], step['decay_abs_range'])


# === block: score_2 (check id='check_val_mape') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if rows is None:
        return 0.0
    split = step.get('split_filter', 'validation')
    filtered = [r for r in rows if str(r.get('split', '')).strip().lower() == split]
    mape = compute_mape(filtered)
    return mape_score(mape, step['target_value'], step['tolerance_abs'], step['decay_abs_range'])


_SCORERS = {
    'check_split_integrity': score_0,
    'check_train_mape': score_1,
    'check_val_mape': score_2,
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
