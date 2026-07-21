import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve
import math


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


# === block: score_0 (check id='step02_recompute_magnetization') ===
def score_0(artifact, step, ctx):
    tol_M = step.get('tolerance_config', {}).get('M_over_2muB_abs_tol', 0.02)
    A1 = 1.00
    A2 = 1.01
    n_total = 2.0

    # ---------- solver utilities ----------
    import warnings
    from scipy.optimize import root

    def z_from_n(n_val, A):
        if n_val <= 0:
            return 0.0
        return (n_val / A) ** (1.0 / 3.0)

    # --- symmetric (paramagnetic) solver ---
    def _residual_symmetric(p, U, J, A1, A2, n_total):
        v, z1, z2 = p
        n1 = 2.0 * A1 * z1**3
        n2 = 2.0 * A2 * z2**3
        f1 = v + U * A1 * z1**3 - z1**2
        f2 = v + U * A2 * z2**3 - z2**2
        f3 = n_total - (n1 + n2)
        return [f1, f2, f3]

    def solve_symmetric(U, J):
        # initial guess: half-filling
        v0 = 0.5
        n_guess = n_total / 4.0  # each of 4 orbitals gets same
        z1_0 = z_from_n(n_guess, A1)
        z2_0 = z_from_n(n_guess, A2)
        init = [v0, z1_0, z2_0]
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            sol = root(lambda p: _residual_symmetric(p, U, J, A1, A2, n_total),
                       init, method='hybr', options={'maxfev': 2000, 'xtol': 1e-12})
            if not sol.success:
                sol = root(lambda p: _residual_symmetric(p, U, J, A1, A2, n_total),
                           init, method='lm', options={'maxiter': 2000, 'xtol': 1e-12})
        if not sol.success:
            return None
        v_sol, z1, z2 = sol.x
        n1p = A1 * z1**3
        n1m = n1p
        n2p = A2 * z2**3
        n2m = n2p
        n1p = max(0.0, n1p)
        n1m = max(0.0, n1m)
        n2p = max(0.0, n2p)
        n2m = max(0.0, n2m)
        M = (n1p - n1m + n2p - n2m) / 2.0
        sum_sq = n1p**2 + n1m**2 + n2p**2 + n2m**2
        cross = (n1p - n1m) * (n2p - n2m)
        u = U * n_total**2 / 2.0 + 0.6 * v_sol * n_total + (U/10.0) * sum_sq + (2.0*J/5.0) * cross
        return {'M_over_2muB': M, 'u': u, 'v': v_sol}

    # --- full (magnetized) solver ---
    def _residual_full(p, U, J, A1, A2, n_total):
        v, z1p, z1m, z2p, z2m = p
        n1p = A1 * z1p**3
        n1m = A1 * z1m**3
        n2p = A2 * z2p**3
        n2m = A2 * z2m**3
        f1 = v + U * n1p + 2.0 * J * (n2p - n2m) - z1p**2
        f2 = v + U * n1m + 2.0 * J * (n2m - n2p) - z1m**2
        f3 = v + U * n2p + 2.0 * J * (n1p - n1m) - z2p**2
        f4 = v + U * n2m + 2.0 * J * (n1m - n1p) - z2m**2
        f5 = n_total - (n1p + n1m + n2p + n2m)
        return [f1, f2, f3, f4, f5]

    def solve_full(U, J, guess_n1p, guess_n1m, guess_n2p, guess_n2m):
        z1p0 = z_from_n(guess_n1p, A1)
        z1m0 = z_from_n(guess_n1m, A1)
        z2p0 = z_from_n(guess_n2p, A2)
        z2m0 = z_from_n(guess_n2m, A2)
        v0 = 0.5
        init = [v0, z1p0, z1m0, z2p0, z2m0]
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            sol = root(lambda p: _residual_full(p, U, J, A1, A2, n_total),
                       init, method='hybr', options={'maxfev': 2000, 'xtol': 1e-12})
            if not sol.success:
                sol = root(lambda p: _residual_full(p, U, J, A1, A2, n_total),
                           init, method='lm', options={'maxiter': 2000, 'xtol': 1e-12})
        if not sol.success:
            return None
        v_sol, z1p, z1m, z2p, z2m = sol.x
        n1p = A1 * z1p**3
        n1m = A1 * z1m**3
        n2p = A2 * z2p**3
        n2m = A2 * z2m**3
        n1p = max(0.0, n1p)
        n1m = max(0.0, n1m)
        n2p = max(0.0, n2p)
        n2m = max(0.0, n2m)
        M = (n1p - n1m + n2p - n2m) / 2.0
        sum_sq = n1p**2 + n1m**2 + n2p**2 + n2m**2
        cross = (n1p - n1m) * (n2p - n2m)
        u = U * n_total**2 / 2.0 + 0.6 * v_sol * n_total + (U/10.0) * sum_sq + (2.0*J/5.0) * cross
        return {'M_over_2muB': M, 'u': u, 'v': v_sol}

    def get_ref(U, J, cache):
        key = (round(U, 8), round(J, 8))
        if key in cache:
            return cache[key]
        # magnetized: try several guesses
        fm = None
        guesses = [
            (1.0, 0.0, 1.0, 0.0),   # full polarization
            (0.8, 0.2, 0.8, 0.2),
            (0.7, 0.3, 0.7, 0.3),
            (0.6, 0.4, 0.6, 0.4),
        ]
        for g in guesses:
            fm = solve_full(U, J, *g)
            if fm is not None:
                break
        # paramagnetic: use symmetric solver
        pm = solve_symmetric(U, J)
        if pm is None:
            # fallback to full solver with equal guess
            pm = solve_full(U, J, 0.5, 0.5, 0.5, 0.5)
        ref = {'mag': fm, 'unmag': pm}
        cache[key] = ref
        return ref

    rows = artifact   # artifact is the loaded CSV as list of dicts
    cache = {}
    n_pass_M = 0
    n_pass_order = 0
    n_rows = len(rows)
    if n_rows == 0:
        return 0.0

    rows_data = []
    for r in rows:
        try:
            U_val = float(r['U'])
            J_val = float(r['J'])
            M_agent = float(r['M_over_2muB'])
            u_mag_agent = float(r['u_magnetized'])
            u_unmag_agent = float(r['u_unmagnetized'])
            rows_data.append((U_val, J_val, M_agent, u_mag_agent, u_unmag_agent))
        except Exception:
            continue

    n_rows = len(rows_data)
    if n_rows == 0:
        return 0.0

    # ------- per-row checks -------
    for U_val, J_val, M_agent, u_mag_agent, u_unmag_agent in rows_data:
        ref = get_ref(U_val, J_val, cache)
        if ref['mag'] is not None:
            M_ref = ref['mag']['M_over_2muB']
        else:
            M_ref = None
        if M_ref is not None and abs(M_agent - M_ref) <= tol_M:
            n_pass_M += 1
        # energy ordering (agent’s own values)
        if u_mag_agent < u_unmag_agent:
            n_pass_order += 1

    frac_M = n_pass_M / n_rows
    frac_order = n_pass_order / n_rows

    # ------- monotonic trends -------
    def check_monotonic_subset(rows_list, fixed_param, fixed_val, sort_param):
        subs = [(v[sort_param], v[2]) for v in rows_list if abs(v[fixed_param] - fixed_val) < 1e-8]
        if len(subs) < 2:
            return 1.0
        subs.sort(key=lambda x: x[0])
        M_vals = [x[1] for x in subs]
        violations = 0
        for i in range(1, len(M_vals)):
            if M_vals[i] < M_vals[i-1] - 1e-9:
                violations += 1
        return 1.0 - violations / (len(M_vals) - 1)

    # sweep1: J=0.1, U varies
    frac1 = check_monotonic_subset(rows_data, 1, 0.1, 0)   # fixed_param index: 0=U,1=J
    # sweep2: U=0.3, J varies
    frac2 = check_monotonic_subset(rows_data, 0, 0.3, 1)
    monotonic_score = 0.5 * frac1 + 0.5 * frac2

    trend_score = 0.5 * frac_order + 0.5 * monotonic_score
    final = 0.7 * frac_M + 0.3 * trend_score
    return max(0.0, min(1.0, final))


_SCORERS = {
    'step02_recompute_magnetization': score_0,
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
