import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "--no-cache-dir", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "numpy", "scipy"])
import os, json
import numpy as np
from scipy.optimize import minimize
import math

def murnaghan(V, E0, V0, B0, Bp):
    """Murnaghan equation of state."""
    # E(V) = E0 + (B0*V0)/(Bp*(Bp-1)) * [ Bp*(1 - V0/V) + (V0/V)**Bp - 1 ]
    if Bp == 1.0:
        return E0 + B0 * V0 * (np.log(V0 / V) + V / V0 - 1.0)
    return E0 + (B0 * V0) * ( (1.0 - Bp) * (V0 / V - 1.0) / (Bp) + (V0 / V)**Bp * (1.0 / (Bp * (Bp - 1.0))) - 1.0 / (Bp * (Bp - 1.0)) )

def fit_murnaghan(volumes, energies):
    """Fit Murnaghan EOS to vol, energy arrays. Returns (V0, B0, Bp, E0) or raises."""
    v = np.array(volumes, dtype=float)
    e = np.array(energies, dtype=float)
    # initial guesses
    idx = np.argmin(e)
    v0_guess = v[idx]
    e0_guess = e[idx]
    # rough B0 guess via curvature
    if len(v) >= 4:
        poly = np.polyfit(v, e, 2)
        curv = poly[0] * 2.0
        b0_guess = curv * v0_guess * 10.0  # heuristic
        b0_guess = max(abs(b0_guess), 10.0)
    else:
        b0_guess = 100.0
    bp_guess = 4.0

    def objective(params):
        E0, V0, B0, Bp = params
        e_fit = murnaghan(v, E0, V0, B0, Bp)
        return np.sum((e - e_fit)**2)

    bounds = [(None, None), (v0_guess*0.5, v0_guess*1.5), (1.0, 2000.0), (1.0, 10.0)]
    res = minimize(objective, [e0_guess, v0_guess, b0_guess, bp_guess],
                   method='L-BFGS-B', bounds=bounds, options={'maxiter': 1000})
    if not res.success:
        raise RuntimeError(f"EOS fit failed: {res.message}")
    E0, V0, B0, Bp = res.x
    # convert B0 from eV/Å^3 to GPa: 1 eV/Å^3 = 160.21766208 GPa
    B0_GPa = B0 * 160.21766208
    return V0, B0_GPa, Bp

# atomic masses (g/mol)
ATOMIC_MASS = {
    'B': 10.81,
    'N': 14.007,
    'P': 30.974,
    'As': 74.922,
    'Sb': 121.76,
    'Bi': 208.98
}

# constants
NA = 6.02214076e23
h = 6.62607015e-34   # J·s
kB = 1.380649e-23     # J/K
ang3_to_m3 = 1e-30
ang3_to_cm3 = 1e-24


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
    energy_path = os.path.join(outputs_dir, 'energy_volume_data.csv')
    elastic_path = os.path.join(outputs_dir, 'elastic_constants.csv')

    if not os.path.exists(energy_path) or not os.path.exists(elastic_path):
        return {}

    import csv

    # load energy-volume data
    with open(energy_path, 'r') as f:
        reader = csv.DictReader(f)
        ev_data = list(reader)

    # load elastic constants
    with open(elastic_path, 'r') as f:
        reader = csv.DictReader(f)
        el_data = list(reader)

    # group ev data
    groups = {}
    for row in ev_data:
        compound = row['compound'].strip()
        phase = row['phase'].strip()
        vol = float(row['volume'])
        energy = float(row['total_energy'])
        key = f"{compound}_{phase}"
        groups.setdefault(key, {'volumes': [], 'energies': []})
        groups[key]['volumes'].append(vol)
        groups[key]['energies'].append(energy)

    # fit each group
    eos_params = {}
    for key, item in groups.items():
        vols = item['volumes']
        energs = item['energies']
        if len(vols) < 7:
            continue
        try:
            V0, B0, Bp = fit_murnaghan(vols, energs)
            eos_params[key] = {'V0': V0, 'B0': B0, 'Bprime': Bp}
        except Exception:
            pass

    # parse elastic constants
    elastic_constants = {}
    for row in el_data:
        comp = row['compound'].strip()
        C11 = float(row['C11'])
        C12 = float(row['C12'])
        C44 = float(row['C44'])
        elastic_constants[comp] = {'C11': C11, 'C12': C12, 'C44': C44}

    return {'eos_params': eos_params, 'elastic_constants': elastic_constants}


