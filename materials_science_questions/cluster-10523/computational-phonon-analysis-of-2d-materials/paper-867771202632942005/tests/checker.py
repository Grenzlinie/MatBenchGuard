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


# === block: score_0 (check id='step_02_value_match') ===
def score_0(artifact, step, ctx):
    csv_data = artifact
    gold = step['config']['gold']
    sw_tol_rel = step['config']['spectral_weight_tol_relative']
    sw_tol_abs = step['config']['spectral_weight_tol_absolute']
    fs_tol_abs = step['config']['frequency_shift_tol_absolute']

    gold_by_doping = {entry['doping']: entry for entry in gold}
    scores = []
    for row in csv_data:
        doping = int(float(row['doping']))
        if doping not in gold_by_doping:
            continue
        gold_entry = gold_by_doping[doping]
        sw_val = float(row['spectral_weight'])
        fs_val = float(row['frequency_shift'])
        sw_ref = gold_entry['spectral_weight']
        if sw_ref == 0:
            sw_tol = sw_tol_abs
        else:
            sw_tol = max(sw_tol_rel * abs(sw_ref), sw_tol_abs)
        sw_pass = abs(sw_val - sw_ref) <= sw_tol
        fs_ref = gold_entry['frequency_shift']
        fs_pass = abs(fs_val - fs_ref) <= fs_tol_abs
        scores.append(0.5 * float(sw_pass) + 0.5 * float(fs_pass))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_02_trend') ===
def score_1(artifact, step, ctx):
    csv_data = artifact
    rows = sorted(csv_data, key=lambda r: float(r['doping']))
    if len(rows) < 2:
        return 1.0
    diffs_sw = [float(rows[i+1]['spectral_weight']) - float(rows[i]['spectral_weight']) for i in range(len(rows)-1)]
    diffs_fs = [float(rows[i+1]['frequency_shift']) - float(rows[i]['frequency_shift']) for i in range(len(rows)-1)]
    sw_ok = all(d >= 0 for d in diffs_sw)
    fs_ok = all(d <= 0 for d in diffs_fs)
    score = 0.0
    if sw_ok:
        score += 0.5
    if fs_ok:
        score += 0.5
    return score


_SCORERS = {
    'step_02_value_match': score_0,
    'step_02_trend': score_1,
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
