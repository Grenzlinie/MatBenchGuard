import os
import json
import csv

# === author imports / helpers ===
import json
import os


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


# === block: score_0 (check id='step_08') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold')
    if not gold or not isinstance(artifact, dict):
        return 0.0
    tolerances = step.get('tolerances', {})
    tol_e = tolerances.get('electronic_energy', 1.0)
    tol_zpe = tolerances.get('zpe_energy', 1.5)
    tol_d = tolerances.get('distance', 0.05)
    tol_angle = tolerances.get('angle', 2.0)

    def within_tol(val, expected, tol):
        try:
            return abs(float(val) - float(expected)) <= tol + 1e-12
        except (ValueError, TypeError):
            return False

    total = 0
    correct = 0

    # cluster 2 energies
    c2 = artifact.get('cluster_2', {})
    for state in ['physisorbed','transition','chemisorbed']:
        st = c2.get(state, {})
        for key in ['electronic_energy_rel_kcal_mol','zpe_corrected_energy_rel_kcal_mol']:
            exp = gold.get('cluster_2', {}).get(state, {}).get(key)
            if exp is None:
                continue
            total += 1
            agent_val = st.get(key)
            tol = tol_e if 'electronic' in key else tol_zpe
            if within_tol(agent_val, exp, tol):
                correct += 1
    # cluster 2 geometry
    for key in ['transition_AlH_Angstrom','transition_OH_Angstrom']:
        exp = gold.get('cluster_2', {}).get(key)
        if exp is not None:
            total += 1
            agent_val = c2.get(key)
            if within_tol(agent_val, exp, tol_d):
                correct += 1
    exp_angle = gold.get('cluster_2', {}).get('chemisorbed_dihedral_O1_O2_Al_Ob_deg')
    if exp_angle is not None:
        total += 1
        agent_val = c2.get('chemisorbed_dihedral_O1_O2_Al_Ob_deg')
        if within_tol(agent_val, exp_angle, tol_angle):
            correct += 1

    # cluster 3
    c3 = artifact.get('cluster_3', {})
    for state in ['physisorbed','transition','chemisorbed']:
        st = c3.get(state, {})
        for key in ['electronic_energy_rel_kcal_mol','zpe_corrected_energy_rel_kcal_mol']:
            exp = gold.get('cluster_3', {}).get(state, {}).get(key)
            if exp is None:
                continue
            total += 1
            agent_val = st.get(key)
            tol = tol_e if 'electronic' in key else tol_zpe
            if within_tol(agent_val, exp, tol):
                correct += 1

    # cluster 9
    c9 = artifact.get('cluster_9', {})
    for state in ['physisorbed','transition','chemisorbed']:
        st = c9.get(state, {})
        for key in ['electronic_energy_rel_kcal_mol','zpe_corrected_energy_rel_kcal_mol']:
            exp = gold.get('cluster_9', {}).get(state, {}).get(key)
            if exp is None:
                continue
            total += 1
            agent_val = st.get(key)
            tol = tol_e if 'electronic' in key else tol_zpe
            if within_tol(agent_val, exp, tol):
                correct += 1

    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    'step_08': score_0,
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
