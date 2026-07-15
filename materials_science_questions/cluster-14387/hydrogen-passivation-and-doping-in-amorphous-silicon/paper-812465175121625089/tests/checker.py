import os
import json
import csv

# === author imports / helpers ===
import math
import random
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
    import math, random, csv

    def _coth(x):
        if abs(x) < 1e-9:
            return 1e12  # large
        e2x = math.exp(2*x)
        return (e2x + 1) / (e2x - 1)

    # constants
    hbar_eVs = 6.582119569e-16  # eV*s
    kB_eVK  = 8.617333262e-5    # eV/K
    u_kg    = 1.66053906660e-27 # kg

    masses = {
        'H': 1.00794 * u_kg,
        'D': 2.0141  * u_kg,
        'Mu': 0.1134 * u_kg
    }
    k_parallel = 18.42  # eV/A^2
    k_perp     = 3.50   # eV/A^2
    T = 50.0            # K for kinetic and angle

    # conversion factor eV/A^2 -> N/m
    J_per_eV = 1.602176634e-19
    A_to_m   = 1e-10
    N_per_eVA2 = J_per_eV / (A_to_m**2)   # = 16.021...

    def _omega(k_eVA2, m_kg):
        k_nm = k_eVA2 * N_per_eVA2     # N/m
        return math.sqrt(k_nm / m_kg)   # rad/s

    def _sigma_perp(k_eVA2, m_kg, T_K):
        omega = _omega(k_eVA2, m_kg)
        x = hbar_eVs * omega / (2 * kB_eVK * T_K)
        hbar_Js = 1.054571817e-34
        sigma2_m = (hbar_Js / (2 * m_kg * omega)) * _coth(x)
        sigma_A = math.sqrt(sigma2_m) / A_to_m
        return sigma_A

    # defect energy per impurity per temperature
    def _energy_HA(m_kg, T_K):
        k_par = k_parallel
        k_perp_local = k_perp
        om1 = _omega(k_par, m_kg)
        om2 = _omega(k_perp_local, m_kg)  # two perpendicular modes
        om3 = om2
        # zero-temperature case: return zero-point energy
        if abs(T_K) < 1e-6:
            return 0.5 * hbar_eVs * (om1 + om2 + om3)
        e = 0.0
        for om in (om1, om2, om3):
            hw = hbar_eVs * om
            e += 0.5 * hw * _coth(hw/(2*kB_eVK*T_K))
        return e

    def _kinetic_HA(m_kg, T_K):
        k_par = k_parallel
        k_perp_local = k_perp
        om1 = _omega(k_par, m_kg)
        om2 = _omega(k_perp_local, m_kg)
        om3 = om2
        K = 0.0
        for om in (om1, om2, om3):
            hw = hbar_eVs * om
            K += 0.25 * hw * _coth(hw/(2*kB_eVK*T_K))
        return K

    # expected defect energies table
    temps_C = [0, 50, 100, 200, 300, 400]
    impurities = ['H', 'D', 'Mu']
    expected_defect = {}
    for imp in impurities:
        m_kg = masses[imp]
        for Ti in temps_C:
            expected_defect[(imp, Ti)] = _energy_HA(m_kg, Ti)

    expected_kinetic = {}
    for imp in impurities:
        expected_kinetic[imp] = _kinetic_HA(masses[imp], T)

    # Reference angle pdfs via sampling
    def _compute_angle_dist(k_parallel, k_perp, d_AA, m_kg, T_K, n_samples=500000, angle_grid_step=0.5):
        sigma_A = _sigma_perp(k_perp, m_kg, T_K)
        angles = []
        half_d = d_AA / 2.0
        random.seed(42)
        for _ in range(n_samples):
            u = random.random()
            rho = sigma_A * math.sqrt(-2.0 * math.log(u))
            num = rho*rho - half_d*half_d
            den = rho*rho + half_d*half_d
            cos_val = num / den
            if cos_val < -1.0: cos_val = -1.0
            if cos_val > 1.0:  cos_val = 1.0
            theta = math.degrees(math.acos(cos_val))
            angles.append(theta)
        min_angle = 110.0
        max_angle = 180.0
        n_bins = int((max_angle - min_angle) / angle_grid_step) + 1
        bins = [min_angle + i*angle_grid_step for i in range(n_bins+1)]
        counts = [0]*n_bins
        for a in angles:
            if a < min_angle: a = min_angle
            if a > max_angle: a = max_angle
            idx = int((a - min_angle) / angle_grid_step)
            if idx >= n_bins: idx = n_bins-1
            counts[idx] += 1
        total = sum(counts)
        if total == 0: total = 1
        pdf = [c / (total * angle_grid_step) for c in counts]
        sum_weight = 0.0
        sum_weight2 = 0.0
        w_total = 0.0
        for i, c in enumerate(counts):
            mid = min_angle + (i+0.5)*angle_grid_step
            w = c
            sum_weight += mid * w
            sum_weight2 += mid*mid * w
            w_total += w
        mean = sum_weight / w_total
        var = sum_weight2 / w_total - mean*mean
        std_deg = math.sqrt(var)
        return bins[:-1], pdf, std_deg

    # HA
    angle_grid_HA, pdf_ref_HA, std_ref_HA = _compute_angle_dist(k_parallel, k_perp, 2.948, masses['Mu'], T)
    # QHA
    d_QHA = 2.899
    k_perp_QHA = 13.84 * d_QHA - 37.30  # eV/A^2
    angle_grid_QHA, pdf_ref_QHA, std_ref_QHA = _compute_angle_dist(k_parallel, k_perp_QHA, d_QHA, masses['Mu'], T)

    PIMC_std_bound = 15.0  # degrees, safe upper bound

    ctx = {
        'expected_defect': expected_defect,
        'expected_kinetic': expected_kinetic,
        'angle_grid_HA': angle_grid_HA,
        'pdf_ref_HA': pdf_ref_HA,
        'std_ref_HA': std_ref_HA,
        'angle_grid_QHA': angle_grid_QHA,
        'pdf_ref_QHA': pdf_ref_QHA,
        'std_ref_QHA': std_ref_QHA,
        'PIMC_std_bound': PIMC_std_bound
    }
    return ctx


