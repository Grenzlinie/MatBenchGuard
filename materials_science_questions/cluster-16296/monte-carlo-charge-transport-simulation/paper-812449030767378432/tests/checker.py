import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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
    import os
    data_dir = outputs_dir
    ctx = {
        "csv_path": os.path.join(data_dir, "step_01_vE_curve.csv"),
        "summary_path": os.path.join(data_dir, "step_02_summary.json")
    }
    return ctx


# === block: score_0 (check id='step_01_vE_curve') ===
def score_0(artifact, step, ctx):
    import os
    import csv

    def _tol_score(diff, tol):
        absd = abs(diff)
        if absd <= tol:
            return 1.0
        range_ = tol * 2.0
        if absd >= tol + range_:
            return 0.0
        return 1.0 - (absd - tol) / range_

    csv_path = ctx.get("csv_path")
    summary_path = ctx.get("summary_path")
    gold = step.get("gold", {})
    tols = step.get("tolerances", {})
    max_rel_dev = step.get("consistency_max_rel_dev", 0.15)
    penalty_factor = step.get("consistency_penalty_factor", 0.5)

    # parse CSV
    rows = artifact
    if not rows:
        return 0.0
    try:
        fields = np.array([float(r["field_kV_per_cm"]) for r in rows])
        v_para = np.array([float(r["v_parabolic"]) for r in rows])
        v_non = np.array([float(r["v_nonparabolic"]) for r in rows])
    except (KeyError, ValueError):
        return 0.0

    # sort by field
    sort_idx = np.argsort(fields)
    fields = fields[sort_idx]
    v_para = v_para[sort_idx]
    v_non = v_non[sort_idx]

    if len(fields) < 5:
        return 0.0

    # helper: find peak and valley
    def find_peak_valley(f, v):
        # peak = field at maximum v
        peak_idx = np.argmax(v)
        peak_field = f[peak_idx]
        # valley = field at minimum v after peak
        if peak_idx + 1 < len(f):
            valley_idx = peak_idx + 1 + np.argmin(v[peak_idx+1:])
            valley_field = f[valley_idx]
        else:
            valley_field = peak_field
        return peak_field, valley_field

    def compute_zero_field_mobility(f, v):
        # use first points where field is low (<0.5 kV/cm) to fit slope
        mask = f < 0.5
        if np.sum(mask) < 3:
            return None
        coeffs = np.polyfit(f[mask], v[mask], 1)
        return coeffs[0]  # cm/s per kV/cm; convert to cm^2/Vs: multiply by 1e6 (since 1 kV/cm = 1e5 V/cm? Wait: 1 kV/cm = 1e5 V/m? Actually 1 kV/cm = 1e5 V/m, but units: mobility = (cm/s) / (V/cm) = cm^2/Vs. Since field is in kV/cm, slope v/f gives cm/s per kV/cm. 1 kV/cm = 1e5 V/cm? No 1 kV = 1000 V, so 1 kV/cm = 1000 V/cm = 1e3 V/cm. So mobility (cm^2/Vs) = (v/f) * (1e3) because v (cm/s) / (f kV/cm) * 1000 (V per kV) yields cm^2/Vs. Actually: mobility μ = v/E (V/cm). E = E_kV_per_cm * 1e3 V/cm. So v / (E_kV_per_cm * 1e3) = (v / E_kV_per_cm) * 1e-3? Let's check: v in cm/s, E in V/cm. If v/f is slope with f in kV/cm, then v/(f*1e3) = (v/f)*1e-3 gives cm^2/(V s). But paper's mobility is huge: 8100 cm^2/Vs. We'll compute slope in cm/s per kV/cm, then multiply by 1e3? Actually dimension: 1 kV/cm = 1000 V/cm. So E (V/cm) = f_kV_cm * 1000. Then mobility = v / (1000*f) = (v/f) / 1000. So if slope a = v/f (cm/s per kV/cm), then μ = a / 1000 cm^2/Vs. Check paper: typical GaAs mobility ~8000 cm^2/Vs. If slope a in cm/s per kV/cm, a / 1000 = 8? Too small. Maybe they use drift velocity in 1e7 cm/s. Let's think: actual v ~ 1e7 cm/s at 3 kV/cm => mobility = 1e7/3e3 ~ 3.3e3 cm^2/Vs. So formula: μ = v (cm/s) / (E_kV_per_cm * 1e3 V/cm) = v/E_kV * 1e-3. So slope a = v/E_kV, then μ = a * 1e-3. So multiply by 1e-3 yields cm^2/Vs. Example: if v=1.5e7 at E=3 kV/cm, slope a = 5e6, μ = 5000 cm^2/Vs. So we compute slope a from polyfit (cm/s per kV/cm), then μ = a * 1e-3. But paper reports 8100, so slope a would be 8.1e6. That's plausible. So we'll do μ = coeff * 1e-3.
        mu = coeffs[0] * 1e-3  # cm^2/Vs
        return mu

    def compute_ndm(f, v):
        # return minimum (most negative) of dv/dE converted to mobility in cm^2/Vs
        if len(f) < 2:
            return None
        dv = np.diff(v)
        df = np.diff(f)
        with np.errstate(divide='ignore', invalid='ignore'):
            slopes = dv / df  # cm/s per kV/cm
        slopes = slopes[np.isfinite(slopes)]
        if len(slopes) == 0:
            return None
        # most negative slope: min
        min_slope = np.min(slopes)
        # convert to mobility (cm^2/Vs): same as above: mobility = slope * 1e-3
        ndm_mobility = min_slope * 1e-3
        return ndm_mobility

    # recompute quantities for both cases
    parabolic_peak, parabolic_valley = find_peak_valley(fields, v_para)
    nonparabolic_peak, nonparabolic_valley = find_peak_valley(fields, v_non)

    parabolic_mu = compute_zero_field_mobility(fields, v_para)
    nonparabolic_mu = compute_zero_field_mobility(fields, v_non)

    parabolic_ndm = compute_ndm(fields, v_para)
    nonparabolic_ndm = compute_ndm(fields, v_non)

    if any(v is None for v in [parabolic_mu, nonparabolic_mu, parabolic_ndm, nonparabolic_ndm]):
        return 0.0

    # score each against gold
    def score_q(diff, tol):
        return _tol_score(diff, tol)

    scores = []
    # threshold fields
    scores.append(score_q(parabolic_peak - gold["parabolic_threshold_field_kV_per_cm"], tols["threshold_field_tol"]))
    scores.append(score_q(nonparabolic_peak - gold["nonparabolic_threshold_field_kV_per_cm"], tols["threshold_field_tol"]))
    # valley fields
    scores.append(score_q(parabolic_valley - gold["parabolic_valley_field_kV_per_cm"], tols["valley_field_tol"]))
    scores.append(score_q(nonparabolic_valley - gold["nonparabolic_valley_field_kV_per_cm"], tols["valley_field_tol"]))
    # zero-field mobility
    scores.append(score_q(parabolic_mu - gold["parabolic_zero_field_mobility_cm2_per_Vs"], tols["mobility_tol"]))
    scores.append(score_q(nonparabolic_mu - gold["nonparabolic_zero_field_mobility_cm2_per_Vs"], tols["mobility_tol"]))
    # NDM
    scores.append(score_q(parabolic_ndm - gold["parabolic_max_NDM_cm2_per_Vs"], tols["ndm_tol"]))
    scores.append(score_q(nonparabolic_ndm - gold["nonparabolic_max_NDM_cm2_per_Vs"], tols["ndm_tol"]))

    base_score = np.mean(scores)

    # cross-consistency check against summary if present
    if os.path.exists(summary_path):
        try:
            with open(summary_path) as f:
                summary = json.load(f)
            # keys to compare: threshold, valley, mobility, ndm
            # we already have recomputed values
            recomp_map = {
                "parabolic_threshold_field_kV_per_cm": parabolic_peak,
                "nonparabolic_threshold_field_kV_per_cm": nonparabolic_peak,
                "parabolic_valley_field_kV_per_cm": parabolic_valley,
                "nonparabolic_valley_field_kV_per_cm": nonparabolic_valley,
                "parabolic_zero_field_mobility_cm2_per_Vs": parabolic_mu,
                "nonparabolic_zero_field_mobility_cm2_per_Vs": nonparabolic_mu,
                "parabolic_max_NDM_cm2_per_Vs": parabolic_ndm,
                "nonparabolic_max_NDM_cm2_per_Vs": nonparabolic_ndm
            }
            bad = False
            for key, recomputed_val in recomp_map.items():
                if key in summary:
                    summar_val = summary[key]
                    if abs(recomputed_val) < 1e-12:
                        rel_dev = abs(summar_val - recomputed_val)
                    else:
                        rel_dev = abs(summar_val - recomputed_val) / abs(recomputed_val)
                    if rel_dev > max_rel_dev:
                        bad = True
                        break
            if bad:
                base_score *= penalty_factor
        except Exception:
            pass

    return float(base_score)


# === block: score_1 (check id='step_02_summary') ===
def score_1(artifact, step, ctx):
    import os
    import json

    def _tol_score(diff, tol):
        absd = abs(diff)
        if absd <= tol:
            return 1.0
        range_ = tol * 2.0
        if absd >= tol + range_:
            return 0.0
        return 1.0 - (absd - tol) / range_

    gold = step.get("gold", {})
    tol = step.get("tolerance", 0.02)

    if not isinstance(artifact, dict):
        return 0.0

    scores = []
    for key in ["parabolic_population_ratio_2kV_per_cm_pct", "nonparabolic_population_ratio_2kV_per_cm_pct"]:
        if key not in artifact or key not in gold:
            scores.append(0.0)
            continue
        diff = artifact[key] - gold[key]
        scores.append(_tol_score(diff, tol))

    if not scores:
        return 0.0
    return float(np.mean(scores))


_SCORERS = {
    'step_01_vE_curve': score_0,
    'step_02_summary': score_1,
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
