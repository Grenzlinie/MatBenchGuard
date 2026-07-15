import os
import json
import csv

# === author imports / helpers ===
import csv
import math


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
    enthalpies_path = os.path.join(outputs_dir, 'step_03_enthalpies.csv')
    enthalpies = []
    with open(enthalpies_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            enthalpies.append(row)
    # extract experimental enthalpies from summary_recompute step config
    steps = spec.get('steps', [])
    expt = {}
    for step in steps:
        if step.get('id') == 'summary_recompute':
            expt = step.get('experimental_enthalpies', {})
            break
    return {'enthalpies': enthalpies, 'expt': expt}


# === block: score_0 (check id='enthalpies_corrected') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold_values', {})
    tol = step.get('tolerance_abs', 3.0)
    total = 0
    ok = 0
    for row in artifact:
        if row.get('enthalpy_type') != 'corrected':
            continue
        species = row.get('species', '')
        method = row.get('method', '')
        try:
            val = float(row.get('delta_H', ''))
        except:
            continue
        if method in gold and species in gold[method]:
            total += 1
            if abs(val - gold[method][species]) <= tol:
                ok += 1
    if total == 0:
        return 0.0
    return ok / total


# === block: score_1 (check id='enthalpies_uncorrected') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold_values', {})
    tol = step.get('tolerance_abs', 5.0)
    total = 0
    ok = 0
    for row in artifact:
        if row.get('enthalpy_type') != 'uncorrected':
            continue
        species = row.get('species', '')
        method = row.get('method', '')
        try:
            val = float(row.get('delta_H', ''))
        except:
            continue
        if method in gold and species in gold[method]:
            total += 1
            if abs(val - gold[method][species]) <= tol:
                ok += 1
    if total == 0:
        return 0.0
    return ok / total


# === block: score_2 (check id='summary_recompute') ===
def score_2(artifact, step, ctx):
    # recompute RMS and mean from corrected enthalpies in ctx
    corrected = {}
    for row in ctx['enthalpies']:
        if row.get('enthalpy_type') != 'corrected':
            continue
        method = row.get('method', '')
        species = row.get('species', '')
        if method not in corrected:
            corrected[method] = {}
        corrected[method][species] = float(row.get('delta_H', 0))
    # compute rms, avg
    import math
    results = {}
    for method, sp_vals in corrected.items():
        errs = []
        for sp, val in sp_vals.items():
            if sp in ctx['expt']:
                errs.append(val - ctx['expt'][sp])
        if errs:
            n = len(errs)
            rms = math.sqrt(sum(e*e for e in errs) / n)
            avg = sum(errs) / n
            results[method] = {'rms': rms, 'avg': avg}
    gold_summary = step.get('gold_values', {})
    tol = step.get('tolerance_abs', 2.0)
    good = 0
    for method in ['G2', 'G2(MP2)', 'CBS-4', 'CBS-Q']:
        if method not in results or method not in gold_summary:
            continue
        rms_ok = abs(results[method]['rms'] - gold_summary[method]['rms_deviation']) <= tol
        avg_ok = abs(results[method]['avg'] - gold_summary[method]['avg_deviation']) <= tol
        if rms_ok and avg_ok:
            good += 1
    return good / 4.0


# === block: score_3 (check id='summary_validity') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    required_cols = {'method', 'enthalpy_type', 'rms_deviation', 'avg_deviation'}
    if not required_cols.issubset(set(artifact[0].keys())):
        return 0.0
    methods = set(row.get('method', '') for row in artifact)
    expected_methods = {'G2', 'G2(MP2)', 'CBS-4', 'CBS-Q'}
    if expected_methods.issubset(methods):
        return 1.0
    return 0.5


_SCORERS = {
    'enthalpies_corrected': score_0,
    'enthalpies_uncorrected': score_1,
    'summary_recompute': score_2,
    'summary_validity': score_3,
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
