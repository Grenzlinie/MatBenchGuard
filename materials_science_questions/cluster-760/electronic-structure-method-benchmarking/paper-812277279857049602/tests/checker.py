import os
import json
import csv

# === author imports / helpers ===
import math
def compute_regression(xs, ys):
    n = len(xs)
    if n < 2:
        return {'a': 0, 'b': 0, 'R': 0, 'SE': float('inf')}
    sx = sum(xs); sy = sum(ys)
    sxx = sum(x*x for x in xs)
    sxy = sum(x*y for x,y in zip(xs, ys))
    syy = sum(y*y for y in ys)
    denom = n * sxx - sx * sx
    if denom == 0:
        return {'a': 0, 'b': 0, 'R': 0, 'SE': float('inf')}
    a = (n * sxy - sx * sy) / denom
    b = (sy - a * sx) / n
    r_num = n * sxy - sx * sy
    r_den = math.sqrt((n * sxx - sx * sx) * (n * syy - sy * sy))
    r = r_num / r_den if r_den else 0
    res = [(ys[i] - (a * xs[i] + b)) ** 2 for i in range(n)]
    ss_res = sum(res)
    se = math.sqrt(ss_res / (n - 2)) if n > 2 else float('inf')
    return {'a': a, 'b': b, 'R': r, 'SE': se}
def r_squared_from_xy(xs, ys):
    n = len(xs)
    if n < 2:
        return 0.0
    sx = sum(xs); sy = sum(ys)
    sxx = sum(x*x for x in xs)
    sxy = sum(x*y for x,y in zip(xs, ys))
    denom = n * sxx - sx * sx
    if denom == 0:
        return 0.0
    a = (n * sxy - sx * sy) / denom
    b = (sy - a * sx) / n
    ss_res = sum((ys[i] - (a * xs[i] + b)) ** 2 for i in range(n))
    mean_y = sy / n
    ss_tot = sum((y - mean_y) ** 2 for y in ys)
    if ss_tot == 0:
        return 1.0 if ss_res == 0 else 0.0
    return 1 - ss_res / ss_tot
def score_regression_params(comp, gold):
    da = abs(comp['a'] - gold['a'])
    if da <= 0.2: sa = 1.0
    elif da <= 0.4: sa = max(0.0, 1.0 - (da - 0.2) / 0.2)
    else: sa = 0.0
    db = abs(comp['b'] - gold['b'])
    if db <= 1.0: sb = 1.0
    elif db <= 2.0: sb = max(0.0, 1.0 - (db - 1.0) / 1.0)
    else: sb = 0.0
    rg = gold['R']; rc = comp['R']
    if rc >= rg - 0.05: sr = 1.0
    elif rc >= rg - 0.15: sr = max(0.0, (rc - (rg - 0.15)) / 0.1)
    else: sr = 0.0
    seg = gold['SE']; sec = comp['SE']
    if sec <= seg + 0.5: sse = 1.0
    elif sec <= seg + 1.5: sse = max(0.0, 1.0 - (sec - seg - 0.5))
    else: sse = 0.0
    return (sa + sb + sr + sse) / 4.0


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
    return {'exp_shifts': spec['experimental_shifts'], 'gold_params': spec['paper_regression_params']}


# === block: score_0 (check id='regression_2a_1H') ===
def score_0(artifact, step, ctx):
    compound = step['compound']; nucleus = step['nucleus']
    ref_list = ctx['exp_shifts'][compound][nucleus]
    calc_map = {r['atom_label']: r['calc_shift'] for r in artifact if r.get('compound')==compound and r.get('nucleus')==nucleus}
    xs = [e['exp_shift'] for e in ref_list if e['atom_label'] in calc_map]
    ys = [calc_map[e['atom_label']] for e in ref_list if e['atom_label'] in calc_map]
    if len(xs) < 2:
        return 0.0
    comp = compute_regression(xs, ys)
    gold = ctx['gold_params'].get(f'{compound}_{nucleus}', {})
    if not gold:
        return 0.0
    return score_regression_params(comp, gold)


