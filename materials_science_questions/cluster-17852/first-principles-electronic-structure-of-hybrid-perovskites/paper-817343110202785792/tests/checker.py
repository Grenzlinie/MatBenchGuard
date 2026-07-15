import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import json

def _interp1d(x, y, xq):
    # simple linear interpolation; x must be sorted ascending
    if xq <= x[0]: return y[0]
    if xq >= x[-1]: return y[-1]
    for i in range(len(x)-1):
        if x[i] <= xq <= x[i+1]:
            t = (xq - x[i])/(x[i+1]-x[i])
            return y[i] + t*(y[i+1]-y[i])
    return 0.0


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
    # Parse hidden solar irradiance from grading_spec
    solar_data = spec.get('hidden_solar_irradiance', [[310,0.5],[400,1.0],[700,1.0],[830,0.5]])
    wl_sun = [p[0] for p in solar_data]
    I_sun_vals = [p[1] for p in solar_data]
    def I_sun(wl):
        return _interp1d(wl_sun, I_sun_vals, wl)
    return {'I_sun': I_sun}


# === block: score_0 (check id='step_absorption_ratio') ===
def score_0(artifact, step, ctx):
    # Artifact: list of dicts with columns wavelength_nm, alpha_Fe_xx_cm1, etc.
    rows = artifact
    if not rows:
        return 0.0
    I_sun = ctx['I_sun']
    # extract arrays
    wls = []
    alpha_Fe = []
    alpha_Pb = []
    for r in rows:
        try:
            wl = float(r['wavelength_nm'])
            aFe_xx = float(r['alpha_Fe_xx_cm1'])
            aFe_yy = float(r['alpha_Fe_yy_cm1'])
            aFe_zz = float(r['alpha_Fe_zz_cm1'])
            aPb_xx = float(r['alpha_Pb_xx_cm1'])
            aPb_yy = float(r['alpha_Pb_yy_cm1'])
            aPb_zz = float(r['alpha_Pb_zz_cm1'])
            wls.append(wl)
            alpha_Fe.append((aFe_xx + aFe_yy + aFe_zz) / 3.0)
            alpha_Pb.append((aPb_xx + aPb_yy + aPb_zz) / 3.0)
        except (ValueError, KeyError):
            continue
    if len(wls) < 2:
        return 0.0
    # sort by wavelength
    idx = sorted(range(len(wls)), key=lambda i: wls[i])
    wls_sorted = [wls[i] for i in idx]
    alpha_Fe_sorted = [alpha_Fe[i] for i in idx]
    alpha_Pb_sorted = [alpha_Pb[i] for i in idx]
    # integrate using trapezoidal rule
    I_vals = [I_sun(w) for w in wls_sorted]
    def trapz(x, y):
        return sum(0.5*(y[i]+y[i+1])*(x[i+1]-x[i]) for i in range(len(x)-1))
    integral_I = trapz(wls_sorted, I_vals)
    if integral_I == 0:
        return 0.0
    integral_Fe_num = trapz(wls_sorted, [alpha_Fe_sorted[i]*I_vals[i] for i in range(len(wls_sorted))])
    integral_Pb_num = trapz(wls_sorted, [alpha_Pb_sorted[i]*I_vals[i] for i in range(len(wls_sorted))])
    integral_Fe_den = trapz(wls_sorted, alpha_Fe_sorted)
    integral_Pb_den = trapz(wls_sorted, alpha_Pb_sorted)
    if integral_Fe_den == 0 or integral_Pb_den == 0:
        return 0.0
    C_Fe = integral_Fe_num / (integral_Fe_den * integral_I)
    C_Pb = integral_Pb_num / (integral_Pb_den * integral_I)
    ratio_R = C_Fe / C_Pb
    # threshold_or_better: better is higher ratio
    if ratio_R >= 0.51:
        return 1.0
    elif ratio_R >= 0.30:
        return (ratio_R - 0.30) / 0.21
    else:
        return 0.0


# === block: score_1 (check id='step_brewster_factor') ===
def score_1(artifact, step, ctx):
    # Artifact: list of dicts with wavelength_nm, n_Fe_xx, n_Fe_yy, n_Fe_zz, n_Pb_xx, n_Pb_yy, n_Pb_zz
    rows = artifact
    if not rows:
        return 0.0
    wls = []
    n_Fe_avg = []
    n_Pb_avg = []
    for r in rows:
        try:
            wl = float(r['wavelength_nm'])
            nFe_xx = float(r['n_Fe_xx'])
            nFe_yy = float(r['n_Fe_yy'])
            nFe_zz = float(r['n_Fe_zz'])
            nPb_xx = float(r['n_Pb_xx'])
            nPb_yy = float(r['n_Pb_yy'])
            nPb_zz = float(r['n_Pb_zz'])
            wls.append(wl)
            n_Fe_avg.append((nFe_xx + nFe_yy + nFe_zz) / 3.0)
            n_Pb_avg.append((nPb_xx + nPb_yy + nPb_zz) / 3.0)
        except (ValueError, KeyError):
            continue
    if len(wls) < 2:
        return 0.0
    # interpolation at 600 nm
    n_Fe = _interp1d(wls, n_Fe_avg, 600.0)
    n_Pb = _interp1d(wls, n_Pb_avg, 600.0)
    # hidden indices
    n_TiO2 = 2.5
    n_spiro = 1.7
    # Brewster angles (atan(n2/n1) where light goes from medium1 to medium2)
    theta_TiO2_Fe = math.atan(n_Fe / n_TiO2)
    theta_TiO2_Pb = math.atan(n_Pb / n_TiO2)
    theta_spiro_Fe = math.atan(n_spiro / n_Fe)
    theta_spiro_Pb = math.atan(n_spiro / n_Pb)
    if theta_TiO2_Pb == 0 or theta_spiro_Fe == 0:
        return 0.0
    r12 = theta_TiO2_Fe / theta_TiO2_Pb
    r23 = theta_spiro_Pb / theta_spiro_Fe
    R_B = r12 * r23
    # threshold_or_better: better is larger R_B
    if R_B >= 1.30:
        return 1.0
    elif R_B >= 1.0:
        return (R_B - 1.0) / 0.30
    else:
        return 0.0


_SCORERS = {
    'step_absorption_ratio': score_0,
    'step_brewster_factor': score_1,
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
