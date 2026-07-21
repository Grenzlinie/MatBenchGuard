import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import minimize_scalar
import math, itertools, csv

SQRT2 = math.sqrt(2)
T_VALUE = 0.5

def build_hamiltonian(U, V):
    """Build 36x36 Hamiltonian in S_z=0 basis."""
    T = T_VALUE
    E_a0 = -0.5 * U
    # generate spin configurations with exactly 2 occupied sites
    up_cfgs = [n for n in range(16) if bin(n).count('1') == 2]
    dn_cfgs = up_cfgs[:]
    n_up = len(up_cfgs)
    n_dn = len(dn_cfgs)
    N = n_up * n_dn
    H = np.zeros((N, N))
    # links (i,j) with hopping amplitude
    links = [((0,1), V), ((1,2), T), ((2,3), T)]
    for i, up_i in enumerate(up_cfgs):
        for j, dn_j in enumerate(dn_cfgs):
            idx = i * n_dn + j
            # diagonal
            diag = 0.0
            if (up_i >> 0) & 1:
                diag += E_a0
            if (dn_j >> 0) & 1:
                diag += E_a0
            if ((up_i >> 0) & 1) and ((dn_j >> 0) & 1):
                diag += U
            H[idx, idx] = diag
            # hopping for each spin
            for (p, q), t in links:
                # spin up
                if ((up_i >> p) & 1) and not ((up_i >> q) & 1):
                    up_f = up_i ^ (1 << p) ^ (1 << q)
                    if up_f in up_cfgs:
                        i_f = up_cfgs.index(up_f)
                        # sign = (-1)^{# of up-electrons between p and q}
                        sign = 1
                        lo = min(p, q) + 1
                        hi = max(p, q) - 1
                        for k in range(lo, hi + 1):
                            if (up_i >> k) & 1:
                                sign = -sign
                        H[i_f * n_dn + j, idx] += -t * sign
                # spin down
                if ((dn_j >> p) & 1) and not ((dn_j >> q) & 1):
                    dn_f = dn_j ^ (1 << p) ^ (1 << q)
                    if dn_f in dn_cfgs:
                        j_f = dn_cfgs.index(dn_f)
                        sign = 1
                        lo = min(p, q) + 1
                        hi = max(p, q) - 1
                        for k in range(lo, hi + 1):
                            if (dn_j >> k) & 1:
                                sign = -sign
                        H[i * n_dn + j_f, idx] += -t * sign
    H = (H + H.T) / 2.0
    return H

def exact_deltaW(U, V):
    T = T_VALUE
    H = build_hamiltonian(U, V)
    w, _ = eigh(H)
    E_ground = w[0]
    E0 = -0.5 * U - 2 * SQRT2 * T
    return E_ground - E0

def weak_deltaW(U, V):
    T = T_VALUE
    return -V*V / (U + 2*SQRT2*T) - 4*V*V / U

def RSC_deltaW(U, V):
    T = T_VALUE
    # unperturbed energy E0 as defined in the instruction
    E0 = -0.5 * U - 2 * SQRT2 * T
    # surface complex energy
    halfU = 0.5 * U
    D = math.sqrt(halfU*halfU + 16.0*V*V)
    E_SC = -0.5 * (halfU + D)   # most negative
    E_3_2 = 2.0 * (SQRT2 - 1.0) * T
    # zero‑order RSC interaction energy (subtract E0)
    deltaW_SC = E_SC + E_3_2 - E0
    # rebonding correction
    D2 = math.sqrt(U*U + 16.0*V*V)
    E_plus = (-U + D2) / 4.0
    E_minus = (-U - D2) / 4.0
    denom_factor = (E_SC*E_SC + 4.0*V*V)
    num1 = (E_SC * E_minus + 2.0*V*V)**2
    den1 = (2.0*E_minus + T - E_SC) * (E_minus*E_minus + V*V)
    term1 = num1 / (den1 * denom_factor) if den1 != 0 else 0.0
    num2 = (E_SC * E_plus + 2.0*V*V)**2
    den2 = (2.0*E_plus + T - E_SC) * (E_plus*E_plus + V*V)
    term2 = num2 / (den2 * denom_factor) if den2 != 0 else 0.0
    deltaW_R = -T*T * (term1 + term2)
    return deltaW_SC + deltaW_R

def RHF_deltaW(U, V):
    T = T_VALUE
    V2 = V*V
    T2 = T*T
    term = math.sqrt(V2*V2 + 4.0*T2*T2)   # sqrt(V^4+4T^4)
    A = V2 + 2.0*T2
    s1 = math.sqrt(A + term)
    s2 = math.sqrt(A - term)
    return -SQRT2 * (s1 + s2 - 2.0*T)