# === block: score_1 (check id='regression_2a_13C') ===
def score_1(artifact, step, ctx):
    compound = step['compound']; nucleus = step['nucleus']
    ref_list = ctx['exp_shifts'][compound][nucleus]
    calc_map = {r['atom_label']: r['calc_shift'] for r in artifact if r.get('compound')==compound and r.get('nucleus')==nucleus}
    xs = [e['exp_shift'] for e in ref_list if e['atom_label'] in calc_map]
    ys = [calc_map[e['atom_label']] for e in ref_list if e['atom_label'] in calc_map]
    if len(xs) < 2:
        return 0.0
    comp = compute_regression(xs, ys)
    gold = ctx['gold_params'].get(f'{compound}_{nucleus}', {})
    if not gold:
        return 0.0
    return score_regression_params(comp, gold)


# === block: score_2 (check id='regression_2b_1H') ===
def score_2(artifact, step, ctx):
    compound = step['compound']; nucleus = step['nucleus']
    ref_list = ctx['exp_shifts'][compound][nucleus]
    calc_map = {r['atom_label']: r['calc_shift'] for r in artifact if r.get('compound')==compound and r.get('nucleus')==nucleus}
    xs = [e['exp_shift'] for e in ref_list if e['atom_label'] in calc_map]
    ys = [calc_map[e['atom_label']] for e in ref_list if e['atom_label'] in calc_map]
    if len(xs) < 2:
        return 0.0
    comp = compute_regression(xs, ys)
    gold = ctx['gold_params'].get(f'{compound}_{nucleus}', {})
    if not gold:
        return 0.0
    return score_regression_params(comp, gold)


# === block: score_3 (check id='regression_2b_13C') ===
def score_3(artifact, step, ctx):
    compound = step['compound']; nucleus = step['nucleus']
    ref_list = ctx['exp_shifts'][compound][nucleus]
    calc_map = {r['atom_label']: r['calc_shift'] for r in artifact if r.get('compound')==compound and r.get('nucleus')==nucleus}
    xs = [e['exp_shift'] for e in ref_list if e['atom_label'] in calc_map]
    ys = [calc_map[e['atom_label']] for e in ref_list if e['atom_label'] in calc_map]
    if len(xs) < 2:
        return 0.0
    comp = compute_regression(xs, ys)
    gold = ctx['gold_params'].get(f'{compound}_{nucleus}', {})
    if not gold:
        return 0.0
    return score_regression_params(comp, gold)


# === block: score_4 (check id='regression_2c_1H') ===
def score_4(artifact, step, ctx):
    compound = step['compound']; nucleus = step['nucleus']
    ref_list = ctx['exp_shifts'][compound][nucleus]
    calc_map = {r['atom_label']: r['calc_shift'] for r in artifact if r.get('compound')==compound and r.get('nucleus')==nucleus}
    xs = [e['exp_shift'] for e in ref_list if e['atom_label'] in calc_map]
    ys = [calc_map[e['atom_label']] for e in ref_list if e['atom_label'] in calc_map]
    if len(xs) < 2:
        return 0.0
    comp = compute_regression(xs, ys)
    gold = ctx['gold_params'].get(f'{compound}_{nucleus}', {})
    if not gold:
        return 0.0
    return score_regression_params(comp, gold)


# === block: score_5 (check id='regression_2c_13C') ===
def score_5(artifact, step, ctx):
    compound = step['compound']; nucleus = step['nucleus']
    ref_list = ctx['exp_shifts'][compound][nucleus]
    calc_map = {r['atom_label']: r['calc_shift'] for r in artifact if r.get('compound')==compound and r.get('nucleus')==nucleus}
    xs = [e['exp_shift'] for e in ref_list if e['atom_label'] in calc_map]
    ys = [calc_map[e['atom_label']] for e in ref_list if e['atom_label'] in calc_map]
    if len(xs) < 2:
        return 0.0
    comp = compute_regression(xs, ys)
    gold = ctx['gold_params'].get(f'{compound}_{nucleus}', {})
    if not gold:
        return 0.0
    return score_regression_params(comp, gold)


