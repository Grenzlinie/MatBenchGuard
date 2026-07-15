import os
import json
import csv

# === author imports / helpers ===
import csv
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
    cond_list = spec.get('gold_conditions', [])
    tol_rel = spec.get('tolerance_relative', 0.10)
    tol_abs = spec.get('tolerance_absolute', 0.05)
    cond_map = {}
    for c in cond_list:
        key = (c['system'], c['temperature_K'])
        cond_map[key] = c
    return {'cond_map': cond_map, 'tol_rel': tol_rel, 'tol_abs': tol_abs}


# === block: score_0 (check id='results_check') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    cols = list(artifact[0].keys())
    required = ['system','temperature_K','beta_self','beta_exch','alpha']
    for c in required:
        if c not in cols:
            return 0.0

    cond_list = step.get('gold_conditions', [])
    tol_rel = step.get('tolerance_relative', 0.10)
    tol_abs = step.get('tolerance_absolute', 0.05)
    cond_map = {}
    for c in cond_list:
        key = (c['system'], c['temperature_K'])
        cond_map[key] = c

    rows = []
    for row in artifact:
        try:
            sys = row['system'].strip().lower()
            temp = float(row['temperature_K'])
            beta_self = float(row['beta_self'])
            beta_exch = float(row['beta_exch'])
            alpha = float(row['alpha'])
        except (ValueError, KeyError):
            return 0.0
        if sys not in ('argon','water'):
            return 0.0
        computed_alpha = round(1.0 - (beta_self + beta_exch), 6)
        if abs(computed_alpha - round(alpha, 6)) > 0.01:
            continue
        rows.append({'system': sys, 'temperature_K': temp, 'beta_self': beta_self, 'beta_exch': beta_exch, 'alpha': alpha, 'computed_alpha': computed_alpha})

    if not rows:
        return 0.0

    row_scores = []
    for row in rows:
        key = (row['system'], row['temperature_K'])
        gold = cond_map.get(key)
        if gold is None:
            row_scores.append(0.0)
            continue
        field_scores = []
        for field in ['beta_self', 'beta_exch', 'alpha']:
            agent_val = row[field]
            gold_val = gold[field]
            diff = abs(agent_val - gold_val)
            threshold = max(tol_rel * abs(gold_val), tol_abs)
            if diff <= threshold:
                field_scores.append(1.0)
            else:
                extra = diff - threshold
                score = max(0.0, 1.0 - extra / 0.3)
                field_scores.append(score)
        row_scores.append(sum(field_scores) / len(field_scores))

    if not row_scores:
        return 0.0
    base_score = sum(row_scores) / len(row_scores)

    system_temps = {}
    for row in rows:
        sys = row['system']
        system_temps.setdefault(sys, []).append((row['temperature_K'], row['alpha']))

    trend_ok = True
    for sys in ['argon','water']:
        pairs = sorted(system_temps.get(sys, []))
        for i in range(1, len(pairs)):
            if pairs[i][1] > pairs[i-1][1] + 0.01:
                trend_ok = False
                break

    beta_exch_ok = True
    for row in rows:
        key = (row['system'], row['temperature_K'])
        gold = cond_map.get(key)
        if gold and gold.get('beta_exch', 1.0) > 0.001 and row['beta_exch'] < 0.001:
            beta_exch_ok = False
            break

    penalty = 0.0
    if not trend_ok:
        penalty += 0.2
    if not beta_exch_ok:
        penalty += 0.1

    final_score = max(0.0, min(1.0, base_score - penalty))
    return final_score


_SCORERS = {
    'results_check': score_0,
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
