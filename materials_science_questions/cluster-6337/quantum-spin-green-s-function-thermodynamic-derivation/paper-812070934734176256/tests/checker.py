import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy import integrate


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
    # Compute coefficient arrays for p=1.5 and p=2.5
    N = 10000
    def _compute_coeffs(p, N):
        n_arr = np.arange(1, N+1)
        n_even = 2 * n_arr
        f_even_factors = 4.0 / (n_even ** p)
        n_odd = 2 * n_arr - 1
        g_odd_factors = 2.0 / (n_odd ** p)
        alpha = np.sum(g_odd_factors)
        return {
            'n_even': n_even,
            'f_even_factors': f_even_factors,
            'n_odd': n_odd,
            'g_odd_factors': g_odd_factors,
            'alpha': alpha
        }
    ctx = {
        'p15': _compute_coeffs(1.5, N),
        'p25': _compute_coeffs(2.5, N),
        'sigma_a': 0.5,
        'N': N
    }
    return ctx


# === block: score_0 (check id='dispersion_accuracy') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows or 'k' not in rows[0] or 'omega_k' not in rows[0]:
        return 0.0
    ks = np.array([float(r['k']) for r in rows])
    omega_agent = np.array([float(r['omega_k']) for r in rows])
    coeffs = ctx['p15']
    sigma_a = ctx['sigma_a']
    # helper functions
    def _f_k_vec(coeffs, k):
        c = np.cos(np.outer(coeffs['n_even'], k))
        c_sub = c - 1.0
        f = np.dot(coeffs['f_even_factors'], c_sub)
        return f
    def _g_k_vec(coeffs, k):
        c = np.cos(np.outer(coeffs['n_odd'], k))
        g = np.dot(coeffs['g_odd_factors'], c)
        return g
    alpha = coeffs['alpha']
    f = _f_k_vec(coeffs, ks)
    g = _g_k_vec(coeffs, ks)
    omega_ref = sigma_a * np.sqrt((alpha - f)**2 - g**2)
    rel_err = np.abs(omega_ref - omega_agent) / np.maximum(np.abs(omega_ref), 1e-12)
    pass_mask = rel_err <= 0.01
    score = np.mean(pass_mask)
    return float(score)


# === block: score_1 (check id='critical_p1.5') ===
def score_1(artifact, step, ctx):
    import scipy.integrate as integrate
    coeffs = ctx['p15']
    # single-k evaluation
    def _f_k_single(coeffs, k):
        c = np.cos(coeffs['n_even'] * k)
        return np.sum(coeffs['f_even_factors'] * (c - 1))
    def _g_k_single(coeffs, k):
        c = np.cos(coeffs['n_odd'] * k)
        return np.sum(coeffs['g_odd_factors'] * c)
    alpha = coeffs['alpha']
    def _integrand(k):
        f = _f_k_single(coeffs, k)
        g = _g_k_single(coeffs, k)
        denom = (alpha - f)**2 - g**2
        return (alpha - f) / denom
    I, _ = integrate.quad(_integrand, -np.pi, np.pi, limit=500)
    I_ref = (2/np.pi) * I
    agent_val = artifact['p1.5_TN_inverse']
    if I_ref == 0.0:
        return 1.0 if abs(agent_val) < 1e-12 else 0.0
    rel_err = abs(I_ref - agent_val) / I_ref
    if rel_err <= 0.05:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (rel_err - 0.05) / 0.1)
    return score


# === block: score_2 (check id='critical_p2.5') ===
def score_2(artifact, step, ctx):
    p25_sentinel = artifact.get('p2.5_TN_inverse', 0.0)
    p25_diverges = artifact.get('p2.5_diverges', False)
    if isinstance(p25_diverges, bool) and p25_diverges and p25_sentinel > 1e6:
        return 1.0
    return 0.0


_SCORERS = {
    'dispersion_accuracy': score_0,
    'critical_p1.5': score_1,
    'critical_p2.5': score_2,
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
