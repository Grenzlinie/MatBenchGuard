import os
import json
import csv

# === author imports / helpers ===
import re


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
    return {
        'gdr_gold': 7.30,
        'exp_gold': 7.31
    }


# === block: score_0 (check id='compute_gdr_q0') ===
def score_0(artifact, step, ctx):
    try:
        match = re.search(r'Q0\s*=\s*(\d+\.?\d*)', artifact, re.IGNORECASE)
        if not match:
            return 0.0
        value = float(match.group(1))
        target = step.get('target', 7.30)
        tol = step.get('tolerance_abs', 0.02)
        if abs(value - target) <= tol:
            return 1.0
        else:
            return 0.0
    except:
        return 0.0


# === block: score_1 (check id='compute_experimental_q0') ===
def score_1(artifact, step, ctx):
    try:
        match = re.search(r'Q0\s*=\s*(\d+\.?\d*)', artifact, re.IGNORECASE)
        if not match:
            return 0.0
        value = float(match.group(1))
        target = step.get('target', 7.31)
        tol = step.get('tolerance_abs', 0.02)
        if abs(value - target) <= tol:
            return 1.0
        else:
            return 0.0
    except:
        return 0.0


# === block: score_2 (check id='compare_q0') ===
def score_2(artifact, step, ctx):
    try:
        lines = artifact.strip().split('\n')
        if len(lines) < 3:
            return 0.0
        # Extract values from first two lines
        m1 = re.search(r'Q0:\s*(\d+\.?\d*)', lines[0])
        m2 = re.search(r'Q0:\s*(\d+\.?\d*)', lines[1])
        if not m1 or not m2:
            return 0.0
        v1 = float(m1.group(1))
        v2 = float(m2.group(1))
        gdr_gold = ctx.get('gdr_gold', 7.30)
        exp_gold = ctx.get('exp_gold', 7.31)
        tol = step.get('tolerance', 0.02)
        bound = step.get('agreement_bound', 0.05)
        if abs(v1 - gdr_gold) > tol or abs(v2 - exp_gold) > tol:
            return 0.0
        # Check third line
        line3 = lines[2]
        diff_match = re.search(r'(\d+\.?\d*)\s*b', line3)
        reported_diff = float(diff_match.group(1)) if diff_match else None
        actual_diff = abs(v1 - v2)
        if reported_diff is not None and abs(reported_diff - actual_diff) > 0.001:
            return 0.0
        if actual_diff > bound:
            return 0.0
        # Check agreement phrase
        lower = line3.lower()
        if 'agree' in lower or 'within' in lower:
            return 1.0
        else:
            return 0.5
    except:
        return 0.0


_SCORERS = {
    'compute_gdr_q0': score_0,
    'compute_experimental_q0': score_1,
    'compare_q0': score_2,
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
