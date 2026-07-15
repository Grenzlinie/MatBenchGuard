import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    step = next(s for s in spec['steps'] if s['id'] == 'step_scored')
    return {
        'gold': step['gold_values'],
        'rxn_tol': step['tolerances']['reaction_energy_upper_abs_eV'],
        'shift_tol': step['tolerances']['adsorption_shift_upper_abs_eV']
    }


# === block: score_0 (check id='step_scored') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold']
    req = {'C1_vacuum_eV','C2_vacuum_eV','C1_with_cations_eV','C2_with_cations_eV','OCCO_adsorption_shift_eV','2CO_adsorption_shift_eV','OCCOH_adsorption_shift_eV'}
    if not isinstance(artifact, dict) or not req.issubset(artifact.keys()):
        return 0.0

    # tolerance check (lower is better) – binary per field
    rxn_keys = ['C1_vacuum_eV','C2_vacuum_eV','C1_with_cations_eV','C2_with_cations_eV']
    shift_keys = ['OCCO_adsorption_shift_eV','2CO_adsorption_shift_eV','OCCOH_adsorption_shift_eV']

    pass_count = 0
    for k in rxn_keys:
        if artifact[k] <= gold[k] + ctx['rxn_tol']:
            pass_count += 1
    for k in shift_keys:
        if artifact[k] <= gold[k] + ctx['shift_tol']:
            pass_count += 1
    abs_score = pass_count / 7.0

    # structural ordering checks
    order_ok = 0.0
    C2 = artifact['C2_with_cations_eV']
    C1c = artifact['C1_with_cations_eV']
    C1v = artifact['C1_vacuum_eV']
    OCCO = artifact['OCCO_adsorption_shift_eV']
    OCCOH = artifact['OCCOH_adsorption_shift_eV']
    CO2 = artifact['2CO_adsorption_shift_eV']
    if C2 < C1c:
        order_ok += 1.0
    if C1c < C1v:   # cation route more favourable than vacuum
        order_ok += 1.0
    if abs(OCCO) > abs(OCCOH) > abs(CO2):
        order_ok += 1.0
    struct_score = order_ok / 3.0

    return 0.6 * abs_score + 0.4 * struct_score


_SCORERS = {
    'step_scored': score_0,
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
