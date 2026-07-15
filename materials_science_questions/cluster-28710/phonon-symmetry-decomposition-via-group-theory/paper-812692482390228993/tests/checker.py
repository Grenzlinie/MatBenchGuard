import os
import json
import csv

# === author imports / helpers ===
import os, csv, re, math


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
    return {'steps': spec['steps']}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    text = artifact if isinstance(artifact, str) else ''
    norm = text.strip().lower()
    # replace common overline representations (single backslash in regex matches literal backslash)
    norm = re.sub(r'\\overline\{1\}', 'bar1', norm)
    # accept (1,-1) notation
    norm = norm.replace('(1,-1)', 'bar1')
    norm = norm.replace('(1, -1)', 'bar1')
    # remove everything except lowercase letters, digits and slashes (drop underscores, spaces, punctuation)
    norm_clean = re.sub(r'[^a-z0-9/]', '', norm)
    # compact form check
    if norm_clean == 'ap21/m1bar1':
        return 1.0
    # full dualistic expansion check: must contain mP2_1/m and (c)B2/m
    if 'mp21/m' in norm_clean and ('cb2/m' in norm_clean or 'b2/m' in norm_clean):
        return 1.0
    return 0.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    # artifact is list of dicts from csv.DictReader
    rows = artifact if isinstance(artifact, list) else []
    expected_rows = step.get('expected_rows', [])
    if not expected_rows:
        return 0.0
    present = set()
    for row in rows:
        refl = str(row.get('reflection', '')).strip().lower()
        cond = str(row.get('condition', '')).strip().lower()
        # normalize condition: 'h even' -> 'h even'
        cond_norm = cond.replace(' ', '')
        present.add((refl, cond_norm))
    expected_set = set()
    for er in expected_rows:
        expected_set.add((er['reflection'].lower(), er['condition'].replace(' ', '').lower()))
    matches = expected_set & present
    # 1.0 if all expected rows present, 0.5 if only one, else 0.0
    if len(expected_set) == 0:
        return 0.0
    if matches == expected_set:
        return 1.0
    elif len(matches) >= 1:
        return 0.5
    else:
        return 0.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    lines = artifact.strip().split('\n') if isinstance(artifact, str) else []
    if len(lines) < 2:
        return 0.0
    basic_line = lines[0]
    incomm_line = lines[1]
    def extract_params(line):
        a = re.search(r'a\s*=\s*([\d.]+)', line)
        b = re.search(r'b\s*=\s*([\d.]+)', line)
        c = re.search(r'c\s*=\s*([\d.]+)', line)
        gamma = re.search(r'gamma\s*=\s*([\d.]+)', line)
        return {
            'a': float(a.group(1)) if a else None,
            'b': float(b.group(1)) if b else None,
            'c': float(c.group(1)) if c else None,
            'gamma': float(gamma.group(1)) if gamma else None
        }
    basic = extract_params(basic_line)
    incomm = extract_params(incomm_line)
    gold = step.get('gold', {})
    tols = step.get('tolerances', {})
    def within_tol(val, target, tol):
        if val is None or target is None:
            return False
        return abs(val - target) <= tol
    points = 0
    total = 9
    gbasic = gold.get('basic', {})
    gincomm = gold.get('incommensurate', {})
    if within_tol(basic.get('a'), gbasic.get('a'), tols.get('a', 0.2)): points += 1
    if within_tol(basic.get('b'), gbasic.get('b'), tols.get('b', 0.2)): points += 1
    if within_tol(basic.get('c'), gbasic.get('c'), tols.get('c', 0.2)): points += 1
    if within_tol(basic.get('gamma'), gbasic.get('gamma'), tols.get('gamma', 1.0)): points += 1
    if within_tol(incomm.get('a'), gincomm.get('a'), tols.get('a', 0.2)): points += 1
    if within_tol(incomm.get('b'), gincomm.get('b'), tols.get('b', 0.2)): points += 1
    if within_tol(incomm.get('c'), gincomm.get('c'), tols.get('c', 0.2)): points += 1
    if within_tol(incomm.get('gamma'), gincomm.get('gamma'), tols.get('gamma', 1.0)): points += 1
    if re.search(r'b[- ]?centered', incomm_line, re.IGNORECASE):
        points += 1
    return points / total


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
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
