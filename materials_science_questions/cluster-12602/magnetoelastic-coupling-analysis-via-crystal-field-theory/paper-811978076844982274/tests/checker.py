import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve
from collections import OrderedDict


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
        # ---- helper to solve A-phase equations at a given t (t>0) ----
        def _solve_A(t, params, guess=(0.5, 0.5)):
            k, c, l, m = params['k'], params['c'], params['l'], params['m']
            def eom(vars):
                sigma, eps = vars
                y1 = sigma * (m - (1.0 + k * eps))
                y2 = l * eps
                exp2 = np.exp(y2 / t)
                ch = np.cosh(y1 / t)
                sh = np.sinh(y1 / t)
                denom = 2.0 * exp2 * ch + 1.0
                sigma_eq = 2.0 * exp2 * sh / denom - sigma
                eps_eq = (1.0 / (2.0 * c)) * (4.0 * l * exp2 * ch / denom - sigma**2 * k) - eps
                return [sigma_eq, eps_eq]
            sol = fsolve(eom, guess, xtol=1e-12, maxfev=1000)
            sigma, eps = sol
            y1 = sigma * (m - (1.0 + k * eps))
            y2 = l * eps
            # compute f_A via eq (7) with sigma1=-sigma, sigma2=sigma, Q1=Q2 from (15)
            exp2 = np.exp(y2 / t)
            ch = np.cosh(y1 / t)
            sh = np.sinh(y1 / t)
            denom = 2.0 * exp2 * ch + 1.0
            Q_val = 2.0 * exp2 * ch / denom
            # free energy densities: f_A from (7) with sigma1=-sigma2 and Q1=Q2=Q
            # note: -sigma1*sigma2*(1+k*eps) = - (-sigma)*sigma*(1+k*eps) = +sigma^2*(1+k*eps)
            term1 = -t * np.log(denom)   # first sublattice
            term2 = -t * np.log(denom)   # second sublattice same
            f = (term1 + term2) + sigma**2 * (1.0 + k * eps) - l * eps * (2.0 * Q_val) - 0.5 * m * (sigma**2 + sigma**2) + 2.0 * y1 * sigma + 2.0 * y2 * Q_val + c * eps**2
            # Actually the free energy f from (7) is already per unit volume? But we just need consistency. However to match the paper's f, we need to use the full expression as given. I'll use the formula directly from eq (7) with sigma1, sigma2, Q1, Q2:
            sigma1 = -sigma
            sigma2 = sigma
            Q1 = Q_val
            Q2 = Q_val
            y3 = sigma1 * (1 + k * eps) + sigma2 * m
            y4 = l * eps
            f = -t * ( np.log(2.0*np.exp(y2/t)*np.cosh(y1/t)+1) + np.log(2.0*np.exp(y4/t)*np.cosh(y3/t)+1) ) - sigma1*sigma2*(1+k*eps) - l*eps*(Q1+Q2) - 0.5*m*(sigma1**2+sigma2**2) + y1*sigma1 + y3*sigma2 + y2*Q1 + y4*Q2 + c*eps**2
            return {'sigma': abs(sigma), 'epsilon': eps, 'f': f}

        # ---- helper to solve F-phase at t>0 ----
        def _solve_F(t, params, guess=(0.5, 0.5)):
            k, c, l, m = params['k'], params['c'], params['l'], params['m']
            def eom(vars):
                sigma, eps = vars
                y1 = sigma * (m + 1.0 + k * eps)
                y2 = l * eps
                exp2 = np.exp(y2 / t)
                ch = np.cosh(y1 / t)
                sh = np.sinh(y1 / t)
                denom = 2.0 * exp2 * ch + 1.0
                sigma_eq = 2.0 * exp2 * sh / denom - sigma
                eps_eq = (1.0 / (2.0 * c)) * (4.0 * l * exp2 * ch / denom + sigma**2 * k) - eps
                return [sigma_eq, eps_eq]
            sol = fsolve(eom, guess, xtol=1e-12, maxfev=1000)
            sigma, eps = sol
            y1 = sigma * (m + 1.0 + k * eps)
            y2 = l * eps
            Q_val = 2.0 * np.exp(y2/t) * np.cosh(y1/t) / (2.0*np.exp(y2/t)*np.cosh(y1/t) + 1.0)
            sigma1 = sigma
            sigma2 = sigma
            Q1 = Q_val
            Q2 = Q_val
            y3 = sigma1 * (1 + k * eps) + sigma2 * m
            y4 = l * eps
            f = -t * ( np.log(2.0*np.exp(y2/t)*np.cosh(y1/t)+1) + np.log(2.0*np.exp(y4/t)*np.cosh(y3/t)+1) ) - sigma1*sigma2*(1+k*eps) - l*eps*(Q1+Q2) - 0.5*m*(sigma1**2+sigma2**2) + y1*sigma1 + y3*sigma2 + y2*Q1 + y4*Q2 + c*eps**2
            return {'sigma': sigma, 'epsilon': eps, 'f': f}

        # ---- analytic T=0 solutions ----
        params = {'k': -1.1, 'c': 1.0, 'l': 1.0, 'm': 2.0}
        epsilon_A0 = (params['l'] - params['k']/2.0) / params['c']  # 1.55
        sigma_A0 = 1.0
        f_A0 = 1.0 - params['m'] - (2*params['l'] - params['k'])**2 / (4*params['c'])
        epsilon_F0 = (params['l'] + params['k']/2.0) / params['c']  # 0.45
        sigma_F0 = 1.0
        f_F0 = -1.0 - params['m'] - (2*params['l'] + params['k'])**2 / (4*params['c'])

        probe_ts = [0.0, 0.5, 1.0, 1.3, 1.5, 2.0]
        gold = {}
        for t in probe_ts:
            if t == 0.0:
                gold[t] = {
                    'sigma_A': sigma_A0, 'epsilon_A': epsilon_A0, 'f_A': f_A0,
                    'sigma_F': sigma_F0, 'epsilon_F': epsilon_F0, 'f_F': f_F0
                }
            else:
                solA = _solve_A(t, params)
                solF = _solve_F(t, params)
                gold[t] = {
                    'sigma_A': solA['sigma'], 'epsilon_A': solA['epsilon'], 'f_A': solA['f'],
                    'sigma_F': solF['sigma'], 'epsilon_F': solF['epsilon'], 'f_F': solF['f']
                }
        return {'gold': gold, 'params': params}


