import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import brentq

# Fundamental constants (cm -> a.u.)
BOHR_CM = 5.29177210903e-9   # 1 Bohr radius in cm
A0_SQ_CM2 = BOHR_CM**2       # 1 a.u.^2 in cm^2

# Energy functional for semiconductor (Inkson), Eq.(2)
def E_func(rs, kappa):
    return (1.105/rs**2
            - 0.4581/(kappa*rs)
            + 0.042 * (kappa/(kappa-1)) * np.log(rs)
            - 0.117 * (2*kappa/(kappa-1) - 1))

def dE_drs_func(rs, kappa):
    return (-2*1.105/rs**3
            + 0.4581/(kappa*rs**2)
            + 0.042 * (kappa/(kappa-1)) / rs)

def nbar_dEdn(rs, kappa):
    return - (rs/3) * dE_drs_func(rs, kappa)

def nbar_from_rs(rs):
    return 3.0/(4*np.pi*rs**3)

# Convert Na (atoms/cm^2) to a.u.^-2
def Na_to_au(Na_cm2):
    return Na_cm2 * A0_SQ_CM2

def compute_s(Na_cm2, d_au, nbar):
    if Na_cm2 == 0:
        return 0.0
    return Na_to_au(Na_cm2) / (nbar * d_au)

# Equation (10) left-hand side
def eq10(y, s, d_au, kappa):
    if s == 0:
        return None   # handled separately
    t1 = (1.0/16.0) * (1-y)**3
    # avoid overflow: if y/s > 100, exp(-y/s) ~ 0
    if s > 0 and y/s > 100:
        t2 = s
    else:
        t2 = -s * (np.exp(-y/s) - 1)
    t3 = -0.5 * y**2 * (2-y) * (1 + 0.9512/(s**2 * d_au**2))
    t4 = (15.0/32.0) * (1-y)**4/(2-y) if abs(y-2) > 1e-12 else 0.0
    return t1 + t2 + t3 + t4

def solve_y(d_au, Na_cm2, rs, kappa, nbar):
    s = compute_s(Na_cm2, d_au, nbar)
    if s == 0:
        return None
    # bracket: y in (0, 1)
    try:
        f = lambda y: eq10(y, s, d_au, kappa)
        y = brentq(f, 1e-12, 0.9999, xtol=1e-12, rtol=1e-12)
        return y
    except Exception:
        return None

def compute_Phi_eV(d_au, Na_cm2, rs, kappa, nbar):
    s = compute_s(Na_cm2, d_au, nbar)
    y = solve_y(d_au, Na_cm2, rs, kappa, nbar)
    if y is None or y <= 1e-12:
        return None
    term = (0.331 * d_au**2 * s**2) / (y**2 * (2-y))
    bracket = (1.0/16.0)*(1-y)**3 + 1 - 0.5*y**2/s*(2-y)
    Phi_a_u = term * bracket - 0.348
    return Phi_a_u * 27.2114

# Density for covered case
def covered_density_params(d_au, Na_cm2, rs, kappa, nbar):
    s = compute_s(Na_cm2, d_au, nbar)
    y = solve_y(d_au, Na_cm2, rs, kappa, nbar)
    A = nbar * (1-y)/(2-y)
    B = nbar / (2-y)
    beta1 = y / (d_au * s * (1-y))
    beta2 = y / (d_au * s)
    return A, B, beta1, beta2, s, y

def n_over_nbar_covered(x, d_au, Na_cm2, rs, kappa, nbar):
    A, B, beta1, beta2, s, y = covered_density_params(d_au, Na_cm2, rs, kappa, nbar)
    if x < 0:
        return 1.0 - (A/nbar) * np.exp(beta1 * x)
    else:
        return (B/nbar) * np.exp(-beta2 * x)


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
    rs = 2.085
    kappa = 16.0
    nbar = nbar_from_rs(rs)
    a0_sq_cm2 = A0_SQ_CM2
    # compute clean Phi reference (from Inkson model limit or known value)
    clean_Phi_target = 5.0   # eV, from paper statement
    ctx = {
        'rs': rs,
        'kappa': kappa,
        'nbar': nbar,
        'a0_sq_cm2': a0_sq_cm2,
        'clean_Phi_target': clean_Phi_target
    }
    return ctx


# === block: score_0 (check id='workfunction_check') ===
def score_0(artifact, step, ctx):
    params = step.get('params', {})
    tol = params.get('abs_tol_Phi', 0.01)
    clean_target = params.get('clean_Phi_target', 5.0)
    clean_tol = params.get('clean_Phi_tol', 0.5)
    rs = ctx['rs']
    kappa = ctx['kappa']
    nbar = ctx['nbar']
    total = 0
    correct = 0.0
    for row in artifact:
        d = float(row['d'])
        Na = float(row['Na'])
        Phi_agent = float(row['Phi'])
        if Na == 0.0:
            if abs(Phi_agent - clean_target) <= clean_tol:
                correct += 1.0
            total += 1
        else:
            Phi_exp = compute_Phi_eV(d, Na, rs, kappa, nbar)
            if Phi_exp is None:
                total += 1
                continue
            if abs(Phi_agent - Phi_exp) <= tol:
                correct += 1.0
            total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_1 (check id='density_check') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    tol = params.get('abs_tol_n', 0.001)
    Na_covered = params.get('Na_covered', 6.7e14)
    d_covered = params.get('d_covered', 7.13)
    rs = ctx['rs']
    kappa = ctx['kappa']
    nbar = ctx['nbar']
    A_cov, B_cov, beta1_cov, beta2_cov, s_cov, y_cov = covered_density_params(d_covered, Na_covered, rs, kappa, nbar)
    total = 0
    correct = 0.0
    for row in artifact:
        case = str(row.get('case', '')).strip().lower()
        x = float(row['x'])
        n_agent = float(row['n_over_nbar'])
        if case == 'covered':
            n_exp = n_over_nbar_covered(x, d_covered, Na_covered, rs, kappa, nbar)
            if n_exp is None:
                total += 1
                continue
            if abs(n_agent - n_exp) <= tol:
                correct += 1.0
            total += 1
        elif case == 'clean':
            if 0.0 <= n_agent <= 1.1:
                correct += 1.0
            total += 1
        else:
            total += 1
    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    'workfunction_check': score_0,
    'density_check': score_1,
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