# === block: score_0 (check id='defect_energies') ===
def score_0(artifact, step, ctx):
    import csv

    def load_csv(path):
        rows = []
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        return rows

    artifact = load_csv('/app/outputs/defect_energies.csv')
    expected = ctx['expected_defect']
    tol = step.get('tolerance_eV', 0.001)

    # count matching rows
    matched = 0
    expected_entries = 0
    for imp in ['H','D','Mu']:
        for T_val in [0,50,100,200,300,400]:
            expected_entries += 1
            key = (imp, T_val)
            val_ref = expected[key]
            found = False
            for row in artifact:
                r_imp = row.get('impurity','').strip()
                try:
                    r_T = int(float(row.get('temperature_K',-999)))
                    r_energy = float(row.get('defect_energy_HA_eV',-1e9))
                except:
                    continue
                if r_imp == imp and r_T == T_val:
                    if abs(r_energy - val_ref) <= tol:
                        matched += 1
                    found = True
                    break
            if not found:
                # count as miss
                pass
    score = matched / expected_entries
    return score


# === block: score_1 (check id='kinetic_energies') ===
def score_1(artifact, step, ctx):
    import csv
    artifact = []
    with open('/app/outputs/kinetic_energies.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            artifact.append(row)
    expected = ctx['expected_kinetic']
    tol = step.get('tolerance_eV', 0.001)
    matched = 0
    for imp in ['H','D','Mu']:
        val_ref = expected[imp]
        found = False
        for row in artifact:
            r_imp = row.get('impurity','').strip()
            try:
                r_energy = float(row.get('kinetic_energy_HA_eV',-1e9))
            except:
                continue
            if r_imp == imp:
                if abs(r_energy - val_ref) <= tol:
                    matched += 1
                found = True
                break
        if not found:
            pass
    score = matched / 3.0
    return score


# === block: score_2 (check id='angle_HA') ===
def score_2(artifact, step, ctx):
    import math
    # load agent csv
    agent_path = '/app/outputs/angle_dist_HA.csv'
    agent_rows = []
    with open(agent_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            agent_rows.append(row)
    # extract angle and pdf, sort by angle
    points = []
    for row in agent_rows:
        try:
            a = float(row.get('angle_deg', -1))
            p = float(row.get('pdf_HA', 0.0))
            points.append((a, p))
        except:
            continue
    if not points:
        return 0.0
    points.sort(key=lambda x: x[0])
    # Resample to reference grid
    ref_grid = ctx['angle_grid_HA']
    ref_pdf = ctx['pdf_ref_HA']
    agent_pdf = []
    for mid_angle in ref_grid:
        # find closest agent point
        best_p = 0.0
        for a, p in points:
            if abs(a - mid_angle) <= 0.25:  # within half step
                best_p = p
                break
        agent_pdf.append(best_p)
    # normalize agent pdf array
    sum_sq = sum(p*p for p in agent_pdf)
    ref_sum_sq = sum(p*p for p in ref_pdf)
    if sum_sq == 0 or ref_sum_sq == 0:
        return 0.0
    dot = sum(agent_pdf[i]*ref_pdf[i] for i in range(len(ref_grid)))
    cosine = dot / (math.sqrt(sum_sq) * math.sqrt(ref_sum_sq))
    # score: cosine >= 0.999 -> 1.0; linear from 0.97 to 0.999
    score = min(1.0, max(0.0, (cosine - 0.97) / 0.029))
    return score


# === block: score_3 (check id='angle_QHA') ===
def score_3(artifact, step, ctx):
    import math
    agent_path = '/app/outputs/angle_dist_QHA.csv'
    agent_rows = []
    with open(agent_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            agent_rows.append(row)
    points = []
    for row in agent_rows:
        try:
            a = float(row.get('angle_deg', -1))
            p = float(row.get('pdf_QHA', 0.0))
            points.append((a, p))
        except:
            continue
    if not points:
        return 0.0
    points.sort(key=lambda x: x[0])
    ref_grid = ctx['angle_grid_QHA']
    ref_pdf = ctx['pdf_ref_QHA']
    agent_pdf = []
    for mid_angle in ref_grid:
        best_p = 0.0
        for a, p in points:
            if abs(a - mid_angle) <= 0.25:
                best_p = p
                break
        agent_pdf.append(best_p)
    sum_sq = sum(p*p for p in agent_pdf)
    ref_sum_sq = sum(p*p for p in ref_pdf)
    if sum_sq == 0 or ref_sum_sq == 0:
        return 0.0
    dot = sum(agent_pdf[i]*ref_pdf[i] for i in range(len(ref_grid)))
    cosine = dot / (math.sqrt(sum_sq) * math.sqrt(ref_sum_sq))
    score = min(1.0, max(0.0, (cosine - 0.97) / 0.029))
    return score


# === block: score_4 (check id='angle_trend') ===
def score_4(artifact, step, ctx):
    import math
    # This scorer needs both CSVs; we'll load them from paths
    ha_path = '/app/outputs/angle_dist_HA.csv'
    qha_path = '/app/outputs/angle_dist_QHA.csv'
    def load_angle_csv(path):
        rows = []
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        points = []
        for row in rows:
            try:
                a = float(row.get('angle_deg', -1))
                if path.endswith('_HA.csv'):
                    p = float(row.get('pdf_HA', 0.0))
                else:
                    p = float(row.get('pdf_QHA', 0.0))
                points.append((a, p))
            except:
                continue
        return points

    ha_points = load_angle_csv(ha_path)
    qha_points = load_angle_csv(qha_path)
    if not ha_points or not qha_points:
        return 0.0

    def weighted_std(points):
        if not points:
            return None
        sum_w = 0.0
        sum_wx = 0.0
        sum_wx2 = 0.0
        for x, w in points:
            sum_w += w
            sum_wx += w * x
            sum_wx2 += w * x * x
        if sum_w == 0:
            return None
        mean = sum_wx / sum_w
        var = max(0.0, sum_wx2 / sum_w - mean*mean)
        return math.sqrt(var)

    std_HA = weighted_std(ha_points)
    std_QHA = weighted_std(qha_points)
    PIMC_bound = ctx['PIMC_std_bound']
    if std_HA is None or std_QHA is None:
        return 0.0
    if std_QHA > std_HA and std_QHA < PIMC_bound:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'defect_energies': score_0,
    'kinetic_energies': score_1,
    'angle_HA': score_2,
    'angle_QHA': score_3,
    'angle_trend': score_4,
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
