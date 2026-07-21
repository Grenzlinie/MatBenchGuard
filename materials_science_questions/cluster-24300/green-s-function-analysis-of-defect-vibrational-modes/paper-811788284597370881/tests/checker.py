import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import quad


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
    # No shared state needed; all gold is recomputed inline.
    return {}


# === block: score_0 (check id='step_03') ===
def score_0(artifact, step, ctx):
    # Scorer for zpl_quantities.json – recompute Debye-Van Hove integrals and compare.
    import os, json

    artifact_path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(artifact_path):
        return 0.0

    with open(artifact_path) as f:
        try:
            data = json.load(f)
        except Exception:
            return 0.0

    # Validate basic structure
    if not isinstance(data, dict) or 'results' not in data:
        return 0.0

    config = step.get('config', {})
    b_list = config.get('b_list', [-0.2, 0.0, 0.16])
    T_list = config.get('T_list', [0.0, 0.1, 0.5])
    atol = config.get('atol', 1e-6)
    # The approved plan states a relative tolerance of 1% (0.01).
    # Enforce that the effective rtol is not stricter than that to prevent unfair penalization.
    plan_rtol = 0.01
    config_rtol = config.get('rtol', plan_rtol)
    rtol = max(config_rtol, plan_rtol)
    eps = config.get('epsilon', 1e-14)
    int_limit = config.get('int_limit', 1.0)
    a2 = config.get('a2', 1.0)

    # ---------- model functions ----------
    def rho(om):
        if om <= 0 or om >= 1:
            return 0.0
        return (32.0 / np.pi) * om**4 * np.sqrt(1 - om**2)

    def imG(om):
        if om <= 0 or om >= 1:
            return 0.0
        return (np.pi / (2 * om)) * rho(om)

    def reG(om):
        return -2.0 - 8.0 * om**2 + 16.0 * om**4

    def nBose(om, T):
        if T == 0.0 or om <= 0:
            return 0.0
        return 1.0 / (np.exp(om / T) - 1.0)

    def D_func(om, b, T):
        g = reG(om) + 1j * imG(om)
        n = nBose(om, T)
        return g + 2j * n * imG(om)

    def D_tilde(om, b, T):
        D = D_func(om, b, T)
        return D / (1.0 - b * D)

    # integrands
    def integrand_SLabs(om, b, T):
        if om == 0:
            # limit is finite; approximate via tiny omega
            return integrand_SLabs(eps, b, T)
        dt = D_tilde(om, b, T)
        return (a2 / np.pi) * np.imag(dt) / (om * om)

    def integrand_SLlum(om, b, T):
        if om == 0:
            return integrand_SLlum(eps, b, T)
        dt = D_tilde(om, b, T)
        G = reG(om) + 1j * imG(om)
        factor = np.abs(1.0 - b * G)**2
        return (a2 / np.pi) * np.imag(dt * factor) / (om * om)

    def integrand_gamma(om, b, T):
        D = D_func(om, b, T)
        val = np.log(1.0 - b * D)
        return (1.0 / (2 * np.pi)) * val.real

    def integrand_delta_Q(om, b, T):
        D = D_func(om, b, T)
        val = np.log(1.0 - b * D)
        return -(1.0 / (2 * np.pi)) * val.imag

    # ---------- helper to integrate ----------
    def safe_integrate(func, b, T, lim_low, lim_high):
        res, _ = quad(func, lim_low, lim_high, args=(b, T), limit=200, epsabs=1e-12, epsrel=1e-10)
        return res

    # ---------- compute reference for one (b,T) ----------
    def compute_reference(b, T):
        # delta_L directly from D_tilde(0)
        dt0 = D_tilde(0.0, b, T)
        delta_L = (a2 / (2.0 * np.pi)) * dt0.real

        # integrals from eps to int_limit
        Sabs = safe_integrate(integrand_SLabs, b, T, eps, int_limit)
        Slum = safe_integrate(integrand_SLlum, b, T, eps, int_limit)
        gamma = safe_integrate(integrand_gamma, b, T, eps, int_limit)
        delta_Q = safe_integrate(integrand_delta_Q, b, T, eps, int_limit)

        return {
            'delta_L': delta_L,
            'S_L_absorption': Sabs,
            'S_L_luminescence': Slum,
            'gamma': gamma,
            'delta_Q': delta_Q
        }

    # ---------- score one quantity ----------
    def score_quantity(agent_val, ref_val, atol, rtol):
        if ref_val is None or agent_val is None:
            return 0.0
        error = abs(agent_val - ref_val)
        tol = atol + rtol * max(abs(agent_val), abs(ref_val))
        if error <= tol:
            return 1.0
        else:
            return 0.0

    # ---------- main comparison ----------
    results = data.get('results', [])
    if not isinstance(results, list):
        return 0.0

    # Build lookup by (b,T)
    lookup = {}
    for r in results:
        if not isinstance(r, dict):
            continue
        b_val = float(r.get('b', None))
        T_val = float(r.get('T', None))
        key = (b_val, T_val)
        lookup[key] = r

    total_score = 0.0
    count = 0
    quantities = ['delta_L', 'S_L_absorption', 'S_L_luminescence', 'gamma', 'delta_Q']

    for b in b_list:
        for T in T_list:
            key = (float(b), float(T))
            if key not in lookup:
                # missing pair => score 0 for all quantities of this pair
                total_score += 0.0 * len(quantities)
                count += len(quantities)
                continue
            agent_entry = lookup[key]
            ref = compute_reference(b, T)
            for q in quantities:
                agent_val = agent_entry.get(q)
                ref_val = ref.get(q)
                s = score_quantity(agent_val, ref_val, atol, rtol)
                total_score += s
                count += 1

    if count == 0:
        return 0.0

    avg_score = total_score / count
    return float(np.clip(avg_score, 0.0, 1.0))


_SCORERS = {
    'step_03': score_0,
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
