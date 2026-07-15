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


# === block: score_0 (check id='check_adsorption_results') ===
def score_0(artifact, step, ctx):
    w_mg_ads = 0.1
    w_band_gap = 0.1
    w_gas_entry = 0.1
    w_pristine_gas = 0.05
    score_val = 0.0

    # Mg adsorption energy
    mg_val = artifact.get('Mg_adsorption_energy')
    if isinstance(mg_val, (int, float)):
        if abs(mg_val - step['rules'][0]['reference']) <= step['rules'][0]['tolerance']:
            score_val += w_mg_ads

    # Band gap
    gap_val = artifact.get('pristine_C3B_band_gap')
    if isinstance(gap_val, (int, float)):
        if abs(gap_val - step['rules'][1]['reference']) <= step['rules'][1]['tolerance']:
            score_val += w_band_gap

    # gas adsorptions
    gas_ads = artifact.get('gas_adsorptions', [])
    ref_gas_list = step['gas_adsorptions_check']['reference']
    tol_E = step['gas_adsorptions_check']['tolerance_E_ad']
    tol_d = step['gas_adsorptions_check']['tolerance_distance']
    for ref_entry in ref_gas_list:
        match = next((a for a in gas_ads if a.get('molecule') == ref_entry['molecule'] and a.get('configuration') == ref_entry['configuration']), None)
        if match is None:
            continue
        e_ad = match.get('E_ad')
        dist = match.get('distance')
        if isinstance(e_ad, (int, float)) and abs(e_ad - ref_entry['E_ad']) <= tol_E:
            score_val += w_gas_entry * 0.5
        if isinstance(dist, (int, float)) and abs(dist - ref_entry['distance']) <= tol_d:
            score_val += w_gas_entry * 0.5

    # pristine gas adsorptions
    pristine_ads = artifact.get('pristine_gas_adsorptions', [])
    ref_pristine_list = step['pristine_gas_adsorptions_check']['reference']
    tol_p = step['pristine_gas_adsorptions_check']['tolerance_E_ad']
    for ref_entry in ref_pristine_list:
        match = next((a for a in pristine_ads if a.get('molecule') == ref_entry['molecule']), None)
        if match is not None and isinstance(match.get('E_ad'), (int, float)):
            if abs(match['E_ad'] - ref_entry['E_ad']) <= tol_p:
                score_val += w_pristine_gas

    return min(max(score_val, 0.0), 1.0)


_SCORERS = {
    'check_adsorption_results': score_0,
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
