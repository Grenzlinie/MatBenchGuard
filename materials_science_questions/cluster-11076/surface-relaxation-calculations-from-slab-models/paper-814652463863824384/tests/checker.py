import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='bulk_shape') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) != 6:
        return 0.0
    systems = {item.get('system') for item in data if isinstance(item, dict)}
    expected = set(step['expected_systems'])
    if systems != expected:
        return 0.0
    required_keys = {'system','y','total_energy','a','b','c','reaction_energy','zpe_correction','helmholtz_enthalpy'}
    for item in data:
        if not all(k in item for k in required_keys):
            return 0.0
        for k in required_keys:
            if k == 'system':
                continue
            if k == 'y':
                if not isinstance(item[k], int) or item[k] not in {15,16}:
                    return 0.0
            elif not isinstance(item[k], (int, float)):
                return 0.0
    return 1.0


# === block: score_1 (check id='bulk_trends') ===
def score_1(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) == 0:
        return 0.0
    # Build lookup system -> y -> helmholtz
    lookup = {}
    for item in data:
        sys = item.get('system')
        y = item.get('y')
        h = item.get('helmholtz_enthalpy')
        if sys is None or y is None or h is None:
            continue
        lookup.setdefault(sys, {})[y] = h
    # Required systems
    required = step.get('expected_systems', ["Mg-Mg7H16","Mg-Mg7H15","Co-Mg7H16","Co-Mg7H15","Ni-Mg7H16","Ni-Mg7H15"])
    for sys in required:
        if sys not in lookup or 15 not in lookup.get(sys, {}) or 16 not in lookup.get(sys, {}):
            return 0.0
    # Check all enthalpies > 0
    for sys in lookup:
        for y in lookup[sys]:
            if lookup[sys][y] <= 0:
                return 0.0
    # Trend for y=16 and y=15
    checks_passed = 0
    total_checks = 2
    for y in (15, 16):
        mg = lookup.get("Mg-Mg7H{}".format(y), None)
        co = lookup.get("Co-Mg7H{}".format(y), None)
        ni = lookup.get("Ni-Mg7H{}".format(y), None)
        if mg is None or co is None or ni is None:
            continue
        if co < mg and ni < mg and co < ni:
            checks_passed += 1
    return checks_passed / total_checks if total_checks else 0.0


# === block: score_2 (check id='bulk_values') ===
def score_2(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list):
        return 0.0
    gold = step['gold_helmholtz']
    tol = step.get('tolerance', 0.1)
    lookup = {}
    for item in data:
        sys = item.get('system')
        val = item.get('helmholtz_enthalpy')
        if sys and val is not None:
            lookup[sys] = val
    passed = 0
    count = 0
    for sys, expected in gold.items():
        count += 1
        actual = lookup.get(sys)
        if actual is None:
            continue
        if abs(actual - expected) <= tol:
            passed += 1
    return passed / count if count else 0.0


# === block: score_3 (check id='surface_shape') ===
def score_3(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) == 0:
        return 0.0
    required_keys = {'system','layer','rumpling','relaxation','adsorption_energy','desorption_energy','desorption_frequency','relative_residence_time_percent'}
    expected_systems = {'Mg-Mg13H28(001)','Co-Mg13H28(001)','Ni-Mg13H28(001)'}
    expected_layers = {'L0','L1','L2','adsorbed'}
    for item in data:
        if not isinstance(item, dict):
            return 0.0
        if not all(k in item for k in required_keys):
            return 0.0
        if item['system'] not in expected_systems:
            return 0.0
        if item['layer'] not in expected_layers:
            return 0.0
    # Check that we have 3 layers per system and one adsorbed
    counts = {}
    for item in data:
        sys = item['system']
        layer = item['layer']
        counts.setdefault(sys, set()).add(layer)
    for sys in expected_systems:
        if 'L0' not in counts.get(sys, set()) or 'L1' not in counts.get(sys, set()) or 'L2' not in counts.get(sys, set()) or 'adsorbed' not in counts.get(sys, set()):
            return 0.0
    return 1.0


