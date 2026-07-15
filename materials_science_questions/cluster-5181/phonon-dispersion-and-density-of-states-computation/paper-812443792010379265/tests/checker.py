import os
import json
import csv

# === author imports / helpers ===
import csv, os


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


# === block: score_0 (check id='ideal_csv_check') ===
def score_0(artifact, step, ctx):
    import csv, os
    path = os.path.join('/app/outputs', step.get('output_file', ''))
    if not os.path.exists(path):
        return 0.0
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames
        if not cols:
            return 0.0
        for r in step.get('required_columns', []):
            if r not in cols:
                return 0.0
        rows = list(reader)
        if len(rows) < step.get('min_rows', 1):
            return 0.0
        if not any(float(row.get('intensity', 0)) > 0 for row in rows):
            return 0.0
    return 1.0


# === block: score_1 (check id='intermixed_csv_check') ===
def score_1(artifact, step, ctx):
    import csv, os
    path = os.path.join('/app/outputs', step.get('output_file', ''))
    if not os.path.exists(path):
        return 0.0
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames
        if not cols:
            return 0.0
        for r in step.get('required_columns', []):
            if r not in cols:
                return 0.0
        rows = list(reader)
        if len(rows) < step.get('min_rows', 1):
            return 0.0
        if not any(float(row.get('intensity', 0)) > 0 for row in rows):
            return 0.0
    return 1.0


# === block: score_2 (check id='peak_relationship') ===
def score_2(artifact, step, ctx):
    import csv, os
    output_dir = '/app/outputs'
    ideal_path = os.path.join(output_dir, 'ideal_raman.csv')
    intermixed_path = os.path.join(output_dir, 'intermixed_raman.csv')

    def load_csv(path):
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def find_main_peak(rows, freq_range):
        max_val = -1
        max_freq = None
        for row in rows:
            freq = float(row['frequency'])
            if freq_range[0] <= freq <= freq_range[1]:
                intens = float(row['intensity'])
                if intens > max_val:
                    max_val = intens
                    max_freq = freq
        return max_freq, max_val

    ideal = load_csv(ideal_path)
    intermixed = load_csv(intermixed_path)

    freq_range = step.get('freq_range', [350, 410])
    delta_min = step.get('delta_min', 5.0)
    secondary_sep_min = step.get('secondary_sep_min', 5.0)
    secondary_rel_intensity = step.get('secondary_rel_intensity', 0.1)

    ideal_freq, ideal_intens = find_main_peak(ideal, freq_range)
    inter_freq, inter_intens = find_main_peak(intermixed, freq_range)

    score = 0.0
    if ideal_freq is not None and ideal_freq > 0:
        score += 0.1
    if inter_freq is not None and inter_freq > 0:
        score += 0.1

    delta = (ideal_freq - inter_freq) if (ideal_freq is not None and inter_freq is not None) else 0
    if delta >= delta_min:
        score += 0.4
    elif delta > 0:
        score += 0.4 * (delta / delta_min)

    # find secondary peak: local maxima in freq_range below inter_freq with intensity > threshold
    secondary_found = False
    if inter_freq is not None:
        points = []
        for row in intermixed:
            freq = float(row['frequency'])
            if freq_range[0] <= freq <= freq_range[1]:
                points.append((freq, float(row['intensity'])))
        points.sort()
        peaks = []
        n = len(points)
        for i in range(n):
            f, v = points[i]
            if i > 0 and i < n - 1:
                if v > points[i-1][1] and v > points[i+1][1]:
                    peaks.append((f, v))
        for f, v in peaks:
            if f < inter_freq and v >= secondary_rel_intensity * inter_intens:
                if (inter_freq - f) >= secondary_sep_min:
                    secondary_found = True
                    break
        if not secondary_found:
            # fallback: just the highest point below inter_freq (if no clear local max)
            below = [(f, v) for f, v in points if f < inter_freq]
            if below:
                best = max(below, key=lambda x: x[1])
                if best[1] >= secondary_rel_intensity * inter_intens and (inter_freq - best[0]) >= secondary_sep_min:
                    secondary_found = True

    if secondary_found:
        score += 0.3

    return min(1.0, score)


_SCORERS = {
    'ideal_csv_check': score_0,
    'intermixed_csv_check': score_1,
    'peak_relationship': score_2,
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
