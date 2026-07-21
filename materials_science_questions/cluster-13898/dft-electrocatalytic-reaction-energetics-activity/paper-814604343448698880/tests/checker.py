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


# === block: score_0 (check id='adsorption_energies') ===
def score_0(artifact, step, ctx):
    import math
    step_ref = step.get('reference', {})
    checks = step.get('checks', {})
    expected_species = checks.get('species_present', list(step_ref.keys()))
    agent_data = {}
    for row in artifact:
        sp = str(row.get('species', '')).strip()
        try:
            val = float(row.get('Eads_ev'))
        except (ValueError, TypeError):
            val = None
        if sp:
            agent_data[sp] = val
    total = len(expected_species)
    if total == 0:
        return 0.0
    passes = 0
    for sp in expected_species:
        ref = step_ref.get(sp)
        if ref is None:
            continue
        ref_val = ref['value']
        tol = ref.get('tolerance_abs', 0.15)
        agent_val = agent_data.get(sp)
        if agent_val is not None and abs(agent_val - ref_val) <= tol + 1e-9:
            passes += 1
    score_val = passes / total
    all_neg = checks.get('all_negative', False)
    if all_neg:
        neg_ok = all(v is not None and v < 0 for v in agent_data.values())
        if not neg_ok:
            score_val *= 0.8
    return max(0.0, min(1.0, score_val))


# === block: score_1 (check id='activation_barriers') ===
def score_1(artifact, step, ctx):
    import math
    step_ref = step.get('reference', {})
    checks = step.get('checks', {})
    expected_rxns = checks.get('reactions_present', list(step_ref.keys()))
    agent_data = {}
    for row in artifact:
        rxn = str(row.get('reaction', '')).strip()
        try:
            val = float(row.get('Ea_ev'))
        except (ValueError, TypeError):
            val = None
        if rxn:
            agent_data[rxn] = val
    tolerance_passes = 0
    for rxn in expected_rxns:
        ref = step_ref.get(rxn)
        if ref is None:
            continue
        ref_val = ref['value']
        tol = ref.get('tolerance_abs', 0.20)
        agent_val = agent_data.get(rxn)
        if agent_val is not None and abs(agent_val - ref_val) <= tol + 1e-9:
            tolerance_passes += 1
    num_checks = len(expected_rxns)
    total_score = tolerance_passes
    all_pos_check = checks.get('all_positive', True)
    if all_pos_check:
        num_checks += 1
        all_pos = all(v is not None and v > 0 for v in agent_data.values())
        total_score += 1 if all_pos else 0
    highest_check = checks.get('O2_dissoc_highest', False)
    if highest_check:
        num_checks += 1
        e_o2d = agent_data.get('O2_dissoc')
        if e_o2d is not None:
            others = [v for k, v in agent_data.items() if k != 'O2_dissoc' and v is not None]
            highest_ok = all(e_o2d >= v for v in others) if others else True
        else:
            highest_ok = False
        total_score += 1 if highest_ok else 0
    return total_score / num_checks


# === block: score_2 (check id='free_energy_diagram') ===
def score_2(artifact, step, ctx):
    import math
    step_ref = step.get('reference', {})
    checks = step.get('checks', {})
    expected_steps = checks.get('steps_present', list(step_ref.keys()))
    agent_data = {}
    for row in artifact:
        sp = str(row.get('step', '')).strip()
        try:
            val = float(row.get('dG_ev'))
        except (ValueError, TypeError):
            val = None
        if sp:
            agent_data[sp] = val
    tolerance_passes = 0
    for sp in expected_steps:
        ref = step_ref.get(sp)
        if ref is None:
            continue
        ref_val = ref['value']
        tol = ref.get('tolerance_abs', 0.15)
        agent_val = agent_data.get(sp)
        if agent_val is not None and abs(agent_val - ref_val) <= tol + 1e-9:
            tolerance_passes += 1
    num_checks = len(expected_steps)
    total_score = tolerance_passes
    oh_pos_check = checks.get('OH_to_H2O_positive', True)
    if oh_pos_check:
        num_checks += 1
        oh_val = agent_data.get('OH->H2O')
        total_score += 1 if (oh_val is not None and oh_val > 0) else 0
    neg_check = checks.get('first_three_negative', True)
    if neg_check:
        num_checks += 1
        neg_steps = ['O2->OOH', 'OOH->O+H2O', 'O->OH']
        neg_ok = all(agent_data.get(s) is not None and agent_data.get(s) < 0 for s in neg_steps)
        total_score += 1 if neg_ok else 0
    return total_score / num_checks


_SCORERS = {
    'adsorption_energies': score_0,
    'activation_barriers': score_1,
    'free_energy_diagram': score_2,
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
