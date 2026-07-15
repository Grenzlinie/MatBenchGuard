import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import csv

def angular_momentum_matrices(J):
    m = np.arange(J, -J-1, -1)
    Jz = np.diag(m)
    Jplus = np.diag(np.sqrt([(J-m_)*(J+m_+1) for m_ in m[:-1]]), k=1)
    Jminus = np.diag(np.sqrt([(J-m_)*(J+m_+1) for m_ in m[:-1]]), k=-1)
    return Jz, Jplus, Jminus

def stevens_operators(Jz, Jplus, Jminus, J=4):
    m = np.diag(Jz)
    O4_0 = np.diag(35 * m**4 - 575 * m**2 + 1080)
    Jplus4 = np.linalg.matrix_power(Jplus, 4)
    Jminus4 = np.linalg.matrix_power(Jminus, 4)
    O4_4 = 0.5 * (Jplus4 + Jminus4)
    O6_0 = np.diag(231 * m**6 - 5565 * m**4 + 31794 * m**2 - 25200)
    # Correct O_6^4 from Hutchings (1964): 1/4 * [(11 Jz^2 - J(J+1) - 38)(J_+^4 + J_-^4) + (J_+^4 + J_-^4)(11 Jz^2 - J(J+1) - 38)]
    Jz2 = Jz @ Jz
    I = np.eye(len(Jz))
    M = 11 * Jz2 - J*(J+1) * I - 38 * I
    O6_4 = (M @ (Jplus4 + Jminus4) + (Jplus4 + Jminus4) @ M) / 4.0
    return O4_0, O4_4, O6_0, O6_4

def build_cef(B4, B6, Jz, Jplus, Jminus):
    O4_0, O4_4, O6_0, O6_4 = stevens_operators(Jz, Jplus, Jminus)
    H = B4 * (O4_0 + 5*O4_4) + B6 * (O6_0 - 21*O6_4)
    return H

def quadrupole_operator_G3(Jx, Jy):
    return Jx @ Jx - Jy @ Jy

def quadrupole_operator_G5(Jz, Jx):
    return Jz @ Jx + Jx @ Jz

def compute_chi_site(B4, B6, O_mat, T):
    Jz, Jp, Jm = angular_momentum_matrices(4)
    H = build_cef(B4, B6, Jz, Jp, Jm)
    evals, evecs = np.linalg.eigh(H)
    O = O_mat
    O_basis = evecs.T.conj() @ O @ evecs
    d = np.real(np.diag(O_basis))
    off_diag_sq = np.abs(O_basis)**2
    np.fill_diagonal(off_diag_sq, 0)
    Z = 0.0
    p = []
    for i in range(len(evals)):
        w = np.exp(-evals[i] / T)
        Z += w
        p.append(w)
    p = np.array(p) / Z
    first = np.dot(p, d)
    second = np.dot(p, d**2)
    curie = (second - first**2) / T
    vanvleck = 0.0
    for i in range(len(evals)):
        for j in range(len(evals)):
            if i == j or abs(evals[i] - evals[j]) < 1e-12:
                continue
            vanvleck += p[i] * (off_diag_sq[i,j] + off_diag_sq[j,i]) / (evals[i] - evals[j])
    S = 2.0 * vanvleck - curie
    chi = -S
    return chi


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
    sus_path = os.path.join(outputs_dir, 'quadrupole_susceptibilities.csv')
    elas_path = os.path.join(outputs_dir, 'elastic_constants.csv')
    with open(sus_path, newline='') as f:
        sus_reader = csv.DictReader(f)
        sus_rows = []
        for row in sus_reader:
            sus_rows.append(row)
    with open(elas_path, newline='') as f:
        elas_reader = csv.DictReader(f)
        elas_rows = []
        for row in elas_reader:
            elas_rows.append(row)

    par = spec['params']
    B4_4a = par['B4_4a']
    B6_4a = par['B6_4a']
    B4_8c = par['B4_8c']
    B6_8c = par['B6_8c']

    Jz, Jp, Jm = angular_momentum_matrices(4)
    Jx = (Jp + Jm) / 2.0
    Jy = (Jp - Jm) / (2j)
    O_v = quadrupole_operator_G3(Jx, Jy)
    O_zx = quadrupole_operator_G5(Jz, Jx)

    ref_sus = []
    T_sus = []
    for row in sus_rows:
        T = float(row['temperature'])
        T_sus.append(T)
        chi3_4a = compute_chi_site(B4_4a, B6_4a, O_v, T)
        chi3_8c = compute_chi_site(B4_8c, B6_8c, O_v, T)
        chi5_4a = compute_chi_site(B4_4a, B6_4a, O_zx, T)
        chi5_8c = compute_chi_site(B4_8c, B6_8c, O_zx, T)
        ref_sus.append((chi3_4a, chi3_8c, chi5_4a, chi5_8c))

    ctx = {
        'sus_rows': sus_rows,
        'T_sus': np.array(T_sus),
        'ref_sus': ref_sus,
        'elas_rows': elas_rows,
        'par': par
    }
    return ctx


