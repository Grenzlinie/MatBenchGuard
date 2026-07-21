import os
import json
import csv

# === author imports / helpers ===
import math

def spearmanr_manual(x, y):
    """Manually compute Spearman rank correlation without scipy."""
    n = len(x)
    if n == 0:
        return 0.0
    from collections import OrderedDict
    def rankdata(a):
        s = sorted(a)
        ranks = {}
        i = 0
        while i < n:
            v = s[i]
            j = i
            while j < n and s[j] == v:
                j += 1
            rank = (i + j - 1) / 2.0
            for k in range(i, j):
                ranks[v] = rank
            i = j
        return [ranks[v] for v in a]
    rx = rankdata(x)
    ry = rankdata(y)
    mean_x = sum(rx) / n
    mean_y = sum(ry) / n
    num = sum((rx[i] - mean_x) * (ry[i] - mean_y) for i in range(n))
    den_x = math.sqrt(sum((rx[i] - mean_x)**2 for i in range(n)))
    den_y = math.sqrt(sum((ry[i] - mean_y)**2 for i in range(n)))
    if den_x * den_y == 0:
        return 0.0
    return num / (den_x * den_y)


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


# === block: score_0 (check id='pristine_numeric') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if len(rows) != 2:
        return 0.0
    gold = step['gold']
    props = ['Youngs_modulus_GPa', 'UTS_GPa', 'failure_strain_percent']
    tols = step['tolerances']
    scores = []
    for row in rows:
        direction = row.get('direction', '').strip().lower()
        if direction not in ('zz', 'am'):
            continue
        g = gold.get('zz' if direction == 'zz' else 'am')
        if g is None:
            continue
        row_scores = []
        for p in props:
            try:
                val = float(row[p])
            except (ValueError, KeyError):
                continue
            gold_val = g[p]
            tol = tols[p]
            if gold_val == 0:
                row_scores.append(1.0 if val == 0 else 0.0)
            else:
                rel_err = abs(val - gold_val) / abs(gold_val)
                if rel_err <= tol:
                    row_scores.append(1.0)
                else:
                    row_scores.append(max(0.0, 1.0 - (rel_err - tol) / (2*tol)))
        if row_scores:
            scores.append(sum(row_scores) / len(row_scores))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='gb_numeric') ===
def score_1(artifact, step, ctx):
    rows = artifact
    gold = step['gold']
    props = ['Youngs_modulus_GPa', 'UTS_GPa', 'failure_strain_percent']
    tols = step['tolerances']
    scores = []
    for row in rows:
        model = row.get('model_name', '').strip()
        if model not in gold:
            continue
        g = gold[model]
        row_scores = []
        for p in props:
            try:
                val = float(row[p])
            except (ValueError, KeyError):
                continue
            gold_val = g[p]
            tol = tols[p]
            if gold_val == 0:
                row_scores.append(1.0 if val == 0 else 0.0)
            else:
                rel_err = abs(val - gold_val) / abs(gold_val)
                if rel_err <= tol:
                    row_scores.append(1.0)
                else:
                    row_scores.append(max(0.0, 1.0 - (rel_err - tol) / (2*tol)))
        if row_scores:
            scores.append(sum(row_scores) / len(row_scores))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='gb_trend') ===
def score_2(artifact, step, ctx):
    rows = artifact
    trends = step['trend_checks']
    scores = []
    for t in trends:
        prop = t['property']
        index = t['index']
        direction = t['direction']
        xs = []
        ys = []
        for row in rows:
            try:
                x = float(row[index])
                y = float(row[prop])
            except (ValueError, KeyError):
                continue
            xs.append(x)
            ys.append(y)
        if len(xs) < 3:
            scores.append(0.0)
            continue
        r = spearmanr_manual(xs, ys)
        if direction == 'decreasing':
            r_expected_sign = -1
        else:
            r_expected_sign = 1
        score = max(0.0, r_expected_sign * r)
        scores.append(min(1.0, score / 0.7))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='strain_rate_numeric') ===
