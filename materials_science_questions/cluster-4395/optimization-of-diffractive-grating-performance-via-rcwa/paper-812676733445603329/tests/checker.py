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


# === block: score_0 (check id='resonant_peaks_check') ===
def score_0(artifact, step, ctx):
    import math

    # step is the dict for this check from grading_spec
    rows = artifact if isinstance(artifact, list) else []
    if not rows:
        return 0.0

    required_cols = {'angle_deg', 'peak_wavelength_nm', 'peak_reflectance', 'FWHM_nm'}
    if not required_cols.issubset(set(rows[0].keys())):
        return 0.0

    # map angle to row
    data = {}
    for r in rows:
        try:
            ang = float(r['angle_deg'])
            wl = float(r['peak_wavelength_nm'])
            ref = float(r['peak_reflectance'])
            fwhm = float(r['FWHM_nm'])
            data[ang] = (wl, ref, fwhm)
        except:
            return 0.0

    if len(data) < 7:
        return 0.0

    expected_peaks = step.get('expected_peaks', [])
    if not expected_peaks:
        return 1.0  # should not happen

    period = step.get('condition_period', 574)
    threshold_angle = step.get('angles_non_subwavelength_threshold', 35)
    tol_config = step.get('tolerances', {})
    wl_tol_map = tol_config.get('peak_wavelength_nm', {})
    main_angles = set(wl_tol_map.get('main_angles', []))
    main_tol = wl_tol_map.get('main_tol', 10)
    other_tol = wl_tol_map.get('other_tol', 20)
    ref_tol = tol_config.get('peak_reflectance', 0.15)
    fwhm_tol = tol_config.get('FWHM_nm', 15)

    row_scores = []
    for exp in expected_peaks:
        angle = exp['angle']
        if angle not in data:
            row_scores.append(0.0)
            continue
        wl_got, ref_got, fwhm_got = data[angle]
        wl_exp = exp['peak_wavelength_nm']
        ref_exp = exp['peak_reflectance']
        fwhm_exp = exp['FWHM_nm']

        # wavelength score with structural condition
        if angle >= threshold_angle:
            if wl_got >= period:
                wl_score = 0.0
            else:
                tol = main_tol if angle in main_angles else other_tol
                diff = abs(wl_got - wl_exp)
                wl_score = max(0.0, 1.0 - diff / tol)
        else:
            # angles 20,25,30: wavelength should be > period
            if wl_got <= period:
                wl_score = 0.0
            else:
                tol = main_tol if angle in main_angles else other_tol
                diff = abs(wl_got - wl_exp)
                wl_score = max(0.0, 1.0 - diff / tol)

        # reflectance score
        diff_ref = abs(ref_got - ref_exp)
        ref_score = max(0.0, 1.0 - diff_ref / ref_tol)

        # FWHM score
        diff_fwhm = abs(fwhm_got - fwhm_exp)
        fwhm_score = max(0.0, 1.0 - diff_fwhm / fwhm_tol)

        # row score: weighted combination
        row_score = 0.6 * wl_score + 0.2 * ref_score + 0.2 * fwhm_score
        row_scores.append(row_score)

    if not row_scores:
        return 0.0
    return sum(row_scores) / len(row_scores)


_SCORERS = {
    'resonant_peaks_check': score_0,
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
