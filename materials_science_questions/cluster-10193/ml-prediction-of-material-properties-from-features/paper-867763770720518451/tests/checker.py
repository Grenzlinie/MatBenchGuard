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
    def prepare(grading_spec):
        spec = grading_spec
        step01 = [s for s in spec['steps'] if s['id'] == 'step_01_regression_coefficients'][0]
        step02 = [s for s in spec['steps'] if s['id'] == 'step_02_sisso_results'][0]
        return {
            'step01_gold': step01['gold'],
            'step01_tol': step01['tolerances'],
            'step02_gold': step02['gold'],
            'step02_tol': step02['tolerances']
        }


# === block: score_0 (check id='step_01_regression_coefficients') ===
def score_0(artifact, step, ctx):
    gold = ctx['step01_gold']
    tol = ctx['step01_tol']

    def coeff_score(val, gold_val, abs_tol):
        diff = abs(val - gold_val)
        if diff <= abs_tol:
            return 1.0
        return max(0.0, 1.0 - (diff - abs_tol) / 0.04)  # reaches 0 at diff=abs_tol+0.04

    coeff_vals = [('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')]
    coeff_scores = []
    for key, gold_key in coeff_vals:
        if key not in artifact:
            coeff_scores.append(0.0)
        else:
            coeff_scores.append(coeff_score(artifact[key], gold[gold_key], tol['coeff_abs']))
    coeff_part = sum(coeff_scores) / len(coeff_scores)

    # Metrics: directional
    mae = artifact.get('MAE')
    rmse = artifact.get('RMSE')
    r2 = artifact.get('R2')

    def mae_score(val, gold_val, abs_tol):
        if val <= gold_val + abs_tol:
            return 1.0
        return max(0.0, 1.0 - (val - (gold_val + abs_tol)) / 0.05)

    def rmse_score(val, gold_val, abs_tol):
        if val <= gold_val + abs_tol:
            return 1.0
        return max(0.0, 1.0 - (val - (gold_val + abs_tol)) / 0.05)

    def r2_score(val, gold_val, abs_tol):
        target = gold_val - abs_tol
        if val >= target:
            return 1.0
        return max(0.0, 1.0 - (target - val) / 0.05)

    metrics_scores = []
    if mae is not None:
        metrics_scores.append(mae_score(mae, gold['MAE'], tol['mae_abs']))
    if rmse is not None:
        metrics_scores.append(rmse_score(rmse, gold['RMSE'], tol['rmse_abs']))
    if r2 is not None:
        metrics_scores.append(r2_score(r2, gold['R2'], tol['r2_abs']))
    metric_part = sum(metrics_scores) / max(1, len(metrics_scores))

    return 0.5 * coeff_part + 0.5 * metric_part


# === block: score_1 (check id='step_02_sisso_results') ===
def score_1(artifact, step, ctx):
    gold = ctx['step02_gold']
    tol = ctx['step02_tol']

    # Map descriptor names to coefficients
    pairs = []
    for i in range(1, 4):
        d = artifact.get(f'descriptor_{i}')
        c = artifact.get(f'coeff_{i}')
        if d is not None and c is not None:
            pairs.append((str(d).strip(), float(c)))

    # Expected mapping
    expected = {
        'V_met': gold['coeff_1'],
        'WF_minus_half_gap': gold['coeff_2'],
        'MBE': gold['coeff_3']
    }

    coeff_scores = []
    for desc, gold_coeff in expected.items():
        found = None
        for d, c in pairs:
            if d == desc:
                found = c
                break
        if found is None:
            coeff_scores.append(0.0)
        else:
            diff = abs(found - gold_coeff)
            if diff <= tol['coeff_abs']:
                coeff_scores.append(1.0)
            else:
                coeff_scores.append(max(0.0, 1.0 - (diff - tol['coeff_abs']) / 0.04))
    coeff_part = sum(coeff_scores) / len(coeff_scores)

    # RMSE directional
    rmse = artifact.get('RMSE')
    if rmse is not None:
        if rmse <= gold['RMSE'] + tol['rmse_abs']:
            rmse_part = 1.0
        else:
            rmse_part = max(0.0, 1.0 - (rmse - (gold['RMSE'] + tol['rmse_abs'])) / 0.05)
    else:
        rmse_part = 0.0

    return 0.5 * coeff_part + 0.5 * rmse_part


_SCORERS = {
    'step_01_regression_coefficients': score_0,
    'step_02_sisso_results': score_1,
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
