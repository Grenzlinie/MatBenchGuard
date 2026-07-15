import os
import json
import csv

# === author imports / helpers ===
def find_peaks_simple(arr, threshold_frac=0.05):
    """Return indices of local maxima in arr whose value >= threshold_frac * max(arr)."""
    if not arr:
        return []
    max_val = max(arr)
    if max_val <= 0:
        return []
    threshold = max_val * threshold_frac
    peaks = []
    n = len(arr)
    for i in range(n):
        left = arr[i - 1] if i > 0 else -float('inf')
        right = arr[i + 1] if i < n - 1 else -float('inf')
        if arr[i] > left and arr[i] > right and arr[i] >= threshold:
            peaks.append(i)
    return peaks


def find_peaks_in_range(w, I, freq_range, prominence_frac=0.05):
    freq_low, freq_high = freq_range
    w_sub = []
    I_sub = []
    for wi, ii in zip(w, I):
        if freq_low <= wi <= freq_high:
            w_sub.append(wi)
            I_sub.append(ii)
    if not w_sub:
        return []
    peaks_idx = find_peaks_simple(I_sub, prominence_frac)
    return [w_sub[i] for i in peaks_idx]


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


# === block: score_0 (check id='density_profile') ===
def score_0(artifact, step, ctx):
    import numpy as np

    artifact_data = artifact
    target_spec = step.get('target', {})
    peaks_spec = target_spec.get('peaks', [])
    if not peaks_spec:
        return 0.0
    z_vals = np.array([float(r.get('z', np.nan)) for r in artifact_data])
    density_vals = np.array([float(r.get('normalized_density', np.nan)) for r in artifact_data])
    mask_valid = np.isfinite(z_vals) & np.isfinite(density_vals)
    if not np.any(mask_valid):
        return 0.0
    z_vals = z_vals[mask_valid]
    density_vals = density_vals[mask_valid]
    total = len(peaks_spec)
    correct = 0
    for p in peaks_spec:
        region = p['region']
        mask = (z_vals >= region[0]) & (z_vals <= region[1])
        if not np.any(mask):
            continue
        idx_max = np.argmax(density_vals[mask])
        max_z = z_vals[mask][idx_max]
        max_d = density_vals[mask][idx_max]
        if abs(max_z - p['expected_z']) <= p['z_tol'] and abs(max_d - p['expected_density']) <= p['density_tol_frac'] * p['expected_density']:
            correct += 1
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='vibrational_dos_oxygen') ===
def score_1(artifact, step, ctx):
    import numpy as np

    artifact_data = artifact
    w = np.array([float(r.get('wavenumber_cm1', np.nan)) for r in artifact_data])
    I = np.array([float(r.get('intensity', np.nan)) for r in artifact_data])
    mask = np.isfinite(w) & np.isfinite(I)
    if not np.any(mask):
        return 0.0
    w = w[mask]
    I = I[mask]
    target = step.get('target', {})
    low_range = target['low_freq_range']
    high_range = target['high_freq_range']
    low_peaks = find_peaks_in_range(w, I, low_range)
    high_peaks = find_peaks_in_range(w, I, high_range)
    low_targets = target.get('peaks_low', [])
    high_targets = target.get('peaks_high', [])
    total_targets = len(low_targets) + len(high_targets)
    if total_targets == 0:
        return 1.0
    matched = 0
    for t in low_targets:
        if 'range' in t:
            r = t['range']
            if any((p >= r[0] and p <= r[1]) for p in low_peaks):
                matched += 1
        else:
            w_target = t['wavenumber']
            tol = t['tolerance']
            if any(abs(p - w_target) <= tol for p in low_peaks):
                matched += 1
    for t in high_targets:
        w_target = t['wavenumber']
        tol = t['tolerance']
        if any(abs(p - w_target) <= tol for p in high_peaks):
            matched += 1
    return matched / total_targets


# === block: score_2 (check id='vibrational_dos_hydrogen') ===
def score_2(artifact, step, ctx):
    import numpy as np

    artifact_data = artifact
    w = np.array([float(r.get('wavenumber_cm1', np.nan)) for r in artifact_data])
    I = np.array([float(r.get('intensity', np.nan)) for r in artifact_data])
    mask = np.isfinite(w) & np.isfinite(I)
    if not np.any(mask):
        return 0.0
    w = w[mask]
    I = I[mask]
    target = step.get('target', {})
    low_range = target['low_freq_range']
    high_range = target['high_freq_range']
    low_peaks = find_peaks_in_range(w, I, low_range)
    high_peaks = find_peaks_in_range(w, I, high_range)
    low_targets = target.get('peaks_low', [])
    high_targets = target.get('peaks_high', [])
    total_targets = len(low_targets) + len(high_targets)
    if total_targets == 0:
        return 1.0
    matched = 0
    for t in low_targets:
        if 'range' in t:
            r = t['range']
            if any((p >= r[0] and p <= r[1]) for p in low_peaks):
                matched += 1
        else:
            w_target = t['wavenumber']
            tol = t['tolerance']
            if any(abs(p - w_target) <= tol for p in low_peaks):
                matched += 1
    for t in high_targets:
        w_target = t['wavenumber']
        tol = t['tolerance']
        if any(abs(p - w_target) <= tol for p in high_peaks):
            matched += 1
    return matched / total_targets


_SCORERS = {
    'density_profile': score_0,
    'vibrational_dos_oxygen': score_1,
    'vibrational_dos_hydrogen': score_2,
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
