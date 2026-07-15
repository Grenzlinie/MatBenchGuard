import os
import json
import csv

# === author imports / helpers ===
import os, json, sys
import numpy as np
from scipy.linalg import eigh

# Physical constants
gJ = 7.0/6.0
muB = 9.274009e-21          # emu
kB = 1.380649e-16           # erg/K
NA = 6.02214076e23           # mol^-1

J_ = 6
M = np.arange(J_, -J_-1, -1)
Jz_mat = np.diag(M)
Jp = np.diag([np.sqrt(J_*(J_+1)-m*(m+1)) for m in M[:-1]], k=-1)
Jm = Jp.T
Jx = 0.5*(Jp+Jm)
Jy = -0.5j*(Jp-Jm)

O20 = 3*np.diag(M**2) - J_*(J_+1)*np.eye(2*J_+1)
O40 = 35*np.diag(M**4) - 30*J_*(J_+1)*np.diag(M**2) + 25*np.diag(M**2) - 6*J_*(J_+1)*np.eye(2*J_+1) + 3*J_**2*(J_+1)**2*np.eye(2*J_+1)
Jp2, Jp4 = Jp@Jp, Jp@Jp@Jp@Jp
Jm2, Jm4 = Jm@Jm, Jm@Jm@Jm@Jm
O44 = 0.5*(Jp4+Jm4)

O60 = (231*np.diag(M**6) - 315*J_*(J_+1)*np.diag(M**4) + 735*np.diag(M**4)
       + 105*J_**2*(J_+1)**2*np.diag(M**2) - 525*J_*(J_+1)*np.diag(M**2) + 294*np.diag(M**2)
       - 5*J_**3*(J_+1)**3*np.eye(2*J_+1) + 40*J_**2*(J_+1)**2*np.eye(2*J_+1)
       - 60*J_*(J_+1)*np.eye(2*J_+1))
O64 = 0.25 * ((11*np.diag(M**2) - J_*(J_+1)*np.eye(2*J_+1) - 38*np.eye(2*J_+1)) @ (Jp4+Jm4))

F4, F6 = 60.0, 13860.0

def build_H_CEF(W, x):
    O4 = O40 + 5*O44
    O6 = O60 - 21*O64
    return W * (x*O4/F4 + (1-abs(x))*O6/F6)

def build_H_111(W, x):
    from scipy.spatial.transform import Rotation
    v_src, v_dst = np.array([0,0,1]), np.array([1,1,1])/np.sqrt(3)
    R = Rotation.align_vectors([v_dst], [v_src])[0].as_matrix()
    Jx_p = R[0,0]*Jx + R[0,1]*Jy + R[0,2]*Jz_mat
    Jy_p = R[1,0]*Jx + R[1,1]*Jy + R[1,2]*Jz_mat
    Jz_p = R[2,0]*Jx + R[2,1]*Jy + R[2,2]*Jz_mat
    O20p = 3*(Jz_p@Jz_p) - J_*(J_+1)*np.eye(2*J_+1)
    Jz2 = Jz_p@Jz_p; Jz4 = Jz2@Jz2
    O40p = 35*Jz4 - 30*J_*(J_+1)*Jz2 + 25*Jz2 - 6*J_*(J_+1)*np.eye(2*J_+1) + 3*J_**2*(J_+1)**2*np.eye(2*J_+1)
    Jpp = Jx_p + 1j*Jy_p; Jpm = Jx_p - 1j*Jy_p
    Jpp4 = Jpp@Jpp@Jpp@Jpp; Jpm4 = Jpm@Jpm@Jpm@Jpm
    O44p = 0.5*(Jpp4+Jpm4)
    Jz6 = Jz4@Jz2
    O60p = (231*Jz6 - 315*J_*(J_+1)*Jz4 + 735*Jz4 + 105*J_**2*(J_+1)**2*Jz2
            - 525*J_*(J_+1)*Jz2 + 294*Jz2 - 5*J_**3*(J_+1)**3*np.eye(2*J_+1)
            + 40*J_**2*(J_+1)**2*np.eye(2*J_+1) - 60*J_*(J_+1)*np.eye(2*J_+1))
    O64p = 0.25 * ((11*Jz2 - J_*(J_+1)*np.eye(2*J_+1) - 38*np.eye(2*J_+1)) @ (Jpp4+Jpm4))
    O4p = O40p + 5*O44p
    O6p = O60p - 21*O64p
    Hp = W * (x*O4p/F4 + (1-abs(x))*O6p/F6)
    return Hp, Jz_p, O20p

