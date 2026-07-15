import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import minimize
import csv, json, os


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
    R = 8.314
    delta_u = {'ZnS': -16e3, 'ZnSe': -25e3, 'ZnTe': 37e3}
    deform = {
        'ZnS': {'u_Cd': 24.983e3, 'u_O': 58.911e3, 'u_104Cd': 58.6102e3, 'u_4O10Cd': 57.243e3},
        'ZnSe': {'u_Cd': 6.225e3, 'u_O': 77.721e3, 'u_104Cd': 97.604e3, 'u_4O10Cd': 101.656e3},
        'ZnTe': {'u_Cd': 6.063e3, 'u_O': 162.03e3, 'u_104Cd': 137.02e3, 'u_4O10Cd': 389.95e3}
    }
    comp = {'ZnS': {'y': 5e-4}, 'ZnSe': {'y': 3e-4}, 'ZnTe': {'y': 2e-3}}
    for m in comp:
        comp[m]['x'] = 2.5 * comp[m]['y']
    temp_range = np.arange(273, 1074, 10)

    def free_energy(alpha_beta, matrix, T):
        alpha, beta = alpha_beta
        y = comp[matrix]['y']
        x = comp[matrix]['x']
        d = deform[matrix]
        delta = delta_u[matrix]
        uB = delta * (alpha + beta) * (1 - x) * y
        uIS = (1 - alpha - beta)*y*d['u_O'] + (x - 2.5*alpha*y - 4*beta*y)*d['u_Cd'] + 0.25*alpha*y*d['u_4O10Cd'] + beta*y*d['u_104Cd']
        eps = 1e-12
        term1 = (1-alpha)*y * np.log(np.clip((1-alpha)*y / (1 - alpha*y), eps, 1-eps))
        term2 = (1-y) * np.log(np.clip((1-y)/(1 - alpha*y), eps, 1-eps))
        v = x - 2.5*alpha*y - 4*beta*y
        denom = 1 - 2.5*alpha*y - 4*beta*y
        if denom <= 0:
            term3 = term4 = 0.0
        else:
            term3 = v * np.log(np.clip(v / denom, eps, 1-eps))
            term4 = (1 - x) * np.log(np.clip((1 - x) / denom, eps, 1-eps))
        term5 = (1 - alpha - beta)*y * np.log(np.clip((1-alpha-beta)/(1-alpha), eps, 1-eps))
        term6 = beta*y * np.log(np.clip(beta/(1-alpha), eps, 1-eps))
        term7 = (1/10)*alpha*y * np.log(np.clip(27*alpha*y/20, eps, 1-eps))
        term8 = (2/27) * np.log(np.clip((20 - 27*alpha*y)/20, eps, 1-eps))
        s = -R * (term1 + term2 + term3 + term4 + term5 + term6 + term7 + term8)
        return uB + uIS - T * s

    gold_curves = {}
    bounds = [(0,1), (0,1)]
    for matrix in ['ZnS','ZnSe','ZnTe']:
        y = comp[matrix]['y']
        x = comp[matrix]['x']
        alphas = []
        betas = []
        for T in temp_range:
            cons_local = [{'type': 'ineq', 'fun': lambda ab: 1 - ab[0] - ab[1]},
                          {'type': 'ineq', 'fun': lambda ab, m=matrix: comp[m]['x'] - 2.5*comp[m]['y']*ab[0] - 4*comp[m]['y']*ab[1]}]
            res = minimize(free_energy, [0.5, 0.1], args=(matrix, T), method='SLSQP', bounds=bounds, constraints=cons_local, options={'maxiter':200, 'ftol':1e-12})
            if res.success:
                alpha, beta = res.x
            else:
                alpha, beta = 0.0, 0.0
            alpha = np.clip(alpha, 0, 1)
            beta = np.clip(beta, 0, 1)
            alphas.append(alpha)
            betas.append(beta)
        gold_curves[matrix] = {'T': temp_range.tolist(), 'alpha': alphas, 'beta': betas}

    gold_reductions = {}
    for matrix in ['ZnS','ZnSe','ZnTe']:
        d = deform[matrix]
        y = comp[matrix]['y']
        x = comp[matrix]['x']
        isolated = y*d['u_O'] + x*d['u_Cd']
        clustered = 0.25*y*d['u_4O10Cd']
        gold_reductions[matrix] = isolated / clustered

    ctx = {'gold_curves': gold_curves, 'gold_reductions': gold_reductions}
    return ctx


