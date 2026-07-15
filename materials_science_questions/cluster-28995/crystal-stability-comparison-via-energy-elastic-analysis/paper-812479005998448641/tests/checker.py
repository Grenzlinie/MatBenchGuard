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


# === block: score_0 (check id='step_01_dft') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    tolerances = step.get('tolerances', {})
    field_weight = step.get('field_weight', 0.8)
    trend_weight = step.get('trend_weight', 0.2)
    materials = ['Be','Mg','Co_NM','Co_FM']
    fields = ['U1','I','U2','xI_over_b']
    correct = 0
    total_fields = 0
    for mat in materials:
        if mat not in artifact:
            return 0.0
        mat_data = artifact[mat]
        mat_gold = gold.get(mat, {})
        for f in fields:
            total_fields += 1
            val = mat_data.get(f)
            if val is None:
                continue
            gold_val = mat_gold.get(f)
            if gold_val is None:
                continue
            tol = tolerances.get(f, {})
            if 'relative' in tol:
                if abs(val - gold_val) <= tol['relative'] * abs(gold_val):
                    correct += 1
            elif 'absolute' in tol:
                if abs(val - gold_val) <= tol['absolute']:
                    correct += 1
    field_score = correct / max(total_fields, 1)
    trend_ok = True
    for mat in materials:
        if mat in artifact:
            u1 = artifact[mat].get('U1')
            u2 = artifact[mat].get('U2')
            if u1 is None or u2 is None or u2 <= u1:
                trend_ok = False
                break
    trend_score = 1.0 if trend_ok else 0.0
    return field_weight * field_score + trend_weight * trend_score


# === block: score_1 (check id='step_02_pfdd') ===
def score_1(artifact, step, ctx):
    gold_rows = step.get('gold', [])
    field_tolerances = step.get('field_tolerances', {})
    field_weight = step.get('field_weight', 0.8)
    trend_weight = step.get('trend_weight', 0.2)
    if not isinstance(artifact, list):
        return 0.0
    row_map = {}
    for row in artifact:
        key = (row.get('material',''), row.get('dislocation_type',''))
        row_map[key] = row
    correct = 0
    total_checks = len(gold_rows) * 3 if gold_rows else 0
    for g in gold_rows:
        key = (g['material'], g['dislocation_type'])
        if key not in row_map:
            continue
        row = row_map[key]
        for field in ['Re','bl','br']:
            val = row.get(field)
            if val is None:
                continue
            gold_val = g.get(field)
            if gold_val is None:
                continue
            tol = field_tolerances.get(field, {})
            if 'absolute' in tol:
                if abs(float(val) - float(gold_val)) <= tol['absolute']:
                    correct += 1
    field_score = correct / max(total_checks, 1) if total_checks > 0 else 0.0
    edge_gt_screw = True
    for mat in ['Mg','Co_FM']:
        edge_key = (mat, 'edge')
        screw_key = (mat, 'screw')
        if edge_key in row_map and screw_key in row_map:
            re_edge = float(row_map[edge_key].get('Re', 0.0))
            re_screw = float(row_map[screw_key].get('Re', 0.0))
            if re_edge <= re_screw:
                edge_gt_screw = False
                break
    trend_score = 1.0 if edge_gt_screw else 0.0
    return field_weight * field_score + trend_weight * trend_score


_SCORERS = {
    'step_01_dft': score_0,
    'step_02_pfdd': score_1,
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
