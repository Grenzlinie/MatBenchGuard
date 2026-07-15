import os
import json
import csv

# === author imports / helpers ===
import os, csv

def load_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def find_value(rows, key, key_col, value_col):
    """Return float value from rows given a key match, or None."""
    for row in rows:
        if row.get(key_col, '').strip() == key:
            try:
                return float(row[value_col])
            except (ValueError, KeyError):
                return None
    return None


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
    # Pre-load dependent artifacts for stabilization recompute
    outputs_dir = spec.get('_outputs_dir', '/app/outputs')
    step_01 = load_csv(os.path.join(outputs_dir, 'step_01_interstitial_energies.csv'))
    step_02 = load_csv(os.path.join(outputs_dir, 'step_02_stack_fault_energies.csv'))
    ctx = {
        'interstitial': step_01,
        'stack_fault': step_02
    }
    return ctx


# === block: score_0 (check id='step_interstitials') ===
def score_0(artifact, step, ctx):
    targets = step.get('targets', {})
    tol = step.get('tolerance_eV', 0.5)
    ordering = step.get('ordering', [])
    value_col = step.get('value_column', 'formation_energy_eV')
    key_col = step.get('key_column', 'defect_name')
    breakdown = step.get('score_breakdown', {})
    value_weight = breakdown.get('value_match', 0.9)
    order_weight = breakdown.get('ordering', 0.1)
    if not artifact:
        return 0.0
    value_score = 0.0
    n = len(targets)
    if n > 0:
        for k, t in targets.items():
            v = find_value(artifact, k, key_col, value_col)
            if v is not None and abs(v - t) <= tol:
                value_score += 1.0 / n
    order_score = 0.0
    if ordering:
        vals = []
        all_found = True
        for k in ordering:
            v = find_value(artifact, k, key_col, value_col)
            if v is None:
                all_found = False
                break
            vals.append(v)
        if all_found and vals == sorted(vals):
            order_score = 1.0
    return value_weight * value_score + order_weight * order_score


# === block: score_1 (check id='step_stack_fault') ===
def score_1(artifact, step, ctx):
    targets = step.get('targets', {})
    tol = step.get('tolerance_meV_per_Ang2', 1.0)
    value_col = step.get('value_column', 'energy_meV_per_Ang2')
    key_col = step.get('key_column', 'stacking_type')
    if not artifact:
        return 0.0
    score = 0.0
    n = len(targets)
    if n == 0:
        return 0.0
    for k, t in targets.items():
        v = find_value(artifact, k, key_col, value_col)
        if v is not None and abs(v - t) <= tol:
            score += 1.0 / n
    return score


# === block: score_2 (check id='step_frenkel_barrier') ===
def score_2(artifact, step, ctx):
    targets = step.get('targets', {})
    tol = step.get('tolerance_eV', 0.5)
    value_col = step.get('value_column', 'barrier_eV')
    if not artifact or len(artifact) == 0:
        return 0.0
    first_row = artifact[0]
    try:
        v = float(first_row[value_col])
    except (ValueError, KeyError):
        return 0.0
    target = list(targets.values())[0] if targets else 0.0
    if abs(v - target) <= tol:
        return 1.0
    return 0.0


# === block: score_3 (check id='step_divacancies') ===
def score_3(artifact, step, ctx):
    targets = step.get('targets', {})
    tol = step.get('tolerance_eV', 0.5)
    ordering = step.get('ordering', [])
    value_col = step.get('value_column', 'formation_energy_eV')
    key_col = step.get('key_column', 'defect_name')
    breakdown = step.get('score_breakdown', {})
    value_weight = breakdown.get('value_match', 0.8)
    order_weight = breakdown.get('ordering', 0.2)
    if not artifact:
        return 0.0
    value_score = 0.0
    n = len(targets)
    if n > 0:
        for k, t in targets.items():
            v = find_value(artifact, k, key_col, value_col)
            if v is not None and abs(v - t) <= tol:
                value_score += 1.0 / n
    order_score = 0.0
    if ordering:
        vals = []
        all_found = True
        for k in ordering:
            v = find_value(artifact, k, key_col, value_col)
            if v is None:
                all_found = False
                break
            vals.append(v)
        if all_found and vals == sorted(vals):
            order_score = 1.0
    return value_weight * value_score + order_weight * order_score


# === block: score_4 (check id='step_stabilization') ===
def score_4(artifact, step, ctx):
    # Recompute stabilization energies from interstitial and stack fault data in context
    tol = step.get('tolerance_eV', 0.2)
    area = step.get('basal_area_Ang2', 82.64)
    formation_map = step.get('formation_key', {})
    sf_map = step.get('stack_fault_key', {})
    value_col = step.get('value_column', 'stabilization_energy_eV')
    key_col = step.get('key_column', 'interstitial_type')
    if not artifact:
        return 0.0
    interstitial = ctx.get('interstitial', [])
    stack_fault = ctx.get('stack_fault', [])
    # Extract needed numbers
    grafted = find_value(interstitial, formation_map.get('grafted', 'grafted'), 'defect_name', 'formation_energy_eV')
    threefold_energy = find_value(interstitial, formation_map.get('threefold', 'threefold'), 'defect_name', 'formation_energy_eV')
    spiro_energy = find_value(interstitial, formation_map.get('spiro', 'spiro'), 'defect_name', 'formation_energy_eV')
    sf_threefold = find_value(stack_fault, sf_map.get('threefold', 'threefold (AA-type)'), 'stacking_type', 'energy_meV_per_Ang2')
    sf_spiro = find_value(stack_fault, sf_map.get('spiro', 'fourfold (ABC-type)'), 'stacking_type', 'energy_meV_per_Ang2')
    if None in (grafted, threefold_energy, spiro_energy, sf_threefold, sf_spiro):
        return 0.0
    # Convert stacking fault from meV/Å² to eV by multiplying by area and 0.001
    stabilization_expected = {
        'threefold': (grafted - threefold_energy) + area * sf_threefold * 0.001,
        'spiro': (grafted - spiro_energy) + area * sf_spiro * 0.001
    }
    score = 0.0
    n = len(stabilization_expected)
    for k, expected in stabilization_expected.items():
        reported = find_value(artifact, k, key_col, value_col)
        if reported is not None and abs(reported - expected) <= tol:
            score += 1.0 / n
    return score


_SCORERS = {
    'step_interstitials': score_0,
    'step_stack_fault': score_1,
    'step_frenkel_barrier': score_2,
    'step_divacancies': score_3,
    'step_stabilization': score_4,
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
