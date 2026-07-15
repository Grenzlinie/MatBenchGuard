import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import csv
import io
import os


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


# === block: score_0 (check id='check_proj') ===
def score_0(artifact, step, ctx):
    csv_path = os.path.join('/app/outputs', step['output_file'])
    try:
        data = np.genfromtxt(csv_path, delimiter=',', dtype=float)
    except Exception:
        return 0.0
    if data is None or data.ndim != 2 or data.shape != (401, 401):
        return 0.0
    if data.size == 0 or np.max(data) <= 0:
        return 0.0

    # symmetry score
    rows_rev = data[:, ::-1]
    diff = np.abs(data - rows_rev)
    total_sum = np.sum(data) + 1e-12
    sym_error = np.sum(diff) / total_sum
    if sym_error < 0.05:
        sym_score = 1.0
    else:
        sym_score = max(0.0, 1.0 - sym_error / 0.1)

    # width score (scale-invariant ratio of half-max radius to half-grid size)
    max_val = np.max(data)
    center = np.unravel_index(np.argmax(data), data.shape)
    if abs(center[0] - 200) > 5 or abs(center[1] - 200) > 5:
        width_score = 0.0
    else:
        y, x = np.indices(data.shape)
        dist = np.sqrt((x - center[1])**2 + (y - center[0])**2)
        # compute mean radial profile
        max_dist = int(np.ceil(np.max(dist)))
        sums = np.zeros(max_dist + 1, dtype=np.float64)
        counts = np.zeros(max_dist + 1, dtype=np.int64)
        flat_dist = dist.ravel()
        flat_data = data.ravel()
        for d, v in zip(flat_dist, flat_data):
            bin_idx = int(round(d))
            if bin_idx <= max_dist:
                sums[bin_idx] += v
                counts[bin_idx] += 1
        valid = counts > 0
        if not np.any(valid):
            width_score = 0.0
        else:
            radial_profile = sums[valid] / counts[valid]
            distances = np.arange(max_dist + 1)[valid]
            threshold = 0.5 * max_val
            above = radial_profile >= threshold
            if not np.any(above):
                width_score = 0.0
            else:
                last_above = distances[above][-1]
                next_idx = np.where(above)[0][-1] + 1
                if next_idx < len(radial_profile):
                    frac = (threshold - radial_profile[last_above]) / (radial_profile[next_idx] - radial_profile[last_above] + 1e-12)
                    half_max_radius = last_above + frac
                else:
                    half_max_radius = last_above
                ratio = half_max_radius / 200.0
                if 0.25 <= ratio <= 0.35:
                    width_score = 1.0
                elif 0.2 <= ratio <= 0.4:
                    width_score = 0.5
                else:
                    width_score = 0.0

    # final score: 0.5 symmetry + 0.5 width
    score = 0.5 * sym_score + 0.5 * width_score
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='check_depth') ===
def score_1(artifact, step, ctx):
    try:
        with open(os.path.join('/app/outputs', step['output_file']), newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except Exception:
        return 0.0
    if not rows:
        return 0.0
    required = {'slice_index', 'depth_midpoint_nm', 'generation_intensity_arbunits'}
    if required - set(rows[0].keys()):
        return 0.0
    vals = []
    for r in rows:
        try:
            v = float(r['generation_intensity_arbunits'])
            if v < 0:
                return 0.0
            vals.append(v)
        except (ValueError, TypeError):
            return 0.0
    if len(vals) != 100:
        return 0.0
    mean_val = np.mean(vals)
    if mean_val <= 0:
        return 0.0
    std_val = np.std(vals)
    coeff_var = std_val / mean_val
    # profile should be nearly uniform (thin foil)
    if coeff_var <= 0.05:
        score = 1.0
    elif coeff_var <= 0.2:
        score = 1.0 - (coeff_var - 0.05) / (0.2 - 0.05)
    else:
        score = 0.0
    return max(0.0, min(1.0, score))


_SCORERS = {
    'check_proj': score_0,
    'check_depth': score_1,
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
