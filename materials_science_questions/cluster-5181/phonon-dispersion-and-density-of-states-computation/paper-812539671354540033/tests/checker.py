import os
import json
import csv

# === author imports / helpers ===
import csv
import math
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
    ref = None
    for step in spec.get('steps', []):
        if step.get('output_file') == 'predicted_tbc.csv':
            ref = step.get('reference')
            break
    if not ref:
        raise ValueError('Missing reference data for predicted_tbc.csv')
    return {'reference': ref}


# === block: score_0 (check id='predicted_tbc_evaluation') ===
def score_0(artifact, step, ctx):
        ref = ctx['reference']
        req_temps = ref['temperature_K']
        agent_data = {}
        for row in artifact:
            t = float(row['temperature_K'])
            agent_data[t] = {
                'Al': float(row['Al_TBC_MW_m2K']),
                'Co': float(row['Co_TBC_MW_m2K']),
                'Ru': float(row['Ru_TBC_MW_m2K'])
            }
        Al_pred = []
        Co_pred = []
        Ru_pred = []
        for t in req_temps:
            if t not in agent_data:
                return 0.0
            d = agent_data[t]
            Al_pred.append(d['Al'])
            Co_pred.append(d['Co'])
            Ru_pred.append(d['Ru'])
        Al_exp = ref['Al_TBC_MW_m2K_experimental']
        Co_exp = ref['Co_TBC_MW_m2K_experimental']
        Ru_exp = ref['Ru_TBC_MW_m2K_experimental']
        def mape(preds, exps):
            total = 0.0
            n = len(preds)
            for p, e in zip(preds, exps):
                if e == 0:
                    return float('inf') if p != 0 else 0.0
                total += abs(p - e) / abs(e)
            return total / n if n > 0 else 0.0
        mape_al = mape(Al_pred, Al_exp)
        mape_co = mape(Co_pred, Co_exp)
        mape_ru = mape(Ru_pred, Ru_exp)
        mape_avg = (mape_al + mape_co + mape_ru) / 3.0
        mape_score = 0.0
        if mape_avg <= 0.15:
            mape_score = 1.0
        elif mape_avg < 0.50:
            mape_score = (0.50 - mape_avg) / (0.50 - 0.15)
        else:
            mape_score = 0.0
        def is_non_decreasing(seq):
            return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))
        mono_ok = is_non_decreasing(Al_pred) and is_non_decreasing(Co_pred) and is_non_decreasing(Ru_pred)
        order_ok = False
        if 300 in agent_data:
            d = agent_data[300]
            if d['Co'] >= d['Al'] and d['Co'] >= d['Ru']:
                order_ok = True
        struct_score = (0.5 if mono_ok else 0.0) + (0.5 if order_ok else 0.0)
        return 0.9 * mape_score + 0.1 * struct_score


_SCORERS = {
    'predicted_tbc_evaluation': score_0,
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
