import os
import json
import csv

# === author imports / helpers ===
import math
import re
import json


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
    lines = artifact.strip().splitlines()
    if len(lines) < 3:
        return 0.0
    coords = []
    for line in lines[2:]:
        parts = line.split()
        if len(parts) >= 4 and parts[0] == 'C':
            try:
                x, y, z = tuple(map(float, parts[1:4]))
                coords.append((x, y, z))
            except:
                pass
    if len(coords) < 2:
        return 0.0
    # Compute centroid
    sum_x = sum(p[0] for p in coords)
    sum_y = sum(p[1] for p in coords)
    n = len(coords)
    cx = sum_x / n
    cy = sum_y / n
    # Max distance from centroid to a carbon atom (radius)
    max_r = 0.0
    for (x, y, _) in coords:
        d = math.sqrt((x - cx)**2 + (y - cy)**2)
        if d > max_r:
            max_r = d
    pore_diameter = 2.0 * max_r
    target = step['target']['pore_diameter_angstrom']
    tol = step['target'].get('tolerance_abs', 0.1)
    diff = abs(pore_diameter - target)
    score = max(0.0, 1.0 - diff / tol)
    return score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    m = re.search(r'(-?[\d.]+)\s*eV', artifact)
    if not m:
        return 0.0
    val = float(m.group(1))
    target = step['target']
    tol_pct = step.get('tolerance_pct', 10.0)
    rel_tol = abs(target) * tol_pct / 100.0
    if rel_tol <= 0:
        return 1.0 if abs(val - target) < 1e-9 else 0.0
    diff = abs(val - target)
    score = max(0.0, 1.0 - diff / rel_tol)
    return score


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    m = re.search(r'(-?[\d.]+)\s*kcal/mol', artifact)
    if not m:
        return 0.0
    val = float(m.group(1))
    target = step['target']
    tol_pct = step.get('tolerance_pct', 20.0)
    rel_tol = abs(target) * tol_pct / 100.0
    if rel_tol <= 0:
        return 1.0 if abs(val - target) < 1e-9 else 0.0
    diff = abs(val - target)
    score = max(0.0, 1.0 - diff / rel_tol)
    return score


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    targets = step['targets']
    tol_pct = step.get('tolerance_pct', 10.0)
    scores = []
    for k, tgt in targets.items():
        val = artifact.get(k)
        if val is None or not isinstance(val, (int, float)):
            scores.append(0.0)
            continue
        rel_tol = abs(tgt) * tol_pct / 100.0 if tgt != 0 else tol_pct
        if rel_tol <= 0:
            s = 1.0 if abs(val - tgt) < 1e-9 else 0.0
        else:
            diff = abs(val - tgt)
            s = max(0.0, 1.0 - diff / rel_tol)
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_4 (check id='step_05') ===
def score_4(artifact, step, ctx):
    m = re.search(r'(-?[\d.]+)\s*L\u00b7m\u207b\u00b2\u00b7h\u207b\u00b9\u00b7bar\u207b\u00b9', artifact)
    # fallback plain pattern
    if not m:
        m = re.search(r'(-?[\d.]+)\s*', artifact)
    if not m:
        return 0.0
    val = float(m.group(1))
    target = step['target']
    if val >= target:
        return 1.0
    else:
        # partial credit proportional to ratio, capped at 1
        return max(0.0, min(1.0, val / target))


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
    'step_05': score_4,
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
