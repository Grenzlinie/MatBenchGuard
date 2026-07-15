import os
import json
import csv

# === author imports / helpers ===
import re, math


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


# === block: score_0 (check id='results_structure') ===
def score_0(artifact, step, ctx):
    return 1.0 if isinstance(artifact, list) and len(artifact) == step.get('required_rows', 16) else 0.0


# === block: score_1 (check id='intercal_energy_trends') ===
def score_1(artifact, step, ctx):
    groups = {}
    for row in artifact:
        stage = int(row.get('stage', -1))
        cnt = int(row.get('PF6_count', -1))
        val = float(row.get('intercalation_energy_eV', 0))
        groups.setdefault(stage, []).append((cnt, val))
    all_ok = True
    for stage, pairs in groups.items():
        pairs.sort(key=lambda x: x[0])
        for i in range(1, len(pairs)):
            if pairs[i][1] > pairs[i-1][1]:  # must be more negative
                all_ok = False
                break
    return 1.0 if all_ok else 0.0


# === block: score_2 (check id='interlayer_distance_trends') ===
def score_2(artifact, step, ctx):
    groups = {}
    for row in artifact:
        stage = int(row.get('stage', -1))
        cnt = int(row.get('PF6_count', -1))
        val = float(row.get('interlayer_distance_Angstrom', 0))
        groups.setdefault(stage, []).append((cnt, val))
    all_ok = True
    for stage, pairs in groups.items():
        pairs.sort(key=lambda x: x[0])
        for i in range(1, len(pairs)):
            if pairs[i][1] < pairs[i-1][1]:
                all_ok = False
                break
    return 1.0 if all_ok else 0.0


# === block: score_3 (check id='intercal_energy_values') ===
def score_3(artifact, step, ctx):
    gold = step.get('gold_table', {})
    tol = step.get('tolerance', 0.10)
    match_cols = step.get('match_columns', ['stage','PF6_count'])
    val_col = step.get('value_column', 'intercalation_energy_eV')
    correct = 0
    total = 0
    for row in artifact:
        key = '-'.join([str(row[c]) for c in match_cols])
        if key in gold:
            diff = abs(float(row.get(val_col, 0)) - gold[key])
            if diff <= tol:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_4 (check id='interlayer_distance_values') ===
def score_4(artifact, step, ctx):
    gold = step.get('gold_table', {})
    tol = step.get('tolerance', 0.05)
    match_cols = step.get('match_columns', ['stage','PF6_count'])
    val_col = step.get('value_column', 'interlayer_distance_Angstrom')
    correct = 0
    total = 0
    for row in artifact:
        key = '-'.join([str(row[c]) for c in match_cols])
        if key in gold:
            diff = abs(float(row.get(val_col, 0)) - gold[key])
            if diff <= tol:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_5 (check id='gallery_expansion') ===
def score_5(artifact, step, ctx):
    filt = step.get('filter', {})
    for row in artifact:
        match = True
        for k, v in filt.items():
            if str(row.get(k, '')) != str(v):
                match = False
                break
        if match:
            d = float(row.get('interlayer_distance_Angstrom', 0))
            exp = 100 * (d / 3.34 - 1)
            # Expected expansion from the paper's gold interlayer distance 7.35 Å
            expected = 100 * (7.35 / 3.34 - 1)
            tol = 5.0
            return 1.0 if abs(exp - expected) <= tol else 0.0
    return 0.0


# === block: score_6 (check id='voltage_range') ===
def score_6(artifact, step, ctx):
    text = artifact if isinstance(artifact, str) else artifact[0] if isinstance(artifact, list) and artifact else ''
    min_pat = step.get('regex_min', r'Voltage range:\s*([0-9.]+)-')
    max_pat = step.get('regex_max', r'\d+-([0-9.]+)')
    v_min = None
    v_max = None
    m = re.search(min_pat, text)
    if m:
        v_min = float(m.group(1))
    m = re.search(max_pat, text)
    if m:
        v_max = float(m.group(1))
    if v_min is None or v_max is None:
        return 0.0
    tol = step.get('tolerance', 0.15)
    ok_min = abs(v_min - step['expected_min']) <= tol
    ok_max = abs(v_max - step['expected_max']) <= tol
    return 0.5 if ok_min else 0.0 + (0.5 if ok_max else 0.0)


# === block: score_7 (check id='specific_capacity') ===
def score_7(artifact, step, ctx):
    text = artifact if isinstance(artifact, str) else artifact[0] if isinstance(artifact, list) and artifact else ''
    pat = step.get('regex', r'Specific capacity:\s*([0-9]+)\s*mAh/g')
    m = re.search(pat, text)
    if not m:
        return 0.0
    val = float(m.group(1))
    return 1.0 if abs(val - step['expected']) <= step.get('tolerance', 10) else 0.0


# === block: score_8 (check id='bader_charge') ===
def score_8(artifact, step, ctx):
    raw = artifact if isinstance(artifact, str) else (artifact[0] if isinstance(artifact, list) and artifact else '')
    try:
        val = float(raw.strip())
    except:
        return 0.0
    return 1.0 if abs(val - step['expected']) <= step.get('tolerance', 0.05) else 0.0


# === block: score_9 (check id='diffusion_barrier') ===
def score_9(artifact, step, ctx):
    raw = artifact if isinstance(artifact, str) else (artifact[0] if isinstance(artifact, list) and artifact else '')
    try:
        val = float(raw.strip())
    except:
        return 0.0
    if val <= step['expected']:
        return 1.0
    factor = step.get('decay_factor', 0.05)
    penalty = (val - step['expected']) / factor
    return max(0.0, 1.0 - penalty)


_SCORERS = {
    'results_structure': score_0,
    'intercal_energy_trends': score_1,
    'interlayer_distance_trends': score_2,
    'intercal_energy_values': score_3,
    'interlayer_distance_values': score_4,
    'gallery_expansion': score_5,
    'voltage_range': score_6,
    'specific_capacity': score_7,
    'bader_charge': score_8,
    'diffusion_barrier': score_9,
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
