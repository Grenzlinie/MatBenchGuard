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
    import csv, os
    repair_path = os.path.join(outputs_dir, 'repairing_process_results.csv')
    remove_path = os.path.join(outputs_dir, 'removing_process_results.csv')
    repair_rows = list(csv.DictReader(open(repair_path, newline='')))
    remove_rows = list(csv.DictReader(open(remove_path, newline='')))
    return {'repair_rows': repair_rows, 'remove_rows': remove_rows}


# === block: score_0 (check id='repairing_numeric') ===
def score_0(artifact, step, ctx):
    rows = ctx['repair_rows']
    reference = step['parameters']['reference']
    tolerances = step['parameters']['tolerances']
    allowed_fields = {'E_ad', 'barrier', 'Hirshfeld_charge_NO'}
    total_fields = 0
    matched = 0
    for row in rows:
        state = row['state'].strip()
        if state not in reference: continue
        ref = reference[state]
        for field, gold in ref.items():
            if gold is None: continue
            if field not in allowed_fields: continue
            if field not in row: continue
            try:
                val = float(row[field])
            except: continue
            tol = tolerances.get(field, tolerances['charge'] if 'charge' in field.lower() else tolerances['E_ad'])
            if abs(val - gold) <= tol:
                matched += 1
            total_fields += 1
    if total_fields == 0: return 0.0
    return matched / total_fields


# === block: score_1 (check id='removing_numeric') ===
def score_1(artifact, step, ctx):
    rows = ctx['remove_rows']
    reference = step['parameters']['reference']
    tolerances = step['parameters']['tolerances']
    total_fields = 0
    matched = 0
    for row in rows:
        state = row['state'].strip()
        if state not in reference: continue
        ref = reference[state]
        # correct Hirshfeld_charge_NO2_total gold from individual charges when available
        corrected_ref = dict(ref)
        if all(k in ref for k in ('Hirshfeld_charge_N2','Hirshfeld_charge_O1','Hirshfeld_charge_O2')):
            corrected_ref['Hirshfeld_charge_NO2_total'] = (
                ref['Hirshfeld_charge_N2'] + ref['Hirshfeld_charge_O1'] + ref['Hirshfeld_charge_O2']
            )
        for field, gold in corrected_ref.items():
            if gold is None: continue
            if field not in row: continue
            try:
                val = float(row[field])
            except: continue
            tol = tolerances.get(field, tolerances['charge'] if 'charge' in field.lower() else tolerances['E_ad'])
            if abs(val - gold) <= tol:
                matched += 1
            total_fields += 1
    if total_fields == 0: return 0.0
    return matched / total_fields


# === block: score_2 (check id='structural_trends') ===
def score_2(artifact, step, ctx):
    repair = ctx['repair_rows']
    remove = ctx['remove_rows']
    fs1_e = None
    ts1_bar = None
    for r in repair:
        s = r['state'].strip()
        if s == 'FS1':
            try: fs1_e = float(r['E_ad'])
            except: pass
        elif s == 'TS1':
            try: ts1_bar = float(r['barrier'])
            except: pass
    ts2_bar = None
    fs2_e = None
    for r in remove:
        s = r['state'].strip()
        if s == 'TS2':
            try: ts2_bar = float(r['barrier'])
            except: pass
        elif s == 'FS2':
            try: fs2_e = float(r['E_ad'])
            except: pass
    c1 = fs1_e is not None and fs1_e < -6.5
    c2 = ts1_bar is not None and ts2_bar is not None and ts1_bar > ts2_bar
    c3 = fs2_e is not None and fs2_e > -0.50
    return (c1 + c2 + c3) / 3.0


_SCORERS = {
    'repairing_numeric': score_0,
    'removing_numeric': score_1,
    'structural_trends': score_2,
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
