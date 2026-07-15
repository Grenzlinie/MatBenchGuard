import os
import json
import csv

# === author imports / helpers ===
import os
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
    def prepare(outputs_dir, spec):
        pred_path = os.path.join(outputs_dir, 'step_01_predictions.csv')
        if not os.path.exists(pred_path):
            return {'r2_computed': None, 'mae_computed': None}
        with open(pred_path, newline='') as f:
            reader = csv.DictReader(f)
            exp = []
            pred = []
            for row in reader:
                exp.append(float(row['experimental_t50']))
                pred.append(float(row['predicted_t50']))
        n = len(exp)
        if n == 0:
            return {'r2_computed': None, 'mae_computed': None}
        mean_exp = sum(exp) / n
        ss_res = sum((e - p) ** 2 for e, p in zip(exp, pred))
        ss_tot = sum((e - mean_exp) ** 2 for e in exp)
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
        mae = sum(abs(e - p) for e, p in zip(exp, pred)) / n
        return {'r2_computed': r2, 'mae_computed': mae}


# === block: score_0 (check id='step_01_predictions') ===
def score_0(artifact, step, ctx):
    if artifact is None or not artifact:
        return 0.0
    # Agent rows from step_01_predictions.csv: each dict has 'experimental_t50' and 'predicted_t50'
    try:
        exp = [float(row['experimental_t50']) for row in artifact]
        pred = [float(row['predicted_t50']) for row in artifact]
    except (KeyError, ValueError):
        return 0.0
    n = len(exp)
    if n == 0:
        return 0.0
    mean_exp = sum(exp) / n
    ss_res = sum((e - p) ** 2 for e, p in zip(exp, pred))
    ss_tot = sum((e - mean_exp) ** 2 for e in exp)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    mae = sum(abs(e - p) for e, p in zip(exp, pred)) / n

    r2_thresh = float(step.get('r2_threshold', 0.68))
    mae_thresh = float(step.get('mae_threshold', 35.0))
    # r2 score: higher is better, full credit if r2 >= threshold
    if r2 >= r2_thresh:
        r2_score = 1.0
    else:
        r2_score = max(0.0, r2 / r2_thresh)
    # mae score: lower is better, full credit if mae <= threshold
    if mae <= mae_thresh:
        mae_score = 1.0
    else:
        decay = (mae - mae_thresh) / (200.0 - mae_thresh)
        mae_score = max(0.0, 1.0 - decay)
    return (r2_score + mae_score) / 2.0


# === block: score_1 (check id='step_02_metrics') ===
def score_1(artifact, step, ctx):
    def score_metrics(artifact, step, ctx):
        if artifact is None or not isinstance(artifact, dict):
            return 0.0
        r2_exp = ctx.get('r2_computed', None)
        mae_exp = ctx.get('mae_computed', None)
        if r2_exp is None or mae_exp is None:
            return 0.0
        r2_agent = artifact.get('r2')
        mae_agent = artifact.get('mae')
        if r2_agent is None or mae_agent is None:
            return 0.0
        r2_tol = float(step.get('r2_tol', 0.05))
        mae_tol = float(step.get('mae_tol', 5.0))
        if abs(float(r2_agent) - r2_exp) <= r2_tol and abs(float(mae_agent) - mae_exp) <= mae_tol:
            return 1.0
        else:
            return 0.0


_SCORERS = {
    'step_01_predictions': score_0,
    'step_02_metrics': score_1,
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
