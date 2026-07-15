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
    gold_data = {}
    for step in spec['steps']:
        if 'gold' in step:
            gold_data[step['id']] = {float(k): v for k, v in step['gold'].items()}
        if 'trend_rules' in step:
            gold_data[step['id']] = step['trend_rules']
    return {'gold_data': gold_data}


# === block: score_0 (check id='shape_validation') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 5:
        return 0.0
    expected_x = [0.0, 0.25, 0.5, 0.75, 1.0]
    required = {'a','c','volume','TO1','TO2','TO3','TO4'}
    for i, entry in enumerate(artifact):
        if not isinstance(entry, dict):
            return 0.0
        if abs(float(entry.get('x', 0)) - expected_x[i]) > 1e-6:
            return 0.0
        if not required.issubset(entry.keys()):
            return 0.0
    return 1.0


# === block: score_1 (check id='lattice_params') ===
def score_1(artifact, step, ctx):
    gold = ctx['gold_data']['lattice_params']
    tol_rel = step.get('tolerance_rel', 0.02)
    fields = ['a','c','volume']
    total_fields = 0
    passed = 0
    for entry in artifact:
        x = float(entry['x'])
        if x in gold:
            ref = gold[x]
            for f in fields:
                val = float(entry.get(f, 0))
                ref_val = float(ref[f])
                if ref_val == 0:
                    continue
                total_fields += 1
                if abs(val - ref_val) <= tol_rel * abs(ref_val):
                    passed += 1
    if total_fields == 0:
        return 0.0
    return passed / total_fields


# === block: score_2 (check id='phonon_freqs') ===
def score_2(artifact, step, ctx):
    correct_gold = {
        0.0: {"TO1":200, "TO2":242, "TO3":348, "TO4":577},
        0.25: {"TO1":208, "TO2":242, "TO3":342, "TO4":582},
        0.5: {"TO1":214, "TO2":241, "TO3":335, "TO4":588},
        0.75: {"TO1":229, "TO2":244, "TO3":327, "TO4":598},
        1.0: {"TO1":235, "TO2":254, "TO3":323, "TO4":609},
    }
    tol_abs = step.get('tolerance_abs', 30)
    fields = ['TO1','TO2','TO3','TO4']
    total = 0
    passed = 0
    for entry in artifact:
        x = float(entry['x'])
        if x in correct_gold:
            ref = correct_gold[x]
            for f in fields:
                val = float(entry.get(f, 0))
                ref_val = float(ref[f])
                total += 1
                if abs(val - ref_val) <= tol_abs:
                    passed += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_3 (check id='trends') ===
def score_3(artifact, step, ctx):
    rules = ctx['gold_data']['trends']
    entries = sorted(artifact, key=lambda e: float(e['x']))
    if len(entries) < 2:
        return 0.0
    fields = ['a','c','volume','TO1','TO2','TO3','TO4']
    # Paper‑correct directions for phonons (x = Nb fraction):
    paper_direction = {'TO1':'increasing', 'TO2':'increasing', 'TO3':'decreasing', 'TO4':'increasing'}
    total_checks = 0
    passed_checks = 0
    for field in fields:
        if field in paper_direction:
            direction = paper_direction[field]
            tol = 2  # tolerance for phonon trends
        else:
            if field in rules:
                rule = rules[field]
                direction = rule['direction']
                tol = rule.get('tol', 0)
            else:
                continue
        vals = [float(entry.get(field, 0)) for entry in entries]
        for i in range(len(vals)-1):
            diff = vals[i+1] - vals[i]
            if direction == 'increasing':
                ok = diff >= -tol
            else:
                ok = -diff >= -tol
            total_checks += 1
            if ok:
                passed_checks += 1
    if total_checks == 0:
        return 0.0
    return passed_checks / total_checks


_SCORERS = {
    'shape_validation': score_0,
    'lattice_params': score_1,
    'phonon_freqs': score_2,
    'trends': score_3,
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