def epsilon_URHF(x, U, V):
    """Epsilon(x) for given U,V,T."""
    T = T_VALUE
    # matrix for spin up (E_a = -U*x), spin down (E_a = +U*x)
    H_up = np.array([[-U*x, -V, 0.0, 0.0],
                     [-V, 0.0, -T, 0.0],
                     [0.0, -T, 0.0, -T],
                     [0.0, 0.0, -T, 0.0]])
    H_dn = np.array([[U*x, -V, 0.0, 0.0],
                     [-V, 0.0, -T, 0.0],
                     [0.0, -T, 0.0, -T],
                     [0.0, 0.0, -T, 0.0]])
    eig_up = np.linalg.eigvalsh(H_up)
    eig_dn = np.linalg.eigvalsh(H_dn)
    # take two lowest occupied for each (half-filled)
    occupied_up = eig_up[np.argsort(eig_up)[:2]]
    occupied_dn = eig_dn[np.argsort(eig_dn)[:2]]
    energy = occupied_up.sum() + occupied_dn.sum()
    counter = U * (0.25 - x*x)
    return energy - counter

def URHF_deltaW(U, V):
    T = T_VALUE
    E0 = -0.5*U - 2*SQRT2*T
    # find optimum x in [0, 0.5]
    res = minimize_scalar(lambda x: epsilon_URHF(x, U, V), bounds=(0.0, 0.5), method='bounded')
    E_min = res.fun
    return E_min - E0

def weak_ratio(U, V):
    T = T_VALUE
    return U/(U + 2*SQRT2*T) + 4.0


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


# === block: score_0 (check id='step_interaction_energies') ===
def score_0(artifact, step, ctx):
    tol_exact = step.get('tolerance_exact_abs', 1e-6)
    tol_approx = step.get('tolerance_approx_rel', 1e-4)
    # expected U and V lists
    U_list = [1.0, 2.5, 4.0]
    V_list = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5]
    expected = {(u, v) for u in U_list for v in V_list}
    rows = artifact  # list of dicts from CSV
    found = set()
    ok = 0
    total = len(expected)
    for row in rows:
        try:
            u = float(row['U'])
            v = float(row['V'])
            exact_a = float(row['exact_deltaW'])
            weak_a = float(row['weak_deltaW'])
            RSC_a = float(row['RSC_deltaW'])
            RHF_a = float(row['RHF_deltaW'])
            URHF_a = float(row['URHF_deltaW'])
        except (KeyError, ValueError):
            continue
        if (u, v) not in expected:
            continue
        found.add((u, v))
        # compute gold
        exact_g = exact_deltaW(u, v)
        weak_g = weak_deltaW(u, v)
        RSC_g = RSC_deltaW(u, v)
        RHF_g = RHF_deltaW(u, v)
        URHF_g = URHF_deltaW(u, v)
        # check exact: absolute
        if abs(exact_a - exact_g) > tol_exact:
            continue
        # check approximations: relative tolerance with floor
        def ok_relative(a, g):
            denom = max(abs(g), 1e-12)
            err = abs(a - g) / denom
            return err <= tol_approx
        if not ok_relative(weak_a, weak_g):
            continue
        if not ok_relative(RSC_a, RSC_g):
            continue
        if not ok_relative(RHF_a, RHF_g):
            continue
        if not ok_relative(URHF_a, URHF_g):
            continue
        ok += 1
    # missing rows counted as failures
    return ok / total if total > 0 else 0.0


# === block: score_1 (check id='step_weak_limits') ===
def score_1(artifact, step, ctx):
    tol = step.get('tolerance_abs', 1e-6)
    T = T_VALUE
    expected = [(4.0, 1e-4), (0.1, 1e-4)]
    rows = artifact
    found = set()
    correct = 0
    for row in rows:
        try:
            u = float(row['U'])
            v = float(row['V'])
            ratio_a = float(row['ratio'])
        except (KeyError, ValueError):
            continue
        if (u, v) not in expected:
            continue
        found.add((u, v))
        # recompute ratio from weak formula
        ratio_g = weak_ratio(u, v)
        if abs(ratio_a - ratio_g) <= tol:
            correct += 1
    # both required rows must be present and correct
    if len(found) == len(expected) and correct == len(expected):
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_interaction_energies': score_0,
    'step_weak_limits': score_1,
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