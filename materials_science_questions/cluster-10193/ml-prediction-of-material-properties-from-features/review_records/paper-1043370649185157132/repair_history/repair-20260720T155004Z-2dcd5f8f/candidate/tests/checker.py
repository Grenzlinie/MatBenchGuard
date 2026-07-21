import os
import json
import csv

# === author imports / helpers ===
import statistics


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


# === block: score_0 (check id='eval_predictions') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or not isinstance(artifact, list) or not artifact:
            return 0.0
        cols = step.get('checks', {}).get('required_columns', [])
        if not all(col in artifact[0] for col in cols):
            return 0.0
        row_min = step['checks'].get('row_count_min', 1)
        true_vals = []
        pred_vals = []
        std_vals = []
        for row in artifact:
            try:
                tv = float(row['true_oxidation_state'])
                pm = float(row['predicted_mean'])
                ps = float(row['predicted_std'])
            except (TypeError, ValueError):
                continue
            true_vals.append(tv)
            pred_vals.append(pm)
            std_vals.append(ps)
        if len(true_vals) < row_min:
            return 0.0
        lo, hi = step['checks'].get('predicted_mean_range', [0.0, 2.0])
        for v in pred_vals:
            if not (lo <= v <= hi):
                return 0.0
        if any(v < 0 for v in std_vals):
            return 0.0
        if len(true_vals) >= 2:
            if statistics.stdev(true_vals) < step['checks'].get('true_label_std_min', 0.0):
                return 0.0
        else:
            return 0.0
        return 1.0

    return score(artifact, step, ctx)


# === block: score_1 (check id='eval_metrics') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, dict):
            return 0.0
        r2 = artifact.get('R2')
        rmse = artifact.get('RMSE')
        if r2 is None or rmse is None:
            return 0.0
        target = step.get('target', {})
        tol = step.get('tolerance', {})
        target_r2 = target.get('R2', 0.85)
        target_rmse = target.get('RMSE', 0.24)
        tol_r2 = tol.get('R2', 0.025)
        tol_rmse = tol.get('RMSE', 0.02)
        # R²: higher is better, threshold = target_r2 - tol_r2
        r2_threshold = target_r2 - tol_r2  # 0.825
        if r2 >= r2_threshold:
            score_r2 = 1.0
        else:
            score_r2 = max(0.0, 1.0 - (r2_threshold - r2) / 0.2)
        # RMSE: lower is better, threshold = target_rmse + tol_rmse
        rmse_threshold = target_rmse + tol_rmse  # 0.26
        if rmse <= rmse_threshold:
            score_rmse = 1.0
        else:
            score_rmse = max(0.0, 1.0 - (rmse - rmse_threshold) / 0.2)
        return (score_r2 + score_rmse) / 2.0

    return score(artifact, step, ctx)


_SCORERS = {
    'eval_predictions': score_0,
    'eval_metrics': score_1,
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
