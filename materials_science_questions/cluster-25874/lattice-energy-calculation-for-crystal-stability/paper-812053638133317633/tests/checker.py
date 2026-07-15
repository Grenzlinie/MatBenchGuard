import os
import json
import csv

# === author imports / helpers ===
import csv, json, os


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


# === block: score_0 (check id='structure_properties') ===
def score_0(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list):
        return 0.0
    step_check = step.get('parameters_check', {})
    required_cols = step_check.get('required_columns', [])
    if not required_cols or not artifact or not all(col in artifact[0] for col in required_cols):
        return 0.0
    items = step_check.get('items', [])
    total = len(items)
    if total == 0:
        return 0.0
    _GOLD = {
        "a": 9.47,
        "b": 5.97,
        "c": 8.15,
        "C(1)-C(2)-C(3)": 127.7,
        "C(2)-C(3)-C(4)": 128.2,
        "C(3)-C(4)-C(1')": 110.2,
        "C(4)-C(1')-C(2')": 111.3,
        "C(3)-C(4)-C(5)": 107.8,
        "C(1)-C(2)-C(3)-C(4)": 0,
        "C(2)-C(3)-C(4)-C(1')": -118.2,
        "C(3)-C(4)-C(1')-C(2')": -177.2,
        "C(4)-C(1')-C(2')-C(3')": 116.8,
        "C(2)-C(3)-C(4)-C(5)": 119.4
    }
    passed = 0
    # Build lookup by parameter name -> (value, unit)
    lookup = {}
    for row in artifact:
        param = row.get('parameter', '').strip()
        if param:
            try:
                val = float(row['value'])
            except (ValueError, TypeError, KeyError):
                continue
            unit = row.get('unit', '').strip()
            lookup[param] = (val, unit)
    for item in items:
        param = item['parameter']
        unit = item.get('unit', '')
        tol = item.get('tolerance', 0)
        gold = _GOLD.get(param)
        if gold is not None and param in lookup:
            val, u_art = lookup[param]
            if u_art == unit and abs(val - gold) <= tol:
                passed += 1
    return round(passed / total, 4)


# === block: score_1 (check id='lattice_energies') ===
def score_1(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, dict):
        return 0.0
    fields_gold = step.get('fields', {})
    tol = step.get('tolerance', 1.0)
    ordering_check = step.get('ordering_check', False)
    total_fields = len(fields_gold)
    if total_fields == 0:
        return 0.0
    matched = 0
    for key, gold_val in fields_gold.items():
        agent_val = artifact.get(key)
        if agent_val is None:
            continue
        try:
            agent_val = float(agent_val)
        except (TypeError, ValueError):
            continue
        if abs(agent_val - gold_val) <= tol:
            matched += 1
    energy_score = matched / total_fields
    ordering_score = 0.0
    if ordering_check:
        a_ein = artifact.get('model_A_Ein')
        b_ein = artifact.get('model_B_Ein')
        a_eopt = artifact.get('model_A_Eopt')
        b_eopt = artifact.get('model_B_Eopt')
        try:
            if (b_ein is not None and a_ein is not None and b_eopt is not None and a_eopt is not None):
                if float(b_ein) < float(a_ein) and float(b_eopt) < float(a_eopt):
                    ordering_score = 1.0
        except (TypeError, ValueError):
            pass
    # Combine with weight: energy 0.8, ordering 0.2
    return 0.8 * energy_score + 0.2 * ordering_score


_SCORERS = {
    'structure_properties': score_0,
    'lattice_energies': score_1,
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
