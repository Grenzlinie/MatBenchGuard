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
    gold = {}
    thresh = {}
    for step in spec.get('steps', []):
        if step['id'] == 'adsorption_energies':
            gold = step.get('gold_values', {})
            tol = step.get('tolerance', 25.0)
        elif step['id'] == 'classification_trends':
            thresh = step.get('thresholds', {})
    return {'gold': gold, 'tol': tol, 'thresh': thresh}


# === block: score_0 (check id='adsorption_energies') ===
def score_0(artifact, step, ctx):
    import math
    energies = artifact
    gold = ctx['gold']
    tol = ctx['tol']

    # mapping from gold key to (complex_key, ref1, ref2)
    pairs = [
        ('ads_Na_G', 'G_Na', 'G', 'Na'),
        ('ads_Na_A', 'A_Na', 'A', 'Na'),
        ('ads_Na_Z', 'Z_Na', 'Z', 'Na'),
        ('ads_NO_G', 'G_NO', 'G', 'NO'),
        ('ads_NO_A', 'A_NO', 'A', 'NO'),
        ('ads_NO_Z', 'Z_NO', 'Z', 'NO'),
        ('ads_NO_G_Na', 'G_Na_NO', 'G_Na', 'NO'),
        ('ads_NO_A_Na', 'A_Na_NO', 'A_Na', 'NO'),
        ('ads_NO_Z_Na', 'Z_Na_NO', 'Z_Na', 'NO'),
    ]
    correct = 0
    for key, comp, refA, refB in pairs:
        target_val = gold.get(key)
        if target_val is None:
            continue
        e_ab = energies.get(comp)
        e_a = energies.get(refA)
        e_b = energies.get(refB)
        if e_ab is None or e_a is None or e_b is None:
            continue
        ads = e_ab - (e_a + e_b)
        if abs(ads - target_val) <= tol + 1e-9:
            correct += 1
    score = correct / len(pairs) if pairs else 1.0
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='classification_trends') ===
def score_1(artifact, step, ctx):
    energies = artifact
    thresh = ctx['thresh']
    chem_max = float(thresh.get('chemisorption_max', -50))
    phys_min_G = float(thresh.get('physisorption_min_G', -30))
    z_tol_percent = float(thresh.get('Z_Na_NO_tolerance_percent', 20)) / 100.0

    # compute adsorption energies
    ads_Na_G = energies.get('G_Na', 0.0) - (energies.get('G', 0.0) + energies.get('Na', 0.0))
    ads_Na_A = energies.get('A_Na', 0.0) - (energies.get('A', 0.0) + energies.get('Na', 0.0))
    ads_Na_Z = energies.get('Z_Na', 0.0) - (energies.get('Z', 0.0) + energies.get('Na', 0.0))
    ads_NO_G = energies.get('G_NO', 0.0) - (energies.get('G', 0.0) + energies.get('NO', 0.0))
    ads_NO_A = energies.get('A_NO', 0.0) - (energies.get('A', 0.0) + energies.get('NO', 0.0))
    ads_NO_Z = energies.get('Z_NO', 0.0) - (energies.get('Z', 0.0) + energies.get('NO', 0.0))
    ads_NO_G_Na = energies.get('G_Na_NO', 0.0) - (energies.get('G_Na', 0.0) + energies.get('NO', 0.0))
    ads_NO_A_Na = energies.get('A_Na_NO', 0.0) - (energies.get('A_Na', 0.0) + energies.get('NO', 0.0))
    ads_NO_Z_Na = energies.get('Z_Na_NO', 0.0) - (energies.get('Z_Na', 0.0) + energies.get('NO', 0.0))

    conditions = []
    # 1-3: all Na ads are chemisorption (< -50)
    conditions.append(ads_Na_G < chem_max)
    conditions.append(ads_Na_A < chem_max)
    conditions.append(ads_Na_Z < chem_max)
    # 4: ordering Z < A < G (more negative first)
    conditions.append(ads_Na_Z < ads_Na_A and ads_Na_A < ads_Na_G)
    # 5: NO on G is physisorption (> -30)
    conditions.append(ads_NO_G > phys_min_G)
    # 6-7: NO on A and Z are chemisorption
    conditions.append(ads_NO_A < chem_max)
    conditions.append(ads_NO_Z < chem_max)
    # 8: NO on G@Na is chemisorption
    conditions.append(ads_NO_G_Na < chem_max)
    # 9: NO on A@Na is more negative than bare A-NO
    conditions.append(ads_NO_A_Na < ads_NO_A)
    # 10: Z@Na-NO within 20% of bare Z-NO
    ref = abs(ads_NO_Z)
    if ref > 1e-9:
        conditions.append(abs(ads_NO_Z_Na - ads_NO_Z) / ref <= z_tol_percent + 1e-9)
    else:
        conditions.append(True)

    correct = sum(1 for c in conditions if c)
    score = correct / len(conditions) if conditions else 1.0
    return max(0.0, min(1.0, score))


_SCORERS = {
    'adsorption_energies': score_0,
    'classification_trends': score_1,
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
