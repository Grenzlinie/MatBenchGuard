import os
import json
import csv

# === author imports / helpers ===
import math
import bisect


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


# === block: score_0 (check id='energies_structure') ===
def score_0(artifact, step, ctx):
    rows = artifact
    cols = step.get('params', {}).get('expected_columns', [])
    min_rows = step.get('params', {}).get('min_rows', 8)
    coverage_range = step.get('params', {}).get('coverage_range', [0.002, 0.07])
    neg = step.get('params', {}).get('negativity', True)
    mono_dec = step.get('params', {}).get('monotonic') == 'decreasing'
    score = 0.0
    if cols and rows:
        actual = set(rows[0].keys())
        req = set(cols)
        if req.issubset(actual):
            score += 0.2
    if len(rows) >= min_rows:
        score += 0.2
    try:
        c_vals = [float(r[cols[0]]) for r in rows]
        if all(coverage_range[0] <= c <= coverage_range[1] for c in c_vals):
            score += 0.2
    except:
        pass
    try:
        e_vals = [float(r[cols[1]]) for r in rows]
        if all(v < 0 for v in e_vals):
            score += 0.2
    except:
        pass
    try:
        pairs = sorted(zip(c_vals, e_vals), key=lambda x: x[0])
        if all(pairs[i][1] >= pairs[i+1][1] for i in range(len(pairs)-1)):
            score += 0.2
    except:
        pass
    return score


# === block: score_1 (check id='energies_values') ===
def score_1(artifact, step, ctx):
    rows = artifact
    params = step.get('params', {})
    rel_tol = params.get('relative_tolerance', 0.15)
    abs_floor = params.get('absolute_floor', 0.2)
    gold_curve = params.get('gold_curve', [])
    if not gold_curve or not rows:
        return 0.0
    gold_x = [p[0] for p in gold_curve]
    gold_y = [p[1] for p in gold_curve]
    def interpolate(x):
        if x <= gold_x[0]:
            return gold_y[0]
        if x >= gold_x[-1]:
            return gold_y[-1]
        i = bisect.bisect_left(gold_x, x)
        x0, x1 = gold_x[i-1], gold_x[i]
        y0, y1 = gold_y[i-1], gold_y[i]
        return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    scores = []
    for row in rows:
        try:
            cov = float(row['coverage_A-2'])
            e = float(row['E_N_K'])
            expected = interpolate(cov)
            err = abs(e - expected)
            threshold = rel_tol * abs(expected) + abs_floor
            scores.append(1.0 if err <= threshold else 0.0)
        except:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='mass_structure') ===
def score_2(artifact, step, ctx):
    rows = artifact
    params = step.get('params', {})
    cols = params.get('expected_columns', [])
    min_rows = params.get('min_rows', 8)
    coverage_range = params.get('coverage_range', [0.002, 0.07])
    min_mass = params.get('min_mass', 1.0)
    score = 0.0
    if cols and rows:
        actual = set(rows[0].keys())
        req = set(cols)
        if req.issubset(actual):
            score += 0.25
    if len(rows) >= min_rows:
        score += 0.25
    try:
        c_vals = [float(r[cols[0]]) for r in rows]
        if all(coverage_range[0] <= c <= coverage_range[1] for c in c_vals):
            score += 0.25
    except:
        pass
    try:
        m_vals = [float(r[cols[1]]) for r in rows]
        if all(v >= min_mass for v in m_vals):
            score += 0.25
    except:
        pass
    return score


# === block: score_3 (check id='mass_values') ===
def score_3(artifact, step, ctx):
    rows = artifact
    params = step.get('params', {})
    rel_tol = params.get('relative_tolerance', 0.20)
    abs_floor = params.get('absolute_floor', 0.05)
    gold_curve = params.get('gold_curve', [])
    if not gold_curve or not rows:
        return 0.0
    gold_x = [p[0] for p in gold_curve]
    gold_y = [p[1] for p in gold_curve]
    def interpolate(x):
        if x <= gold_x[0]:
            return gold_y[0]
        if x >= gold_x[-1]:
            return gold_y[-1]
        i = bisect.bisect_left(gold_x, x)
        x0, x1 = gold_x[i-1], gold_x[i]
        y0, y1 = gold_y[i-1], gold_y[i]
        return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    scores = []
    for row in rows:
        try:
            cov = float(row['coverage_A-2'])
            m = float(row['m_star_mHe'])
            expected = interpolate(cov)
            err = abs(m - expected)
            threshold = rel_tol * abs(expected) + abs_floor
            scores.append(1.0 if err <= threshold else 0.0)
        except:
            scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'energies_structure': score_0,
    'energies_values': score_1,
    'mass_structure': score_2,
    'mass_values': score_3,
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