def _chi0_CEF(evals, evecs, J_op, Q_op, T):
    d = len(evals)
    J_basis = evecs.conj().T @ J_op @ evecs
    Q_basis = evecs.conj().T @ Q_op @ evecs
    J2 = np.abs(J_basis)**2
    Q2 = np.abs(Q_basis)**2
    J_diag = np.real(np.diag(J_basis))
    Q_diag = np.real(np.diag(Q_basis))
    beta = 1.0/T
    Z = np.sum(np.exp(-evals/T))
    f = np.exp(-evals/T)/Z
    # chi0^(1)
    s1 = 0.0
    for i in range(d):
        term = -2*sum(J2[i,j]/(evals[i]-evals[j]) for j in range(d) if j!=i) + beta*J_diag[i]**2
        s1 += f[i]*term
    chi01 = s1 * gJ**2 * muB**2 * NA
    # chi2
    s2 = 0.0
    for i in range(d):
        term = -2*sum(Q2[i,j]/(evals[i]-evals[j]) for j in range(d) if j!=i) + beta*Q_diag[i]**2
        s2 += f[i]*term
    # chi2^(2)
    s22 = 0.0
    for i in range(d):
        fi = f[i]
        t1 = 0.0
        for j in range(d):
            if j==i: continue
            denom_ij = evals[i]-evals[j]
            for jp in range(d):
                if jp==i: continue
                denom_ijp = evals[i]-evals[jp]
                t1 += (J_basis[i,j]*Q_basis[j,jp]*J_basis[jp,i] + 2*Q_basis[i,j]*J_basis[j,jp]*J_basis[jp,i]) / (denom_ij*denom_ijp)
        t2 = 0.0
        for j in range(d):
            if j==i: continue
            denom = evals[i]-evals[j]
            t2 += -(J2[i,j]*Q_diag[i] + 2*Q_basis[i,j]*J_basis[j,i]*J_diag[i]) / denom * (1/denom + beta)
        t3 = 0.5*beta**2 * J_diag[i]**2 * Q_diag[i]
        s22 += fi*(t1 + t2 + t3)
    chi22 = s22 * gJ**2 * muB**2 * NA
    # chi0^(3)
    s3 = -0.5*beta * chi01**2
    extra = 0.0
    for i in range(d):
        fi = f[i]
        s4 = 0.0
        for j in range(d):
            if j==i: continue
            denom_ij = evals[i]-evals[j]
            for jp in range(d):
                if jp==i: continue
                denom_ijp = evals[i]-evals[jp]
                for jpp in range(d):
                    if jpp==i: continue
                    denom_ijpp = evals[i]-evals[jpp]
                    s4 += -4 * J_basis[i,j]*J_basis[j,jp]*J_basis[jp,jpp]*J_basis[jpp,i] / (denom_ij*denom_ijp*denom_ijpp)
        for j in range(d):
            if j==i: continue
            denom_ij = evals[i]-evals[j]
            for jp in range(d):
                if jp==i: continue
                denom_ijp = evals[i]-evals[jp]
                s4 += 2*(J2[i,j]*J2[i,jp] + 2*J_basis[i,j]*J_basis[j,jp]*J_basis[jp,i]*J_diag[i])/(denom_ij*denom_ijp) * (2/denom_ij + beta)
        for j in range(d):
            if j==i: continue
            denom = evals[i]-evals[j]
            s4 += -2 * J_diag[i]**2 * J2[i,j] / denom * (2/denom**2 + 2/(denom*T) + 1/(T**2))
        s4 += (1/(6*T**3)) * J_diag[i]**4
        extra += fi * s4
    chi03 = s3 + extra * gJ**4 * muB**4 * NA
    return chi01, chi03, s2, chi22

def compute_chiM1_ref(params, T_array):
    W = params['W']; x = params['x']; Theta_star = params['Theta_star']
    C = gJ**2 * muB**2 * J_*(J_+1) / 3.0
    n = Theta_star / C
    H = build_H_CEF(W, x)
    evals, evecs = eigh(H)
    chiM1 = np.zeros_like(T_array)
    for k, T in enumerate(T_array):
        chi01, _, _, _ = _chi0_CEF(evals, evecs, Jz_mat, O20, T)
        chiM1[k] = chi01 / (1 - n*chi01)
    return chiM1

