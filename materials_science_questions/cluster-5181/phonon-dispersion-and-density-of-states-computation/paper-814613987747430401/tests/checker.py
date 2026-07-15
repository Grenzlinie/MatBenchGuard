import os
import json
import csv

# === author imports / helpers ===
import numpy as np


def find_dos_peaks(freqs, dos, smooth_window=3, threshold_frac=0.02):
    """
    Simple peak finder for DOS spectra.
    Returns a list of peak frequencies and the cutoff frequency.
    """
    freqs = np.array(freqs, dtype=float)
    dos = np.array(dos, dtype=float)
    if len(freqs) < 3:
        return [], None
    # smooth
    kernel = np.ones(smooth_window) / smooth_window
    dos_smooth = np.convolve(dos, kernel, mode='same')
    # threshold based on max
    thresh_val = threshold_frac * np.max(dos_smooth)
    # local maxima
    peaks_idx = []
    for i in range(1, len(dos_smooth)-1):
        if dos_smooth[i] > dos_smooth[i-1] and dos_smooth[i] > dos_smooth[i+1] and dos_smooth[i] > thresh_val:
            peaks_idx.append(i)
    peaks = freqs[peaks_idx].tolist()
    # cutoff: max frequency where dos_smooth > thresh_val
    cutoff_idx = np.where(dos_smooth > thresh_val)[0]
    cutoff = float(freqs[cutoff_idx[-1]]) if len(cutoff_idx) > 0 else None
    return peaks, cutoff


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
    import os, csv, json

    def prepare(output_dir, spec):
        ctx = {}
        for out in spec.get('output_contract', {}).get('outputs', []):
            fname = os.path.join(output_dir, out['file'].split('/')[-1])
            if not os.path.exists(fname):
                continue
            key = out['file'].split('/')[-1].replace('.', '_')
            if out['format'] == 'csv':
                with open(fname, newline='') as f:
                    ctx[key] = list(csv.DictReader(f))
            elif out['format'] == 'json':
                with open(fname) as f:
                    ctx[key] = json.load(f)
        return ctx


# === block: score_0 (check id='check_fitted_params_77K') ===
def score_0(artifact, step, ctx):
    try:
        gold = step.get('gold', {})
        tolerances = step.get('tolerances', {})
        force_rel = tolerances.get('force_relative', 0.05)
        small_abs = tolerances.get('small_absolute', 10.0)
        sigma_abs = tolerances.get('sigma_B_absolute', 0.1)
        chi_rel = tolerances.get('chi_squared_relative', 0.1)

        if artifact is None or len(artifact) == 0:
            return 0.0
        params = {row['parameter_name']: float(row['value']) for row in artifact}
        total = len(gold)
        if total == 0:
            return 0.0
        matched = 0
        for name, gold_val in gold.items():
            if name not in params:
                continue
            val = params[name]
            if name == 'sigma_B':
                if abs(val - gold_val) <= sigma_abs:
                    matched += 1
            elif name == 'chi_squared':
                if abs(val - gold_val) / abs(gold_val) <= chi_rel:
                    matched += 1
            else:
                if abs(gold_val) > 100:
                    if abs(val - gold_val) / abs(gold_val) <= force_rel:
                        matched += 1
                else:
                    if abs(val - gold_val) <= small_abs:
                        matched += 1
        return matched / total
    except Exception:
        return 0.0


