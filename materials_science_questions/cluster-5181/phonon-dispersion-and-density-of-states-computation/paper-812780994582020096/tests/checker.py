import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
    gold_lattice = {}
    for step in spec['steps']:
        if step['id'] == 'step_lattice_params':
            for row in step['gold']['rows']:
                key = (float(row['composition']), row['pseudopotential'])
                gold_lattice[key] = float(row['lattice_parameter_angstrom'])
            ctx = {'gold_lattice': gold_lattice, 'step_lattice_params': step}
        if step['id'] == 'step_vegard_deviation':
            ctx.setdefault('step_vegard_deviation', step)
    return ctx


# === block: score_0 (check id='step_lattice_params') ===
def score_0(artifact, step, ctx):
    gold_map = ctx['gold_lattice']
    tol = ctx['step_lattice_params']['tolerance']
    rows = artifact
    if not rows:
        return 0.0
    correct = 0
    for row in rows:
        comp = float(row.get('composition', None))
        pseudo = row.get('pseudopotential', '')
        val = float(row.get('lattice_parameter_angstrom', None))
        key = (comp, pseudo)
        if key in gold_map:
            if abs(val - gold_map[key]) <= tol:
                correct += 1
    return correct / max(len(gold_map), 1) if len(gold_map) > 0 else 0.0


# === block: score_1 (check id='step_vegard_deviation') ===
def score_1(artifact, step, ctx):
    import csv
    lattice_path = os.path.join('/app/outputs', ctx['step_vegard_deviation']['recompute']['source_file'])
    if not os.path.exists(lattice_path):
        return 0.0
    lattice_rows = []
    with open(lattice_path, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            lattice_rows.append(r)
    if not lattice_rows:
        return 0.0
    # group by pseudopotential
    pseudo_vals = {}
    for row in lattice_rows:
        pseudo = row['pseudopotential']
        comp = float(row['composition'])
        a = float(row['lattice_parameter_angstrom'])
        if pseudo not in pseudo_vals:
            pseudo_vals[pseudo] = {}
        pseudo_vals[pseudo][comp] = a
    # recompute max deviation
    comps = ctx['step_vegard_deviation']['recompute']['params']['compositions']
    gold = ctx['step_vegard_deviation']['gold']
    tol = ctx['step_vegard_deviation']['tolerance']
    scores = []
    for pseudo in gold:
        if pseudo not in pseudo_vals:
            scores.append(0.0)
            continue
        comp_dict = pseudo_vals[pseudo]
        if 0.0 not in comp_dict or 1.0 not in comp_dict:
            scores.append(0.0)
            continue
        a0 = comp_dict[0.0]
        a1 = comp_dict[1.0]
        max_dev = 0.0
        for x in comps:
            if x not in comp_dict:
                continue
            a = comp_dict[x]
            a_ideal = x * a1 + (1 - x) * a0
            dev = 100.0 * abs(a - a_ideal) / a_ideal
            max_dev = max(max_dev, dev)
        gold_val = gold[pseudo]
        if abs(max_dev - gold_val) <= tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'step_lattice_params': score_0,
    'step_vegard_deviation': score_1,
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
