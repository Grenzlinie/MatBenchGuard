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
    import json
    import csv
    import os

    def prepare(outputs_dir, spec):
        steps = spec.get('steps', [])
        ctx = {}
        for step in steps:
            if step.get('id') == 'pointwise_check':
                ctx['ref_temps'] = step.get('reference_temperatures', [])
                ctx['ref_p'] = step.get('reference_p_I2_mbar', [])
                ctx['tolerance'] = step.get('tolerance_relative', 0.10)
            elif step.get('id') == 'structural_check':
                ctx['threshold'] = step.get('threshold', 0.04)
                ctx['temp_range'] = step.get('threshold_temperature_range', [110, 130])
                ctx['expected_max'] = step.get('expected_max', 0.10)
                ctx['max_tol'] = step.get('max_tolerance_relative', 0.20)
        return ctx


# === block: score_0 (check id='pointwise_check') ===
def score_0(artifact, step, ctx):
    import csv
    import os

    def score(artifact, step, ctx):
        agent_data = artifact  # list of dicts
        # Build lookup from temperature (C) to p_I2
        agent_map = {}
        for row in agent_data:
            try:
                t = float(row['temperature_C'])
                p = float(row['p_I2_mbar'])
            except (KeyError, ValueError):
                continue
            agent_map[t] = p
        ref_temps = ctx.get('ref_temps', [])
        ref_p = ctx.get('ref_p', [])
        tolerance = ctx.get('tolerance', 0.10)
        if not ref_temps:
            return 0.0
        passed = 0
        for i, t_ref in enumerate(ref_temps):
            p_ref = ref_p[i] if i < len(ref_p) else None
            if p_ref is None:
                continue
            if t_ref in agent_map:
                p_agent = agent_map[t_ref]
                rel_err = abs(p_agent - p_ref) / max(abs(p_ref), 1e-12)
                if rel_err <= tolerance:
                    passed += 1
        total = len(ref_temps)
        if total == 0:
            return 0.0
        return passed / total


# === block: score_1 (check id='structural_check') ===
def score_1(artifact, step, ctx):
    import csv
    import os

    def score(artifact, step, ctx):
        agent_data = artifact
        threshold = ctx.get('threshold', 0.04)
        t_low, t_high = ctx.get('temp_range', [110, 130])
        expected_max = ctx.get('expected_max', 0.10)
        max_tol = ctx.get('max_tol', 0.20)
    
        temps = []
        p_vals = []
        for row in agent_data:
            try:
                t = float(row['temperature_C'])
                p = float(row['p_I2_mbar'])
                temps.append(t)
                p_vals.append(p)
            except (KeyError, ValueError):
                continue
        if not p_vals:
            return 0.0
        # Check threshold crossing range
        crossing_ok = True
        for t, p in zip(temps, p_vals):
            if p > threshold:
                if t < t_low or t > t_high:
                    crossing_ok = False
                    break
        # Check max value
        max_p = max(p_vals)
        max_err = abs(max_p - expected_max) / max(abs(expected_max), 1e-12)
        max_ok = max_err <= max_tol
    
        score_val = 0.0
        if crossing_ok:
            score_val += 0.5
        if max_ok:
            score_val += 0.5
        return score_val


_SCORERS = {
    'pointwise_check': score_0,
    'structural_check': score_1,
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
