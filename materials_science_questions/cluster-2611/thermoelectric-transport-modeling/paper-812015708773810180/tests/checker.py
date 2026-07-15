import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

def fermi_integral(r, xi):
    if r <= -1:
        raise ValueError('Fermi integral requires r > -1')
    upper = max(50, xi + 20) if xi < 50 else xi + 20
    def integrand(x):
        return x**r / (1.0 + np.exp(x - xi))
    res, _ = quad(integrand, 0, upper, limit=200)
    return res

def solve_reduced_chemical_potential(S_v_per_K, r=0.5):
    k_b = 1.380649e-23
    e = 1.602176634e-19
    def f(xi):
        F_r = fermi_integral(r, xi)
        F_rp1 = fermi_integral(r+1, xi)
        lhs = - (k_b / e) * ( ((r+2)*F_rp1) / ((r+1)*F_r) - xi )
        return lhs - S_v_per_K
    a, b = -50, 50
    try:
        xi = brentq(f, a, b, xtol=1e-12, rtol=1e-12)
    except ValueError:
        a, b = -200, 200
        xi = brentq(f, a, b, xtol=1e-12, rtol=1e-12)
    return xi

def compute_md_star(n_e, S_uv_per_K):
    h = 6.62607015e-34
    k_b = 1.380649e-23
    n_e_SI = n_e * 1e27
    S_SI = S_uv_per_K * 1e-6
    xi = solve_reduced_chemical_potential(S_SI)
    F12 = fermi_integral(0.5, xi)
    md_star = (h**2 / (2*k_b*300)) * ( n_e_SI / (4*np.pi*F12) )**(2/3)
    md_star /= 9.10938356e-31
    return md_star

def compute_tau(mu_Hall, md_star):
    e = 1.602176634e-19
    m_e = 9.10938356e-31
    mu_si = mu_Hall * 1e-4
    tau_s = mu_si * md_star * m_e / e
    return tau_s * 1e15

def compute_PF(n_e, mu_Hall, S_uv_per_K):
    e = 1.602176634e-19
    n_e_SI = n_e * 1e27
    mu_si = mu_Hall * 1e-4
    sigma = n_e_SI * e * mu_si
    S_SI = S_uv_per_K * 1e-6
    return S_SI**2 * sigma


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


# === block: score_0 (check id='step_01_recompute') ===
def score_0(artifact, step, ctx):
    import os
    import csv as csv_module

    ref_data = {}
    try:
        with open(os.path.join('/tests', 'table_1_reference.csv'), newline='') as f:
            reader = csv_module.DictReader(f)
            for r in reader:
                ref_data[r['composition'].strip()] = (float(r['n_e']), float(r['mu_Hall']), float(r['S']))
    except Exception:
        return 0.0

    score = 0.0
    rows = 0
    tolerances = step.get('config', {}).get('tolerances', {'m_d_star':0.005, 'tau':0.01, 'PF':0.01})
    tol_md = tolerances.get('m_d_star', 0.005)
    tol_tau = tolerances.get('tau', 0.01)
    tol_PF = tolerances.get('PF', 0.01)

    for row in artifact:
        comp = row.get('composition', '').strip()
        if comp not in ref_data:
            continue
        ref_n_e, ref_mu, ref_S = ref_data[comp]
        try:
            md_agent = float(row['m_d_star'])
            tau_agent = float(row['tau'])
            PF_agent = float(row['PF'])
        except (ValueError, KeyError):
            continue
        md_our = compute_md_star(ref_n_e, ref_S)
        tau_our = compute_tau(ref_mu, md_our)
        PF_our = compute_PF(ref_n_e, ref_mu, ref_S)
        rel_md = abs(md_agent - md_our) / (abs(md_our) + 1e-12)
        rel_tau = abs(tau_agent - tau_our) / (abs(tau_our) + 1e-12)
        rel_PF = abs(PF_agent - PF_our) / (abs(PF_our) + 1e-12)
        def qscore(re, tol):
            if re <= tol:
                return 1.0
            return max(0.0, 1.0 - (re - tol) / tol)
        row_score = (qscore(rel_md, tol_md) + qscore(rel_tau, tol_tau) + qscore(rel_PF, tol_PF)) / 3.0
        score += row_score
        rows += 1

    if rows == 0:
        return 0.0
    return score / rows


# === block: score_1 (check id='step_02_trend') ===
def score_1(artifact, step, ctx):
    tau_map = {}
    for row in artifact:
        try:
            comp = row['composition'].strip()
            tau_map[comp] = float(row['tau'])
        except (ValueError, KeyError):
            continue
    if 'Sr' not in tau_map:
        return 0.0
    tau_sr = tau_map['Sr']
    for comp, t in tau_map.items():
        if comp != 'Sr' and t >= tau_sr - 1e-6:
            return 0.0
    return 1.0


_SCORERS = {
    'step_01_recompute': score_0,
    'step_02_trend': score_1,
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
