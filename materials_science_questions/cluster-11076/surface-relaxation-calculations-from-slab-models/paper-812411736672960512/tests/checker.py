import os
import json
import csv

# === author imports / helpers ===
from collections import defaultdict


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
    gold = {}
    for step in spec.get('steps', []):
        rows = step.get('gold_rows')
        if rows:
            gold[step['output_file']] = rows
    return {'gold': gold}


# === block: score_0 (check id='delta_E_numeric') ===
def score_0(artifact, step, ctx):
    gold_rows_all = ctx['gold'].get('delta_E_results.csv', [])
    # Only compare systems for which we have FLAPW gold (Gd(0001))
    gold_rows = [g for g in gold_rows_all if g.get('system') == 'Gd(0001)']
    if not gold_rows:
        return 0.0
    agent_lookup = {}
    for row in artifact:
        key = (row['system'], row['surface_type'])
        agent_lookup[key] = row
    tol_abs = step.get('tol_abs', 1.0)
    tol_rel_pct = step.get('tol_rel_pct', 5)
    total = len(gold_rows)
    pass_count = 0
    for g in gold_rows:
        key = (g['system'], g['surface_type'])
        arow = agent_lookup.get(key)
        if arow is None:
            continue
        # Delta_E_bulk
        ref = g['Delta_E_bulk']
        val = float(arow.get('Delta_E_bulk', 0))
        tol = max(tol_abs, tol_rel_pct / 100.0 * abs(ref))
        ok_bulk = abs(val - ref) <= tol + 1e-12
        # Delta_E_surf
        ref_s = g['Delta_E_surf']
        val_s = float(arow.get('Delta_E_surf', 0))
        tol_s = max(tol_abs, tol_rel_pct / 100.0 * abs(ref_s))
        ok_surf = abs(val_s - ref_s) <= tol_s + 1e-12
        if ok_bulk and ok_surf:
            pass_count += 1
    score = pass_count / total if total > 0 else 0.0
    return score


# === block: score_1 (check id='delta_E_trend') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    n = len(artifact)
    ok = 0
    for row in artifact:
        try:
            d_bulk = float(row['Delta_E_bulk'])
            d_surf = float(row['Delta_E_surf'])
            if d_surf > d_bulk + 1e-12:
                ok += 1
        except (ValueError, KeyError):
            pass
    score = ok / n if n > 0 else 0.0
    return score


# === block: score_2 (check id='J0_numeric') ===
def score_2(artifact, step, ctx):
    gold_rows = ctx['gold'].get('J0_results.csv', [])
    if not gold_rows:
        return 0.0
    agent_lookup = {}
    for row in artifact:
        key = (row['system'], row['surface_type'], row['layer_index'])
        agent_lookup[key] = row
    tol_abs = step.get('tol_abs', 0.5)
    tol_rel_pct = step.get('tol_rel_pct', 10)
    total = len(gold_rows)
    pass_count = 0
    for g in gold_rows:
        key = (g['system'], g['surface_type'], str(g['layer_index']))
        arow = agent_lookup.get(key)
        if arow is None:
            continue
        ref = g['J_R0']
        val = float(arow.get('J_R0', 0))
        tol = max(tol_abs, tol_rel_pct / 100.0 * abs(ref))
        ok = abs(val - ref) <= tol + 1e-12
        if ok:
            pass_count += 1
    score = pass_count / total if total > 0 else 0.0
    return score


# === block: score_3 (check id='J0_structural') ===
def score_3(artifact, step, ctx):
    from collections import defaultdict
    if not artifact:
        return 0.0
    groups = defaultdict(list)
    for row in artifact:
        key = (row['system'], row['surface_type'])
        try:
            layer = int(row['layer_index'])
            jval = float(row['J_R0'])
            groups[key].append((layer, jval))
        except (ValueError, KeyError):
            pass
    total_groups = len(groups)
    if total_groups == 0:
        return 0.0
    pass_groups = 0
    for key, items in groups.items():
        top_val = None
        others = []
        for l, v in items:
            if l == 0:
                top_val = v
            else:
                others.append(v)
        if top_val is None or not others:
            pass_groups += 1
            continue
        max_other = max(others)
        if top_val < max_other + 1e-12:
            pass_groups += 1
    score = pass_groups / total_groups
    return score


_SCORERS = {
    'delta_E_numeric': score_0,
    'delta_E_trend': score_1,
    'J0_numeric': score_2,
    'J0_structural': score_3,
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
