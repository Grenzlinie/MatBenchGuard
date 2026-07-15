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


# === block: score_0 (check id='builtin_potentials') ===
def score_0(artifact, step, ctx):
    import json

    artifact_data = artifact
    if not isinstance(artifact_data, list):
        return 0.0

    # Build lookup
    data_by_iface = {}
    for entry in artifact_data:
        iface = entry.get("interface")
        val = entry.get("builtin_potential_eV")
        if iface and val is not None:
            data_by_iface[iface] = float(val)

    gold = step.get("gold_values", {})
    tol = step.get("tolerance", 0.15)
    expected_ifaces = ["PbI/titania", "MAI/titania", "MAIdep/titania"]
    scores = []
    for iface in expected_ifaces:
        if iface not in data_by_iface:
            scores.append(0.0)
            continue
        val = data_by_iface[iface]
        target = gold.get(iface)
        if target is None:
            scores.append(0.0)
            continue
        diff = abs(val - target)
        if diff <= tol:
            scores.append(1.0)
        else:
            # partial credit: decay linearly beyond tolerance up to 2* tolerance
            partial = max(0.0, 1.0 - (diff - tol) / tol)
            scores.append(partial)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='interface_band_gaps') ===
def score_1(artifact, step, ctx):
    import json

    artifact_data = artifact
    if not isinstance(artifact_data, list):
        return 0.0

    # Extract values for each interface
    data_by_iface = {}
    for entry in artifact_data:
        iface = entry.get("interface")
        gap = entry.get("band_gap_eV")
        if iface and gap is not None:
            data_by_iface[iface] = float(gap)

    expected_order = step.get("expected_order", [])
    if len(expected_order) != 3:
        return 0.0

    # Build ordering list
    values = []
    for iface in expected_order:
        if iface not in data_by_iface:
            return 0.0
        values.append(data_by_iface[iface])

    # Check strict increasing order: PbI < MAIdep < MAI
    # Count correctly ordered pairs
    correct = 0
    total = 3  # pairs: (0,1), (1,2), (0,2)
    pairs = [(0,1), (1,2), (0,2)]
    for i, j in pairs:
        if values[i] < values[j]:
            correct += 1
        # If equal, we might treat as half? Conservative: not correct.

    return correct / total


# === block: score_2 (check id='driving_force_ranking') ===
def score_2(artifact, step, ctx):
    import json

    artifact_data = artifact
    if not isinstance(artifact_data, dict):
        return 0.0

    agent_ranking = artifact_data.get("ranking")
    if not isinstance(agent_ranking, list) or len(agent_ranking) != 3:
        return 0.0

    gold_ranking = step.get("gold_ranking")
    if not gold_ranking:
        return 0.0

    # exact match
    if agent_ranking == gold_ranking:
        return 1.0

    # partial credit based on first and last elements
    first_correct = (agent_ranking[0] == gold_ranking[0])
    last_correct = (agent_ranking[2] == gold_ranking[2])

    if first_correct and last_correct:
        return 0.7
    elif first_correct:
        return 0.4
    else:
        return 0.0


_SCORERS = {
    'builtin_potentials': score_0,
    'interface_band_gaps': score_1,
    'driving_force_ranking': score_2,
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
