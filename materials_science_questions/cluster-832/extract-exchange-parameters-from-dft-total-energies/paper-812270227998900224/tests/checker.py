import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import fsolve

# Table I coefficients (i=1..22)
table1 = [
 (24, 16, 0, 8, 4, 0, 2, 2, 0),
 (-24, 16, 0, -8, -4, 0, 2, 2, 0),
 (48, 64, 0, 16, 2, 0, 0, 2, 0),
 (-48, 64, 0, -16, -2, 0, 0, 2, 0),
 (0, 32, 0, 0, 0, 0, -2, 2, 0),
 (0, 64, 0, 0, 0, 0, 0, 2, 0),
 (0, -32, -24, -4, 4, 8, 0, 2, 8),
 (0, -32, -24, 4, -4, 8, 0, 2, 8),
 (0, -72, -54, -12, 3, 4, 0, 1.5, 4),
 (0, -72, -54, 12, -3, 4, 0, 1.5, 4),
 (0, -32, -24, -8, 2, 2, 0, 1, 2),
 (0, -16, -12, -4, 2, 0, 0, 1, 0),
 (0, -32, -24, -8, 2, 0, 0, 2, 8),
 (0, -32, -24, 8, -2, 2, 0, 1, 2),
 (0, -16, -12, 4, -2, 0, 0, 1, 0),
 (0, -32, -24, 8, -2, 0, 0, 2, 8),
 (0, -8, -6, -4, 1, 0, 0, 0.5, 0),
 (0, -16, -12, -8, 1, 0, 0, 1.5, 4),
 (0, -8, -6, -4, 1, -4, 0, 1.5, 4),
 (0, -8, -6, 4, -1, 0, 0, 0.5, 0),
 (0, -16, -12, 8, -1, 0, 0, 1.5, 4),
 (0, -8, -6, 4, -1, -4, 0, 1.5, 4)
]

# Table II coefficients (j=1..27)
table2 = [
 (24, 16, 0, 8, 4, 0, 2, 2, 0),
 (24, -16, 0, 8, -4, 0, 2, 2, 0),
 (24, 32, 0, 8, 2, 0, 0, 2, 0),
 (24, -32, 0, 8, -2, 0, 0, 2, 0),
 (24, 0, 0, 8, 0, 0, 2, 0, 0),
 (24, 0, 0, 8, 0, 0, 0, 0, 0),
 (0, -32, -24, -4, 4, 8, 0, 2, 8),
 (0, 32, 24, -4, -4, 8, 0, 2, 8),
 (0, -96, -72, -16, 3, 4, 0, 1.5, 4),
 (0, 96, 72, -16, -3, 4, 0, 1.5, 4),
 (0, -64, -48, -16, 2, 2, 0, 1, 2),
 (0, 64, 48, -16, -2, 2, 0, 1, 2),
 (0, -32, -24, -8, 2, 0, 0, 1, 0),
 (0, -64, -48, -16, 2, 0, 0, 2, 8),
 (0, 32, 24, -8, -2, 0, 0, 1, 0),
 (0, 64, 48, -16, -2, 0, 0, 2, 8),
 (0, -32, -24, -16, 1, 0, 0, 0.5, 0),
 (0, -64, -48, -32, 1, 0, 0, 1.5, 4),
 (0, -32, -24, -16, 1, -4, 0, 1.5, 4),
 (0, 32, 24, -16, -1, 0, 0, 0.5, 0),
 (0, 64, 48, -32, -1, 0, 0, 1.5, 4),
 (0, 32, 24, -16, -1, -4, 0, 1.5, 4),
 (0, 0, 0, -32, 0, -2, 0, 1, 2),
 (0, 0, 0, -16, 0, 0, 0, 1, 0),
 (0, 0, 0, -16, 0, 0, 0, 2, 8),
 (0, 0, 0, -8, 0, -8, 0, 2, 8),
 (0, 0, 0, -4, 0, 0, 0, 0, 0)
]

