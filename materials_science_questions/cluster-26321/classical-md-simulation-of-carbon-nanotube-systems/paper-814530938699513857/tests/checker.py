import os
import json
import csv

# === author imports / helpers ===
import statistics, math


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
    import csv, os
    rows_by_cond = {}
    output_file = spec['output_contract']['outputs'][0]['file']
    path = os.path.join(outputs_dir, output_file)
    try:
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = (row['scheme'], float(row['temperature']))
                rows_by_cond.setdefault(key, []).append({
                    'time': float(row['time']),
                    'mid_freq': float(row['mid_rotor_frequency']),
                    'inner_freq': float(row['inner_rotor_frequency']),
                    'z_pos': float(row['inner_rotor_z_position']),
                })
    except Exception:
        pass
    return {'rows_by_cond': rows_by_cond}


# === block: score_0 (check id='stable_freq_4LR_200K') ===
def score_0(artifact, step, ctx):
    import statistics

    scheme = step['scheme']
    temperature = step['temperature']
    target = step['target_freq']
    tol = step['tolerance_relative']

    rows = None
    if 'rows_by_cond' in ctx:
        key = (scheme, temperature)
        rows = ctx['rows_by_cond'].get(key, [])

    if not rows:
        # fallback: filter the raw artifact list
        rows = [r for r in artifact if r.get('scheme') == scheme and abs(float(r.get('temperature', 0)) - temperature) < 1e-6]

    if not rows:
        return 0.0

    rows.sort(key=lambda r: float(r['time'] if 'time' in r else r.get('time', 0)))
    last_time = float(rows[-1]['time'])
    window_rows = [r for r in rows if float(r['time']) >= last_time - 1000.0]
    if not window_rows:
        return 0.0

    vals = []
    for r in window_rows:
        val = r.get('mid_freq') if 'mid_freq' in r else r.get('mid_rotor_frequency', 0.0)
        vals.append(float(val))

    mean_freq = statistics.mean(vals)
    if target == 0.0:
        return 0.0

    rel_err = abs(mean_freq - target) / target
    if rel_err <= tol:
        return 1.0
    # linear decay: full credit at rel_err <= tol, 0 at 2*tol
    score_decay = max(0.0, (2 * tol - rel_err) / tol)
    return min(1.0, score_decay)


# === block: score_1 (check id='stable_freq_4LR_300K') ===
def score_1(artifact, step, ctx):
    rows_by_cond = ctx['rows_by_cond']
    key = (step['scheme'], step['temperature'])
    if key not in rows_by_cond:
        return 0.0
    rows = rows_by_cond[key]
    rows.sort(key=lambda r: r['time'])
    last_time = rows[-1]['time']
    window_rows = [r for r in rows if r['time'] >= last_time - 1000.0]
    if not window_rows:
        return 0.0
    mean_freq = statistics.mean(r['mid_freq'] for r in window_rows)
    target = step['target_freq']
    tol = step['tolerance_relative']
    rel_err = abs(mean_freq - target) / target if target else abs(mean_freq - target)
    if rel_err <= tol:
        return 1.0
    else:
        score_decay = max(0.0, (2*tol - rel_err) / tol)
        return score_decay


# === block: score_2 (check id='temp_trend_1LR') ===
def score_2(artifact, step, ctx):
    rows_by_cond = ctx['rows_by_cond']
    scheme = step['scheme']
    temps = step['temperatures']
    means = []
    for t in temps:
        key = (scheme, t)
        if key not in rows_by_cond:
            return 0.0
        rows = rows_by_cond[key]
        rows.sort(key=lambda r: r['time'])
        last_time = rows[-1]['time']
        window_rows = [r for r in rows if r['time'] >= last_time - 1000.0]
        if not window_rows:
            return 0.0
        mean_freq = statistics.mean(r['mid_freq'] for r in window_rows)
        means.append(mean_freq)
    increasing = sum(1 for i in range(len(means)-1) if means[i] < means[i+1])
    if increasing == len(means)-1:
        return 1.0
    elif increasing == len(means)-2:
        return 0.5
    else:
        return 0.0


# === block: score_3 (check id='oscillation_amplitude_1LR_300K') ===
def score_3(artifact, step, ctx):
    rows_by_cond = ctx['rows_by_cond']
    key = (step['scheme'], step['temperature'])
    if key not in rows_by_cond:
        return 0.0
    rows = rows_by_cond[key]
    rows.sort(key=lambda r: r['time'])
    last_time = rows[-1]['time']
    window_rows = [r for r in rows if r['time'] >= last_time - 1000.0]
    if not window_rows:
        return 0.0
    z_positions = [r['z_pos'] for r in window_rows]
    amplitude = max(z_positions) - min(z_positions)
    target = step['target_amplitude']
    tol = step['tolerance_abs']
    exceed = abs(amplitude - target) - tol
    if exceed <= 0:
        return 1.0
    else:
        return max(0.0, 1.0 - exceed / tol)


# === block: score_4 (check id='stabilization_check') ===
def score_4(artifact, step, ctx):
    rows_by_cond = ctx['rows_by_cond']
    scores = []
    for key, rows_list in rows_by_cond.items():
        rows = sorted(rows_list, key=lambda r: r['time'])
        last_time = rows[-1]['time']
        window_rows = [r for r in rows if r['time'] >= last_time - 1000.0]
        if len(window_rows) < 2:
            continue
        times = [r['time'] for r in window_rows]
        freqs = [r['mid_freq'] for r in window_rows]
        slope, intercept = statistics.linear_regression(times, freqs)
        if slope > 0.001:
            scores.append(max(0.0, 1.0 - slope / 0.01))
        else:
            scores.append(1.0)
    return statistics.mean(scores) if scores else 1.0


_SCORERS = {
    'stable_freq_4LR_200K': score_0,
    'stable_freq_4LR_300K': score_1,
    'temp_trend_1LR': score_2,
    'oscillation_amplitude_1LR_300K': score_3,
    'stabilization_check': score_4,
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
