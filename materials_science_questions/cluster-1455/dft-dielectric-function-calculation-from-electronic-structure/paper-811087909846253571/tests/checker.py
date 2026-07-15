import os
import json
import csv


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
    ctx = {}
    for step in spec.get('steps', []):
        gold = step.get('gold', None)
        if gold is not None:
            ctx[step['id'] + '_gold'] = gold
    return ctx


# === block: score_0 (check id='s02_binary_structural') ===
def score_0(artifact, step, ctx):
    gold = ctx['s02_binary_structural_gold']
    scores = []
    for row in artifact:
        compound = row['compound'].strip()
        if compound in gold:
            gold_vals = gold[compound]
            a0 = float(row['a0'])
            B0 = float(row['B0'])
            err_a = abs(a0 - gold_vals['a0']) / gold_vals['a0']
            score_a = 1.0 if err_a <= 0.02 else 0.0
            err_B = abs(B0 - gold_vals['B0']) / gold_vals['B0']
            score_B = 1.0 if err_B <= 0.05 else 0.0
            scores.extend([score_a, score_B])
    total = len(gold) * 2
    return sum(scores) / total if total > 0 else 0.0


# === block: score_1 (check id='s03_binary_bandgaps') ===
def score_1(artifact, step, ctx):
    gold_list = ctx['s03_binary_bandgaps_gold']['gaps']
    gap_rows = {}
    for row in artifact:
        key = (row['compound'].strip(), row['gap_type'].strip())
        gap_rows[key] = float(row['TB_mBJ_gap'])
    score = 0
    for g in gold_list:
        key = (g['compound'], g['gap_type'])
        if key in gap_rows:
            if abs(gap_rows[key] - g['TB_mBJ_gap']) <= 0.2:
                score += 1
    return score / len(gold_list) if gold_list else 0.0


# === block: score_2 (check id='s05_quaternary_bandgap') ===
def score_2(artifact, step, ctx):
    required = ctx['s05_quaternary_bandgap_gold']['required']
    req_x = required['x']
    req_y = required['y']
    req_gap = required['gap']
    gap_req = None
    rows_count = len(artifact) if isinstance(artifact, list) else 0
    for row in artifact:
        if float(row['x']) == req_x and float(row['y']) == req_y:
            gap_req = float(row['direct_gap'])
            break
    req_score = 1.0 if gap_req is not None and abs(gap_req - req_gap) <= 0.2 else 0.0
    extra_score = 1.0 if rows_count >= 2 else 0.0
    return 0.8 * req_score + 0.2 * extra_score


# === block: score_3 (check id='s07_optical_dielectric') ===
def score_3(artifact, step, ctx):
    gold = ctx['s07_optical_dielectric_gold']
    expected_xs = set(gold['x_values'])
    low_range = gold['static_dielectric_range']['min']
    high_range = gold['static_dielectric_range']['max']
    from collections import defaultdict
    data = defaultdict(list)
    for row in artifact:
        x = float(row['x'])
        energy = float(row['energy'])
        epsilon1 = float(row['epsilon1'])
        data[x].append((energy, epsilon1))
    static_eps = {}
    for x, entries in data.items():
        vals = [eps for e, eps in entries if 0.0 <= e <= 0.5]
        if vals:
            static_eps[x] = sum(vals) / len(vals)
    completeness = 1.0 if expected_xs.issubset(static_eps.keys()) else 0.0
    x_order = sorted(expected_xs)
    if len(x_order) == 4 and all(x in static_eps for x in x_order):
        monotonic = 1.0 if static_eps[x_order[0]] <= static_eps[x_order[1]] <= static_eps[x_order[2]] <= static_eps[x_order[3]] else 0.0
    else:
        monotonic = 0.0
    range_ok = 1.0 if completeness and all(low_range <= static_eps[x] <= high_range for x in expected_xs) else 0.0
    return 0.3 * completeness + 0.4 * monotonic + 0.3 * range_ok


_SCORERS = {
    's02_binary_structural': score_0,
    's03_binary_bandgaps': score_1,
    's05_quaternary_bandgap': score_2,
    's07_optical_dielectric': score_3,
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
