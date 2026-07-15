import os
import json
import csv


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
    import json, os

    def load_json(path):
        with open(path) as f:
            return json.load(f)

    ctx = {}
    for key, fname in [('monomer_pbe_data','monomer_pbe_spectrum.json'),
                        ('monomer_b3lyp_data','monomer_b3lyp_spectrum.json'),
                        ('dimer_pbe_data','dimer_pbe_spectrum.json')]:
        p = os.path.join('/app/outputs', fname)
        if os.path.exists(p):
            ctx[key] = load_json(p)
        else:
            ctx[key] = None
    return ctx


# === block: score_0 (check id='monomer_pbe_peak') ===
def score_0(artifact, step, ctx):
    def find_first_major_peak(data):
        energies = [d['energy_ev'] for d in data]
        abs_vals = [d['absorption'] for d in data]
        peaks = []
        for i in range(1, len(abs_vals)-1):
            if abs_vals[i] > abs_vals[i-1] and abs_vals[i] > abs_vals[i+1] and energies[i] > 2.0:
                peaks.append((energies[i], abs_vals[i]))
        if not peaks:
            return None
        peaks.sort(key=lambda x: -x[1])
        return peaks[0]

    artifact_list = artifact
    if not artifact_list:
        return 0.0
    peak = find_first_major_peak(artifact_list)
    if peak is None:
        return 0.0
    target = step['gold']['energy_ev']
    tol = step['gold']['tolerance_ev']
    diff = abs(peak[0] - target)
    if diff <= tol:
        return 1.0
    elif diff <= 2*tol:
        return 1.0 - (diff - tol)/tol
    else:
        return 0.0


# === block: score_1 (check id='monomer_b3lyp_peak') ===
def score_1(artifact, step, ctx):
    def find_first_major_peak(data):
        energies = [d['energy_ev'] for d in data]
        abs_vals = [d['absorption'] for d in data]
        peaks = []
        for i in range(1, len(abs_vals)-1):
            if abs_vals[i] > abs_vals[i-1] and abs_vals[i] > abs_vals[i+1] and energies[i] > 2.0:
                peaks.append((energies[i], abs_vals[i]))
        if not peaks:
            return None
        peaks.sort(key=lambda x: -x[1])
        return peaks[0]

    artifact_list = artifact
    if not artifact_list:
        return 0.0
    peak = find_first_major_peak(artifact_list)
    if peak is None:
        return 0.0
    target = step['gold']['energy_ev']
    tol = step['gold']['tolerance_ev']
    diff = abs(peak[0] - target)
    if diff <= tol:
        return 1.0
    elif diff <= 2*tol:
        return 1.0 - (diff - tol)/tol
    else:
        return 0.0


# === block: score_2 (check id='dimer_pbe_spec') ===
def score_2(artifact, step, ctx):
    def find_all_peaks(data):
        energies = [d['energy_ev'] for d in data]
        abs_vals = [d['absorption'] for d in data]
        peaks = []
        for i in range(1, len(abs_vals)-1):
            if abs_vals[i] > abs_vals[i-1] and abs_vals[i] > abs_vals[i+1] and energies[i] > 2.0:
                peaks.append((energies[i], abs_vals[i]))
        return peaks

    artifact_list = artifact
    if not artifact_list:
        return 0.0
    peaks = find_all_peaks(artifact_list)
    if not peaks:
        return 0.0
    main_peak = max(peaks, key=lambda x: x[1])
    main_energy = main_peak[0]
    target = step['gold']['main_peak_ev']
    tol = step['gold']['main_peak_tolerance_ev']
    diff = abs(main_energy - target)
    main_score = 1.0 if diff <= tol else (1.0 - (diff - tol)/tol if diff <= 2*tol else 0.0)

    shoulder_found = False
    threshold = main_peak[1] * step['gold']['shoulder_intensity_ratio']
    for e, val in peaks:
        if step['gold']['shoulder_energy_min'] <= e <= step['gold']['shoulder_energy_max'] and val >= threshold:
            shoulder_found = True
            break
    shoulder_score = 1.0 if shoulder_found else 0.0
    return 0.7 * main_score + 0.3 * shoulder_score


# === block: score_3 (check id='summary') ===
def score_3(artifact, step, ctx):
    def find_first_major_peak(data):
        energies = [d['energy_ev'] for d in data]
        abs_vals = [d['absorption'] for d in data]
        peaks = []
        for i in range(1, len(abs_vals)-1):
            if abs_vals[i] > abs_vals[i-1] and abs_vals[i] > abs_vals[i+1] and energies[i] > 2.0:
                peaks.append((energies[i], abs_vals[i]))
        if not peaks:
            return None
        peaks.sort(key=lambda x: -x[1])
        return peaks[0]

    def find_all_peaks(data):
        energies = [d['energy_ev'] for d in data]
        abs_vals = [d['absorption'] for d in data]
        peaks = []
        for i in range(1, len(abs_vals)-1):
            if abs_vals[i] > abs_vals[i-1] and abs_vals[i] > abs_vals[i+1] and energies[i] > 2.0:
                peaks.append((energies[i], abs_vals[i]))
        return peaks

    pbe_data = ctx.get('monomer_pbe_data')
    b3lyp_data = ctx.get('monomer_b3lyp_data')
    dimer_data = ctx.get('dimer_pbe_data')
    if pbe_data is None or b3lyp_data is None or dimer_data is None:
        return 0.0

    pbe_peak = find_first_major_peak(pbe_data)
    b3lyp_peak = find_first_major_peak(b3lyp_data)
    dimer_peaks = find_all_peaks(dimer_data)
    if not dimer_peaks:
        return 0.0
    dimer_main = max(dimer_peaks, key=lambda x: x[1])

    # shoulder in dimer
    dimer_shoulder_e = None
    threshold = dimer_main[1] * 0.1
    for e, val in dimer_peaks:
        if 2.55 <= e <= 2.95 and val >= threshold:
            dimer_shoulder_e = e
            break

    tol = step['cross_check']['peak_tolerance_ev']
    summary = artifact
    score = 0.0

    if pbe_peak and abs(pbe_peak[0] - summary.get('monomer_pbe_peak1_ev', 0)) <= tol:
        score += 0.2
    if b3lyp_peak and abs(b3lyp_peak[0] - summary.get('monomer_b3lyp_peak1_ev', 0)) <= tol:
        score += 0.2
    if dimer_main and abs(dimer_main[0] - summary.get('dimer_pbe_peak1_ev', 0)) <= tol:
        score += 0.2

    rep_shoulder = summary.get('shoulder_energy_ev')
    if rep_shoulder is None:
        if dimer_shoulder_e is None:
            score += 0.2
    else:
        if dimer_shoulder_e is not None and abs(rep_shoulder - dimer_shoulder_e) <= tol:
            score += 0.2

    if pbe_peak and b3lyp_peak:
        recomputed_sens = 100.0 * abs(pbe_peak[0] - b3lyp_peak[0]) / ((pbe_peak[0] + b3lyp_peak[0]) / 2.0)
        rep_sens = summary.get('functional_sensitivity_percent')
        if (step['cross_check']['expected_sensitivity_min_percent'] <= recomputed_sens <= step['cross_check']['expected_sensitivity_max_percent']
            and abs(rep_sens - recomputed_sens) <= step['cross_check']['sensitivity_tolerance_percent']):
            score += 0.2

    return min(score, 1.0)


_SCORERS = {
    'monomer_pbe_peak': score_0,
    'monomer_b3lyp_peak': score_1,
    'dimer_pbe_spec': score_2,
    'summary': score_3,
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
