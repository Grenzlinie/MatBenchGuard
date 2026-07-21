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
    import json
    spec_path = "/tests/grading_spec.json"
    with open(spec_path) as f:
        spec = json.load(f)
    ctx = {"gold": spec.get("gold", {})}
    return ctx


# === block: score_0 (check id='step_zero_T_phases') ===
def score_0(artifact, step, ctx):
    import csv, os
    artifact_path = "/app/outputs/zero_T_phases.csv"
    if not os.path.exists(artifact_path):
        return 0.0
    rows = []
    with open(artifact_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    if len(rows) == 0:
        return 0.0
    req_cols = ['alpha1','alpha2','stable_phase']
    if not all(c in rows[0] for c in req_cols):
        return 0.0
    expected_pairs = []
    for a1 in [round(x*0.1,1) for x in range(0,21)]:
        for a2 in [round(x*0.1,1) for x in range(0,21)]:
            expected_pairs.append((a1,a2))
    agent_phases = {}
    for r in rows:
        try:
            a1 = round(float(r['alpha1']),1)
            a2 = round(float(r['alpha2']),1)
        except:
            continue
        agent_phases[(a1,a2)] = r['stable_phase'].strip()
    present = 0
    total = len(expected_pairs)
    for pair in expected_pairs:
        if pair in agent_phases:
            present += 1
    grid_score = present / max(total,1)
    checkpoints = ctx['gold']['zero_T_checkpoints']
    correct = 0
    for cp in checkpoints:
        a1 = cp['alpha1']
        a2 = cp['alpha2']
        expected = cp['expected_phase']
        phase = agent_phases.get((round(a1,1), round(a2,1)), '')
        if phase == expected:
            correct += 1
    checkpoint_score = correct / max(len(checkpoints),1)
    return 0.3 * grid_score + 0.7 * checkpoint_score


# === block: score_1 (check id='step_transition_temperatures') ===
def score_1(artifact, step, ctx):
    import csv, os
    artifact_path = "/app/outputs/transition_temperatures.csv"
    if not os.path.exists(artifact_path):
        return 0.0
    rows = []
    with open(artifact_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    if len(rows) == 0:
        return 0.0
    req_cols = ['alpha1','alpha2','T_c']
    if not all(c in rows[0] for c in req_cols):
        return 0.0
    gold_data = ctx['gold']['transition_T_c']
    tolerance = gold_data.get('tolerance', 0.05)
    gold_tc = {k: v for k,v in gold_data.items() if k != 'tolerance'}
    tc_matches = 0
    total = len(gold_tc)
    for key, expected_tc in gold_tc.items():
        a1, a2 = map(float, key.split('_'))
        for r in rows:
            try:
                row_a1 = round(float(r['alpha1']),2)
                row_a2 = round(float(r['alpha2']),2)
                if abs(row_a1 - a1) < 0.005 and abs(row_a2 - a2) < 0.005:
                    tc = float(r['T_c'])
                    if abs(tc - expected_tc) <= tolerance:
                        tc_matches += 1
                    break
            except:
                continue
    return tc_matches / max(total,1)


# === block: score_2 (check id='step_susceptibility_trend') ===
def score_2(artifact, step, ctx):
    import csv, os
    artifact_path = "/app/outputs/susceptibility_trend.csv"
    if not os.path.exists(artifact_path):
        return 0.0
    rows = []
    with open(artifact_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    if len(rows) == 0:
        return 0.0
    req_cols = ['alpha1','alpha2','T','chi']
    if not all(c in rows[0] for c in req_cols):
        return 0.0
    chi_by_T = {}
    for r in rows:
        try:
            T_val = float(r['T'])
            chi_val = float(r['chi'])
            chi_by_T[T_val] = chi_val
        except:
            continue
    if 0.2 in chi_by_T and 0.6 in chi_by_T:
        return 1.0 if chi_by_T[0.6] > chi_by_T[0.2] else 0.0
    else:
        return 0.0


_SCORERS = {
    'step_zero_T_phases': score_0,
    'step_transition_temperatures': score_1,
    'step_susceptibility_trend': score_2,
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