# === block: score_0 (check id='structural_parameters') ===
def score_0(artifact, step, ctx):
    eos_params = ctx.get('eos_params', {})
    step_gold = step.get('gold', {})
    if not step_gold or not eos_params:
        return 0.0

    # compute scores per group
    group_keys = [
        'BN_ZB','BP_ZB','BAs_ZB','BSb_ZB','BBi_ZB',
        'BN_NaCl','BP_NaCl','BAs_NaCl','BSb_NaCl','BBi_NaCl',
        'BN_WZ','BP_WZ','BAs_WZ','BSb_WZ','BBi_WZ'
    ]
    # collect scores for V0, B0, Bprime
    v0_scores = []
    b0_scores = []
    bp_scores = []
    for key in group_keys:
        gold = step_gold.get(key)
        fitted = eos_params.get(key)
        if not gold or not fitted:
            v0_scores.append(0.0)
            b0_scores.append(0.0)
            bp_scores.append(0.0)
            continue
        # V0 score (relative error)
        rel_err_v0 = abs(fitted['V0'] - gold['V0']) / (abs(gold['V0']) + 1e-9)
        v0_score = 1.0 if rel_err_v0 <= 0.02 else max(0.0, 1.0 - (rel_err_v0 - 0.02)/0.1)
        v0_scores.append(v0_score)
        # B0 score
        rel_err_b0 = abs(fitted['B0'] - gold['B0']) / (abs(gold['B0']) + 1e-9)
        b0_score = 1.0 if rel_err_b0 <= 0.10 else max(0.0, 1.0 - (rel_err_b0 - 0.10)/0.2)
        b0_scores.append(b0_score)
        # B' score
        rel_err_bp = abs(fitted['Bprime'] - gold['Bprime']) / (abs(gold['Bprime']) + 1e-9)
        bp_score = 1.0 if rel_err_bp <= 0.20 else max(0.0, 1.0 - (rel_err_bp - 0.20)/0.3)
        bp_scores.append(bp_score)

    avg_v0 = np.mean(v0_scores) if v0_scores else 0.0
    avg_b0 = np.mean(b0_scores) if b0_scores else 0.0
    avg_bp = np.mean(bp_scores) if bp_scores else 0.0
    group_avg = (avg_v0 + avg_b0 + avg_bp) / 3.0

    # monotonic B0 for ZB phase
    mono_correct = True
    zb_b0 = []
    for comp in ['BN','BP','BAs','BSb','BBi']:
        key = f"{comp}_ZB"
        fitted = eos_params.get(key)
        if not fitted:
            mono_correct = False
            break
        zb_b0.append(fitted['B0'])
    if mono_correct:
        for i in range(len(zb_b0)-1):
            if zb_b0[i] <= zb_b0[i+1]:
                mono_correct = False
                break
    mono_score = 1.0 if mono_correct else 0.0

    # overall score: 0.7 group average, 0.3 monotonic
    overall = 0.7 * group_avg + 0.3 * mono_score
    return min(1.0, max(0.0, overall))


