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
    steps = spec.get('steps', [])
    ctx = {}
    for s in steps:
        if s.get('id') == 'energy_range':
            ctx['range_targets'] = s['targets']
        elif s.get('id') == 'triamine_averages':
            ctx['avg_targets'] = s['targets']
        elif s.get('id') == 'outcome_trend':
            ctx['outcome_mapping'] = s['outcome_mapping']
    return ctx


# === block: score_0 (check id='energy_range') ===
def score_0(artifact, step, ctx):
    targets = ctx['range_targets']
    min_val = min(float(row['FormationEnergy_kJ_per_mol_per_imine_bond']) for row in artifact)
    max_val = max(float(row['FormationEnergy_kJ_per_mol_per_imine_bond']) for row in artifact)
    tol = targets['tolerance_abs']
    within_min = 1.0 if abs(min_val - targets['min_target']) <= tol else 0.0
    within_max = 1.0 if abs(max_val - targets['max_target']) <= tol else 0.0
    return (within_min + within_max) / 2.0


# === block: score_1 (check id='triamine_averages') ===
def score_1(artifact, step, ctx):
    targets = ctx['avg_targets']
    tol = targets['tolerance_abs']
    groups = {}
    for row in artifact:
        tri = row['Triamine']
        e = float(row['FormationEnergy_kJ_per_mol_per_imine_bond'])
        groups.setdefault(tri, []).append(e)
    scores = 0
    for tri, gold in [('A', targets['A']), ('B', targets['B']), ('C', targets['C'])]:
        if tri in groups and groups[tri]:
            avg = statistics.mean(groups[tri])
            if abs(avg - gold) <= tol:
                scores += 1
        else:
            pass
    return scores / 3.0


# === block: score_2 (check id='outcome_trend') ===
def score_2(artifact, step, ctx):
    mapping = ctx['outcome_mapping']
    lookup = {}
    for m in mapping:
        key = (m['Triamine'], m['Aldehyde'])
        lookup[key] = m['Outcome']
    cat_vals = {'clean': [], 'partial': [], 'none': []}
    for row in artifact:
        key = (row['Triamine'], int(row['Aldehyde']))
        outcome = lookup.get(key)
        if outcome is None:
            continue
        cat_vals[outcome].append(float(row['FormationEnergy_kJ_per_mol_per_imine_bond']))
    means = {}
    for cat in ['clean', 'partial', 'none']:
        if cat_vals[cat]:
            means[cat] = statistics.mean(cat_vals[cat])
        else:
            means[cat] = None
    if means['clean'] is None or means['partial'] is None or means['none'] is None:
        return 0.0
    if means['clean'] <= means['partial'] <= means['none']:
        return 1.0
    return 0.0


_SCORERS = {
    'energy_range': score_0,
    'triamine_averages': score_1,
    'outcome_trend': score_2,
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
