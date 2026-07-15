import os
import json
import csv

# === author imports / helpers ===
import math, csv, os, json


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


# === block: score_0 (check id='grid_quality_and_recompute') ===
def score_0(artifact, step, ctx):
    def model_qs_local(x, x_c1, x_c2, m1, m2, m3, alpha, gamma):
        if x <= 0:
            return (0.0, 0.0, 0.0)
        lam1 = (1.0 / x) * math.log(1.0 + x)
        Q1 = (x * x / m1) * math.exp(-1.0 / lam1)
        if x <= x_c1:
            Q2 = Q3 = 0.0
        else:
            x2 = math.sqrt(alpha) * math.sqrt(max(0.0, x * x - x_c1 * x_c1))
            if x2 == 0.0:
                Q2 = 0.0
            else:
                denom2 = x + alpha * x2
                lam2 = (alpha / x2) * math.log(1.0 + x2 * x2 / denom2)
                Q2 = (x * x / m2) * math.exp(-1.0 / lam2)
            if x <= x_c2:
                Q3 = 0.0
            else:
                x3 = math.sqrt(gamma) * math.sqrt(max(0.0, x * x - x_c2 * x_c2))
                if x3 == 0.0:
                    Q3 = 0.0
                else:
                    denom3 = x + alpha * x2 + gamma * x3
                    lam3 = (gamma / x3) * math.log(1.0 + x3 * x3 / denom3)
                    Q3 = (x * x / m3) * math.exp(-1.0 / lam3)
        return (Q1, Q2, Q3)

    params = step.get("params", {})
    nb_min = params["density_points_per_band"]
    x_c1 = params["x_c1"]
    x_c2 = params["x_c2"]
    test_xs = params["test_x"]
    tol = params["tolerance_relative"]
    m1, m2, m3 = 1.8, 3.5, 6.0
    alpha = m2 / m1
    gamma = m3 / m1
    rows = artifact if artifact else []
    xs = []
    q1, q2, q3 = [], [], []
    for r in rows:
        try:
            xs.append(float(r["x"]))
            q1.append(float(r["Q1"]))
            q2.append(float(r["Q2"]))
            q3.append(float(r["Q3"]))
        except (ValueError, KeyError):
            return 0.0
    if not xs:
        return 0.0
    count1 = sum(1 for x in xs if x <= x_c1)
    count2 = sum(1 for x in xs if x_c1 < x <= x_c2)
    count3 = sum(1 for x in xs if x > x_c2)
    min_count = min(count1, count2, count3)
    density_score = min(1.0, min_count / nb_min)
    errors = []
    for tx in test_xs:
        idx = min(range(len(xs)), key=lambda i: abs(xs[i] - tx))
        agent_vals = [q1[idx], q2[idx], q3[idx]]
        expected = model_qs_local(tx, x_c1, x_c2, m1, m2, m3, alpha, gamma)
        for a, e in zip(agent_vals, expected):
            if abs(e) > 1e-12:
                err = abs(a - e) / abs(e)
                errors.append(err)
    if errors:
        avg_err = sum(errors) / len(errors)
        recompute_score = max(0.0, 1.0 - avg_err / tol)
    else:
        recompute_score = 1.0
    return 0.25 * density_score + 0.75 * recompute_score


