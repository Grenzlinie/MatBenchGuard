import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    return {"steps_gold": {s["id"]: s for s in spec["steps"]}}


# === block: score_0 (check id='drift_velocity') ===
def score_0(artifact, step, ctx):
    # Extract gold and config from ctx
    step = ctx["steps_gold"][step["id"]]
    gold_fields = step["gold_fields"]
    gold_velocities = step["gold_velocities"]
    tol = step["tolerance_relative"]
    range = step["overshoot_field_range"]
    min_peak = step["min_peak_velocity"]
    max_peak = step["max_peak_velocity"]

    # Read agent CSV
    rows = list(csv.DictReader(open(os.path.join("/app/outputs", step["output_file"]))))
    fields = [float(r["electric_field_kV_cm"]) for r in rows]
    vels = [float(r["drift_velocity_cm_s"]) for r in rows]
    fdict = dict(zip(fields, vels))

    point_scores = []
    for gf, gv in zip(gold_fields, gold_velocities):
        if gf in fdict:
            av = fdict[gf]
        else:
            closest_f = min(fields, key=lambda x: abs(x - gf))
            if abs(closest_f - gf) <= 0.1:
                av = fdict[closest_f]
            else:
                point_scores.append(0.0)
                continue
        err = abs(av - gv) / (abs(gv) + 1e-9)
        if err <= tol:
            point_scores.append(1.0)
        else:
            point_scores.append(max(0.0, 1.0 - (err - tol) / tol))

    avg = sum(point_scores) / len(point_scores) if point_scores else 0.0

    # Overshoot peak structural check
    peak_f = max(fdict, key=lambda f: fdict[f])
    peak_v = fdict[peak_f]
    peak_ok = (range[0] <= peak_f <= range[1] and min_peak <= peak_v <= max_peak)
    if not peak_ok:
        avg *= 0.5

    return avg


# === block: score_1 (check id='device_iv') ===
def score_1(artifact, step, ctx):
    # Extract gold and config from ctx
    step = ctx["steps_gold"][step["id"]]
    gold_voltages = step["gold_voltages"]
    gold_currents = step["gold_currents"]
    tol = step["tolerance_relative"]

    rows = list(csv.DictReader(open(os.path.join("/app/outputs", step["output_file"]))))
    voltages = [float(r["bias_voltage_V"]) for r in rows]
    currents = [float(r["current_density_A_cm2"]) for r in rows]
    vdict = dict(zip(voltages, currents))

    point_scores = []
    for gv, gc in zip(gold_voltages, gold_currents):
        if gv in vdict:
            ac = vdict[gv]
        else:
            closest_v = min(voltages, key=lambda x: abs(x - gv))
            if abs(closest_v - gv) <= 0.1:
                ac = vdict[closest_v]
            else:
                point_scores.append(0.0)
                continue
        denom = abs(gc) if gc != 0 else 1.0
        err = abs(ac - gc) / (denom + 1e-9)
        if err <= tol:
            point_scores.append(1.0)
        else:
            point_scores.append(max(0.0, 1.0 - (err - tol) / tol))

    avg = sum(point_scores) / len(point_scores) if point_scores else 0.0

    # Monotonicity structural check
    sorted_vals = sorted(zip(voltages, currents), key=lambda x: x[0])
    mono = all(sorted_vals[i][1] <= sorted_vals[i+1][1] + 1e-9 for i in range(len(sorted_vals)-1))
    if not mono:
        avg *= 0.5

    return avg


_SCORERS = {
    'drift_velocity': score_0,
    'device_iv': score_1,
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
