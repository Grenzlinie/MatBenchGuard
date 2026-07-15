import os
import json
import csv

# === author imports / helpers ===
import csv, json, math


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


# === block: score_0 (check id='step_01_nwpdos_ordered') ===
def score_0(artifact, step, ctx):
    def local_maxima(xy, min_height=0.01, min_distance=5):
        peaks = []
        n = len(xy)
        for i in range(1, n-1):
            if xy[i][1] > xy[i-1][1] and xy[i][1] > xy[i+1][1] and xy[i][1] > min_height:
                peaks.append(xy[i])
        filtered = []
        for p in sorted(peaks, key=lambda x: x[1], reverse=True):
            if all(abs(p[0] - fp[0]) >= min_distance for fp in filtered):
                filtered.append(p)
        filtered.sort(key=lambda x: x[0])
        return filtered

    def detect_peaks_in_windows(xy, windows):
        all_peaks = local_maxima(xy)
        bands = []
        for lo, hi in windows:
            best = None
            for p in all_peaks:
                if lo <= p[0] <= hi:
                    if best is None or p[1] > best[1]:
                        best = p
            bands.append(best)
        return bands

    csv_artifact = artifact
    if not csv_artifact or not isinstance(csv_artifact, list):
        return 0.0
    try:
        data = [(float(row['energy_cm1']), float(row['nwpdos'])) for row in csv_artifact]
    except Exception:
        return 0.0
    gold = step.get('gold_peaks', {})
    windows = gold.get('windows', [])
    expected_pos = gold.get('expected_positions', [])
    expected_ints = gold.get('relative_intensities', [])
    pos_tol = gold.get('position_tolerance', 10)
    int_tol = gold.get('intensity_tolerance', 0.15)

    if not windows or len(windows) != len(expected_pos):
        return 0.0

    bands = detect_peaks_in_windows(data, windows)
    if not bands or len(bands) != len(expected_pos):
        return 0.0
    if any(b is None for b in bands):
        return 0.0

    # Compute relative intensities from the detected peaks
    max_h = max(p[1] for p in bands)
    score = 0.0
    n = len(expected_pos)
    for i in range(n):
        pos, h = bands[i]
        rel_int = h / max_h if max_h != 0 else 0
        pos_ok = abs(pos - expected_pos[i]) <= pos_tol
        int_ok = abs(rel_int - expected_ints[i]) <= int_tol
        if pos_ok and int_ok:
            score += 1.0 / n
        elif pos_ok or int_ok:
            score += 0.5 / n
    return min(1.0, score)


# === block: score_1 (check id='step_02_nwpdos_disordered_delta_trans') ===
def score_1(artifact, step, ctx):
    def local_maxima(xy, min_height=0.01, min_distance=5):
        peaks = []
        n = len(xy)
        for i in range(1, n-1):
            if xy[i][1] > xy[i-1][1] and xy[i][1] > xy[i+1][1] and xy[i][1] > min_height:
                peaks.append(xy[i])
        filtered = []
        for p in sorted(peaks, key=lambda x: x[1], reverse=True):
            if all(abs(p[0] - fp[0]) >= min_distance for fp in filtered):
                filtered.append(p)
        filtered.sort(key=lambda x: x[0])
        return filtered

    def detect_peaks_in_windows(xy, windows):
        all_peaks = local_maxima(xy)
        bands = []
        for lo, hi in windows:
            best = None
            for p in all_peaks:
                if lo <= p[0] <= hi:
                    if best is None or p[1] > best[1]:
                        best = p
            bands.append(best)
        return bands

    csv_artifact = artifact
    if not csv_artifact or not isinstance(csv_artifact, list):
        return 0.0
    try:
        data = [(float(row['energy_cm1']), float(row['nwpdos'])) for row in csv_artifact]
    except Exception:
        return 0.0
    gold = step.get('gold_peaks', {})
    windows = gold.get('windows', [])
    expected_pos = gold.get('expected_positions', [])
    expected_ints = gold.get('relative_intensities', [])
    pos_tol = gold.get('position_tolerance', 10)
    int_tol = gold.get('intensity_tolerance', 0.15)

    bands = detect_peaks_in_windows(data, windows)
    if not bands or len(bands) != len(expected_pos):
        return 0.0

    max_h = max(p[1] for p in bands if p)
    score = 0.0
    n = len(expected_pos)
    for i in range(n):
        if bands[i] is None:
            continue
        pos, h = bands[i]
        rel_int = h / max_h if max_h != 0 else 0
        pos_ok = abs(pos - expected_pos[i]) <= pos_tol
        int_ok = abs(rel_int - expected_ints[i]) <= int_tol
        if pos_ok and int_ok:
            score += 1.0 / n
        elif pos_ok or int_ok:
            score += 0.5 / n
    return min(1.0, score)


# === block: score_2 (check id='step_03_difference_spectrum') ===
def score_2(artifact, step, ctx):
    csv_artifact = artifact
    if not csv_artifact or not isinstance(csv_artifact, list):
        return 0.0
    try:
        data = [(float(row['energy_cm1']), float(row['delta_nwpdos'])) for row in csv_artifact]
    except Exception:
        return 0.0
    windows = step.get('negative_windows', [])
    if not windows:
        return 0.0
    correct = 0
    for lo, hi in windows:
        vals = [v for e, v in data if lo <= e <= hi]
        if len(vals) == 0:
            continue
        # Check that the average delta in this window is negative (or the minimum is negative)
        avg = sum(vals) / len(vals)
        if avg < 0:
            correct += 1
        else:
            # also check if any negative dip exists (could be noise)
            if min(vals) < 0:
                correct += 1
    score = correct / len(windows)
    return min(1.0, score)


# === block: score_3 (check id='step_04_peak_analysis') ===
def score_3(artifact, step, ctx):
    artifact_json = artifact
    if not isinstance(artifact_json, dict):
        return 0.0
    gold_ord = step.get('gold_ordered_bands', [])
    gold_dis = step.get('gold_disordered_bands', [])
    pos_tol = step.get('position_tolerance', 8)
    int_tol = step.get('intensity_tolerance', 0.15)

    def compare_bands(submitted, gold):
        if not isinstance(submitted, list) or len(submitted) != len(gold):
            return 0.0
        score = 0.0
        n = len(gold)
        for i in range(n):
            sub = submitted[i]
            g = gold[i]
            if not isinstance(sub, dict) or not isinstance(g, dict):
                continue
            pos_s = sub.get('peak_cm1')
            int_s = sub.get('relative_intensity')
            if pos_s is None or int_s is None:
                continue
            pos_ok = abs(pos_s - g['peak_cm1']) <= pos_tol
            int_ok = abs(int_s - g['relative_intensity']) <= int_tol
            if pos_ok and int_ok:
                score += 1.0 / n
            elif pos_ok or int_ok:
                score += 0.5 / n
        return score

    ord_score = compare_bands(artifact_json.get('ordered_bands', []), gold_ord)
    dis_score = compare_bands(artifact_json.get('disordered_bands', []), gold_dis)
    return (ord_score + dis_score) / 2.0


_SCORERS = {
    'step_01_nwpdos_ordered': score_0,
    'step_02_nwpdos_disordered_delta_trans': score_1,
    'step_03_difference_spectrum': score_2,
    'step_04_peak_analysis': score_3,
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
