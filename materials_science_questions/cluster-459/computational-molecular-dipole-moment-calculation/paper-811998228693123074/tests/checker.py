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


# === block: score_0 (check id='step_01_monomer') ===
def score_0(artifact, step, ctx):
    checks = step.get('checks', [])
    total_weight = 0.0
    score = 0.0
    for c in checks:
        field = c['field']
        target = c['target']
        tol = c['tolerance']
        w = c['weight']
        if field in artifact:
            val = artifact[field]
            if abs(val - target) <= tol:
                score += w
        total_weight += w
    if total_weight > 0:
        return score / total_weight
    return 0.0


# === block: score_1 (check id='step_03_dimer_Ia') ===
def score_1(artifact, step, ctx):
    checks = step.get('checks', [])
    total_weight = 0.0
    score = 0.0
    for c in checks:
        field = c['field']
        target = c['target']
        tol = c['tolerance']
        w = c['weight']
        if field in artifact:
            val = artifact[field]
            if abs(val - target) <= tol:
                score += w
        total_weight += w
    if total_weight > 0:
        return score / total_weight
    return 0.0


# === block: score_2 (check id='step_04_dimer_Ib') ===
def score_2(artifact, step, ctx):
    checks = step.get('checks', [])
    total_weight = 0.0
    score = 0.0
    for c in checks:
        field = c['field']
        target = c['target']
        tol = c['tolerance']
        w = c['weight']
        if field in artifact:
            val = artifact[field]
            if abs(val - target) <= tol:
                score += w
        total_weight += w
    if total_weight > 0:
        return score / total_weight
    return 0.0


# === block: score_3 (check id='step_05_formation') ===
def score_3(artifact, step, ctx):
    import os
    checks = step.get('checks', [])
    score = 0.0
    total_weight = sum(c['weight'] for c in checks)

    monomer_path = os.path.join('/app/outputs', 'monomer_properties.json')
    dimer_Ia_path = os.path.join('/app/outputs', 'dimer_Ia_properties.json')
    dimer_Ib_path = os.path.join('/app/outputs', 'dimer_Ib_properties.json')
    formation_path = os.path.join('/app/outputs', 'formation_energies.json')

    # Load energies
    E_mon = None
    E_Ia = None
    E_Ib = None
    formation_data = None
    if os.path.exists(monomer_path):
        with open(monomer_path) as f:
            mon = json.load(f)
            E_mon = mon.get('energy')
    if os.path.exists(dimer_Ia_path):
        with open(dimer_Ia_path) as f:
            Ia = json.load(f)
            E_Ia = Ia.get('energy')
    if os.path.exists(dimer_Ib_path):
        with open(dimer_Ib_path) as f:
            Ib = json.load(f)
            E_Ib = Ib.get('energy')
    if os.path.exists(formation_path):
        with open(formation_path) as f:
            formation_data = json.load(f)

    HARTREE_TO_KCAL = 627.509

    for c in checks:
        field = c['field']
        target = c['target']
        tol = c['tolerance']
        w = c['weight']

        if field == 'Ia_recomputed_delta_E' and E_mon is not None and E_Ia is not None:
            delta_E_ha = E_Ia - 2 * E_mon
            delta_E_kcal = delta_E_ha * HARTREE_TO_KCAL
            if abs(delta_E_kcal - target) <= tol:
                score += w
        elif field == 'Ib_recomputed_delta_E' and E_mon is not None and E_Ib is not None:
            delta_E_ha = E_Ib - 2 * E_mon
            delta_E_kcal = delta_E_ha * HARTREE_TO_KCAL
            if abs(delta_E_kcal - target) <= tol:
                score += w
        elif field == 'Ia_delta_E0' and formation_data is not None:
            if 'Ia_delta_E0' in formation_data and formation_data['Ia_delta_E0'] is not None:
                val = formation_data['Ia_delta_E0']
                if abs(val - target) <= tol:
                    score += w
        elif field == 'Ib_delta_E0' and formation_data is not None:
            if 'Ib_delta_E0' in formation_data and formation_data['Ib_delta_E0'] is not None:
                val = formation_data['Ib_delta_E0']
                if abs(val - target) <= tol:
                    score += w
        elif field == 'Ia_delta_E_solvent' and formation_data is not None:
            if 'Ia_delta_E_solvent' in formation_data and formation_data['Ia_delta_E_solvent'] is not None:
                val = formation_data['Ia_delta_E_solvent']
                if abs(val - target) <= tol:
                    score += w
        elif field == 'Ib_delta_E_solvent' and formation_data is not None:
            if 'Ib_delta_E_solvent' in formation_data and formation_data['Ib_delta_E_solvent'] is not None:
                val = formation_data['Ib_delta_E_solvent']
                if abs(val - target) <= tol:
                    score += w

    # Solvent formation energy bonus (paper: Ia ΔE(solvent)=1.38 kcal/mol, Ib ΔE(solvent)=2.14 kcal/mol)
    # These are unconditionally checked if the artifact includes the fields, ensuring the headline
    # solvent result is scored even if the grading spec omits the corresponding checks.
    solvent_checks = [
        {'field': 'Ia_delta_E_solvent', 'target': 1.38, 'tolerance': 0.5, 'weight': 0.1},
        {'field': 'Ib_delta_E_solvent', 'target': 2.14, 'tolerance': 0.5, 'weight': 0.1},
    ]
    for sc in solvent_checks:
        if formation_data is not None and sc['field'] in formation_data and formation_data[sc['field']] is not None:
            if abs(formation_data[sc['field']] - sc['target']) <= sc['tolerance']:
                score += sc['weight']
        total_weight += sc['weight']

    if total_weight > 0:
        return score / total_weight
    return 0.0


_SCORERS = {
    'step_01_monomer': score_0,
    'step_03_dimer_Ia': score_1,
    'step_04_dimer_Ib': score_2,
    'step_05_formation': score_3,
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
