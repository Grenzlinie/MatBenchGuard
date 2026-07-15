import os
import json
import csv

# === author imports / helpers ===
import os, json, math
try:
    import numpy as np
except ImportError:
    class _matrix:
        __slots__ = ('data', 'shape')
        def __init__(self, data, shape):
            self.data = data
            self.shape = shape
        def __getitem__(self, idx):
            if isinstance(idx, tuple):
                return self.data[idx[0]][idx[1]]
            return self.data[idx]
        def __setitem__(self, idx, val):
            if isinstance(idx, tuple):
                self.data[idx[0]][idx[1]] = val
            else:
                self.data[idx] = val
        @staticmethod
        def zeros(shape):
            return _matrix([[0.0] * shape[1] for _ in range(shape[0])], shape)
        @staticmethod
        def inv(mat):
            n = mat.shape[0]
            A = [[float(mat[i, j]) for j in range(n)] for i in range(n)]
            M = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
            for i in range(n):
                max_row = max(range(i, n), key=lambda r: abs(M[r][i]))
                if M[max_row][i] == 0:
                    raise ZeroDivisionError('Singular matrix')
                if max_row != i:
                    M[i], M[max_row] = M[max_row], M[i]
                pivot = M[i][i]
                for j in range(2 * n):
                    M[i][j] /= pivot
                for k in range(n):
                    if k != i:
                        factor = M[k][i]
                        for j in range(2 * n):
                            M[k][j] -= factor * M[i][j]
            invA = [row[n:] for row in M]
            return _matrix(invA, (n, n))
    class _linalg:
        inv = staticmethod(_matrix.inv)
    class _np:
        zeros = staticmethod(_matrix.zeros)
        linalg = _linalg()
        @staticmethod
        def mean(x):
            if not x:
                return 0.0
            return sum(x) / len(x)
    np = _np()


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


# === block: score_0 (check id='lattice_properties') ===
def score_0(artifact, step, ctx):
    def numeric_score(agent_vals, gold, tolerances, fields, weights):
        tot, wsum = 0.0, 0.0
        for key in fields:
            w = weights.get(key, 0.0)
            if w <= 0:
                continue
            wsum += w
            if key not in gold or key not in agent_vals:
                continue
            if key == 'band_gap_type':
                if str(agent_vals[key]).strip().lower() == str(gold[key]).strip().lower():
                    tot += w
                continue
            ref = gold[key]
            val = agent_vals[key]
            if key in tolerances:
                t = tolerances[key]
            else:
                t = 0.05
            if ref == 0:
                if abs(val) < t * 1e-6:
                    tot += w
            else:
                if abs(val - ref) <= t * abs(ref):
                    tot += w
        return tot / wsum if wsum > 0 else 0.0

    data = artifact
    gold = step.get('gold', {})
    tolerances = step.get('tolerances', {})
    fields = step.get('score_fields', [])
    weights = step.get('field_weights', {})
    scores = []
    for comp in ['C2N2O', 'Si2N2O', 'Ge2N2O']:
        if comp not in data or comp not in gold:
            continue
        scores.append(numeric_score(data[comp], gold[comp], tolerances, fields, weights))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='elastic_constants') ===
def score_1(artifact, step, ctx):
    def numeric_score(agent_vals, gold, tol, fields, weights):
        tot, wsum = 0.0, 0.0
        for key in fields:
            w = weights.get(key, 0.0)
            if w <= 0:
                continue
            wsum += w
            if key not in gold or key not in agent_vals:
                continue
            ref = gold[key]
            val = agent_vals[key]
            if ref == 0:
                if abs(val) < tol * 1e-6:
                    tot += w
            else:
                if abs(val - ref) <= tol * abs(ref):
                    tot += w
        return tot / wsum if wsum > 0 else 0.0

    data = artifact
    gold = step.get('gold', {})
    tol = step.get('tolerance', 0.10)
    fields = step.get('score_fields', [])
    weights = step.get('field_weights', {})
    scores = []
    for comp in ['C2N2O', 'Si2N2O', 'Ge2N2O']:
        if comp not in data or comp not in gold:
            continue
        scores.append(numeric_score(data[comp], gold[comp], tol, fields, weights))
    if not scores:
        return 0.0
    return np.mean(scores)


