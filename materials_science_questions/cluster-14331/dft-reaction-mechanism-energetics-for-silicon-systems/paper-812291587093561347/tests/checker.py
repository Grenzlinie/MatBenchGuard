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
    for step in spec['steps']:
        sid = step.get('id','')
        if sid == 'energy_accuracy':
            ctx['gold_map'] = step.get('state_level_gold', {})
            ctx['tolerance_kcal'] = step.get('tolerance_kcal', 2.0)
        elif sid == 'energy_completeness':
            ctx['required_pairs'] = step.get('required_state_levels', [])
        elif sid == 'geometry_presence':
            ctx['required_geometries'] = step.get('required_geometries', [])
            ctx['forbidden_geometries'] = step.get('forbidden_geometries', [])
    return ctx


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    data = artifact
    if isinstance(data, dict) and 'energies' in data and 'geometries' in data:
        return 1.0
    return 0.0


# === block: score_1 (check id='energy_completeness') ===
def score_1(artifact, step, ctx):
    energies = artifact.get('energies', [])
    required = step.get('required_state_levels', [])
    present = 0
    for state, level in required:
        if any(e.get('state') == state and e.get('level') == level for e in energies):
            present += 1
    total = len(required)
    return present / total if total > 0 else 1.0


# === block: score_2 (check id='energy_accuracy') ===
def score_2(artifact, step, ctx):
    energies = artifact.get('energies', [])
    gold_map = ctx.get('gold_map', {})
    tol = ctx.get('tolerance_kcal', 2.0)
    reactants = {}
    for e in energies:
        if e.get('state') == 'reactants':
            level = e.get('level')
            if level and 'energy_au' in e:
                reactants[level] = e['energy_au']
    if not reactants:
        return 0.0
    score = 0.0
    count = 0
    for key, target in gold_map.items():
        try:
            state, level = key.split('::', 1)
        except:
            continue
        reactant_au = reactants.get(level)
        if reactant_au is None:
            continue
        entry = next((e for e in energies if e.get('state') == state and e.get('level') == level), None)
        if entry is None or 'energy_au' not in entry:
            continue
        rel = (entry['energy_au'] - reactant_au) * 627.509
        diff = abs(rel - target)
        if diff <= tol:
            score += 1.0
        count += 1
    return score / count if count > 0 else 0.0


# === block: score_3 (check id='energy_ordering') ===
def score_3(artifact, step, ctx):
    energies = artifact.get('energies', [])
    pairs = step.get('pairs', [])
    score = 0.0
    count = len(pairs)
    for pair in pairs:
        lower = pair['lower']
        higher = pair['higher']
        level = pair['level']
        e_low = next((e for e in energies if e.get('state') == lower and e.get('level') == level), None)
        e_high = next((e for e in energies if e.get('state') == higher and e.get('level') == level), None)
        if e_low and e_high and 'energy_au' in e_low and 'energy_au' in e_high:
            if e_low['energy_au'] < e_high['energy_au']:
                score += 1.0
    return score / count if count > 0 else 1.0


# === block: score_4 (check id='geometry_presence') ===
def score_4(artifact, step, ctx):
    geometries = artifact.get('geometries', {})
    required = step.get('required_geometries', [])
    forbidden = step.get('forbidden_geometries', [])
    if not isinstance(geometries, dict):
        return 0.0
    req_present = sum(1 for r in required if r in geometries)
    req_score = req_present / len(required) if required else 1.0
    forb_ok = all(f not in geometries for f in forbidden)
    return req_score * (1.0 if forb_ok else 0.5)


_SCORERS = {
    'shape_check': score_0,
    'energy_completeness': score_1,
    'energy_accuracy': score_2,
    'energy_ordering': score_3,
    'geometry_presence': score_4,
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
