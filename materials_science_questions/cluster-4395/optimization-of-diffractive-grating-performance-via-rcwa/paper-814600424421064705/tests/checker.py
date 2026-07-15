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


# === block: score_0 (check id='step_spectrum_valid_ccgf1') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts
    if not rows:
        return 0.0
    wavelengths = []
    reflectivities = []
    try:
        for r in rows:
            wl = float(r['wavelength_nm'])
            rf = float(r['reflectivity'])
            if rf < step['config']['reflectivity_min'] or rf > step['config']['reflectivity_max']:
                return 0.0
            wavelengths.append(wl)
            reflectivities.append(rf)
    except (KeyError, ValueError):
        return 0.0
    if len(wavelengths) < 2:
        return 0.0
    if wavelengths != sorted(wavelengths):
        return 0.0
    # simple peak detection: local maxima
    peaks = 0
    for i in range(1, len(reflectivities)-1):
        if reflectivities[i] > reflectivities[i-1] and reflectivities[i] > reflectivities[i+1]:
            peaks += 1
    if peaks >= step['config']['min_peaks']:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step_spectrum_valid_ccgf2') ===
def score_1(artifact, step, ctx):
    rows = artifact  # list of dicts
    if not rows:
        return 0.0
    wavelengths = []
    reflectivities = []
    try:
        for r in rows:
            wl = float(r['wavelength_nm'])
            rf = float(r['reflectivity'])
            if rf < step['config']['reflectivity_min'] or rf > step['config']['reflectivity_max']:
                return 0.0
            wavelengths.append(wl)
            reflectivities.append(rf)
    except (KeyError, ValueError):
        return 0.0
    if len(wavelengths) < 2:
        return 0.0
    if wavelengths != sorted(wavelengths):
        return 0.0
    # simple peak detection: local maxima
    peaks = 0
    for i in range(1, len(reflectivities)-1):
        if reflectivities[i] > reflectivities[i-1] and reflectivities[i] > reflectivities[i+1]:
            peaks += 1
    if peaks >= step['config']['min_peaks']:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='step_peak_params') ===
def score_2(artifact, step, ctx):
    data = artifact  # dict
    ref = step['config']['reference']
    tol = step['config']['tolerances']
    peak_scores = []
    for ccgf_key, label_start in [('ccgf1_peaks', 'A'), ('ccgf2_peaks', 'C')]:
        ref_peaks = ref[ccgf_key]
        user_peaks = data.get(ccgf_key, [])
        if len(user_peaks) != len(ref_peaks):
            return 0.0
        user_by_label = {p.get('peak_label'): p for p in user_peaks}
        for rp in ref_peaks:
            up = user_by_label.get(rp['peak_label'])
            if up is None:
                peak_scores.append(0.0)
                continue
            param_scores = []
            # central wavelength
            wl_diff = abs(float(up.get('central_wavelength_nm', 0)) - rp['central_wavelength_nm'])
            param_scores.append(1.0 if wl_diff <= tol['central_wavelength_nm'] else 0.0)
            # peak reflectivity (threshold_or_better: higher is not penalised)
            rf = float(up.get('peak_reflectivity', 0))
            param_scores.append(1.0 if rf >= rp['peak_reflectivity'] - tol['peak_reflectivity'] else 0.0)
            # FWHM
            fwhm_diff = abs(float(up.get('FWHM_nm', 0)) - rp['FWHM_nm'])
            param_scores.append(1.0 if fwhm_diff <= tol['FWHM_nm'] else 0.0)
            peak_scores.append(sum(param_scores) / len(param_scores))
    if not peak_scores:
        return 0.0
    return sum(peak_scores) / len(peak_scores)


_SCORERS = {
    'step_spectrum_valid_ccgf1': score_0,
    'step_spectrum_valid_ccgf2': score_1,
    'step_peak_params': score_2,
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
