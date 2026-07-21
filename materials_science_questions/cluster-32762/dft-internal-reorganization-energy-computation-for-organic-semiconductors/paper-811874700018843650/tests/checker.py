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
    step = spec["steps"][0]
    gold_molecules = step["gold_molecules"]
    return {"gold_molecules": gold_molecules}


# === block: score_0 (check id='reorganization_energy_check') ===
def score_0(artifact, step, ctx):
    gold_map = ctx["gold_molecules"]
    tolerance = 0.01
    ev_per_ha = 27.2114

    molecules_list = artifact.get("molecules", [])
    if not molecules_list:
        return 0.0

    total_mols = len(gold_map)
    count_within_tol = 0
    all_below_02 = True

    for mol_entry in molecules_list:
        name = mol_entry.get("molecule", "")
        if name not in gold_map:
            continue
        try:
            e0_q0 = float(mol_entry["E0_Q0"])
            e0_qplus = float(mol_entry["E0_Qplus"])
            eplus_q0 = float(mol_entry["Eplus_Q0"])
            eplus_qplus = float(mol_entry["Eplus_Qplus"])
            e0_qminus = float(mol_entry["E0_Qminus"])
            eminus_q0 = float(mol_entry["Eminus_Q0"])
            eminus_qminus = float(mol_entry["Eminus_Qminus"])
        except (KeyError, ValueError):
            continue
        lambda_plus_ha = (e0_qplus - e0_q0) + (eplus_q0 - eplus_qplus)
        lambda_minus_ha = (e0_qminus - e0_q0) + (eminus_q0 - eminus_qminus)
        lambda_plus_ev = lambda_plus_ha * ev_per_ha
        lambda_minus_ev = lambda_minus_ha * ev_per_ha
        target_plus = gold_map[name]["lambda_plus"]
        target_minus = gold_map[name]["lambda_minus"]
        if abs(lambda_plus_ev - target_plus) <= tolerance and abs(lambda_minus_ev - target_minus) <= tolerance:
            count_within_tol += 1
        if lambda_plus_ev >= 0.2 or lambda_minus_ev >= 0.2:
            all_below_02 = False

    fraction_tol = count_within_tol / total_mols if total_mols > 0 else 0.0
    fraction_threshold = 1.0 if all_below_02 else 0.0
    score = 0.8 * fraction_tol + 0.2 * fraction_threshold
    return score


_SCORERS = {
    'reorganization_energy_check': score_0,
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
