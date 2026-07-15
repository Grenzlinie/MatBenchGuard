import os
import json
import csv

# === author imports / helpers ===
import os, json, math
try:
    from scipy.integrate import quad
except ImportError:
    quad = None

# physical constants
h = 6.62607015e-34
kB = 1.380649e-23
NA = 6.02214076e23
pi = math.pi

# atomic masses (g/mol)
MASS = {'C3': 12.0107, 'Si3': 28.0855, 'Ge3': 72.63}

def isotropic_velocities(rho, B, G):
    # rho in g/cm^3, B,G in GPa; returns m/s
    rho_si = rho * 1000.0
    B_si = B * 1e9
    G_si = G * 1e9
    v_l = math.sqrt((3*B_si + 4*G_si) / (3*rho_si))
    v_t = math.sqrt(G_si / rho_si)
    v_m = ((1.0/3.0) * (1.0/v_l**3 + 2.0/v_t**3)) ** (-1.0/3.0)
    return v_l, v_t, v_m

def debye_temp(v_m, rho, M, n=1):
    # v_m in m/s, rho in g/cm^3, M in g/mol; returns K
    rho_si = rho * 1000.0
    M_si = M * 1e-3
    factor = (3*n/(4*pi)) * (NA * rho_si / M_si)
    return (h/kB) * (factor ** (1/3)) * v_m

def anisotropic_velocities(C11, C12, C13, C33, C44, rho):
    # Cij in GPa, rho in g/cm^3; returns dict with [001] and [100]
    rho_si = rho * 1000.0
    C11_si = C11 * 1e9
    C12_si = C12 * 1e9
    C33_si = C33 * 1e9
    C44_si = C44 * 1e9
    vl_001 = math.sqrt(C33_si / rho_si)
    vt1_001 = math.sqrt(C44_si / rho_si)
    vl_100 = math.sqrt((C11_si - C12_si) / (2*rho_si))
    vt1_100 = math.sqrt(C11_si / rho_si)
    vt2_100 = math.sqrt(C44_si / rho_si)
    return {
        '[001]': {'v_l': vl_001, 'v_t1': vt1_001, 'v_t2': vt1_001},
        '[100]': {'v_l': vl_100, 'v_t1': vt1_100, 'v_t2': vt2_100}
    }

def _cahill_integrand(x):
    expx = math.exp(x)
    return x**3 * expx / (expx - 1)**2

def min_thermal_conductivity(v_l, v_t1, v_t2, rho, M, T=300):
    # v in m/s, rho in g/cm^3, M in g/mol; returns W/(cm*K)
    if quad is None:
        raise RuntimeError('scipy required for Cahill integral')
    rho_si = rho * 1000.0
    M_si = M * 1e-3
    N = NA * rho_si / M_si
    hbar = h / (2*pi)
    vels = [v_l, v_t1, v_t2]
    total = 0.0
    for vi in vels:
        Theta_i = vi * hbar / kB * (6*pi**2*N)**(1/3)
        upper = Theta_i / T
        integral, _ = quad(_cahill_integrand, 0, upper, limit=200)
        total += vi * (T / Theta_i)**2 * integral
    kappa_SI = (pi/6)**(1/3) * kB * N**(2/3) * total  # W/(m*K)
    return kappa_SI * 0.01  # convert to W/(cm*K)


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
        eco_path = os.path.join(outputs_dir, 'elastic_constants.json')
        ctx = {}
        if os.path.exists(eco_path):
            with open(eco_path) as f:
                eco = json.load(f)
            ctx['elastic_constants'] = eco
        return ctx


