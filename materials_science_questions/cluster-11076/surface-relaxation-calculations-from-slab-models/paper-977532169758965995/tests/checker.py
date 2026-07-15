import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, os


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


# === block: score_0 (check id='bulk_distortion_modes_check') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    fields = [('d1_pm', 1.5), ('d2_pm', 1.5), ('d3_pm', 1.5), ('theta_z_deg', 3.0)]
    score = 0.0
    for field, tol in fields:
        if field in artifact and isinstance(artifact[field], (int, float)):
            if abs(artifact[field] - step['gold'][field]) <= tol:
                score += 0.25
    return score


# === block: score_1 (check id='bulk_band_gap_moment_check') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    thresholds = step.get('thresholds', {})
    band_gap_ok = artifact.get('band_gap_eV', 0) > thresholds.get('band_gap_eV_min', 0.1)
    mag_ok = abs(artifact.get('total_magnetization_muB', 1.0)) < thresholds.get('total_magnetization_abs_max', 1.0)
    return (0.5 if band_gap_ok else 0.0) + (0.5 if mag_ok else 0.0)


# === block: score_2 (check id='slab_layer_heights_check') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 6:
        return 0.0
    criteria = step.get('pattern_criteria', {})
    min_pairs = criteria.get('min_consecutive_pairs_alternating', 3)
    min_diff = criteria.get('min_height_difference_pm', 2.0)
    start_layer = criteria.get('layer_index_start', -1)
    num_layers = criteria.get('num_layers', 6)
    # Filter rows for layers start_layer .. start_layer - (num_layers-1)
    target_layers = set(range(start_layer, start_layer - num_layers, -1))
    rows = []
    for r in artifact:
        try:
            idx = int(r['layer_index'])
            if idx in target_layers:
                rows.append((idx, float(r['Oap_Oap_distance_pm'])))
        except (ValueError, KeyError):
            continue
    if len(rows) < num_layers:
        return 0.0
    rows.sort(key=lambda x: x[0])
    # Compute consecutive differences
    alternating_count = 0
    for i in range(len(rows)-1):
        diff = abs(rows[i][1] - rows[i+1][1])
        if diff > min_diff:
            alternating_count += 1
    return 1.0 if alternating_count >= min_pairs else 0.0


# === block: score_3 (check id='slab_band_gap_moment_check') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    thresholds = step.get('thresholds', {})
    band_gap_ok = artifact.get('band_gap_eV', 0) > thresholds.get('band_gap_eV_min', 0.1)
    mag_ok = abs(artifact.get('total_magnetization_muB', 1.0)) < thresholds.get('total_magnetization_abs_max', 1.0)
    return (0.5 if band_gap_ok else 0.0) + (0.5 if mag_ok else 0.0)


_SCORERS = {
    'bulk_distortion_modes_check': score_0,
    'bulk_band_gap_moment_check': score_1,
    'slab_layer_heights_check': score_2,
    'slab_band_gap_moment_check': score_3,
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
