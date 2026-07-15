import os
import json
import csv

# === author imports / helpers ===
def find_nearest_index(times, target):
    import bisect
    t = [float(r.strip()) for r in times if r.strip() != '']
    if not t:
        return None
    pos = bisect.bisect_left(t, target)
    if pos == 0:
        return 0
    if pos == len(t):
        return len(t)-1
    before = t[pos-1]
    after = t[pos]
    return pos if (after - target) < (target - before) else pos-1

def compute_max_rel_diff_csv(rows, selected_times, col_no_ee, col_with_ee):
    times = [row['time_ps'] for row in rows]
    max_rel = 0.0
    for t in selected_times:
        idx = find_nearest_index(times, t)
        if idx is None:
            continue
        v1 = float(rows[idx][col_no_ee])
        v2 = float(rows[idx][col_with_ee])
        d = abs(v1 - v2)
        denom = max(abs(v1), abs(v2))
        if denom == 0.0:
            rel = 0.0 if d == 0.0 else 1.0
        else:
            rel = d / denom
        if rel > max_rel:
            max_rel = rel
    return max_rel


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
    import json
    # spec is already provided as the second argument; do not use ctx
    params = {}
    for step in spec.get('steps', []):
        params[step['id']] = step.get('parameters', {})
    return params


# === block: score_0 (check id='consistency_drift') ===
def score_0(artifact, step, ctx):
    params = step.get('parameters', {})
    tol = params.get('tolerance', 0.05)
    selected = params.get('selected_times_ps', [0.2,0.5,1.0,1.5,2.0])
    col_no = params.get('col_no_ee', 'v_drift_no_ee_cm_s')
    col_ee = params.get('col_with_ee', 'v_drift_with_ee_cm_s')
    if not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0
    max_rel = compute_max_rel_diff_csv(artifact, selected, col_no, col_ee)
    if max_rel <= tol:
        return 1.0
    # proportional decay
    return max(0.0, tol / max_rel)


# === block: score_1 (check id='consistency_temp') ===
def score_1(artifact, step, ctx):
    params = ctx.get('consistency_temp', {})
    tol = params.get('tolerance', 0.05)
    selected = params.get('selected_times_ps', [0.2,0.5,1.0,1.5,2.0])
    col_no = params.get('col_no_ee', 'Te_no_ee_K')
    col_ee = params.get('col_with_ee', 'Te_with_ee_K')
    if not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0
    max_rel = compute_max_rel_diff_csv(artifact, selected, col_no, col_ee)
    if max_rel <= tol:
        return 1.0
    return max(0.0, tol / max_rel)


# === block: score_2 (check id='consistency_valley') ===
def score_2(artifact, step, ctx):
    params = ctx.get('consistency_valley', {})
    tol = params.get('tolerance', 0.05)
    selected = params.get('selected_times_ps', [0.2,0.5,1.0,1.5,2.0])
    pairs = params.get('col_pairs', [['Gamma_no_ee','Gamma_with_ee'],['L_no_ee','L_with_ee']])
    if not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0
    max_rel = 0.0
    for pair in pairs:
        m = compute_max_rel_diff_csv(artifact, selected, pair[0], pair[1])
        if m > max_rel:
            max_rel = m
    if max_rel <= tol:
        return 1.0
    return max(0.0, tol / max_rel)


# === block: score_3 (check id='steady_vdrift') ===
def score_3(artifact, step, ctx):
    params = ctx.get('steady_vdrift', {})
    target_t = params.get('target_time_ps', 2.0)
    gold = params.get('gold_drift_cm_s', 1.0e7)
    tol = params.get('tolerance', 0.10)
    col_no = params.get('col_no_ee', 'v_drift_no_ee_cm_s')
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    times = [row['time_ps'] for row in artifact]
    idx = find_nearest_index(times, target_t)
    if idx is None:
        return 0.0
    v = float(artifact[idx][col_no])
    if v == 0.0 and gold == 0.0:
        return 1.0
    rel_err = abs(v - gold) / max(1e-30, abs(gold))
    if rel_err <= tol:
        return 1.0
    # decay proportionally
    return max(0.0, tol / rel_err)


_SCORERS = {
    'consistency_drift': score_0,
    'consistency_temp': score_1,
    'consistency_valley': score_2,
    'steady_vdrift': score_3,
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
