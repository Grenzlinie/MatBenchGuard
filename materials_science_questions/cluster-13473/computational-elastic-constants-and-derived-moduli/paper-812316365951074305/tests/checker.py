import os
import json
import csv
import numpy as np
from math import sqrt, pi

# === Reference table for Step 1 (MD elastic constants) ===
REFERENCE_SYSTEMS = {
    "silica":                   {"E": 88.7, "G": 41.0},
    "polyimide":                {"E": 4.2,  "G": 1.5},
    "silica_composite":         {"E": 3.4,  "G": 1.2},
    "hydroxylated_composite":   {"E": 3.3,  "G": 1.2},
    "phenoxybenzene_composite": {"E": 2.2,  "G": 0.8},
    "functionalized_composite": {"E": 4.0,  "G": 1.5},
}


def stiffness_voigt_from_iso(E, nu):
    G = E/(2*(1+nu))
    K = E/(3*(1-2*nu))
    C11 = K + 4*G/3
    C12 = K - 2*G/3
    C44 = G
    C = np.zeros((6,6))
    C[0,0]=C[1,1]=C[2,2]=C11
    C[0,1]=C[0,2]=C[1,0]=C[1,2]=C[2,0]=C[2,1]=C12
    C[3,3]=C[4,4]=C[5,5]=C44
    return C

def eshelby_sphere(nu):
    S1111 = (7-5*nu)/(15*(1-nu))
    S1122 = (5*nu-1)/(15*(1-nu))
    S2323 = (4-5*nu)/(15*(1-nu))
    return S1111, S1122, S2323

def mori_tanaka_two_phase(E_m, G_m, E_p, G_p, c_p):
    nu_m = E_m/(2*G_m)-1
    nu_p = E_p/(2*G_p)-1
    C_m = stiffness_voigt_from_iso(E_m, nu_m)
    C_p = stiffness_voigt_from_iso(E_p, nu_p)
    I = np.eye(6)
    S1111, S1122, S2323 = eshelby_sphere(nu_m)
    S = np.zeros((6,6))
    S[0,0]=S[1,1]=S[2,2]=S1111
    S[0,1]=S[0,2]=S[1,0]=S[1,2]=S[2,0]=S[2,1]=S1122
    S[3,3]=S[4,4]=S[5,5]=S2323
    C_m_inv = np.linalg.inv(C_m)
    T_p = np.linalg.inv(I + S @ C_m_inv @ (C_p - C_m))
    c_m = 1 - c_p
    C_eff = (c_m*C_m + c_p*C_p@T_p) @ np.linalg.inv(c_m*I + c_p*T_p)
    C11 = C_eff[0,0]
    C12 = C_eff[0,1]
    G_eff = C_eff[3,3]
    K_eff = (C11 + 2*C12)/3
    E_eff = 9*K_eff*G_eff/(3*K_eff + G_eff)
    return E_eff, G_eff

def composite_moduli_effective_interface(r_p, t, vf_p_given, E_p, G_p, E_m, G_m, E_i, G_i, nu_i):
    V_p = 4.0/3.0 * np.pi * r_p**3
    V_total = V_p / vf_p_given
    r_outer = r_p + t
    V_i = 4.0/3.0 * np.pi * (r_outer**3 - r_p**3)
    vf_i = V_i / V_total
    vf_p = vf_p_given
    vf_m = 1 - vf_p - vf_i
    if vf_m < 0:
        vf_m = 0
    nu_m = E_m/(2*G_m)-1
    C_p = stiffness_voigt_from_iso(E_p, E_p/(2*G_p)-1)
    C_m = stiffness_voigt_from_iso(E_m, nu_m)
    C_i = stiffness_voigt_from_iso(E_i, nu_i)
    I = np.eye(6)
    S1111, S1122, S2323 = eshelby_sphere(nu_m)
    S = np.zeros((6,6))
    S[0,0]=S[1,1]=S[2,2]=S1111
    S[0,1]=S[0,2]=S[1,0]=S[1,2]=S[2,0]=S[2,1]=S1122
    S[3,3]=S[4,4]=S[5,5]=S2323
    C_m_inv = np.linalg.inv(C_m)
    T_p = np.linalg.inv(I + S @ C_m_inv @ (C_p - C_m))
    # T_pi computing
    cp_ci = vf_p + vf_i
    try:
        C_i_minus_Cm_inv = np.linalg.inv(C_i - C_m)
    except np.linalg.LinAlgError:
        return 0.0, 0.0
    term_i = np.linalg.inv(S + C_i_minus_Cm_inv @ C_m)
    try:
        C_p_minus_Cm_inv = np.linalg.inv(C_p - C_m)
    except np.linalg.LinAlgError:
        return 0.0, 0.0
    term_p = np.linalg.inv(S + C_p_minus_Cm_inv @ C_m)
    T_pi = I - S @ ( (vf_p/cp_ci)*term_p + (vf_i/cp_ci)*term_i )
    # composite stiffness
    C_comp = C_m + ( cp_ci * (C_i - C_m) @ T_pi + vf_p * (C_p - C_i) @ T_p ) @ np.linalg.inv( vf_m * I + cp_ci * T_pi )
    C11 = C_comp[0,0]
    C12 = C_comp[0,1]
    G_c = C_comp[3,3]
    K_c = (C11 + 2*C12)/3
    E_c = 9*K_c*G_c/(3*K_c + G_c)
    return E_c, G_c


