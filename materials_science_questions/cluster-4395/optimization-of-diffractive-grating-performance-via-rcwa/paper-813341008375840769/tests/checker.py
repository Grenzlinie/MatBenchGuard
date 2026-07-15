import os
import json
import csv

# === author imports / helpers ===
import csv, os, json, math


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


# === block: score_0 (check id='step_01_efficiency_table') ===
def score_0(artifact, step, ctx):
    rows = artifact
    gold_dict = step['config']['duty_cycle_gold']
    optimal_cfg = step['config']['optimal_row']
    score = 0.0
    checks = 0
    total = 0

    # gold keys are percentages (e.g. '48.9'); convert to fraction for matching
    for dc_str, vals in gold_dict.items():
        dc_frac = float(dc_str) / 100.0
        found_row = None
        for row in rows:
            try:
                if abs(float(row['duty_cycle']) - dc_frac) < 1e-3:
                    found_row = row
                    break
            except: continue
        if found_row:
            m1 = float(found_row['efficiency_m1'])
            p1 = float(found_row['efficiency_p1'])
            p0 = float(found_row['efficiency_0'])
            tol = vals['tolerance_abs']
            if abs(m1 - vals['efficiency_m1']) <= tol and abs(p1 - vals['efficiency_p1']) <= tol:
                checks += 1
            if p0 <= vals['P0_max']:
                checks += 1
            total += 2
        # else row missing => no score

    # optimal separate row (duty_cycle already a fraction)
    found_opt = None
    for row in rows:
        try:
            if abs(float(row['duty_cycle']) - optimal_cfg['duty_cycle']) < 1e-3 and abs(float(row['incidence_angle_deg']) - optimal_cfg['incidence_angle_deg']) < optimal_cfg['angle_tol_deg']:
                found_opt = row
                break
        except: continue
    if found_opt:
        m1 = float(found_opt['efficiency_m1'])
        p1 = float(found_opt['efficiency_p1'])
        p0 = float(found_opt['efficiency_0'])
        if abs(m1 - optimal_cfg['efficiency_m1_target']) <= optimal_cfg['efficiency_tol_abs']:
            checks += 1
        if abs(p1 - optimal_cfg['efficiency_p1_target']) <= optimal_cfg['efficiency_tol_abs']:
            checks += 1
        if p0 <= optimal_cfg['P0_max']:
            checks += 1
        total += 3

    score = checks / total if total > 0 else 0.0
    return score


# === block: score_1 (check id='step_02_polarization') ===
def score_1(artifact, step, ctx):
    rows = artifact
    cfg = step['config']
    if not rows:
        return 0.0

    m1_vals = []
    p1_vals = []
    diffs = []
    for row in rows:
        try:
            m1 = float(row['efficiency_m1'])
            p1 = float(row['efficiency_p1'])
            m1_vals.append(m1)
            p1_vals.append(p1)
            diffs.append(abs(m1 - p1))
        except: continue

    if not m1_vals:
        return 0.0

    symmetry_pass = all(d <= cfg['symmetry_tol_abs'] for d in diffs)
    m1_range = max(m1_vals) - min(m1_vals) if m1_vals else 1.0
    p1_range = max(p1_vals) - min(p1_vals) if p1_vals else 1.0
    variation_pass = m1_range <= cfg['variation_tol_abs'] and p1_range <= cfg['variation_tol_abs']

    score = 0.0
    if symmetry_pass:
        score += 0.5
    if variation_pass:
        score += 0.5
    return score


