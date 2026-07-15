import os
import json
import csv

# === author imports / helpers ===
import os, csv, json, math


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
    import os, csv, math

    def load_csv(path):
        if not os.path.exists(path):
            return None
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)

    rec = {'recomputed_A': None, 'recomputed_thetaE': None, 'recomputed_theta_inf': None}
    try:
        csv_path = os.path.join(outputs_dir, 'step_01_cv_ch.csv')
        rows = load_csv(csv_path)
        if rows is None:
            return rec
        # Check required columns
        if 'T' not in rows[0] or 'Cv' not in rows[0]:
            return rec
        # Filter T>=650 and collect data
        x_vals, y_vals = [], []
        R = 8.314
        for r in rows:
            try:
                T = float(r['T'])
                Cv = float(r['Cv'])
            except (ValueError, KeyError):
                continue
            if T < 650.0:
                continue
            x = T ** (-3)
            y = (Cv - 9*R) / T
            x_vals.append(x)
            y_vals.append(y)
        if len(x_vals) < 2:
            return rec
        # Closed-form OLS
        n = len(x_vals)
        sum_x = math.fsum(x_vals)
        sum_y = math.fsum(y_vals)
        sum_xx = math.fsum([x*x for x in x_vals])
        sum_xy = math.fsum([x_vals[i]*y_vals[i] for i in range(n)])
        denom = n*sum_xx - sum_x*sum_x
        if abs(denom) < 1e-30:
            return rec
        slope = (n*sum_xy - sum_x*sum_y) / denom
        intercept = (sum_xx*sum_y - sum_x*sum_xy) / denom
        A = intercept
        # theta_inf from slope: slope = -(9R/20) * theta_inf**2
        if slope >= 0:
            return rec  # physically impossible (should be negative)
        theta_inf_sq = -slope * (20.0 / (9*R))
        if theta_inf_sq <= 0:
            return rec
        theta_inf = math.sqrt(theta_inf_sq)
        # thetaE from eq (11)
        thetaD = 778.0
        inner = theta_inf_sq - (1.0/6.0)*thetaD*thetaD
        if inner <= 0:
            return rec
        thetaE = math.sqrt(inner * (18.0/25.0))
        rec['recomputed_A'] = A
        rec['recomputed_thetaE'] = thetaE
        rec['recomputed_theta_inf'] = theta_inf
    except Exception:
        pass
    return rec


# === block: score_0 (check id='step_fit_and_table') ===
def score_0(artifact, step, ctx):
    import math

    A_recomputed = ctx.get('recomputed_A')
    thetaE_recomputed = ctx.get('recomputed_thetaE')
    if A_recomputed is None or thetaE_recomputed is None:
        return 0.0

    R = 8.314
    A_gold = -1.24e-3
    thetaE_gold = 607.0

    # Score A (symmetric tolerance – physical parameter, not a performance metric)
    if abs(A_gold) < 1e-12:
        score_A = 1.0 if abs(A_recomputed) < 1e-12 else 0.0
    else:
        rel_err_A = abs(A_recomputed - A_gold) / abs(A_gold)
        if rel_err_A <= 0.05:
            score_A = 1.0
        else:
            score_A = max(0.0, 1.0 - (rel_err_A - 0.05) / 0.1)  # decays linearly to 0 at 15%

    # Score thetaE
    rel_err_thetaE = abs(thetaE_recomputed - thetaE_gold) / thetaE_gold
    if rel_err_thetaE <= 0.02:
        score_thetaE = 1.0
    else:
        score_thetaE = max(0.0, 1.0 - (rel_err_thetaE - 0.02) / 0.05)  # decays to 0 at 7%

    # Weighted combination (A is primary)
    return 0.6 * score_A + 0.4 * score_thetaE


# === block: score_1 (check id='step_fitted_params') ===
def score_1(artifact, step, ctx):
    import math

    data = artifact  # JSON dict
    try:
        A_json = float(data['anharmonic_coefficient_A'])
        thetaE_json = float(data['einstein_temperature_thetaE'])
        theta_inf_json = float(data['high_temp_debye_theta_inf'])
    except (KeyError, TypeError, ValueError):
        return 0.0

    A_rec = ctx.get('recomputed_A')
    thetaE_rec = ctx.get('recomputed_thetaE')
    theta_inf_rec = ctx.get('recomputed_theta_inf')
    if A_rec is None or thetaE_rec is None or theta_inf_rec is None:
        # If recompute failed, check existence only (low credit)
        return 0.5

    # Allowed relative tolerance (generous, 2%)
    tol = 0.02
    pass_A = (abs(A_json - A_rec) / max(abs(A_rec), 1e-12)) <= tol if abs(A_rec) > 1e-12 else abs(A_json) < 1e-12
    pass_thetaE = abs(thetaE_json - thetaE_rec) <= tol * thetaE_rec
    pass_theta_inf = abs(theta_inf_json - theta_inf_rec) <= tol * theta_inf_rec

    if pass_A and pass_thetaE and pass_theta_inf:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'step_fit_and_table': score_0,
    'step_fitted_params': score_1,
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