# === block: score_6 (check id='regression_2d_1H') ===
def score_6(artifact, step, ctx):
    compound = step['compound']; nucleus = step['nucleus']
    ref_list = ctx['exp_shifts'][compound][nucleus]
    calc_map = {r['atom_label']: r['calc_shift'] for r in artifact if r.get('compound')==compound and r.get('nucleus')==nucleus}
    xs = [e['exp_shift'] for e in ref_list if e['atom_label'] in calc_map]
    ys = [calc_map[e['atom_label']] for e in ref_list if e['atom_label'] in calc_map]
    if len(xs) < 2:
        return 0.0
    comp = compute_regression(xs, ys)
    gold = ctx['gold_params'].get(f'{compound}_{nucleus}', {})
    if not gold:
        return 0.0
    return score_regression_params(comp, gold)


# === block: score_7 (check id='regression_2d_13C') ===
def score_7(artifact, step, ctx):
    compound = step['compound']; nucleus = step['nucleus']
    ref_list = ctx['exp_shifts'][compound][nucleus]
    calc_map = {r['atom_label']: r['calc_shift'] for r in artifact if r.get('compound')==compound and r.get('nucleus')==nucleus}
    xs = [e['exp_shift'] for e in ref_list if e['atom_label'] in calc_map]
    ys = [calc_map[e['atom_label']] for e in ref_list if e['atom_label'] in calc_map]
    if len(xs) < 2:
        return 0.0
    comp = compute_regression(xs, ys)
    gold = ctx['gold_params'].get(f'{compound}_{nucleus}', {})
    if not gold:
        return 0.0
    return score_regression_params(comp, gold)


# === block: score_8 (check id='overall_R2') ===
def score_8(artifact, step, ctx):
    xs_all = []; ys_all = []
    exp_shifts = ctx['exp_shifts']
    for compound in exp_shifts:
        for nucleus in exp_shifts[compound]:
            ref_list = exp_shifts[compound][nucleus]
            calc_map = {r['atom_label']: r['calc_shift'] for r in artifact if r.get('compound')==compound and r.get('nucleus')==nucleus}
            for entry in ref_list:
                if entry['atom_label'] in calc_map:
                    xs_all.append(entry['exp_shift'])
                    ys_all.append(calc_map[entry['atom_label']])
    if len(xs_all) < 2:
        return 0.0
    overall_r2 = r_squared_from_xy(xs_all, ys_all)
    gold_r2 = ctx['gold_params'].get('overall_R2', 0.9989)
    diff = abs(overall_r2 - gold_r2)
    if diff <= 0.001:
        return 1.0
    elif diff <= 0.005:
        return max(0.0, 1.0 - (diff - 0.001) / 0.004)
    return 0.0


# === block: score_9 (check id='atom_labels_completeness') ===
def score_9(artifact, step, ctx):
    expected_labels = set()
    exp_shifts = ctx['exp_shifts']
    for compound in exp_shifts:
        for nucleus in exp_shifts[compound]:
            for entry in exp_shifts[compound][nucleus]:
                expected_labels.add((compound, nucleus, entry['atom_label']))
    actual_labels = set()
    for r in artifact:
        actual_labels.add((r.get('compound'), r.get('nucleus'), r.get('atom_label')))
    missing = len(expected_labels - actual_labels)
    extra = len(actual_labels - expected_labels)
    total = len(expected_labels)
    if total == 0:
        return 0.0
    return max(0.0, 1.0 - 0.5 * (missing + extra) / total)


_SCORERS = {
    'regression_2a_1H': score_0,
    'regression_2a_13C': score_1,
    'regression_2b_1H': score_2,
    'regression_2b_13C': score_3,
    'regression_2c_1H': score_4,
    'regression_2c_13C': score_5,
    'regression_2d_1H': score_6,
    'regression_2d_13C': score_7,
    'overall_R2': score_8,
    'atom_labels_completeness': score_9,
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
