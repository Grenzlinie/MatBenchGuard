import os
import json
import csv


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


# === block: score_0 (check id='step_soc_results') ===
def score_0(artifact, step, ctx):
    artifact_key = step.get("output_file", "")
    if not isinstance(artifact, dict):
        return 0.0

    rubric = step.get("rubric", {})
    if not rubric:
        return 0.0

    # --- value match ---
    vm_rubric = rubric.get("soc_value_match", {})
    fields = vm_rubric.get("fields", [])
    gold = vm_rubric.get("gold", [])
    tols = vm_rubric.get("tolerances", [])
    sub_weight_vm = float(vm_rubric.get("sub_weight", 0.0))

    match_count = 0
    total_soc = len(fields)
    for i, fld in enumerate(fields):
        val = artifact.get(fld, None)
        if val is None:
            continue
        try:
            val = float(val)
        except (ValueError, TypeError):
            continue
        ref = gold[i] if i < len(gold) else 0.0
        tol = tols[i] if i < len(tols) else 50.0
        if abs(val - ref) <= tol:
            match_count += 1

    score_vm = (match_count / total_soc) * sub_weight_vm if total_soc > 0 else 0.0

    # --- ordering ---
    ord_rubric = rubric.get("ordering", {})
    rules = ord_rubric.get("rules", [])
    sub_weight_ord = float(ord_rubric.get("sub_weight", 0.0))

    satisfied_rules = 0
    for rule in rules:
        # rule is a string like "forward_1A''_to_13A''_SOC_cm-1 > forward_13A''_to_5A'_SOC_cm-1"
        try:
            parts = rule.split(" > ")
            left_key = parts[0].strip()
            right_key = parts[1].strip()
            left_val = artifact.get(left_key)
            right_val = artifact.get(right_key)
            if left_val is not None and right_val is not None:
                if float(left_val) > float(right_val):
                    satisfied_rules += 1
        except Exception:
            pass

    score_ord = (satisfied_rules / len(rules)) * sub_weight_ord if len(rules) > 0 else 0.0

    # --- booleans ---
    bool_rubric = rubric.get("booleans", {})
    sub_weight_bool = float(bool_rubric.get("sub_weight", 0.0))

    fw = artifact.get("forward_crossover_preferred", False)
    bw = artifact.get("backward_crossover_preferred", False)
    score_bool = sub_weight_bool if (fw is True and bw is True) else 0.0

    return score_vm + score_ord + score_bool


_SCORERS = {
    'step_soc_results': score_0,
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