# === block: score_0 (check id='step_cop_zns') ===
def score_0(artifact, step, ctx):
    data = artifact
    gold = ctx['gold_curves']['ZnS']
    gold_T = np.array(gold['T'])
    gold_alpha = np.array(gold['alpha'])
    try:
        agent_T = np.array([float(row['T (K)']) for row in data])
        agent_alpha = np.array([float(row['alpha']) for row in data])
    except (KeyError, ValueError):
        return 0.0
    if len(agent_T) != len(gold_T) or not np.allclose(agent_T, gold_T, atol=1.0):
        return 0.0
    abs_tol = 0.02
    rel_tol = 0.05
    mask = np.isfinite(agent_alpha)
    if not np.all(mask):
        return 0.0
    diffs = np.abs(agent_alpha - gold_alpha)
    allowed = np.where(gold_alpha > 0.1, np.maximum(abs_tol, rel_tol * np.abs(gold_alpha)), abs_tol + 1e-6)
    score = np.mean(diffs <= allowed)
    return float(score)


# === block: score_1 (check id='step_cop_znse') ===
def score_1(artifact, step, ctx):
    data = artifact
    gold = ctx['gold_curves']['ZnSe']
    gold_T = np.array(gold['T'])
    gold_alpha = np.array(gold['alpha'])
    try:
        agent_T = np.array([float(row['T (K)']) for row in data])
        agent_alpha = np.array([float(row['alpha']) for row in data])
    except (KeyError, ValueError):
        return 0.0
    if len(agent_T) != len(gold_T) or not np.allclose(agent_T, gold_T, atol=1.0):
        return 0.0
    abs_tol = 0.02
    rel_tol = 0.05
    mask = np.isfinite(agent_alpha)
    if not np.all(mask):
        return 0.0
    diffs = np.abs(agent_alpha - gold_alpha)
    allowed = np.where(gold_alpha > 0.1, np.maximum(abs_tol, rel_tol * np.abs(gold_alpha)), abs_tol + 1e-6)
    score = np.mean(diffs <= allowed)
    return float(score)


# === block: score_2 (check id='step_cop_znte') ===
def score_2(artifact, step, ctx):
    data = artifact
    gold = ctx['gold_curves']['ZnTe']
    gold_T = np.array(gold['T'])
    gold_alpha = np.array(gold['alpha'])
    try:
        agent_T = np.array([float(row['T (K)']) for row in data])
        agent_alpha = np.array([float(row['alpha']) for row in data])
    except (KeyError, ValueError):
        return 0.0
    if len(agent_T) != len(gold_T) or not np.allclose(agent_T, gold_T, atol=1.0):
        return 0.0
    abs_tol = 0.02
    rel_tol = 0.05
    mask = np.isfinite(agent_alpha)
    if not np.all(mask):
        return 0.0
    diffs = np.abs(agent_alpha - gold_alpha)
    allowed = np.where(gold_alpha > 0.1, np.maximum(abs_tol, rel_tol * np.abs(gold_alpha)), abs_tol + 1e-6)
    score = np.mean(diffs <= allowed)
    return float(score)


# === block: score_3 (check id='step_strain_reduction') ===
def score_3(artifact, step, ctx):
    gold = ctx['gold_reductions']
    try:
        agent_factors = {}
        for row in artifact:
            m = row['matrix'].strip()
            agent_factors[m] = float(row['reduction_factor'])
    except (KeyError, ValueError):
        return 0.0
    if len(agent_factors) != 3:
        return 0.0
    tolerance = 0.1
    correct = sum(1 for m, gf in gold.items() if m in agent_factors and abs(agent_factors[m] - gf) <= tolerance)
    return correct / 3


_SCORERS = {
    'step_cop_zns': score_0,
    'step_cop_znse': score_1,
    'step_cop_znte': score_2,
    'step_strain_reduction': score_3,
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
