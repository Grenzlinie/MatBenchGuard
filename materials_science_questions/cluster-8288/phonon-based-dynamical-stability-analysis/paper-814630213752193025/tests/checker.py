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


# === block: score_0 (check id='step_01_structure') ===
def score_0(artifact, step, ctx):
    import math
    artifact = artifact  # passed in
    fields = step.get('fields', {})
    total = len(fields)
    if total == 0:
        return 0.0
    passed = 0
    for field, cfg in fields.items():
        val = artifact.get(field)
        if val is None or not isinstance(val, (int, float)):
            continue
        tol = cfg.get('tolerance', 0.0)
        target = cfg.get('target', 0.0)
        if abs(val - target) <= tol + 1e-9:
            passed += 1
    return passed / total


# === block: score_1 (check id='step_04_band_gap') ===
def score_1(artifact, step, ctx):
    minority = artifact.get('minority_gap')
    majority = artifact.get('majority_has_bands_at_Fermi')
    score = 0.0
    if isinstance(minority, (int, float)) and minority > step.get('minority_gap_min', 0.0):
        score += 0.5
    if majority is True or majority == step.get('majority_required', True):
        score += 0.5
    return score


# === block: score_2 (check id='step_02_phonon') ===
def score_2(artifact, step, ctx):
    import math
    branches = step.get('expected_branches', [])
    tol = step.get('tolerance_freq', 15.0)
    agent_list = artifact if isinstance(artifact, list) else []
    if not branches:
        return 0.0
    satisfied = 0
    for expected in branches:
        target_freq = expected['frequency']
        target_raman = expected['Raman_active']
        target_ir = expected['IR_active']
        need_count = expected.get('count', 1)
        matches = 0
        for item in agent_list:
            freq = item.get('frequency')
            raman = item.get('Raman_active')
            ir = item.get('IR_active')
            if freq is None or raman is None or ir is None:
                continue
            if abs(freq - target_freq) <= tol + 1e-9 and raman == target_raman and ir == target_ir:
                matches += 1
        if matches >= need_count:
            satisfied += 1
    return satisfied / len(branches)


# === block: score_3 (check id='step_03_magnetic') ===
def score_3(artifact, step, ctx):
    def within(val, target, tol):
        return abs(val - target) <= tol + 1e-9
    score = 0.0
    deltaE = artifact.get('energy_difference_per_primitive_cell')
    if isinstance(deltaE, (int, float)) and within(deltaE, step.get('target_deltaE', 93.0), step.get('tolerance_deltaE', 10.0)):
        score += 0.5
    J = artifact.get('exchange_parameter_J')
    if isinstance(J, (int, float)) and within(J, step.get('target_J', 0.97), step.get('tolerance_J', 0.2)):
        score += 0.25
    Tc = artifact.get('Curie_temperature')
    if isinstance(Tc, (int, float)) and within(Tc, step.get('target_Tc', 17.0), step.get('tolerance_Tc', 5.0)):
        score += 0.25
    return score


_SCORERS = {
    'step_01_structure': score_0,
    'step_04_band_gap': score_1,
    'step_02_phonon': score_2,
    'step_03_magnetic': score_3,
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