# === block: score_2 (check id='mechanical_properties') ===
def score_2(artifact, step, ctx):
    def compute_mech(elas):
        C = elas
        # Compute compliance matrix S = C^{-1} for orthorhombic
        # For orthorhombic, C is 6x6 with zeros except diagonal and C12, C13, C23.
        # We'll compute S numerically.
        Cmat = np.zeros((6,6))
        idx = ['11','22','33','44','55','66','12','13','23']
        Cmat[0,0]=C['C11']
        Cmat[1,1]=C['C22']
        Cmat[2,2]=C['C33']
        Cmat[3,3]=C['C44']
        Cmat[4,4]=C['C55']
        Cmat[5,5]=C['C66']
        Cmat[0,1]=Cmat[1,0]=C['C12']
        Cmat[0,2]=Cmat[2,0]=C['C13']
        Cmat[1,2]=Cmat[2,1]=C['C23']
        Smat = np.linalg.inv(Cmat)
        S11, S22, S33 = Smat[0,0], Smat[1,1], Smat[2,2]
        S12, S13, S23 = Smat[0,1], Smat[0,2], Smat[1,2]
        S44, S55, S66 = Smat[3,3], Smat[4,4], Smat[5,5]
        # Voigt bulk
        BV = (C['C11']+C['C22']+C['C33']+2*(C['C12']+C['C13']+C['C23']))/9.0
        # Voigt shear
        GV = (C['C11']+C['C22']+C['C33']-(C['C12']+C['C13']+C['C23'])+3*(C['C44']+C['C55']+C['C66']))/15.0
        # Reuss bulk
        BR = 1.0/(S11+S22+S33+2*(S12+S13+S23))
        # Reuss shear
        GR = 15.0/(4*(S11+S22+S33)-4*(S12+S13+S23)+3*(S44+S55+S66))
        BH = (BV+BR)/2.0
        GH = (GV+GR)/2.0
        E = 9*BH*GH/(3*BH+GH)
        v = (3*BH-2*GH)/(2*(3*BH+GH))
        BG_ratio = BH/GH
        A_U = 5*GV/GR + BV/BR - 6
        A_B = (BV-BR)/(BV+BR)*100
        A_G = (GV-GR)/(GV+GR)*100
        A1 = 4*C['C44']/(C['C11']+C['C33']-2*C['C13'])
        A2 = 4*C['C55']/(C['C22']+C['C33']-2*C['C23'])
        A3 = 4*C['C66']/(C['C11']+C['C22']-2*C['C12'])
        k_a = S11+S12+S13
        k_b = S12+S22+S23
        k_c = S13+S23+S33
        return {'B':BH, 'G':GH, 'E':E, 'v':v, 'BG_ratio':BG_ratio,
                'A_U':A_U, 'A_B':A_B, 'A_G':A_G, 'A1':A1, 'A2':A2, 'A3':A3,
                'k_a':k_a, 'k_b':k_b, 'k_c':k_c}

    props_key = 'mechanical_properties'
    outputs_dir = ctx.get('outputs_dir', '/app/outputs')
    elas_path = os.path.join(outputs_dir, 'elastic_constants.json')
    if not os.path.exists(elas_path):
        return 0.0
    with open(elas_path) as f:
        elas_data = json.load(f)
    gold = step.get('gold', {})
    tol = step.get('tolerance', 0.10)
    scores = []
    for comp in ['C2N2O', 'Si2N2O', 'Ge2N2O']:
        if comp not in elas_data or comp not in gold:
            continue
        elas = elas_data[comp]
        recomputed = compute_mech(elas)
        ref = gold[comp]
        # All fields are directional (absolute diff relative to gold is fine)
        field_score = 0.0
        nf = 0
        for fld in ['B','G','E','v','BG_ratio','A_U','A_B','A_G','A1','A2','A3','k_a','k_b','k_c']:
            if fld not in recomputed or fld not in ref:
                continue
            rv = recomputed[fld]
            gv = ref[fld]
            if gv == 0:
                if abs(rv) <= tol:
                    field_score += 1.0
            else:
                if abs(rv - gv) <= tol * abs(gv):
                    field_score += 1.0
            nf += 1
        if nf > 0:
            scores.append(field_score / nf)
    if not scores:
        return 0.0
    return np.mean(scores)