# ====== contract gate (unchanged) ======
import os as _ff_os
import json as _ff_json

def _ff_validate_output_contract():
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
            except Exception as exc:
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
            except Exception as exc:
                violations.append(base + ": cannot read table (" + str(exc) + ")")
                continue
            required_cols = schema.get("required_columns", []) or []
            for col in required_cols:
                name = col.get("name") if isinstance(col, dict) else col
                if name and name not in cols:
                    violations.append(base + ": missing table column '" + str(name) + "'")
    return violations

def _ff_contract_gate():
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
        except Exception:
            return None
    if path.endswith(".csv") or path.endswith(".tsv"):
        delim = "\t" if path.endswith(".tsv") else ","
        with open(path, newline="") as f:
            return list(csv.DictReader(f, delimiter=delim))
    with open(path) as f:
        return f.read()


def prepare(outputs_dir, spec):
    # no gold needed
    return {}


# === block: score_0 (step2_elastic_constants) ===
def score_0(artifact, step, ctx):
    rows = artifact
    if len(rows) != 6:
        return 0.0
    tolerance = 1e-4   # essentially exact match
    correct = 0
    for row in rows:
        sys = row["system"].strip()
        if sys in REFERENCE_SYSTEMS:
            try:
                E = float(row["E"])
                G = float(row["G"])
            except:
                continue
            ref_E = REFERENCE_SYSTEMS[sys]["E"]
            ref_G = REFERENCE_SYSTEMS[sys]["G"]
            if abs(E - ref_E) <= tolerance and abs(G - ref_G) <= tolerance:
                correct += 1
    return correct / 6.0


# === block: score_1 (step3_mori_tanaka_rve) ===
def score_1(artifact, step, ctx):
    rows = artifact
    if len(rows) != 4:
        return 0.0
    # load pure moduli from the agent's elastic_constants
    elastic_path = "/app/outputs/elastic_constants_systems.csv"
    if not os.path.exists(elastic_path):
        return 0.0
    with open(elastic_path, newline='') as f:
        elastic_rows = list(csv.DictReader(f))
    pure = {}
    for r in elastic_rows:
        pure[r["system"].strip()] = {"E": float(r["E"]), "G": float(r["G"])}
    if "silica" not in pure or "polyimide" not in pure:
        return 0.0
    E_s = pure["silica"]["E"]
    G_s = pure["silica"]["G"]
    E_m = pure["polyimide"]["E"]
    G_m = pure["polyimide"]["G"]
    c_p = 0.017
    # Compute expected Mori-Tanaka
    E_exp, G_exp = mori_tanaka_two_phase(E_m, G_m, E_s, G_s, c_p)
    # Compare each composite row (they are all the same MT prediction)
    tolerance = 0.01  # 1%
    correct = 0
    for row in rows:
        try:
            E = float(row["E_MT"])
            G = float(row["G_MT"])
        except:
            continue
        if abs(E - E_exp)/E_exp <= tolerance and abs(G - G_exp)/G_exp <= tolerance:
            correct += 1
    return correct / 4.0


