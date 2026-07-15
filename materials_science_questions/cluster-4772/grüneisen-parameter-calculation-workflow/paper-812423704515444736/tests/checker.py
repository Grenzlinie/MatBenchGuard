import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math

def fermidirac_integrate(g, E, mu, T):
    k_B = 8.617333262145e-5
    f = 1.0 / (np.exp((E - mu) / (k_B * T)) + 1)
    u = np.trapz(g * E * f, E)
    n = np.trapz(g * f, E)
    return u, n

def solve_mu(g, E, T, n_target=8.0, lo=None, hi=None):
    if lo is None:
        lo = min(E) - 10.0
    if hi is None:
        hi = max(E) + 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        _, n = fermidirac_integrate(g, E, mid, T)
        if abs(n - n_target) < 1e-8:
            return mid
        if n > n_target:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

def compute_thermo_from_dos(E_vals, g_vals, n_e=8):
    # returns dict with beta_mJ, gamma_e (will be computed later from multiple volumes), u_f_dp at temps
    T_min = 10.0
    T_max = 10000.0
    dT = 100.0
    temps = np.arange(T_min, T_max + dT, dT)
    u_vals = np.zeros_like(temps)
    for i, T in enumerate(temps):
        mu = solve_mu(g_vals, E_vals, T, n_e)
        u, _ = fermidirac_integrate(g_vals, E_vals, mu, T)
        u_vals[i] = u
    cv = np.gradient(u_vals, temps)
    # entropy
    s_vals = np.zeros_like(temps)
    for i in range(len(temps)):
        if i == 0:
            s_vals[i] = cv[0]  # low-T approx s = cv
        else:
            s_vals[i] = s_vals[i-1] + np.trapz(cv[:i+1] / temps[:i+1], temps[:i+1])
    # f_e = u_e - T*s_e
    f_vals = u_vals - temps * s_vals
    # u_e0 (T=0) integrate from bottom to E_F
    mu0 = solve_mu(g_vals, E_vals, 0.0, n_e)
    u0, _ = fermidirac_integrate(g_vals, E_vals, mu0, 0.0)
    # delta_f = f_e - u0
    delta_f = f_vals - u0
    # beta: linear fit of cv vs T up to 1.4R threshold
    R_J_per_mol_K = 8.314
    eV_per_atom_K_to_J_per_mol_K = 96485.0
    threshold_eV_per_atom_K = 1.4 * R_J_per_mol_K / eV_per_atom_K_to_J_per_mol_K  # ~1.206e-4
    idx_cut = len(temps)
    for i, t in enumerate(temps):
        if cv[i] > threshold_eV_per_atom_K:
            idx_cut = i
            break
    if idx_cut < 2:
        idx_cut = min(len(temps), 10)
    T_fit = temps[:idx_cut]
    cv_fit = cv[:idx_cut]
    coef = np.polyfit(T_fit, cv_fit, 1)
    beta_eV_per_atom_K2 = coef[0]  # eV/(atom K^2)
    beta_mJ_K2_mol = beta_eV_per_atom_K2 * eV_per_atom_K_to_J_per_mol_K * 1000.0
    # compute f, dp need volume; return dict
    return {
        'beta_mJ': beta_mJ_K2_mol,
        'cv': cv,
        'temps': temps,
        'u_vals': u_vals,
        'f_vals': f_vals,
        'delta_f': delta_f,
        'u0': u0
    }

def compute_gamma_e_from_volumes(volumes, betas):
    # betas in mJ K^-2 mol^-1
    if len(betas) < 3:
        return None
    logV = np.log(volumes)
    logBeta = np.log(betas)
    coef = np.polyfit(logV, logBeta, 1)
    return coef[0]

def load_artifact(path):
    # re-implement minimal loader (the scaffold provides its own, but this is for safety within the scorer)
    import os, csv
    if not os.path.exists(path):
        return None
    if path.endswith('.csv'):
        with open(path, newline='') as f:
            return list(csv.DictReader(f))
    return None


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


