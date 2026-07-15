import os
import json
import csv

# === author imports / helpers ===
import json, os, math


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
    steps = spec.get('steps', [])
    if steps:
        step0 = steps[0]
        return {'gold': step0.get('gold', {}), 'tolerances': step0.get('tolerances', {})}
    return {'gold': {}, 'tolerances': {}}


# === block: score_0 (check id='reproduction_results') ===
def score_0(artifact, step, ctx):
    def _isclose_path(path, expected_val, actual_val, tol_config):
        if 'distance' in path:
            atol = tol_config.get('distance_abs', 0.05)
        elif 'energy' in path or 'band_gap' in path:
            atol = tol_config.get('energy_abs', 0.05)
        elif 'magnetic' in path:
            atol = tol_config.get('magnetic_abs', 0.05)
        else:
            atol = 0.001
        if not isinstance(actual_val, (int, float)) or not isinstance(expected_val, (int, float)):
            return actual_val == expected_val
        return math.isclose(actual_val, expected_val, abs_tol=atol)

    def _walk(actual, expected, tol_config, path=''):
        checks = []
        if isinstance(expected, dict):
            if not isinstance(actual, dict):
                checks.append(False)
                return checks
            for k in expected:
                new_path = path + '.' + k
                if k not in actual:
                    checks.append(False)
                else:
                    checks.extend(_walk(actual[k], expected[k], tol_config, new_path))
        elif isinstance(expected, list):
            if not isinstance(actual, list):
                checks.append(False)
                return checks
            if len(expected) == 0:
                return checks
            if isinstance(expected[0], dict) and 'label' in expected[0]:
                act_by_label = {item.get('label'): item for item in actual if isinstance(item, dict)}
                for exp_item in expected:
                    label = exp_item.get('label')
                    if label not in act_by_label:
                        checks.append(False)
                    else:
                        checks.extend(_walk(act_by_label[label], exp_item, tol_config, path + '.' + label))
            else:
                if len(actual) != len(expected):
                    for i, exp_item in enumerate(expected):
                        if i < len(actual):
                            checks.extend(_walk(actual[i], exp_item, tol_config, path + f'[{i}]'))
                        else:
                            checks.append(False)
                else:
                    for i, (act_item, exp_item) in enumerate(zip(actual, expected)):
                        checks.extend(_walk(act_item, exp_item, tol_config, path + f'[{i}]'))
        elif isinstance(expected, (int, float)):
            checks.append(_isclose_path(path, expected, actual, tol_config))
        else:
            checks.append(actual == expected)
        return checks

    gold = dict(ctx['gold'])
    # band_gap value is not reported in the paper; remove it from gold to avoid
    # scoring an unreachable target.
    if 'monolayer' in gold and 'band_gap' in gold['monolayer']:
        del gold['monolayer']['band_gap']
    tol_config = ctx['tolerances']
    artifact_data = artifact
    checks = _walk(artifact_data, gold, tol_config)
    if not checks:
        return 0.0
    passed = sum(1 for c in checks if c)
    return passed / len(checks)


_SCORERS = {
    'reproduction_results': score_0,
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
