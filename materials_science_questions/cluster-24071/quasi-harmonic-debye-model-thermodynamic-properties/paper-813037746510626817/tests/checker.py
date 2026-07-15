import os
import json
import csv


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
    ctx = {}
    for step in spec.get('steps', []):
        if step['id'] == 'thermodynamic_check':
            ctx['thermo_gold'] = step.get('gold_thermo_0GPa', [])
            ctx['dulong_petit_ref'] = step.get('dulong_petit_ref', 423.99)
            ctx['dulong_tol_frac'] = step.get('dulong_tol_frac', 0.10)
            ctx['alpha_tol_frac'] = step.get('alpha_tol_frac', 0.20)
            ctx['gamma_tol_frac'] = step.get('gamma_tol_frac', 0.10)
            ctx['t3_slope_tol'] = step.get('t3_slope_tol', 0.5)
        elif step['id'] == 'transport_check':
            ctx['transport_gold_300K'] = step.get('gold_transport_300K', {})
            ctx['seebeck_tol_frac'] = step.get('seebeck_tol_frac', 0.10)
            ctx['kappa_tol_frac'] = step.get('kappa_tol_frac', 0.20)
            ctx['pf_tol_frac'] = step.get('pf_tol_frac', 0.20)
            ctx['sigma_mono_allow_fluct'] = step.get('sigma_mono_allow_fluct', 0.02)
    return ctx