# === block: score_1 (check id='maxima_check') ===
def score_1(artifact, step, ctx):
    def model_qs_local(x, x_c1, x_c2, m1, m2, m3, alpha, gamma):
        if x <= 0:
            return (0.0, 0.0, 0.0)
        lam1 = (1.0 / x) * math.log(1.0 + x)
        Q1 = (x * x / m1) * math.exp(-1.0 / lam1)
        if x <= x_c1:
            Q2 = Q3 = 0.0
        else:
            x2 = math.sqrt(alpha) * math.sqrt(max(0.0, x * x - x_c1 * x_c1))
            if x2 == 0.0:
                Q2 = 0.0
            else:
                denom2 = x + alpha * x2
                lam2 = (alpha / x2) * math.log(1.0 + x2 * x2 / denom2)
                Q2 = (x * x / m2) * math.exp(-1.0 / lam2)
            if x <= x_c2:
                Q3 = 0.0
            else:
                x3 = math.sqrt(gamma) * math.sqrt(max(0.0, x * x - x_c2 * x_c2))
                if x3 == 0.0:
                    Q3 = 0.0
                else:
                    denom3 = x + alpha * x2 + gamma * x3
                    lam3 = (gamma / x3) * math.log(1.0 + x3 * x3 / denom3)
                    Q3 = (x * x / m3) * math.exp(-1.0 / lam3)
        return (Q1, Q2, Q3)

    params = step.get("params", {})
    x_tol = params["x_tolerance_abs"]
    Q_tol_rel = params["Q_tolerance_rel"]
    x_c1 = params["x_c1"]
    x_c2 = params["x_c2"]
    m1 = params["m1"]; m2 = params["m2"]; m3 = params["m3"]
    alpha = params["alpha"]; gamma = params["gamma"]
    maxima_rows = artifact if artifact else []
    agent_max = {}
    for row in maxima_rows:
        try:
            b = int(row["band"])
            agent_max[b] = {
                "x_max": float(row["x_max"]),
                "n_s_max": float(row["n_s_max"]),
                "Q_max": float(row["Q_max"])
            }
        except (ValueError, KeyError):
            continue
    if not agent_max:
        return 0.0
    csv_path = os.path.join("/app/outputs", "lambda_and_Tc.csv")
    if not os.path.isfile(csv_path):
        consistency_score = 0.0
    else:
        with open(csv_path, newline='') as f:
            rdr = csv.DictReader(f)
            grid_rows = list(rdr)
        def find_max_from_grid(col):
            best = (-1.0, -1.0, -1e9)
            for r in grid_rows:
                try:
                    xv = float(r["x"])
                    ns = float(r["n_s"])
                    qv = float(r[col])
                    if qv > best[2]:
                        best = (xv, ns, qv)
                except (ValueError, KeyError):
                    continue
            return best
        grid_max = {
            1: find_max_from_grid("Q1"),
            2: find_max_from_grid("Q2"),
            3: find_max_from_grid("Q3")
        }
        consist_scores = []
        for b in [1,2,3]:
            if b not in agent_max or b not in grid_max or grid_max[b][2] == -1e9:
                consist_scores.append(0.0)
            else:
                rep = agent_max[b]
                gx, gns, gQ = grid_max[b]
                rx = rep["x_max"]; rQ = rep["Q_max"]
                dx = abs(rx - gx) / max(abs(gx), 1e-6)
                dQ = abs(rQ - gQ) / max(abs(gQ), 1e-6)
                err = max(dx, dQ)
                consist_scores.append(max(0.0, 1.0 - err / 0.01))
        consistency_score = sum(consist_scores) / len(consist_scores) if consist_scores else 0.0

    x_min, x_max = 0.5, 35.0
    fine_n = 20000
    step_x = (x_max - x_min) / (fine_n - 1)
    best_x = {1: None, 2: None, 3: None}
    best_Q = {1: -1.0, 2: -1.0, 3: -1.0}
    for i in range(fine_n):
        x = x_min + i * step_x
        Qs = model_qs_local(x, x_c1, x_c2, m1, m2, m3, alpha, gamma)
        for b in [1,2,3]:
            if Qs[b-1] > best_Q[b]:
                best_Q[b] = Qs[b-1]
                best_x[b] = x
    theo_scores = []
    for b in [1,2,3]:
        if b not in agent_max or best_x[b] is None:
            theo_scores.append(0.0)
        else:
            rep = agent_max[b]
            err_x = abs(rep["x_max"] - best_x[b])
            err_Q = abs(rep["Q_max"] - best_Q[b]) / max(abs(best_Q[b]), 1e-6)
            if err_x > x_tol:
                theo_scores.append(0.0)
            else:
                theo_scores.append(max(0.0, 1.0 - err_Q / Q_tol_rel))
    theo_score = sum(theo_scores) / len(theo_scores) if theo_scores else 0.0

    n_s_vals = [agent_max.get(b, {}).get("n_s_max", 0.0) for b in [1,2,3]]
    order_score = 1.0 if n_s_vals[0] < n_s_vals[1] < n_s_vals[2] else 0.0

    return 0.35 * consistency_score + 0.5 * theo_score + 0.15 * order_score


_SCORERS = {
    'grid_quality_and_recompute': score_0,
    'maxima_check': score_1,
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
