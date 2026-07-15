import os
import json
import csv

# === author imports / helpers ===
import os
import json
import numpy as np
from scipy.optimize import curve_fit, bisect
from scipy.integrate import quad

# WKB constants and unit conversions
MU_U = 7.3938
U_TO_ME = 1822.888484  # 1 u = 1822.888 electronic masses
MU_AU = MU_U * U_TO_ME
PI = np.pi

BOHR_PER_A = 0.52917721092
AU_TO_KCAL = 627.509474
AU_TO_CM1 = 219474.63

def morse_v(x, V0, gamma_A, xmin_A):
    """Morse potential in atomic units; x in Bohr, gamma_A in A^-1 converted to Bohr^-1."""
    gamma_bohr = gamma_A * BOHR_PER_A
    xmin_bohr = xmin_A / BOHR_PER_A
    dx = x - xmin_bohr
    return V0 * ((1.0 - np.exp(-gamma_bohr * dx))**2 - 1.0)

def morse_fit_func(x_A, V0, gamma, xmin_A):
    """For curve fitting: x in A, returns potential in au."""
    dx = x_A - xmin_A
    return V0 * ((1.0 - np.exp(-gamma * dx))**2 - 1.0)

def compute_wkb_energies(V0, gamma_A, xmin_A):
    """Return list of bound state energies (au) for Morse potential using WKB.
    Quantization: integral sqrt(2*mu*(E-V))dx = h/2 (n+0.5) with h=2pi au -> pi*(n+0.5)."""
    gamma_bohr = gamma_A * BOHR_PER_A
    xmin_bohr = xmin_A / BOHR_PER_A
    # function for integrand
    def integrand(x, E):
        V = morse_v(x, V0, gamma_A, xmin_A)
        return np.sqrt(2.0 * MU_AU * (E - V))
    # I(E) = integral between turning points
    def I_E(E):
        # turning points analytical for Morse
        inner = 1.0 + E/V0
        if inner <= 0.0:
            return 0.0
        sqrt_inner = np.sqrt(inner)
        x1 = xmin_bohr - (1.0/gamma_bohr) * np.log(1.0 - sqrt_inner)
        x2 = xmin_bohr - (1.0/gamma_bohr) * np.log(1.0 + sqrt_inner)
        res, _ = quad(integrand, x1, x2, args=(E,), limit=200, epsabs=1e-12)
        return res
    # find all bound states
    energies = []
    n = 0
    while True:
        target = PI * (n + 0.5)
        f = lambda E: I_E(E) - target
        E_upper = 0.0
        E_lower = -V0
        # check if bracket exists
        try:
            root = bisect(f, E_lower, E_upper, xtol=1e-12, maxiter=200)
        except ValueError:
            break
        energies.append(root)
        n += 1
        if n > 10:  # safety
            break
    return energies


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
    path_curve = os.path.join(outputs_dir, "step_04_potential_curve.csv")
    import csv
    rows = []
    if os.path.exists(path_curve):
        with open(path_curve, newline='') as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)
    else:
        rows = []
    curve_data = rows
    # check shape
    valid_curve = len(rows) == 35
    r_A = []
    energy_au = []
    if valid_curve:
        for r in rows:
            try:
                ra = float(r.get("r_A", ""))
                e = float(r.get("energy_au", ""))
            except (ValueError, TypeError):
                valid_curve = False
                break
            r_A.append(ra)
            energy_au.append(e)
    else:
        valid_curve = False
    # fit Morse
    if valid_curve and len(r_A) == 35:
        x_arr = np.array(r_A)
        y_arr = np.array(energy_au)
        try:
            popt, pcov = curve_fit(morse_fit_func, x_arr, y_arr, p0=[0.003, 0.87, 3.0], maxfev=10000)
            V0_fit, gamma_fit, xmin_fit = popt
            y_pred = morse_fit_func(x_arr, *popt)
            rms = np.sqrt(np.mean((y_arr - y_pred)**2))
        except Exception:
            # fitting failed
            V0_fit, gamma_fit, xmin_fit = 0.0, 0.0, 0.0
            rms = 1.0
    else:
        V0_fit, gamma_fit, xmin_fit = 0.0, 0.0, 0.0
        rms = 1.0
    ctx = {
        "valid_curve": valid_curve,
        "curve_r_A": r_A,
        "curve_energy_au": energy_au,
        "refit_V0": V0_fit,
        "refit_gamma": gamma_fit,
        "refit_xmin_A": xmin_fit,
        "refit_rms": rms
    }
    return ctx


# === block: score_0 (check id='step_02') ===
def score_0(artifact, step, ctx):
    data = artifact
    target = step.get("target", {})
    tol_rel = float(step.get("tolerance", 0.005))
    scores = []
    for field in ["A_MHz", "B_MHz", "C_MHz"]:
        val = data.get(field)
        tgt = target.get(field)
        if val is None or tgt is None or tgt == 0:
            scores.append(0.0)
        else:
            rel_err = abs(val - tgt) / abs(tgt)
            if rel_err <= tol_rel:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel))
    return float(np.mean(scores))


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    data = artifact
    tgt = float(step["target"]["D0_kcal_mol"])
    tol = float(step.get("tolerance_abs", 0.10))
    val = data.get("D0_kcal_mol")
    if val is None:
        return 0.0
    err = abs(val - tgt)
    if err <= tol:
        return 1.0
    elif err <= 2*tol:
        return max(0.0, 1.0 - (err - tol) / tol)
    else:
        return 0.0


