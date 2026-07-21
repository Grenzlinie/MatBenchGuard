import os
import json
import csv

# === author imports / helpers ===
import csv, math, bisect


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
    import bisect
    rows = spec.get('steps', spec.get('checks', []))
    gold_q = {}
    gold_lt = []
    for s in rows:
        if s['id'] == 'dynamic_order_parameter':
            g = s['gold']
            gold_q['p'] = g['p']
            gold_q['Q'] = g['Q_abs']
        if s['id'] == 'metastable_lifetime':
            gold_lt = s['gold_points']
    return {'gold_q': gold_q, 'gold_lt': gold_lt}


# === block: score_0 (check id='dynamic_order_parameter') ===
def score_0(artifact, step, ctx):
    tol = step.get('tolerance_abs', 0.05)
    gold = ctx['gold_q']
    gold_p = gold['p']
    gold_Q = gold['Q']
    rows = artifact
    if not rows:
        return 0.0
    scores = []
    for r in rows:
        try:
            p = float(r['p'])
            Q = float(r['Q_abs'])
        except:
            scores.append(0.0)
            continue
        # interpolate gold Q_abs
        if p <= gold_p[0]:
            gQ = gold_Q[0]
        elif p >= gold_p[-1]:
            gQ = gold_Q[-1]
        else:
            i = bisect.bisect_right(gold_p, p) - 1
            if i < 0:
                i = 0
            if i >= len(gold_p)-1:
                i = len(gold_p)-2
            x0, x1 = gold_p[i], gold_p[i+1]
            y0, y1 = gold_Q[i], gold_Q[i+1]
            gQ = y0 + (p - x0) * (y1 - y0) / (x1 - x0)
        dist = abs(Q - gQ)
        row_score = max(0.0, 1.0 - dist / (2.0 * tol))
        scores.append(row_score)
    return sum(scores) / len(scores)


# === block: score_1 (check id='metastable_lifetime') ===
def score_1(artifact, step, ctx):
    tol_rel = step.get('tolerance_relative', 0.20)
    trend_w = step.get('trend_subweight', 0.2)
    gold_pts = ctx['gold_lt']
    rows = artifact
    if not rows:
        return 0.0
    agent = {}
    for r in rows:
        try:
            h0 = float(r['h0'])
            p = float(r['p'])
            tau = float(r['tau_avg'])
            key = (round(h0, 6), round(p, 6))
            agent[key] = tau
        except:
            continue
    point_scores = []
    for gp in gold_pts:
        h0g, pg, tg = gp['h0'], gp['p'], gp['tau']
        key = (round(h0g, 6), round(pg, 6))
        if key not in agent:
            point_scores.append(0.0)
            continue
        tau_agent = agent[key]
        if tg == 0:
            point_scores.append(1.0 if tau_agent == 0 else 0.0)
            continue
        rel_err = abs(tau_agent - tg) / tg
        ps = max(0.0, 1.0 - rel_err / (2.0 * tol_rel))
        point_scores.append(ps)
    avg_point = sum(point_scores) / len(point_scores) if point_scores else 0.0
    h0_groups = {}
    for r in rows:
        try:
            h0 = float(r['h0'])
            p = float(r['p'])
            tau = float(r['tau_avg'])
            h0_groups.setdefault(round(h0,6), []).append((p, tau))
        except:
            continue
    trend_score = 0.0
    if h0_groups:
        group_scores = []
        for h0, pts in h0_groups.items():
            pts.sort(key=lambda x: x[0])
            ok = True
            for i in range(1, len(pts)):
                if pts[i][1] < pts[i-1][1] * 0.95:
                    ok = False
                    break
            group_scores.append(1.0 if ok else 0.0)
        trend_score = sum(group_scores) / len(group_scores)
    else:
        trend_score = 0.0
    overall = avg_point * (1.0 - trend_w) + trend_score * trend_w
    return overall


_SCORERS = {
    'dynamic_order_parameter': score_0,
    'metastable_lifetime': score_1,
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
