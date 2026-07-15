import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import dblquad

mu0 = 4e-7 * np.pi
eps0 = 8.854187817e-12
c = 299792458.0
Z0 = np.sqrt(mu0 / eps0)


def X_val(a):
    f = lambda y, x: np.arcsin(np.sin(y) / np.sin(a))
    res, _ = dblquad(f, 0, a, lambda x: x, lambda x: a, epsabs=1e-12, epsrel=1e-12)
    return res


def capacitive_L(w, T):
    theta = np.pi * w / (2 * T)
    ln_cosec = np.log(1.0 / np.sin(theta))
    ln_sec = np.log(1.0 / np.cos(theta))
    Xa = X_val(theta)
    L = (mu0 * T / (4 * np.pi)) * (ln_cosec + (np.pi**2 * w**2 / (12 * T**2) - (2 / np.pi) * Xa) / ln_sec)
    return L


def capacitive_C(w, T, eps1, eps2):
    theta = np.pi * w / (2 * T)
    C = eps0 * (eps1 + eps2) / np.pi * T * np.log(1.0 / np.cos(theta))
    return C


def Y_inductive(s, T, eps1, eps2, omega):
    theta = np.pi * s / (2 * T)
    term1 = (2 * np.pi * 1j) / (omega * mu0 * s * np.log(1.0 / np.cos(theta)))
    term2 = -1j * omega * eps0 * T * (eps1 + eps2) / np.pi * np.log(1.0 / np.sin(theta))
    return term1 + term2


def Y_capacitive(w, T, eps1, eps2, omega, L, C):
    return 1j / (omega * L) - 1j * omega * C


def grating_S(Y, eps1, eps2):
    sqrt_e1 = np.sqrt(eps1)
    sqrt_e2 = np.sqrt(eps2)
    denom = sqrt_e1 + sqrt_e2 + Z0 * Y
    S11 = (sqrt_e1 - sqrt_e2 - Z0 * Y) / denom
    S12 = 2 * (eps1 * eps2)**0.25 / denom
    S21 = S12
    S22 = (sqrt_e2 - sqrt_e1 - Z0 * Y) / denom
    return np.array([[S11, S12], [S21, S22]])


def S_to_ABCD(S, Z1, Z2):
    S11, S12, S21, S22 = S[0,0], S[0,1], S[1,0], S[1,1]
    Delta = S11*S22 - S21*S12
    A = (1 + S11 - S22 - Delta) * np.sqrt(Z1/Z2) / (2*S21)
    B = (1 + S11 + S22 + Delta) * np.sqrt(Z1*Z2) / (2*S21)
    C = (1 - S11 - S22 + Delta) / (2*S21 * np.sqrt(Z1*Z2))
    D = (1 - S11 + S22 - Delta) * np.sqrt(Z2/Z1) / (2*S21)
    return np.array([[A, B], [C, D]])


def dielectric_ABCD(h, eps_complex, omega):
    eps_sqrt = np.sqrt(eps_complex)
    theta = omega * eps_sqrt * h / c
    cosT = np.cos(theta)
    sinT = np.sin(theta)
    A = cosT
    B = -1j * (Z0 / eps_sqrt) * sinT
    C = -1j * (eps_sqrt / Z0) * sinT
    D = cosT
    return np.array([[A, B], [C, D]])


def ABCD_to_S(ABCD, Z1, Z2):
    A, B, C, D = ABCD[0,0], ABCD[0,1], ABCD[1,0], ABCD[1,1]
    denom = A*Z2 + B + C*Z1*Z2 + D*Z1
    S11 = (A*Z2 + B - C*Z1*Z2 - D*Z1) / denom
    S12 = 2*(A*D - B*C)*np.sqrt(Z1*Z2) / denom
    S21 = 2*np.sqrt(Z1*Z2) / denom
    S22 = (-A*Z2 + B - C*Z1*Z2 + D*Z1) / denom
    return np.array([[S11, S12], [S21, S22]])


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
    T = 3.0e-3
    h = 1.29e-3
    eps_r = 11.2
    tan_delta = 0.0022
    eps_diel_real = eps_r
    eps_diel_complex = eps_r * (1 - 1j * tan_delta)
    s_L1 = 2.846e-3
    s_L2 = 1.570e-3
    w_C1 = 1.770e-3
    w_C2 = 2.205e-3

    L1 = capacitive_L(w_C1, T)
    C1 = capacitive_C(w_C1, T, eps_diel_real, eps_diel_real)
    L2 = capacitive_L(w_C2, T)
    C2 = capacitive_C(w_C2, T, eps_diel_real, eps_diel_real)

    ctx = {
        'T': T, 'h': h, 'eps_diel_real': eps_diel_real, 'eps_diel_complex': eps_diel_complex,
        's_L1': s_L1, 's_L2': s_L2, 'w_C1': w_C1, 'w_C2': w_C2,
        'L1': L1, 'C1': C1, 'L2': L2, 'C2': C2
    }
    return ctx


