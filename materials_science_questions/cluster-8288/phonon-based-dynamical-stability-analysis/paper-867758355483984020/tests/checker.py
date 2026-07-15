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


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    params = step.get('parameters', {})
    required_compounds = set(params.get('required_compounds', []))
    required_keys = params.get('required_keys', [])
    zlen = params.get('zeta_length', 5)
    tlen = params.get('TA2_length', 5)
    if not isinstance(artifact, dict):
        return 0.0
    if set(artifact.keys()) != required_compounds:
        return 0.0
    for comp in required_compounds:
        data = artifact[comp]
        if not isinstance(data, dict):
            return 0.0
        for k in required_keys:
            if k not in data:
                return 0.0
        if len(data['zeta']) != zlen or len(data['TA2']) != tlen:
            return 0.0
    return 1.0


# === block: score_1 (check id='stability_classification') ===
def score_1(artifact, step, ctx):
    params = step.get('parameters', {})
    threshold = float(params.get('imaginary_threshold', -1e-9))
    expected = params.get('expected', {})
    if not isinstance(artifact, dict):
        return 0.0
    correct = 0
    for comp, exp_label in expected.items():
        if comp not in artifact:
            continue
        ta2 = artifact[comp].get('TA2', [])
        if not ta2:
            continue
        agent_label = 'unstable' if min(ta2) < threshold else 'stable'
        if agent_label == exp_label:
            correct += 1
    return correct / len(expected) if expected else 0.0


# === block: score_2 (check id='t2g_inversion_self_consistency') ===
def score_2(artifact, step, ctx):
    params = step.get('parameters', {})
    threshold = float(params.get('imaginary_threshold', -1e-9))
    if not isinstance(artifact, dict):
        return 0.0
    unstable_t2g = []
    stable_t2g = []
    for comp, data in artifact.items():
        if not isinstance(data, dict):
            continue
        ta2 = data.get('TA2', [])
        t2g = data.get('T2g_at_Gamma')
        if not ta2 or t2g is None:
            continue
        if min(ta2) < threshold:
            unstable_t2g.append(t2g)
        else:
            stable_t2g.append(t2g)
    if not unstable_t2g or not stable_t2g:
        return 0.0
    max_unstable = max(unstable_t2g)
    min_stable = min(stable_t2g)
    return 1.0 if max_unstable < min_stable else 0.0


_SCORERS = {
    'shape_check': score_0,
    'stability_classification': score_1,
    't2g_inversion_self_consistency': score_2,
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
