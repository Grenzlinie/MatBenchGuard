import os
import json
import csv

# === author imports / helpers ===
import math
import os


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


# === block: score_0 (check id='elastic_check') ===
def score_0(artifact, step, ctx):
    data = artifact  # dict
    ref = step.get('gold', {})
    tol_abs = 5.0
    tol_pct = 5.0
    props = ['c11','c12','c44','G','B','Y','ν']
    total = 0
    passed = 0
    for alloy, ref_props in ref.items():
        agent_props = data.get(alloy)
        if agent_props is None:
            continue
        for p in props:
            rv = ref_props.get(p)
            av = agent_props.get(p)
            if rv is None or av is None:
                continue
            tol = max(tol_abs, tol_pct/100.0 * abs(rv))
            total += 1
            if abs(av - rv) <= tol:
                passed += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_1 (check id='phonon_check') ===
def score_1(artifact, step, ctx):
    data = artifact  # dict
    threshold = step.get('threshold', -0.1)
    alloys = ['CoFeTiGa','CoFeVGa','CoFeCrGa','CoFeMnGa','CoFeCuGa','CoFeNbGa']
    passed = sum(1 for a in alloys if data.get(a, -999) >= threshold)
    if not alloys:
        return 0.0
    return passed / len(alloys)


# === block: score_2 (check id='magnetic_check') ===
def score_2(artifact, step, ctx):
    rows = artifact  # list of dicts from csv
    ref_rows = step.get('gold', [])
    tolerances = {'Type':0,'a':0.05,'M_Co':0.05,'M_Fe':0.05,'M_R':0.05,'M_Ga':0.05,'M_tot':0.05,'Phase':0}
    key_col = 'Alloy'
    def all_cols_match(row, ref):
        for col, tol in tolerances.items():
            if col in ('Type','Phase'):
                if str(row.get(col)).strip() != str(ref.get(col)).strip():
                    return False
            else:
                try:
                    rv = float(ref.get(col, 0.0))
                    av = float(row.get(col, 0.0))
                except ValueError:
                    return False
                if abs(av - rv) > tol:
                    return False
        return True
    matched = 0
    ref_by_key = {r[key_col].lower(): r for r in ref_rows}
    for row in rows:
        key = str(row.get(key_col, '')).lower()
        ref = ref_by_key.get(key)
        if ref and all_cols_match(row, ref):
            matched += 1
    return matched / len(ref_rows) if ref_rows else 1.0


# === block: score_3 (check id='transport_cocrga') ===
def score_3(artifact, step, ctx):
    rows = artifact  # list of dicts
    col = step['column']
    alloy = step['alloy']
    threshold = float(step['threshold'])
    for row in rows:
        if row.get('Alloy','').strip() == alloy:
            val = float(row.get(col, 0.0))
            if val <= threshold:
                return 1.0
            # partial credit: linear decay from threshold to zero
            max_penalty = -threshold  # distance from threshold to zero
            if max_penalty <= 0:
                return 0.0
            ratio = (val - threshold) / max_penalty
            return max(0.0, 1.0 - ratio)
    return 0.0


# === block: score_4 (check id='transport_others') ===
def score_4(artifact, step, ctx):
    rows = artifact  # list of dicts
    gold_rows = step.get('gold', [])
    tol = step.get('tolerances',{}).get('S_spin',2.0)
    key_col = 'Alloy'
    target_col = 'S_spin'
    ref_map = {r[key_col].lower(): float(r[target_col]) for r in gold_rows}
    matched = 0
    total = 0
    for row in rows:
        key = str(row.get(key_col,'')).lower()
        if key in ref_map:
            total += 1
            try:
                av = float(row.get(target_col, 0.0))
            except ValueError:
                continue
            rv = ref_map[key]
            if abs(av - rv) <= tol:
                matched += 1
    if total == 0:
        return 1.0
    return matched / total


# === block: score_5 (check id='transport_ordering') ===
def score_5(artifact, step, ctx):
    rows = artifact  # list of dicts
    target_key = 'CoFeCrGa'
    target_val = None
    others = []
    for row in rows:
        key = str(row.get('Alloy','')).strip()
        val = float(row.get('S_spin', 0.0))
        if key == target_key:
            target_val = abs(val)
        else:
            others.append(abs(val))
    if target_val is None or not others:
        return 0.0
    return 1.0 if all(target_val > o for o in others) else 0.0


# === block: score_6 (check id='transport_support') ===
def score_6(artifact, step, ctx):
    rows = artifact  # list of dicts
    gold_rows = step.get('gold', [])
    tols = step.get('tolerances', {})
    key_col = 'Alloy'
    ref_map = {r[key_col].lower(): r for r in gold_rows}
    matched = 0
    total = 0
    for row in rows:
        key = str(row.get(key_col,'')).lower()
        ref = ref_map.get(key)
        if ref is None:
            continue
        for col in ['S_up','S_down']:
            tol = tols.get(col, 5.0)
            total += 1
            try:
                av = float(row.get(col, 0.0))
                rv = float(ref.get(col, 0.0))
            except ValueError:
                continue
            if abs(av - rv) <= tol:
                matched += 1
    if total == 0:
        return 0.0
    return matched / total


_SCORERS = {
    'elastic_check': score_0,
    'phonon_check': score_1,
    'magnetic_check': score_2,
    'transport_cocrga': score_3,
    'transport_others': score_4,
    'transport_ordering': score_5,
    'transport_support': score_6,
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
