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
    return {}


# === block: score_0 (check id='formation_enthalpy') ===
def score_0(artifact, step, ctx):
    targets = step['targets']
    tol_rel = step['tolerance_rel']
    passed = 0
    for comp, gold in targets.items():
        agent_val = artifact.get(comp, {}).get('formation_enthalpy', None)
        if agent_val is not None and abs(agent_val - gold) <= tol_rel * abs(gold) + 1e-12:
            passed += 1
    return passed / len(targets) if targets else 1.0


# === block: score_1 (check id='bulk_modulus') ===
def score_1(artifact, step, ctx):
    targets = step['targets']
    tol_rel = step['tolerance_rel']
    passed = 0
    for comp, gold in targets.items():
        agent_val = artifact.get(comp, {}).get('bulk_modulus', None)
        if agent_val is not None and abs(agent_val - gold) <= tol_rel * abs(gold) + 1e-12:
            passed += 1
    return passed / len(targets) if targets else 1.0


# === block: score_2 (check id='shear_modulus') ===
def score_2(artifact, step, ctx):
    targets = step['targets']
    tol_rel = step['tolerance_rel']
    passed = 0
    for comp, gold in targets.items():
        agent_val = artifact.get(comp, {}).get('shear_modulus', None)
        if agent_val is not None and abs(agent_val - gold) <= tol_rel * abs(gold) + 1e-12:
            passed += 1
    return passed / len(targets) if targets else 1.0


# === block: score_3 (check id='youngs_modulus') ===
def score_3(artifact, step, ctx):
    targets = step['targets']
    tol_rel = step['tolerance_rel']
    passed = 0
    for comp, gold in targets.items():
        agent_val = artifact.get(comp, {}).get('youngs_modulus', None)
        if agent_val is not None and abs(agent_val - gold) <= tol_rel * abs(gold) + 1e-12:
            passed += 1
    return passed / len(targets) if targets else 1.0


# === block: score_4 (check id='poissons_ratio') ===
def score_4(artifact, step, ctx):
    targets = step['targets']
    tol_rel = step['tolerance_rel']
    passed = 0
    for comp, gold in targets.items():
        agent_val = artifact.get(comp, {}).get('poissons_ratio', None)
        if agent_val is not None and abs(agent_val - gold) <= tol_rel * abs(gold) + 1e-12:
            passed += 1
    return passed / len(targets) if targets else 1.0


# === block: score_5 (check id='debye_temperature') ===
def score_5(artifact, step, ctx):
    targets = step['targets']
    tol_rel = step['tolerance_rel']
    passed = 0
    for comp, gold in targets.items():
        agent_val = artifact.get(comp, {}).get('debye_temperature', None)
        if agent_val is not None and abs(agent_val - gold) <= tol_rel * abs(gold) + 1e-12:
            passed += 1
    return passed / len(targets) if targets else 1.0


# === block: score_6 (check id='bonding_electron_number') ===
def score_6(artifact, step, ctx):
    targets = step['targets']
    tol_rel = step['tolerance_rel']
    passed = 0
    for comp, gold in targets.items():
        agent_val = artifact.get(comp, {}).get('bonding_electron_number', None)
        if agent_val is not None and abs(agent_val - gold) <= tol_rel * abs(gold) + 1e-12:
            passed += 1
    return passed / len(targets) if targets else 1.0


# === block: score_7 (check id='Ba2Pb_band_gap') ===
def score_7(artifact, step, ctx):
    targets = step['targets']
    tol_abs = step['tolerance_abs']
    gold = targets['Ba2Pb_band_gap']
    agent_val = artifact.get('Ba2Pb_band_gap', None)
    if agent_val is not None and abs(agent_val - gold) <= tol_abs:
        return 1.0
    return 0.0


# === block: score_8 (check id='stability_order') ===
def score_8(artifact, step, ctx):
    target = step['targets']['stability_order']
    agent_order = artifact.get('stability_order', [])
    if agent_order == target:
        return 1.0
    return 0.0


_SCORERS = {
    'formation_enthalpy': score_0,
    'bulk_modulus': score_1,
    'shear_modulus': score_2,
    'youngs_modulus': score_3,
    'poissons_ratio': score_4,
    'debye_temperature': score_5,
    'bonding_electron_number': score_6,
    'Ba2Pb_band_gap': score_7,
    'stability_order': score_8,
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
