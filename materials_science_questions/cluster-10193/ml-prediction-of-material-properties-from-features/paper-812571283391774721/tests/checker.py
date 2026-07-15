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
    ctx = {}
    for step in spec.get('steps', []):
        ctx[step['id']] = step.get('params', {})
    return ctx


# === block: score_0 (check id='model_eval') ===
def score_0(artifact, step, ctx):
    r2 = float(artifact.get('r_squared', 0))
    mae = float(artifact.get('mae', 0))
    rmse = float(artifact.get('rmse', 0))
    params = step.get('params', {})
    r2_thresh = params.get('threshold_r2', 0.9)
    mae_ok = params.get('mae_max', 0.3)
    rmse_ok = params.get('rmse_max', 0.4)

    # R²: higher is better, full credit if >= threshold
    r2_score = 1.0 if r2 >= r2_thresh else max(0.0, r2 / r2_thresh)

    # MAE: lower is better
    if mae <= mae_ok:
        mae_score = 1.0
    else:
        mae_score = max(0.0, 1.0 - (mae - mae_ok) / (2 * mae_ok))

    # RMSE: lower is better
    if rmse <= rmse_ok:
        rmse_score = 1.0
    else:
        rmse_score = max(0.0, 1.0 - (rmse - rmse_ok) / (2 * rmse_ok))

    # Combine: R² carries most weight, MAE/RMSE are secondary consistency
    return 0.7 * r2_score + 0.15 * mae_score + 0.15 * rmse_score


# === block: score_1 (check id='feature_importances') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    targets = params.get('target_features', [])
    top_name = params.get('top_feature_name', '')

    feat_map = {}
    for row in artifact:
        name = row.get('feature_name', '')
        imp = float(row.get('importance_percent', 0))
        feat_map[name] = imp

    # Per-target score
    scores = []
    for t in targets:
        name = t['name']
        imp = t.get('importance', 0)
        tol = t.get('tolerance', 3.0)
        match_type = t.get('match_type', 'exact')
        if name in feat_map:
            val = feat_map[name]
            if match_type == 'exact':
                err = abs(val - imp)
                if err <= tol:
                    scores.append(1.0)
                else:
                    # partial credit outside tolerance
                    scores.append(max(0.0, 1.0 - err / (tol * 3.0)))
            else:
                # presence: must have importance > 0
                scores.append(1.0 if val > 0 else 0.0)
        else:
            scores.append(0.0)

    # Average target score
    if scores:
        avg_target = sum(scores) / len(scores)
    else:
        avg_target = 0.0

    # Top-feature ordering check
    if artifact:
        top_in_csv = artifact[0].get('feature_name', '')
        order_score = 1.0 if top_in_csv == top_name else 0.0
    else:
        order_score = 0.0

    return 0.8 * avg_target + 0.2 * order_score


_SCORERS = {
    'model_eval': score_0,
    'feature_importances': score_1,
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
