import os
import json
import csv

# === author imports / helpers ===
import csv
import os
import json


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
    return {"step": spec['steps'][0]}


# === block: score_0 (check id='step_03') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not isinstance(artifact, list) or not artifact:
            return 0.0
        ref = step.get('reference_values', {})
        tol = step.get('tolerance_abs', 0.2)
        trends = step.get('trend_checks', {})
    
        # build mapping from condition to list of Y values
        y_dict = {}
        for row in artifact:
            cond = (row.get('Condition') or '').strip()
            y_str = (row.get('Youngs_modulus_TPa') or '').strip()
            if not cond or y_str == '':
                continue
            try:
                y_val = float(y_str)
            except (ValueError, TypeError):
                continue
            y_dict.setdefault(cond, []).append(y_val)
    
        # average per condition
        y_avg = {c: sum(vals)/len(vals) for c, vals in y_dict.items()}
    
        # score per condition
        total_cond = len(ref)
        acc_score = 0.0
        for cond, gold in ref.items():
            val = y_avg.get(cond, None)
            if val is None:
                continue
            diff = abs(val - gold)
            if diff <= tol:
                acc_score += 1.0
            else:
                acc_score += max(0.0, 1.0 - (diff - tol) / tol)  # decay beyond tolerance
        cond_score = acc_score / total_cond if total_cond > 0 else 0.0
    
        # trend checks
        def get_cond(name):
            return y_avg.get(name, None)
    
        trend_score = 0.0
        num_trends = 0
        for tid, t in trends.items():
            try:
                if "min_diff" in t:
                    a = get_cond(t['cond_small']) if 'cond_small' in t else get_cond(t['cond_low'])
                    b = get_cond(t['cond_large']) if 'cond_large' in t else get_cond(t['cond_high'])
                    if a is None or b is None:
                        continue
                    if b - a >= t['min_diff']:
                        trend_score += 1.0
                    else:
                        trend_score += max(0.0, 1.0 - (t['min_diff'] - (b-a)) / t['min_diff'])
                elif "max_diff" in t:
                    v1 = get_cond(t.get('cond_large'))
                    v2 = get_cond(t.get('cond_sat'))
                    if v1 is None or v2 is None:
                        continue
                    diff = abs(v2 - v1)
                    if diff <= t['max_diff']:
                        trend_score += 1.0
                    else:
                        trend_score += max(0.0, 1.0 - (diff - t['max_diff']) / t['max_diff'])
                num_trends += 1
            except Exception:
                continue
        trend_score_final = trend_score / num_trends if num_trends > 0 else 0.0
    
        w_acc = 0.7
        w_trend = 0.3
        return w_acc * cond_score + w_trend * trend_score_final


_SCORERS = {
    'step_03': score_0,
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