# === block: score_3 (check id='vickers_hardness') ===
def score_3(artifact, step, ctx):
    def compute_hardness(bonds_data, cell_volume, shear_modulus):
        # bonds_data: list of dicts with bond_length, overlap_population, number_of_bonds
        # compute denominator sum_v (d^3 * N^v)
        sum_d3N = 0.0
        for b in bonds_data:
            d = b['bond_length']
            N = b['number_of_bonds']
            sum_d3N += (d**3) * N
        if sum_d3N == 0:
            return None, None
        bond_hardnesses = []
        for b in bonds_data:
            d = b['bond_length']
            P = b['overlap_population']
            if P <= 0:
                continue
            vb = cell_volume * (d**3) / sum_d3N
            H_mu = 740 * P * (vb ** (-5.0/3.0))
            bond_hardnesses.append((H_mu, b['number_of_bonds']))
        if not bond_hardnesses:
            return None, None
        # geometric average: product(H_mu ^ N_mu) ** (1/total_N)
        log_H = 0.0
        total_N = 0
        for H_mu, N in bond_hardnesses:
            log_H += math.log(H_mu) * N
            total_N += N
        H_v_gao = math.exp(log_H / total_N)
        H_v_jiang = shear_modulus / 6.78 if shear_modulus is not None else None
        return H_v_gao, H_v_jiang

    outputs_dir = ctx.get('outputs_dir', '/app/outputs')
    kpath = os.path.join(outputs_dir, 'vickers_hardness.json')
    elas_path = os.path.join(outputs_dir, 'elastic_constants.json')
    latt_path = os.path.join(outputs_dir, 'lattice_properties.json')
    if not os.path.exists(kpath) or not os.path.exists(elas_path) or not os.path.exists(latt_path):
        return 0.0
    with open(kpath) as f:
        vickers_data = json.load(f)
    with open(elas_path) as f:
        elas_data = json.load(f)
    with open(latt_path) as f:
        latt_data = json.load(f)

    # Compute mechanical properties to get G (shear modulus) from elastic constants
    # reuse compute_mech from mechanical properties; we'll define it here inline or import from earlier? 
    # Since scorer bodies are independent, we need to replicate the helper.
    def compute_mech_for_G(elas):
        C = elas
        Cmat = np.zeros((6,6))
        Cmat[0,0]=C['C11']; Cmat[1,1]=C['C22']; Cmat[2,2]=C['C33']
        Cmat[3,3]=C['C44']; Cmat[4,4]=C['C55']; Cmat[5,5]=C['C66']
        Cmat[0,1]=Cmat[1,0]=C['C12']; Cmat[0,2]=Cmat[2,0]=C['C13']; Cmat[1,2]=Cmat[2,1]=C['C23']
        Smat = np.linalg.inv(Cmat)
        S11, S22, S33 = Smat[0,0], Smat[1,1], Smat[2,2]
        S12, S13, S23 = Smat[0,1], Smat[0,2], Smat[1,2]
        S44, S55, S66 = Smat[3,3], Smat[4,4], Smat[5,5]
        GV = (C['C11']+C['C22']+C['C33']-(C['C12']+C['C13']+C['C23'])+3*(C['C44']+C['C55']+C['C66']))/15.0
        GR = 15.0/(4*(S11+S22+S33)-4*(S12+S13+S23)+3*(S44+S55+S66))
        GH = (GV+GR)/2.0
        return GH

    gold = step.get('gold', {})
    tolerances = step.get('tolerances', {})
    scores = []
    for comp in ['C2N2O', 'Si2N2O', 'Ge2N2O']:
        if comp not in vickers_data or comp not in latt_data or comp not in elas_data or comp not in gold:
            continue
        bonds = vickers_data[comp].get('bonds', [])
        cell_volume = latt_data[comp].get('cell_volume')
        elas = elas_data[comp]
        shear_modulus = compute_mech_for_G(elas)
        H_gao, H_jiang = compute_hardness(bonds, cell_volume, shear_modulus)
        if H_gao is None:
            continue
        ref = gold[comp]
        tol_gao = tolerances.get('H_v_Gao', 0.05)
        tol_jiang = tolerances.get('H_v_Jiang', 0.10)
        score_gao = 1.0 if abs(H_gao - ref['H_v_Gao']) <= tol_gao * abs(ref['H_v_Gao']) else 0.0
        if H_jiang is not None and ref.get('H_v_Jiang') is not None:
            score_jiang = 1.0 if abs(H_jiang - ref['H_v_Jiang']) <= tol_jiang * abs(ref['H_v_Jiang']) else 0.0
        else:
            score_jiang = 1.0  # treat missing as ok
        scores.append(0.8*score_gao + 0.2*score_jiang)
    if not scores:
        return 0.0
    return np.mean(scores)


