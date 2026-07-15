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
    def prepare(outputs_dir, spec):
        gold = spec.get('gold', {})
        return {'gold': gold}


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
        if not isinstance(artifact, list) or len(artifact) != 10:
            return 0.0
        required_cols = {'system', 'shape', 'formation_energy'}
        if not all(col in artifact[0] for col in required_cols):
            return 0.0
        shapes = {d['shape'] for d in artifact}
        systems = {d['system'] for d in artifact}
        if shapes != {'4S', '4N', '4T', '4L', '4l'} or systems != {'Pt4/Cu', 'Au4/Ag'}:
            return 0.0
        return 1.0


# === block: score_1 (check id='value_check') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        gold_vals = ctx['gold']['formation_energies']
        tol = step.get('tolerance', 0.05)
        count = 0
        for row in artifact:
            sys = row['system']
            shape = row['shape']
            val = float(row['formation_energy'])
            ref = gold_vals.get(sys, {}).get(shape)
            if ref is not None and abs(val - ref) <= tol:
                count += 1
        return count / len(artifact) if artifact else 0.0


# === block: score_2 (check id='ordering_check') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        slack = step.get('slack', 0.01)
        by_system = {}
        for row in artifact:
            sys = row['system']
            shape = row['shape']
            val = float(row['formation_energy'])
            by_system.setdefault(sys, {})[shape] = val
        inequalities = []
        for sys, vals in by_system.items():
            v4l = vals.get('4l')
            v4S = vals.get('4S')
            if v4l is None or v4S is None:
                continue
            others = [v for s, v in vals.items() if s not in ('4l', '4S')]
            for other in others:
                inequalities.append(v4l - other >= -slack)
            for other in others:
                inequalities.append(v4S - other >= -slack)
        if not inequalities:
            return 0.0
        return sum(inequalities) / len(inequalities)


_SCORERS = {
    'shape_check': score_0,
    'value_check': score_1,
    'ordering_check': score_2,
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
