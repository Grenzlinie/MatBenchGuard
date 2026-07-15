import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    return {'spec': spec}


# === block: score_0 (check id='step_01_band_properties') ===
def score_0(artifact, step, ctx):
    ref = step['reference']['cases']
    tols = step.get('tolerances', {})
    if not artifact:
        return 0.0
    rows_by_case = {row.get('case',''): row for row in artifact}
    score_sum = 0.0
    for c in ref:
        row = rows_by_case.get(c['case'])
        if not row:
            continue
        eg_ok = abs(float(row.get('Eg',float('nan'))) - c['Eg']) <= tols.get('Eg',0.1)
        cbm_ok = abs(float(row.get('CBM_vacuum',float('nan'))) - c['CBM_vacuum']) <= tols.get('CBM_vacuum',0.1)
        vbm_ok = abs(float(row.get('VBM_vacuum',float('nan'))) - c['VBM_vacuum']) <= tols.get('VBM_vacuum',0.1)
        type_ok = row.get('band_type','') == c['band_type']
        num_score = (1.0*eg_ok + 1.0*cbm_ok + 1.0*vbm_ok) / 3.0
        row_score = num_score * 0.9 + (1.0 if type_ok else 0.0) * 0.1
        score_sum += row_score
    return score_sum / max(1, len(ref))


# === block: score_1 (check id='step_02_oer_thermodynamics') ===
def score_1(artifact, step, ctx):
    ref = step['reference']['cases']
    tols = step.get('tolerances', {})
    if not artifact:
        return 0.0
    rows_by_case = {row.get('case',''): row for row in artifact}
    def _str_to_bool(val):
        if isinstance(val, bool):
            return val
        return str(val).strip().lower() in ('true','1','yes')
    score_sum = 0.0
    for c in ref:
        row = rows_by_case.get(c['case'])
        if not row:
            continue
        pds0_ok = abs(float(row.get('PDS_pH0',float('nan'))) - c['PDS_pH0']) <= tols.get('PDS_pH0',0.1)
        edf0_ok = abs(float(row.get('EDF_pH0',float('nan'))) - c['EDF_pH0']) <= tols.get('EDF_pH0',0.1)
        feas0_ok = _str_to_bool(row.get('feasible_pH0')) == c['feasible_pH0']
        pds7_ok = abs(float(row.get('PDS_pH7',float('nan'))) - c['PDS_pH7']) <= tols.get('PDS_pH7',0.1)
        edf7_ok = abs(float(row.get('EDF_pH7',float('nan'))) - c['EDF_pH7']) <= tols.get('EDF_pH7',0.1)
        feas7_ok = _str_to_bool(row.get('feasible_pH7')) == c['feasible_pH7']
        pH0_num = (1.0*pds0_ok + 1.0*edf0_ok) / 2.0
        pH0_score = pH0_num * 0.8 + (1.0 if feas0_ok else 0.0) * 0.2
        pH7_num = (1.0*pds7_ok + 1.0*edf7_ok) / 2.0
        pH7_score = pH7_num * 0.8 + (1.0 if feas7_ok else 0.0) * 0.2
        row_score = (pH0_score + pH7_score) / 2.0
        score_sum += row_score
    return score_sum / max(1, len(ref))


_SCORERS = {
    'step_01_band_properties': score_0,
    'step_02_oer_thermodynamics': score_1,
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
