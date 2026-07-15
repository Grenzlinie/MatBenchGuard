import os
import json
import csv

# === author imports / helpers ===
import json, os, math

def score_numeric(value, target, tol_frac, hard_cap_factor=2.0):
    if target == 0:
        return 1.0 if abs(value) <= 1e-6 else 0.0
    rel_err = abs(value - target) / abs(target)
    if rel_err <= tol_frac:
        return 1.0
    cap_err = hard_cap_factor * tol_frac
    if rel_err >= cap_err:
        return 0.0
    return 1.0 - (rel_err - tol_frac) / (cap_err - tol_frac)


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
    outputs_dir = os.path.abspath(outputs_dir)
    b4_path = os.path.join(outputs_dir, 'pl_b4_results.json')
    b8_path = os.path.join(outputs_dir, 'pl_b8_results.json')
    data = {}
    for path, key in [(b4_path, 'b4'), (b8_path, 'b8')]:
        if os.path.exists(path):
            with open(path) as f:
                data[key] = json.load(f)
        else:
            data[key] = None
    return data


# === block: score_0 (check id='b4_kappa') ===
def score_0(artifact, step, ctx):
    val = artifact.get('K_L_300K')
    if val is None:
        return 0.0
    target = step['config']['target']
    tol = step['config']['tolerance_frac']
    return score_numeric(val, target, tol)


# === block: score_1 (check id='b8_kappa') ===
def score_1(artifact, step, ctx):
    val = artifact.get('K_L_300K')
    if val is None:
        return 0.0
    target = step['config']['target']
    tol = step['config']['tolerance_frac']
    return score_numeric(val, target, tol)


# === block: score_2 (check id='b4_scattering') ===
def score_2(artifact, step, ctx):
    base_obj = artifact.get('branch_scattering_rates', {})
    targets = step['config']['targets']
    tol = step['config']['tolerance_frac']
    fields = step['config']['fields']
    scores = []
    for f in fields:
        v = base_obj.get(f)
        if v is None:
            scores.append(0.0)
        else:
            scores.append(score_numeric(v, targets[f], tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_3 (check id='b8_scattering') ===
def score_3(artifact, step, ctx):
    base_obj = artifact.get('branch_scattering_rates', {})
    targets = step['config']['targets']
    tol = step['config']['tolerance_frac']
    fields = step['config']['fields']
    scores = []
    for f in fields:
        v = base_obj.get(f)
        if v is None:
            scores.append(0.0)
        else:
            scores.append(score_numeric(v, targets[f], tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_4 (check id='b4_groupvel') ===
def score_4(artifact, step, ctx):
    base_obj = artifact.get('branch_group_velocities', {})
    targets = step['config']['targets']
    tol = step['config']['tolerance_frac']
    fields = step['config']['fields']
    scores = []
    for f in fields:
        v = base_obj.get(f)
        if v is None:
            scores.append(0.0)
        else:
            scores.append(score_numeric(v, targets[f], tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_5 (check id='b8_groupvel') ===
def score_5(artifact, step, ctx):
    base_obj = artifact.get('branch_group_velocities', {})
    targets = step['config']['targets']
    tol = step['config']['tolerance_frac']
    fields = step['config']['fields']
    scores = []
    for f in fields:
        v = base_obj.get(f)
        if v is None:
            scores.append(0.0)
        else:
            scores.append(score_numeric(v, targets[f], tol))
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_6 (check id='trend_scattering') ===
def score_6(artifact, step, ctx):
    b4 = ctx.get('b4', {})
    b8 = ctx.get('b8', {})
    if not b4 or not b8:
        return 0.0
    b4_scat = b4.get('branch_scattering_rates', {})
    b8_scat = b8.get('branch_scattering_rates', {})
    threshold = step['config'].get('threshold_ratio', 2.0)
    branches = ['TA1','TA2','LA','Optical']
    satisfy = 0
    for b in branches:
        v4 = b4_scat.get(b)
        v8 = b8_scat.get(b)
        if v4 is not None and v8 is not None and v8 > 0:
            if v4 / v8 >= threshold:
                satisfy += 1
        else:
            pass
    return satisfy / len(branches) if branches else 0.0


# === block: score_7 (check id='trend_kappa') ===
def score_7(artifact, step, ctx):
    b4 = ctx.get('b4', {})
    b8 = ctx.get('b8', {})
    if not b4 or not b8:
        return 0.0
    k_b4 = b4.get('K_L_300K')
    k_b8 = b8.get('K_L_300K')
    if k_b4 is None or k_b8 is None:
        return 0.0
    return 1.0 if k_b4 < k_b8 else 0.0


_SCORERS = {
    'b4_kappa': score_0,
    'b8_kappa': score_1,
    'b4_scattering': score_2,
    'b8_scattering': score_3,
    'b4_groupvel': score_4,
    'b8_groupvel': score_5,
    'trend_scattering': score_6,
    'trend_kappa': score_7,
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
