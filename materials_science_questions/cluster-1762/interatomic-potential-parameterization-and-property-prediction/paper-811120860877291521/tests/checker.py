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
    return {
        "abs_params": spec["steps"][0]["params"],
        "order_params": spec["steps"][1]["params"]
    }


# === block: score_0 (check id='mad_abs_dev') ===
def score_0(artifact, step, ctx):
    import json
    artifact_list = artifact  # artifact is the loaded list of dicts
    gold = {
        "Na3PO4": -16.60,
        "Ca3(PO4)2": -16.44,
        "Mn3(PO4)2": -14.56,
        "Ni3(PO4)2": -13.33,
        "InPO4": -14.05,
        "FePO4": -13.60,
        "GaPO4": -13.81,
        "BPO4": -12.52
    }
    tol = 0.01
    compound_key = "compound"
    value_key = "V_M"

    agent_vals = {}
    for item in artifact_list:
        name = item.get(compound_key)
        val = item.get(value_key)
        if name is not None and val is not None:
            agent_vals[name] = val

    if not agent_vals:
        return 0.0

    correct = 0
    total = len(gold)
    for comp, gold_val in gold.items():
        agent_val = agent_vals.get(comp)
        if agent_val is None:
            continue
        err = abs(agent_val - gold_val)
        if err <= tol:
            correct += 1.0
        else:
            excess = err - tol
            if excess <= tol:
                correct += max(0.0, 1.0 - excess / tol)

    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='mad_order') ===
def score_1(artifact, step, ctx):
    import json
    artifact_list = artifact
    # Hardcoded expected ordering based on ionicity-corrected Madelung potentials V_Mc from Table 1
    expected_order = [
        "Na3PO4",
        "Ca3(PO4)2",
        "Mn3(PO4)2",
        "InPO4",
        "GaPO4",
        "FePO4",
        "Ni3(PO4)2",
        "BPO4"
    ]
    tie_groups = []  # no compounds are tied in V_Mc
    compound_key = "compound"
    value_key = "V_M"
    order_tol = 0.05

    # Build dict
    agent_vals = {}
    for item in artifact_list:
        name = item.get(compound_key)
        val = item.get(value_key)
        if name is not None and val is not None:
            agent_vals[name] = val

    if len(agent_vals) < 2:
        return 0.0

    # Compute score: fraction of correctly ordered pairs (most negative first)
    total_pairs = 0
    correct_pairs = 0

    for i in range(len(expected_order)):
        for j in range(i+1, len(expected_order)):
            comp_i = expected_order[i]
            comp_j = expected_order[j]
            if comp_i not in agent_vals or comp_j not in agent_vals:
                continue
            # For descending order, expect V_M_i <= V_M_j
            vi = agent_vals[comp_i]
            vj = agent_vals[comp_j]
            if vi <= vj + order_tol:
                correct_pairs += 1
            total_pairs += 1

    if total_pairs == 0:
        return 1.0
    return correct_pairs / total_pairs


_SCORERS = {
    'mad_abs_dev': score_0,
    'mad_order': score_1,
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
