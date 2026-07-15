import os
import json
import csv

# === author imports / helpers ===
import math

# Material constants
L0 = 2.45e-8
k_te = 1.90
rho_te = 0.85e-5
M0 = k_te * rho_te
eta = 0.19e-3
Cp = 1.04
CL = 199
u = Cp / CL
Tc = 77.0
Tr = 300.0

beta0 = math.sqrt(L0)

def compute_residual_PCL_f0(Z1, Z2, Tj):
    sin_bz1 = math.sin(beta0 * Z1)
    if abs(sin_bz1) < 1e-12:
        return 1e9
    cot_bz1 = math.cos(beta0 * Z1) / sin_bz1
    denominator = eta + beta0 * cot_bz1
    if abs(denominator) < 1e-12:
        return 1e9
    expected_Tj = (M0 * Z2 + Tc * beta0 / sin_bz1) / denominator
    resid1 = abs(Tj - expected_Tj)
    Tj_from_Z2 = Tr - 0.5 * M0 * Z2 * Z2
    resid2 = abs(Tj - Tj_from_Z2)
    return max(resid1, resid2)

def compute_residual_PCL_f_nonzero(Z1, Z2, Tj, f, q):
    alpha = f * q * u / 2.0
    if L0 - alpha * alpha < 0:
        return 1e9
    beta = math.sqrt(L0 - alpha * alpha)
    if beta < 1e-12:
        return 1e9
    sin_bz1 = math.sin(beta * Z1)
    if abs(sin_bz1) < 1e-12:
        return 1e9
    cot_bz1 = math.cos(beta * Z1) / sin_bz1
    exp_term = math.exp(alpha * Z1)
    # LHS of (21b) = Tr - (M0/(2α)) Z2 + (M0/(4α²)) (1 - e^{-2α Z2})
    if abs(alpha) < 1e-12:
        return 1e9
    two_alpha = 2 * alpha
    four_alpha2 = 4 * alpha * alpha
    lhs = Tr - (M0 / two_alpha) * Z2 + (M0 / four_alpha2) * (1 - math.exp(-two_alpha * Z2))
    # RHS of (21b)
    rhs_num = (M0 / two_alpha) * (1 - math.exp(-two_alpha * Z2)) + Tc * beta * exp_term / sin_bz1
    rhs_den = alpha + eta + beta * cot_bz1
    if abs(rhs_den) < 1e-12:
        return 1e9
    rhs = rhs_num / rhs_den
    resid = abs(lhs - rhs)
    # additionally Tj should equal lhs
    resid2 = abs(Tj - lhs)
    return max(resid, resid2)

def check_Cu_f0(Z1):
    return abs(math.cos(beta0 * Z1) - Tc / Tr)

def compute_residual_Cu_f_nonzero(Z1, q, f):
    alpha = f * q * u / 2.0
    if L0 - alpha * alpha < 0:
        return 1e9
    beta = math.sqrt(L0 - alpha * alpha)
    if beta < 1e-12:
        return 1e9
    sin_bz1 = math.sin(beta * Z1)
    if abs(sin_bz1) < 1e-12:
        return 1e9
    cot_bz1 = math.cos(beta * Z1) / sin_bz1
    exp_term = math.exp(alpha * Z1)
    lhs = Tr * (alpha + beta * cot_bz1)
    rhs = Tc * beta * exp_term / sin_bz1
    return abs(lhs - rhs)

def temp_Cu_general(z, Z1, Tc, T_j, alpha, beta):
    if abs(beta) < 1e-12:
        return None
    sin_bz1 = math.sin(beta * Z1)
    exp_Z1 = math.exp(alpha * Z1)
    cot_bz1 = math.cos(beta * Z1) / sin_bz1
    expz = math.exp(alpha * z)
    term1 = T_j * expz * math.sin(beta * z) / (exp_Z1 * sin_bz1)
    term2 = Tc * expz * (math.cos(beta * z) - math.sin(beta * z) * cot_bz1)
    return term1 + term2

def temp_Cu_f0(z, Z1, Tc, T_j):
    return temp_Cu_general(z, Z1, Tc, T_j, alpha=0.0, beta=beta0)

def temp_TE_f0(z, Z2, Tr, M0):
    # Eq (18)
    return Tr - 0.5 * M0 * (z - Z2) * (z - Z2)

