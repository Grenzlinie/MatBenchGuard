import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import json
    artifact = load_artifact(os.path.join('/app/outputs', step['output_file']))
    if artifact is None or not isinstance(artifact, dict):
        return 0.0
    gold = step.get('gold', {})
    tolerance = step.get('tolerance_abs', {})
    a_ok = abs(artifact.get('a', 0) - gold['a']) <= tolerance.get('a', 0.02)
    c_ok = abs(artifact.get('c', 0) - gold['c']) <= tolerance.get('c', 0.02)
    te_ok = artifact.get('Te', -999) == gold.get('Te', 0)
    if not te_ok:
        return 0.0
    score = (float(a_ok) + float(c_ok)) / 2.0
    return score


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    import csv, math
    artifact = load_artifact(os.path.join('/app/outputs', step['output_file']))
    if not artifact or not isinstance(artifact, list):
        return 0.0
    gold_modes = step.get('gold_modes', {})
    tol = step.get('tolerance_abs', 2.0)
    total = len(gold_modes)
    if total == 0:
        return 0.0
    scores = []
    for row in artifact:
        mode = row.get('mode', '').strip()
        val_str = row.get('omega_meV', '')
        if mode not in gold_modes:
            continue
        try:
            val = float(val_str)
        except:
            continue
        err = abs(val - gold_modes[mode])
        scores.append(max(0.0, 1.0 - err / tol))
    if len(scores) == 0:
        return 0.0
    return sum(scores) / total


# === block: score_2 (check id='step_05') ===
def score_2(artifact, step, ctx):
    import csv, math
    artifact = load_artifact(os.path.join('/app/outputs', step['output_file']))
    if not artifact or not isinstance(artifact, list):
        return 0.0
    # The paper reports DFPT gold only for modes I, II, III, V at Te=4 eV
    # (modes IV and VI are not published in Table III).  Score only those.
    scored_modes = {'I', 'II', 'III', 'V'}
    gold_modes = step.get('gold_modes', {})
    tol = step.get('tolerance_abs', 2.0)
    # Build a filtered gold dict containing only the modes we can score.
    valid_gold = {m: v for m, v in gold_modes.items() if m in scored_modes}
    if not valid_gold:
        return 0.0
    total = len(valid_gold)
    scores = []
    for row in artifact:
        mode = row.get('mode', '').strip()
        val_str = row.get('omega_meV', '')
        if mode not in valid_gold:
            continue
        try:
            val = float(val_str)
        except:
            continue
        err = abs(val - valid_gold[mode])
        scores.append(max(0.0, 1.0 - err / tol))
    if len(scores) == 0:
        return 0.0
    return sum(scores) / total


# === block: score_3 (check id='step_06') ===
def score_3(artifact, step, ctx):
    import csv, math
    artifact = load_artifact(os.path.join('/app/outputs', step['output_file']))
    if not artifact or not isinstance(artifact, list):
        return 0.0
    gold_rows = step.get('gold_rows', [])
    tol = step.get('tolerance_abs', 2.0)
    if not gold_rows:
        return 0.0
    gold_by_pnn = {str(row['pNN']): row for row in gold_rows}
    num_gold = len(gold_rows)
    num_matched = 0
    score_sum = 0.0
    for row in artifact:
        pnn = str(row.get('pNN', '')).strip()
        if pnn not in gold_by_pnn:
            continue
        gold = gold_by_pnn[pnn]
        for col in ['Te0_omega_I_meV', 'Te4_omega_I_meV']:
            try:
                agent_val = float(row.get(col, 0))
            except:
                continue
            ref_val = gold[col]
            err = abs(agent_val - ref_val)
            cell_score = max(0.0, 1.0 - err / tol)
            score_sum += cell_score
            num_matched += 1
    if num_matched == 0:
        return 0.0
    # each gold row contributes two cells (Te0 and Te4)
    expected_cells = num_gold * 2
    return (score_sum / num_matched) * (num_matched / expected_cells) if num_matched > 0 else 0.0


_SCORERS = {
    'step_01': score_0,
    'step_03': score_1,
    'step_05': score_2,
    'step_06': score_3,
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
