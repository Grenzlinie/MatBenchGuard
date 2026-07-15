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
    ctx = {
        'range_low': 18000.0 - 500.0,
        'range_high': 22000.0 + 500.0,
        'ordered_states': ['Gamma8_a_1', 'Gamma8_a_2', 'Gamma7', 'Gamma8_b_1', 'Gamma8_b_2', 'Gamma6'],
        'Gamma8a_target': 850.0,
        'Gamma8a_tol': 0.3,
        'Gamma8b_target': 200.0,
        'Gamma8b_tol': 0.3,
        'reported_splitting_target': 180.0,
        'reported_splitting_tol': 50.0
    }
    return ctx


# === block: score_0 (check id='range_check') ===
def score_0(artifact, step, ctx):
    energies = artifact.get('energies', [])
    if not isinstance(energies, list) or len(energies) != 6:
        return 0.0
    for entry in energies:
        e = entry.get('energy_cm1', 0.0)
        if not (ctx['range_low'] <= e <= ctx['range_high']):
            return 0.0
    return 1.0


# === block: score_1 (check id='ordering_check') ===
def score_1(artifact, step, ctx):
    energies = artifact.get('energies', [])
    if not isinstance(energies, list) or len(energies) != 6:
        return 0.0
    # Build a dict mapping state -> energy
    edict = {}
    for entry in energies:
        state = entry.get('state', '')
        e = entry.get('energy_cm1', 0.0)
        edict[state] = e
    # Must contain all expected states
    for s in ctx['ordered_states']:
        if s not in edict:
            return 0.0
    # Check strict increasing order
    prev = None
    for s in ctx['ordered_states']:
        v = edict[s]
        if prev is not None and v <= prev:
            return 0.0
        prev = v
    return 1.0


# === block: score_2 (check id='splitting_Gamma8a_check') ===
def score_2(artifact, step, ctx):
    energies = artifact.get('energies', [])
    if not isinstance(energies, list):
        return 0.0
    edict = {}
    for entry in energies:
        state = entry.get('state', '')
        e = entry.get('energy_cm1', 0.0)
        edict[state] = e
    if 'Gamma8_a_1' not in edict or 'Gamma8_a_2' not in edict:
        return 0.0
    split = abs(edict['Gamma8_a_2'] - edict['Gamma8_a_1'])
    allowed = ctx['Gamma8a_target'] * ctx['Gamma8a_tol']
    if abs(split - ctx['Gamma8a_target']) <= allowed:
        return 1.0
    return 0.0


# === block: score_3 (check id='splitting_Gamma8b_from_energies_check') ===
def score_3(artifact, step, ctx):
    energies = artifact.get('energies', [])
    if not isinstance(energies, list):
        return 0.0
    edict = {}
    for entry in energies:
        state = entry.get('state', '')
        e = entry.get('energy_cm1', 0.0)
        edict[state] = e
    if 'Gamma8_b_1' not in edict or 'Gamma8_b_2' not in edict:
        return 0.0
    split = abs(edict['Gamma8_b_2'] - edict['Gamma8_b_1'])
    allowed = ctx['Gamma8b_target'] * ctx['Gamma8b_tol']
    if abs(split - ctx['Gamma8b_target']) <= allowed:
        return 1.0
    return 0.0


# === block: score_4 (check id='reported_Gamma8b_splitting_check') ===
def score_4(artifact, step, ctx):
    reported = artifact.get('Gamma8_b_splitting_cm1', None)
    if reported is None or not isinstance(reported, (int, float)):
        return 0.0
    if abs(reported - ctx['reported_splitting_target']) <= ctx['reported_splitting_tol']:
        return 1.0
    return 0.0


_SCORERS = {
    'range_check': score_0,
    'ordering_check': score_1,
    'splitting_Gamma8a_check': score_2,
    'splitting_Gamma8b_from_energies_check': score_3,
    'reported_Gamma8b_splitting_check': score_4,
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
