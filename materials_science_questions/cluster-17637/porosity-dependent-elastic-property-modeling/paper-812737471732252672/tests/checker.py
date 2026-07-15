import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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
    steps = spec.get('steps', [])
    gold_porosity = {}
    gold_eff = {}
    for step in steps:
        if step.get('id') == 'porosity_check':
            gold_porosity['min'] = step['gold_min']
            gold_porosity['max'] = step['gold_max']
            gold_porosity['avg'] = step['gold_avg']
            gold_porosity['tol_min_max'] = step['tolerance_min_max_abs']
            gold_porosity['tol_avg'] = step['tolerance_avg_abs']
        elif step.get('id') == 'effective_modulus_check':
            gold_eff['values'] = step['gold_values']
            gold_eff['tol'] = step['value_tolerance_abs']
    return {'porosity': gold_porosity, 'effective_modulus': gold_eff}


# === block: score_0 (check id='porosity_check') ===
def score_0(artifact, step, ctx):
    import csv
    if not isinstance(artifact, list) or len(artifact) != 36:
        return 0.0
    required = {'D_um','d_um','theta_pattern','porosity_percent'}
    if not required.issubset(artifact[0].keys()):
        return 0.0
    rows = []
    for r in artifact:
        try:
            rows.append({'D': int(r['D_um']), 'd': int(r['d_um']), 'theta': int(r['theta_pattern']), 'por': float(r['porosity_percent'])})
        except (ValueError, KeyError):
            return 0.0
    gold = ctx.get('porosity', {})
    tol_mm = gold.get('tol_min_max', 2.0)
    tol_avg = gold.get('tol_avg', 2.0)
    min_por = min(r['por'] for r in rows)
    max_por = max(r['por'] for r in rows)
    avg_por = sum(r['por'] for r in rows) / len(rows)
    min_ok = 1.0 if abs(min_por - gold['min']) <= tol_mm else 0.0
    max_ok = 1.0 if abs(max_por - gold['max']) <= tol_mm else 0.0
    avg_ok = 1.0 if abs(avg_por - gold['avg']) <= tol_avg else 0.0
    accuracy = (min_ok + max_ok + avg_ok) / 3.0
    # Trend checks
    by_Dd_theta = {}
    for r in rows:
        key = (r['D'], r['d'])
        by_Dd_theta.setdefault(key, {})[r['theta']] = r['por']
    violations = 0
    total_comps = 0
    # theta trend (increase with theta)
    for key, th_dict in by_Dd_theta.items():
        thetas = sorted(th_dict.keys())
        for i in range(len(thetas)-1):
            t1, t2 = thetas[i], thetas[i+1]
            total_comps += 1
            if th_dict[t2] - th_dict[t1] < 1e-4:
                violations += 1
    # d trend (increase with d)
    by_Dt_d = {}
    for r in rows:
        key = (r['D'], r['theta'])
        by_Dt_d.setdefault(key, {})[r['d']] = r['por']
    for key, d_dict in by_Dt_d.items():
        ds = sorted(d_dict.keys())
        for i in range(len(ds)-1):
            total_comps += 1
            if d_dict[ds[i+1]] - d_dict[ds[i]] < 1e-4:
                violations += 1
    # D trend (decrease with D)
    by_dt_D = {}
    for r in rows:
        key = (r['d'], r['theta'])
        by_dt_D.setdefault(key, {})[r['D']] = r['por']
    for key, D_dict in by_dt_D.items():
        Ds = sorted(D_dict.keys())
        for i in range(len(Ds)-1):
            total_comps += 1
            if D_dict[Ds[i]] - D_dict[Ds[i+1]] < 1e-4:
                violations += 1
    trend_score = 1.0 - (violations / max(total_comps, 1))
    return 0.4 * accuracy + 0.6 * trend_score


# === block: score_1 (check id='effective_modulus_check') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 8:
        return 0.0
    required = {'composite_id','model_name','E_eff_GPa'}
    if not required.issubset(artifact[0].keys()):
        return 0.0
    gold_vals = ctx.get('effective_modulus', {}).get('values', {})
    tol = ctx.get('effective_modulus', {}).get('tol', 2.0)
    if not gold_vals:
        return 0.0
    val_scores = []
    trend_pass = 0
    trend_total = len(gold_vals)
    reported = {}
    for row in artifact:
        cid = str(row.get('composite_id',''))
        mname = str(row.get('model_name',''))
        try:
            E = float(row['E_eff_GPa'])
        except (ValueError, KeyError):
            return 0.0
        reported.setdefault(cid, {})[mname] = E
    for cid, models in gold_vals.items():
        if cid not in reported:
            val_scores.append(0.0)
            continue
        low_model = '0.4_0.5_4'
        high_model = '0.8_0.3_1'
        E_high = reported[cid].get(high_model)
        E_low = reported[cid].get(low_model)
        # value accuracy (average of two models)
        for model_name, gold_E in models.items():
            rep = reported[cid].get(model_name)
            if rep is None:
                val_scores.append(0.0)
            else:
                diff = abs(rep - gold_E)
                if diff <= tol:
                    val_scores.append(1.0)
                elif diff <= 3*tol:
                    val_scores.append(0.5)
                else:
                    val_scores.append(0.0)
        # trend check: low model must have lower modulus
        if E_high is not None and E_low is not None:
            if E_high > E_low:
                trend_pass += 1
    value_score = sum(val_scores) / max(len(val_scores), 1)
    trend_score = trend_pass / max(trend_total, 1)
    return 0.8 * value_score + 0.2 * trend_score


_SCORERS = {
    'porosity_check': score_0,
    'effective_modulus_check': score_1,
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