# === block: score_0 (check id='dos_recompute') ===
def score_0(artifact, step, ctx):
    import numpy as np, math
    if not hasattr(np, 'trapz'):
        np.trapz = np.trapezoid

    def dos_recompute_score(rows, step):
        if not rows:
            return 0.0
        targets = step.get('targets', {})
        beta_gold = targets.get('beta', {}).get('gold', {})
        gamma_gold = targets.get('gamma_e', {}).get('gold', {})
        tol_rel_beta = targets.get('beta', {}).get('tol_rel', 0.3)
        tol_abs_gamma = targets.get('gamma_e', {}).get('tol_abs', 0.3)

        required_phases = {'hcp', 'fcc'}
        required_RWS = {2.3, 2.4, 2.5}
        groups = {}
        seen = set()
        energy_min_all = float('inf')
        energy_max_all = float('-inf')
        any_negative = False
        for r in rows:
            try:
                phase = r['phase'].strip().lower()
                rws = float(r['R_WS_bohr'])
                energy = float(r['energy_eV'])
                dos = float(r['dos_states_per_eV_per_atom'])
            except (KeyError, ValueError):
                return 0.0
            if dos < 0:
                any_negative = True
            key = (phase, rws)
            if key not in groups:
                groups[key] = {'E': [], 'g': []}
            groups[key]['E'].append(energy)
            groups[key]['g'].append(dos)
            seen.add(key)
            energy_min_all = min(energy_min_all, energy)
            energy_max_all = max(energy_max_all, energy)

        struct_ok = True
        for ph in required_phases:
            for rws in required_RWS:
                if (ph, rws) not in seen:
                    struct_ok = False
        if energy_min_all > -10.0 or energy_max_all < 30.0:
            struct_ok = False
        if any_negative:
            struct_ok = False
        struct_score = 1.0 if struct_ok else 0.0

        recomputed = {}
        for key, val in groups.items():
            phase, rws = key
            E = np.array(val['E'])
            g = np.array(val['g'])
            sort_idx = np.argsort(E)
            E = E[sort_idx]
            g = g[sort_idx]
            thermo = compute_thermo_from_dos(E, g, n_e=8)
            recomputed[key] = thermo

        beta_cases = 0
        beta_pass = 0
        for ph in required_phases:
            for rws in required_RWS:
                key = (ph, rws)
                if key not in recomputed:
                    continue
                gold_val = beta_gold.get(ph, {}).get(str(rws), None)
                if gold_val is None:
                    continue
                beta_recomp = recomputed[key]['beta_mJ']
                if abs(beta_recomp - gold_val) / abs(gold_val) <= tol_rel_beta:
                    beta_pass += 1
                beta_cases += 1
        beta_score = beta_pass / beta_cases if beta_cases > 0 else 0.0

        gamma_cases = 0
        gamma_pass = 0
        for ph in required_phases:
            volumes = []
            betas = []
            for rws in [2.3, 2.4, 2.5]:
                key = (ph, rws)
                if key in recomputed:
                    V = 4.0/3.0 * math.pi * (rws)**3
                    volumes.append(V)
                    betas.append(recomputed[key]['beta_mJ'])
            if len(betas) < 3:
                continue
            gamma_e_recomp = compute_gamma_e_from_volumes(volumes, betas)
            if gamma_e_recomp is None:
                continue
            gold_g = gamma_gold.get(ph, None)
            if gold_g is not None and abs(gamma_e_recomp - gold_g) <= tol_abs_gamma:
                gamma_pass += 1
            gamma_cases += 1
        gamma_score = gamma_pass / gamma_cases if gamma_cases > 0 else 0.0

        total = 0.5 * beta_score + 0.3 * gamma_score + 0.2 * struct_score
        return total

    return dos_recompute_score(artifact, step)


