import os
import json
import csv

# === author imports / helpers ===
import json
import os


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
    # Gold reference values (not exposed to agent)
    gold = {
        "Ni(OH)2_U0": [0.9, 1.7, 3.05, -0.73],
        "Ni(OH)2_U123": [-0.33, 0.47, 1.82, -1.96],
        "doped_U0": [0.6, 1.2, 2.55, 0.57],
        "doped_U123": [-0.63, -0.03, 1.32, -0.66],
        "Cl_diff": 0.3
    }
    ctx = {'gold': gold, 'spec': spec}
    return ctx


# === block: score_0 (check id='ni_oh2_u0') ===
def score_0(artifact, step, ctx):
    import math
    expected = ctx['gold']['Ni(OH)2_U0']
    actual = artifact.get('Ni(OH)2', {}).get('U0', {})
    mae = sum(abs(actual.get(k, 1e9) - val) for k, val in zip(['G1','G2','G3','G4'], expected)) / 4.0
    score = max(0.0, 1.0 - mae / 0.5)
    return score


# === block: score_1 (check id='ni_oh2_u123') ===
def score_1(artifact, step, ctx):
    import math
    expected = ctx['gold']['Ni(OH)2_U123']
    actual = artifact.get('Ni(OH)2', {}).get('U123', {})
    mae = sum(abs(actual.get(k, 1e9) - val) for k, val in zip(['G1','G2','G3','G4'], expected)) / 4.0
    score = max(0.0, 1.0 - mae / 0.5)
    return score


# === block: score_2 (check id='doped_u0') ===
def score_2(artifact, step, ctx):
    import math
    expected = ctx['gold']['doped_U0']
    actual = artifact.get('doped', {}).get('U0', {})
    mae = sum(abs(actual.get(k, 1e9) - val) for k, val in zip(['G1','G2','G3','G4'], expected)) / 4.0
    score = max(0.0, 1.0 - mae / 0.5)
    return score


# === block: score_3 (check id='doped_u123') ===
def score_3(artifact, step, ctx):
    import math
    expected = ctx['gold']['doped_U123']
    actual = artifact.get('doped', {}).get('U123', {})
    mae = sum(abs(actual.get(k, 1e9) - val) for k, val in zip(['G1','G2','G3','G4'], expected)) / 4.0
    score = max(0.0, 1.0 - mae / 0.5)
    return score


# === block: score_4 (check id='cl_diff') ===
def score_4(artifact, step, ctx):
    expected = ctx['gold']['Cl_diff']
    actual = artifact.get('Cl_adsorption_difference', None)
    if actual is None:
        return 0.0
    diff = abs(actual - expected)
    score = max(0.0, 1.0 - diff / 0.25)
    return score


# === block: score_5 (check id='rds') ===
def score_5(artifact, step, ctx):
    ni_o = artifact.get('Ni(OH)2', {}).get('U123', {})
    doped_o = artifact.get('doped', {}).get('U123', {})
    keys = ['G1','G2','G3','G4']
    if not ni_o or not doped_o:
        return 0.0
    ni_vals = [ni_o.get(k) for k in keys]
    doped_vals = [doped_o.get(k) for k in keys]
    if None in ni_vals or None in doped_vals:
        return 0.0
    ni_max = max(ni_vals)
    doped_max = max(doped_vals)
    ni_rds_idx = ni_vals.index(ni_max)
    doped_rds_idx = doped_vals.index(doped_max)
    score = 0.0
    if keys[ni_rds_idx] == 'G3':
        score += 0.4
    if keys[doped_rds_idx] == 'G3':
        score += 0.4
    if doped_max < ni_max - 0.05:
        score += 0.2
    return score


# === block: score_6 (check id='cl_positive') ===
def score_6(artifact, step, ctx):
    val = artifact.get('Cl_adsorption_difference', None)
    if val is None:
        return 0.0
    return 1.0 if val > 0.0 else 0.0


_SCORERS = {
    'ni_oh2_u0': score_0,
    'ni_oh2_u123': score_1,
    'doped_u0': score_2,
    'doped_u123': score_3,
    'cl_diff': score_4,
    'rds': score_5,
    'cl_positive': score_6,
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