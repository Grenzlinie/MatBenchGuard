import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.integrate import solve_ivp


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
    mu1 = 129.1267       # MPa
    mu2 = 70.3011        # MPa
    v   = 12.4878        # MPa·s
    beta = 0.5666
    a0 = 24.0            # mm² (ASTM D638 Type 4 nominal)

    def compute_expected_force(condition, t_agent, kind='stress_relaxation'):
        """Solve ODE and return force (N) at times t_agent (sorted)."""
        # Unpack parameters
        if kind == 'stress_relaxation':
            strain = condition['strain']
            rate   = condition['stretch_rate']
            t_ramp = strain / rate
            def lambda_t(t):
                return np.where(t < t_ramp, 1.0 + rate * t, 1.0 + strain)
            def dlambda_dt_t(t):
                return np.where(t < t_ramp, rate, 0.0)
        else:  # cyclic
            peak_strain = condition['peak_strain']
            strain_ratio = condition['strain_ratio']
            freq = condition['freq_hz']
            T = 1.0 / freq
            delta = peak_strain * (1.0 - strain_ratio)   # = 0.06*(1-0.1)=0.054
            min_strain = peak_strain * strain_ratio      # = 0.006
            def lambda_t(t):
                t_mod = t % T
                # piecewise linear triangle
                frac = t_mod / (T/2)
                strain = np.where(frac <= 1.0,
                                  min_strain + 2*delta * (t_mod / T),
                                  min_strain + 2*delta * (1.0 - (t_mod - T/2) / (T/2)))
                return 1.0 + strain
            def dlambda_dt_t(t):
                t_mod = t % T
                return np.where(t_mod < T/2, 2*delta / T, -2*delta / T)

        # ODE system
        def dbdt(t, B):
            lam = lambda_t(t)
            dlam = dlambda_dt_t(t)
            if lam <= 0:
                lam = 1e-12
            sqrtB = np.sqrt(B) if B > 0 else 1e-6
            term1 = 2 * (mu1/(2*v))**(1/(2*beta-1))
            denom = 2*B*sqrtB + 1
            if denom <= 0:
                denom = 1e-12
            inside = ( (2 + B*sqrtB)/sqrtB - 9*B/denom )**((1-beta)/(2*beta-1))
            factor = (3*B/denom - B)
            return term1 * inside * factor + 2*B * dlam / lam

        # Solve ODE at agent's time points (must start at 0)
        t_span = (0.0, max(t_agent[-1], 1e-12))
        t_eval = t_agent.copy()
        sol = solve_ivp(dbdt, t_span, [1.0], t_eval=t_eval, method='RK45', rtol=1e-9, atol=1e-12)
        B_arr = sol.y[0]
        # Compute force
        lam_arr = lambda_t(t_agent)
        Tzz = mu1*(B_arr - 1.0/np.sqrt(B_arr)) + mu2*(lam_arr**2 - 1.0/lam_arr)
        force = a0 * Tzz / lam_arr
        return force

    ctx = {
        'mu1': mu1, 'mu2': mu2, 'v': v, 'beta': beta, 'a0': a0,
        'compute_expected_force': compute_expected_force
    }
    return ctx