# === block: score_1 (check id='check_fitted_params_296K') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold', {})
    tolerances = step.get('tolerances', {})
    force_rel = tolerances.get('force_relative', 0.05)
    small_abs = tolerances.get('small_absolute', 10.0)
    sigma_abs = tolerances.get('sigma_B_absolute', 0.1)
    chi_rel = tolerances.get('chi_squared_relative', 0.1)

    params = {row['parameter_name']: float(row['value']) for row in artifact}
    total = len(gold)
    if total == 0:
        return 0.0
    matched = 0
    for name, gold_val in gold.items():
        if name not in params:
            continue
        val = params[name]
        if name == 'sigma_B':
            if abs(val - gold_val) <= sigma_abs:
                matched += 1
        elif name == 'chi_squared':
            if abs(val - gold_val) / abs(gold_val) <= chi_rel:
                matched += 1
        else:
            if abs(gold_val) > 100:
                if abs(val - gold_val) / abs(gold_val) <= force_rel:
                    matched += 1
            else:
                if abs(val - gold_val) <= small_abs:
                    matched += 1
    return matched / total


# === block: score_2 (check id='check_dos_77K') ===
def score_2(artifact, step, ctx):
    freqs = [float(row['frequency']) for row in artifact]
    dos_vals = [float(row['dos']) for row in artifact]
    peaks_cfg = step.get('metrics', {}).get('peaks', {})
    cutoff_cfg = step.get('metrics', {}).get('cutoff', {})
    gold_peaks = peaks_cfg.get('gold', [])
    gold_cutoff = cutoff_cfg.get('gold', None)
    peak_tol = peaks_cfg.get('tolerance', 0.2)
    cutoff_tol = cutoff_cfg.get('tolerance', 0.15)
    pf_cfg = step.get('peak_finding', {})

    found_peaks, found_cutoff = find_dos_peaks(freqs, dos_vals,
                                               pf_cfg.get('smooth_window', 3),
                                               pf_cfg.get('threshold_frac', 0.02))
    if found_cutoff is None:
        return 0.0

    # match peaks
    if len(gold_peaks) == 0:
        peak_score = 1.0
    else:
        matched = 0
        for gp in gold_peaks:
            for fp in found_peaks:
                if abs(fp - gp) <= peak_tol:
                    matched += 1
                    break
        peak_score = matched / len(gold_peaks)

    cutoff_score = 1.0 if abs(found_cutoff - gold_cutoff) <= cutoff_tol else 0.0
    return 0.8 * peak_score + 0.2 * cutoff_score


# === block: score_3 (check id='check_dos_296K') ===
def score_3(artifact, step, ctx):
    freqs = [float(row['frequency']) for row in artifact]
    dos_vals = [float(row['dos']) for row in artifact]
    pf_cfg = step.get('peak_finding', {})

    found_peaks, found_cutoff = find_dos_peaks(freqs, dos_vals,
                                               pf_cfg.get('smooth_window', 3),
                                               pf_cfg.get('threshold_frac', 0.02))

    reported = ctx.get('reported_results_json', {})
    reported_peaks = reported.get('dos_296K_peaks', [])
    reported_cutoff = reported.get('dos_296K_cutoff', None)

    peak_tol = step.get('peak_match_tolerance', 0.05)
    cutoff_tol = step.get('cutoff_match_tolerance', 0.05)

    # match peaks (bi-directional: how many reported peaks are found in raw)
    if len(reported_peaks) == 0:
        peak_score = 1.0
    else:
        matched = 0
        for rp in reported_peaks:
            for fp in found_peaks:
                if abs(fp - rp) <= peak_tol:
                    matched += 1
                    break
        peak_score = matched / len(reported_peaks)

    if found_cutoff is not None and reported_cutoff is not None:
        cutoff_score = 1.0 if abs(found_cutoff - reported_cutoff) <= cutoff_tol else 0.0
    else:
        cutoff_score = 0.0

    return 0.6 * peak_score + 0.4 * cutoff_score