def eq_residual(vars, j1p, j2p, j2, j3):
    K1, r = vars
    if K1 < 0:
        return [1e6, 1e6]  # discourage negative K1
    K1p = j1p * K1
    K2p = j2p * K1
    K2 = j2 * K1
    K3 = j3 * K1
    s1 = 0.0
    for (a,b,c,d,p,q,rr,u,v) in table1:
        term = (a*K1 + b*K2) + (c*K1 + d*K3)*r
        arg = p*K1 + q*K2 + rr*K3 + u*K1p + v*K2p
        s1 += term * np.exp(arg)
    s2 = 0.0
    for (a,b,c,d,p,q,rr,u,v) in table2:
        term = (a*K1 + b*K2) + (c*K1 + d*K3)*r
        arg = p*K1 + q*K2 + rr*K3 + u*K1p + v*K2p
        s2 += term * np.exp(arg)
    return [s1, s2]

def solve_one_point(j1p, j2p, j2, j3):
    """Return (Tc, mu1_over_lambda1) or (None,None) if solver fails."""
    try:
        sol = fsolve(eq_residual, [0.5, 0.5], args=(j1p, j2p, j2, j3), maxfev=2000, xtol=1e-12)
        K1, r = sol[0], sol[1]
        if K1 <= 0:
            return (0.0, r)  # Not physically meaningful, but for J1' far negative Tc=0
        Tc = 1.0 / K1
        return (Tc, r)
    except Exception:
        return (None, None)


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


