import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math, re


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
    return {'outputs_dir': '/app/outputs'}


# === block: score_0 (check id='s1') ===
def score_0(artifact, step, ctx):
    import re
    path = os.path.join(ctx['outputs_dir'], 'step_01_lattice_parameter.txt')
    try:
        with open(path) as f:
            text = f.read()
        m = re.search(r'lattice_parameter_angstrom\s*=\s*([\d.]+)', text)
        if not m:
            return 0.0
        val = float(m.group(1))
    except:
        return 0.0
    gold = step['config']['gold_a0']
    tol = step['config']['tolerance']
    max_dev = step['config']['max_deviation']
    diff = abs(val - gold)
    if diff <= tol:
        return 1.0
    score = max(0.0, 1.0 - (diff - tol) / (max_dev - tol))
    return score


# === block: score_1 (check id='s2') ===
def score_1(artifact, step, ctx):
    val = artifact
    gold = step['config']['gold']
    tol = step['config']['tolerance']
    max_dev = step['config']['max_deviation']
    keys = ['C11_GPa','C12_GPa','C44_GPa']
    scores = []
    for k in keys:
        v = val.get(k)
        g = gold[k]
        if v is None:
            scores.append(0.0)
            continue
        d = abs(v - g)
        if d <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (d - tol)/(max_dev - tol)))
    return sum(scores)/len(scores)


# === block: score_2 (check id='s3') ===
def score_2(artifact, step, ctx):
    path_c = os.path.join(ctx['outputs_dir'], 'step_02_elastic_constants.json')
    try:
        with open(path_c) as f:
            c = json.load(f)
        C11 = c['C11_GPa']
        C12 = c['C12_GPa']
        C44 = c['C44_GPa']
    except:
        return 0.0
    B = (C11 + 2*C12) / 3.0
    G_v = (C11 - C12 + 3*C44) / 5.0
    G_r = 5*(C11-C12)*C44 / (4*C44 + 3*(C11-C12))
    G = (G_v + G_r) / 2.0
    E_val = 9*B*G / (3*B + G)
    Poisson = (3*B - 2*G) / (2*(3*B + G))
    G_B = G / B
    recomputed = {'B': B, 'G': G, 'E': E_val, 'Poisson': Poisson, 'G_B': G_B}
    gold = step['config']['gold']
    tol = step['config']['tolerance']
    max_dev = step['config'].get('max_deviation', {k: v*2 for k,v in tol.items()})
    map_keys = {'B_VRH_GPa': 'B', 'G_VRH_GPa': 'G', 'E_VRH_GPa': 'E', 'Poisson_ratio': 'Poisson', 'G_B_ratio': 'G_B'}
    scores = []
    for k_sub, k_rec in map_keys.items():
        v_rec = recomputed[k_rec]
        g = gold[k_sub]
        d = abs(v_rec - g)
        t = tol.get(k_sub, 0.1)
        if d <= t:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (d - t) / (max_dev.get(k_sub, t*2))))
    gold_score = sum(scores)/len(scores)
    consistency = 0.0
    if artifact is not None:
        try:
            cons_keys = [('B_VRH_GPa','B'), ('G_VRH_GPa','G'), ('E_VRH_GPa','E'), ('Poisson_ratio','Poisson'), ('G_B_ratio','G_B')]
            c_scores = []
            for k_sub, k_rec in cons_keys:
                if k_sub in artifact:
                    d = abs(artifact[k_sub] - recomputed[k_rec])
                    if d < 0.1:
                        c_scores.append(1.0)
                    else:
                        c_scores.append(max(0.0, 1.0 - d*10))
                else:
                    c_scores.append(0.0)
            consistency = sum(c_scores)/len(c_scores)
        except:
            consistency = 0.0
    return 0.9 * gold_score + 0.1 * consistency


# === block: score_3 (check id='s4') ===
def score_3(artifact, step, ctx):
    path_a = os.path.join(ctx['outputs_dir'], 'step_01_lattice_parameter.txt')
    path_c = os.path.join(ctx['outputs_dir'], 'step_02_elastic_constants.json')
    try:
        with open(path_a) as f:
            txt = f.read()
        m = re.search(r'lattice_parameter_angstrom\s*=\s*([\d.]+)', txt)
        a0 = float(m.group(1))
        with open(path_c) as f:
            c = json.load(f)
        C11 = c['C11_GPa']
        C12 = c['C12_GPa']
        C44 = c['C44_GPa']
    except:
        return 0.0
    a_cm = a0 * 1e-8
    vol_uc = a_cm**3
    N_A = 6.02214076e23
    M_per_formula = 174.967 + 2*1.008
    Z = 4
    mass_uc = Z * M_per_formula / N_A
    rho = mass_uc / vol_uc
    rho_kgm3 = rho * 1000.0
    G_v = (C11 - C12 + 3*C44)/5.0
    G_r = 5*(C11-C12)*C44/(4*C44+3*(C11-C12))
    G = (G_v+G_r)/2.0
    B = (C11+2*C12)/3.0
    G_Pa = G * 1e9
    B_Pa = B * 1e9
    Vs = math.sqrt(G_Pa / rho_kgm3) * 1e-3
    Vp = math.sqrt((B_Pa + 4.0*G_Pa/3.0) / rho_kgm3) * 1e-3
    Vm = ( (2.0/(Vs**3) + 1.0/(Vp**3)) / 3.0 ) ** (-1.0/3.0)
    h = 6.62607015e-34
    k_B = 1.380649e-23
    n_atoms = 3
    M_kg = M_per_formula / 1000.0
    factor = (3.0 * n_atoms / (4.0 * math.pi) * (N_A * rho_kgm3 / M_kg)) ** (1.0/3.0)
    Theta = h / k_B * factor * Vm * 1000.0
    k_val = G/B
    Hv = 2.0 * (k_val**2 * G) ** 0.585 - 3.0
    recomputed = {'Vs': Vs, 'Vp': Vp, 'Vm': Vm, 'Theta': Theta, 'Hv': Hv}
    gold = step['config']['gold']
    tol = step['config']['tolerance']
    max_dev = step['config'].get('max_deviation', {k: v*2 for k,v in tol.items()})
    keys = ['Vs_km_s','Vp_km_s','Vm_km_s','Debye_temperature_K','Hardness_Hv_GPa']
    map_rec = {'Vs_km_s':'Vs','Vp_km_s':'Vp','Vm_km_s':'Vm','Debye_temperature_K':'Theta','Hardness_Hv_GPa':'Hv'}
    scores = []
    for k in keys:
        v = recomputed[map_rec[k]]
        g = gold[k]
        d = abs(v - g)
        t = tol.get(k, 0.1)
        if d <= t:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (d - t) / (max_dev.get(k, t*2))))
    return sum(scores)/len(scores)