# === block: score_0 (check id='susceptibilities_check') ===
def score_0(artifact, step, ctx):
    tol = step.get('tolerance', {'atol':1e-6,'rtol':0.01})
    atol = tol['atol']
    rtol = tol['rtol']
    sus_rows = ctx['sus_rows']
    ref_sus = ctx['ref_sus']
    total = 0
    ok = 0
    for row, (r3_4a, r3_8c, r5_4a, r5_8c) in zip(sus_rows, ref_sus):
        v3_4a = float(row['chi_Gamma3_4a'])
        v3_8c = float(row['chi_Gamma3_8c'])
        v5_4a = float(row['chi_Gamma5_4a'])
        v5_8c = float(row['chi_Gamma5_8c'])
        for v, r in [(v3_4a,r3_4a),(v3_8c,r3_8c),(v5_4a,r5_4a),(v5_8c,r5_8c)]:
            total += 1
            if np.isnan(v) or np.isnan(r):
                continue
            thresh = atol + rtol * max(abs(v), abs(r))
            if abs(v - r) <= thresh:
                ok += 1
    if total == 0:
        return 0.0
    return ok / total


# === block: score_1 (check id='elastic_constants_check') ===
def score_1(artifact, step, ctx):
    tol = step.get('tolerance', {'atol':1e6,'rtol':0.005})
    atol = tol['atol']
    rtol = tol['rtol']
    par = ctx['par']
    T_sus = ctx['T_sus']
    ref_sus = ctx['ref_sus']
    N3 = par['N3']
    N23 = par['N23']
    total = 0
    ok = 0

    for row in ctx['elas_rows']:
        T = float(row['temperature'])
        # interpolate susceptibilities at T
        idx = np.searchsorted(T_sus, T)
        if idx == 0:
            r3_4a, r3_8c, r5_4a, r5_8c = ref_sus[0]
        elif idx >= len(T_sus):
            r3_4a, r3_8c, r5_4a, r5_8c = ref_sus[-1]
        else:
            T1 = T_sus[idx-1]
            T2 = T_sus[idx]
            f = (T - T1) / (T2 - T1) if T2 > T1 else 0.0
            r1 = ref_sus[idx-1]
            r2 = ref_sus[idx]
            r3_4a = r1[0] + f*(r2[0]-r1[0])
            r3_8c = r1[1] + f*(r2[1]-r1[1])
            r5_4a = r1[2] + f*(r2[2]-r1[2])
            r5_8c = r1[3] + f*(r2[3]-r1[3])
    
        # Gamma3 channel
        pr = par['Gamma3']
        C0_3 = pr['a'] + pr['b']*T + pr['c']*T*T
        term_4a = N3 * pr['g_4a']**2 * r3_4a / (1.0 - pr['gp_4a'] * r3_4a)
        term_8c = N23 * pr['g_8c']**2 * r3_8c / (1.0 - pr['gp_8c'] * r3_8c)
        C3_ref = C0_3 - term_4a - term_8c
        # Gamma5 channel
        pr5 = par['Gamma5']
        C0_5 = pr5['a'] + pr5['b']*T + pr5['c']*T*T
        term_4a5 = N3 * pr5['g_4a']**2 * r5_4a / (1.0 - pr5['gp_4a'] * r5_4a)
        term_8c5 = N23 * pr5['g_8c']**2 * r5_8c / (1.0 - pr5['gp_8c'] * r5_8c)
        C5_ref = C0_5 - term_4a5 - term_8c5
    
        C3 = float(row['C_Gamma3'])
        C5 = float(row['C_Gamma5'])
        for v, r in [(C3, C3_ref), (C5, C5_ref)]:
            total += 1
            if np.isnan(v) or np.isnan(r):
                continue
            thresh = atol + rtol * max(abs(v), abs(r))
            if abs(v - r) <= thresh:
                ok += 1
    if total == 0:
        return 0.0
    return ok / total


_SCORERS = {
    'susceptibilities_check': score_0,
    'elastic_constants_check': score_1,
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
