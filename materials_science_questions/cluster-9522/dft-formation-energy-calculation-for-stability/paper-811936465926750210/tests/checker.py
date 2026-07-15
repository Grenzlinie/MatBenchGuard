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


# === block: score_0 (check id='dft_formation_check') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # list of dicts
    gold = step['params']['gold']['compounds']
    tol_fe = step['params']['tolerances']['formation_energy_kJ_per_mol']
    tol_latt = step['params']['tolerances']['lattice_relative']

    def score_numeric(val, gold_val, abs_tol, max_extra=None):
        if max_extra is None:
            max_extra = abs_tol * 5
        err = abs(val - gold_val)
        if err <= abs_tol:
            return 1.0
        if max_extra <= abs_tol:
            return 0.0
        return max(0.0, 1.0 - (err - abs_tol) / (max_extra - abs_tol))

    # Build lookup
    rows_by_compound = {}
    for row in artifact:
        name = (row.get('compound', '') or '').strip()
        if name:
            rows_by_compound[name.lower()] = row

    scores = []
    for comp_name, comp_gold in gold.items():
        row = rows_by_compound.get(comp_name.lower())
        if row is None:
            scores.append(0.0)
            continue
        comp_scores = []
        # formation energy
        try:
            fe_val = float(row.get('formation_energy_kJ_per_mol', 0.0))
        except (ValueError, TypeError):
            fe_val = 0.0
        comp_scores.append(score_numeric(fe_val, comp_gold['formation_energy_kJ_per_mol'], tol_fe, 10.0))
        # lattice constants
        for key in ['a_Ang', 'b_Ang', 'c_Ang']:
            if key not in comp_gold:
                continue
            try:
                lat_val = float(row.get(key, -999))
            except (ValueError, TypeError):
                lat_val = -999
            gold_lat = comp_gold[key]
            abs_tol_lat = abs(gold_lat) * tol_latt
            max_extra_lat = abs(gold_lat) * 0.1
            comp_scores.append(score_numeric(lat_val, gold_lat, abs_tol_lat, max_extra_lat))
        if comp_scores:
            scores.append(sum(comp_scores) / len(comp_scores))
        else:
            scores.append(0.0)

    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='calphad_check') ===
def score_1(artifact, step, ctx):
    rows = artifact  # list of dicts
    gold = step['params']['gold']['properties']
    tol_T = step['params']['tolerances']['liquidus_T']
    tol_a = step['params']['tolerances']['a_As']

    def score_value(val, gold_val, abs_tol, max_extra=None):
        if max_extra is None:
            max_extra = abs_tol * 3
        err = abs(val - gold_val)
        if err <= abs_tol:
            return 1.0
        if max_extra <= abs_tol:
            return 0.0
        return max(0.0, 1.0 - (err - abs_tol) / (max_extra - abs_tol))

    props = {}
    for row in rows:
        prop = (row.get('property', '') or '').strip()
        if prop:
            props[prop] = row

    scores = []
    for prop_name, prop_gold in gold.items():
        row = props.get(prop_name)
        if row is None:
            scores.append(0.0)
            continue
        try:
            val = float(row.get('value', 0.0))
        except (ValueError, TypeError):
            val = 0.0
        if 'a_As' in prop_name:
            scores.append(score_value(val, prop_gold['value'], tol_a, 0.09))
        else:
            scores.append(score_value(val, prop_gold['value'], tol_T, 90.0))

    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'dft_formation_check': score_0,
    'calphad_check': score_1,
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
