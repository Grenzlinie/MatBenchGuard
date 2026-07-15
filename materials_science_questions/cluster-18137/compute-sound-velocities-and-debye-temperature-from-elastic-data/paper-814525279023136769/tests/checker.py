import os
import json
import csv

# === author imports / helpers ===
import json
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
    return {}


# === block: score_0 (check id='elastic_constants_match') ===
def score_0(artifact, step, ctx):
    artifact_path = '/app/outputs/elastic_constants.json'
    try:
        with open(artifact_path) as f:
            data = json.load(f)
    except Exception:
        return 0.0

    gold = step.get('gold', {})
    tolerance_rel = step.get('tolerance_rel', 0.10)

    keys = ['C11', 'C12', 'C13', 'C33', 'C44', 'C66']
    functionals = ['LDA', 'GGA-WC']

    ok = 0
    total = 0
    for func in functionals:
        g = gold.get(func, {})
        d = data.get(func, {})
        for k in keys:
            v_gold = g.get(k)
            v_sub = d.get(k)
            if v_gold is None or v_sub is None:
                continue
            total += 1
            if abs(v_gold) > 1e-12:
                rel_err = abs(v_sub - v_gold) / abs(v_gold)
                if rel_err <= tolerance_rel:
                    ok += 1
            else:
                ok += 1

    if total == 0:
        const_score = 0.0
    else:
        const_score = ok / total

    # mechanical stability criteria for hexagonal
    stability_ok = True
    for func in functionals:
        d = data.get(func, {})
        if not d:
            stability_ok = False
            break
        C11 = d.get('C11', 0)
        C12 = d.get('C12', 0)
        C13 = d.get('C13', 0)
        C33 = d.get('C33', 0)
        C44 = d.get('C44', 0)
        if not (C11 > 0 and C44 > 0 and (C11 - C12) > 0 and ((C11 + C12) * C33 - 2 * C13**2) > 0):
            stability_ok = False
            break

    stab_score = 1.0 if stability_ok else 0.0
    return 0.5 * const_score + 0.5 * stab_score


# === block: score_1 (check id='polycrystalline_recompute') ===
def score_1(artifact, step, ctx):
    with open('/app/outputs/elastic_constants.json') as f:
        C = json.load(f)

    gold = step['gold']
    tols = step.get('tolerances', {})

    def compute_props(c):
        C11 = c['C11']; C12 = c['C12']; C13 = c['C13']
        C33 = c['C33']; C44 = c['C44']; C66 = c['C66']
        B_V = (2/9) * (C11 + C12 + C33/2 + 2*C13)
        G_V = (1/30) * (7*C11 - 5*C12 + 12*C44 + 2*C33 - 4*C13)
        denom = C11 + C12 + 2*C33 - 4*C13
        if denom == 0:
            return None
        B_R = ((C11 + C12)*C33 - 2*C13**2) / denom
        num = ((C11 + C12)*C33 - 2*C13**2) * C44 * C66
        den_G = 3*B_V*C44*C66 + ((C11 + C12)*C33 - 2*C13**2)*(C44 + C66)
        if den_G == 0:
            return None
        G_R = (5/2) * (num / den_G)
        B = (B_V + B_R) / 2
        G = (G_V + G_R) / 2
        E = 9*B*G / (3*B + G)
        sigma = (3*B - 2*G) / (2*(3*B + G))
        A_val = 2*C44 / (C11 - C12)
        B_over_G = B / G if G != 0 else 0
        H = (1 - 2*sigma)*E / (6*(1 + sigma))
        return {'B': B, 'G': G, 'E': E, 'sigma': sigma, 'A': A_val, 'B_over_G': B_over_G, 'H': H}

    functionals = ['LDA', 'GGA-WC']
    ok = 0
    total = 0
    for func in functionals:
        c = C.get(func)
        if not c:
            continue
        comp = compute_props(c)
        if comp is None:
            continue
        g = gold.get(func, {})
        for prop, tol in tols.items():
            val_gold = g.get(prop)
            val_comp = comp.get(prop)
            if val_gold is None or val_comp is None:
                continue
            total += 1
            if 'abs' in tol:
                if abs(val_comp - val_gold) <= tol['abs']:
                    ok += 1
            elif 'rel' in tol:
                if abs(val_gold) > 1e-12:
                    rel_err = abs(val_comp - val_gold) / abs(val_gold)
                    if rel_err <= tol['rel']:
                        ok += 1
                else:
                    ok += 1
            else:
                pass

    if total == 0:
        return 0.0
    return ok / total


