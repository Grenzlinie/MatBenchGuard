import os
import json
import csv

# === author imports / helpers ===
import json
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
    spec = json.load(open('/tests/grading_spec.json'))
    gold = spec.get('gold_overpotentials', {})
    return {'gold': gold}


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    artifact_data = artifact
    if not isinstance(artifact_data, dict) or 'systems' not in artifact_data:
        return 0.0
    systems = artifact_data['systems']
    expected = {'pristine','on_graphene','on_Ni111','on_graphene_Ni111'}
    if set(systems.keys()) != expected:
        return 0.0
    for sys_name, data in systems.items():
        if not isinstance(data, dict):
            return 0.0
        if 'free_energy_steps' not in data or 'overpotentials' not in data:
            return 0.0
        steps = data['free_energy_steps']
        if not isinstance(steps, dict) or set(steps.keys()) != {'OER','ORR'}:
            return 0.0
        oer = steps.get('OER')
        orr = steps.get('ORR')
        if not isinstance(oer, list) or len(oer) != 4:
            return 0.0
        if not isinstance(orr, list) or len(orr) != 4:
            return 0.0
        if not all(isinstance(x, (int, float)) for x in oer + orr):
            return 0.0
        overpot = data['overpotentials']
        if not isinstance(overpot, dict) or 'ORR' not in overpot or 'OER' not in overpot:
            return 0.0
        if not isinstance(overpot['ORR'], (int, float)) or not isinstance(overpot['OER'], (int, float)):
            return 0.0
    return 1.0


# === block: score_1 (check id='self_consistency') ===
def score_1(artifact, step, ctx):
    systems = artifact.get('systems', {})
    expected = {'pristine','on_graphene','on_Ni111','on_graphene_Ni111'}
    if set(systems.keys()) != expected:
        return 0.0
    total = 0
    passed = 0
    for sys_name in expected:
        data = systems[sys_name]
        oer_steps = data['free_energy_steps']['OER']
        orr_steps = data['free_energy_steps']['ORR']
        oer_max = max(oer_steps)
        orr_max = max(orr_steps)
        recomputed_oer = oer_max - 1.23
        recomputed_orr = orr_max + 1.23
        sub_oer = data['overpotentials']['OER']
        sub_orr = data['overpotentials']['ORR']
        if abs(recomputed_oer - sub_oer) <= 1e-6:
            passed += 1
        if abs(recomputed_orr - sub_orr) <= 1e-6:
            passed += 1
        total += 2
    return passed / total if total > 0 else 0.0


# === block: score_2 (check id='free_energy_sum') ===
def score_2(artifact, step, ctx):
    systems = artifact.get('systems', {})
    expected = {'pristine','on_graphene','on_Ni111','on_graphene_Ni111'}
    if set(systems.keys()) != expected:
        return 0.0
    total = 0
    passed = 0
    for sys_name in expected:
        steps = systems[sys_name]['free_energy_steps']
        oer_sum = sum(steps['OER'])
        orr_sum = sum(steps['ORR'])
        if abs(oer_sum - 4.92) <= 0.1:
            passed += 1
        if abs(orr_sum - (-4.92)) <= 0.1:
            passed += 1
        total += 2
    return passed / total if total > 0 else 0.0


# === block: score_3 (check id='absolute_overpotential') ===
def score_3(artifact, step, ctx):
    gold = ctx.get('gold', {})
    if not gold:
        return 0.0
    systems = artifact.get('systems', {})
    expected = {'pristine','on_graphene','on_Ni111','on_graphene_Ni111'}
    if set(systems.keys()) != expected:
        return 0.0
    total = 0
    passed = 0
    for sys_name in expected:
        if sys_name not in gold:
            continue
        data = systems[sys_name]
        oer_steps = data['free_energy_steps']['OER']
        orr_steps = data['free_energy_steps']['ORR']
        recomputed_oer = max(oer_steps) - 1.23
        recomputed_orr = max(orr_steps) + 1.23
        gold_oer = gold[sys_name]['OER']
        gold_orr = gold[sys_name]['ORR']
        if recomputed_oer <= gold_oer + 0.15:
            passed += 1
        if recomputed_orr <= gold_orr + 0.15:
            passed += 1
        total += 2
    return passed / total if total > 0 else 0.0


# === block: score_4 (check id='trends') ===
def score_4(artifact, step, ctx):
    systems = artifact.get('systems', {})
    sys_need = {'pristine','on_graphene','on_Ni111','on_graphene_Ni111'}
    if not all(s in systems for s in sys_need):
        return 0.0
    overpot = {}
    for sys_name in sys_need:
        data = systems[sys_name]
        oer_steps = data['free_energy_steps']['OER']
        orr_steps = data['free_energy_steps']['ORR']
        overpot[sys_name] = {
            'OER': max(oer_steps) - 1.23,
            'ORR': max(orr_steps) + 1.23
        }
    checks = []
    checks.append(overpot['on_graphene_Ni111']['ORR'] < overpot['pristine']['ORR'])
    checks.append(overpot['on_graphene_Ni111']['OER'] < overpot['on_Ni111']['OER'])
    checks.append(abs(overpot['pristine']['ORR'] - overpot['on_graphene']['ORR']) <= 0.15)
    checks.append(abs(overpot['pristine']['OER'] - overpot['on_graphene']['OER']) <= 0.15)
    passed = sum(checks)
    return passed / 4.0


_SCORERS = {
    'shape_check': score_0,
    'self_consistency': score_1,
    'free_energy_sum': score_2,
    'absolute_overpotential': score_3,
    'trends': score_4,
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
