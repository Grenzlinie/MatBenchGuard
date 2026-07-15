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
    gold = spec.get('gold', {})
    tolerances = spec.get('tolerances', {})
    return {'gold': gold, 'tol': tolerances}


# === block: score_0 (check id='formation_energies') ===
def score_0(artifact, step, ctx):
    gold_data = ctx['gold']['formation_energies_at_charge_neutrality.json']
    tol_Ef0 = ctx['tol']['E_F0']
    tol_fe = ctx['tol']['formation_energy']

    def score_value(value, target, tol):
        diff = abs(value - target)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / (4 * tol))

    subs = []
    # Pb_rich E_F0
    if 'Pb_rich' in artifact and 'E_F0' in artifact['Pb_rich']:
        subs.append(score_value(artifact['Pb_rich']['E_F0'], gold_data['Pb_rich']['E_F0'], tol_Ef0))
    else:
        subs.append(0.0)
    # Br_rich E_F0
    if 'Br_rich' in artifact and 'E_F0' in artifact['Br_rich']:
        subs.append(score_value(artifact['Br_rich']['E_F0'], gold_data['Br_rich']['E_F0'], tol_Ef0))
    else:
        subs.append(0.0)

    # Pb_rich defects
    pb_defects = artifact.get('Pb_rich', {}).get('defects', [])
    pb_map = {d['defect']: d['formation_energy'] for d in pb_defects if isinstance(d, dict) and 'defect' in d and 'formation_energy' in d}
    for name, target_fe in gold_data['Pb_rich']['defects'].items():
        subs.append(score_value(pb_map.get(name, float('inf')), target_fe, tol_fe))
    # Br_rich defects
    br_defects = artifact.get('Br_rich', {}).get('defects', [])
    br_map = {d['defect']: d['formation_energy'] for d in br_defects if isinstance(d, dict) and 'defect' in d and 'formation_energy' in d}
    for name, target_fe in gold_data['Br_rich']['defects'].items():
        subs.append(score_value(br_map.get(name, float('inf')), target_fe, tol_fe))

    score = sum(subs) / len(subs) if subs else 0.0
    return score


# === block: score_1 (check id='transition_levels') ===
def score_1(artifact, step, ctx):
    gold_trans = ctx['gold']['defect_transition_levels.json']
    tol_tl = ctx['tol']['transition_level']

    def score_value(value, target, tol):
        diff = abs(value - target)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / (4 * tol))

    subs = []
    for key, target in gold_trans.items():
        if key not in artifact:
            subs.append(0.0)
        else:
            subs.append(score_value(artifact[key], target, tol_tl))
    score = sum(subs) / len(subs) if subs else 0.0
    return score


_SCORERS = {
    'formation_energies': score_0,
    'transition_levels': score_1,
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
