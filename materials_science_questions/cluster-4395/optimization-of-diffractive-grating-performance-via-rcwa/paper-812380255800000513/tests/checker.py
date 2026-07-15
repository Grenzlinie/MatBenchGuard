import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
    csv_path = os.path.join(outputs_dir, 'spectral_response.csv')
    peaks = fwhm_calc = max_side_db = 0.0
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        wavelengths = []
        reflectances = []
        for row in reader:
            wavelengths.append(float(row['wavelength_nm']))
            reflectances.append(float(row['reflectance']))
    peak_val = max(reflectances)
    idx_peak = reflectances.index(peak_val)
    lambda_peak = wavelengths[idx_peak]
    half = peak_val / 2.0
    low_i = high_i = None
    for i, r in enumerate(reflectances):
        if r >= half:
            if low_i is None:
                low_i = i
            high_i = i
    if low_i is not None:
        fwhm_calc = wavelengths[high_i] - wavelengths[low_i]
    else:
        fwhm_calc = 0.0
    low_bound = lambda_peak - 0.5
    high_bound = lambda_peak + 0.5
    side_refs = [r for w, r in zip(wavelengths, reflectances) if w < low_bound or w > high_bound]
    if side_refs:
        max_side = max(side_refs)
        max_side_db = 10.0 * math.log10(max_side) if max_side > 0 else -100.0
    else:
        max_side_db = -100.0
    return {'peak_ref': peak_val, 'fwhm': fwhm_calc, 'max_side_db': max_side_db}


# === block: score_0 (check id='simulate_grating') ===
def score_0(artifact, step, ctx):
    peak_target = step['metrics']['peak_reflectance']['target']
    if ctx['peak_ref'] >= peak_target:
        peak_score = 1.0
    else:
        peak_score = max(0.0, 1.0 - (peak_target - ctx['peak_ref']) / peak_target)

    fwhm_target = step['metrics']['fwhm_nm']['target']
    decay = step['metrics']['fwhm_nm'].get('decay_scale', 0.05)
    if ctx['fwhm'] <= fwhm_target:
        fwhm_score = 1.0
    else:
        diff = ctx['fwhm'] - fwhm_target
        fwhm_score = max(0.0, 1.0 - diff / decay)

    side_threshold = step['metrics']['max_side_lobe_dB']['threshold']
    side_decay = step['metrics']['max_side_lobe_dB'].get('decay_scale', 10.0)
    if ctx['max_side_db'] <= side_threshold:
        side_score = 1.0
    else:
        side_score = max(0.0, 1.0 - (ctx['max_side_db'] - side_threshold) / side_decay)

    sub_w = step['sub_weights']
    return peak_score * sub_w['peak_reflectance'] + fwhm_score * sub_w['fwhm_nm'] + side_score * sub_w['max_side_lobe_dB']


# === block: score_1 (check id='extract_metrics') ===
def score_1(artifact, step, ctx):
    tol = step.get('consistency_tolerance', {})
    acceptable = True
    for key in ['peak_reflectance', 'fwhm_nm', 'max_side_lobe_dB']:
        ref = None
        if key == 'peak_reflectance':
            ref = ctx['peak_ref']
        elif key == 'fwhm_nm':
            ref = ctx['fwhm']
        elif key == 'max_side_lobe_dB':
            ref = ctx['max_side_db']
        val = artifact.get(key)
        if val is None:
            acceptable = False
            break
        if abs(val - ref) > tol.get(key, 0.0):
            acceptable = False
            break
    return 1.0 if acceptable else 0.0


_SCORERS = {
    'simulate_grating': score_0,
    'extract_metrics': score_1,
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
