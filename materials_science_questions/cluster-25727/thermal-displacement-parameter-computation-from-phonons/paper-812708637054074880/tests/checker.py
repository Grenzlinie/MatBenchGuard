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
    return {}


# === block: score_0 (check id='pbte_gap') ===
def score_0(artifact, step, ctx):
    rows = [row for row in artifact if row.get('temperature_K') and row.get('gap_L_eV')]
    if not rows:
        return 0.0

    # extract expected data from step config
    expected_gaps = step.get('expected_gaps', [])
    pointwise_tol = step.get('pointwise_tolerance_abs', 0.02)
    expected_slope = step.get('expected_slope_eV_per_K', 3.3e-4)
    slope_tol = step.get('slope_tolerance_abs_eV_per_K', 0.5e-4)
    slope_Ts = step.get('slope_temperatures_K', [100, 300])
    pw_weight = step.get('pointwise_weight', 0.7)
    slope_weight = step.get('slope_weight', 0.3)

    # map temperature -> gap
    gap_map = {}
    for row in rows:
        try:
            T = int(float(row['temperature_K']))
            gap = float(row['gap_L_eV'])
            gap_map[T] = gap
        except (ValueError, TypeError):
            continue

    # pointwise score
    n_points = len(expected_gaps)
    points_correct = 0
    for item in expected_gaps:
        T = item['temperature_K']
        expected_gap = item['gap_L_eV']
        if T in gap_map and abs(gap_map[T] - expected_gap) <= pointwise_tol:
            points_correct += 1
    pointwise_score = points_correct / n_points if n_points > 0 else 0.0

    # slope score
    slope_score = 0.0
    T_low, T_high = slope_Ts
    if T_low in gap_map and T_high in gap_map:
        delta_T = T_high - T_low
        if delta_T > 0:
            computed_slope = (gap_map[T_high] - gap_map[T_low]) / delta_T
            if abs(computed_slope - expected_slope) <= slope_tol:
                slope_score = 1.0
            else:
                # allow partial credit based on relative error if outside tolerance
                rel = abs(computed_slope - expected_slope) / (abs(expected_slope) + 1e-12)
                slope_score = max(0.0, 1.0 - rel)

    return pw_weight * pointwise_score + slope_weight * slope_score


# === block: score_1 (check id='snte_gap') ===
def score_1(artifact, step, ctx):
    rows = [row for row in artifact if row.get('temperature_K') and row.get('gap_L_eV')]
    if not rows:
        return 0.0

    expected_gaps = step.get('expected_gaps', [])
    pointwise_tol = step.get('pointwise_tolerance_abs', 0.02)
    expected_slope = step.get('expected_slope_eV_per_K', -1.3e-4)
    slope_tol = step.get('slope_tolerance_abs_eV_per_K', 0.5e-4)
    slope_Ts = step.get('slope_temperatures_K', [100, 300])
    pw_weight = step.get('pointwise_weight', 0.7)
    slope_weight = step.get('slope_weight', 0.3)

    gap_map = {}
    for row in rows:
        try:
            T = int(float(row['temperature_K']))
            gap = float(row['gap_L_eV'])
            gap_map[T] = gap
        except (ValueError, TypeError):
            continue

    n_points = len(expected_gaps)
    points_correct = 0
    for item in expected_gaps:
        T = item['temperature_K']
        expected_gap = item['gap_L_eV']
        if T in gap_map and abs(gap_map[T] - expected_gap) <= pointwise_tol:
            points_correct += 1
    pointwise_score = points_correct / n_points if n_points > 0 else 0.0

    slope_score = 0.0
    T_low, T_high = slope_Ts
    if T_low in gap_map and T_high in gap_map:
        delta_T = T_high - T_low
        if delta_T > 0:
            computed_slope = (gap_map[T_high] - gap_map[T_low]) / delta_T
            if abs(computed_slope - expected_slope) <= slope_tol:
                slope_score = 1.0
            else:
                rel = abs(computed_slope - expected_slope) / (abs(expected_slope) + 1e-12)
                slope_score = max(0.0, 1.0 - rel)

    return pw_weight * pointwise_score + slope_weight * slope_score


_SCORERS = {
    'pbte_gap': score_0,
    'snte_gap': score_1,
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
