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
    return {}


# === block: score_0 (check id='csv_shape') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 15:
        return 0.0
    required_cols = {'substrate_type','orientation','mismatch_delta','T_n_K'}
    for row in artifact:
        if set(row.keys()) != required_cols:
            return 0.0
    return 1.0


# === block: score_1 (check id='t_n_accuracy') ===
def score_1(artifact, step, ctx):
    target_data = step.get('target_data', [])
    tol = step.get('tolerance', 0.5)
    if not target_data:
        return 0.0
    gold_map = {}
    for g in target_data:
        key = (g['substrate_type'], g['orientation'], g['mismatch_delta'])
        gold_map[key] = g['T_n_K']
    valid = 0
    for row in artifact:
        key = (row.get('substrate_type',''), row.get('orientation',''), int(row.get('mismatch_delta',0)))
        try:
            tn = float(row['T_n_K'])
        except:
            continue
        gold = gold_map.get(key)
        if gold is not None and abs(tn - gold) <= tol:
            valid += 1
    return valid / len(gold_map) if gold_map else 0.0


# === block: score_2 (check id='slope_check') ===
def score_2(artifact, step, ctx):
    slope_range = step.get('slope_range', [-4.5, -3.5])
    def extract_pairs(substrate, orient):
        pairs = []
        for row in artifact:
            if row.get('substrate_type') == substrate and row.get('orientation') == orient:
                try:
                    delta = float(row['mismatch_delta'])
                    tn = float(row['T_n_K'])
                    pairs.append((delta, tn))
                except:
                    continue
        return pairs

    def lin_slope(pairs):
        n = len(pairs)
        if n < 2:
            return None
        sx = sy = sxy = sx2 = 0.0
        for x,y in pairs:
            sx += x
            sy += y
            sxy += x*y
            sx2 += x*x
        denom = n*sx2 - sx*sx
        if abs(denom) < 1e-9:
            return None
        return (n*sxy - sx*sy) / denom

    rigid_pairs = extract_pairs('rigid', 'pII')
    wells_pairs = extract_pairs('wells', 'pII')
    slopes = []
    for pairs in (rigid_pairs, wells_pairs):
        s = lin_slope(pairs)
        if s is None:
            return 0.0
        slopes.append(s)
    # check each slope within range
    ok = all(slope_range[0] <= s <= slope_range[1] for s in slopes)
    if ok:
        return 1.0
    # partial credit: how many slopes satisfy
    score = sum(1.0 for s in slopes if slope_range[0] <= s <= slope_range[1]) / len(slopes)
    return score


# === block: score_3 (check id='ordering_flexibility') ===
def score_3(artifact, step, ctx):
    delta_vals = [5,7,8]
    count = 0
    valid = 0
    for d in delta_vals:
        tn_rig = tn_well = None
        for row in artifact:
            if row.get('orientation') != 'pII':
                continue
            try:
                if int(row['mismatch_delta']) == d:
                    tn = float(row['T_n_K'])
            except:
                continue
            if row.get('substrate_type') == 'rigid':
                tn_rig = tn
            elif row.get('substrate_type') == 'wells':
                tn_well = tn
        if tn_rig is not None and tn_well is not None:
            count += 1
            if tn_well > tn_rig:
                valid += 1
    return valid / count if count > 0 else 0.0


# === block: score_4 (check id='ordering_orientation') ===
def score_4(artifact, step, ctx):
    delta_vals = [5,7,8]
    count = 0
    valid = 0
    for d in delta_vals:
        tn_basal = tn_pI = tn_pII = None
        for row in artifact:
            if row.get('substrate_type') != 'wells':
                continue
            try:
                if int(row['mismatch_delta']) == d:
                    tn = float(row['T_n_K'])
            except:
                continue
            orient = row.get('orientation')
            if orient == 'basal':
                tn_basal = tn
            elif orient == 'pI':
                tn_pI = tn
            elif orient == 'pII':
                tn_pII = tn
        if tn_pI is not None and tn_pII is not None and tn_basal is not None:
            count += 1
            if tn_pI > tn_pII and tn_pII > tn_basal:
                valid += 1
    return valid / count if count > 0 else 0.0


_SCORERS = {
    'csv_shape': score_0,
    't_n_accuracy': score_1,
    'slope_check': score_2,
    'ordering_flexibility': score_3,
    'ordering_orientation': score_4,
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
