import os
import json
import csv

# === author imports / helpers ===
import csv, re, math


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
    steps = spec['steps']
    ctx = {}
    for step in steps:
        if step['id'] == 'step01':
            ctx['step01_ref'] = step['reference_values']['rows']
            ctx['step01_tol'] = step['tolerance']
            ctx['step01_weights'] = step['sub_weights']
        elif step['id'] == 'step02':
            ctx['step02_ref'] = step['reference_lines']
            ctx['step02_tol_abs'] = step['tolerance_abs']
    return ctx


# === block: score_0 (check id='step01') ===
def score_0(artifact, step, ctx):
    ref_rows = ctx['step01_ref']
    tol = ctx['step01_tol']
    weights = ctx['step01_weights']
    fields = ['V_l','V_s','V_m','theta']
    ref_by_comp = {row['composition']: row for row in ref_rows}
    row_scores = []
    for ref_comp, ref_row in sorted(ref_by_comp.items()):
        art_row = None
        for row in artifact:
            if row.get('composition','').strip() == ref_comp:
                art_row = row
                break
        if art_row is None:
            row_scores.append(0.0)
            continue
        field_scores = []
        for f in fields:
            val = float(art_row.get(f, 0))
            ref_val = float(ref_row.get(f, 0))
            if ref_val == 0:
                score = 1.0 if abs(val) < tol.get('abs_for_zeros',1) else 0.0
            else:
                if abs(val - ref_val) / abs(ref_val) <= tol['relative']:
                    score = 1.0
                else:
                    score = 0.0
            field_scores.append(score)
        row_score = sum(weights[f] * s for f,s in zip(fields, field_scores))
        row_scores.append(row_score)
    if row_scores:
        total = sum(row_scores) / len(row_scores)
    else:
        total = 0.0
    return total


# === block: score_1 (check id='step02') ===
def score_1(artifact, step, ctx):
    refs = ctx['step02_ref']
    tol = ctx['step02_tol_abs']
    lines = artifact.strip().splitlines()
    matches = 0
    for entry in refs:
        pair = entry['pair']
        expect = entry['percent']
        found = False
        for line in lines:
            if pair.lower() in line.lower():
                nums = re.findall(r'[\d.]+', line)
                for num_str in nums:
                    try:
                        val = float(num_str)
                        if abs(val - expect) <= tol:
                            matches += 1
                            found = True
                            break
                    except:
                        continue
                if found:
                    break
    return matches / len(refs)


_SCORERS = {
    'step01': score_0,
    'step02': score_1,
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
