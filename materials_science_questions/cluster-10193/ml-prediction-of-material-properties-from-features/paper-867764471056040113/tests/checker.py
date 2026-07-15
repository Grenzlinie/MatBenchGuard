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
    return spec.get('gold', {})


# === block: score_0 (check id='mae_metrics') ===
def score_0(artifact, step, ctx):
    import math

    gold = ctx
    margin = 15.0

    def mae_score(val, ref, base_ref):
        if not isinstance(val, (int, float)) or math.isnan(val):
            return 0.0
        if val <= ref + margin:
            return 1.0
        denom = base_ref - (ref + margin)
        if denom <= 0:
            return 0.0
        return max(0.0, min(1.0, (base_ref - val) / denom))

    # === T1 recompute: load raw prediction CSVs and compute MAE ===
    single_path = '/app/outputs/single_predictions.csv'
    ensemble_path = '/app/outputs/ensemble_predictions.csv'

    try:
        single_rows = load_artifact(single_path)
        ensemble_rows = load_artifact(ensemble_path)
    except Exception:
        single_rows = None
        ensemble_rows = None

    if not single_rows or not ensemble_rows:
        # Evidence files missing or empty — agent did not run the core pipeline
        return 0.0

    def compute_mae_from_rows(rows, fold_key='fold', pred_key='predicted_delta_T', true_key='true_delta_T'):
        fold_errors = {}
        all_errors = []
        for row in rows:
            try:
                pred = float(row[pred_key])
                true_val = float(row[true_key])
                fold = int(row[fold_key])
            except (KeyError, ValueError, TypeError):
                return None, None
            err = abs(pred - true_val)
            fold_errors.setdefault(fold, []).append(err)
            all_errors.append(err)
        if not all_errors:
            return {}, 0.0
        fold_mae = {f: sum(errs) / len(errs) for f, errs in sorted(fold_errors.items())}
        overall = sum(all_errors) / len(all_errors)
        return fold_mae, overall

    single_fold_map, single_overall = compute_mae_from_rows(single_rows)
    ensemble_fold_map, ensemble_overall = compute_mae_from_rows(ensemble_rows)

    if single_fold_map is None or ensemble_fold_map is None:
        return 0.0

    # Convert to ordered lists for folds 1-5
    single_fold_mae_list = [single_fold_map.get(i + 1) for i in range(5)]
    ensemble_fold_mae_list = [ensemble_fold_map.get(i + 1) for i in range(5)]

    if any(v is None for v in single_fold_mae_list) or any(v is None for v in ensemble_fold_mae_list):
        return 0.0

    # === Consistency check: JSON-reported values must match CSV-recomputed values ===
    json_single_fold = artifact.get('single_fold_mae')
    json_ensemble_fold = artifact.get('ensemble_fold_mae')
    json_single_overall = artifact.get('overall_single_mae')
    json_ensemble_overall = artifact.get('overall_ensemble_mae')

    if isinstance(json_single_fold, list) and len(json_single_fold) == 5:
        for i in range(5):
            if abs(json_single_fold[i] - single_fold_mae_list[i]) > 1.0:
                return 0.0
    else:
        return 0.0

    if isinstance(json_ensemble_fold, list) and len(json_ensemble_fold) == 5:
        for i in range(5):
            if abs(json_ensemble_fold[i] - ensemble_fold_mae_list[i]) > 1.0:
                return 0.0
    else:
        return 0.0

    if isinstance(json_single_overall, (int, float)) and isinstance(json_ensemble_overall, (int, float)):
        if abs(json_single_overall - single_overall) > 1.0:
            return 0.0
        if abs(json_ensemble_overall - ensemble_overall) > 1.0:
            return 0.0
    else:
        return 0.0

    # === Score the recomputed MAEs against paper gold ===
    scores = {}
    scores['overall_single'] = mae_score(single_overall, gold['overall_single_paper'], gold['overall_baseline'])
    scores['overall_ensemble'] = mae_score(ensemble_overall, gold['overall_ensemble_paper'], gold['overall_baseline'])

    fold_scores = [mae_score(single_fold_mae_list[i], gold['single_fold_paper'][i], gold['single_fold_baseline'][i]) for i in range(5)]
    scores['single_fold'] = sum(fold_scores) / 5.0

    fold_scores = [mae_score(ensemble_fold_mae_list[i], gold['ensemble_fold_paper'][i], gold['ensemble_fold_baseline'][i]) for i in range(5)]
    scores['ensemble_fold'] = sum(fold_scores) / 5.0

    total = (scores['overall_ensemble'] * 0.5 +
             scores['overall_single'] * 0.2 +
             scores['single_fold'] * 0.15 +
             scores['ensemble_fold'] * 0.15)
    return total


_SCORERS = {
    'mae_metrics': score_0,
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
