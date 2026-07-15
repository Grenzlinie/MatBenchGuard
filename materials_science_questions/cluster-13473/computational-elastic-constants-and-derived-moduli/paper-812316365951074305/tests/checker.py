import os
import json
import csv

# === author imports / helpers ===
import csv
import numpy as np
from math import sqrt, pi

def stiffness_from_e_g(E, G):
    nu = E/(2*G) - 1
    K = E/(3*(1-2*nu))
    C11 = K + 4*G/3
    C12 = K - 2*G/3
    C44 = G
    return C11, C12, C44, nu

def eshelby_sphere(nu):
    S1111 = (7-5*nu)/(15*(1-nu))
    S1122 = (5*nu-1)/(15*(1-nu))
    S2323 = (4-5*nu)/(15*(1-nu))
    return S1111, S1122, S2323

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

def composite_moduli_effective_interface(r_p, t, vf_p_given, E_p, G_p, E_m, G_m, E_i, G_i, nu_i):
    # volume fractions
    V_p = 4.0/3.0 * np.pi * r_p**3
    V_total = V_p / vf_p_given
    r_outer = r_p + t
    V_i = 4.0/3.0 * np.pi * (r_outer**3 - r_p**3)
    vf_i = V_i / V_total
    vf_p = vf_p_given
    vf_m = 1 - vf_p - vf_i
    if vf_m < 0:
        vf_m = 0
    # stiffness matrices
    C_p = stiffness_voigt_from_iso(E_p, (E_p/(2*G_p)-1))
    C_m = stiffness_voigt_from_iso(E_m, (E_m/(2*G_m)-1))
    nu_m = E_m/(2*G_m)-1
    S1111, S1122, S2323 = eshelby_sphere(nu_m)
    S = np.zeros((6,6))
    S[0,0]=S[1,1]=S[2,2]=S1111
    S[0,1]=S[0,2]=S[1,0]=S[1,2]=S[2,0]=S[2,1]=S1122
    S[3,3]=S[4,4]=S[5,5]=S2323
    # Eshelby tensor for spherical inclusion
    I_mat = np.eye(6)
    C_m_inv = np.linalg.inv(C_m)
    # T^p
    T_p = np.linalg.inv(I_mat + S @ C_m_inv @ (C_p - C_m))
    # interface stiffness
    C_i = stiffness_voigt_from_iso(E_i, nu_i)
    # c^p + c^i
    cp_ci = vf_p + vf_i
    # term1: S + (C_i - C_m)^-1 C_m
    try:
        C_i_minus_Cm_inv = np.linalg.inv(C_i - C_m)
    except np.linalg.LinAlgError:
        return 0.0, 0.0
    term_i = np.linalg.inv(S + C_i_minus_Cm_inv @ C_m)
    # term_p: S + (C_p - C_m)^-1 C_m
    C_p_minus_Cm_inv = np.linalg.inv(C_p - C_m)
    term_p = np.linalg.inv(S + C_p_minus_Cm_inv @ C_m)
    # T^pi
    T_pi = I_mat - S @ ( (vf_p/cp_ci)*term_p + (vf_i/cp_ci)*term_i )
    # composite stiffness
    C_comp = C_m + ( cp_ci * (C_i - C_m) @ T_pi + vf_p * (C_p - C_i) @ T_p ) @ np.linalg.inv( vf_m * I_mat + cp_ci * T_pi )
    # extract isotropic moduli
    C11 = C_comp[0,0]
    C12 = C_comp[0,1]
    G_c = C_comp[3,3]
    K_c = (C11 + 2*C12)/3
    E_c = 9*K_c*G_c/(3*K_c + G_c)
    return E_c, G_c


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
    return {"gold": spec.get("gold", {})}


# === block: score_0 (check id='step2_elastic_constants') ===
def score_0(artifact, step, ctx):
    rows = artifact
    gold_data = ctx["gold"]["systems"]
    if len(rows) != 6:
        return 0.0
    tolerance = 0.20
    correct = 0
    for row in rows:
        sys = row["system"].strip()
        if sys in gold_data:
            try:
                E = float(row["E"])
                G = float(row["G"])
            except:
                continue
            gold_E = gold_data[sys]["E"]
            gold_G = gold_data[sys]["G"]
            if abs(E - gold_E) / gold_E <= tolerance and abs(G - gold_G) / gold_G <= tolerance:
                correct += 1
    return correct / 6.0


