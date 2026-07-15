import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, statistics, math


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


# === block: score_0 (check id='size_k_sanity') ===
def score_0(artifact, step, ctx):
    import collections
    fn = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(fn):
        return 0.0
    with open(fn, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        return 0.0
    score = 0.0
    cols = set(reader.fieldnames)
    required = {'direction', 'length_nm', 'k_W_per_mK'}
    if required.issubset(cols):
        score += 0.3
    groups = collections.defaultdict(list)
    for r in rows:
        dir_ = r.get('direction', '').strip()
        try:
            L = float(r['length_nm'])
            k = float(r['k_W_per_mK'])
        except (ValueError, KeyError):
            continue
        groups[dir_].append((L, k))
    valid_dirs = 0
    for d in ['a*','b*','c*']:
        pts = groups.get(d, [])
        if len(pts) >= 3:
            valid_dirs += 1
    score += (valid_dirs / 3.0) * 0.3
    monotonic_dirs = 0
    for d in ['a*','b*','c*']:
        pts = sorted(groups.get(d, []), key=lambda x: x[0])
        if len(pts) < 2:
            continue
        if all(pts[i][1] <= pts[i+1][1] for i in range(len(pts)-1)):
            monotonic_dirs += 1
    if valid_dirs > 0:
        score += (monotonic_dirs / valid_dirs) * 0.4
    return min(1.0, score)


# === block: score_1 (check id='bulk_k_recompute') ===
def score_1(artifact, step, ctx):
    fn_csv = os.path.join('/app/outputs', 'size_dependent_k.csv')
    if not os.path.exists(fn_csv):
        return 0.0
    with open(fn_csv, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    data = {d: [] for d in ['a*','b*','c*']}
    for r in rows:
        d = r.get('direction','').strip()
        if d not in data:
            continue
        try:
            L = float(r['length_nm'])
            k = float(r['k_W_per_mK'])
        except (ValueError, KeyError):
            continue
        if k <= 0 or L <= 0:
            continue
        data[d].append((L, k))
    targets = step.get('target', {})
    tol_rel = float(step.get('tolerance_rel', 0.2))
    scores = []
    for d in ['a*','b*','c*']:
        pts = data[d]
        if len(pts) < 3:
            scores.append(0.0)
            continue
        x = [1.0/L for L,_ in pts]
        y = [1.0/k for _,k in pts]
        n = len(x)
        sx = sum(x)
        sy = sum(y)
        sxx = sum(xi*xi for xi in x)
        sxy = sum(xi*yi for xi,yi in zip(x,y))
        denom = n*sxx - sx*sx
        if abs(denom) < 1e-30:
            scores.append(0.0)
            continue
        intercept = (sxx*sy - sx*sxy) / denom
        if intercept <= 0:
            scores.append(0.0)
            continue
        k_bulk_computed = 1.0 / intercept
        target_val = targets.get(d)
        if target_val is None:
            scores.append(0.0)
            continue
        rel_err = abs(k_bulk_computed - target_val) / target_val
        max_err = tol_rel
        if rel_err <= tol_rel:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (rel_err - tol_rel) / (tol_rel)))  # linear decay beyond tolerance
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='tbr_check') ===
def score_2(artifact, step, ctx):
    fn = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(fn):
        return 0.0
    with open(fn) as f:
        data = json.load(f)
    fields = step.get('fields', ['a*-b*', 'a*-c*', 'b*-c*'])
    targets = step.get('target', {})
    tol = float(step.get('tolerance_abs', 0.5e-9))
    scores = []
    for field in fields:
        if field not in data:
            scores.append(0.0)
            continue
        entry = data[field]
        mean_val = entry.get('mean_TBR')
        if mean_val is None:
            scores.append(0.0)
            continue
        target_val = targets.get(field)
        if target_val is None:
            scores.append(0.0)
            continue
        err = abs(float(mean_val) - target_val)
        if err <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (err - tol) / tol))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='vacancy_check') ===
def score_3(artifact, step, ctx):
    fn = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(fn):
        return 0.0
    with open(fn) as f:
        data = json.load(f)
    fields = step.get('fields', ['a*','b*','c*'])
    sub = step.get('subfield', 'reduction_percent')
    targets = step.get('target', {})
    tol = float(step.get('tolerance_abs', 8.0))
    scores = []
    for field in fields:
        if field not in data:
            scores.append(0.0)
            continue
        val = data[field].get(sub)
        if val is None:
            scores.append(0.0)
            continue
        target_val = targets.get(field)
        if target_val is None:
            scores.append(0.0)
            continue
        err = abs(float(val) - target_val)
        if err <= tol:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (err - tol) / tol))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'size_k_sanity': score_0,
    'bulk_k_recompute': score_1,
    'tbr_check': score_2,
    'vacancy_check': score_3,
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
