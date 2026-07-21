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
    ctx = {}
    steps = spec.get('steps', [])
    for s in steps:
        if s['id'] == 'evaluate_hppp':
            params = s.get('params', {})
            ctx['gold'] = params.get('gold', {})
            ctx['tolerances'] = params.get('tolerances', {})
            break
    return ctx


# === block: score_0 (check id='hyperparam_opt') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    required = ['r_cut', 'gamma', 'beta1', 'beta2', 'alpha']
    for k in required:
        if k not in artifact:
            return 0.0
        val = artifact[k]
        if not isinstance(val, (int, float)):
            return 0.0
    return 1.0


# === block: score_1 (check id='evaluate_hppp') ===
def score_1(artifact, step, ctx):
    gold = ctx.get('gold', {})
    tolerances = ctx.get('tolerances', {})
    if not isinstance(artifact, dict):
        return 0.0
    expected_keys = {'100','300','500','1000'}
    if not all(k in artifact for k in expected_keys):
        return 0.0
    agent = {}
    for size in ['100','300','500','1000']:
        d = artifact.get(size, {})
        if not isinstance(d, dict):
            return 0.0
        mae = d.get('MAE')
        rmse = d.get('RMSE')
        if not isinstance(mae, (int,float)) or not isinstance(rmse, (int,float)):
            return 0.0
        agent[size] = {'MAE': float(mae), 'RMSE': float(rmse)}

    def score_metric(size, metric, agent_val):
        ref = gold.get(size, {}).get(metric)
        if ref is None:
            return 0.0
        if size == '1000':
            if metric == 'MAE':
                abs_tol = tolerances.get('MAE_1000_abs', 0.6)
            else:
                abs_tol = tolerances.get('RMSE_1000_abs', 1.0)
            threshold = ref + abs_tol
        else:
            rel_tol = tolerances.get('rel_tol', 0.3)
            threshold = ref * (1 + rel_tol)
        if agent_val <= threshold:
            return 1.0
        else:
            if threshold == 0:
                return 0.0
            score = max(0.0, 1.0 - (agent_val - threshold) / threshold)
            return score

    acc_sum = 0.0
    count = 0
    for size in ['100','300','500','1000']:
        for metric in ['MAE','RMSE']:
            s = score_metric(size, metric, agent[size][metric])
            acc_sum += s
            count += 1
    acc_score = acc_sum / count if count else 0.0

    maes = [agent[str(s)]['MAE'] for s in [100,300,500,1000]]
    rmses = [agent[str(s)]['RMSE'] for s in [100,300,500,1000]]
    trend_mae = 1 if (maes[0] > maes[1] > maes[2] > maes[3]) else 0
    trend_rmse = 1 if (rmses[0] > rmses[1] > rmses[2] > rmses[3]) else 0
    trend_score = (trend_mae + trend_rmse) / 2.0

    overall = 0.7 * acc_score + 0.3 * trend_score
    return overall


_SCORERS = {
    'hyperparam_opt': score_0,
    'evaluate_hppp': score_1,
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