# === block: score_1 (check id='elastic_properties') ===
def score_1(artifact, step, ctx):
    eos_params = ctx.get('eos_params', {})
    elastic_constants = ctx.get('elastic_constants', {})
    step_gold = step.get('gold', {})
    if not elastic_constants:
        return 0.0

    compounds = ['BN','BP','BAs','BSb','BBi']
    mech_scores = []
    prop_scores_list = []

    for comp in compounds:
        gold = step_gold.get(comp)
        C = elastic_constants.get(comp)
        if gold is None or C is None:
            mech_scores.append(0.0)
            prop_scores_list.append([0.0]*11)
            continue
        C11 = C['C11']
        C12 = C['C12']
        C44 = C['C44']
        # mechanical stability
        stable = (C11 - C12 > 0) and (C44 > 0) and (C11 + 2*C12 > 0)
        B = (C11 + 2*C12)/3.0
        stable = stable and (C12 < B < C11)
        mech_scores.append(1.0 if stable else 0.0)

        # compute derived quantities
        # Bulk modulus (already computed)
        # Shear modulus (Hill average)
        diff = C11 - C12
        if diff <= 0 or C44 <= 0:
            prop_scores_list.append([0.0]*11)
            continue
        G_V = (diff + 3*C44)/5.0
        G_R = 5.0 / (4.0/diff + 3.0/C44)
        G = 0.5 * (G_V + G_R)
        Y_mod = 9.0 * B * G / (3.0*B + G)
        nu = (3.0*B - 2.0*G) / (2.0*(3.0*B + G))
        A_fact = 2.0 * C44 / diff
        zeta_val = (C11 + 8.0*C12) / (7.0*C11 + 2.0*C12)

        # volume from EOS for ZB
        zb_key = f"{comp}_ZB"
        ev_params = eos_params.get(zb_key, {})
        V0_fu = ev_params.get('V0', None)
        if V0_fu is None:
            prop_scores_list.append([0.0]*11)
            continue
        # density (g/cm^3)
        # molar mass
        elements = {'BN': ('B','N'), 'BP': ('B','P'), 'BAs': ('B','As'),
                    'BSb': ('B','Sb'), 'BBi': ('B','Bi')}
        e1, e2 = elements[comp]
        M = ATOMIC_MASS[e1] + ATOMIC_MASS[e2]
        V_cm3 = V0_fu * 1e-24  # Å^3 to cm^3
        rho = M / (NA * V_cm3)  # g/cm^3
        # wave velocities (m/s)
        rho_kgm3 = rho * 1000.0  # kg/m^3
        G_Pa = G * 1e9  # Pa
        B_Pa = B * 1e9
        v_t = math.sqrt(G_Pa / rho_kgm3)
        v_l = math.sqrt((3*B_Pa + 4*G_Pa) / (3*rho_kgm3))
        v_m = (1.0/3.0 * (2.0/v_t**3 + 1.0/v_l**3)) ** (-1.0/3.0)
        # Debye temperature (K) using formula theta_D = (h/kB) * v_m * (3*n/(4*pi*V0_fu_in_m3))^(1/3), n=2
        n_atom = 2
        V_m3 = V0_fu * 1e-30
        factor = ( (3.0 * n_atom) / (4.0 * math.pi * V_m3) ) ** (1.0/3.0)
        theta_D = (h / kB) * v_m * factor
        # melting point (K): Tm = 553 + 5.91*C11 (C11 in GPa)
        Tm = 553.0 + 5.91 * C11

        # collect property gold and compute scores
        gold_g = gold['G']
        gold_y = gold['Y']
        gold_nu = gold['v']
        gold_A = gold['A']
        gold_zeta = gold['zeta']
        gold_rho = gold['rho']
        gold_vl = gold['v_l']
        gold_vt = gold['v_t']
        gold_vm = gold['v_m']
        gold_td = gold['theta_D']
        gold_tm = gold['Tm']

        # scoring functions: monotonic with tolerance
        def rel_score(val, gold, tol):
            re = abs(val - gold) / (abs(gold) + 1e-9)
            if re <= tol:
                return 1.0
            else:
                return max(0.0, 1.0 - (re - tol)/0.3)  # decay over 0.3 additional

        def abs_score(val, gold, atol):
            diff = abs(val - gold)
            if diff <= atol:
                return 1.0
            else:
                return max(0.0, 1.0 - (diff - atol)/ (atol*2.0))

        s_G = rel_score(G, gold_g, 0.15)
        s_Y = rel_score(Y_mod, gold_y, 0.15)
        s_nu = abs_score(nu, gold_nu, 0.05)
        s_A = rel_score(A_fact, gold_A, 0.10)
        s_zeta = rel_score(zeta_val, gold_zeta, 0.10)
        s_rho = rel_score(rho, gold_rho, 0.05)
        s_vl = rel_score(v_l, gold_vl, 0.10)
        s_vt = rel_score(v_t, gold_vt, 0.10)
        s_vm = rel_score(v_m, gold_vm, 0.10)
        s_td = rel_score(theta_D, gold_td, 0.15)
        # Tm: combine absolute and relative
        rel_tm = abs(Tm - gold_tm) / (abs(gold_tm) + 1e-9)
        abs_tm = abs(Tm - gold_tm)
        if abs_tm <= 200 or rel_tm <= 0.15:
            s_tm = 1.0
        else:
            s_tm = max(0.0, 1.0 - (abs_tm - 200)/200.0)

        prop_scores = [s_G, s_Y, s_nu, s_A, s_zeta, s_rho, s_vl, s_vt, s_vm, s_td, s_tm]
        prop_scores_list.append(prop_scores)

    # average over compounds and properties
    avg_mech = np.mean(mech_scores) if mech_scores else 0.0
    # combine property scores: per compound average, then overall average
    property_means = []
    for scores in prop_scores_list:
        if len(scores) > 0:
            property_means.append(np.mean(scores))
        else:
            property_means.append(0.0)
    avg_prop = np.mean(property_means) if property_means else 0.0
    overall = 0.1 * avg_mech + 0.9 * avg_prop
    return min(1.0, max(0.0, overall))


_SCORERS = {
    'structural_parameters': score_0,
    'elastic_properties': score_1,
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