# === block: score_2 (step4_effective_interface) ===
def score_2(artifact, step, ctx):
    rows = artifact
    if len(rows) != 4:
        return 0.0
    # load composite MD moduli from agent
    elastic_path = "/app/outputs/elastic_constants_systems.csv"
    if not os.path.exists(elastic_path):
        return 0.0
    with open(elastic_path, newline='') as f:
        elastic_rows = list(csv.DictReader(f))
    pure = {}
    comp = {}
    for r in elastic_rows:
        sys = r["system"].strip()
        e = float(r["E"])
        g = float(r["G"])
        if sys == "silica":
            pure["silica"] = {"E": e, "G": g}
        elif sys == "polyimide":
            pure["polyimide"] = {"E": e, "G": g}
        else:
            comp[sys] = {"E": e, "G": g}
    if "silica" not in pure or "polyimide" not in pure:
        return 0.0
    E_s = pure["silica"]["E"]
    G_s = pure["silica"]["G"]
    E_m = pure["polyimide"]["E"]
    G_m = pure["polyimide"]["G"]
    composites = ["silica_composite", "hydroxylated_composite", "phenoxybenzene_composite", "functionalized_composite"]
    tolerance = 0.01
    correct = 0
    for row in rows:
        ctype = row["composite_type"].strip()
        if ctype not in composites or ctype not in comp:
            continue
        try:
            Ei = float(row["E_interface"])
            Gi = float(row["G_interface"])
        except:
            continue
        target_E = comp[ctype]["E"]
        target_G = comp[ctype]["G"]
        nu_i = 0.4
        rp = 6.0
        t = 12.0
        vf = 0.017
        E_pred, G_pred = composite_moduli_effective_interface(rp, t, vf, E_s, G_s, E_m, G_m, Ei, Gi, nu_i)
        if E_pred <= 0 or G_pred <= 0:
            continue
        err_E = abs(E_pred - target_E)/target_E
        err_G = abs(G_pred - target_G)/target_G
        if err_E <= tolerance and err_G <= tolerance:
            correct += 1
    return correct / 4.0