# === block: score_1 (check id='step3_mori_tanaka_rve') ===
def score_1(artifact, step, ctx):
    rows = artifact
    gold_data = ctx["gold"]["mori_tanaka_rve"]
    if len(rows) != 4:
        return 0.0
    tolerance = 0.10
    correct = 0
    for row in rows:
        comp = row["composite"].strip()
        if comp in gold_data:
            try:
                E = float(row["E_MT"])
                G = float(row["G_MT"])
            except:
                continue
            gold_E = gold_data[comp]["E"]
            gold_G = gold_data[comp]["G"]
            if abs(E - gold_E) / gold_E <= tolerance and abs(G - gold_G) / gold_G <= tolerance:
                correct += 1
    return correct / 4.0


# === block: score_2 (check id='step4_effective_interface') ===
def score_2(artifact, step, ctx):
    rows = artifact
    gold_data = ctx["gold"]["interface"]
    if len(rows) != 4:
        return 0.0
    tolerance = 0.30
    correct = 0
    for row in rows:
        comp = row["composite_type"].strip()
        if comp in gold_data:
            try:
                E = float(row["E_interface"])
                G = float(row["G_interface"])
            except:
                continue
            gold_E = gold_data[comp]["E"]
            gold_G = gold_data[comp]["G"]
            if abs(E - gold_E) / gold_E <= tolerance and abs(G - gold_G) / gold_G <= tolerance:
                correct += 1
    return correct / 4.0


