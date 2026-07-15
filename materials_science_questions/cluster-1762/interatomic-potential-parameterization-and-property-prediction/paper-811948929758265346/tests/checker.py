import os
import json
import csv

# === author imports / helpers ===
import json, csv, math


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
    spec = json.load(open('/tests/grading_spec.json'))
    gold_table = spec.get('gold_table', {})
    # ensure keys are strings
    if gold_table:
        gold_table = {str(k): v for k, v in gold_table.items()}
    return {'gold_table': gold_table, 'spec': spec}


# === block: score_0 (check id='static_results') ===
def score_0(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    if not rows:
        return 0.0
    gold_table = ctx['gold_table']
    tol = ctx['spec']['steps'][0]['tolerance_spec']  # step id static_results
    agent = {}
    for r in rows:
        try:
            a = str(float(r['alpha']))
            agent[a] = r
        except (ValueError, KeyError):
            continue
    alphas = sorted(gold_table.keys(), key=lambda x: float(x))
    total_checks = 0
    passed = 0
    for a in alphas:
        if a not in agent:
            continue
        row = agent[a]
        gold = gold_table[a]
        for key in gold:
            if key not in row:
                continue
            try:
                val = float(row[key])
            except (ValueError, TypeError):
                continue
            gval = float(gold[key])
            if key in tol:
                t = tol[key]
                if 'abs' in t:
                    ok = abs(val - gval) <= t['abs']
                elif 'rel' in t:
                    denom = max(abs(gval), 1e-6)
                    ok = abs(val - gval) / denom <= t['rel']
                else:
                    ok = abs(val - gval) <= 1e-6
            else:
                ok = abs(val - gval) <= 1e-4
            total_checks += 1
            if ok:
                passed += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


# === block: score_1 (check id='lattice_frequencies') ===
def score_1(artifact, step, ctx):
    rows = artifact if isinstance(artifact, list) else []
    if not rows:
        return 0.0
    spec = ctx['spec']['steps'][1]
    expected_reps = set(spec['expected_representations'])
    mode_counts = spec['mode_counts']
    acoustic_reps = set(spec['acoustic_reps'])
    zero_thresh = spec['zero_threshold_cm-1']
    exp_alphas = set([str(i/10.0) for i in range(28, 41)])
    agent_alphas = set()
    rep_counts = {}
    score = 0.0
    total_checks = 0
    def inc(val):
        nonlocal score, total_checks
        score += val
        total_checks += 1
    # column check
    if all(col in (rows[0] if rows else {}) for col in ['alpha','representation','frequency_cm-1']):
        inc(1.0)
    else:
        inc(0.0)
    for row in rows:
        try:
            alpha = str(float(row['alpha']))
            rep = row['representation']
            freq = float(row['frequency_cm-1'])
        except (ValueError, KeyError):
            continue
        agent_alphas.add(alpha)
        rep_counts.setdefault(rep, []).append(freq)
    # alpha set check
    if agent_alphas == exp_alphas:
        inc(1.0)
    else:
        inc(max(0.0, 1.0 - 0.1*abs(len(agent_alphas) - len(exp_alphas))))
    # representation validity
    valid_reps = expected_reps
    for rep in rep_counts:
        if rep in valid_reps:
            inc(1.0)
        else:
            inc(0.0)
    # mode counts
    for rep, cnt in mode_counts.items():
        if rep in rep_counts and len(rep_counts[rep]) == cnt:
            inc(1.0)
        else:
            inc(0.0)
    # non-negative frequencies
    nonneg = all(f >= -1e-6 for f in [f for flist in rep_counts.values() for f in flist])
    inc(1.0 if nonneg else 0.0)
    # acoustic zeros
    acoustic_ok = True
    for rep in acoustic_reps:
        freqs = rep_counts.get(rep, [])
        if not freqs:
            acoustic_ok = False
            continue
        if any(abs(f) > zero_thresh for f in freqs):
            acoustic_ok = False
    inc(1.0 if acoustic_ok else 0.0)
    if total_checks == 0:
        return 0.0
    return score / total_checks


_SCORERS = {
    'static_results': score_0,
    'lattice_frequencies': score_1,
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
