import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from numpy import linalg as LA
import csv, io, math, itertools


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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    # Compute chiT reference values and compare to agent CSV.
    # artifact is list of dicts with keys compound, T, chiT (header expected).
    # Return score = fraction of points within tolerance.

    # --- physical constants ---
    kB_cm = 0.69503476      # cm^-1 / K
    C_chiT = 0.125048       # (N_A * mu_B^2) / (3 * k_B) in cm^3 K mol^-1

    # model parameters
    LAMBDA = -180.0
    KAPPA = 0.8
    HBAR_OMEGA_HS = 95.0
    HBAR_OMEGA_LS = 105.0
    N_VIB = 15

    # compound-specific parameters: (J1, J2, Delta_hl, Delta, y_hs)
    compounds = {
        '1': (24.4, 132.0, 885.0, -300.0, 0.204),
        '2': (18.6, 100.7, 1264.0, -300.0, 0.040),
        '3': (18.6, 100.7, 894.0, -300.0, 0.018),
    }

    # --- spin-orbit matrices for high-spin (L=1, S=3/2) ---

    def spin_matrices():
        # S = 3/2
        S = 1.5
        mS = np.arange(S, -S-1, -1).astype(float)
        dimS = len(mS)
        Sz = np.diag(mS)
        Sp = np.zeros((dimS, dimS))
        for i in range(dimS):
            if i > 0:
                Sp[i-1, i] = np.sqrt(S*(S+1) - mS[i]*(mS[i]-1))
        Sm = np.copy(Sp.T)
        return Sz, Sp, Sm

    def orbital_matrices_l1():
        # L = 1
        L = 1.0
        mL = np.arange(L, -L-1, -1).astype(float)
        dimL = len(mL)
        Lz = np.diag(mL)
        Lp = np.zeros((dimL, dimL))
        for i in range(dimL):
            if i > 0:
                Lp[i-1, i] = np.sqrt(L*(L+1) - mL[i]*(mL[i]-1))
        Lm = np.copy(Lp.T)
        return Lz, Lp, Lm

    def hs_hamiltonian_so():
        Sz, Sp, Sm = spin_matrices()
        Lz, Lp, Lm = orbital_matrices_l1()
        dimS, dimL = len(Sz), len(Lz)
        # basis: |mL, mS>  row = mL*major? we'll flatten
        mz = np.kron(Lz, np.eye(dimS))  # Lz
        Sz_op = np.kron(np.eye(dimL), Sz)
        Lp_op = np.kron(Lp, np.eye(dimS))
        Lm_op = np.kron(Lm, np.eye(dimS))
        # spin operators
        Sp_op = np.kron(np.eye(dimL), Sp)
        Sm_op = np.kron(np.eye(dimL), Sm)
        # S·L = Sz*Lz + 0.5*(S+ L- + S- L+)
        SdotL = Sz_op @ mz + 0.5*(Sp_op @ Lm_op + Sm_op @ Lp_op)
        # spin-orbit coefficient
        coeff = -1.5 * KAPPA * LAMBDA  # = 216 cm^-1
        H_so = coeff * SdotL
        # magnetization operator mz_total = g0*Sz - 1.5*KAPPA*Lz
        g0 = 2.0
        mz_op = g0 * Sz_op - 1.5 * KAPPA * mz
        return H_so, mz_op

    H_hs, mz_hs = hs_hamiltonian_so()
    # eigenvalues and eigenvectors of hs hamiltonian (without gap shift)
    E_hs, U_hs = LA.eigh(H_hs)

    # precompute hs chiT for each temperature (Van Vleck)
    def compute_chiT_hs(kT):
        Z = np.sum(np.exp(-E_hs / kT))
        # diagonal part
        mz_eig = U_hs.T @ mz_hs @ U_hs
        diag_part = np.sum(np.diag(mz_eig)**2 * np.exp(-E_hs / kT)) / Z
        # off-diagonal part
        off_part = 0.0
        for i in range(len(E_hs)):
            for j in range(i+1, len(E_hs)):
                deltaE = E_hs[j] - E_hs[i]
                if abs(deltaE) < 1e-10:
                    continue
                weight = (np.exp(-E_hs[i]/kT) - np.exp(-E_hs[j]/kT)) / deltaE
                off_part += 2.0 * abs(mz_eig[i,j])**2 * weight / Z
        mu2 = diag_part + off_part
        return C_chiT * mu2

    def chiT_hs_only(T):
        kT = kB_cm * T
        return compute_chiT_hs(kT)

    # ls susceptibility constant: spin only g0^2 * 3/4
    chiT_ls0 = C_chiT * (2.0**2) * 0.75  # = 0.375 cm^3 K mol^{-1}

    # vibrational partition function
    def vib_factor(freq, kT):
        if kT < 1e-6:
            return 1.0
        x = freq / (2.0 * kT)
        return (1.0 / (2.0 * math.sinh(x))) ** N_VIB

    # solve I2 self-consistent: I2 = tanh((Delta/2 - J2*I2)/kT)
    def solve_I2(J2, Delta, kT):
        if kT < 1e-6:
            # low T limit: sign based on Delta
            return np.sign(Delta/2) if abs(Delta)>1e-12 else 0.0
        # function f(I2) = tanh((Delta/2 - J2*I)/kT)
        # use fixed-point with relaxation
        I = 0.0
        for _ in range(1000):
            arg = (Delta/2.0 - J2 * I) / kT
            I_new = math.tanh(arg)
            if abs(I_new - I) < 1e-12:
                break
            I = I_new
        return I

    # solve tau_mean self-consistently after I2 known
    def solve_tau_mean(J1, J2, Delta_hl, Delta, kT):
        I2 = solve_I2(J2, Delta, kT)
        # Z_hs0 = sum exp(-E_i/kT)
        Z_hs0 = np.sum(np.exp(-E_hs / kT))
        # Z_ls0 for ls internal energies: 4 states (2 orbital * 2 spin) with energies +/- (Delta/2 - J2*I2)
        Delta_eff = Delta/2.0 - J2 * I2
        Z_ls0 = 4.0 * math.cosh(Delta_eff / kT)
        Z_hs_vib = vib_factor(HBAR_OMEGA_HS, kT)
        Z_ls_vib = vib_factor(HBAR_OMEGA_LS, kT)
        A = Z_hs0 * Z_hs_vib
        B = Z_ls0 * Z_ls_vib
        # Correct symmetric shifts: HS (+Delta_hl/2), LS (-Delta_hl/2)
        factor_hs = math.exp(-Delta_hl / (2.0 * kT))
        factor_ls = math.exp(Delta_hl / (2.0 * kT))
        tau = 0.0
        for _ in range(2000):
            e_pos = math.exp(J1 * tau / kT)
            e_neg = 1.0 / e_pos
            numerator = A * e_pos * factor_hs - B * e_neg * factor_ls
            denominator = A * e_pos * factor_hs + B * e_neg * factor_ls
            tau_new = numerator / denominator
            if abs(tau_new - tau) < 1e-10:
                break
            tau = tau_new
        return tau, I2, A, B, Z_hs0, Z_ls0, Z_hs_vib, Z_ls_vib, factor_hs, factor_ls

    # compute chiT for SCO fraction at given T
    def compute_chiT_SCO(J1, J2, Delta_hl, Delta, kT):
        tau, I2, A, B, Z_hs0, Z_ls0, Z_hs_vib, Z_ls_vib, factor_hs, factor_ls = solve_tau_mean(J1, J2, Delta_hl, Delta, kT)
        # P_hs, P_ls
        e_pos = math.exp(J1 * tau / kT)
        e_neg = 1.0 / e_pos
        Z_hs_total = A * e_pos * factor_hs
        Z_ls_total = B * e_neg * factor_ls
        Z_total = Z_hs_total + Z_ls_total
        P_hs = Z_hs_total / Z_total
        P_ls = Z_ls_total / Z_total
        chiT_hs = compute_chiT_hs(kT)
        chiT_SCO = P_hs * chiT_hs + P_ls * chiT_ls0
        return chiT_SCO

    # total chiT for a compound
    def total_chiT(compound, T):
        J1, J2, Delta_hl, Delta, y_hs = compounds[compound]
        kT = kB_cm * T
        chiT_hs = compute_chiT_hs(kT)
        chiT_sco = compute_chiT_SCO(J1, J2, Delta_hl, Delta, kT)
        return y_hs * chiT_hs + (1.0 - y_hs) * chiT_sco

    # === scoring ===
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    # build lookup
    data = {}
    try:
        for row in artifact:
            comp = str(row.get('compound', '')).strip()
            t = float(row.get('T', 0))
            c = float(row.get('chiT', 0))
            data[(comp, t)] = c
    except Exception:
        return 0.0

    # expected points
    temps = np.arange(50, 355, 5)
    total_points = 0
    matched = 0
    for comp in ['1', '2', '3']:
        for t in temps:
            total_points += 1
            key = (comp, t)
            if key not in data:
                continue
            agent_val = data[key]
            ref_val = total_chiT(comp, t)
            # tolerance
            if ref_val <= 1.0:
                tol = 0.1
            else:
                tol = 0.05 * abs(ref_val)
            if abs(agent_val - ref_val) <= max(tol, 1e-9):
                matched += 1

    score = matched / total_points if total_points > 0 else 0.0
    return float(score)


_SCORERS = {
    'step_01': score_0,
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
