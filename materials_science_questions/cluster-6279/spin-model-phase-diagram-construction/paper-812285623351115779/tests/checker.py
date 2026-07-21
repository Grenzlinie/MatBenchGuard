import os
import json
import csv

# === author imports / helpers ===
import csv
import json
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
    # structural_coefficients.csv audit
    artifact = artifact  # list of dicts from csv
    step = step
    tol_a1 = step.get("checks", {}).get("a1_1_zero_tol", 0.005)
    rel_diff = step.get("checks", {}).get("a0_1_max_rel_diff", 0.1)
    exp_phases = set(step.get("checks", {}).get("expected_phases", []))
    # gather rows by phase
    data = {}
    for row in artifact:
        phase = row.get("phase", "")
        coeff = row.get("coefficient", "")
        try:
            val = float(row.get("value", 0))
        except:
            val = None
        if phase not in data:
            data[phase] = {}
        if coeff:
            data[phase][coeff] = val
    # checks
    checks_passed = 0
    total_checks = 0
    # 1. all expected phases present
    for p in exp_phases:
        total_checks += 1
        if p in data:
            checks_passed += 1
    # 2. a1(1) approx zero for <1>
    if "<1>" in data and "a1(1)" in data["<1>"]:
        total_checks += 1
        v = data["<1>"]["a1(1)"]
        if v is not None and abs(v) <= tol_a1:
            checks_passed += 1
    # 3. a112(3) negative for <21>
    if "<21>" in data and "a112(3)" in data["<21>"]:
        total_checks += 1
        v = data["<21>"]["a112(3)"]
        if v is not None and v < 0:
            checks_passed += 1
    # 4. a0(1) consistent across phases (relative diff < rel_diff)
    a0_vals = []
    for p in exp_phases:
        if p in data and "a0(1)" in data[p]:
            v = data[p]["a0(1)"]
            if v is not None:
                a0_vals.append(v)
    if len(a0_vals) >= 2:
        total_checks += 1
        max_v = max(a0_vals)
        min_v = min(a0_vals)
        if max_v != 0:
            if (max_v - min_v) / abs(max_v) <= rel_diff:
                checks_passed += 1
        else:
            if min_v == 0:
                checks_passed += 1
    elif len(a0_vals) == 1:
        total_checks += 1
        checks_passed += 1  # alone trivial
    # return fraction
    if total_checks == 0:
        return 0.0
    return checks_passed / total_checks


# === block: score_1 (check id='step_03') ===
def score_1(artifact, step, ctx):
    # phase_boundaries.csv threshold_or_better
    artifact = artifact
    gold_points = step.get("gold_points", {})
    tol = step.get("tolerance", {"delta": 0.05, "T_c": 0.05})
    total_gold = 0
    satisfied = 0
    # group agent points by boundary
    agent = {}
    for row in artifact:
        boundary = row.get("boundary", "")
        try:
            delta = float(row.get("delta"))
            T_c = float(row.get("T_c"))
        except:
            continue
        agent.setdefault(boundary, []).append((delta, T_c))

    for bname, gpts in gold_points.items():
        for gp in gpts:
            gd = gp["delta"]
            gT = gp["T_c"]
            total_gold += 1
            matched = False
            for ad, aT in agent.get(bname, []):
                if abs(ad - gd) <= tol["delta"] and abs(aT - gT) <= tol["T_c"]:
                    matched = True
                    break
            if matched:
                satisfied += 1
    if total_gold == 0:
        return 0.0
    return satisfied / total_gold


_SCORERS = {
    'step_01': score_0,
    'step_03': score_1,
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