# === block: score_2 (check id='thermodynamic_recompute') ===
def score_2(artifact, step, ctx):
    with open('/app/outputs/elastic_constants.json') as f:
        C = json.load(f)

    h = 6.62607015e-34
    k_B = 1.380649e-23
    NA = 6.02214076e23

    def compute_BG(c):
        C11 = c['C11']; C12 = c['C12']; C13 = c['C13']
        C33 = c['C33']; C44 = c['C44']; C66 = c['C66']
        B_V = (2/9) * (C11 + C12 + C33/2 + 2*C13)
        G_V = (1/30) * (7*C11 - 5*C12 + 12*C44 + 2*C33 - 4*C13)
        denom = C11 + C12 + 2*C33 - 4*C13
        if denom == 0:
            return None
        B_R = ((C11 + C12)*C33 - 2*C13**2) / denom
        num = ((C11 + C12)*C33 - 2*C13**2) * C44 * C66
        den_G = 3*B_V*C44*C66 + ((C11 + C12)*C33 - 2*C13**2)*(C44 + C66)
        if den_G == 0:
            return None
        G_R = (5/2) * (num / den_G)
        B = (B_V + B_R) / 2
        G = (G_V + G_R) / 2
        return B, G

    gold = step['gold']
    density_gold_map = step.get('density_gold', {})
    tolerance_rel = step.get('tolerance_rel', 0.10)

    functionals = ['LDA', 'GGA-WC']
    ok = 0
    total = 0
    for func in functionals:
        c = C.get(func)
        if not c:
            continue
        bg = compute_BG(c)
        if bg is None:
            continue
        B, G = bg
        rho = density_gold_map.get(func)
        if rho is None:
            continue
        rho_SI = rho * 1000
        B_SI = B * 1e9
        G_SI = G * 1e9
        v_l = math.sqrt((3*B_SI + 4*G_SI) / (3 * rho_SI))
        v_t = math.sqrt(G_SI / rho_SI)
        v_m = ((1/3) * (1/v_l**3 + 2/v_t**3)) ** (-1/3)

        M = 175.8205  # Mg3Rh molar mass g/mol
        n_atoms_per_fu = 4
        V_a = M / (rho * NA)   # cm^3 per formula unit
        V_atom = V_a / n_atoms_per_fu  # cm^3 per atom
        V_atom_m3 = V_atom * 1e-6
        prefactor = (3 / (4 * math.pi * V_atom_m3)) ** (1/3)
        Theta_D = (h / k_B) * prefactor * v_m

        vals = {'v_l': v_l, 'v_t': v_t, 'v_m': v_m, 'Theta_D': Theta_D}
        g = gold.get(func, {})
        for key in ['v_l', 'v_t', 'v_m', 'Theta_D']:
            gval = g.get(key)
            cval = vals[key]
            if gval is None:
                continue
            total += 1
            if abs(gval) > 1e-12:
                if abs(cval - gval) / abs(gval) <= tolerance_rel:
                    ok += 1
            else:
                ok += 1

    if total == 0:
        return 0.0
    return ok / total


