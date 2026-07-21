import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    gold_rows = None
    atol = {}
    rtol = 0.05
    for step in spec.get('steps', []):
        if step['id'] == 'step_tricritical_points':
            params = step.get('params', {})
            gold_rows = params.get('gold_rows', [])
            atol = params.get('atol', {})
            rtol = params.get('rtol', 0.05)
            break
    if gold_rows is None:
        gold_rows = []
    return {'gold_rows': gold_rows, 'atol': atol, 'rtol': rtol}


# === block: score_0 (check id='step_tricritical_points') ===
def score_0(artifact, step, ctx):
    rows = []
    try:
        for r in artifact:
            row = {}
            for k in ['W_over_A4', 'T_star', 'eta', 'P_star']:
                v = r.get(k)
                if v is not None:
                    row[k] = float(v)
                else:
                    row[k] = None
            rows.append(row)
        if not rows:
            return 0.0
    except Exception:
        return 0.0

    gold_rows = ctx['gold_rows']
    atol = ctx['atol']
    rtol = ctx['rtol']
    if not gold_rows:
        return 0.0

    scores = []
    for g in gold_rows:
        w = g['W_over_A4']
        match = None
        for r in rows:
            try:
                if abs(float(r['W_over_A4']) - w) < 1e-6:
                    match = r
                    break
            except:
                continue
        if match is None:
            scores.append(0.0)
            continue
        row_score = 0.0
        count = 0
        for field in ['T_star', 'eta', 'P_star']:
            v = match.get(field)
            if v is None:
                continue
            gold = g[field]
            tol = atol.get(field, 0.0) + rtol * abs(gold)
            if tol <= 0:
                tol = 1e-9
            err = abs(v - gold)
            if err <= tol:
                row_score += 1.0
            else:
                rel = err / tol
                if rel < 10.0:
                    row_score += max(0.0, 1.0 - rel)
            count += 1
        scores.append(row_score / max(1.0, count))
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_order_parameters') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = []
    try:
        for r in artifact:
            eta = float(r.get('eta', None))
            Sz = float(r.get('S_z', None))
            Sx = float(r.get('S_x', None))
            Sxy = float(r.get('S_xy', None))
            rows.append((eta, Sz, Sx, Sxy))
        if len(rows) < 2:
            return 0.0
    except Exception:
        return 0.0

    rows.sort(key=lambda x: x[0])
    eta_start = rows[0][3]
    eta_end = rows[-1][3]
    score1 = 0.0
    if abs(eta_start) < 0.01:
        score1 += 0.25
    elif abs(eta_start) < 0.05:
        score1 += 0.1
    if abs(eta_end) < 0.01:
        score1 += 0.25
    elif abs(eta_end) < 0.05:
        score1 += 0.1

    # find contiguous interval where conditions hold
    best_len = 0
    current = 0
    for eta, Sz, Sx, Sxy in rows:
        if Sz < -0.2 and abs(Sx) < 0.05 and Sxy > 0.1:
            current += 1
            if current > best_len:
                best_len = current
        else:
            current = 0
    if best_len >= 5:
        score2 = 0.5
    elif best_len >= 3:
        score2 = 0.3
    elif best_len >= 1:
        score2 = 0.1
    else:
        score2 = 0.0
    return score1 + score2


_SCORERS = {
    'step_tricritical_points': score_0,
    'step_order_parameters': score_1,
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
