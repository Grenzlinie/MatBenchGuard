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
    return {}


# === block: score_0 (check id='znS_emission_check') ===
def score_0(artifact, step, ctx):
    peaks = step['peak_energies']
    tol = step['tolerance_energy']
    order = step['ordering_rule']

    data = [(float(r['energy']), float(r['intensity'])) for r in artifact]
    data.sort(key=lambda x: x[0])

    # detect local maxima (strict: must be higher than immediate neighbours)
    local_max = []
    for i in range(1, len(data)-1):
        e_prev, i_prev = data[i-1]
        e_here, i_here = data[i]
        e_next, i_next = data[i+1]
        if i_here > i_prev and i_here > i_next:
            local_max.append((e_here, i_here))

    def find_peak(target_energy):
        """Return (energy, intensity) of the local maximum CLOSEST to target_energy within tol, or None."""
        best = None
        min_dist = float('inf')
        for e, intensity in local_max:
            dist = abs(e - target_energy)
            if dist <= tol:
                if dist < min_dist:
                    min_dist = dist
                    best = (e, intensity)
        return best

    found = [find_peak(p) for p in peaks]
    if any(f is None for f in found):
        return 0.0

    # final tolerance check (redundant given find_peak, but kept for safety)
    within_tol = all(abs(f[0] - p) <= tol for f, p in zip(found, peaks))
    if not within_tol:
        return 0.0

    # check ordering: peaks[0] is lower energy, peaks[1] higher
    if order == 'lower_stronger':
        correct = found[0][1] > found[1][1]
    else:  # higher_stronger
        correct = found[1][1] > found[0][1]
    return 1.0 if correct else 0.5


# === block: score_1 (check id='znS_absorption_check') ===
def score_1(artifact, step, ctx):
    peaks = step['peak_energies']
    tol = step['tolerance_energy']
    order = step['ordering_rule']
    data = [(float(r['energy']), float(r['intensity'])) for r in artifact]

    def find_peak(target):
        best_e, best_i = None, -1.0
        for e,i in data:
            if abs(e - target) <= 5.0:
                if i > best_i:
                    best_i = i
                    best_e = e
        return best_e, best_i

    found = [find_peak(p) for p in peaks]
    if any(f[0] is None for f in found):
        return 0.0
    within_tol = all(abs(f[0] - p) <= tol for f,p in zip(found, peaks))
    if not within_tol:
        return 0.0
    if order == 'lower_stronger':
        correct = found[0][1] > found[1][1]
    else:
        correct = found[1][1] > found[0][1]
    return 1.0 if correct else 0.5


# === block: score_2 (check id='znSe_emission_check') ===
def score_2(artifact, step, ctx):
    peaks = step['peak_energies']
    tol = step['tolerance_energy']
    order = step['ordering_rule']
    data = [(float(r['energy']), float(r['intensity'])) for r in artifact]

    def find_peak(target):
        best_e, best_i = None, -1.0
        for e,i in data:
            if abs(e - target) <= 5.0:
                if i > best_i:
                    best_i = i
                    best_e = e
        return best_e, best_i

    found = [find_peak(p) for p in peaks]
    if any(f[0] is None for f in found):
        return 0.0
    within_tol = all(abs(f[0] - p) <= tol for f,p in zip(found, peaks))
    if not within_tol:
        return 0.0
    if order == 'lower_stronger':
        correct = found[0][1] > found[1][1]
    else:
        correct = found[1][1] > found[0][1]
    return 1.0 if correct else 0.5


# === block: score_3 (check id='znSe_absorption_check') ===
def score_3(artifact, step, ctx):
    peaks = step['peak_energies']
    tol = step['tolerance_energy']
    order = step['ordering_rule']
    data = [(float(r['energy']), float(r['intensity'])) for r in artifact]

    def find_peak(target):
        best_e, best_i = None, -1.0
        for e,i in data:
            if abs(e - target) <= 5.0:
                if i > best_i:
                    best_i = i
                    best_e = e
        return best_e, best_i

    found = [find_peak(p) for p in peaks]
    if any(f[0] is None for f in found):
        return 0.0
    within_tol = all(abs(f[0] - p) <= tol for f,p in zip(found, peaks))
    if not within_tol:
        return 0.0
    if order == 'lower_stronger':
        correct = found[0][1] > found[1][1]
    else:
        correct = found[1][1] > found[0][1]
    return 1.0 if correct else 0.5


# === block: score_4 (check id='zero_phonon_params_check') ===
def score_4(artifact, step, ctx):
    import json
    # artifact is already parsed dict
    try:
        p = artifact
    except Exception:
        return 0.0
    # verify required keys exist
    required = ['znS_emission_peaks','znS_absorption_peaks','znSe_emission_peaks','znSe_absorption_peaks','S_tau_ZnS','S_tau_ZnSe']
    if not all(k in p for k in required):
        return 0.0

    # extract reference values from step
    tol_peak = step.get('tolerance_peak', 3.0)
    tol_S = step.get('tolerance_S', 0.01)
    znS_ref = step['peak_energies_ZnS']
    znSe_ref = step['peak_energies_ZnSe']
    S_ZnS_ref = step['S_tau_ZnS_ref']
    S_ZnSe_ref = step['S_tau_ZnSe_ref']

    def check_peak_array(arr, ref, tol):
        if not isinstance(arr, list) or len(arr) != 2:
            return False
        try:
            v = [float(x) for x in arr]
        except Exception:
            return False
        return all(abs(v[i] - ref[i]) <= tol for i in range(2)) and v[0] < v[1]   # enforce ascending order

    peak_ok = [
        check_peak_array(p.get('znS_emission_peaks'), znS_ref, tol_peak),
        check_peak_array(p.get('znS_absorption_peaks'), znS_ref, tol_peak),
        check_peak_array(p.get('znSe_emission_peaks'), znSe_ref, tol_peak),
        check_peak_array(p.get('znSe_absorption_peaks'), znSe_ref, tol_peak),
    ]
    peak_score = sum(peak_ok) / 4.0

    # S_tau check
    try:
        s_ZnS = float(p['S_tau_ZnS'])
        s_ZnSe = float(p['S_tau_ZnSe'])
    except Exception:
        return 0.0
    s_ok = (abs(s_ZnS - S_ZnS_ref) <= tol_S) and (abs(s_ZnSe - S_ZnSe_ref) <= tol_S)
    s_score = 1.0 if s_ok else 0.0

    return 0.5 * peak_score + 0.5 * s_score


_SCORERS = {
    'znS_emission_check': score_0,
    'znS_absorption_check': score_1,
    'znSe_emission_check': score_2,
    'znSe_absorption_check': score_3,
    'zero_phonon_params_check': score_4,
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