def score_3(artifact, step, ctx):
    rows = artifact
    gold = step['gold']
    props = ['UTS_GPa', 'Youngs_modulus_GPa']
    tols = step['tolerances']
    scores = []
    for row in rows:
        model = row.get('model_name', '').strip()
        try:
            rate = str(row.get('strain_rate_s-1')).strip()
        except:
            continue
        if model not in gold:
            continue
        g = gold[model]
        if rate not in g:
            continue
        gv = g[rate]
        row_scores = []
        for p in props:
            try:
                val = float(row[p])
            except:
                continue
            gold_val = gv[p]
            tol = tols[p]
            if gold_val == 0:
                row_scores.append(1.0 if val == 0 else 0.0)
            else:
                rel_err = abs(val - gold_val) / abs(gold_val)
                if rel_err <= tol:
                    row_scores.append(1.0)
                else:
                    row_scores.append(max(0.0, 1.0 - (rel_err - tol) / (2*tol)))
        if row_scores:
            scores.append(sum(row_scores) / len(row_scores))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_4 (check id='strain_rate_trend') ===
def score_4(artifact, step, ctx):
    rows = artifact
    trends = step['trend_checks']
    models = set(row.get('model_name', '').strip() for row in rows)
    scores = []
    for model in models:
        model_rows = [r for r in rows if r.get('model_name', '').strip() == model]
        if not model_rows:
            continue
        for t in trends:
            prop = t['property']
            index = t['index']
            direction = t['direction']
            xs = []
            ys = []
            for row in model_rows:
                try:
                    x = float(row[index])
                    y = float(row[prop])
                except:
                    continue
                xs.append(x)
                ys.append(y)
            if len(xs) < 3:
                scores.append(0.0)
                continue
            r = spearmanr_manual(xs, ys)
            if direction == 'decreasing':
                r_sign = -1
            else:
                r_sign = 1
            score = max(0.0, r_sign * r)
            scores.append(min(1.0, score / 0.7))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_5 (check id='temperature_numeric') ===
def score_5(artifact, step, ctx):
    rows = artifact
    gold = step['gold']
    props = ['UTS_GPa', 'Youngs_modulus_GPa']
    tols = step['tolerances']
    scores = []
    for row in rows:
        model = row.get('model_name', '').strip()
        try:
            temp = str(int(float(row.get('temperature_K', 0))))
        except:
            continue
        if model not in gold:
            continue
        g = gold[model]
        if temp not in g:
            continue
        gv = g[temp]
        row_scores = []
        for p in props:
            try:
                val = float(row[p])
            except:
                continue
            gold_val = gv[p]
            tol = tols[p]
            if gold_val == 0:
                row_scores.append(1.0 if val == 0 else 0.0)
            else:
                rel_err = abs(val - gold_val) / abs(gold_val)
                if rel_err <= tol:
                    row_scores.append(1.0)
                else:
                    row_scores.append(max(0.0, 1.0 - (rel_err - tol) / (2*tol)))
        if row_scores:
            scores.append(sum(row_scores) / len(row_scores))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_6 (check id='temperature_trend') ===
def score_6(artifact, step, ctx):
    rows = artifact
    trends = step['trend_checks']
    models = set(row.get('model_name', '').strip() for row in rows)
    scores = []
    for model in models:
        model_rows = [r for r in rows if r.get('model_name', '').strip() == model]
        if not model_rows:
            continue
        for t in trends:
            prop = t['property']
            index = t['index']
            direction = t['direction']
            xs = []
            ys = []
            for row in model_rows:
                try:
                    x = float(row[index])
                    y = float(row[prop])
                except:
                    continue
                xs.append(x)
                ys.append(y)
            if len(xs) < 3:
                scores.append(0.0)
                continue
            r = spearmanr_manual(xs, ys)
            if direction == 'decreasing':
                r_sign = -1
            else:
                r_sign = 1
            score = max(0.0, r_sign * r)
            scores.append(min(1.0, score / 0.7))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'pristine_numeric': score_0,
    'gb_numeric': score_1,
    'gb_trend': score_2,
    'strain_rate_numeric': score_3,
    'strain_rate_trend': score_4,
    'temperature_numeric': score_5,
    'temperature_trend': score_6,
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
