import os
import json
import csv

# === author imports / helpers ===
import csv, math, cmath


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
    ctx = {'gold_tables': {}}
    for step in spec['steps']:
        sid = step['id']
        if sid == 'planar_fresnel':
            eps_Ag = {float(k): complex(*v) for k,v in step['eps_Ag'].items()}
            c = step['c']; eps_d = step['eps_d']; l0_nm = step['l0_nm']
            omega0 = 2*math.pi*c/(l0_nm*1e-9)
            expected = {}
            for lR_nm in step['raman_shift_nm_list']:
                epsR = eps_Ag[lR_nm]; omegaR = 2*math.pi*c/(lR_nm*1e-9)
                for theta0_deg in step['angles_deg']:
                    theta0 = math.radians(theta0_deg)
                    q = math.sqrt(eps_d)*(omega0/c)*math.sin(theta0)
                    alpha0_0 = cmath.sqrt(eps_d*(omega0/c)**2 - q**2)
                    eps0 = eps_Ag[l0_nm]
                    alpha0 = cmath.sqrt(eps0*(omega0/c)**2 - q**2)
                    Rp0 = (eps0*alpha0_0 - eps_d*alpha0)/(eps0*alpha0_0 + eps_d*alpha0)
                    Rs0 = (alpha0_0 - alpha0)/(alpha0_0 + alpha0)
                    alphaR_0 = cmath.sqrt(eps_d*(omegaR/c)**2 - q**2)
                    alphaR = cmath.sqrt(epsR*(omegaR/c)**2 - q**2)
                    mu = 0.5*(1.0/(eps_d**2) + 1.0/(eps0*epsR))
                    factor = -4j*math.pi*(omegaR/omega0)
                    denom_p = epsR*alphaR_0 + eps_d*alphaR
                    Rp_par = factor * (alpha0_0*eps_d*alphaR*(1.0 - Rp0))/denom_p
                    Rp_perp = -factor * (epsR*mu*q**2*(1.0 + Rp0))/denom_p
                    Rs = 4j*math.pi*(omega0*omegaR/(c**2))*(1.0 + Rs0)/(alphaR_0 + alphaR)
                    expected[(theta0_deg, lR_nm)] = (abs(Rp_par)**2, abs(Rp_perp)**2, abs(Rs)**2)
            ctx['gold_tables'][sid] = expected
        else:
            ctx['gold_tables'][sid] = step['gold_rows']
    return ctx


# === block: score_0 (check id='planar_fresnel') ===
def score_0(artifact, step, ctx):
    import cmath, math

    eps_Ag = {float(k): complex(v[0], v[1]) for k,v in step['eps_Ag'].items()}
    c = step['c']
    eps_d = step['eps_d']
    l0_nm = step['l0_nm']
    omega0 = 2*math.pi*c/(l0_nm*1e-9)
    tol = step['tolerance_relative']

    expected = {}
    for lR_nm in step['raman_shift_nm_list']:
        epsR = eps_Ag[lR_nm]
        omegaR = 2*math.pi*c/(lR_nm*1e-9)
        for theta0_deg in step['angles_deg']:
            theta0 = math.radians(theta0_deg)
            q = math.sqrt(eps_d)*(omega0/c)*math.sin(theta0)
            # pump Fresnel coefficients
            alpha0_0 = cmath.sqrt(eps_d*(omega0/c)**2 - q**2)
            eps0 = eps_Ag[l0_nm]
            alpha0 = cmath.sqrt(eps0*(omega0/c)**2 - q**2)
            Rp0 = (eps0*alpha0_0 - eps_d*alpha0)/(eps0*alpha0_0 + eps_d*alpha0)
            Rs0 = (alpha0_0 - alpha0)/(alpha0_0 + alpha0)
            # Fresnel coefficients at Raman frequency
            alphaR_0 = cmath.sqrt(eps_d*(omegaR/c)**2 - q**2)
            alphaR = cmath.sqrt(epsR*(omegaR/c)**2 - q**2)
            RpR = (epsR*alphaR_0 - eps_d*alphaR)/(epsR*alphaR_0 + eps_d*alphaR)
            RsR = (alphaR_0 - alphaR)/(alphaR_0 + alphaR)
            # normalized effective Raman Fresnel coefficients (Eqs. 13‑15)
            R_ppar_norm = (1.0 - RpR) * (1.0 - Rp0)
            R_pperp_norm = (1.0 + RpR) * (1.0 + Rp0)
            R_s_norm = (1.0 + RsR) * (1.0 + Rs0)
            expected[(theta0_deg, lR_nm)] = (
                abs(R_ppar_norm)**2,
                abs(R_pperp_norm)**2,
                abs(R_s_norm)**2
            )

    total = 0.0
    count = 0
    for row in artifact:
        try:
            angle = float(row['incident_angle_deg'])
            shift = float(row['raman_shift_nm'])
        except (KeyError, ValueError):
            continue
        key = (angle, shift)
        if key not in expected:
            continue
        ref = expected[key]
        max_err = 0.0
        for i, col in enumerate(['R_ppar_sq', 'R_pperp_sq', 'R_s_sq']):
            val = float(row[col])
            ref_val = ref[i]
            if ref_val == 0.0:
                err = abs(val)
            else:
                err = abs(val - ref_val) / abs(ref_val)
            if err > max_err:
                max_err = err
        row_score = 1.0 if max_err <= tol else max(0.0, 1.0 - (max_err - tol) / 0.5)
        total += row_score
        count += 1
    return total / count if count > 0 else 0.0


