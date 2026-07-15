import os
import json
import csv

# === author imports / helpers ===
import csv
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
    def load_csv(path):
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    step03 = load_csv(os.path.join(outputs_dir, 'step_03_thermoelectric_data.csv'))
    step04 = load_csv(os.path.join(outputs_dir, 'step_04_peak_results.csv'))
    for r in step03:
        r['Lg_nm'] = float(r['Lg_nm'])
        r['Cd_percent'] = int(r['Cd_percent'])
        r['avg_PF_mW_per_mK2'] = float(r['avg_PF_mW_per_mK2'])
    for r in step04:
        r['Cd_percent'] = int(r['Cd_percent'])
        r['max_PF_mW_per_mK2'] = float(r['max_PF_mW_per_mK2'])
        r['optimum_Lg_nm'] = float(r['optimum_Lg_nm'])
    return {'step03_data': step03, 'step04_data': step04}


# === block: score_0 (check id='step_03_shape') ===
def score_0(artifact, step, ctx):
    data = ctx['step03_data']
    return 1.0 if data and len(data) > 0 else 0.0


# === block: score_1 (check id='step_03_headline_pf') ===
def score_1(artifact, step, ctx):
    gold = step['target_value']
    tol = step['tolerance_relative']
    cond = step['condition']
    col = step['column']
    for row in ctx['step03_data']:
        if row['Lg_nm'] == cond['Lg_nm'] and row['Cd_percent'] == cond['Cd_percent']:
            val = row[col]
            if abs(val - gold) <= tol * gold:
                return 1.0
            else:
                return 0.0
    return 0.0


# === block: score_2 (check id='step_03_trends_mono5') ===
def score_2(artifact, step, ctx):
    cd = step['condition']['Cd_percent']
    rows = [r for r in ctx['step03_data'] if r['Cd_percent'] == cd]
    rows.sort(key=lambda r: r['Lg_nm'])
    x = [r['Lg_nm'] for r in rows]
    y = [r['avg_PF_mW_per_mK2'] for r in rows]
    if len(x) < 2:
        return 0.0
    n = len(x)
    mean_x = sum(x)/n
    mean_y = sum(y)/n
    cov = sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(n))
    std_x = math.sqrt(sum((v-mean_x)**2 for v in x))
    std_y = math.sqrt(sum((v-mean_y)**2 for v in y))
    if std_x == 0 or std_y == 0:
        return 0.0
    r = cov/(std_x*std_y)
    return 1.0 if r > step['correlation_threshold'] else 0.0


# === block: score_3 (check id='step_03_trends_peak10_15_20') ===
def score_3(artifact, step, ctx):
    cds = step['conditions']
    y_col = step['column_y']
    def has_single_peak(rows):
        rows_sorted = sorted(rows, key=lambda r: r['Lg_nm'])
        y = [r[y_col] for r in rows_sorted]
        if len(y) < 3:
            return False
        max_idx = max(range(len(y)), key=lambda i: y[i])
        for i in range(1, max_idx+1):
            if y[i] < y[i-1]:
                return False
        for i in range(max_idx+1, len(y)):
            if y[i] > y[i-1]:
                return False
        return True
    total = 0
    count = 0
    for cd in cds:
        rows_cd = [r for r in ctx['step03_data'] if r['Cd_percent'] == cd]
        if rows_cd:
            count += 1
            if has_single_peak(rows_cd):
                total += 1
    return total/count if count else 0.0


# === block: score_4 (check id='step_04_consistency') ===
def score_4(artifact, step, ctx):
    ref_data = ctx['step03_data']
    step04 = ctx['step04_data']
    tol_pf = step['tolerance_pf']
    tol_lg = step['tolerance_lg']
    matches = 0
    total = 0
    for row in step04:
        cd = row['Cd_percent']
        rep_pf = row['max_PF_mW_per_mK2']
        rep_lg = row['optimum_Lg_nm']
        rows_cd = [r for r in ref_data if r['Cd_percent'] == cd]
        if not rows_cd:
            continue
        max_row = max(rows_cd, key=lambda r: r['avg_PF_mW_per_mK2'])
        max_pf = max_row['avg_PF_mW_per_mK2']
        max_lg = max_row['Lg_nm']
        if abs(rep_pf - max_pf) <= tol_pf and abs(rep_lg - max_lg) <= tol_lg:
            matches += 1
        total += 1
    return matches/total if total else 0.0


# === block: score_5 (check id='step_04_ordering') ===
def score_5(artifact, step, ctx):
    step04 = ctx['step04_data']
    group = {}
    for r in step04:
        group[r['Cd_percent']] = r['optimum_Lg_nm']
    order = step['order']
    if not all(cd in group for cd in order):
        return 0.0
    for i in range(len(order)-1):
        if group[order[i]] <= group[order[i+1]]:
            return 0.0
    return 1.0


_SCORERS = {
    'step_03_shape': score_0,
    'step_03_headline_pf': score_1,
    'step_03_trends_mono5': score_2,
    'step_03_trends_peak10_15_20': score_3,
    'step_04_consistency': score_4,
    'step_04_ordering': score_5,
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
