import os
import json
import csv

# === author imports / helpers ===
import os, json

def score_error_metric(value, target_max, max_for_zero):
    if value <= target_max:
        return 1.0
    if value >= max_for_zero:
        return 0.0
    return max(0.0, 1.0 - (value - target_max) / (max_for_zero - target_max))

def score_accuracy_metric(value, target_min):
    if value >= target_min:
        return 1.0
    if value <= 0.0:
        return 0.0
    return value / target_min


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
    import os, json

    def prepare(outputs_dir, spec):
        # Extract hidden configurations from steps for easy access
        ctx = {}
        for step in spec.get('steps', []):
            sid = step['id']
            ctx[sid] = step.get('hidden_config', {})
        return ctx


# === block: score_0 (check id='desc_set') ===
def score_0(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    agent_set = set(line.strip() for line in lines if line.strip())
    expected = set(step.get('hidden_config', {}).get('expected_set', []))
    if not expected:
        return 0.0
    intersection = agent_set & expected
    return len(intersection) / len(expected)


# === block: score_1 (check id='coeff_struct') ===
def score_1(artifact, step, ctx):
    cfg = step.get('hidden_config', {})
    expected_descriptors = set(cfg.get('expected_descriptors', []))
    score = 0.0
    if isinstance(artifact, dict):
        # constant_A present and numeric
        if isinstance(artifact.get('constant_A'), (int, float)):
            score += 0.2
        coeff = artifact.get('coefficients')
        if isinstance(coeff, dict):
            # exactly 17 keys
            if len(coeff) == 17:
                score += 0.4
            # all keys in expected set
            if set(coeff.keys()) == expected_descriptors:
                score += 0.4
        else:
            score += 0.0
    return min(1.0, score)


# === block: score_2 (check id='mae_after') ===
def score_2(artifact, step, ctx):
    cfg = step.get('hidden_config', {})
    field = step.get('field', 'mae_after_calibration')
    if not isinstance(artifact, dict) or field not in artifact:
        return 0.0
    value = artifact[field]
    if not isinstance(value, (int, float)):
        return 0.0
    target_max = cfg.get('target_max', 2.6)
    max_for_zero = cfg.get('max_for_zero', 6.0)
    return score_error_metric(value, target_max, max_for_zero)


# === block: score_3 (check id='r2') ===
def score_3(artifact, step, ctx):
    cfg = step.get('hidden_config', {})
    field = step.get('field', 'r_squared')
    if not isinstance(artifact, dict) or field not in artifact:
        return 0.0
    value = artifact[field]
    if not isinstance(value, (int, float)):
        return 0.0
    target_min = cfg.get('target_min', 0.81)
    return score_accuracy_metric(value, target_min)


# === block: score_4 (check id='q2') ===
def score_4(artifact, step, ctx):
    cfg = step.get('hidden_config', {})
    field = step.get('field', 'q_squared')
    if not isinstance(artifact, dict) or field not in artifact:
        return 0.0
    value = artifact[field]
    if not isinstance(value, (int, float)):
        return 0.0
    target_min = cfg.get('target_min', 0.79)
    return score_accuracy_metric(value, target_min)


_SCORERS = {
    'desc_set': score_0,
    'coeff_struct': score_1,
    'mae_after': score_2,
    'r2': score_3,
    'q2': score_4,
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