# === block: score_3 (check id='internal_consistency') ===
def score_3(artifact, step, ctx):
    base = '/app/outputs'
    try:
        with open(f'{base}/elastic_constants.json') as f:
            ec = json.load(f)
        with open(f'{base}/polycrystalline_properties.json') as f:
            pc = json.load(f)
        with open(f'{base}/thermodynamic_properties.json') as f:
            td = json.load(f)
    except Exception:
        return 0.0

    rho_gold_map = step.get('rho_gold', {})

    # ---- helpers ----
    def compute_BG(c):
        C11 = c['C11']; C12 = c['C12']; C13 = c['C13']
        C33 = c['C33']; C44 = c['C44']; C66 = c['C66']
        B_V = (2/9) * (C11 + C12 + C33/2 + 2*C13)
        G_V = (1/30) * (7*C11 - 5*C12 + 12*C44 + 2*C33 - 4*C13)
        denom = C11 + C12 + 2*C33 - 4*C13
        if denom == 0:
            return None
        B_R = ((C11 + C12)*C33 - 2*C13**2) / denom
        num = ((C11 + C12)*C33 - 2*C13**2) * C44 * C66
        den_G = 3*B_V*C44*C66 + ((C11 + C12)*C33 - 2*C13**2)*(C44 + C66)
        if den_G == 0:
            return None
        G_R = (5/2) * (num / den_G)
        B = (B_V + B_R) / 2
        G = (G_V + G_R) / 2
        return B, G

    def compute_poly(c):
        C11 = c['C11']; C12 = c['C12']; C13 = c['C13']
        C33 = c['C33']; C44 = c['C44']; C66 = c['C66']
        B_V = (2/9) * (C11 + C12 + C33/2 + 2*C13)
        G_V = (1/30) * (7*C11 - 5*C12 + 12*C44 + 2*C33 - 4*C13)
        denom = C11 + C12 + 2*C33 - 4*C13
        if denom == 0:
            return None
        B_R = ((C11 + C12)*C33 - 2*C13**2) / denom
        num = ((C11 + C12)*C33 - 2*C13**2) * C44 * C66
        den_G = 3*B_V*C44*C66 + ((C11 + C12)*C33 - 2*C13**2)*(C44 + C66)
        if den_G == 0:
            return None
        G_R = (5/2) * (num / den_G)
        B = (B_V + B_R) / 2
        G = (G_V + G_R) / 2
        E = 9*B*G / (3*B + G)
        sigma = (3*B - 2*G) / (2*(3*B + G))
        A_val = 2*C44 / (C11 - C12)
        B_over_G = B / G if G != 0 else 0
        H = (1 - 2*sigma)*E / (6*(1 + sigma))
        return {'B': B, 'G': G, 'E': E, 'sigma': sigma, 'A': A_val, 'B_over_G': B_over_G, 'H': H}

    # ---- stability ----
    stab_ok = True
    for func in ['LDA', 'GGA-WC']:
        c = ec.get(func)
        if not c:
            stab_ok = False; break
        C11=c['C11']; C12=c['C12']; C13=c['C13']; C33=c['C33']; C44=c['C44']
        if not (C11>0 and C44>0 and (C11-C12)>0 and ((C11+C12)*C33 - 2*C13**2)>0):
            stab_ok = False; break

    # ---- poly consistency ----
    pc_ok = 0
    pc_total = 0
    tol_rel_pc = 0.01
    for func in ['LDA', 'GGA-WC']:
        c = ec.get(func)
        sp = pc.get(func, {})
        if not c or not sp:
            continue
        comp = compute_poly(c)
        if comp is None:
            continue
        for key in ['B','G','E','sigma','A','B_over_G','H']:
            v_sub = sp.get(key)
            v_comp = comp.get(key)
            if v_sub is None or v_comp is None:
                continue
            pc_total += 1
            if abs(v_comp) > 1e-12:
                if abs(v_sub - v_comp) / abs(v_comp) <= tol_rel_pc:
                    pc_ok += 1
            else:
                pc_ok += 1

    # ---- thermo consistency ----
    h = 6.62607015e-34
    k_B = 1.380649e-23
    NA = 6.02214076e23
    tol_rel_td = 0.05
    td_ok = 0
    td_total = 0
    for func in ['LDA', 'GGA-WC']:
        c = ec.get(func)
        sp = td.get(func, {})
        if not c or not sp:
            continue
        B, G = compute_BG(c)
        rho = rho_gold_map.get(func)
        if rho is None:
            continue
        rho_SI = rho * 1000
        B_SI = B * 1e9
        G_SI = G * 1e9
        v_l_c = math.sqrt((3*B_SI + 4*G_SI) / (3 * rho_SI))
        v_t_c = math.sqrt(G_SI / rho_SI)
        v_m_c = ((1/3) * (1/v_l_c**3 + 2/v_t_c**3)) ** (-1/3)
        M = 175.8205
        n_atoms = 4
        V_a = M / (rho * NA)
        V_atom = V_a / n_atoms
        V_atom_m3 = V_atom * 1e-6
        pref = (3 / (4 * math.pi * V_atom_m3)) ** (1/3)
        Theta_D_c = (h / k_B) * pref * v_m_c
        comp_map = {'v_l': v_l_c, 'v_t': v_t_c, 'v_m': v_m_c, 'Theta_D': Theta_D_c}
        for key in ['v_l','v_t','v_m','Theta_D']:
            v_sub = sp.get(key)
            v_comp = comp_map[key]
            if v_sub is None or v_comp is None:
                continue
            td_total += 1
            if abs(v_comp) > 1e-12:
                if abs(v_sub - v_comp) / abs(v_comp) <= tol_rel_td:
                    td_ok += 1
            else:
                td_ok += 1

    # ---- rho consistency ----
    rho_ok = 0
    rho_total = 0
    for func in ['LDA','GGA-WC']:
        sp_rho = td.get(func, {}).get('rho')
        grho = rho_gold_map.get(func)
        if sp_rho is not None and grho is not None:
            rho_total += 1
            if abs(sp_rho - grho) / abs(grho) <= 0.01:
                rho_ok += 1

    passed = (1 if stab_ok else 0) + pc_ok + td_ok + rho_ok
    total_checks = 1 + pc_total + td_total + rho_total
    if total_checks == 0:
        return 0.0
    return passed / total_checks


_SCORERS = {
    'elastic_constants_match': score_0,
    'polycrystalline_recompute': score_1,
    'thermodynamic_recompute': score_2,
    'internal_consistency': score_3,
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
