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


# === block: score_0 (check id='score_results') ===
def score_0(artifact, step, ctx):
    data = artifact
    gold = step.get('gold', {})
    tol = step.get('tolerances', {})
    energy_tol = tol.get('energy', 0.2)
    dist_tol = tol.get('distance', 0.2)
    hsc_tol = tol.get('hsc', 0.5)

    def compare(actual, gold_val, tol):
        if isinstance(gold_val, list) and isinstance(actual, list):
            if len(actual) != len(gold_val):
                return False
            return all(abs(a - g) <= tol for a, g in zip(actual, gold_val))
        else:
            try:
                return abs(float(actual) - float(gold_val)) <= tol
            except (TypeError, ValueError):
                return False

    total = 0
    passed = 0

    # binding_energy_Li_on_pure_graphene
    key = 'binding_energy_Li_on_pure_graphene'
    if key in data:
        total += 1
        g = gold.get(key, {}).get('value')
        if g is not None and abs(data[key] - g) <= energy_tol:
            passed += 1
    else:
        total += 1

    # Li_nO
    for ent in gold.get('Li_nO', []):
        n = ent.get('n')
        agent_list = data.get('Li_nO', [])
        agent = next((a for a in agent_list if a.get('n') == n), None)
        if agent is None:
            if n == 4:
                total += 7
            else:
                total += 5
            continue
        for field, gval in ent.items():
            if field == 'n':
                continue
            total += 1
            t = dist_tol if field in ('d_O_graphene','d_Li_graphene','d_O_Li') else energy_tol
            if field in agent and compare(agent[field], gval, t):
                passed += 1

    # Li_mOH
    for ent in gold.get('Li_mOH', []):
        m = ent.get('m')
        agent_list = data.get('Li_mOH', [])
        agent = next((a for a in agent_list if a.get('m') == m), None)
        if agent is None:
            total += 5
            continue
        for field, gval in ent.items():
            if field in ('m','n'):
                continue
            total += 1
            t = dist_tol if field in ('d_O_graphene','d_Li_graphene','d_O_Li') else energy_tol
            if field in agent and compare(agent[field], gval, t):
                passed += 1

    # binding_energies_O_C_ratios
    for ent in gold.get('binding_energies_O_C_ratios', []):
        cfg = ent.get('config')
        agent_list = data.get('binding_energies_O_C_ratios', [])
        agent = next((a for a in agent_list if a.get('config') == cfg), None)
        if agent is None:
            total += 2
            continue
        for field in ('E_b_Li','E_b_cluster'):
            total += 1
            if field in agent and compare(agent[field], ent[field], energy_tol):
                passed += 1

    # H2_adsorption_Li4O
    for ent in gold.get('H2_adsorption_Li4O', []):
        n_h2 = ent.get('n_H2')
        agent_list = data.get('H2_adsorption_Li4O', [])
        agent = next((a for a in agent_list if a.get('n_H2') == n_h2), None)
        if agent is None:
            total += 1
            continue
        total += 1
        if 'E_ad' in agent and compare(agent['E_ad'], ent['E_ad'], energy_tol):
            passed += 1

    # H2_adsorption_Li3OH
    for ent in gold.get('H2_adsorption_Li3OH', []):
        n_h2 = ent.get('n_H2')
        agent_list = data.get('H2_adsorption_Li3OH', [])
        agent = next((a for a in agent_list if a.get('n_H2') == n_h2), None)
        if agent is None:
            total += 1
            continue
        total += 1
        if 'E_ad' in agent and compare(agent['E_ad'], ent['E_ad'], energy_tol):
            passed += 1

    # HSC_adsorption
    for ent in gold.get('HSC_adsorption', []):
        sys = ent.get('system')
        agent_list = data.get('HSC_adsorption', [])
        agent = next((a for a in agent_list if a.get('system') == sys), None)
        if agent is None:
            total += 2
            continue
        for field in ('E_ad','HSC_wt'):
            total += 1
            if field not in agent:
                continue
            t = energy_tol if field == 'E_ad' else hsc_tol
            if compare(agent[field], ent[field], t):
                passed += 1

    score = passed / total if total > 0 else 0.0
    return score


_SCORERS = {
    'score_results': score_0,
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