# === block: score_0 (check id='compute_response') ===
def score_0(artifact, step, ctx):
    artifact_csv = artifact
    if not artifact_csv:
        return 0.0

    agent_f = np.array([float(row['f']) for row in artifact_csv])
    agent_s21 = np.array([float(row['S21_dB']) for row in artifact_csv])
    agent_s11 = np.array([float(row['S11_dB']) for row in artifact_csv])

    freq_tol = step.get('freq_tol_HZ', 1e6)
    tol_dB = step.get('tol_dB', 0.5)
    tol_dB_low = step.get('tol_dB_low', 2.0)
    low_thresh = step.get('low_threshold_dB', -40.0)

    expected_f = np.arange(8e9, 18e9 + 1e-8, 10e6)

    T = ctx['T']
    h = ctx['h']
    eps_diel_real = ctx['eps_diel_real']
    eps_diel_complex = ctx['eps_diel_complex']
    s_L1 = ctx['s_L1']
    s_L2 = ctx['s_L2']
    w_C1 = ctx['w_C1']
    w_C2 = ctx['w_C2']
    L1 = ctx['L1']
    C1 = ctx['C1']
    L2 = ctx['L2']
    C2 = ctx['C2']

    Z_free = Z0 / np.sqrt(1.0)
    Z_diel = Z0 / np.sqrt(eps_diel_real)

    expected_s21 = []
    expected_s11 = []

    for fe in expected_f:
        omega = 2.0 * np.pi * fe
        Y_L1 = Y_inductive(s_L1, T, 1.0, eps_diel_real, omega)
        S_L1 = grating_S(Y_L1, 1.0, eps_diel_real)
        ABCD_L1 = S_to_ABCD(S_L1, Z_free, Z_diel)
        ABCD_d1 = dielectric_ABCD(h, eps_diel_complex, omega)
        Y_C1 = Y_capacitive(w_C1, T, eps_diel_real, eps_diel_real, omega, L1, C1)
        S_C1 = grating_S(Y_C1, eps_diel_real, eps_diel_real)
        ABCD_C1 = S_to_ABCD(S_C1, Z_diel, Z_diel)
        ABCD_d2 = dielectric_ABCD(h, eps_diel_complex, omega)
        Y_L2 = Y_inductive(s_L2, T, eps_diel_real, eps_diel_real, omega)
        S_L2 = grating_S(Y_L2, eps_diel_real, eps_diel_real)
        ABCD_L2 = S_to_ABCD(S_L2, Z_diel, Z_diel)
        ABCD_d3 = dielectric_ABCD(h, eps_diel_complex, omega)
        Y_C2 = Y_capacitive(w_C2, T, eps_diel_real, eps_diel_real, omega, L2, C2)
        S_C2 = grating_S(Y_C2, eps_diel_real, eps_diel_real)
        ABCD_C2 = S_to_ABCD(S_C2, Z_diel, Z_diel)
        ABCD_d4 = dielectric_ABCD(h, eps_diel_complex, omega)

        ABCD_L2_2 = ABCD_L2
        ABCD_d5 = ABCD_d3
        ABCD_C1_2 = ABCD_C1
        ABCD_d6 = ABCD_d2
        Y_L1_2 = Y_inductive(s_L1, T, eps_diel_real, 1.0, omega)
        S_L1_2 = grating_S(Y_L1_2, eps_diel_real, 1.0)
        ABCD_L1_2 = S_to_ABCD(S_L1_2, Z_diel, Z_free)

        ABCD_total = ABCD_L1
        ABCD_total = ABCD_total @ ABCD_d1
        ABCD_total = ABCD_total @ ABCD_C1
        ABCD_total = ABCD_total @ ABCD_d2
        ABCD_total = ABCD_total @ ABCD_L2
        ABCD_total = ABCD_total @ ABCD_d3
        ABCD_total = ABCD_total @ ABCD_C2
        ABCD_total = ABCD_total @ ABCD_d4
        ABCD_total = ABCD_total @ ABCD_L2_2
        ABCD_total = ABCD_total @ ABCD_d5
        ABCD_total = ABCD_total @ ABCD_C1_2
        ABCD_total = ABCD_total @ ABCD_d6
        ABCD_total = ABCD_total @ ABCD_L1_2

        S_total = ABCD_to_S(ABCD_total, Z_free, Z_free)
        s21_db = 20.0 * np.log10(np.abs(S_total[1, 0]) + 1e-30)
        s11_db = 20.0 * np.log10(np.abs(S_total[0, 0]) + 1e-30)
        expected_s21.append(s21_db)
        expected_s11.append(s11_db)

    expected_s21 = np.array(expected_s21)
    expected_s11 = np.array(expected_s11)

    pass_count = 0
    total = len(expected_f)
    for i, fe in enumerate(expected_f):
        diffs = np.abs(agent_f - fe)
        idx = np.argmin(diffs)
        if diffs[idx] > freq_tol:
            continue
        effective_tol = tol_dB_low if (expected_s21[i] < low_thresh or expected_s11[i] < low_thresh) else tol_dB
        s21_ok = abs(agent_s21[idx] - expected_s21[i]) <= effective_tol
        s11_ok = abs(agent_s11[idx] - expected_s11[i]) <= effective_tol
        if s21_ok and s11_ok:
            pass_count += 1

    return pass_count / total if total > 0 else 0.0


_SCORERS = {
    'compute_response': score_0,
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
