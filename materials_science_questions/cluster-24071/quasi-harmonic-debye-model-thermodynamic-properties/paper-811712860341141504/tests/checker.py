import os
import json
import csv

# === author imports / helpers ===
import csv
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


# === block: score_0 (check id='step01_structural') ===
def score_0(artifact, step, ctx):
    rows = {row['material']: row for row in artifact}
    checks = step.get('checks', [])
    passed = 0
    total = len(checks)
    if total == 0:
        return 0.0
    for c in checks:
        try:
            if c['type'] == 'numeric':
                mat = c['material']
                field = c['field']
                target = float(c['target'])
                if 'tolerance_rel' in c:
                    tol = c['tolerance_rel'] * abs(target)
                else:
                    tol = c.get('tolerance_abs', 0.0)
                val = float(rows[mat][field])
                if abs(val - target) <= max(tol, 1e-9):
                    passed += 1
            elif c['type'] == 'trend':
                field = c['field']
                if 'material2' in c:
                    val1 = float(rows[c['material1']][field])
                    val2 = float(rows[c['material2']][field])
                    rel = c['relation']
                    if rel == 'greater' and val1 > val2:
                        passed += 1
                    elif rel == 'less' and val1 < val2:
                        passed += 1
                    else:
                        pass
                else:
                    val = float(rows[c['material1']][field])
                    rel = c['relation']
                    threshold = c.get('threshold')
                    if rel == 'less' and threshold is not None and val < threshold:
                        passed += 1
                    elif rel == 'greater' and threshold is not None and val > threshold:
                        passed += 1
        except Exception:
            pass
    return passed / total


# === block: score_1 (check id='step02_elastic') ===
def score_1(artifact, step, ctx):
    rows = {row['material']: row for row in artifact}
    checks = step.get('checks', [])
    passed = 0
    total = len(checks)
    if total == 0:
        return 0.0
    for c in checks:
        try:
            if c['type'] == 'numeric':
                mat = c['material']
                field = c['field']
                target = float(c['target'])
                tol = c['tolerance_rel'] * abs(target)
                val = float(rows[mat][field])
                if abs(val - target) <= max(tol, 1e-9):
                    passed += 1
            elif c['type'] == 'trend':
                field = c['field']
                val1 = float(rows[c['material1']][field])
                val2 = float(rows[c['material2']][field])
                if c['relation'] == 'greater' and val1 > val2:
                    passed += 1
        except Exception:
            pass
    return passed / total


# === block: score_2 (check id='step03_derived_elastic') ===
def score_2(artifact, step, ctx):
    rows = {row['material']: row for row in artifact}
    checks = step.get('checks', [])
    passed = 0
    total = len(checks)
    if total == 0:
        return 0.0
    for c in checks:
        try:
            if c['type'] == 'numeric':
                mat = c['material']
                field = c['field']
                target = float(c['target'])
                if 'tolerance_rel' in c:
                    tol = c['tolerance_rel'] * abs(target)
                else:
                    tol = c.get('tolerance_abs', 0.0)
                val = float(rows[mat][field])
                if abs(val - target) <= max(tol, 1e-9):
                    passed += 1
            elif c['type'] == 'trend':
                if 'material2' in c:
                    val1 = float(rows[c['material1']][c['field']])
                    val2 = float(rows[c['material2']][c['field']])
                    if c['relation'] == 'greater' and val1 > val2:
                        passed += 1
                else:
                    val = float(rows[c['material1']][c['field']])
                    if c['relation'] == 'less' and c.get('threshold') is not None and val < c['threshold']:
                        passed += 1
        except Exception:
            pass
    return passed / total


# === block: score_3 (check id='step04_thermodynamic') ===
def score_3(artifact, step, ctx):
    rows = {row['material']: row for row in artifact}
    checks = step.get('checks', [])
    passed = 0
    total = len(checks)
    if total == 0:
        return 0.0
    for c in checks:
        try:
            if c['type'] == 'numeric':
                mat = c['material']
                field = c['field']
                target = float(c['target'])
                tol = c['tolerance_rel'] * abs(target)
                val = float(rows[mat][field])
                if abs(val - target) <= max(tol, 1e-9):
                    passed += 1
            elif c['type'] == 'trend':
                field = c['field']
                val1 = float(rows[c['material1']][field])
                val2 = float(rows[c['material2']][field])
                if c['relation'] == 'greater' and val1 > val2:
                    passed += 1
        except Exception:
            pass
    return passed / total


_SCORERS = {
    'step01_structural': score_0,
    'step02_elastic': score_1,
    'step03_derived_elastic': score_2,
    'step04_thermodynamic': score_3,
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