# === block: score_0 (check id='parameter_scans') ===
def score_0(artifact, step, ctx):
    import csv
    import os
    import numpy as np
    from scipy.optimize import fsolve, brentq

    def solve_one_point_robust(j1p, j2p, j2, j3):
        """Return (Tc, mu1_over_lambda1) by solving A1*B2 - A2*B1 = 0 for K1."""
        def f(K1):
            if K1 <= 0:
                return 1e9
            K1p = j1p * K1
            K2p = j2p * K1
            K2v = j2 * K1
            K3v = j3 * K1
            A1 = 0.0; B1 = 0.0
            for (a,b,c,d,p,q,r,u,v) in table1:
                arg = p*K1 + q*K2v + r*K3v + u*K1p + v*K2p
                if arg > 100:
                    return 1e6
                e = np.exp(arg)
                A1 += (a*K1 + b*K2v) * e
                B1 += (c*K1 + d*K3v) * e
            A2 = 0.0; B2 = 0.0
            for (a,b,c,d,p,q,r,u,v) in table2:
                arg = p*K1 + q*K2v + r*K3v + u*K1p + v*K2p
                if arg > 100:
                    return 1e6
                e = np.exp(arg)
                A2 += (a*K1 + b*K2v) * e
                B2 += (c*K1 + d*K3v) * e
            return A1 * B2 - A2 * B1

        guesses = [2.0, 1.0, 3.0, 0.5, 0.2, 5.0]
        K1 = None
        for guess in guesses:
            try:
                sol = fsolve(lambda x: f(x[0]), [guess], maxfev=2000, xtol=1e-12)
                if sol[0] > 0 and abs(f(sol[0])) < 1e-6:
                    K1 = sol[0]
                    break
            except Exception:
                continue
        if K1 is None:
            # fallback: grid search for sign change and Brent
            ks = np.logspace(-1, 1, 200)
            fvals = [f(k) for k in ks]
            signs = np.sign(fvals)
            change = np.where(np.diff(signs))[0]
            if len(change) == 0:
                return (None, None)
            a, b = ks[change[0]], ks[change[0]+1]
            try:
                K1 = brentq(lambda x: f(x), a, b, xtol=1e-12)
            except Exception:
                return (None, None)
        if K1 is None or K1 <= 0:
            return (None, None)
        # compute r = -A1/B1
        K1p = j1p * K1
        K2p = j2p * K1
        K2v = j2 * K1
        K3v = j3 * K1
        A1 = 0.0; B1 = 0.0
        for (a,b,c,d,p,q,r,u,v) in table1:
            arg = p*K1 + q*K2v + r*K3v + u*K1p + v*K2p
            e = np.exp(arg)
            A1 += (a*K1 + b*K2v) * e
            B1 += (c*K1 + d*K3v) * e
        r_val = -A1 / B1 if abs(B1) > 1e-12 else float('nan')
        Tc = 1.0 / K1
        return (Tc, r_val)

    csv_path = os.path.join('/app/outputs', step.get('output_file', 'parameter_scans.csv'))
    if artifact is None:
        return 0.0

    check_points = [
        ('J1′', -1.5, -1.5, 0.0, 0.0, 0.0),
        ('J1′', -1.0, -1.0, 0.0, 0.0, 0.0),
        ('J1′', -0.5, -0.5, 0.0, 0.0, 0.0),
        ('J1′', 0.0, 0.0, 0.0, 0.0, 0.0),
        ('J1′', 0.5, 0.5, 0.0, 0.0, 0.0),
        ('J1′', 1.0, 1.0, 0.0, 0.0, 0.0),
        ('J2′', -2.0, 0.0, -2.0, 0.0, 0.0),
        ('J2′', -1.0, 0.0, -1.0, 0.0, 0.0),
        ('J2′', 0.0, 0.0, 0.0, 0.0, 0.0),
        ('J2′', 1.0, 0.0, 1.0, 0.0, 0.0),
        ('J2′', 2.0, 0.0, 2.0, 0.0, 0.0),
        ('J2', -0.8, 0.0, 0.0, -0.8, 0.0),
        ('J2', -0.4, 0.0, 0.0, -0.4, 0.0),
        ('J2', 0.0, 0.0, 0.0, 0.0, 0.0),
        ('J2', 0.4, 0.0, 0.0, 0.4, 0.0),
        ('J2', 0.8, 0.0, 0.0, 0.8, 0.0),
        ('J3', -2.0, 0.0, 0.0, 0.0, -2.0),
        ('J3', -1.0, 0.0, 0.0, 0.0, -1.0),
        ('J3', 0.0, 0.0, 0.0, 0.0, 0.0),
        ('J3', 1.0, 0.0, 0.0, 0.0, 1.0),
        ('J3', 2.0, 0.0, 0.0, 0.0, 2.0),
    ]

    tol_tc_rel = 0.03
    tol_r_rel = 0.05

    scores = []
    for param_str, val, j1p, j2p, j2, j3 in check_points:
        rows = [r for r in artifact if r.get('parameter') == param_str and abs(float(r.get('parameter_value',0)) - val) < 1e-3]
        if not rows:
            scores.append(0.0)
            continue
        row = rows[0]
        agent_tc = float(row.get('kB_Tc_over_J1', 0))
        agent_r = float(row.get('mu1_over_lambda1', 0))

        exp_tc, exp_r = solve_one_point_robust(j1p, j2p, j2, j3)
        if exp_tc is None:
            scores.append(0.0)
            continue

        if abs(exp_tc) < 1e-6:
            tc_err = 0.0 if abs(agent_tc) < 1e-6 else 1.0
            tc_score = 1.0 if tc_err == 0 else 0.0
        else:
            rel_err_tc = abs(agent_tc - exp_tc) / max(abs(exp_tc), 1e-6)
            tc_score = max(0.0, 1.0 - rel_err_tc / tol_tc_rel)

        if abs(exp_r) < 1e-6:
            r_err = 0.0 if abs(agent_r) < 1e-6 else 1.0
            r_score = 1.0 if r_err == 0 else 0.0
        else:
            rel_err_r = abs(agent_r - exp_r) / max(abs(exp_r), 1e-6)
            r_score = max(0.0, 1.0 - rel_err_r / tol_r_rel)

        scores.append(0.5 * tc_score + 0.5 * r_score)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='instability_point') ===
def score_1(artifact, step, ctx):
    import os, csv, numpy as np

    csv_path = os.path.join('/app/outputs', step.get('output_file', 'instability_point.csv'))
    if artifact is None:
        return 0.0
    row = artifact[0] if artifact else None
    if row is None:
        return 0.0

    agent_crit = float(row.get('critical_value', 0))

    # Recomputation of critical J1'/J1 via scan
    def find_critical():
        # scan from -1.95 to -1.75 in fine steps
        vals = np.arange(-1.95, -1.74, 0.001)
        for v in vals:
            Tc, r = solve_one_point(v, 0, 0, 0)
            if Tc is not None and Tc <= 1e-6:
                return v
        return -1.85  # fallback
    expected_crit = find_critical()

    # score by absolute difference
    diff = abs(agent_crit - expected_crit)
    if diff <= 0.04:
        score = 1.0
    elif diff <= 0.08:
        score = 0.5
    elif diff <= 0.15:
        score = 0.2
    else:
        score = 0.0
    return score


_SCORERS = {
    'parameter_scans': score_0,
    'instability_point': score_1,
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
