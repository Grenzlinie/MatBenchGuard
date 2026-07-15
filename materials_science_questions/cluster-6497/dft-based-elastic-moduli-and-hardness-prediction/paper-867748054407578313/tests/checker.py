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
    return {}


# === block: score_0 (check id='phase_d09_a') ===
def score_0(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_9')
    val = phase['a']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_1 (check id='phase_d09_V0') ===
def score_1(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_9')
    val = phase['V0']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_2 (check id='phase_d09_Ecoh') ===
def score_2(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_9')
    val = phase['Ecoh']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_3 (check id='phase_d09_B0') ===
def score_3(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_9')
    val = phase['B0']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_4 (check id='phase_d09_B0_prime') ===
def score_4(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_9')
    val = phase['B0_prime']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_5 (check id='phase_d09_band_gap') ===
def score_5(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_9')
    val = phase['band_gap']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_6 (check id='phase_d09_band_gap_type') ===
def score_6(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_9')
    val = phase['band_gap_type']
    return 1.0 if val == step['target'] else 0.0


# === block: score_7 (check id='phase_d2_a') ===
def score_7(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_2')
    val = phase['a']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_8 (check id='phase_d2_V0') ===
def score_8(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_2')
    val = phase['V0']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_9 (check id='phase_d2_Ecoh') ===
def score_9(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_2')
    val = phase['Ecoh']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_10 (check id='phase_d2_B0') ===
def score_10(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_2')
    val = phase['B0']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_11 (check id='phase_d2_B0_prime') ===
def score_11(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_2')
    val = phase['B0_prime']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_12 (check id='phase_d2_band_gap') ===
def score_12(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_2')
    val = phase['band_gap']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_13 (check id='phase_d2_band_gap_type') ===
def score_13(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'D0_2')
    val = phase['band_gap_type']
    return 1.0 if val == step['target'] else 0.0


# === block: score_14 (check id='phase_rhf3_a') ===
def score_14(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'RhF3')
    val = phase['a']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_15 (check id='phase_rhf3_V0') ===
def score_15(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'RhF3')
    val = phase['V0']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_16 (check id='phase_rhf3_Ecoh') ===
def score_16(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'RhF3')
    val = phase['Ecoh']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_17 (check id='phase_rhf3_B0') ===
def score_17(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'RhF3')
    val = phase['B0']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_18 (check id='phase_rhf3_B0_prime') ===
def score_18(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'RhF3')
    val = phase['B0_prime']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_19 (check id='phase_rhf3_band_gap') ===
def score_19(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'RhF3')
    val = phase['band_gap']
    target = step['target']
    tol = step['tolerance']
    err = abs(val - target)
    score = max(0.0, 1.0 - err / (2.0 * tol))
    return score


# === block: score_20 (check id='phase_rhf3_band_gap_type') ===
def score_20(artifact, step, ctx):
    import json
    artifact_data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phase = next(p for p in artifact_data['phases'] if p['name'] == 'RhF3')
    val = phase['band_gap_type']
    return 1.0 if val == step['target'] else 0.0


# === block: score_21 (check id='cross_V0_consistency') ===
def score_21(artifact, step, ctx):
    import json
    data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phases = data['phases']
    def get_prop(name, prop):
        for p in phases:
            if p['name'] == name:
                return p[prop]
        raise ValueError('Phase not found')
    ref = get_prop('D0_9', 'V0')
    vals = [get_prop('D0_2', 'V0'), get_prop('RhF3', 'V0')]
    max_dev = max(abs(v - ref) for v in vals)
    tol = step['tolerance_absolute']
    score = max(0.0, 1.0 - max_dev / (2.0 * tol))
    return score


# === block: score_22 (check id='cross_Ecoh_consistency') ===
def score_22(artifact, step, ctx):
    import json
    data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phases = data['phases']
    def get_prop(name, prop):
        for p in phases:
            if p['name'] == name:
                return p[prop]
        raise ValueError('Phase not found')
    ref = get_prop('D0_9', 'Ecoh')
    vals = [get_prop('D0_2', 'Ecoh'), get_prop('RhF3', 'Ecoh')]
    max_dev = max(abs(v - ref) for v in vals)
    tol = step['tolerance_absolute']
    score = max(0.0, 1.0 - max_dev / (2.0 * tol))
    return score


# === block: score_23 (check id='cross_bandgap_consistency') ===
def score_23(artifact, step, ctx):
    import json
    data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phases = data['phases']
    def get_prop(name, prop):
        for p in phases:
            if p['name'] == name:
                return p[prop]
        raise ValueError('Phase not found')
    ref = get_prop('D0_9', 'band_gap')
    vals = [get_prop('D0_2', 'band_gap'), get_prop('RhF3', 'band_gap')]
    max_dev = max(abs(v - ref) for v in vals)
    tol = step['tolerance_absolute']
    score = max(0.0, 1.0 - max_dev / (2.0 * tol))
    return score


# === block: score_24 (check id='cross_B0_consistency') ===
def score_24(artifact, step, ctx):
    import json
    data = json.load(open(os.path.join('/app/outputs', 'ag3n_equilibrium_properties.json')))
    phases = data['phases']
    def get_prop(name, prop):
        for p in phases:
            if p['name'] == name:
                return p[prop]
        raise ValueError('Phase not found')
    ref = get_prop('D0_9', 'B0')
    vals = [get_prop('D0_2', 'B0'), get_prop('RhF3', 'B0')]
    max_dev = max(abs(v - ref) for v in vals)
    tol = step['tolerance_absolute']
    score = max(0.0, 1.0 - max_dev / (2.0 * tol))
    return score


_SCORERS = {
    'phase_d09_a': score_0,
    'phase_d09_V0': score_1,
    'phase_d09_Ecoh': score_2,
    'phase_d09_B0': score_3,
    'phase_d09_B0_prime': score_4,
    'phase_d09_band_gap': score_5,
    'phase_d09_band_gap_type': score_6,
    'phase_d2_a': score_7,
    'phase_d2_V0': score_8,
    'phase_d2_Ecoh': score_9,
    'phase_d2_B0': score_10,
    'phase_d2_B0_prime': score_11,
    'phase_d2_band_gap': score_12,
    'phase_d2_band_gap_type': score_13,
    'phase_rhf3_a': score_14,
    'phase_rhf3_V0': score_15,
    'phase_rhf3_Ecoh': score_16,
    'phase_rhf3_B0': score_17,
    'phase_rhf3_B0_prime': score_18,
    'phase_rhf3_band_gap': score_19,
    'phase_rhf3_band_gap_type': score_20,
    'cross_V0_consistency': score_21,
    'cross_Ecoh_consistency': score_22,
    'cross_bandgap_consistency': score_23,
    'cross_B0_consistency': score_24,
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