# === block: score_0 (check id='step02_stress_relaxation') ===
def score_0(artifact, step, ctx):
    import csv, io, os
    conditions = step.get('conditions', [])
    artifact_rows = artifact  # list of dicts with keys test_id, time_s, force_N
    if not artifact_rows:
        return 0.0
    # Group rows by test_id
    groups = {}
    for row in artifact_rows:
        tid = row['test_id']
        try:
            t = float(row['time_s'])
            f = float(row['force_N'])
        except (ValueError, KeyError):
            continue
        groups.setdefault(tid, []).append((t, f))
    scores = []
    # Robust recomputation function (replaces ctx['compute_expected_force'])
    def compute_expected_force_robust(cond, t_agent):
        mu1 = ctx['mu1']
        mu2 = ctx['mu2']
        v   = ctx['v']
        beta = ctx['beta']
        a0  = ctx['a0']  # mm^2
        strain = cond['strain']
        rate   = cond['stretch_rate']
        t_ramp = strain / rate
        # Piecewise stretch and its derivative
        def lambda_t(t):
            return np.where(t < t_ramp, 1.0 + rate * t, 1.0 + strain)
        def dlambda_dt_t(t):
            return np.where(t < t_ramp, rate, 0.0)
        # ODE right‑hand side with safety clamps
        def dbdt(t, B):
            lam = lambda_t(t)
            dlam = dlambda_dt_t(t)
            B = max(B, 1e-12)          # keep B positive
            sqrtB = np.sqrt(B)
            denom = 2.0 * B * sqrtB + 1.0
            if denom <= 1e-30:
                denom = 1e-30
            term1 = 2.0 * (mu1 / (2.0 * v)) ** (1.0 / (2.0 * beta - 1.0))
            inside_base = (2.0 + B * sqrtB) / sqrtB - 9.0 * B / denom
            inside_base = max(inside_base, 1e-30)  # avoid negative base for fractional exponent
            inside = inside_base ** ((1.0 - beta) / (2.0 * beta - 1.0))
            factor = 3.0 * B / denom - B
            ret = term1 * inside * factor + 2.0 * B * dlam / lam
            # Cap extremely large derivatives to prevent overflow
            max_dbdt = 1e6
            if abs(ret) > max_dbdt:
                ret = np.sign(ret) * max_dbdt
            return ret
        # Integrate with a stiff‑tolerant method
        t_max = max(t_agent[-1], 1e-6)
        try:
            sol = solve_ivp(dbdt, [0.0, t_max], [1.0], method='Radau',
                            t_eval=t_agent, rtol=1e-9, atol=1e-12, max_step=0.1)
            B_arr = sol.y[0]
        except Exception:
            return None
        # Compute axial force
        lam_arr = lambda_t(t_agent)
        Tzz = mu1 * (B_arr - 1.0 / np.sqrt(B_arr)) + mu2 * (lam_arr**2 - 1.0 / lam_arr)
        force = a0 * Tzz / lam_arr
        return force

    for cond in conditions:
        tid = cond['test_id']
        if tid not in groups:
            scores.append(0.0)
            continue
        pts = sorted(groups[tid], key=lambda x: x[0])
        t_agent = np.array([p[0] for p in pts])
        f_agent = np.array([p[1] for p in pts])
        # Compute expected force using the robust integrator
        f_expected = compute_expected_force_robust(cond, t_agent)
        if f_expected is None:
            scores.append(0.0)
            continue
        # Relative error scaled by max absolute expected force (avoid division by zero)
        max_abs = max(np.max(np.abs(f_expected)), 1e-9)
        rel_err = np.abs(f_agent - f_expected) / max_abs
        median_err = np.median(rel_err)
        tol = step.get('tolerance_rel', 0.03)
        score_cond = max(0.0, min(1.0, 1.0 - median_err / tol))
        scores.append(score_cond)
    return float(np.mean(scores)) if scores else 0.0


# === block: score_1 (check id='step03_cyclic_loading') ===
def score_1(artifact, step, ctx):
    import csv
    cyclic_params = step.get('cyclic_params', {})
    artifact_rows = artifact  # list of dicts with time_s, force_N
    if not artifact_rows:
        return 0.0
    pts = []
    for row in artifact_rows:
        try:
            t = float(row['time_s'])
            f = float(row['force_N'])
            pts.append((t, f))
        except (ValueError, KeyError):
            continue
    if not pts:
        return 0.0
    pts.sort(key=lambda x: x[0])
    t_agent = np.array([p[0] for p in pts])
    f_agent = np.array([p[1] for p in pts])
    try:
        f_expected = ctx['compute_expected_force'](cyclic_params, t_agent, kind='cyclic')
    except Exception:
        return 0.0
    max_abs = max(np.max(np.abs(f_expected)), 1e-9)
    rel_err = np.abs(f_agent - f_expected) / max_abs
    median_err = np.median(rel_err)
    tol = step.get('tolerance_rel', 0.05)
    score = max(0.0, min(1.0, 1.0 - median_err / tol))
    return float(score)


_SCORERS = {
    'step02_stress_relaxation': score_0,
    'step03_cyclic_loading': score_1,
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