# === block: score_4 (check id='check_dispersion_points') ===
def score_4(artifact, step, ctx):
    rows = artifact
    # group by (temperature, symmetry_point)
    data = {}
    for r in rows:
        t = r['temperature']
        sp = r['symmetry_point']
        freq = float(r['frequency'])
        data.setdefault(t, {}).setdefault(sp, []).append(freq)

    # check M point for 77K
    score_M = 0.0
    if step.get('check_77K_M'):
        if '77' in data and 'M' in data['77']:
            freqs = data['77']['M']
            ac_found = any(abs(f - step['M_acoustic_gold']) <= step['M_acoustic_tol'] for f in freqs)
            op_found = any(abs(f - step['M_optic_gold']) <= step['M_optic_tol'] for f in freqs)
            if ac_found and op_found:
                score_M = 1.0
            elif ac_found or op_found:
                score_M = 0.5

    # existence/range check: each T and each point has at least one entry with freq in [0,12]
    required_points = ['Gamma', 'M', 'A', 'L', 'H', 'K']
    required_temps = ['77', '296']
    r_ok = 0
    total_checks = len(required_temps) * len(required_points)
    for t in required_temps:
        for sp in required_points:
            if t in data and sp in data[t]:
                freqs = data[t][sp]
                if any(0 <= f <= 12 for f in freqs):
                    r_ok += 1
    range_score = r_ok / total_checks if total_checks > 0 else 1.0

    return 0.6 * score_M + 0.4 * range_score


# === block: score_5 (check id='check_reported_results_consistency') ===
def score_5(artifact, step, ctx):
    reported = artifact
    # cross-check with raw dos files
    dos77 = ctx.get('dos_77K_csv', [])
    dos296 = ctx.get('dos_296K_csv', [])
    tol = step.get('dos_peak_match_tolerance', 0.05)
    cut_tol = step.get('cutoff_match_tolerance', 0.05)

    def extract_raw_peaks(dos_list):
        try:
            freqs = [float(r['frequency']) for r in dos_list]
            vals = [float(r['dos']) for r in dos_list]
        except:
            return [], None
        return find_dos_peaks(freqs, vals)

    # 77K consistency
    rp77 = reported.get('dos_77K_peaks', [])
    rc77 = reported.get('dos_77K_cutoff', None)
    fp77, fc77 = extract_raw_peaks(dos77)
    match_77 = 0.0
    if rp77 and fp77:
        m = 0
        for rp in rp77:
            for fp in fp77:
                if abs(fp - rp) <= tol:
                    m += 1
                    break
        match_77 = m / len(rp77)
    elif not rp77 and not fp77:
        match_77 = 1.0

    cut_77 = 0.0
    if rc77 is not None and fc77 is not None and abs(rc77 - fc77) <= cut_tol:
        cut_77 = 1.0

    # 296K consistency
    rp296 = reported.get('dos_296K_peaks', [])
    rc296 = reported.get('dos_296K_cutoff', None)
    fp296, fc296 = extract_raw_peaks(dos296)
    match_296 = 0.0
    if rp296 and fp296:
        m = 0
        for rp in rp296:
            for fp in fp296:
                if abs(fp - rp) <= tol:
                    m += 1
                    break
        match_296 = m / len(rp296)
    elif not rp296 and not fp296:
        match_296 = 1.0

    cut_296 = 0.0
    if rc296 is not None and fc296 is not None and abs(rc296 - fc296) <= cut_tol:
        cut_296 = 1.0

    # chi-squared plausibility
    chi_ok = 0.0
    chi77 = reported.get('chi_squared_77K')
    chi296 = reported.get('chi_squared_296K')
    if isinstance(chi77, (int, float)) and chi77 > 0:
        chi_ok += 0.5
    if isinstance(chi296, (int, float)) and chi296 > 0:
        chi_ok += 0.5

    score_peak_cut = 0.3 * match_77 + 0.1 * cut_77 + 0.3 * match_296 + 0.1 * cut_296
    score_chi = 0.2 * chi_ok
    return score_peak_cut + score_chi


_SCORERS = {
    'check_fitted_params_77K': score_0,
    'check_fitted_params_296K': score_1,
    'check_dos_77K': score_2,
    'check_dos_296K': score_3,
    'check_dispersion_points': score_4,
    'check_reported_results_consistency': score_5,
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