# === block: score_4 (check id='thermal_properties') ===
def score_4(artifact, step, ctx):
    outputs_dir = ctx.get('outputs_dir', '/app/outputs')
    elas_path = os.path.join(outputs_dir, 'elastic_constants.json')
    latt_path = os.path.join(outputs_dir, 'lattice_properties.json')
    if not os.path.exists(elas_path) or not os.path.exists(latt_path):
        return 0.0
    with open(elas_path) as f:
        elas_data = json.load(f)
    with open(latt_path) as f:
        latt_data = json.load(f)
    gold = step.get('gold', {})
    tolerances = step.get('tolerances', {})
    atomic_masses = {'C':12.011, 'Si':28.085, 'Ge':72.64, 'N':14.007, 'O':15.999}
    A_map = {'C2N2O':'C', 'Si2N2O':'Si', 'Ge2N2O':'Ge'}
    scores = []
    for comp in ['C2N2O', 'Si2N2O', 'Ge2N2O']:
        if comp not in elas_data or comp not in latt_data or comp not in gold:
            continue
        elas = elas_data[comp]
        latt = latt_data[comp]
        A_el = A_map[comp]
        m_fu = 2*atomic_masses[A_el] + 2*atomic_masses['N'] + atomic_masses['O']
        NA = 6.02214076e23
        V = latt['cell_volume']
        m_fu_kg = (m_fu / NA) * 1e-3
        V_m3 = V * 1e-30
        rho = m_fu_kg / V_m3
        C = elas
        Cmat = np.zeros((6,6))
        Cmat[0,0]=C['C11']; Cmat[1,1]=C['C22']; Cmat[2,2]=C['C33']
        Cmat[3,3]=C['C44']; Cmat[4,4]=C['C55']; Cmat[5,5]=C['C66']
        Cmat[0,1]=Cmat[1,0]=C['C12']; Cmat[0,2]=Cmat[2,0]=C['C13']; Cmat[1,2]=Cmat[2,1]=C['C23']
        Smat = np.linalg.inv(Cmat)
        S11, S22, S33 = Smat[0,0], Smat[1,1], Smat[2,2]
        S12, S13, S23 = Smat[0,1], Smat[0,2], Smat[1,2]
        S44, S55, S66 = Smat[3,3], Smat[4,4], Smat[5,5]
        BV = (C['C11']+C['C22']+C['C33']+2*(C['C12']+C['C13']+C['C23']))/9.0
        GV = (C['C11']+C['C22']+C['C33']-(C['C12']+C['C13']+C['C23'])+3*(C['C44']+C['C55']+C['C66']))/15.0
        BR = 1.0/(S11+S22+S33+2*(S12+S13+S23))
        GR = 15.0/(4*(S11+S22+S33)-4*(S12+S13+S23)+3*(S44+S55+S66))
        BH = (BV+BR)/2.0
        GH = (GV+GR)/2.0
        B_Pa = BH * 1e9
        G_Pa = GH * 1e9
        vl = math.sqrt((B_Pa + 4.0/3.0*G_Pa) / rho)
        vt = math.sqrt(G_Pa / rho)
        vm = (1.0/3.0 * (2.0/vt**3 + 1.0/vl**3)) ** (-1.0/3.0)
        k_B = 1.380649e-23
        h = 6.62607015e-34
        n = 5
        M = m_fu * 1e-3
        factor = (3*n/(4*math.pi) * (NA*rho/M)) ** (1.0/3.0)
        theta_D = h/k_B * factor * vm
        E = 9*BH*GH/(3*BH+GH) * 1e9
        p = n / V_m3
        M_a = M / (n * NA)
        k_min_clarke = 0.87 * k_B * (M_a ** (-2.0/3.0)) * (E ** 0.5) * (p ** (1.0/6.0))
        k_min_cahill = (k_B / 2.48) * (p ** (2.0/3.0)) * (vl + 2*vt)
        recomputed = {
            'longitudinal_velocity': vl,
            'transverse_velocity': vt,
            'mean_velocity': vm,
            'Debye_temperature': theta_D,
            'k_min_Clarke': k_min_clarke,
            'k_min_Cahill': k_min_cahill
        }
        ref = gold[comp]
        field_score = 0.0
        nf = 0
        for fld in ['longitudinal_velocity','transverse_velocity','mean_velocity','Debye_temperature','k_min_Clarke','k_min_Cahill']:
            rv = recomputed.get(fld)
            gv = ref.get(fld)
            if rv is None or gv is None:
                continue
            tol = tolerances.get(fld, 0.10)
            if gv == 0:
                if abs(rv) <= tol:
                    field_score += 1.0
            else:
                if abs(rv - gv) <= tol * abs(gv):
                    field_score += 1.0
            nf += 1
        if nf > 0:
            scores.append(field_score / nf)
    if not scores:
        return 0.0
    return np.mean(scores)


_SCORERS = {
    'lattice_properties': score_0,
    'elastic_constants': score_1,
    'mechanical_properties': score_2,
    'vickers_hardness': score_3,
    'thermal_properties': score_4,
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
