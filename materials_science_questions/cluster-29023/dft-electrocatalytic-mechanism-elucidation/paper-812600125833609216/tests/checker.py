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


# === block: score_0 (check id='systems_values') ===
def score_0(artifact, step, ctx):
    gold_systems = step['gold_systems']
    tol = step['tolerance']
    systems = artifact.get('systems', {})
    expected_count = len(gold_systems) * 4  # 4 systems * 4 values each
    total_score = 0.0
    for sys_name, gold_vals in gold_systems.items():
        vals = systems.get(sys_name)
        if not isinstance(vals, list) or len(vals) != 4:
            continue
        for i, gv in enumerate(gold_vals):
            if i >= len(vals):
                break
            diff = abs(vals[i] - gv)
            score = max(0.0, 1.0 - diff / (2 * tol))
            total_score += score
    for sys_name in gold_systems:
        if systems.get(sys_name) is None:
            total_score += 0.0  # missing system contributes zero
    return total_score / expected_count


# === block: score_1 (check id='rd_steps') ===
def score_1(artifact, step, ctx):
    systems = artifact.get('systems', {})
    gold_barriers = step['gold_barriers']
    tol = step['tolerance']
    ordering_required = step['ordering_required']
    recomputed = {}
    for sys in gold_barriers.keys():
        vals = systems.get(sys, [])
        if not isinstance(vals, list) or len(vals) != 4:
            recomputed[sys] = None
        else:
            recomputed[sys] = max(vals)
    total_barrier_score = 0.0
    n_barriers = len(gold_barriers)
    for sys, gold_val in gold_barriers.items():
        val = recomputed.get(sys)
        if val is None:
            score = 0.0
        else:
            diff = abs(val - gold_val)
            score = max(0.0, 1.0 - diff / (2 * tol))
        total_barrier_score += score
    barrier_avg = total_barrier_score / n_barriers
    ordering_ok = True
    for sys_a, sys_b in ordering_required:
        a_val = recomputed.get(sys_a)
        b_val = recomputed.get(sys_b)
        if a_val is None or b_val is None:
            ordering_ok = False
        elif a_val >= b_val:
            ordering_ok = False
    ordering_score = 1.0 if ordering_ok else 0.0
    return 0.7 * barrier_avg + 0.3 * ordering_score


# === block: score_2 (check id='mulliken') ===
def score_2(artifact, step, ctx):
    val = artifact.get('mulliken_charge_difference_fe_ooH')
    if val is None or not isinstance(val, (int, float)) or math.isnan(val):
        return 0.0
    diff = abs(val - step['gold_value'])
    tol = step['tolerance']
    return max(0.0, 1.0 - diff / (2 * tol))


_SCORERS = {
    'systems_values': score_0,
    'rd_steps': score_1,
    'mulliken': score_2,
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
