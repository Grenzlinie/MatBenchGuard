import os
import json
import csv

# === author imports / helpers ===
import math


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
    return {"spec": spec}


# === block: score_0 (check id='radial_profile_check') ===
def score_0(artifact, step, ctx):
    data = sorted(artifact, key=lambda row: float(row['r0_um']))
    r_vals = [float(r['r0_um']) for r in data]
    j_vals = [float(r['Jprime_A']) for r in data]
    if len(r_vals)==0: return 0.0
    max_j = max(j_vals)
    max_idx = j_vals.index(max_j)
    peak_r = r_vals[max_idx]
    half_max = max_j / 2.0
    # find left crossing
    left_r = r_vals[0]
    for i in range(len(r_vals)-1):
        if j_vals[i] <= half_max and j_vals[i+1] > half_max:
            left_r = r_vals[i] + (half_max - j_vals[i]) * (r_vals[i+1]-r_vals[i]) / (j_vals[i+1]-j_vals[i])
            break
    right_r = r_vals[-1]
    for i in range(len(r_vals)-1, 0, -1):
        if j_vals[i] <= half_max and j_vals[i-1] > half_max:
            right_r = r_vals[i-1] + (half_max - j_vals[i-1]) * (r_vals[i]-r_vals[i-1]) / (j_vals[i]-j_vals[i-1])
            break
    fwhm = right_r - left_r
    peak_gold = step['peak_radius_gold']
    fwhm_gold = step['fwhm_gold']
    peak_tol = step['peak_radius_tol']
    fwhm_tol = step['fwhm_tol']
    min_radius = step['annulus_min_radius']
    peak_diff = abs(peak_r - peak_gold)
    peak_score = 1.0 if peak_diff <= peak_tol else max(0, 1 - (peak_diff - peak_tol) / (peak_gold * 0.5))
    fwhm_diff = abs(fwhm - fwhm_gold)
    fwhm_score = 1.0 if fwhm_diff <= fwhm_tol else max(0, 1 - (fwhm_diff - fwhm_tol) / (fwhm_gold * 0.5))
    annulus_score = 1.0 if peak_r > min_radius else 0.0
    return 0.4 * peak_score + 0.4 * fwhm_score + 0.2 * annulus_score


# === block: score_1 (check id='angular_distribution_check') ===
def score_1(artifact, step, ctx):
    data = sorted(artifact, key=lambda row: float(row['theta_deg']))
    theta = [float(r['theta_deg']) for r in data]
    I = [float(r['I_theta']) for r in data]
    if len(theta)==0: return 0.0
    def integrate(theta_list, I_list, t0, t1):
        total = 0.0
        for i in range(len(theta_list)-1):
            t_i = theta_list[i]
            t_j = theta_list[i+1]
            if t_j < t0:
                continue
            if t_i > t1:
                break
            a = max(t_i, t0)
            b = min(t_j, t1)
            if b <= a:
                continue
            I_i = I_list[i]
            I_j = I_list[i+1]
            dt = t_j - t_i
            if dt == 0:
                avg = I_i
            else:
                avg = I_i + (I_j - I_i) * ((a+b)/2 - t_i) / dt
            total += avg * (b - a)
        return total
    total = integrate(theta, I, 0, step['max_angle_deg'])
    partial = integrate(theta, I, 0, step['analyzer_angle_deg'])
    eta = partial / total if total > 0 else 0.0
    eta_gold = step['eta_gold']
    eta_tol = step['eta_tol']
    eta_diff = abs(eta - eta_gold)
    eta_score = 1.0 if eta_diff <= eta_tol else max(0, 1 - (eta_diff - eta_tol) / (eta_gold * 0.5))
    conc_partial = integrate(theta, I, 0, step['angular_concentration_threshold_deg'])
    conc_frac = conc_partial / total if total > 0 else 0.0
    shape_score = 1.0 if conc_frac >= step['angular_concentration_frac_min'] else 0.0
    return 0.8 * eta_score + 0.2 * shape_score


_SCORERS = {
    'radial_profile_check': score_0,
    'angular_distribution_check': score_1,
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
