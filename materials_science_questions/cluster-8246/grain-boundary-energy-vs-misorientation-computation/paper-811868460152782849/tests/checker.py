import os
import json
import csv

# === author imports / helpers ===
import csv, io, math


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


# === block: score_0 (check id='check_energy_profile') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < step['spec'].get('min_rows', 5):
        return 0.0
    try:
        disps = [float(r['displacement_fraction']) for r in rows]
        energs = [float(r['gb_energy']) for r in rows]
    except (KeyError, ValueError):
        return 0.0

    spec = step['spec']

    def find_peak(disp_arr, en_arr, target, tol):
        indices = [i for i, d in enumerate(disp_arr) if abs(d - target) <= tol]
        if not indices:
            return None
        return max(en_arr[i] for i in indices)

    score = 0.0
    checks = 5

    peak1 = find_peak(disps, energs, spec['peak1_position'], spec['peak1_tolerance_pos'])
    if peak1 is not None and peak1 >= spec['peak1_energy_min']:
        score += 1.0

    peak2 = find_peak(disps, energs, spec['peak2_position'], spec['peak2_tolerance_pos'])
    if peak2 is not None and peak2 >= spec['peak2_energy_min']:
        score += 1.0

    valley_indices = [i for i, d in enumerate(disps) if abs(d - spec['valley_position']) <= spec['valley_tolerance_pos']]
    if valley_indices:
        valley_energy = min(energs[i] for i in valley_indices)
        if valley_energy <= spec['valley_energy_max']:
            score += 1.0

    # barrier: overall max - overall min
    barrier = max(energs) - min(energs)
    if barrier >= spec['barrier_min']:
        score += 0.5

    # sequence monotonic? not required
    # extra 0.5 for displacement covering [0,1]
    disp_range = max(disps) - min(disps)
    if disp_range >= 0.8:
        score += 0.5

    return score / float(checks)


# === block: score_1 (check id='check_sliding_sigma3_002') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    try:
        times = [float(r['time_ps']) for r in rows]
        slides = [float(r['sliding_A']) for r in rows]
    except (KeyError, ValueError):
        return 0.0

    spec = step['spec']
    target_t = spec['target_time_ps']
    target_s = spec['target_sliding_A']
    tol = spec['relative_tolerance']

    # find row closest to target time
    best_idx = min(range(len(times)), key=lambda i: abs(times[i] - target_t))
    sliding_at_target = slides[best_idx]
    dev = abs(sliding_at_target - target_s) / max(abs(target_s), 1e-9)

    score_val = 1.0 if dev <= tol else max(0.0, 1.0 - (dev - tol) / (0.5 - tol))  # linear decay after tol, cap at dev=0.5

    # check increasing trend (first half vs second half average ratio)
    mid = len(slides)//2
    if mid > 0:
        avg_first = sum(slides[:mid])/mid
        avg_second = sum(slides[mid:])/(len(slides)-mid)
        increase = avg_second > avg_first
    else:
        increase = False

    inc_score = 0.15 if increase else 0.0
    return min(1.0, score_val + inc_score)


# === block: score_2 (check id='check_migration_sigma3_002') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    try:
        times = [float(r['time_ps']) for r in rows]
        migs = [float(r['migration_A']) for r in rows]
    except (KeyError, ValueError):
        return 0.0

    spec = step['spec']
    d111 = spec['d111']
    target_mig = spec['expected_final_migration_A']
    final_tol = spec['final_tolerance_abs']
    final_mig = migs[-1]

    score = 0.0

    # final migration check
    if abs(final_mig - target_mig) <= final_tol:
        score += 0.5
    else:
        score += max(0.0, 0.5 - (abs(final_mig - target_mig) - final_tol) / 3.0)  # partial decay

    # stepwise check: at least one jump between consecutive rows in [min_step, max_step]
    jumps = [abs(migs[i+1] - migs[i]) for i in range(len(migs)-1)]
    step_ok = any(spec['min_step_size'] <= j <= spec['max_step_size'] for j in jumps)
    score += 0.5 if step_ok else 0.0

    return min(1.0, score)


# === block: score_3 (check id='check_gb_energy_effect') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 2:
        return 0.0

    try:
        data = {r['boundary_label'].strip(): float(r['sliding_at_5ps']) for r in rows}
    except (KeyError, ValueError):
        return 0.0

    spec = step['spec']
    targets = spec['targets']
    tol = spec['relative_tolerance']

    sigma3_key = 'Sigma3(1-11)'
    sigma9_key = 'Sigma9(2-21)'

    if sigma3_key not in data or sigma9_key not in data:
        return 0.0

    s3 = data[sigma3_key]
    s9 = data[sigma9_key]

    score = 0.0

    # trend check
    if s9 > s3:
        score += 0.3

    # individual value checks
    target_s3 = targets.get(sigma3_key)
    if target_s3 is not None:
        dev = abs(s3 - target_s3) / abs(target_s3)
        if dev <= tol:
            score += 0.35
        else:
            score += 0.35 * max(0.0, 1.0 - (dev - tol) / 0.3)

    target_s9 = targets.get(sigma9_key)
    if target_s9 is not None:
        dev = abs(s9 - target_s9) / abs(target_s9)
        if dev <= tol:
            score += 0.35
        else:
            score += 0.35 * max(0.0, 1.0 - (dev - tol) / 0.3)

    return min(1.0, score)


_SCORERS = {
    'check_energy_profile': score_0,
    'check_sliding_sigma3_002': score_1,
    'check_migration_sigma3_002': score_2,
    'check_gb_energy_effect': score_3,
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