def compute_chiM3_ref(params, T_array):
    W = params['W']; x = params['x']; Theta_star = params['Theta_star']
    G1 = params['G1']; G2 = params['G2']
    C = gJ**2 * muB**2 * J_*(J_+1) / 3.0
    n = Theta_star / C
    H001 = build_H_CEF(W, x)
    ev001, evc001 = eigh(H001)
    H111, Jz111, O20_111 = build_H_111(W, x)
    ev111, evc111 = eigh(H111)
    chi3_001 = np.zeros_like(T_array)
    chi3_111 = np.zeros_like(T_array)
    for k, T in enumerate(T_array):
        chi01_001, chi03_001, chi2_001, chi22_001 = _chi0_CEF(ev001, evc001, Jz_mat, O20, T)
        chi01_111, chi03_111, chi2_111, chi22_111 = _chi0_CEF(ev111, evc111, Jz111, O20_111, T)
        denom1 = 1 - n*chi01_001
        chi3_001[k] = chi03_001 / denom1**4 + 2*G1 * chi22_001**2 / (denom1**4 * (1 - G1*chi2_001))
        chi3_111[k] = chi03_111 / denom1**4 + (1/6)*G2 * chi22_111**2 / (denom1**4 * (1 - (1/12)*G2*chi2_111))
    return chi3_001, chi3_111


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
    spec = json.load(open('/tests/grading_spec.json'))
    model_params = spec['model_params']
    return dict(model_params=model_params, steps=spec['steps'], spec=spec)


# === block: score_0 (check id='chi_M1') ===
def score_0(artifact, step, ctx):
    def _interp_from_csv(artifact, T_col, val_col, T_targets):
        import numpy as np
        T = np.array([float(r[T_col]) for r in artifact])
        V = np.array([float(r[val_col]) for r in artifact])
        idx = np.argsort(T)
        T, V = T[idx], V[idx]
        interp_vals = np.interp(T_targets, T, V, left=np.nan, right=np.nan)
        return interp_vals

    import numpy as np
    step_params = ctx['steps'][0]['params']
    T_checks = np.array(step_params['checkpoints'])
    # compute reference
    mp = ctx['model_params']
    ref_vals = compute_chiM1_ref(mp, T_checks)  # defined in imports
    agent_vals = _interp_from_csv(artifact, 'T', 'chi_M1', T_checks)
    if np.any(np.isnan(agent_vals)):
        return 0.0
    rel_err = np.abs(agent_vals - ref_vals) / np.maximum(np.abs(ref_vals), 1e-12)
    tol = step_params['tolerance']
    max_err = step_params['max_relative_error']
    score_per_point = np.clip(1.0 - (rel_err - tol) / (max_err - tol), 0.0, 1.0)
    score = np.mean(score_per_point)
    return float(score)


# === block: score_1 (check id='chi_M3') ===
def score_1(artifact, step, ctx):
    def _interp_from_csv(artifact, T_col, val_col, T_targets):
        import numpy as np
        T = np.array([float(r[T_col]) for r in artifact])
        V = np.array([float(r[val_col]) for r in artifact])
        idx = np.argsort(T)
        T, V = T[idx], V[idx]
        interp_vals = np.interp(T_targets, T, V, left=np.nan, right=np.nan)
        return interp_vals

    import numpy as np
    step_params = ctx['steps'][1]['params']
    T_checks = np.array(step_params['checkpoints'])
    mp = ctx['model_params']
    from checker_ref import compute_chiM3_ref  # defined in imports
    ref_001, ref_111 = compute_chiM3_ref(mp, T_checks)
    agent_001 = _interp_from_csv(artifact, 'T', 'chi_M3_001', T_checks)
    agent_111 = _interp_from_csv(artifact, 'T', 'chi_M3_111', T_checks)
    if np.any(np.isnan(agent_001)) or np.any(np.isnan(agent_111)):
        return 0.0
    rel_err_001 = np.abs(agent_001 - ref_001) / np.maximum(np.abs(ref_001), 1e-12)
    rel_err_111 = np.abs(agent_111 - ref_111) / np.maximum(np.abs(ref_111), 1e-12)
    tol = step_params['tolerance']
    max_err = step_params['max_relative_error']
    score_001 = np.mean(np.clip(1.0 - (rel_err_001 - tol) / (max_err - tol), 0.0, 1.0))
    score_111 = np.mean(np.clip(1.0 - (rel_err_111 - tol) / (max_err - tol), 0.0, 1.0))
    score = 0.5 * (score_001 + score_111)
    return float(score)


_SCORERS = {
    'chi_M1': score_0,
    'chi_M3': score_1,
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
