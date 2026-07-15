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
    gold_hoop = spec['steps'][0]['gold']
    gold_crack = spec['steps'][1]['gold']
    return {'hoop': gold_hoop, 'crack': gold_crack}


# === block: score_0 (check id='hoop_stress') ===
def score_0(artifact, step, ctx):
    gold = ctx['hoop']
    times_gold = gold['times']
    rows = {str(r['time']): r for r in artifact}

    def _get_vals(values_key):
        result = []
        for t in times_gold:
            key = str(t)
            if key not in rows:
                return None
            try:
                v = float(rows[key][values_key])
            except (KeyError, ValueError):
                return None
            result.append(v)
        return result

    vals_A = _get_vals('hoop_stress_A')
    vals_B = _get_vals('hoop_stress_B')
    if vals_A is None or vals_B is None:
        return 0.0

    # Pointwise accuracy
    point_scores = []
    for i, t in enumerate(times_gold):
        for vals, gold_vals in [(vals_A, gold['hoop_stress_A']), (vals_B, gold['hoop_stress_B'])]:
            gv = gold_vals[i]
            val = vals[i]
            tol = max(0.2, 0.2 * abs(gv))
            point_scores.append(1.0 if abs(val - gv) <= tol else 0.0)
    accuracy = sum(point_scores) / len(point_scores) if point_scores else 0.0

    # Transition to tension at t=6s
    idx6 = times_gold.index(6.0) if 6.0 in times_gold else None
    transition = 1.0 if (idx6 is not None and vals_A[idx6] > 0 and vals_B[idx6] > 0) else 0.0

    # Monotonicity after t=4s
    start_mono = 1  # index of t=4s (first time after 2s)
    def _is_monotonic(vals, start):
        for i in range(start, len(vals)-1):
            if vals[i+1] < vals[i] - 1e-9:
                return 0.0
        return 1.0
    mono_A = _is_monotonic(vals_A, start_mono)
    mono_B = _is_monotonic(vals_B, start_mono)

    # Stress at B > stress at A for t>=6s
    idx_B_larger = None
    for i, t in enumerate(times_gold):
        if t >= 6.0:
            idx_B_larger = i
            break
    b_larger = 1.0
    if idx_B_larger is not None:
        for i in range(idx_B_larger, len(times_gold)):
            if vals_B[i] < vals_A[i] - 1e-9:
                b_larger = 0.0
                break
    else:
        b_larger = 0.0

    # Combine with reduced weight on raw accuracy, increased on structural consistency
    score = 0.5 * accuracy + 0.1 * transition + 0.15 * mono_A + 0.15 * mono_B + 0.1 * b_larger
    return score


# === block: score_1 (check id='crack_length') ===
def score_1(artifact, step, ctx):
    gold = ctx['crack']
    socs = [str(s) for s in gold['socs']]
    rows = {str(r['soc']): r for r in artifact}
    agent_lengths = []
    gold_lengths = []
    for i, soc in enumerate(gold['socs']):
        key = str(soc)
        if key not in rows:
            return 0.0
        try:
            al = float(rows[key]['crack_length'])
        except (KeyError, ValueError):
            return 0.0
        agent_lengths.append(al)
        gold_lengths.append(gold['crack_length'][i])
    # accuracy
    score_i = []
    for al, gl in zip(agent_lengths, gold_lengths):
        if gl > 0:
            e = abs(al - gl) / max(abs(gl), 1e-9)
            si = max(0.0, 1.0 - e / 0.30)
            score_i.append(si)
        else:
            score_i.append(1.0 if al <= 0.02 else 0.0)
    accuracy = sum(score_i) / len(score_i) if score_i else 0.0
    # monotonic
    monotonic = 1.0
    for i in range(1, len(agent_lengths)):
        if agent_lengths[i] < agent_lengths[i-1] - 1e-9:
            monotonic = 0.0
            break
    # soc range of first crack
    first_soc_idx = None
    for i, al in enumerate(agent_lengths):
        if al > 0.005:
            first_soc_idx = i
            break
    if first_soc_idx is not None:
        first_soc = gold['socs'][first_soc_idx]
        if 0.12 <= first_soc <= 0.28:
            soc_range_score = 1.0
        else:
            soc_range_score = 0.0
    else:
        soc_range_score = 0.0
    return 0.6 * accuracy + 0.2 * monotonic + 0.2 * soc_range_score


_SCORERS = {
    'hoop_stress': score_0,
    'crack_length': score_1,
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
