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
    gold = spec.get('gold_values', {})
    tolerances = spec.get('tolerances', {})
    ctx = {'gold': gold, 'tolerances': tolerances}
    return ctx


# === block: score_0 (check id='csv_schema') ===
def score_0(artifact, step, ctx):
    required = ['metal', 'step', 'description', 'delta_G_sol_prime']
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    if not all(col in artifact[0] for col in required):
        return 0.0
    for row in artifact:
        try:
            float(row['delta_G_sol_prime'])
        except (ValueError, KeyError, TypeError):
            return 0.0
    return 1.0


# === block: score_1 (check id='row_completeness') ===
def score_1(artifact, step, ctx):
    gold = ctx['gold']
    expected = set()
    for metal, steps in gold.items():
        for s in steps:
            expected.add((metal, s))
    actual = set()
    for row in artifact:
        try:
            actual.add((row['metal'], row['step']))
        except KeyError:
            return 0.0
    if not expected:
        return 0.0
    missing = expected - actual
    return max(0.0, 1.0 - len(missing) / len(expected))


# === block: score_2 (check id='numeric_accuracy') ===
def score_2(artifact, step, ctx):
    gold = ctx['gold']
    tolerances = ctx['tolerances']
    def get_tol(step):
        if step in ('i-a','ii-a'):
            return tolerances.get('attachment', 0.2)
        elif step in ('i-b','ii-b'):
            return tolerances.get('relaxation', 0.3)
        elif step in ('i','ii','iii'):
            return tolerances.get('adiabatic', 0.25)
        elif step == 'iSC':
            return tolerances.get('iSC', 0.1)
        return 0.3
    total = 0
    correct = 0
    for row in artifact:
        metal = row.get('metal')
        step = row.get('step')
        if metal not in gold or step not in gold[metal]:
            continue
        try:
            val = float(row['delta_G_sol_prime'])
        except (ValueError, KeyError):
            continue
        if abs(val - gold[metal][step]) <= get_tol(step):
            correct += 1
        total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_3 (check id='trend_i_a') ===
def score_3(artifact, step, ctx):
    vals = {}
    for row in artifact:
        if row.get('step') == 'i-a':
            metal = row.get('metal')
            try:
                vals[metal] = float(row['delta_G_sol_prime'])
            except (ValueError, KeyError):
                pass
    if 'Fe' not in vals or 'Ru' not in vals or 'Os' not in vals:
        return 0.0
    # trend: Fe < Ru < Os (more negative means smaller number)
    if vals['Fe'] < vals['Ru'] < vals['Os']:
        return 1.0
    return 0.0


# === block: score_4 (check id='trend_ii') ===
def score_4(artifact, step, ctx):
    vals = {}
    for row in artifact:
        if row.get('step') == 'ii':
            metal = row.get('metal')
            try:
                vals[metal] = float(row['delta_G_sol_prime'])
            except (ValueError, KeyError):
                pass
    if 'Fe' not in vals or 'Ru' not in vals or 'Os' not in vals:
        return 0.0
    # trend: Fe > Ru > Os (less negative means larger number)
    if vals['Fe'] > vals['Ru'] > vals['Os']:
        return 1.0
    return 0.0


# === block: score_5 (check id='disproportionation_signs') ===
def score_5(artifact, step, ctx):
    i_vals = {}
    iii_vals = {}
    for row in artifact:
        if row.get('step') == 'i':
            try:
                i_vals[row['metal']] = float(row['delta_G_sol_prime'])
            except (ValueError, KeyError):
                pass
        elif row.get('step') == 'iii':
            try:
                iii_vals[row['metal']] = float(row['delta_G_sol_prime'])
            except (ValueError, KeyError):
                pass
    if set(i_vals.keys()) != {'Fe','Ru','Os'} or set(iii_vals.keys()) != {'Fe','Ru','Os'}:
        return 0.0
    disp = {m: i_vals[m] - iii_vals[m] for m in ['Fe','Ru','Os']}
    cond_fe = disp['Fe'] > 0.0
    cond_ru = abs(disp['Ru']) <= 0.2
    cond_os = disp['Os'] < -0.3
    return 1.0 if (cond_fe and cond_ru and cond_os) else 0.0


_SCORERS = {
    'csv_schema': score_0,
    'row_completeness': score_1,
    'numeric_accuracy': score_2,
    'trend_i_a': score_3,
    'trend_ii': score_4,
    'disproportionation_signs': score_5,
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
