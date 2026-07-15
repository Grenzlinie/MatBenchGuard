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


# === block: score_0 (check id='check_u_j') ===
def score_0(artifact, step, ctx):
    params = step.get('params', {})
    gold_rows = params.get('gold_rows', [])
    key_cols = params.get('key_columns', [])
    val_cols = params.get('value_columns', [])
    tols = params.get('tolerances', {})
    if not gold_rows or not key_cols or not val_cols:
        return 0.0
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    artifact_by_key = {}
    for row in artifact:
        k = tuple(row.get(c, '').strip() for c in key_cols)
        artifact_by_key[k] = row
    n_correct = 0
    n_total = len(gold_rows)
    for g in gold_rows:
        k = tuple(str(g.get(c, '')).strip() for c in key_cols)
        row = artifact_by_key.get(k)
        if row is None:
            continue
        ok = True
        for vcol in val_cols:
            try:
                agent_val = float(row.get(vcol))
            except (ValueError, TypeError):
                ok = False
                break
            gold_val = float(g.get(vcol))
            tol = float(tols.get(vcol, 0.0))
            if abs(agent_val - gold_val) > tol + 1e-12:
                ok = False
                break
        if ok:
            n_correct += 1
    return n_correct / max(1, n_total)


# === block: score_1 (check id='check_bandgaps') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    gold_rows = params.get('gold_rows', [])
    key_cols = params.get('key_columns', [])
    val_cols = params.get('value_columns', [])
    tols = params.get('tolerances', {})
    if not gold_rows or not key_cols or not val_cols:
        return 0.0
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    artifact_by_key = {}
    for row in artifact:
        k = tuple(row.get(c, '').strip() for c in key_cols)
        artifact_by_key[k] = row
    n_correct = 0
    n_total = len(gold_rows)
    for g in gold_rows:
        k = tuple(str(g.get(c, '')).strip() for c in key_cols)
        row = artifact_by_key.get(k)
        if row is None:
            continue
        ok = True
        for vcol in val_cols:
            try:
                agent_val = float(row.get(vcol))
            except (ValueError, TypeError):
                ok = False
                break
            gold_val = float(g.get(vcol))
            tol = float(tols.get(vcol, 0.0))
            if abs(agent_val - gold_val) > tol + 1e-12:
                ok = False
                break
        if ok:
            n_correct += 1
    return n_correct / max(1, n_total)


# === block: score_2 (check id='check_defect_formation') ===
def score_2(artifact, step, ctx):
    params = step.get('params', {})
    gold_rows = params.get('gold_rows', [])
    key_cols = params.get('key_columns', [])
    val_cols = params.get('value_columns', [])
    tols = params.get('tolerances', {})
    if not gold_rows or not key_cols or not val_cols:
        return 0.0
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    artifact_by_key = {}
    for row in artifact:
        k = tuple(row.get(c, '').strip() for c in key_cols)
        artifact_by_key[k] = row
    n_correct = 0
    n_total = len(gold_rows)
    for g in gold_rows:
        k = tuple(str(g.get(c, '')).strip() for c in key_cols)
        row = artifact_by_key.get(k)
        if row is None:
            continue
        ok = True
        for vcol in val_cols:
            try:
                agent_val = float(row.get(vcol))
            except (ValueError, TypeError):
                ok = False
                break
            gold_val = float(g.get(vcol))
            tol = float(tols.get(vcol, 0.0))
            if abs(agent_val - gold_val) > tol + 1e-12:
                ok = False
                break
        if ok:
            n_correct += 1
    return n_correct / max(1, n_total)


# === block: score_3 (check id='check_bandgap_ordering') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    params = step.get('params', [])
    if not params:
        return 0.0
    # Build lookup by (material, functional)
    rows = {}
    for r in artifact:
        mat = (r.get('material','') or '').strip()
        func = (r.get('functional','') or '').strip()
        rows[(mat, func)] = r
    n_ok = 0
    n_total = len(params)
    for cond in params:
        mat = cond.get('material','').strip()
        check_str = cond.get('check','')
        # parse: 'PBE+U_eff > PBE+U+J'
        if '>' not in check_str:
            continue
        left_func, right_func = [s.strip() for s in check_str.split('>',1)]
        try:
            v_left = float(rows.get((mat, left_func), {}).get('bandgap'))
            v_right = float(rows.get((mat, right_func), {}).get('bandgap'))
        except (ValueError, TypeError):
            continue
        if v_left > v_right:
            n_ok += 1
    return n_ok / max(1, n_total)


_SCORERS = {
    'check_u_j': score_0,
    'check_bandgaps': score_1,
    'check_defect_formation': score_2,
    'check_bandgap_ordering': score_3,
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