def temp_TE_f_nonzero(z, Z2, Tr, M0, alpha):
    # Eq (15)
    diff = z - Z2
    two_alpha = 2 * alpha
    four_alpha2 = 4 * alpha * alpha
    if abs(alpha) < 1e-12:
        return temp_TE_f0(z, Z2, Tr, M0)
    return Tr + (M0 / two_alpha) * diff + (M0 / four_alpha2) * (1 - math.exp(two_alpha * diff))


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
    import csv, os

    def load_csv(path):
        with open(path, newline='') as f:
            return list(csv.DictReader(f))

    optimal_rows = load_csv(os.path.join(outputs_dir, 'optimal_parameters.csv'))
    optimal_dict = {}
    for row in optimal_rows:
        f_val = str(row.get('f', '')).strip()
        try:
            float(f_val)
        except ValueError:
            continue
        optimal_dict[f_val] = row

    profiles_rows = []
    prof_path = os.path.join(outputs_dir, 'temperature_profiles.csv')
    if os.path.exists(prof_path):
        profiles_rows = load_csv(prof_path)

    return {'optimal_dict': optimal_dict, 'profiles_rows': profiles_rows}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    optimal_dict = ctx.get('optimal_dict', {})
    gold = step.get('gold', {})
    tol = step.get('tolerances', {})
    rows = artifact
    row_by_f = {}
    for r in rows:
        f_val = str(r.get('f', '')).strip()
        try:
            float(f_val)
        except:
            continue
        row_by_f[f_val] = r

    total = 0.0
    n = 0
    for f_str, g in gold.items():
        row = row_by_f.get(f_str)
        if not row:
            continue
        n += 1
        try:
            qp = float(row['q_PCL'])
            qc = float(row['q_Cu'])
            z1p = float(row['Z1_PCL'])
            z2p = float(row['Z2_PCL'])
            tjp = float(row['Tj_PCL'])
            trep = float(row['t'])
            z1c = float(row['Z1_Cu'])
            qc_for_z = float(row['q_Cu'])
            pn_p = float(row['p_net_PCL'])
            pt_p = float(row['p_tot_PCL'])
            pn_c = float(row['p_net_Cu'])
            pt_c = float(row['p_tot_Cu'])
        except (KeyError, ValueError):
            continue

        s_qp = 1.0 if abs(qp - g['q_PCL']) / g['q_PCL'] <= tol.get('q_PCL_rel', 0.01) else 0.0
        s_qc = 1.0 if abs(qc - g['q_Cu']) / g['q_Cu'] <= tol.get('q_Cu_rel', 0.01) else 0.0
        s_z1p = 1.0 if abs(z1p - g['Z1_PCL']) / g['Z1_PCL'] <= tol.get('Z1_PCL_rel', 0.02) else 0.0
        s_z2p = 1.0 if abs(z2p - g['Z2_PCL']) / g['Z2_PCL'] <= tol.get('Z2_PCL_rel', 0.02) else 0.0
        s_tj = 1.0 if abs(tjp - g['Tj_PCL']) <= tol.get('Tj_PCL_abs', 0.5) else 0.0
    
        computed_t = 100.0 * (qc - qp) / qc if qc != 0 else 0.0
        s_tt = 1.0 if abs(computed_t - trep) <= tol.get('t_abs', 0.1) else 0.0

        s_pn_p = 1.0 if abs(pn_p - g['p_net_PCL']) / g['p_net_PCL'] <= tol.get('p_net_PCL_rel', 0.02) else 0.0
        s_pt_p = 1.0 if abs(pt_p - g['p_tot_PCL']) / g['p_tot_PCL'] <= tol.get('p_tot_PCL_rel', 0.02) else 0.0
        s_pn_c = 1.0 if abs(pn_c - g['p_net_Cu']) / g['p_net_Cu'] <= tol.get('p_net_Cu_rel', 0.02) else 0.0
        s_pt_c = 1.0 if abs(pt_c - g['p_tot_Cu']) / g['p_tot_Cu'] <= tol.get('p_tot_Cu_rel', 0.02) else 0.0

        f_val = float(f_str)
        if f_val == 0.0:
            resid_pcl = compute_residual_PCL_f0(z1p, z2p, tjp)
            resid_cu = check_Cu_f0(z1c)
        else:
            resid_pcl = compute_residual_PCL_f_nonzero(z1p, z2p, tjp, f_val, qp)
            resid_cu = compute_residual_Cu_f_nonzero(z1c, qc_for_z, f_val)
    
        constraint_ok = (abs(resid_pcl) <= tol.get('constraint_residual_abs', 1e-4) and
                         abs(resid_cu) <= tol.get('constraint_residual_abs', 1e-4))
        s_con = 1.0 if constraint_ok else 0.0

        checks = [s_qp, s_qc, s_z1p, s_z2p, s_tj, s_tt, s_con, s_pn_p, s_pt_p, s_pn_c, s_pt_c]
        row_score = sum(checks) / len(checks)
        total += row_score

    if n == 0:
        return 0.0
    return total / n


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    optimal_dict = ctx.get('optimal_dict', {})
    profiles = artifact
    if not profiles:
        return 0.0

    profiles_by_key = {}
    for p in profiles:
        f_val = str(p.get('f', '')).strip()
        lt = str(p.get('lead_type', '')).strip()
        key = (f_val, lt)
        if key not in profiles_by_key:
            profiles_by_key[key] = []
        profiles_by_key[key].append(p)

    TEMP_TOL = step.get('temperature_tolerance_K', 1.0)
    INT_TOL = step.get('interface_tolerance_K', 0.5)

    profile_scores = []

    for (f_str, lt), points in profiles_by_key.items():
        f_val = float(f_str)
        if f_val not in [0.0, 1.0]:
            continue
        if lt not in ['PCL', 'Cu']:
            continue
        if len(points) == 0:
            continue

        # get optima
        if lt == 'PCL':
            opt = optimal_dict.get(f_str)
            if not opt:
                continue
            try:
                Z1_opt = float(opt['Z1_PCL'])
                Z2_opt = float(opt['Z2_PCL'])
                Tj_opt = float(opt['Tj_PCL'])
            except (KeyError, ValueError):
                continue
        else:  # Cu
            opt = optimal_dict.get(f_str)
            if not opt:
                continue
            try:
                Z1_opt = float(opt['Z1_Cu'])
            except (KeyError, ValueError):
                continue
            Z2_opt = 0.0
            Tj_opt = Tr   # hot end of Cu lead is room temp

        # guard against invalid alpha (q too large)
        alpha_valid = True
        if f_val != 0.0:
            qval = float(opt.get('q_PCL' if lt == 'PCL' else 'q_Cu', 0.0))
            alpha_temp = f_val * qval * u / 2.0
            if L0 - alpha_temp * alpha_temp <= 0:
                alpha_valid = False
        if not alpha_valid:
            # invalid q -> profile cannot be recomputed; skip with score 0
            profile_scores.append(0.0)
            continue

        # sort by normalized_position
        points.sort(key=lambda x: float(x.get('normalized_position', 0.0)))

        # compute expected temperatures
        temps_expected = []
        temps_reported = []
        for pt in points:
            try:
                np = float(pt['normalized_position'])
                t = float(pt['temperature_K'])
            except (KeyError, ValueError):
                continue
            if lt == 'PCL':
                if np <= 0.0:
                    # Cu segment, z from 0 to Z1, mapped: np from -1 to 0 -> z = (np+1)*Z1_opt
                    z = (np + 1.0) * Z1_opt
                    if f_val == 0.0:
                        Te = temp_Cu_f0(z, Z1_opt, Tc, Tj_opt)
                    else:
                        alpha = f_val * float(opt.get('q_PCL', 0.0)) * u / 2.0
                        beta = math.sqrt(L0 - alpha*alpha)
                        Te = temp_Cu_general(z, Z1_opt, Tc, Tj_opt, alpha, beta)
                else:
                    # TE segment, z from 0 to Z2, np from 0 to 1 -> z = np * Z2_opt
                    z = np * Z2_opt
                    if f_val == 0.0:
                        Te = temp_TE_f0(z, Z2_opt, Tr, M0)
                    else:
                        alpha = f_val * float(opt.get('q_PCL', 0.0)) * u / 2.0
                        Te = temp_TE_f_nonzero(z, Z2_opt, Tr, M0, alpha)
            else:  # all-Cu
                # only Cu segment, np -1 to 0 mapping as above
                z = (np + 1.0) * Z1_opt
                if f_val == 0.0:
                    Te = temp_Cu_f0(z, Z1_opt, Tc, Tr)
                else:
                    alpha = f_val * float(opt.get('q_Cu', 0.0)) * u / 2.0
                    beta = math.sqrt(L0 - alpha*alpha)
                    Te = temp_Cu_general(z, Z1_opt, Tc, Tr, alpha, beta)

            temps_expected.append(Te)
            temps_reported.append(t)

        if not temps_expected:
            continue

        # pointwise score
        ok_points = sum(1 for te, tr in zip(temps_expected, temps_reported) if abs(te - tr) <= TEMP_TOL)
        point_score = ok_points / len(temps_expected)

        # interface check
        interface_ok = True
        if lt == 'PCL':
            # find point with np ≈ 0
            iface_pt = next((p for p in points if abs(float(p.get('normalized_position', 0.0)) - 0.0) < 1e-4), None)
            if iface_pt:
                T_iface = float(iface_pt['temperature_K'])
                if abs(T_iface - Tj_opt) > INT_TOL:
                    interface_ok = False
            else:
                interface_ok = False
        else:  # all-Cu
            # hot end at np=0 should be Tr
            iface_pt = next((p for p in points if abs(float(p.get('normalized_position', 0.0)) - 0.0) < 1e-4), None)
            if iface_pt:
                T_iface = float(iface_pt['temperature_K'])
                if abs(T_iface - Tr) > INT_TOL:
                    interface_ok = False
            else:
                interface_ok = False
            # cold end at np=-1 should be Tc
            cold_pt = next((p for p in points if abs(float(p.get('normalized_position', 0.0)) - (-1.0)) < 1e-4), None)
            if cold_pt:
                T_cold = float(cold_pt['temperature_K'])
                if abs(T_cold - Tc) > INT_TOL:
                    interface_ok = False

        # monotonicity (increasing with increasing normalized_position)
        monotonic = True
        for i in range(len(temps_reported) - 1):
            if temps_reported[i+1] < temps_reported[i] - 1e-6:
                monotonic = False
                break

        # combine
        pen_interface = 1.0 if interface_ok else 0.5
        pen_mono = 1.0 if monotonic else 0.7
        profile_score = point_score * pen_interface * pen_mono
        profile_scores.append(profile_score)

    if not profile_scores:
        return 0.0
    return sum(profile_scores) / len(profile_scores)


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
