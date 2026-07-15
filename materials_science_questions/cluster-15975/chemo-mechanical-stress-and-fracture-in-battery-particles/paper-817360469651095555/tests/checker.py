import os
import json
import csv

# === author imports / helpers ===
import math, csv


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
        step_id = step.get('id')
        if step_id:
            ctx[step_id] = step.get('params', {})
    return ctx


# === block: score_0 (check id='kmc_depletion') ===
def score_0(artifact, step, ctx):
    secondary_y_min, secondary_y_max = ctx['kmc_depletion'].get('secondary_y_range', [26.5, 33.5])
    min_diff = ctx['kmc_depletion'].get('min_occupancy_diff', 0.01)
    sec_vals = []
    bulk_vals = []
    for row in artifact:
        try:
            y = float(row['y'])
            occ = float(row['occupancy'])
        except (ValueError, KeyError):
            return 0.0
        if secondary_y_min <= y <= secondary_y_max:
            sec_vals.append(occ)
        else:
            bulk_vals.append(occ)
    if len(sec_vals) == 0 or len(bulk_vals) == 0:
        return 0.0
    avg_sec = sum(sec_vals) / len(sec_vals)
    avg_bulk = sum(bulk_vals) / len(bulk_vals)
    diff = avg_bulk - avg_sec
    return 1.0 if diff >= min_diff else 0.0


# === block: score_1 (check id='fem_stress_gradient') ===
def score_1(artifact, step, ctx):
    centers = ctx['fem_stress_gradient'].get('inclusion_centers', [[480,420],[330,150],[120,330]])
    near_radius = ctx['fem_stress_gradient'].get('near_radius', 30.0)
    far_min = ctx['fem_stress_gradient'].get('far_min_distance', 150.0)
    min_diff_MPa = ctx['fem_stress_gradient'].get('min_diff_MPa', 0.05)
    near_stress = []
    far_stress = []
    for row in artifact:
        try:
            x = float(row['x'])
            y = float(row['y'])
            stress = float(row['hydrostatic_stress'])
        except (ValueError, KeyError):
            return 0.0
        d = min(math.hypot(x - cx, y - cy) for cx, cy in centers)
        if d <= near_radius:
            near_stress.append(stress)
        elif d >= far_min:
            far_stress.append(stress)
    if len(near_stress) == 0 or len(far_stress) == 0:
        return 0.0
    mean_near = sum(near_stress) / len(near_stress)
    mean_far = sum(far_stress) / len(far_stress)
    return 1.0 if abs(mean_near - mean_far) >= min_diff_MPa else 0.0


# === block: score_2 (check id='fem_potential_gradient') ===
def score_2(artifact, step, ctx):
    centers = ctx['fem_potential_gradient'].get('inclusion_centers', [[480,420],[330,150],[120,330]])
    near_radius = ctx['fem_potential_gradient'].get('near_radius', 30.0)
    far_min = ctx['fem_potential_gradient'].get('far_min_distance', 150.0)
    min_diff_V = ctx['fem_potential_gradient'].get('min_diff_V', 0.0005)
    near_pot = []
    far_pot = []
    for row in artifact:
        try:
            x = float(row['x'])
            y = float(row['y'])
            pot = float(row['electric_potential'])
        except (ValueError, KeyError):
            return 0.0
        d = min(math.hypot(x - cx, y - cy) for cx, cy in centers)
        if d <= near_radius:
            near_pot.append(pot)
        elif d >= far_min:
            far_pot.append(pot)
    if len(near_pot) == 0 or len(far_pot) == 0:
        return 0.0
    mean_near = sum(near_pot) / len(near_pot)
    mean_far = sum(far_pot) / len(far_pot)
    return 1.0 if abs(mean_near - mean_far) >= min_diff_V else 0.0


_SCORERS = {
    'kmc_depletion': score_0,
    'fem_stress_gradient': score_1,
    'fem_potential_gradient': score_2,
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