# === block: score_0 (check id='thermodynamic_check') ===
def score_0(artifact, step, ctx):
    import math

    rows = artifact
    if not rows:
        return 0.0

    # build lookup
    lookup = {}
    for r in rows:
        try:
            T = float(r['T(K)'])
            P = float(r['P(GPa)'])
            cv = float(r['CV(J/mol·K)'])
            alpha = float(r['alpha(1/K)'])
            gamma = float(r['gamma'])
            lookup[(T,P)] = (cv, alpha, gamma)
        except:
            pass

    # expected (T,P) combos
    expected_T = [50, 100, 200, 300, 370]
    expected_P = [0, 5, 10]
    found = sum(1 for T in expected_T for P in expected_P if (T,P) in lookup)
    fmt_score = min(1.0, found/15.0)

    # Dulong-Petit: T=370,P=0
    cv_dp = None
    if (370,0) in lookup:
        cv_dp = lookup[(370,0)][0]
    dp_ref = ctx['dulong_petit_ref']
    dp_tol = ctx['dulong_tol_frac']
    if cv_dp is not None:
        err = abs(cv_dp - dp_ref)/dp_ref if dp_ref>0 else 0
        if err <= dp_tol:
            dp_score = 1.0
        elif err <= 2*dp_tol:
            dp_score = 1.0 - (err - dp_tol)/dp_tol
        else:
            dp_score = 0.0
    else:
        dp_score = 0.0

    # T^3 law: fit log10(CV) vs log10(T) for T=50,100,200 at P=0
    t3_logT = []
    t3_logCV = []
    for T in [50,100,200]:
        if (T,0) in lookup and lookup[(T,0)][0] > 0:
            t3_logT.append(math.log10(T))
            t3_logCV.append(math.log10(lookup[(T,0)][0]))
    if len(t3_logT) >= 3:
        n = len(t3_logT)
        sum_x = sum(t3_logT)
        sum_y = sum(t3_logCV)
        sum_xy = sum(x*y for x,y in zip(t3_logT, t3_logCV))
        sum_x2 = sum(x*x for x in t3_logT)
        denom = n*sum_x2 - sum_x*sum_x
        if abs(denom) > 1e-30:
            slope = (n*sum_xy - sum_x*sum_y) / denom
        else:
            slope = 0.0
        t3_score = max(0.0, 1.0 - abs(slope-3.0)/ctx['t3_slope_tol'])
    else:
        t3_score = 0.0

    # alpha at 300K,0GPa
    if (300,0) in lookup:
        alpha_val = lookup[(300,0)][1]
    else:
        alpha_val = None
    alpha_gold = 6.7e-6
    alpha_tol = ctx['alpha_tol_frac']
    if alpha_val is not None and alpha_gold>0:
        err_a = abs(alpha_val - alpha_gold)/alpha_gold
        if err_a <= alpha_tol:
            a_score = 1.0
        elif err_a <= 0.5:
            a_score = 1.0 - (err_a - alpha_tol)/(0.5 - alpha_tol)
        else:
            a_score = 0.0
    else:
        a_score = 0.0

    # gamma at 300K,0GPa
    if (300,0) in lookup:
        gamma_val = lookup[(300,0)][2]
    else:
        gamma_val = None
    gamma_gold = 2.12
    gamma_tol = ctx['gamma_tol_frac']
    if gamma_val is not None:
        err_g = abs(gamma_val - gamma_gold)/gamma_gold
        if err_g <= gamma_tol:
            g_score = 1.0
        elif err_g <= 0.2:
            g_score = 1.0 - (err_g - gamma_tol)/(0.2 - gamma_tol)
        else:
            g_score = 0.0
    else:
        g_score = 0.0

    # pressure monotonic check (C_V decreases with pressure)
    mono_pairs = 0
    mono_good = 0
    for T in expected_T:
        for i in range(len(expected_P)-1):
            p1 = expected_P[i]
            p2 = expected_P[i+1]
            if (T,p1) in lookup and (T,p2) in lookup:
                mono_pairs += 1
                if lookup[(T,p1)][0] >= lookup[(T,p2)][0] - 1e-9:
                    mono_good += 1
    if mono_pairs > 0:
        mono_score = mono_good / mono_pairs
    else:
        mono_score = 0.0

    # combine with weights
    score = 0.05*fmt_score + 0.25*dp_score + 0.25*t3_score + 0.15*a_score + 0.15*g_score + 0.15*mono_score
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='transport_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0

    lookup = {}
    for r in rows:
        try:
            T = float(r['T(K)'])
            S = float(r['Seebeck(µV/K)'])
            s_tau = float(r['sigma_tau(Ω⁻¹·m⁻¹·s⁻¹)'])
            kap = float(r['kappa(W/m·K)'])
            pf = float(r['PF(µW/(cm·K²·s))'])
            lookup[T] = (S, s_tau, kap, pf)
        except:
            pass

    expected_T = [50,100,200,300,400,600,800]
    found = sum(1 for T in expected_T if T in lookup)
    fmt_score = min(1.0, found/7.0)

    # Gold at 300K
    g = ctx['transport_gold_300K']
    T0 = 300
    seebeck_gold = g['Seebeck']
    kappa_gold = g['kappa']
    pf_gold = g['PF']
    seebeck_tol = ctx['seebeck_tol_frac']
    kappa_tol = ctx['kappa_tol_frac']
    pf_tol = ctx['pf_tol_frac']

    if T0 in lookup:
        S_val, stau_val, kap_val, pf_val = lookup[T0]
    else:
        S_val = stau_val = kap_val = pf_val = None

    # Seebeck (higher magnitude better? Actually negative sign, so better means more negative. Check if Seebeck is more negative than -158. If agent's value is <= -158 (more negative), full credit. Else if less negative, penalize)
    if S_val is not None and seebeck_gold != 0:
        if S_val <= seebeck_gold:  # more negative or equal
            s_score = 1.0
        else:
            rel = abs((S_val - seebeck_gold)/seebeck_gold) if seebeck_gold!=0 else abs(S_val-seebeck_gold)
            if rel <= seebeck_tol:
                s_score = 1.0
            elif rel <= 0.3:
                s_score = 1.0 - (rel - seebeck_tol)/(0.3 - seebeck_tol)
            else:
                s_score = 0.0
    else:
        s_score = 0.0

    # Kappa (lower is better for thermoelectrics, but we want close to 1.8; we'll use absolute relative error)
    if kap_val is not None and kappa_gold > 0:
        rel_k = abs(kap_val - kappa_gold)/kappa_gold
        if rel_k <= kappa_tol:
            k_score = 1.0
        elif rel_k <= 0.4:
            k_score = 1.0 - (rel_k - kappa_tol)/(0.4 - kappa_tol)
        else:
            k_score = 0.0
    else:
        k_score = 0.0

    # PF (higher is better) if pf_val >= pf_gold*(1 - pf_tol) => 1.0, else decay
    if pf_val is not None and pf_gold > 0:
        if pf_val >= pf_gold * (1 - pf_tol):
            pf_score = 1.0
        elif pf_val >= pf_gold * 0.5:
            pf_score = (pf_val/pf_gold - 0.5) / (0.5 - pf_tol) if (0.5 - pf_tol) > 0 else 0
        else:
            pf_score = 0.0
    else:
        pf_score = 0.0

    # sigma_tau monotonic decreasing: for each consecutive T pair, check that sigma_tau[i] <= sigma_tau[i-1]*(1+allow_fluct)
    allow = ctx['sigma_mono_allow_fluct']
    ordered_T = sorted([T for T in expected_T if T in lookup])
    mono_checks = 0
    mono_ok = 0
    for i in range(1, len(ordered_T)):
        prev = lookup[ordered_T[i-1]][1]
        curr = lookup[ordered_T[i]][1]
        mono_checks += 1
        if curr <= prev * (1+allow):
            mono_ok += 1
    if mono_checks > 0:
        mono_score = mono_ok / mono_checks
    else:
        mono_score = 0.0

    # combine
    score = 0.05*fmt_score + 0.30*s_score + 0.25*k_score + 0.20*pf_score + 0.20*mono_score
    return max(0.0, min(1.0, score))


_SCORERS = {
    'thermodynamic_check': score_0,
    'transport_check': score_1,
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
