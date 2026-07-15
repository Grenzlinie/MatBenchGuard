import os
import json
import csv

# === author imports / helpers ===
import json
import math

def get_nested(data, path):
    parts = path.split('.')
    cur = data
    for p in parts:
        if isinstance(cur, dict):
            cur = cur.get(p)
            if cur is None:
                return None
        else:
            return None
    return cur

def score_value(val, spec):
    targets = spec.get('target')
    policy = spec.get('policy', 'reference_match')
    if policy == 'exact_match':
        return 1.0 if val == targets else 0.0
    tol_abs = spec.get('tol_abs', None)
    tol_abs_rel = spec.get('tol_abs_rel', None)
    if policy == 'reference_match':
        if tol_abs is not None:
            # linear decay: full credit within tolerance, zero beyond 2*tolerance
            diff = abs(val - targets)
            if diff <= tol_abs:
                return 1.0
            return max(0.0, 1.0 - (diff - tol_abs) / tol_abs)
        elif tol_abs_rel is not None:
            if targets == 0:
                return 0.0
            rel_err = abs(val - targets) / abs(targets)
            if rel_err <= tol_abs_rel:
                return 1.0
            return max(0.0, 1.0 - (rel_err - tol_abs_rel) / tol_abs_rel)
        return 0.0
    if policy == 'threshold_or_better':
        # directional: higher is better
        if val >= targets:
            return 1.0
        # decay below target, using tol_abs as decay margin
        decay_tol = spec.get('tol_abs', 2.0)  # default 2 pp
        deficit = targets - val
        return max(0.0, 1.0 - deficit / (decay_tol * 1.5))
    return 0.0


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


# === block: score_0 (check id='monolayer_check') ===
def score_0(artifact, step, ctx):
    artifact_path = '/app/outputs/monolayer_properties.json'
    import json
    with open(artifact_path, 'r') as f:
        data = json.load(f)
    fields = step.get('fields', {})
    if not fields:
        return 1.0
    scores = []
    for path, spec in fields.items():
        val = get_nested(data, path)
        if val is None:
            scores.append(0.0)
            continue
        scores.append(score_value(val, spec))
    return sum(scores) / len(scores)


# === block: score_1 (check id='hetero_check') ===
def score_1(artifact, step, ctx):
    artifact_path = '/app/outputs/heterostructure_properties.json'
    import json
    with open(artifact_path, 'r') as f:
        data = json.load(f)
    fields = step.get('fields', {})
    if not fields:
        return 1.0
    scores = []
    for path, spec in fields.items():
        val = get_nested(data, path)
        if val is None:
            scores.append(0.0)
            continue
        scores.append(score_value(val, spec))
    return sum(scores) / len(scores)


# === block: score_2 (check id='sth_check') ===
def score_2(artifact, step, ctx):
    artifact_path = '/app/outputs/st_hydrogen_efficiency.json'
    import json
    with open(artifact_path, 'r') as f:
        data = json.load(f)
    fields = step.get('fields', {})
    if not fields:
        return 1.0
    scores = []
    for path, spec in fields.items():
        val = get_nested(data, path)
        if val is None:
            scores.append(0.0)
            continue
        scores.append(score_value(val, spec))
    return sum(scores) / len(scores)


_SCORERS = {
    'monolayer_check': score_0,
    'hetero_check': score_1,
    'sth_check': score_2,
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
