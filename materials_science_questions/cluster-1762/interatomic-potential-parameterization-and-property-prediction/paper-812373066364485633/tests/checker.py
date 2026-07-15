import os
import json
import csv

# === author imports / helpers ===
import math

def spearmanr(x, y):
    n = len(x)
    if n <= 1:
        return 0.0, 0.0
    def rankdata(vals):
        sorted_pairs = sorted((v, i) for i, v in enumerate(vals))
        ranks = [0] * n
        for rank, (val, i) in enumerate(sorted_pairs, start=1):
            ranks[i] = rank
        return ranks
    x_ranks = rankdata(x)
    y_ranks = rankdata(y)
    mx = sum(x_ranks) / n
    my = sum(y_ranks) / n
    num = sum((rx - mx) * (ry - my) for rx, ry in zip(x_ranks, y_ranks))
    den = math.sqrt(sum((rx - mx)**2 for rx in x_ranks) * sum((ry - my)**2 for ry in y_ranks))
    if den == 0.0:
        return 0.0, 0.0
    corr = num / den
    return corr, 0.0


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


# === block: score_0 (check id='step_calib_Y') ===
def score_0(artifact, step, ctx):
    for row in artifact:
        if row['compound'] == step['compound']:
            break
    else:
        return 0.0
    if abs(float(row['u']) - step['gold_u']) <= step['tolerance'] and abs(float(row['v']) - step['gold_v']) <= step['tolerance']:
        return 1.0
    return 0.0


# === block: score_1 (check id='step_calib_Nd') ===
def score_1(artifact, step, ctx):
    for row in artifact:
        if row['compound'] == step['compound']:
            break
    else:
        return 0.0
    if abs(float(row['u']) - step['gold_u']) <= step['tolerance'] and abs(float(row['v']) - step['gold_v']) <= step['tolerance']:
        return 1.0
    return 0.0


# === block: score_2 (check id='step_calib_Er') ===
def score_2(artifact, step, ctx):
    for row in artifact:
        if row['compound'] == step['compound']:
            break
    else:
        return 0.0
    if abs(float(row['u']) - step['gold_u']) <= step['tolerance'] and abs(float(row['v']) - step['gold_v']) <= step['tolerance']:
        return 1.0
    return 0.0


# === block: score_3 (check id='step_trend') ===
def score_3(artifact, step, ctx):
    required = set(step['required_compounds'])
    compounds_in_csv = [row['compound'] for row in artifact]
    if set(compounds_in_csv) != required:
        return 0.0
    lanth_rows = [row for row in artifact if 58 <= int(row['Z']) <= 71]
    if not lanth_rows:
        return 0.0
    Z = [int(r['Z']) for r in lanth_rows]
    u_vals = [float(r['u']) for r in lanth_rows]
    v_vals = [float(r['v']) for r in lanth_rows]
    corr_u, _ = spearmanr(Z, u_vals)
    corr_v, _ = spearmanr(Z, v_vals)
    score_u = (corr_u + 1) / 2.0 if not hasattr(math, 'isnan') or not math.isnan(corr_u) else 0.0
    score_v = (1 - corr_v) / 2.0 if not math.isnan(corr_v) else 0.0
    score_u = max(0.0, min(1.0, score_u))
    score_v = max(0.0, min(1.0, score_v))
    return 0.5 * score_u + 0.5 * score_v


_SCORERS = {
    'step_calib_Y': score_0,
    'step_calib_Nd': score_1,
    'step_calib_Er': score_2,
    'step_trend': score_3,
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