# === block: score_0 (check id='step4_isotropic_thermo') ===
def score_0(artifact, step, ctx):
        gold = step['gold']
        tol_gold = step['tolerances_gold']
        tol_cons = step.get('tolerance_consistency', 0.01)
        w_gold = step.get('weight_gold', 0.8)
        w_cons = step.get('weight_consistency', 0.2)
        eco = ctx.get('elastic_constants')
        materials = ['C3', 'Si3', 'Ge3']
        prop_names = ['v_l', 'v_t', 'v_m', 'Theta_D']
        scores_gold = []
        scores_cons = []
        for mat in materials:
            if mat not in artifact:
                continue
            agent_vals = artifact[mat]
            gold_vals = gold.get(mat, {})
            if eco and mat in eco:
                rho = eco[mat].get('density')
                B = eco[mat].get('B')
                G = eco[mat].get('G')
                if rho is None or B is None or G is None:
                    continue
                v_l, v_t, v_m = isotropic_velocities(rho, B, G)
                M = MASS[mat]
                Theta_D = debye_temp(v_m, rho, M)
                recomputed = {'v_l': v_l, 'v_t': v_t, 'v_m': v_m, 'Theta_D': Theta_D}
                for p in prop_names:
                    if p in agent_vals and p in recomputed:
                        ref = recomputed[p]
                        aval = agent_vals[p]
                        tc = tol_cons * max(abs(ref), 1.0)
                        scores_cons.append(1.0 if abs(aval - ref) <= tc else 0.0)
                    else:
                        scores_cons.append(0.0)
                for p in prop_names:
                    if p in gold_vals and p in recomputed:
                        gv = gold_vals[p]
                        rv = recomputed[p]
                        tg = tol_gold.get(p, 0.05) * max(abs(gv), 1e-9)
                        scores_gold.append(1.0 if abs(rv - gv) <= tg else 0.0)
                    else:
                        scores_gold.append(0.0)
            else:
                for p in prop_names:
                    if p in agent_vals and p in gold_vals:
                        gv = gold_vals[p]
                        av = agent_vals[p]
                        tg = tol_gold.get(p, 0.05) * max(abs(gv), 1e-9)
                        scores_gold.append(1.0 if abs(av - gv) <= tg else 0.0)
        avg_gold = sum(scores_gold)/len(scores_gold) if scores_gold else 0.0
        avg_cons = sum(scores_cons)/len(scores_cons) if scores_cons else 0.0
        return w_gold * avg_gold + w_cons * avg_cons


# === block: score_1 (check id='step5_anisotropic_velocities') ===
def score_1(artifact, step, ctx):
        gold = step['gold']
        tol_gold = step['tolerances_gold']
        tol_cons = step.get('tolerance_consistency', 0.01)
        w_gold = step.get('weight_gold', 0.8)
        w_cons = step.get('weight_consistency', 0.2)
        eco = ctx.get('elastic_constants')
        materials = ['C3', 'Si3', 'Ge3']
        dirs = ['[001]', '[100]']
        prop_names = ['v_l', 'v_t1', 'v_t2']
        scores_gold = []
        scores_cons = []
        for mat in materials:
            if mat not in artifact:
                continue
            agent_mat = artifact[mat]
            gold_mat = gold.get(mat, {})
            if eco and mat in eco and all(k in eco[mat] for k in ['density','C11','C12','C13','C33','C44']):
                rho = eco[mat]['density']
                C11 = eco[mat]['C11']
                C12 = eco[mat]['C12']
                C13 = eco[mat]['C13']
                C33 = eco[mat]['C33']
                C44 = eco[mat]['C44']
                recomputed = anisotropic_velocities(C11, C12, C13, C33, C44, rho)
                for d in dirs:
                    agent_dir = agent_mat.get(d, {})
                    rec_dir = recomputed.get(d, {})
                    gold_dir = gold_mat.get(d, {})
                    for p in prop_names:
                        if p in agent_dir and p in rec_dir:
                            ref = rec_dir[p]
                            aval = agent_dir[p]
                            tc = tol_cons * max(abs(ref), 1.0)
                            scores_cons.append(1.0 if abs(aval - ref) <= tc else 0.0)
                        else:
                            scores_cons.append(0.0)
                        if p in gold_dir and p in rec_dir:
                            gv = gold_dir[p]
                            rv = rec_dir[p]
                            tg = tol_gold.get(p, 0.05) * max(abs(gv), 1e-9)
                            scores_gold.append(1.0 if abs(rv - gv) <= tg else 0.0)
                        else:
                            scores_gold.append(0.0)
            else:
                for d in dirs:
                    agent_dir = agent_mat.get(d, {})
                    gold_dir = gold_mat.get(d, {})
                    for p in prop_names:
                        if p in agent_dir and p in gold_dir:
                            gv = gold_dir[p]
                            av = agent_dir[p]
                            tg = tol_gold.get(p, 0.05) * max(abs(gv), 1e-9)
                            scores_gold.append(1.0 if abs(av - gv) <= tg else 0.0)
        avg_gold = sum(scores_gold)/len(scores_gold) if scores_gold else 0.0
        avg_cons = sum(scores_cons)/len(scores_cons) if scores_cons else 0.0
        return w_gold * avg_gold + w_cons * avg_cons


