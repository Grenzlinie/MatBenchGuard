import os
import json
import csv

# === author imports / helpers ===
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
    step = None
    for s in spec.get('steps', []):
        if s.get('id') == 'results_check':
            step = s
            break
    if step is None:
        step = {}
    reference = step.get('reference', {})
    dist_tol = step.get('distance_tolerance', 0.02)
    hyd_tol = step.get('hydration_trend_tolerance_3nm', 0.5)
    return {'reference': reference, 'distance_tolerance': dist_tol, 'hydration_trend_tolerance_3nm': hyd_tol}


# === block: score_0 (check id='results_check') ===
def score_0(artifact, step, ctx):
    reference = ctx.get('reference', {})
    dist_tol = ctx.get('distance_tolerance', 0.02)
    hyd_tol = ctx.get('hydration_trend_tolerance_3nm', 0.5)
    if not isinstance(artifact, dict) or 'systems' not in artifact:
        return 0.0
    systems = artifact['systems']
    sys_map = {s.get('name'): s for s in systems if s.get('name')}
    dist_fields = ['water_water_nn_distance', 'Na_water_nn_distance', 'Cl_water_nn_distance']
    total_dist = 0
    passed_dist = 0
    for sys_name, exp in reference.items():
        agent_sys = sys_map.get(sys_name)
        if agent_sys is None:
            continue
        for field in dist_fields:
            ev = exp.get(field)
            av = agent_sys.get(field)
            if ev is not None and av is not None and isinstance(av, (int, float)):
                total_dist += 1
                if abs(av - ev) <= dist_tol:
                    passed_dist += 1
    dist_score = passed_dist / total_dist if total_dist > 0 else 0.0
    bulk = reference.get('bulk', {})
    bulk_Na = bulk.get('Na_hydration_number')
    bulk_Cl = bulk.get('Cl_hydration_number')
    if bulk_Na is None or bulk_Cl is None:
        trend_score = 0.0
    else:
        checks = {
            '1nm_CNT': {
                'Na_hydration_number': lambda v: v < bulk_Na,
                'Cl_hydration_number': lambda v: v < bulk_Cl
            },
            '2nm_CNT': {
                'Na_hydration_number': lambda v: v < bulk_Na,
                'Cl_hydration_number': lambda v: v > bulk_Cl
            },
            '3nm_CNT': {
                'Na_hydration_number': lambda v: abs(v - bulk_Na) <= hyd_tol,
                'Cl_hydration_number': lambda v: abs(v - bulk_Cl) <= hyd_tol
            }
        }
        total_trend = 0
        passed_trend = 0
        for sys_name, fields in checks.items():
            agent_sys = sys_map.get(sys_name)
            if agent_sys is None:
                continue
            for field, func in fields.items():
                val = agent_sys.get(field)
                if val is not None:
                    total_trend += 1
                    if func(val):
                        passed_trend += 1
        trend_score = passed_trend / total_trend if total_trend > 0 else 0.0
    return 0.6 * dist_score + 0.4 * trend_score


_SCORERS = {
    'results_check': score_0,
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
