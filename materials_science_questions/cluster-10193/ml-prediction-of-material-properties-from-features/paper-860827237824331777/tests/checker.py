import os
import json
import csv

# === author imports / helpers ===
import math, csv, json, os


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
    steps = spec.get("steps", spec.get("checks", []))
    ctx = {}
    for s in steps:
        ctx[s["id"]] = s
    return ctx


# === block: score_0 (check id='regression_rmse') ===
def score_0(artifact, step, ctx):
    target = ctx[step["id"]]["target"]
    sq_sum = 0.0
    n = 0
    for row in artifact:
        try:
            pred = float(row["predicted_Tc_mean"])
            true = float(row["measured_Tc"])
            sq_sum += (pred - true) ** 2
            n += 1
        except:
            pass
    if n == 0:
        return 0.0
    rmse = math.sqrt(sq_sum / n)
    if rmse <= target:
        return 1.0
    else:
        return max(0.0, 1.0 - (rmse - target) / target)


# === block: score_1 (check id='classification_precision') ===
def score_1(artifact, step, ctx):
    target = ctx[step["id"]]["target"]
    tp = fp = 0
    for row in artifact:
        try:
            true = int(row["true_label"])
            pred = int(row["predicted_class"])
            if true == 1 and pred == 1:
                tp += 1
            elif true == 0 and pred == 1:
                fp += 1
        except:
            pass
    if tp + fp == 0:
        return 0.0
    precision = tp / (tp + fp)
    if precision >= target:
        return 1.0
    else:
        return max(0.0, precision / target)


# === block: score_2 (check id='classification_recall') ===
def score_2(artifact, step, ctx):
    target = ctx[step["id"]]["target"]
    tp = fn = 0
    for row in artifact:
        try:
            true = int(row["true_label"])
            pred = int(row["predicted_class"])
            if true == 1 and pred == 1:
                tp += 1
            elif true == 1 and pred == 0:
                fn += 1
        except:
            pass
    if tp + fn == 0:
        return 0.0
    recall = tp / (tp + fn)
    if recall >= target:
        return 1.0
    else:
        return max(0.0, recall / target)


# === block: score_3 (check id='ima_candidates') ===
def score_3(artifact, step, ctx):
    required = ctx[step["id"]].get("required_members", [])
    name_col = ctx[step["id"]].get("name_column", "mineral_name")
    class_col = ctx[step["id"]].get("class_column", "classification")
    class_val = ctx[step["id"]].get("class_value", "SC")
    found = 0
    present_names = set()
    for row in artifact:
        name = row.get(name_col, "").strip()
        cls = row.get(class_col, "").strip()
        if cls == class_val:
            present_names.add(name)
    for member in required:
        if member in present_names:
            found += 1
    if len(required) == 0:
        return 0.0
    return found / len(required)


_SCORERS = {
    'regression_rmse': score_0,
    'classification_precision': score_1,
    'classification_recall': score_2,
    'ima_candidates': score_3,
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