# === block: score_4 (check id='surface_trends') ===
def score_4(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list):
        return 0.0
    def get_by(entries, system, layer):
        for e in entries:
            if e.get('system') == system and e.get('layer') == layer:
                return e
        return None
    systems = ['Mg-Mg13H28(001)','Co-Mg13H28(001)','Ni-Mg13H28(001)']
    # L0 relaxation
    mg_relax0 = get_by(data, systems[0], 'L0')
    co_relax0 = get_by(data, systems[1], 'L0')
    ni_relax0 = get_by(data, systems[2], 'L0')
    if not all([mg_relax0, co_relax0, ni_relax0]):
        return 0.0
    relax0_ok = (co_relax0['relaxation'] < mg_relax0['relaxation']) and (ni_relax0['relaxation'] < mg_relax0['relaxation'])
    # L1 relaxation
    mg_relax1 = get_by(data, systems[0], 'L1')
    co_relax1 = get_by(data, systems[1], 'L1')
    ni_relax1 = get_by(data, systems[2], 'L1')
    if not all([mg_relax1, co_relax1, ni_relax1]):
        return 0.0
    relax1_ok = (co_relax1['relaxation'] > mg_relax1['relaxation']) and (ni_relax1['relaxation'] > mg_relax1['relaxation'])
    # Adsorption energy sign
    mg_ads = get_by(data, systems[0], 'adsorbed')
    co_ads = get_by(data, systems[1], 'adsorbed')
    ni_ads = get_by(data, systems[2], 'adsorbed')
    if not all([mg_ads, co_ads, ni_ads]):
        return 0.0
    ads_sign_ok = (mg_ads['adsorption_energy'] < 0) and (co_ads['adsorption_energy'] > 0) and (ni_ads['adsorption_energy'] < 0)
    # Desorption energy ordering Mg > Ni > Co
    des_energies = {}
    for sys in systems:
        entry = get_by(data, sys, 'adsorbed')
        if entry:
            des_energies[sys] = entry['desorption_energy']
    if len(des_energies) != 3:
        return 0.0
    des_order_ok = (des_energies[systems[0]] > des_energies[systems[2]] > des_energies[systems[1]])
    # Relative residence time Ni < Co < Mg
    res_times = {}
    for sys in systems:
        entry = get_by(data, sys, 'adsorbed')
        if entry:
            res_times[sys] = entry['relative_residence_time_percent']
    if len(res_times) != 3:
        return 0.0
    res_order_ok = (res_times[systems[2]] < res_times[systems[1]] < res_times[systems[0]])
    checks = [relax0_ok, relax1_ok, ads_sign_ok, des_order_ok, res_order_ok]
    return sum(checks) / len(checks)


# === block: score_5 (check id='surface_values') ===
def score_5(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list):
        return 0.0
    gold = step['gold_surface']
    tols = step['tolerances']
    systems = ['Mg-Mg13H28(001)','Co-Mg13H28(001)','Ni-Mg13H28(001)']
    def get_by(entries, system, layer):
        for e in entries:
            if e.get('system') == system and e.get('layer') == layer:
                return e
        return None
    checks = []
    # Relaxation L0
    for sys in systems:
        entry = get_by(data, sys, 'L0')
        if entry is None:
            checks.append(0)
            continue
        expected = gold['relaxation_L0'][sys]
        actual = entry['relaxation']
        if abs(actual - expected) <= tols['relaxation_L0']:
            checks.append(1)
        else:
            checks.append(0)
    # Relaxation L1
    for sys in systems:
        entry = get_by(data, sys, 'L1')
        if entry is None:
            checks.append(0)
            continue
        expected = gold['relaxation_L1'][sys]
        actual = entry['relaxation']
        if abs(actual - expected) <= tols['relaxation_L1']:
            checks.append(1)
        else:
            checks.append(0)
    # Adsorbed entry values
    for field in ['adsorption_energy','desorption_energy','desorption_frequency','relative_residence_time_percent']:
        gold_field = field
        tol_key = field
        for sys in systems:
            entry = get_by(data, sys, 'adsorbed')
            if entry is None:
                checks.append(0)
                continue
            expected = gold[gold_field][sys]
            actual = entry[field]
            if abs(actual - expected) <= tols[tol_key]:
                checks.append(1)
            else:
                checks.append(0)
    return sum(checks) / len(checks) if checks else 0.0


_SCORERS = {
    'bulk_shape': score_0,
    'bulk_trends': score_1,
    'bulk_values': score_2,
    'surface_shape': score_3,
    'surface_trends': score_4,
    'surface_values': score_5,
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