# === block: score_4 (check id='s5') ===
def score_4(artifact, step, ctx):
    try:
        direction = artifact.get('direction')
        strength = artifact.get('ideal_tensile_strength_GPa')
        strain = artifact.get('failure_strain_percent')
    except:
        return 0.0
    gold = step['config']['gold']
    tol = step['config']['tolerance']
    max_dev = step['config'].get('max_deviation', {k: v*2 for k,v in tol.items()})
    d_s = abs(strength - gold['strength'])
    d_e = abs(strain - gold['strain'])
    t_s = tol.get('strength', 2.0)
    t_e = tol.get('strain', 5.0)
    md_s = max_dev.get('strength', t_s*2)
    md_e = max_dev.get('strain', t_e*2)
    scores = []
    if d_s <= t_s:
        scores.append(1.0)
    else:
        scores.append(max(0.0, 1.0 - (d_s - t_s)/(md_s - t_s)))
    if d_e <= t_e:
        scores.append(1.0)
    else:
        scores.append(max(0.0, 1.0 - (d_e - t_e)/(md_e - t_e)))
    return sum(scores)/len(scores)


# === block: score_5 (check id='s7') ===
def score_5(artifact, step, ctx):
    val = artifact
    freqs = ['T1u_DFPT_THz','T1u_finite_displacement_THz','T2g_DFPT_THz','T2g_finite_displacement_THz']
    gold = step['config']['gold']
    tol = step['config']['tolerance']
    max_dev = step['config'].get('max_deviation', tol)
    scores = []
    for f in freqs:
        v = val.get(f)
        g = gold[f]
        if v is None:
            scores.append(0.0)
            continue
        d = abs(v - g)
        if d <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (d - tol)/(max_dev - tol)))
    freq_score = sum(scores)/len(freqs)
    order_scores = []
    try:
        if val.get('T2g_DFPT_THz',0) > val.get('T1u_DFPT_THz',0):
            order_scores.append(1.0)
        else:
            order_scores.append(0.0)
        if val.get('T2g_finite_displacement_THz',0) > val.get('T1u_finite_displacement_THz',0):
            order_scores.append(1.0)
        else:
            order_scores.append(0.0)
        if val.get('T1u_DFPT_THz',0) > val.get('T1u_finite_displacement_THz',0):
            order_scores.append(1.0)
        else:
            order_scores.append(0.0)
        if val.get('T2g_DFPT_THz',0) > val.get('T2g_finite_displacement_THz',0):
            order_scores.append(1.0)
        else:
            order_scores.append(0.0)
    except:
        order_scores = [0.0,0.0,0.0,0.0]
    order_score = sum(order_scores)/len(order_scores)
    return 0.8 * freq_score + 0.2 * order_score


# === block: score_6 (check id='s8') ===
def score_6(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < step['config']['min_rows']:
        return 0.0
    cols = {'temperature_K','entropy_J_per_mol_K','heat_capacity_Cv_J_per_mol_K'}
    if not all(c in rows[0] for c in cols):
        return 0.0
    Ts = []
    Ss = []
    Cvs = []
    for r in rows:
        try:
            Ts.append(float(r['temperature_K']))
            Ss.append(float(r['entropy_J_per_mol_K']))
            Cvs.append(float(r['heat_capacity_Cv_J_per_mol_K']))
        except:
            return 0.0
    def non_decreasing(seq):
        return all(y >= x for x,y in zip(seq, seq[1:]))
    def strictly_increasing(seq):
        return all(y > x for x,y in zip(seq, seq[1:]))
    scores = []
    scores.append(1.0 if len(rows) >= step['config']['min_rows'] else 0.0)
    scores.append(1.0 if strictly_increasing(Ts) else 0.0)
    scores.append(1.0 if non_decreasing(Ss) else 0.0)
    scores.append(1.0 if non_decreasing(Cvs) else 0.0)
    final_cv = Cvs[-1] if Cvs else 0
    dp_score = 1.0 if 70 <= final_cv <= 80 else 0.0
    scores.append(dp_score)
    weights = [0.1, 0.2, 0.2, 0.2, 0.3]
    return sum(w * s for w, s in zip(weights, scores))


_SCORERS = {
    's1': score_0,
    's2': score_1,
    's3': score_2,
    's4': score_3,
    's5': score_4,
    's7': score_5,
    's8': score_6,
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
