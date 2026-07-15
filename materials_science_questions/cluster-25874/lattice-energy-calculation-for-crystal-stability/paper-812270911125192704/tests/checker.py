import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math
import os
import json


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
    dos_path = os.path.join(outputs_dir, 'density_of_states.json')
    zone_path = os.path.join(outputs_dir, 'zone_center_frequencies.json')
    dos = None
    if os.path.exists(dos_path):
        with open(dos_path) as f:
            dos = json.load(f)
    zone = None
    if os.path.exists(zone_path):
        with open(zone_path) as f:
            zone = json.load(f)
    return {'dos': dos, 'zone': zone}


# === block: score_0 (check id='zone_center_frequencies') ===
def score_0(artifact, step, ctx):
    artifact # list of dicts with 'mode','frequency'
    gold = step.get('gold_frequencies', {})
    tol = step.get('tolerance', 5.0)
    if not gold:
        return 0.0
    matches = 0
    for entry in artifact:
        mode = entry.get('mode')
        if mode in gold:
            if abs(entry['frequency'] - gold[mode]) <= tol:
                matches += 1
    total = len(gold)
    if total == 0:
        return 0.0
    return matches / total


# === block: score_1 (check id='density_of_states') ===
def score_1(artifact, step, ctx):
    artifact # dict with 'bin_centers','density'
    bin_centers = artifact.get('bin_centers', [])
    density = artifact.get('density', [])
    expected_count = step.get('expected_bin_count', 150)
    bin_range = step.get('gold_bin_range', [1.0, 150.0])
    gold_peaks = step.get('gold_peaks', [])
    tol_peaks = step.get('tolerance_peaks', 5.0)

    # shape check
    shape_score = 0.0
    if len(bin_centers) == expected_count and len(density) == expected_count:
        if len(bin_centers) > 0:
            first = bin_centers[0]
            step_val = bin_centers[1] - bin_centers[0] if len(bin_centers) > 1 else 0
            if abs(first - bin_range[0]) < 0.1 and abs(step_val - 1.0) < 0.01:
                shape_score = 1.0

    # peak check
    peak_score = 0.0
    if gold_peaks:
        # find maxima in density as a simple local peak detector
        dens = np.array(density)
        # local maxima: greater than left and right neighbor
        local_max = np.r_[True, dens[1:] > dens[:-1]] & np.r_[dens[:-1] > dens[1:], True]
        peak_bins = np.array(bin_centers)[local_max]
        peaks_found = 0
        for gp in gold_peaks:
            # any local maximum within tolerance?
            if any(abs(peak_bins - gp) <= tol_peaks):
                peaks_found += 1
        peak_score = peaks_found / len(gold_peaks)

    return 0.5 * shape_score + 0.5 * peak_score


# === block: score_2 (check id='heat_capacity') ===
def score_2(artifact, step, ctx):
    artifact # list of dicts with 'temperature','Cv'
    ctx_dos = ctx.get('dos')
    if ctx_dos is None:
        return 0.0
    bin_centers = np.array(ctx_dos.get('bin_centers', []))
    density = np.array(ctx_dos.get('density', []))
    if len(bin_centers) == 0 or len(density) == 0:
        return 0.0

    # Physical constants
    hc_over_k = 1.43877736  # cm·K  (h*c/k_B)
    R_cal = 1.9872042586     # cal/mol/K

    # --- Part 1: Self-consistency gate (recompute Cv from submitted DOS) ---
    reported = {}
    for entry in artifact:
        reported[float(entry['temperature'])] = float(entry['Cv'])
    if not reported:
        return 0.0

    max_abs_diff = 0.0
    for T, cv_reported in reported.items():
        if T == 0.0:
            cv_recomp = 0.0
        else:
            x_vals = hc_over_k * bin_centers / T
            exp_x = np.exp(np.clip(x_vals, None, 100.0))
            mask = exp_x > 1.0
            safe_x = x_vals[mask]
            safe_exp_x = exp_x[mask]
            integrand = np.zeros_like(x_vals)
            with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
                integrand[mask] = (safe_x**2 * safe_exp_x) / ((safe_exp_x - 1.0)**2)
            # x -> 0 limit: x^2 e^x / (e^x - 1)^2 -> 1
            small = (x_vals < 0.01) & (~mask)
            integrand[small] = 1.0
            cv_recomp = 5.0 * R_cal * np.sum(density * integrand)
        diff = abs(cv_recomp - cv_reported)
        if diff > max_abs_diff:
            max_abs_diff = diff

    consistency_tol = step.get('self_consistency_tolerance', 0.1)
    if max_abs_diff > consistency_tol:
        return 0.0  # self-consistency is a hard gate

    # --- Part 2: Reference comparison to paper experimental heat capacity ---
    # Use hardcoded digitized values from Fig. 4 (Oliver et al. 1937) at selected temperatures.
    gold_ref = step.get('gold_Cv_reference', {})
    if not gold_ref:
        gold_ref = {
            "20.0": 1.0,
            "50.0": 6.5,
            "100.0": 11.0
        }

    ref_tol = step.get('reference_tolerance', 2.0)
    temps_agent = np.array(sorted(reported.keys()))
    cvs_agent = np.array([reported[t] for t in temps_agent])

    matches = 0
    total_ref = 0
    for T_ref_str, cv_ref in gold_ref.items():
        T_ref = float(T_ref_str)
        cv_ref = float(cv_ref)
        total_ref += 1
        idx = np.argmin(np.abs(temps_agent - T_ref))
        if abs(cvs_agent[idx] - cv_ref) <= ref_tol:
            matches += 1

    if total_ref == 0:
        return 1.0
    return matches / total_ref


# === block: score_3 (check id='lattice_energy') ===
def score_3(artifact, step, ctx):
    artifact_text = artifact  # string content
    if artifact_text is None:
        return 0.0
    try:
        val = float(artifact_text.strip())
    except Exception:
        return 0.0
    gold = step.get('gold_value', -9.06)
    tol = step.get('tolerance', 0.5)
    if abs(val - gold) <= tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'zone_center_frequencies': score_0,
    'density_of_states': score_1,
    'heat_capacity': score_2,
    'lattice_energy': score_3,
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
