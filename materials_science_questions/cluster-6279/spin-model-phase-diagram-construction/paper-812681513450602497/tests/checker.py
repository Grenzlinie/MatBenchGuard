import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy import integrate, special


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


# === block: score_0 (check id='step01') ===
def score_0(artifact, step, ctx):
    cfg = step.get("temperature_points", [])
    rel_tol = step.get("rel_tol", 1e-4)
    if not cfg or not artifact:
        return 0.0
    rows = artifact
    t_arr = np.array([float(r["temperature"]) for r in rows])
    c_arr = np.array([float(r["heat_capacity"]) for r in rows])
    s_arr = np.array([float(r["entropy"]) for r in rows])
    if len(t_arr) == 0:
        return 0.0

    def gold_step01(T):
        Jxd = -1.0; Jyd = -1.0; Jx = -0.8; Jy = -3.0
        Kxd = Jxd / T; Kyd = Jyd / T; Kx = Jx / T; Ky = Jy / T
        # simplified formulas for d=1
        C1 = 0.5 * np.exp(2*Kx + 4*Kxd) + 0.5 * np.exp(-2*Kx)
        S1 = 0.5 * np.exp(2*Kx + 4*Kxd) - 0.5 * np.exp(-2*Kx)
        D1 = np.exp(2*Kxd)
        C2 = 0.5 * np.exp(2*Ky + 4*Kyd) + 0.5 * np.exp(-2*Ky)
        S2 = 0.5 * np.exp(2*Ky + 4*Kyd) - 0.5 * np.exp(-2*Ky)
        D2 = np.exp(2*Kyd)
        def integrand(phi, theta):
            denom = C1*C2 - S1*D2*np.cos(phi) - S2*D1*np.cos(theta)
            return np.log(denom)
        I, err = integrate.nquad(integrand, [[0, 2*np.pi], [0, 2*np.pi]], opts={'epsabs': 1e-8, 'epsrel': 1e-8})
        N0 = 3.0
        ln_lam = I / (8*np.pi**2 * N0) + np.log(2.0)
        h = 1e-4 * T + 1e-6
        def I_val(Tv):
            Kxd = Jxd/Tv; Kyd = Jyd/Tv; Kx = Jx/Tv; Ky = Jy/Tv
            C1 = 0.5 * np.exp(2*Kx + 4*Kxd) + 0.5 * np.exp(-2*Kx)
            S1 = 0.5 * np.exp(2*Kx + 4*Kxd) - 0.5 * np.exp(-2*Kx)
            D1 = np.exp(2*Kxd)
            C2 = 0.5 * np.exp(2*Ky + 4*Kyd) + 0.5 * np.exp(-2*Ky)
            S2 = 0.5 * np.exp(2*Ky + 4*Kyd) - 0.5 * np.exp(-2*Ky)
            D2 = np.exp(2*Kyd)
            def integrand_inner(phi, theta):
                denom = C1*C2 - S1*D2*np.cos(phi) - S2*D1*np.cos(theta)
                return np.log(denom)
            I_in, e_in = integrate.nquad(integrand_inner, [[0, 2*np.pi], [0, 2*np.pi]], opts={'epsabs': 1e-8, 'epsrel': 1e-8})
            return I_in
        Ip = I_val(T + h)
        Im = I_val(T - h)
        dI_dT = (Ip - Im) / (2*h)
        d2I_dT2 = (Ip - 2*I + Im) / (h*h)
        dln_lam_dT = dI_dT / (8*np.pi**2 * N0)
        d2ln_lam_dT2 = d2I_dT2 / (8*np.pi**2 * N0)
        S = (ln_lam + T * dln_lam_dT) / N0
        dS_dT = (2*dln_lam_dT + T*d2ln_lam_dT2) / N0
        C = T * dS_dT
        return C, S

    scores = []
    for T_gold in cfg:
        idx = np.argmin(np.abs(t_arr - T_gold))
        C_agent = c_arr[idx]
        S_agent = s_arr[idx]
        C_gold, S_gold = gold_step01(T_gold)
        if C_gold == 0 and S_gold == 0:
            continue
        rel_C = abs(C_agent - C_gold) / max(abs(C_gold), 1e-12)
        rel_S = abs(S_agent - S_gold) / max(abs(S_gold), 1e-12)
        if rel_C <= rel_tol and rel_S <= rel_tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return np.mean(scores)


# === block: score_1 (check id='step02') ===
def score_1(artifact, step, ctx):
    cfg = step.get("temperature_points", [])
    rel_tol = step.get("rel_tol", 1e-4)
    if not cfg or not artifact:
        return 0.0
    rows = artifact
    t_arr = np.array([float(r["temperature"]) for r in rows])
    c_arr = np.array([float(r["heat_capacity"]) for r in rows])
    if len(t_arr) == 0:
        return 0.0

    def gold_step02(T):
        Kd = 1.0 / T
        m = 2.0 * np.sinh(2*Kd) * np.sinh(4*Kd) / (np.cosh(2*Kd)**2 + 1)**2
        h = 1e-5
        Kp = Kd + h
        Km = Kd - h
        mp = 2.0 * np.sinh(2*Kp) * np.sinh(4*Kp) / (np.cosh(2*Kp)**2 + 1)**2
        mm = 2.0 * np.sinh(2*Km) * np.sinh(4*Km) / (np.cosh(2*Km)**2 + 1)**2
        dm = (mp - mm) / (2*h)
        d2m = (mp - 2*m + mm) / (h*h)
        Kel = special.ellipk(m)
        Eel = special.ellipe(m)
        if m == 0 or np.isnan(m):
            return 0.0
        coth4 = 1.0 / np.tanh(4*Kd)
        csch4 = 1.0 / np.sinh(4*Kd)
        term1 = np.pi * (3 + np.cosh(4*Kd)) * (csch4**2)
        term2 = 0.25 * (2*dm**2 - m*d2m) / (m**2) * Kel
        term3 = (coth4 + 3*csch4)**2 * Eel
        C = (4*Kd**2 / (3*np.pi)) * (term1 + term2 - term3)
        return C

    scores = []
    for T_gold in cfg:
        idx = np.argmin(np.abs(t_arr - T_gold))
        C_agent = c_arr[idx]
        C_gold = gold_step02(T_gold)
        if C_gold == 0:
            continue
        rel = abs(C_agent - C_gold) / max(abs(C_gold), 1e-12)
        if rel <= rel_tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    if not scores:
        return 0.0
    return np.mean(scores)


# === block: score_2 (check id='step03') ===
def score_2(artifact, step, ctx):
    artifact_text = artifact
    try:
        Tc_agent = float(artifact_text.strip())
    except:
        return 0.0
    Tc_gold = 2.0 / np.arccosh(1 + np.sqrt(2))
    abs_tol = step.get("abs_tol", 0.01)
    if abs(Tc_agent - Tc_gold) <= abs_tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step01': score_0,
    'step02': score_1,
    'step03': score_2,
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