# === block: score_2 (check id='step6_min_thermal_conductivity') ===
def score_2(artifact, step, ctx):
        gold = step['gold']
        tol_gold = step['tolerances_gold']
        tol_cons = step.get('tolerance_consistency', 0.02)
        w_gold = step.get('weight_gold', 0.8)
        w_cons = step.get('weight_consistency', 0.2)
        eco = ctx.get('elastic_constants')
        materials = ['C3', 'Si3', 'Ge3']
        keys = ['isotropic', '[001]', '[100]']
        scores_gold = []
        scores_cons = []
        for mat in materials:
            if mat not in artifact:
                continue
            agent_mat = artifact[mat]
            gold_mat = gold.get(mat, {})
            if eco and mat in eco and all(k in eco[mat] for k in ['density','B','G','C11','C12','C13','C33','C44']):
                rho = eco[mat]['density']
                B = eco[mat]['B']
                G = eco[mat]['G']
                C11 = eco[mat]['C11']
                C12 = eco[mat]['C12']
                C13 = eco[mat]['C13']
                C33 = eco[mat]['C33']
                C44 = eco[mat]['C44']
                M = MASS[mat]
                # isotropic kappa from isotropic sound velocities
                v_l, v_t, v_m = isotropic_velocities(rho, B, G)
                kappa_iso = min_thermal_conductivity(v_l, v_t, v_t, rho, M, T=300)
                # directional kappa from anisotropic velocities
                aniso = anisotropic_velocities(C11, C12, C13, C33, C44, rho)
                dir001 = aniso['[001]']
                kappa_001 = min_thermal_conductivity(dir001['v_l'], dir001['v_t1'], dir001['v_t2'], rho, M, T=300)
                dir100 = aniso['[100]']
                kappa_100 = min_thermal_conductivity(dir100['v_l'], dir100['v_t1'], dir100['v_t2'], rho, M, T=300)
                recomputed = {'isotropic': kappa_iso, '[001]': kappa_001, '[100]': kappa_100}
                for k in keys:
                    if k in agent_mat and k in recomputed:
                        ref = recomputed[k]
                        aval = agent_mat[k]
                        tc = tol_cons * max(abs(ref), 1e-9)
                        scores_cons.append(1.0 if abs(aval - ref) <= tc else 0.0)
                    else:
                        scores_cons.append(0.0)
                    if k in gold_mat and k in recomputed:
                        gv = gold_mat[k]
                        rv = recomputed[k]
                        tg = tol_gold.get(k, 0.10) * max(abs(gv), 1e-9)
                        scores_gold.append(1.0 if abs(rv - gv) <= tg else 0.0)
                    else:
                        scores_gold.append(0.0)
            else:
                for k in keys:
                    if k in agent_mat and k in gold_mat:
                        gv = gold_mat[k]
                        av = agent_mat[k]
                        tg = tol_gold.get(k, 0.10) * max(abs(gv), 1e-9)
                        scores_gold.append(1.0 if abs(av - gv) <= tg else 0.0)
        avg_gold = sum(scores_gold)/len(scores_gold) if scores_gold else 0.0
        avg_cons = sum(scores_cons)/len(scores_cons) if scores_cons else 0.0
        return w_gold * avg_gold + w_cons * avg_cons


_SCORERS = {
    'step4_isotropic_thermo': score_0,
    'step5_anisotropic_velocities': score_1,
    'step6_min_thermal_conductivity': score_2,
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