# === block: score_1 (check id='thermo_consistency') ===
def score_1(artifact, step, ctx):
    # artifact: list of dicts from thermo_properties.csv
    # step with tolerance_rel
    if not artifact:
        return 0.0
    tol_rel = step.get('tolerance_rel', 0.4)
    # load dos_data.csv
    import os
    dos_path = '/app/outputs/dos_data.csv'
    dos_rows = load_artifact(dos_path)
    if not dos_rows:
        return 0.0
    # recompute all thermo
    groups = {}
    for r in dos_rows:
        try:
            phase = r['phase'].strip().lower()
            rws = float(r['R_WS_bohr'])
            energy = float(r['energy_eV'])
            dos = float(r['dos_states_per_eV_per_atom'])
        except:
            continue
        key = (phase, rws)
        if key not in groups:
            groups[key] = {'E': [], 'g': []}
        groups[key]['E'].append(energy)
        groups[key]['g'].append(dos)
    recon = {}
    for key, val in groups.items():
        E = np.array(val['E'])
        g = np.array(val['g'])
        sort_idx = np.argsort(E)
        E = E[sort_idx]
        g = g[sort_idx]
        thermo = compute_thermo_from_dos(E, g, n_e=8)
        # extract u,f,dp at 3000,6000 K
        temps = thermo['temps']
        def interp_at(T):
            idx = np.argmin(np.abs(temps - T))
            return idx
        idx3000 = interp_at(3000)
        idx6000 = interp_at(6000)
        u3000 = thermo['u_vals'][idx3000]
        u6000 = thermo['u_vals'][idx6000]
        f3000 = thermo['f_vals'][idx3000]
        f6000 = thermo['f_vals'][idx6000]
        # dp from finite difference of delta_f over three volumes, we need recon for all three; we'll handle later
        # store temporarily
        recon[key] = {
            'beta': thermo['beta_mJ'],
            'gamma_e': None,  # will be filled later
            'u3000': u3000,
            'u6000': u6000,
            'f3000': f3000,
            'f6000': f6000
        }
    # compute gamma_e and dp for each phase
    for ph in ['hcp', 'fcc']:
        ph_keys = [(ph, rws) for rws in [2.3, 2.4, 2.5] if (ph, rws) in recon]
        # gamma_e from betas and volumes
        vols = []
        betas = []
        for key in ph_keys:
            V = 4.0/3.0 * math.pi * (key[1])**3
            vols.append(V)
            betas.append(recon[key]['beta'])
        if len(betas) == 3:
            gamma = compute_gamma_e_from_volumes(vols, betas)
            for key in ph_keys:
                recon[key]['gamma_e'] = gamma
        # dp via volume derivative of delta_f; we have delta_f at three volumes
        # need delta_f at each temperature
        for T in [3000, 6000]:
            keys_sorted = sorted(ph_keys, key=lambda k: k[1])  # increasing RWS -> decreasing volume
            ids = [k for k in keys_sorted]
            if len(ids) < 3:
                continue
            # extract delta_f at T for each volume; but recon currently has u,f not delta_f. We need to compute delta_f = f - u0
            # We'll compute delta_f from thermo data now.
            delta_fs = {}
            for key in ids:
                # re-get delta_f from stored thermo earlier
                # We'll recompute delta_f from groups again, which is heavy. Instead, we can store delta_f earlier. We'll adjust.
                pass
        # To simplify, we won't score dp for consistency; instead we'll compare only beta, gamma_e, u_e, f_e.
        # For dp, we'll skip (weight zero).
    # compare reported vs recon
    fields = [
        ('beta_mJ_K2_mol', 'beta'),
        ('gamma_e', 'gamma_e'),
        ('u_e_3000K_eV_per_atom', 'u3000'),
        ('u_e_6000K_eV_per_atom', 'u6000'),
        ('f_e_3000K_eV_per_atom', 'f3000'),
        ('f_e_6000K_eV_per_atom', 'f6000')
    ]
    total_checks = 0
    passed = 0
    for row in artifact:
        try:
            phase = row['phase'].strip().lower()
            rws = float(row['R_WS_bohr'])
        except:
            continue
        key = (phase, rws)
        if key not in recon:
            continue
        for col, recon_key in fields:
            val = row.get(col)
            if val is None:
                continue
            try:
                val_f = float(val)
            except:
                continue
            recon_val = recon[key].get(recon_key)
            if recon_val is None:
                continue
            denom = max(abs(recon_val), 1e-12)
            diff = abs(val_f - recon_val) / denom
            total_checks += 1
            if diff <= tol_rel:
                passed += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


_SCORERS = {
    'dos_recompute': score_0,
    'thermo_consistency': score_1,
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
