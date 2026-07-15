import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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


# === block: score_0 (check id='step_1') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    groups = {}
    for row in rows:
        key = row['channel'] + '_' + row['impurity_type']
        groups.setdefault(key, []).append(row)
    expected_peaks = step.get('expected_peak_positions', {})
    peak_tol = step.get('peak_tolerance', 0.3)
    exponent_ranges = step.get('exponent_ranges', {})
    low_freq_max = step.get('low_freq_max', 0.5)
    total_checks = len(expected_peaks) + len(exponent_ranges)
    if total_checks == 0:
        return 1.0
    score = 0.0
    for key, group_rows in groups.items():
        vals = []
        for r in group_rows:
            try:
                f = float(r['frequency'])
                i = float(r['intensity'])
            except (ValueError, TypeError):
                continue
            vals.append((f, i))
        if not vals:
            continue
        freqs, ints = zip(*vals)
        freqs = np.array(freqs)
        ints = np.array(ints)
        if key in expected_peaks:
            peak_idx = np.argmax(ints)
            peak_freq = freqs[peak_idx]
            if abs(peak_freq - expected_peaks[key]) <= peak_tol:
                score += 1.0
        if key in exponent_ranges:
            mask = (freqs > 0) & (freqs <= low_freq_max)
            if np.sum(mask) >= 3:
                log_f = np.log(freqs[mask])
                log_i = np.log(np.maximum(ints[mask], 1e-12))
                fit = np.polyfit(log_f, log_i, 1)
                exponent = fit[0]
                low, high = exponent_ranges[key]['min'], exponent_ranges[key]['max']
                if low <= exponent <= high:
                    score += 1.0
    return min(1.0, score / total_checks)


# === block: score_1 (check id='step_2') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    vals = []
    for r in rows:
        try:
            f = float(r['frequency'])
            i = float(r['intensity'])
        except (ValueError, TypeError):
            continue
        vals.append((f, i))
    if not vals:
        return 0.0
    freqs = np.array([v[0] for v in vals])
    ints = np.array([v[1] for v in vals])
    hi_min = step.get('high_freq_min', 3.0)
    hi_max = step.get('high_freq_max', 4.0)
    mask = (freqs >= hi_min) & (freqs <= hi_max)
    if np.sum(mask) < 3:
        return 0.0
    log_f = np.log(freqs[mask])
    log_i = np.log(np.maximum(ints[mask], 1e-12))
    fit = np.polyfit(log_f, log_i, 1)
    exponent = fit[0]
    target_exp = step.get('expected_exponent', -1.0)
    tol = step.get('exponent_tolerance', 0.4)
    dist = abs(exponent - target_exp)
    if dist <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (dist - tol) / tol)


_SCORERS = {
    'step_1': score_0,
    'step_2': score_1,
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
