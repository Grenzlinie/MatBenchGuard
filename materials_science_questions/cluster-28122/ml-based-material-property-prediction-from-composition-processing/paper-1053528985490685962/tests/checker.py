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


# === block: score_0 (check id='anova_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) != 9:
        return 0.0
    gold = step['gold']
    gold_rows = gold['rows']
    tol = gold['contribution_tolerance']
    p_thresh = gold['p_value_significance_threshold']
    total = 0.0
    for gr in gold_rows:
        match = None
        for r in rows:
            if r.get('response','').strip() == gr['response'] and r.get('factor','').strip() == gr['factor']:
                match = r
                break
        if match is None:
            continue
        try:
            contrib = float(match['contribution_%'])
            pval = float(match['p_value'])
        except (ValueError, KeyError):
            continue
        contrib_score = 1.0 if abs(contrib - gr['contribution']) <= tol else 0.0
        p_score = 1.0 if (gr['p_value'] < p_thresh and pval < p_thresh) or (gr['p_value'] >= p_thresh and pval >= p_thresh) else 0.0
        total += 0.5 * contrib_score + 0.5 * p_score
    return total / len(gold_rows)


# === block: score_1 (check id='nsga2_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) != 1:
        return 0.0
    row = rows[0]
    gold = step['gold']
    tol = gold['tolerances']
    fields = ['LP_opt','SS_opt','PF_opt','P_pred','D_pred','MH_pred']
    total = 0.0
    for f in fields:
        try:
            val = float(row[f])
        except (ValueError, KeyError):
            continue
        if abs(val - gold[f]) <= tol[f]:
            total += 1.0
    return total / len(fields)


# === block: score_2 (check id='ml_metrics_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) != 9:
        return 0.0
    gold = step['gold']
    gold_rows = gold['rows']
    slack = gold['slack']
    k = gold['decay_factor']
    total = 0.0
    for gr in gold_rows:
        match = None
        for r in rows:
            if r.get('model','').strip() == gr['model'] and r.get('target','').strip() == gr['target']:
                match = r
                break
        if match is None:
            continue
        try:
            r2 = float(match['R2'])
            mae = float(match['MAE'])
            rmse = float(match['RMSE'])
        except (ValueError, KeyError):
            continue
        # R2: higher better
        if r2 >= gr['R2'] - slack['R2']:
            score_r2 = 1.0
        else:
            score_r2 = max(0.0, 1.0 - (gr['R2'] - r2 - slack['R2']) / (k * gr['R2']))
        # MAE: lower better
        if mae <= gr['MAE'] + slack['MAE']:
            score_mae = 1.0
        else:
            score_mae = max(0.0, 1.0 - (mae - gr['MAE'] - slack['MAE']) / (k * gr['MAE']))
        # RMSE: lower better
        if rmse <= gr['RMSE'] + slack['RMSE']:
            score_rmse = 1.0
        else:
            score_rmse = max(0.0, 1.0 - (rmse - gr['RMSE'] - slack['RMSE']) / (k * gr['RMSE']))
        total += (score_r2 + score_mae + score_rmse) / 3.0
    return total / len(gold_rows)


_SCORERS = {
    'anova_check': score_0,
    'nsga2_check': score_1,
    'ml_metrics_check': score_2,
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
