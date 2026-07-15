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
    return {}


# === block: score_0 (check id='step_lattice') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    points = []
    for row in rows:
        try:
            x = float(row['x'])
            a = float(row['a'])
        except (ValueError, KeyError):
            continue
        points.append((x, a))
    if len(points) < 2:
        return 0.0
    points.sort(key=lambda p: p[0])
    # coverage: must span most of the doping range
    x_first = points[0][0]
    x_last = points[-1][0]
    if x_first > 0.05 or x_last < 0.35:
        return 0.0
    # physically plausible range for Ce1-xSmxO2-x/2 at room temperature
    for _, a in points:
        if a < 5.38 or a > 5.50:
            return 0.0
    # monotonic increase (allow negligible rounding)
    prev_a = points[0][1]
    for _, a in points[1:]:
        if a < prev_a - 0.001:
            return 0.0
        prev_a = a
    # simple linear regression --- slope and R²
    n = len(points)
    sum_x = sum(p[0] for p in points)
    sum_a = sum(p[1] for p in points)
    sum_x2 = sum(p[0]**2 for p in points)
    sum_xa = sum(p[0]*p[1] for p in points)
    denom = n * sum_x2 - sum_x**2
    if abs(denom) < 1e-15:
        return 0.0
    slope = (n * sum_xa - sum_x * sum_a) / denom
    intercept = (sum_a - slope * sum_x) / n
    if not (0.05 < slope < 0.15):
        return 0.0
    mean_a = sum_a / n
    ss_res = sum((a - (slope * x + intercept))**2 for x, a in points)
    ss_tot = sum((a - mean_a)**2 for _, a in points)
    if ss_tot <= 0:
        return 0.0
    r2 = 1.0 - ss_res / ss_tot
    if r2 < 0.90:
        return 0.0
    return 1.0


# === block: score_1 (check id='step_assoc') ===
def score_1(artifact, step, ctx):
    gold_list = step['gold']; tol = step['tolerance']; key = step['key']; val_key = step['value_key']; rows = artifact
    row_map = {}
    for row in rows:
        try:
            k = row[key].strip()
            v = float(row[val_key])
        except (ValueError, KeyError):
            continue
        row_map[k] = v
    correct = 0
    for item in gold_list:
        k = item[key]
        ref = item[val_key]
        v = row_map.get(k)
        if v is not None and abs(v - ref) <= tol:
            correct += 1
    return correct / len(gold_list) if gold_list else 0.0


# === block: score_2 (check id='step_mig') ===
def score_2(artifact, step, ctx):
    gold_list = step['gold']; tol = step['tolerance']; key = step['key']; val_key = step['value_key']; rows = artifact
    row_map = {}
    for row in rows:
        try:
            k = row[key].strip()
            v = float(row[val_key])
        except (ValueError, KeyError):
            continue
        row_map[k] = v
    correct = 0
    for item in gold_list:
        k = item[key]
        ref = item[val_key]
        v = row_map.get(k)
        if v is not None and abs(v - ref) <= tol:
            correct += 1
    return correct / len(gold_list) if gold_list else 0.0


# === block: score_3 (check id='step_trap') ===
def score_3(artifact, step, ctx):
    gold_list = step['gold']; tol = step['tolerance']; key = step['key']; val_key = step['value_key']; rows = artifact
    row_map = {}
    for row in rows:
        try:
            k = row[key].strip()
            v = float(row[val_key])
        except (ValueError, KeyError):
            continue
        row_map[k] = v
    correct = 0
    for item in gold_list:
        k = item[key]
        ref = item[val_key]
        v = row_map.get(k)
        if v is not None and abs(v - ref) <= tol:
            correct += 1
    return correct / len(gold_list) if gold_list else 0.0


# === block: score_4 (check id='step_cond') ===
def score_4(artifact, step, ctx):
    gold = step['gold']; x_vals = gold['x_vals']; sigma_refs = gold['sigma_vals']; rows = artifact
    if not rows: return 0.0
    row_by_x = {}
    max_sigma = -1.0
    peak_x = None
    for row in rows:
        try:
            x = float(row['x'])
            s = float(row['sigma'])
        except (ValueError, KeyError):
            continue
        row_by_x[x] = s
    factor_score = 0.0
    for x, ref in zip(x_vals, sigma_refs):
        s = row_by_x.get(x)
        if s is not None and ref > 0 and s > 0:
            ratio = s / ref
            if 0.5 <= ratio <= 2.0:
                factor_score += 1.0
        elif s is not None and ref == 0:
            if s == 0:
                factor_score += 1.0
    factor_frac = factor_score / len(x_vals) if x_vals else 0.0
    # peak location: target is the x where gold sigma is maximal
    try:
        peak_target = x_vals[sigma_refs.index(max(sigma_refs))]
    except (ValueError, IndexError):
        peak_target = 0.15
    peak_tol = step.get('peak_tolerance', 0.02)
    for x, s in row_by_x.items():
        if s > max_sigma:
            max_sigma = s
            peak_x = x
    if peak_x is not None and abs(peak_x - peak_target) <= peak_tol:
        peak_ok = 1.0
    else:
        peak_ok = 0.0
    return 0.7 * factor_frac + 0.3 * peak_ok


_SCORERS = {
    'step_lattice': score_0,
    'step_assoc': score_1,
    'step_mig': score_2,
    'step_trap': score_3,
    'step_cond': score_4,
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