# === block: score_0 (check id='check_free_energy_rmse') ===
def score_0(artifact, step, ctx):
        from scipy.interpolate import interp1d
        from scipy.optimize import fsolve
        import numpy as np

        k = -1.1
        c = 1.0
        l = 1.0
        m = 2.0

        def safe_logcosh(x):
            ax = np.abs(x)
            return ax + np.log1p(np.exp(-2*ax)) - np.log(2)

        def f_system(z, t, phase):
            sigma, eps = z
            if sigma < 0:
                sigma = 0.0
            if t == 0:
                return [0.0, 0.0]
            a = l * eps / t
            if phase == 'A':
                b = sigma * (m - (1 + k*eps)) / t
            else:
                b = sigma * (m + 1 + k*eps) / t
            logcosh_b = safe_logcosh(b)
            logX = np.log(2) + a + logcosh_b
            tanh_b = np.tanh(b)
            if logX > 0:
                sigma_eq = tanh_b / (1.0 + np.exp(-logX))
            else:
                sigma_eq = np.exp(logX) * tanh_b / (1.0 + np.exp(logX))
            tmp = 1.0 / (1.0 + np.exp(-logX))
            term1 = 2.0 * l * tmp
            if phase == 'A':
                eps_eq = (term1 - sigma**2 * k) / (2.0 * c)
            else:
                eps_eq = (term1 + sigma**2 * k) / (2.0 * c)
            return [sigma_eq - sigma, eps_eq - eps]

        def compute_f(sigma, eps, t, phase):
            if t == 0:
                if phase == 'A':
                    return 1.0 - m - (2*l - k)**2 / (4*c)
                else:
                    return -1.0 - m - (2*l + k)**2 / (4*c)
            sigma1 = sigma if phase == 'F' else sigma
            sigma2 = sigma if phase == 'F' else -sigma
            y2 = l * eps
            y4 = y2
            y1 = sigma2 * (1 + k*eps) + sigma1 * m
            y3 = sigma1 * (1 + k*eps) + sigma2 * m
            a2 = y2 / t
            a4 = y4 / t
            b1 = y1 / t
            b3 = y3 / t
            logcosh1 = safe_logcosh(b1)
            logX1 = np.log(2) + a2 + logcosh1
            X1 = np.exp(logX1)
            Z1 = X1 + 1
            Q1 = X1 / Z1
            logcosh2 = safe_logcosh(b3)
            logX2 = np.log(2) + a4 + logcosh2
            X2 = np.exp(logX2)
            Z2 = X2 + 1
            Q2 = X2 / Z2
            term_log = t * (np.log(Z1) + np.log(Z2))
            f = -term_log
            f += -sigma1 * sigma2 * (1 + k*eps)
            f += -l * eps * (Q1 + Q2)
            f += -0.5 * m * (sigma1**2 + sigma2**2)
            f += y1 * sigma1 + y3 * sigma2
            f += y2 * Q1 + y4 * Q2
            f += c * eps**2
            return f

        def solve_phase(phase, t_vals):
            if phase == 'A':
                eps0 = (4*l - k) / (2*c)
                sigma0 = 1.0
            else:
                eps0 = (4*l + k) / (2*c)
                sigma0 = 1.0
            results = {}
            prev = [sigma0, eps0]
            for t in sorted(t_vals):
                if t == 0.0:
                    sol = [sigma0, eps0]
                else:
                    try:
                        sol = fsolve(lambda z: f_system(z, t, phase), prev, xtol=1e-10, maxfev=5000)
                        if np.linalg.norm(f_system(sol, t, phase)) < 1e-6:
                            prev = sol
                    except Exception:
                        pass
                    sol = prev
                sigma, eps = sol
                f_val = compute_f(sigma, eps, t, phase)
                results[t] = {'sigma': abs(sigma), 'epsilon': eps, 'f': f_val}
            return results

        probe_ts = [0.0, 0.5, 1.0, 1.3, 1.5, 2.0]
        gold_A = solve_phase('A', probe_ts)
        gold_F = solve_phase('F', probe_ts)

        rows = artifact
        ts = np.array([float(r['t']) for r in rows])
        f_A = np.array([float(r['f_A']) for r in rows])
        f_F = np.array([float(r['f_F']) for r in rows])

        try:
            interp_A = interp1d(ts, f_A, kind='linear', fill_value='extrapolate')
            interp_F = interp1d(ts, f_F, kind='linear', fill_value='extrapolate')
        except Exception:
            return 0.0

        agent_f_A = interp_A(probe_ts)
        agent_f_F = interp_F(probe_ts)

        gold_f_A = np.array([gold_A[t]['f'] for t in probe_ts])
        gold_f_F = np.array([gold_F[t]['f'] for t in probe_ts])

        avg_mag = (np.mean(np.abs(gold_f_A)) + np.mean(np.abs(gold_f_F))) / 2.0
        if avg_mag == 0:
            avg_mag = 1.0

        rmse_A = np.sqrt(np.mean((agent_f_A - gold_f_A)**2)) / avg_mag
        rmse_F = np.sqrt(np.mean((agent_f_F - gold_f_F)**2)) / avg_mag
        combined_rmse = (rmse_A + rmse_F) / 2.0

        tol = 0.02
        if combined_rmse <= tol:
            score = 1.0
        else:
            decay_max = 0.2
            score = max(0.0, 1.0 - (combined_rmse - tol) / (decay_max - tol))

        return score


# === block: score_1 (check id='check_transition_crossing') ===
def score_1(artifact, step, ctx):
        t_range = [1.2, 1.4]
        rows = artifact
        ts = [float(r['t']) for r in rows]
        f_A = [float(r['f_A']) for r in rows]
        f_F = [float(r['f_F']) for r in rows]
        # find any t where f_F < f_A within range
        crossing_found = False
        for i, t in enumerate(ts):
            if t >= t_range[0] and t <= t_range[1]:
                if f_F[i] < f_A[i]:
                    crossing_found = True
                    break
        # bonus: also check that before the crossing (say t<1.2) f_A < f_F (A stable)
        # but not strictly required; existence of crossing in window is enough.
        return 1.0 if crossing_found else 0.0


_SCORERS = {
    'check_free_energy_rmse': score_0,
    'check_transition_crossing': score_1,
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
