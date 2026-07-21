import os
import json
import csv

# === author imports / helpers ===
import csv, math, json, os

def spearmanr(x, y):
    n = len(x)
    if n <= 1:
        return 0.0
    # compute ranks (simple version, ties ignored)
    x_ranks = [sorted(x).index(v)+1 for v in x]
    y_ranks = [sorted(y).index(v)+1 for v in y]
    d2 = sum((rx - ry)**2 for rx, ry in zip(x_ranks, y_ranks))
    return 1.0 - 6.0 * d2 / (n * (n*n - 1))


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
    step = next(s for s in spec['steps'] if s['id'] == 'structural_results')
    gold_list = step['gold']
    tolerances = step['tolerances']
    trend_check = step.get('trend_check_metrics', {})
    trend_threshold = step.get('trend_threshold', 0.8)
    return {
        'gold_list': gold_list,
        'tolerances': tolerances,
        'trend_check': trend_check,
        'trend_threshold': trend_threshold,
        'metric_weights': {
            'density': 0.25,
            'D': 0.25,
            'xi_x': 0.1,
            'xi_y_cos_beta': 0.15,
            'beta': 0.1,
            'anisotropy_ratio': 0.15
        }
    }


# === block: score_0 (check id='structural_results') ===
def score_0(artifact, step, ctx):
    import csv, math

    rows = artifact  # artifact is list of dicts from csv.DictReader
    gold_list = ctx['gold_list']
    tols = ctx['tolerances']
    trend_check = ctx['trend_check']
    trend_threshold = ctx['trend_threshold']
    weights = ctx['metric_weights']

    # Map agent rows by alpha (float)
    agent = {}
    for r in rows:
        alpha = float(r['alpha'])
        agent[alpha] = r

    metrics = ['density', 'D', 'xi_x', 'xi_y_cos_beta', 'beta', 'anisotropy_ratio']

    # Value agreement per metric
    value_scores = {}
    for m in metrics:
        count = 0
        total = 0
        for g in gold_list:
            a = float(g['alpha'])
            if a not in agent:
                continue
            total += 1
            gold_val = g[m]
            agent_val = float(agent[a][m])
            if abs(agent_val - gold_val) <= tols[m]:
                count += 1
        if total == 0:
            value_scores[m] = 0.0
        else:
            value_scores[m] = count / total

    # Trend scores
    trend_scores = {}
    for m, direction in trend_check.items():
        pairs = []
        for g in gold_list:
            a = float(g['alpha'])
            if a in agent:
                pairs.append((a, float(agent[a][m])))
        if len(pairs) < 2:
            trend_scores[m] = 0.0
            continue
        x = [p[0] for p in pairs]
        y = [p[1] for p in pairs]
        r = spearmanr(x, y)
        # expected sign
        if direction == 'increasing':
            if r > 0:
                score = min(1.0, max(0.0, (abs(r) - 0.5) / 0.5))
            else:
                score = 0.0
        else:  # decreasing
            if r < 0:
                score = min(1.0, max(0.0, (abs(r) - 0.5) / 0.5))
            else:
                score = 0.0
        trend_scores[m] = score

    # Combine per metric: value weight 0.7, trend weight 0.3 (if trend applicable)
    combined = {}
    for m in metrics:
        vs = value_scores[m]
        if m in trend_scores:
            ts = trend_scores[m]
            score = 0.7 * vs + 0.3 * ts
        else:
            score = vs
        combined[m] = score

    # Weighted average across metrics
    overall = 0.0
    total_w = 0.0
    for m in metrics:
        w = weights.get(m, 0.1)
        overall += w * combined[m]
        total_w += w
    if total_w == 0:
        return 0.0
    return overall


_SCORERS = {
    'structural_results': score_0,
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
