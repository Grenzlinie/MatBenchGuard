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


# === block: score_0 (check id='bond_lengths') ===
def score_0(artifact, step, ctx):
    gold = step['params']['gold_table']
    tol = step['params']['tolerance']
    col = step['params']['column']
    # build lookup
    art_map = {}
    for row in artifact:
        try:
            key = (row['X'].strip(), row['species'].strip())
            val = float(row[col])
            art_map[key] = val
        except (ValueError, KeyError):
            continue
    scores = []
    for g in gold:
        gx = (g['X'], g['species'])
        if gx not in art_map:
            scores.append(0.0)
            continue
        err = abs(art_map[gx] - g[col])
        if err < 1e-12:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - err / tol))
    if not scores:
        return 0.0
    mean_val = sum(scores) / len(scores)
    # trend: radical bond < closed‑shell for every X
    all_X = set(g['X'] for g in gold)
    trend_ok = True
    for x in all_X:
        r_ch3x = art_map.get((x, 'CH3X'))
        r_dot = art_map.get((x, 'dotCH2X'))
        r_ch3xh = art_map.get((x, 'CH3XH+'))
        r_doth = art_map.get((x, 'dotCH2XH+'))
        if r_ch3x is not None and r_dot is not None:
            if r_dot >= r_ch3x - 1e-6:
                trend_ok = False
        if r_ch3xh is not None and r_doth is not None:
            if r_doth >= r_ch3xh - 1e-6:
                trend_ok = False
    penalty = 0.2 if not trend_ok else 0.0
    return max(0.0, mean_val - penalty)


# === block: score_1 (check id='rse') ===
def score_1(artifact, step, ctx):
    gold = step['params']['gold_table']
    tol = step['params']['tolerance']
    col = step['params']['column']
    art_map = {}
    for row in artifact:
        try:
            key = (row['X'].strip(), row['state'].strip())
            val = float(row[col])
            art_map[key] = val
        except (ValueError, KeyError):
            continue
    scores = []
    for g in gold:
        gx = (g['X'], g['state'])
        if gx not in art_map:
            scores.append(0.0)
            continue
        err = abs(art_map[gx] - g[col])
        if err < 1e-12:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - err / tol))
    if not scores:
        return 0.0
    mean_val = sum(scores) / len(scores)
    # trend: pi-donors RSE(dotCH2XH+) < 0, pi-acceptors > 0
    pi_donors = {'NH2','OH','OCH3','PH2','SH','F','Cl','Br'}
    pi_acceptors = {'CN','CHO','NO2'}
    trend_ok = True
    for x in pi_donors:
        v = art_map.get((x, 'dotCH2XH+'))
        if v is not None and v >= 0:
            trend_ok = False
    for x in pi_acceptors:
        v = art_map.get((x, 'dotCH2XH+'))
        if v is not None and v <= 0:
            trend_ok = False
    penalty = 0.2 if not trend_ok else 0.0
    return max(0.0, mean_val - penalty)


# === block: score_2 (check id='pa') ===
def score_2(artifact, step, ctx):
    gold = step['params']['gold_table']
    tol = step['params']['tolerance']
    col = step['params']['column']
    art_map = {}
    for row in artifact:
        try:
            key = (row['X'].strip(), row['species'].strip())
            val = float(row[col])
            art_map[key] = val
        except (ValueError, KeyError):
            continue
    scores = []
    for g in gold:
        gx = (g['X'], g['species'])
        if gx not in art_map:
            scores.append(0.0)
            continue
        err = abs(art_map[gx] - g[col])
        if err < 1e-12:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - err / tol))
    if not scores:
        return 0.0
    mean_val = sum(scores) / len(scores)
    # trend: for pi-donors, PA(dotCH2X) < PA(CH3X)
    pi_donors = {'NH2','OH','OCH3','PH2','SH','F','Cl','Br'}
    trend_ok = True
    for x in pi_donors:
        pa_ch3 = art_map.get((x, 'CH3X'))
        pa_dot = art_map.get((x, 'dotCH2X'))
        if pa_ch3 is not None and pa_dot is not None:
            if pa_dot >= pa_ch3:
                trend_ok = False
    penalty = 0.2 if not trend_ok else 0.0
    return max(0.0, mean_val - penalty)


# === block: score_3 (check id='hof') ===
def score_3(artifact, step, ctx):
    gold = step['params']['gold_table']
    tol = step['params']['tolerance']
    col = step['params']['column']
    art_map = {}
    for row in artifact:
        try:
            key = (row['X'].strip(), row['species'].strip())
            val = float(row[col])
            art_map[key] = val
        except (ValueError, KeyError):
            continue
    scores = []
    for g in gold:
        gx = (g['X'], g['species'])
        if gx not in art_map:
            scores.append(0.0)
            continue
        err = abs(art_map[gx] - g[col])
        if err < 1e-12:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - err / tol))
    if not scores:
        return 0.0
    mean_val = sum(scores) / len(scores)
    return mean_val


_SCORERS = {
    'bond_lengths': score_0,
    'rse': score_1,
    'pa': score_2,
    'hof': score_3,
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