# === block: score_3 (check id='step5_moduli_vs_radius') ===
def score_3(artifact, step, ctx):
    # score width_weight
    # Extract raw data from other artifacts? We need elastic_constants and interface from previous outputs. 
    # We will load those files from /app/outputs. The checker has access to output_dir.
    # However, our scorer only receives the artifact of this step. We'll have to load the other CSVs manually.
    # We can use artifact parameter but also access the files via context or by reading from outputs_dir, but prepare does not receive path. 
    # The main checker may provide context with artifacts loaded? In the given pattern, the scorer is passed artifact and step and ctx. But ctx is the prepared data from grading_spec only. 
    # So we need to load the other CSVs from /app/outputs inside the scorer. That's fine.
    import os, csv
    output_dir = "/app/outputs"
    elastic_path = os.path.join(output_dir, "elastic_constants_systems.csv")
    interface_path = os.path.join(output_dir, "effective_interface_properties.csv")

    # load pure phase moduli
    def load_pure_moduli(path):
        data = {}
        if not os.path.exists(path):
            return data
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data[row["system"].strip()] = {"E": float(row["E"]), "G": float(row["G"])}
        return data

    def load_interface(path):
        data = {}
        if not os.path.exists(path):
            return data
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data[row["composite_type"].strip()] = {"E": float(row["E_interface"]), "G": float(row["G_interface"])}
        return data

    pure = load_pure_moduli(elastic_path)
    if "silica" not in pure or "polyimide" not in pure:
        return 0.0
    E_s = pure["silica"]["E"]
    G_s = pure["silica"]["G"]
    E_m = pure["polyimide"]["E"]
    G_m = pure["polyimide"]["G"]
    nu_m = E_m/(2*G_m)-1
    interface = load_interface(interface_path)

    rows = artifact
    composites = ["silica_composite", "hydroxylated_composite", "phenoxybenzene_composite", "functionalized_composite"]
    # separate rows by model_type
    ei_rows = [r for r in rows if r["model_type"].strip() == "Effective-Interface"]
    mt_rows = [r for r in rows if r["model_type"].strip() == "Mori-Tanaka"]

    # internal consistency: recompute EI moduli from interface properties
    score_consistency = 0.0
    if ei_rows:
        total_points = 0
        consistent_points = 0
        for r in ei_rows:
            comp = r["composite_type"].strip()
            if comp not in composites or comp not in interface:
                continue
            try:
                radius = float(r["radius_A"])
                E_sub = float(r["E"])
                G_sub = float(r["G"])
            except:
                continue
            Ei = interface[comp]["E"]
            Gi = interface[comp]["G"]
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

    # gold curve comparison
    gold_curves = ctx["gold"]["radius_curves"]
    gold_radii = gold_curves["radii_A"]
    curves_gold = gold_curves["curves"]
    tol_curve = 0.20
    score_gold = 0.0
    if ei_rows:
        matched = 0
        total = 0
        for comp in composites:
            if comp not in curves_gold:
                continue
            gdata = curves_gold[comp]
            for i, gr in enumerate(gold_radii):
                # find nearest radius in submitted rows for this composite
                comp_rows = [r for r in ei_rows if r["composite_type"].strip() == comp]
                if not comp_rows:
                    continue
                try:
                    comp_radii = [float(r["radius_A"]) for r in comp_rows]
                except:
                    continue
                # find closest
                diffs = [abs(r - gr) for r in comp_radii]
                if min(diffs) > 1.0:
                    continue
                idx = diffs.index(min(diffs))
                try:
                    E_val = float(comp_rows[idx]["E"])
                    G_val = float(comp_rows[idx]["G"])
                except:
                    continue
                gold_E = gdata["E"][i]
                gold_G = gdata["G"][i]
                if abs(E_val - gold_E) / gold_E <= tol_curve and abs(G_val - gold_G) / gold_G <= tol_curve:
                    matched += 1
                total += 1
        if total > 0:
            score_gold = matched / total

    # convergence to Mori-Tanaka at large radii
    conv_points = 0
    conv_ok = 0
    if ei_rows and mt_rows:
        # compute expected MT moduli for 5% Vf using pure phase constants
        # (same as we'd get from Mori-Tanaka model; we can compute using same function but without interface)
        # We'll compute using the Mori-Tanaka formula directly.
        # For simplicity, compare each composite's EI modulus at radius 1000 and 5000 with the MT row
        for comp in composites:
            mt_comp_rows = [r for r in mt_rows if r["composite_type"].strip() == comp]
            if not mt_comp_rows:
                continue
            try:
                mt_E = float(mt_comp_rows[0]["E"])
                mt_G = float(mt_comp_rows[0]["G"])
            except:
                continue
            # get EI rows for this comp
            ei_comp = [r for r in ei_rows if r["composite_type"].strip() == comp]
            for target_radius in [1000, 5000]:
                # find nearest
                radii = [float(r["radius_A"]) for r in ei_comp]
                diffs = [abs(r - target_radius) for r in radii]
                if min(diffs) > 500: # within 500
                    continue
                idx = diffs.index(min(diffs))
                E_val = float(ei_comp[idx]["E"])
                G_val = float(ei_comp[idx]["G"])
                if mt_E > 0:
                    if abs(E_val - mt_E) / mt_E <= 0.05 and abs(G_val - mt_G) / mt_G <= 0.05:
                        conv_ok += 1
                    conv_points += 1
    score_convergence = conv_ok / conv_points if conv_points > 0 else 0.0

    # monotonic increase check
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

    # ordering among composites at the highest radius
    ordering_score = 0.0
    if ei_rows:
        # at maximum common radius, check functionalized > silica_composite >= hydroxylated > phenoxybenzene
        # pick the largest radius common to all composites
        max_radius = 0
        radii_by_comp = {}
        for comp in composites:
            comp_rows = [r for r in ei_rows if r["composite_type"].strip() == comp]
            if not comp_rows:
                continue
            radii = [float(r["radius_A"]) for r in comp_rows]
            max_r = max(radii)
            radii_by_comp[comp] = max_r
        if len(radii_by_comp) == 4:
            # use minimum max_radius to have common
            common_r = min(radii_by_comp.values())
            vals = {}
            for comp in composites:
                comp_rows = [r for r in ei_rows if r["composite_type"].strip() == comp]
                # find row with radius closest to common_r
                radii = [float(r["radius_A"]) for r in comp_rows]
                idx = min(range(len(radii)), key=lambda i: abs(radii[i]-common_r))
                vals[comp] = {"E": float(comp_rows[idx]["E"]), "G": float(comp_rows[idx]["G"])}
            # check ordering
            ok = 0
            total = 0
            if vals["functionalized_composite"]["E"] >= vals["silica_composite"]["E"] >= vals["hydroxylated_composite"]["E"] >= vals["phenoxybenzene_composite"]["E"]:
                ok += 1
            total += 1
            if vals["functionalized_composite"]["G"] >= vals["silica_composite"]["G"] >= vals["hydroxylated_composite"]["G"] >= vals["phenoxybenzene_composite"]["G"]:
                ok += 1
            total += 1
            ordering_score = ok / total if total > 0 else 0.0

    # combine sub-scores with weights
    final_score = 0.5 * score_consistency + 0.3 * score_gold + 0.1 * score_convergence + 0.05 * score_monotonic + 0.05 * ordering_score
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
