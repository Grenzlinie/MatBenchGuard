import os
import json
import csv

# === author imports / helpers ===
import math

def find_gap(artifact, threshold_factor=0.01):
    energies = []
    dos = []
    for row in artifact:
        energies.append(float(row['energy']))
        dos.append(float(row['dos']))
    max_dos = max(dos)
    threshold = max_dos * threshold_factor
    # find contiguous regions with dos < threshold
    regions = []
    in_gap = False
    start = None
    for i, d in enumerate(dos):
        if d < threshold:
            if not in_gap:
                start = i
                in_gap = True
        else:
            if in_gap:
                regions.append((energies[start], energies[i-1], start, i-1))
                in_gap = False
    if in_gap:
        regions.append((energies[start], energies[-1], start, len(dos)-1))
    # select region closest to 0 eV (Fermi energy) that is plausible (width < 5 eV)
    best_gap = None
    min_dist = float('inf')
    for low, high, si, ei in regions:
        mid = 0.5 * (low + high)
        width = high - low
        if width < 5.0 and abs(mid) < min_dist:
            best_gap = width
            min_dist = abs(mid)
    return best_gap

def find_peaks(energies, values, energy_range=None, prominence_fraction=0.05):
    n = len(values)
    peaks = []
    for i in range(1, n-1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            e = energies[i]
            v = values[i]
            if energy_range is None or (e >= energy_range[0] and e <= energy_range[1]):
                peaks.append((e, v))
    if not peaks:
        return []
    max_peak_val = max(p[1] for p in peaks)
    threshold = max_peak_val * prominence_fraction
    significant = [(e, v) for e, v in peaks if v >= threshold]
    significant.sort(key=lambda x: x[1], reverse=True)
    return significant


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


# === block: score_0 (check id='dos_4x4_gap') ===
def score_0(artifact, step, ctx):
        gap = find_gap(artifact, step.get('dos_threshold_factor', 0.01))
        if gap is None:
            return 0.0
        target = step['target_gap']
        tol = step.get('tolerance', 0.15)
        return 1.0 if abs(gap - target) <= tol else 0.0


# === block: score_1 (check id='dos_8x8_gap') ===
def score_1(artifact, step, ctx):
        gap = find_gap(artifact, step.get('dos_threshold_factor', 0.01))
        if gap is None:
            return 0.0
        target = step['target_gap']
        tol = step.get('tolerance', 0.15)
        return 1.0 if abs(gap - target) <= tol else 0.0


# === block: score_2 (check id='eps2_4x4_peak_split') ===
def score_2(artifact, step, ctx):
        pol = step.get('polarization', 'parallel')
        col = 'epsilon2_parallel' if pol == 'parallel' else 'epsilon2_perpendicular'
        energies = [float(row['energy']) for row in artifact]
        values = [float(row[col]) for row in artifact]
        peaks = find_peaks(energies, values, step['energy_range'], step.get('prominence_fraction', 0.05))
        if len(peaks) < 2:
            return 0.0
        split = abs(peaks[0][0] - peaks[1][0])
        return 1.0 if split >= step['split_threshold'] else 0.0


# === block: score_3 (check id='eps2_8x8_main_peak') ===
def score_3(artifact, step, ctx):
        pol = step.get('polarization', 'parallel')
        col = 'epsilon2_parallel' if pol == 'parallel' else 'epsilon2_perpendicular'
        energies = [float(row['energy']) for row in artifact]
        values = [float(row[col]) for row in artifact]
        peaks = find_peaks(energies, values, step['energy_range'], step.get('prominence_fraction', 0.05))
        if not peaks:
            return 0.0
        main_e = peaks[0][0]
        target = step['target_peak_energy']
        tol = step.get('tolerance', 0.4)
        if abs(main_e - target) > tol:
            return 0.0
        split_absence = step.get('split_absence_threshold', 0.3)
        if len(peaks) >= 2 and abs(peaks[0][0] - peaks[1][0]) >= split_absence:
            return 0.0
        return 1.0


# === block: score_4 (check id='dos_4x4_structure') ===
def score_4(artifact, step, ctx):
        energies = [float(row['energy']) for row in artifact]
        dos = [float(row['dos']) for row in artifact]
        peaks = find_peaks(energies, dos, step.get('energy_range', None), step.get('prominence_fraction', 0.05))
        return 1.0 if len(peaks) >= step['min_peaks'] else 0.0


# === block: score_5 (check id='dos_8x8_structure') ===
def score_5(artifact, step, ctx):
        energies = [float(row['energy']) for row in artifact]
        dos = [float(row['dos']) for row in artifact]
        peaks = find_peaks(energies, dos, step.get('energy_range', None), step.get('prominence_fraction', 0.05))
        return 1.0 if len(peaks) >= step['min_peaks'] else 0.0


_SCORERS = {
    'dos_4x4_gap': score_0,
    'dos_8x8_gap': score_1,
    'eps2_4x4_peak_split': score_2,
    'eps2_8x8_main_peak': score_3,
    'dos_4x4_structure': score_4,
    'dos_8x8_structure': score_5,
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
