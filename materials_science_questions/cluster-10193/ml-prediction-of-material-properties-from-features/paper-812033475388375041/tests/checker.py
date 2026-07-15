import os
import json
import csv

# === author imports / helpers ===
import csv
import os


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
        gold = spec.get('gold_metrics', {})
        return {'gold': gold}


# === block: score_0 (check id='check_metrics') ===
def score_0(artifact, step, ctx):
        gold = ctx['gold']
        # Build expected combinations
        expected = []
        for prop in ['formation_energy', 'stability', 'volume_per_atom', 'vacancy_energy']:
            for model in ['SVM-RBF', 'RF', 'RR', 'BPNN']:
                expected.append((prop, model))
    
        # Read artifact
        rows = artifact  # artifact is already list of dicts from csv.DictReader
        if not rows:
            return 0.0
    
        # Map agent rows by (property, model)
        agent_map = {}
        for r in rows:
            p = r.get('property', '').strip()
            m = r.get('model', '').strip()
            if p and m:
                agent_map[(p, m)] = r
    
        # Score each expected combination
        row_scores = []
        for prop, model in expected:
            if (prop, model) not in agent_map:
                row_scores.append(0.0)
                continue
            r = agent_map[(prop, model)]
            try:
                mae = float(r.get('MAE', float('nan')))
                mse = float(r.get('MSE', float('nan')))
                r2 = float(r.get('R2', float('nan')))
            except (ValueError, TypeError):
                row_scores.append(0.0)
                continue
            gold_entry = gold.get(prop, {}).get(model)
            if not gold_entry:
                row_scores.append(0.0)  # no reference
                continue
        
            gold_mae = float(gold_entry['MAE'])
            gold_mse = float(gold_entry['MSE'])
            gold_r2 = float(gold_entry['R2'])
        
            # MAE score (lower better)
            if mae <= gold_mae * 1.2:
                mae_score = 1.0
            elif mae <= gold_mae * 1.5:
                mae_score = 0.5
            else:
                mae_score = 0.0
        
            # MSE score
            if mse <= gold_mse * 1.2:
                mse_score = 1.0
            elif mse <= gold_mse * 1.5:
                mse_score = 0.5
            else:
                mse_score = 0.0
        
            # R2 score (higher better)
            if r2 >= gold_r2 - 0.1:
                r2_score = 1.0
            elif r2 >= gold_r2 - 0.2:
                r2_score = 0.5
            else:
                r2_score = 0.0
        
            row_score = (mae_score + mse_score + r2_score) / 3.0
            row_scores.append(row_score)
    
        if not row_scores:
            return 0.0
        return sum(row_scores) / len(row_scores)


_SCORERS = {
    'check_metrics': score_0,
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