# === block: score_2 (check id='step_03_angular_phi') ===
def score_2(artifact, step, ctx):
    rows = artifact
    cfg = step['config']
    if not rows:
        return 0.0

    angles = []
    m1s = []
    p1s = []
    p0s = []
    for row in rows:
        try:
            ang = float(row['incidence_angle_deg'])
            m1 = float(row['efficiency_m1'])
            p1 = float(row['efficiency_p1'])
            p0 = float(row['efficiency_0'])
            angles.append(ang)
            m1s.append(m1)
            p1s.append(p1)
            p0s.append(p0)
        except: continue

    if not angles:
        return 0.0

    # find minimum P0
    p0_min_val = min(p0s)
    p0_min_idx = p0s.index(p0_min_val)
    p0_min_angle = angles[p0_min_idx]

    score = 0.0
    # check P0 min angle close to target
    if abs(p0_min_angle - cfg['P0_min_angle_target']) <= cfg['angle_tol_deg']:
        score += 0.4
    # check P0 min value small
    if p0_min_val <= cfg['P0_min_max']:
        score += 0.2
    # check ±1 efficiencies at minimum close to target
    if abs(m1s[p0_min_idx] - cfg['efficiency_m1_approx']) <= cfg['efficiency_tol_abs'] and abs(p1s[p0_min_idx] - cfg['efficiency_p1_approx']) <= cfg['efficiency_tol_abs']:
        score += 0.2
    # quick monotonicity check: P0 should increase as we move away from min
    left_increase = True
    right_increase = True
    for i in range(1, p0_min_idx+1):
        if p0s[i-1] > p0s[i]:
            left_increase = False
            break
    for i in range(p0_min_idx+1, len(angles)):
        if p0s[i-1] < p0s[i]:
            right_increase = False
            break
    if left_increase and right_increase:
        score += 0.2
    return score


# === block: score_3 (check id='step_04_angular_dpsi') ===
def score_3(artifact, step, ctx):
    rows = artifact
    cfg = step['config']
    if not rows:
        return 0.0

    # find row with tilt_angle_deg == 0.0 (close)
    zero_rows = []
    for row in rows:
        try:
            if abs(float(row['tilt_angle_deg'])) < 1e-4:
                zero_rows.append(row)
        except: continue
    if not zero_rows:
        return 0.0
    # use first
    r = zero_rows[0]
    m1 = float(r['efficiency_m1'])
    p1 = float(r['efficiency_p1'])
    p0 = float(r['efficiency_0'])
    score = 0.0
    if abs(m1 - p1) <= cfg['symmetry_at_zero_tol_abs']:
        score += 0.4
    if p0 <= cfg['P0_at_zero_max']:
        score += 0.3
    # also check overall symmetry across other entries? optional
    sym_all = True
    for row in rows:
        try:
            m1v = float(row['efficiency_m1'])
            p1v = float(row['efficiency_p1'])
            if abs(m1v - p1v) > cfg['symmetry_at_zero_tol_abs']:
                sym_all = False
                break
        except: continue
    if sym_all:
        score += 0.3
    return score


# === block: score_4 (check id='step_05_wavelength') ===
def score_4(artifact, step, ctx):
    rows = artifact
    cfg = step['config']
    target_wl = cfg['target_wavelength_nm']
    found = None
    for row in rows:
        try:
            if abs(float(row['wavelength_nm']) - target_wl) < 0.01:
                found = row
                break
        except: continue
    if not found:
        return 0.0
    m1 = float(found['efficiency_m1'])
    p1 = float(found['efficiency_p1'])
    p0 = float(found['efficiency_0'])
    score = 0.0
    if abs(m1 - cfg['efficiency_m1_target']) <= cfg['tol_abs'] and abs(p1 - cfg['efficiency_p1_target']) <= cfg['tol_abs']:
        score += 0.6
    if p0 <= cfg['P0_max']:
        score += 0.4
    return score


# === block: score_5 (check id='step_06_tilt_sample') ===
def score_5(artifact, step, ctx):
    rows = artifact
    # Corrected gold from paper Table 2: P+-1 = 35.3% (0.353) for duty cycle 54.7%
    gold_m1 = 0.353
    gold_p1 = 0.353
    tol_abs = 0.02
    P0_max = 0.005

    # find row with tilt_angle_deg == 0
    zero_row = None
    for row in rows:
        try:
            if abs(float(row['tilt_angle_deg'])) < 1e-4:
                zero_row = row
                break
        except: continue
    if not zero_row:
        return 0.0
    m1 = float(zero_row['efficiency_m1'])
    p1 = float(zero_row['efficiency_p1'])
    p0 = float(zero_row['efficiency_0'])
    score = 0.0
    if abs(m1 - gold_m1) <= tol_abs and abs(p1 - gold_p1) <= tol_abs:
        score += 0.6
    if p0 <= P0_max:
        score += 0.4
    return score


_SCORERS = {
    'step_01_efficiency_table': score_0,
    'step_02_polarization': score_1,
    'step_03_angular_phi': score_2,
    'step_04_angular_dpsi': score_3,
    'step_05_wavelength': score_4,
    'step_06_tilt_sample': score_5,
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