# === block: score_3 (step5_moduli_vs_radius) ===
def score_3(artifact, step, ctx):
    rows = artifact
    # load pure & interface from agent
    elastic_path = "/app/outputs/elastic_constants_systems.csv"
    interface_path = "/app/outputs/effective_interface_properties.csv"
    if not os.path.exists(elastic_path) or not os.path.exists(interface_path):
        return 0.0

    with open(elastic_path, newline='') as f:
        elastic_rows = list(csv.DictReader(f))
    pure = {"silica": None, "polyimide": None}
    for r in elastic_rows:
        sys = r["system"].strip()
        if sys in pure:
            pure[sys] = {"E": float(r["E"]), "G": float(r["G"])}
    if pure["silica"] is None or pure["polyimide"] is None:
        return 0.0
    E_s = pure["silica"]["E"]
    G_s = pure["silica"]["G"]
    E_m = pure["polyimide"]["E"]
    G_m = pure["polyimide"]["G"]

    with open(interface_path, newline='') as f:
        int_rows = list(csv.DictReader(f))
    interfaces = {}
    for r in int_rows:
        interfaces[r["composite_type"].strip()] = {"E": float(r["E_interface"]), "G": float(r["G_interface"])}

    composites = ["silica_composite", "hydroxylated_composite", "phenoxybenzene_composite", "functionalized_composite"]
    ei_rows = [r for r in rows if r["model_type"].strip() == "Effective-Interface"]
    mt_rows = [r for r in rows if r["model_type"].strip() == "Mori-Tanaka"]

    # 1) EI internal consistency
    score_consistency = 0.0
    if ei_rows:
        total_points = 0
        consistent_points = 0
        for r in ei_rows:
            comp = r["composite_type"].strip()
            if comp not in composites or comp not in interfaces:
                continue
            try:
                radius = float(r["radius_A"])
                E_sub = float(r["E"])
                G_sub = float(r["G"])
            except:
                continue
            Ei = interfaces[comp]["E"]
            Gi = interfaces[comp]["G"]
            nu_i = 0.4
            t = 12.0
            vf_p = 0.05
            E_pred, G_pred = composite_moduli_effective_interface(radius, t, vf_p, E_s, G_s, E_m, G_m, Ei, Gi, nu_i)
            if E_pred <= 0 or G_pred <= 0:
                continue
            err_E = abs(E_sub - E_pred) / E_pred if E_pred > 1e-6 else 1.0
            err_G = abs(G_sub - G_pred) / G_pred if G_pred > 1e-6 else 1.0
            if err_E <= 0.01 and err_G <= 0.01:
                consistent_points += 1
            total_points += 1
        if total_points > 0:
            score_consistency = consistent_points / total_points

    # 2) MT correctness
    score_mt = 0.0
    if mt_rows:
        c_p = 0.05
        E_mt_exp, G_mt_exp = mori_tanaka_two_phase(E_m, G_m, E_s, G_s, c_p)
        total_mt = 0
        ok_mt = 0
        for r in mt_rows:
            try:
                Emt = float(r["E"])
                Gmt = float(r["G"])
            except:
                continue
            if abs(Emt - E_mt_exp)/E_mt_exp <= 0.02 and abs(Gmt - G_mt_exp)/G_mt_exp <= 0.02:
                ok_mt += 1
            total_mt += 1
        if total_mt > 0:
            score_mt = ok_mt / total_mt

    # 3) Convergence at large radii (EI vs MT)
    conv_points = 0
    conv_ok = 0
    if ei_rows and mt_rows:
        for comp in composites:
            mt_comp_rows = [r for r in mt_rows if r["composite_type"].strip() == comp]
            if not mt_comp_rows:
                continue
            try:
                mt_E = float(mt_comp_rows[0]["E"])
                mt_G = float(mt_comp_rows[0]["G"])
            except:
                continue
            ei_comp = [r for r in ei_rows if r["composite_type"].strip() == comp]
            if not ei_comp:
                continue
            for target_radius in [1000, 5000]:
                radii = [float(r["radius_A"]) for r in ei_comp]
                diffs = [abs(r - target_radius) for r in radii]
                if min(diffs) > 500:
                    continue
                idx = np.argmin(diffs)
                try:
                    E_val = float(ei_comp[idx]["E"])
                    G_val = float(ei_comp[idx]["G"])
                except:
                    continue
                if mt_E > 0:
                    if abs(E_val - mt_E)/mt_E <= 0.05 and abs(G_val - mt_G)/mt_G <= 0.05:
                        conv_ok += 1
                    conv_points += 1
    score_convergence = conv_ok / conv_points if conv_points > 0 else 0.0

    # 4) Monotonic increase
    monotonic_points = 0
    monotonic_violations = 0
    if ei_rows:
        for comp in composites:
            comp_rows = [r for r in ei_rows if r["composite_type"].strip() == comp]
            if len(comp_rows) < 2:
                continue
            sorted_rows = sorted(comp_rows, key=lambda r: float(r["radius_A"]))
            prev_E = None
            prev_G = None
            for r in sorted_rows:
                try:
                    E = float(r["E"])
                    G = float(r["G"])
                except:
                    continue
                if prev_E is not None:
                    if E < prev_E - 1e-6 or G < prev_G - 1e-6:
                        monotonic_violations += 1
                    monotonic_points += 2
                prev_E = E
                prev_G = G
    score_monotonic = 1.0 - (monotonic_violations / monotonic_points) if monotonic_points > 0 else 0.0

    # 5) Ordering among composites at the largest common radius
    ordering_score = 0.0
    if ei_rows:
        radii_by_comp = {}
        for comp in composites:
            comp_rows = [r for r in ei_rows if r["composite_type"].strip() == comp]
            if not comp_rows:
                continue
            radii = [float(r["radius_A"]) for r in comp_rows]
            radii_by_comp[comp] = max(radii)
        if len(radii_by_comp) == 4:
            common_r = min(radii_by_comp.values())
            vals = {}
            for comp in composites:
                comp_rows = [r for r in ei_rows if r["composite_type"].strip() == comp]
                radii = [float(r["radius_A"]) for r in comp_rows]
                idx = np.argmin([abs(r - common_r) for r in radii])
                vals[comp] = {"E": float(comp_rows[idx]["E"]), "G": float(comp_rows[idx]["G"])}
            # expected order: functionalized >= silica_composite >= hydroxylated >= phenoxybenzene
            ok = 0
            total = 0
            if vals["functionalized_composite"]["E"] >= vals["silica_composite"]["E"] >= vals["hydroxylated_composite"]["E"] >= vals["phenoxybenzene_composite"]["E"]:
                ok += 1
            total += 1
            if vals["functionalized_composite"]["G"] >= vals["silica_composite"]["G"] >= vals["hydroxylated_composite"]["G"] >= vals["phenoxybenzene_composite"]["G"]:
                ok += 1
            total += 1
            ordering_score = ok / total if total > 0 else 0.0

    # Combine sub-scores (weights reflect importance)
    final_score = 0.5 * score_consistency + 0.2 * score_mt + 0.15 * score_convergence + 0.1 * score_monotonic + 0.05 * ordering_score
    return min(max(final_score, 0.0), 1.0)


_SCORERS = {
    'step2_elastic_constants': score_0,
    'step3_mori_tanaka_rve': score_1,
    'step4_effective_interface': score_2,
    'step5_moduli_vs_radius': score_3,
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
            except Exception as exc:
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