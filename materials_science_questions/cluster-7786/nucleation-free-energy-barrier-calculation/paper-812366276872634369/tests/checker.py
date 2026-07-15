import os
import json
import csv

# === author imports / helpers ===
import csv
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
    return {"spec": spec}


# === block: score_0 (check id='saddle_point_table') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts from CSV
    if not rows:
        return 0.0
    gold_rows = step["gold_rows"]
    tolerances = step["tolerances"]
    gold_map = {r["relative_humidity_pct"]: r for r in gold_rows}
    total_fields = 0
    matched = 0
    fields_to_check = ["acid_vapor_activity", "acid_vapor_pressure_torr", "composition_X_star",
                       "radius_A", "molecules_per_nucleus", "deltaG_over_kT", "frequency_factor_C"]
    for row in rows:
        rh = int(row.get("relative_humidity_pct", -1))
        gold = gold_map.get(rh)
        if not gold:
            continue
        for field in fields_to_check:
            try:
                val = float(row[field])
                gold_val = gold[field]
            except (ValueError, KeyError):
                continue
            total_fields += 1
            tol = tolerances.get(field)
            if tol["type"] == "absolute":
                if abs(val - gold_val) <= tol["value"]:
                    matched += 1
            else:  # relative
                if abs(gold_val) > 1e-12:
                    if abs(val - gold_val) / abs(gold_val) <= tol["value"]:
                        matched += 1
                else:
                    if abs(val - gold_val) <= 1e-9:
                        matched += 1
    if total_fields == 0:
        return 0.0
    return matched / total_fields


# === block: score_1 (check id='growth_curve_100RH') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold_samples = step.get("gold_samples", [])
    tol_abs = step.get("tol_abs", 0.02)
    # Find nearest radius in submitted data for each gold sample
    points = []
    for d in rows:
        try:
            r = float(d["radius_A"])
            x = float(d["composition_X"])
        except (ValueError, KeyError):
            continue
        points.append((r, x))
    if not points:
        return 0.0
    points.sort(key=lambda p: p[0])
    radii, comps = zip(*points)

    matched = 0
    for gs in gold_samples:
        target_r = gs["radius_A"]
        # find closest
        idx = 0
        for i, r in enumerate(radii):
            if r >= target_r:
                idx = i
                break
        else:
            idx = len(radii) - 1
        # simple linear interpolation could be used, but we take closest
        best_comp = comps[idx]
        if abs(best_comp - gs["composition_X"]) <= tol_abs:
            matched += 1
    return matched / len(gold_samples) if gold_samples else 1.0


_SCORERS = {
    'saddle_point_table': score_0,
    'growth_curve_100RH': score_1,
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