# === block: score_2 (check id='step_04') ===
def score_2(artifact, step, ctx):
    valid = ctx.get("valid_curve", False)
    shape_score = 1.0 if valid else 0.0
    if not valid:
        return 0.0
    V0_ref = ctx.get("refit_V0", 0.0)
    gamma_ref = ctx.get("refit_gamma", 0.0)
    target = step.get("target", {})
    tols = step.get("tolerances", {})
    tgt_V0 = target.get("V0_au", 0.00305)
    tgt_gamma = target.get("gamma", 0.86897)
    tol_V0 = tols.get("V0_au", 0.0002)
    tol_gamma = tols.get("gamma", 0.02)
    def score_param(val, tgt, tol):
        err = abs(val - tgt)
        if err <= tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (err - tol) / tol)
    s_V0 = score_param(V0_ref, tgt_V0, tol_V0)
    s_gamma = score_param(gamma_ref, tgt_gamma, tol_gamma)
    return 0.4 * shape_score + 0.3 * s_V0 + 0.3 * s_gamma


# === block: score_3 (check id='step_05') ===
def score_3(artifact, step, ctx):
    data = artifact
    target = step.get("target", {})
    field_tols = step.get("field_tolerances", {})
    def score_field(val, tgt, tol_info):
        if val is None or tgt is None:
            return 0.0
        if tol_info["type"] == "absolute":
            tol = float(tol_info["tol"])
            err = abs(val - tgt)
            return 1.0 if err <= tol else max(0.0, 1.0 - (err - tol) / tol)
        elif tol_info["type"] == "threshold_upper":
            th = float(tol_info["threshold"])
            if val <= th:
                return 1.0
            else:
                return max(0.0, 1.0 - (val - th) / (th * 0.5))
        else:
            return 0.0
    weights = {"V0_au": 0.3, "gamma": 0.3, "x_min_A": 0.2, "rms_deviation_au": 0.2}
    total = 0.0
    for field, w in weights.items():
        tgt = target.get(field)
        if tgt is None:
            continue
        tol_info = field_tols.get(field)
        if tol_info is None:
            continue
        s = score_field(data.get(field), tgt, tol_info)
        total += w * s
    return total


# === block: score_4 (check id='step_06') ===
def score_4(artifact, step, ctx):
    data = artifact
    # Load Morse parameters from step_05
    path_step05 = os.path.join("/app/outputs", "step_05_morse_fit_params.json")
    if not os.path.exists(path_step05):
        return 0.0
    with open(path_step05) as f:
        morse_params = json.load(f)
    V0 = morse_params.get("V0_au")
    gamma = morse_params.get("gamma")
    xmin = morse_params.get("x_min_A")
    if None in (V0, gamma, xmin) or V0 <= 0 or gamma <= 0:
        return 0.0
    # recompute WKB energies
    computed_energies = compute_wkb_energies(V0, gamma, xmin)
    n_comp = len(computed_energies)
    # paper targets from spec
    target = step["target"]
    tgt_n = target["n_bound_states"]
    tgt_energies = target["energies_au"]
    tgt_fund = target["fundamental_cm-1"]
    tgt_over = target["first_overtone_cm-1"]
    tgt_zpve = target["zpve_kcal_mol"]
    tols = step.get("tolerances", {})
    tol_energy = tols.get("energy_au", 1e-5)
    tol_fund = tols.get("fundamental_cm-1", 0.10)
    tol_over = tols.get("overtone_cm-1", 0.10)
    tol_zpve = tols.get("zpve_kcal_mol", 0.02)
    # score components
    # n_bound_states
    s_n = 1.0 if data.get("n_bound_states", 0) == tgt_n else 0.0
    # energies shape check
    agent_energies = data.get("energies_au", [])
    if isinstance(agent_energies, list) and len(agent_energies) == tgt_n:
        sorted_e = sorted(agent_energies)  # should be increasing (less negative)
        if all(sorted_e[i] < sorted_e[i+1] for i in range(len(sorted_e)-1)):
            s_shape = 1.0
        else:
            s_shape = 0.5
    else:
        s_shape = 0.0
    # energy accuracy (compare computed to paper)
    if n_comp >= tgt_n:
        errs = []
        for i in range(tgt_n):
            if i < n_comp:
                errs.append(abs(computed_energies[i] - tgt_energies[i]))
            else:
                errs.append(1.0)
        s_energy = np.mean([max(0.0, 1.0 - e / tol_energy) for e in errs])
    else:
        s_energy = 0.0
    # derived quantities from agent's reported values
    fund = data.get("fundamental_cm-1")
    over = data.get("first_overtone_cm-1")
    zpve = data.get("zpve_kcal_mol")
    def score_rel(val, ref, tol):
        if val is None or ref == 0:
            return 0.0
        rel_err = abs(val - ref) / abs(ref)
        return 1.0 if rel_err <= tol else max(0.0, 1.0 - (rel_err - tol) / tol)
    s_fund = score_rel(fund, tgt_fund, tol_fund)
    s_over = score_rel(over, tgt_over, tol_over)
    s_zpve = 1.0 if zpve is not None and abs(zpve - tgt_zpve) <= tol_zpve else max(0.0, 1.0 - (abs(zpve - tgt_zpve) - tol_zpve)/tol_zpve) if zpve is not None else 0.0
    s_derived = (s_fund + s_over + s_zpve) / 3.0
    # combine weights
    w_n = 0.2
    w_shape = 0.1
    w_energy = 0.4
    w_derived = 0.3
    return w_n*s_n + w_shape*s_shape + w_energy*s_energy + w_derived*s_derived


_SCORERS = {
    'step_02': score_0,
    'step_03': score_1,
    'step_04': score_2,
    'step_05': score_3,
    'step_06': score_4,
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