# === block: score_1 (check id='rough_sers_wavelength') ===
def score_1(artifact, step, ctx):
    tol_peak = 40   # nm around expected peak
    peak_expected = 620.0
    min_ratio = 10.0   # paper: up to 10² factor

    wl_list = []
    c_list = []
    a_list = []
    for row in artifact:
        try:
            w = float(row['pump_wavelength_nm'])
            c = float(row['G_SERS_collective'])
            a = float(row['G_SERS_approx'])
        except (KeyError, ValueError):
            continue
        wl_list.append(w)
        c_list.append(c)
        a_list.append(a)

    if len(wl_list) < 3:
        return 0.0

    # locate peak using the larger (approx) signal
    peak_idx = max(range(len(a_list)), key=lambda i: a_list[i])
    peak_wl = wl_list[peak_idx]
    peak_coll = c_list[peak_idx]
    peak_approx = a_list[peak_idx]

    # 1. peak location (0.25 weight)
    dist = abs(peak_wl - peak_expected)
    if dist <= tol_peak:
        loc_score = 1.0
    else:
        loc_score = max(0.0, 1.0 - (dist - tol_peak) / (tol_peak * 2))

    # 2. overestimation ratio at peak (0.35)
    ratio = peak_approx / peak_coll if peak_coll > 0 else 0.0
    ratio_score = 1.0 if ratio >= min_ratio else (ratio / min_ratio) if ratio > 0 else 0.0

    # 3. collective always lower than approximation (0.25)
    all_lower = all(a > c for c, a in zip(c_list, a_list))
    order_score = 1.0 if all_lower else 0.0

    # 4. roughly unimodal (left increasing, right decreasing) (0.15)
    left = a_list[:peak_idx]
    right = a_list[peak_idx+1:]
    inc = True
    if len(left) > 1:
        inc = all(left[i] <= left[i+1] for i in range(len(left)-1))
    dec = True
    if len(right) > 1:
        dec = all(right[i] >= right[i+1] for i in range(len(right)-1))
    shape_score = 1.0 if inc and dec else 0.0

    final = 0.25 * loc_score + 0.35 * ratio_score + 0.25 * order_score + 0.15 * shape_score
    return max(0.0, min(1.0, final))


# === block: score_2 (check id='rough_sers_raman') ===
def score_2(artifact, step, ctx):
    shifts = []
    colls = []
    approxs = []
    for row in artifact:
        try:
            s = float(row['fractional_raman_shift'])
            c = float(row['G_SERS_collective'])
            a = float(row['G_SERS_approx'])
            shifts.append(s)
            colls.append(c)
            approxs.append(a)
        except (KeyError, ValueError):
            continue

    n = len(shifts)
    if n < 3:
        return 0.0

    # 1. approx always > collective (0.35 weight)
    all_greater = all(a > c for c, a in zip(colls, approxs))
    order_score = 1.0 if all_greater else 0.0

    # 2. peak at zero shift (0.25 weight)
    peak_idx = max(range(n), key=lambda i: approxs[i])
    peak_shift = shifts[peak_idx]
    peak_tol = 0.02
    if abs(peak_shift) < peak_tol:
        peak_score = 1.0
    else:
        peak_score = max(0.0, 1.0 - (abs(peak_shift) - peak_tol) / 0.05)

    # 3. monotonic decay as |shift| increases (0.25 weight)
    abs_shifts = [abs(s) for s in shifts]
    sorted_idx = sorted(range(n), key=lambda i: abs_shifts[i])
    def check_monotonic(vals, idxs):
        for i in range(len(idxs)-1):
            if vals[idxs[i+1]] > vals[idxs[i]] + 1e-9:
                return False
        return True
    mono_coll = check_monotonic(colls, sorted_idx)
    mono_approx = check_monotonic(approxs, sorted_idx)
    decay_score = (1.0 if mono_coll else 0.0) * 0.5 + (1.0 if mono_approx else 0.0) * 0.5

    # 4. overestimation ratio at peak (0.15 weight)
    peak_coll = colls[peak_idx]
    peak_approx = approxs[peak_idx]
    ratio = peak_approx / peak_coll if peak_coll > 0 else 0.0
    min_ratio = 10.0   # paper states up to 10^2 factor
    ratio_score = min(ratio / min_ratio, 1.0) if ratio > 0 else 0.0

    final = 0.35 * order_score + 0.25 * peak_score + 0.25 * decay_score + 0.15 * ratio_score
    return max(0.0, min(1.0, final))


_SCORERS = {
    'planar_fresnel': score_0,
    'rough_sers_wavelength': score_1,
    'rough_sers_raman': score_2,
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
