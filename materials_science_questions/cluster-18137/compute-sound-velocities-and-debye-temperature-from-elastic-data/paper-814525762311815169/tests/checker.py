import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math


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
    spec_steps = spec.get('steps', [])
    step_props = next((s for s in spec_steps if s.get('id') == 'check_properties'), None)
    if step_props:
        gold_data = step_props.get('gold_data', {})
        tolerance_map = step_props.get('tolerance_map', {})
    else:
        gold_data = {}
        tolerance_map = {}

    ni_step = next((s for s in spec_steps if s.get('id') == 'check_Ni_trend'), None)
    pd_step = next((s for s in spec_steps if s.get('id') == 'check_Pd_trend'), None)

    return {
        'gold_data': gold_data,
        'tolerance_map': tolerance_map,
        'ni_step': ni_step,
        'pd_step': pd_step
    }


# === block: score_0 (check id='check_properties') ===
def score_0(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    gold_data = ctx['gold_data']
    tolerance_map = ctx['tolerance_map']
    if not rows or not gold_data:
        return 0.0

    # Build lookup from row composition
    row_by_comp = {}
    for r in rows:
        comp = r.get('composition', '').strip()
        if comp:
            row_by_comp[comp] = r

    scored_cols = [k for k in tolerance_map.keys()]
    all_scores = []

    for comp, gold in gold_data.items():
        row = row_by_comp.get(comp)
        if row is None:
            # missing composition counts as zero for that row
            all_scores.extend([0.0] * len(scored_cols))
            continue
        for col in scored_cols:
            gold_val = gold.get(col)
            if gold_val is None:
                all_scores.append(0.0)
                continue
            try:
                val = float(row.get(col, 0))
            except (TypeError, ValueError):
                all_scores.append(0.0)
                continue

            tol = tolerance_map[col]
            if abs(gold_val) < 1e-12:
                # absolute fallback
                sc = max(0.0, 1.0 - abs(val - gold_val) / (tol * 1.0 if tol > 0 else 1.0))
            else:
                rel_err = abs(val - gold_val) / (tol * abs(gold_val))
                sc = max(0.0, 1.0 - rel_err)
            all_scores.append(sc)

    if not all_scores:
        return 0.0
    return sum(all_scores) / len(all_scores)


# === block: score_1 (check id='check_Ni_trend') ===
def score_1(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    ni_step = ctx.get('ni_step', {})
    if not ni_step:
        return 0.0
    ni_comps = ni_step.get('ni_compositions', [])
    trends = ni_step.get('trend_checks', [])
    if not ni_comps or not trends:
        return 0.0

    comp_vals = {}
    for r in rows:
        comp = r.get('composition', '').strip()
        if comp in ni_comps:
            comp_vals[comp] = r

    # ensure all three compositions present
    if not all(c in comp_vals for c in ni_comps):
        return 0.0

    checks_passed = True
    for t in trends:
        prop = t['property']
        direction = t['direction']
        vals = []
        for c in ni_comps:
            try:
                v = float(comp_vals[c].get(prop, 0))
            except (TypeError, ValueError):
                vals = []
                break
            vals.append(v)
        if len(vals) != 3:
            checks_passed = False
            break
        if direction == 'increasing':
            if not (vals[0] <= vals[1] <= vals[2]):
                checks_passed = False
                break
        elif direction == 'decreasing':
            if not (vals[0] >= vals[1] >= vals[2]):
                checks_passed = False
                break

    return 1.0 if checks_passed else 0.0


# === block: score_2 (check id='check_Pd_trend') ===
def score_2(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    pd_step = ctx.get('pd_step', {})
    if not pd_step:
        return 0.0
    comp_a = pd_step.get('pd_a', '')
    comp_b = pd_step.get('pd_b', '')
    comparisons = pd_step.get('comparisons', [])
    if not comp_a or not comp_b or not comparisons:
        return 0.0

    row_a = None
    row_b = None
    for r in rows:
        c = r.get('composition', '').strip()
        if c == comp_a:
            row_a = r
        elif c == comp_b:
            row_b = r

    if row_a is None or row_b is None:
        return 0.0

    for comp in comparisons:
        prop = comp['property']
        rel = comp['relation']
        try:
            va = float(row_a.get(prop, 0))
            vb = float(row_b.get(prop, 0))
        except (TypeError, ValueError):
            return 0.0
        if rel == '>':
            if not (va > vb):
                return 0.0
        elif rel == '<':
            if not (va < vb):
                return 0.0

    return 1.0


_SCORERS = {
    'check_properties': score_0,
    'check_Ni_trend': score_1,
    'check_Pd_trend': score_2,
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
