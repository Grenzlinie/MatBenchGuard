import os
import json
import csv

# === author imports / helpers ===
import csv, os, re


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


# === block: score_0 (check id='check_bandgap') ===
def score_0(artifact, step, ctx):
    raw = artifact.strip()
    match = re.search(r'[\d.]+(?:[eE][+-]?\d+)?', raw)
    if not match:
        return 0.0
    val = float(match.group())
    ref = step['reference']
    tol = step.get('tolerance_abs', 0.0)
    if abs(val - ref) <= tol:
        return 1.0
    return 0.0


# === block: score_1 (check id='check_N0') ===
def score_1(artifact, step, ctx):
    rows = {}
    for row in artifact:
        try:
            x = str(float(row['x']))
            rows[x] = float(row['N0'])
        except:
            pass
    ref = step['reference']
    if not ref:
        return 0.0
    sorted_x = sorted(rows.keys(), key=lambda x: float(x))
    vals = [rows[x] for x in sorted_x]
    monotonic = all(vals[i] < vals[i+1] for i in range(len(vals)-1)) if len(vals) >= 2 else False
    if not monotonic:
        return 0.0
    rel_tol = step.get('tolerance_rel', 0.2)
    ok = 0.0
    for x_key, ref_val in ref.items():
        agent_val = rows.get(x_key)
        if agent_val is None:
            continue
        if abs(agent_val - ref_val) / ref_val <= rel_tol:
            ok += 1.0
    return ok / len(ref) if len(ref) > 0 else 0.0


# === block: score_2 (check id='check_lambda') ===
def score_2(artifact, step, ctx):
    rows = {}
    for row in artifact:
        try:
            x = str(float(row['x']))
            rows[x] = float(row['lambda'])
        except:
            pass
    ref = step['reference']
    if not ref:
        return 0.0
    sorted_x = sorted(rows.keys(), key=lambda x: float(x))
    vals = [rows[x] for x in sorted_x]
    monotonic = all(vals[i] < vals[i+1] for i in range(len(vals)-1)) if len(vals) >= 2 else False
    if not monotonic:
        return 0.0
    rel_tol = step.get('tolerance_rel', 0.2)
    ok = 0.0
    for x_key, ref_val in ref.items():
        agent_val = rows.get(x_key)
        if agent_val is None:
            continue
        if abs(agent_val - ref_val) / ref_val <= rel_tol:
            ok += 1.0
    return ok / len(ref) if len(ref) > 0 else 0.0


# === block: score_3 (check id='check_Tc') ===
def score_3(artifact, step, ctx):
    raw = artifact.strip().split()
    try:
        vals = [float(v) for v in raw[:2]]
    except:
        return 0.0
    ref = step['reference']
    tol = step.get('tolerance_abs', [5.0, 5.0])
    ok = 0
    for i in range(2):
        if abs(vals[i] - ref[i]) <= tol[i]:
            ok += 1
    return ok / 2.0


_SCORERS = {
    'check_bandgap': score_0,
    'check_N0': score_1,
    'check_lambda': score_2,
    'check_Tc': score_3,
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
