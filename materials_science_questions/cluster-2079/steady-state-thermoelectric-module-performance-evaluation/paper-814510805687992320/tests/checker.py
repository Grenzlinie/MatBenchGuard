import os
import json
import csv

# === author imports / helpers ===
import json
import csv
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
    step_corr = None
    step_pred = None
    for s in spec['steps']:
        if s['id'] == 'step_03_correlation':
            step_corr = s
        elif s['id'] == 'step_04_predictions':
            step_pred = s
    paper_coeffs = step_corr['paper_coefficients']
    paper_std_exp = step_corr['paper_standardized_exponents']
    r2_thresh = step_corr['R2_threshold']
    med_thresh = step_corr['median_error_threshold']
    tol_exp = step_corr['tolerance_rel_exponents']
    test_points = step_pred['test_points']
    max_abs_rel = step_pred['max_abs_rel_error']
    true_ccr = {tp['input_index']: tp['true_CCR'] for tp in test_points}
    return {
        'paper_coeffs': paper_coeffs,
        'paper_std_exp': paper_std_exp,
        'r2_thresh': r2_thresh,
        'med_thresh': med_thresh,
        'tol_exp': tol_exp,
        'true_ccr': true_ccr,
        'max_abs_rel': max_abs_rel
    }


# === block: score_0 (check id='step_03_correlation') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    coeffs_data = artifact.get('coefficient')
    std_exp_data = artifact.get('standardized_exponents')
    if not isinstance(coeffs_data, dict) or not isinstance(std_exp_data, dict):
        return 0.0
    paper_coeffs = ctx['paper_coeffs']
    paper_std = ctx['paper_std_exp']
    tol = ctx['tol_exp']
    items_passed = 0
    keys_coeff = ['a','b','c','d','e','f','g','h','i','j','k']
    for key in keys_coeff:
        paper_val = paper_coeffs[key]
        agent_val = coeffs_data.get(key)
        if agent_val is None:
            continue
        rel_err = abs(agent_val - paper_val) / (abs(paper_val) + 1e-9)
        if rel_err <= tol:
            items_passed += 1
    # standardized exponents
    keys_std = ['b','c','d','e','f','g','h','i','j','k']
    for key in keys_std:
        paper_val = paper_std[key]
        agent_val = std_exp_data.get(key)
        if agent_val is None:
            continue
        rel_err = abs(agent_val - paper_val) / (abs(paper_val) + 1e-9)
        if rel_err <= tol:
            items_passed += 1
    # R2
    r2_val = artifact.get('R2')
    if r2_val is not None and isinstance(r2_val, (int, float)) and r2_val >= ctx['r2_thresh']:
        items_passed += 1
    # median relative error
    med_err = artifact.get('median_relative_error')
    if med_err is not None and isinstance(med_err, (int, float)) and med_err <= ctx['med_thresh']:
        items_passed += 1
    # total: 11 coeffs + 10 std exp + 2 = 23
    total = 23.0
    return items_passed / total


# === block: score_1 (check id='step_04_predictions') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    true_ccr = ctx['true_ccr']
    max_err = ctx['max_abs_rel']
    total_score = 0.0
    count = 0
    for row in artifact:
        idx = row.get('input_index')
        if idx is None:
            continue
        try:
            idx_int = int(idx)
        except:
            continue
        pred_str = row.get('CCR_predicted')
        if pred_str is None:
            continue
        try:
            pred = float(pred_str)
        except:
            continue
        true_val = true_ccr.get(idx_int)
        if true_val is None:
            continue
        abs_rel_err = abs(pred - true_val) / (abs(true_val) + 1e-9)
        if abs_rel_err <= max_err:
            total_score += 1.0
        count += 1
    if count == 0:
        return 0.0
    return total_score / count


_SCORERS = {
    'step_03_correlation': score_0,
    'step_04_predictions': score_1,
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
