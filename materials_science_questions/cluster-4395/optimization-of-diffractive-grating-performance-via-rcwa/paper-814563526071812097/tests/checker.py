import os
import json
import csv

# === author imports / helpers ===
import os, json, csv

def load_artifact(path):
    if not os.path.exists(path):
        return None
    if path.endswith('.json'):
        with open(path) as f:
            return json.load(f)
    if path.endswith('.csv'):
        with open(path, newline='') as f:
            return list(csv.DictReader(f))
    with open(path) as f:
        return f.read()


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
    ctx = {}
    for step in spec.get('steps', []):
        if step.get('output_file') == 'designed_hcg_parameters.csv':
            ctx['csv_constraints'] = step.get('constraints', {})
        elif step.get('id') == 'step_sim_angle':
            ctx['angle_gold'] = step.get('gold_value')
            ctx['angle_tol'] = step.get('tolerance')
        elif step.get('id') == 'step_sim_reflectivity':
            ctx['refl_gold'] = step.get('gold_value')
            ctx['refl_min'] = step.get('partial_min')
    return ctx


# === block: score_0 (check id='step_design_csv') ===
def score_0(artifact, step, ctx):
    rows = artifact  # artifact is a list of dicts
    constraints = ctx.get('csv_constraints', {})
    num_bars = constraints.get('num_bars', 14)
    period_min = constraints.get('period_min', 0.6)
    period_max = constraints.get('period_max', 0.9)
    width_min = constraints.get('width_min', 0.2)
    width_max = constraints.get('width_max', 0.7)
    total_width = constraints.get('total_width', 9.66)
    total_width_tol = constraints.get('total_width_tolerance', 0.5)

    if not rows or len(rows) < num_bars + 1:
        return 0.0

    bar_rows = []
    total_row = None
    for row in rows:
        bn = row.get('bar_number', '').strip().lower()
        if bn == 'total_width_um':
            total_row = row
        else:
            try:
                idx = int(bn)
                bar_rows.append(row)
            except:
                pass

    if len(bar_rows) != num_bars:
        return 0.0
    if total_row is None:
        return 0.0

    for row in bar_rows:
        try:
            p = float(row.get('period_um'))
            w = float(row.get('bar_width_um'))
        except (ValueError, TypeError):
            return 0.0
        if not (period_min <= p <= period_max):
            return 0.0
        if not (width_min <= w <= width_max):
            return 0.0

    try:
        tw = float(total_row.get('period_um'))
    except (ValueError, TypeError):
        return 0.0
    if abs(tw - total_width) > total_width_tol:
        return 0.0

    return 1.0


# === block: score_1 (check id='step_sim_angle') ===
def score_1(artifact, step, ctx):
    gold = ctx.get('angle_gold')
    tol = ctx.get('angle_tol', 1.5)
    if gold is None:
        return 0.0
    val = artifact.get('deflection_angle_deg')
    if val is None:
        return 0.0
    try:
        val = float(val)
    except (ValueError, TypeError):
        return 0.0
    if abs(val - gold) <= tol:
        return 1.0
    return 0.0


# === block: score_2 (check id='step_sim_reflectivity') ===
def score_2(artifact, step, ctx):
    gold = ctx.get('refl_gold')
    partial_min = ctx.get('refl_min', 80.0)
    if gold is None:
        return 0.0
    val = artifact.get('reflectivity_pct')
    if val is None:
        return 0.0
    try:
        val = float(val)
    except (ValueError, TypeError):
        return 0.0
    if val >= gold:
        return 1.0
    if val <= partial_min:
        return 0.0
    return (val - partial_min) / (gold - partial_min)


_SCORERS = {
    'step_design_csv': score_0,
    'step_sim_angle': score_1,
    'step_sim_reflectivity': score_2,
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
