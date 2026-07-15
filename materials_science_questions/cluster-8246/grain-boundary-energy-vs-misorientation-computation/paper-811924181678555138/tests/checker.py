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
    step = spec['steps'][0]
    ctx = {
        'tolerance': step.get('tolerance', 0.05),
        'sanity_low': step['sanity_range'][0],
        'sanity_high': step['sanity_range'][1],
    }
    return ctx


# === block: score_0 (check id='step_structural_trend') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts from csv
    import math

    sanity_low = ctx['sanity_low']
    sanity_high = ctx['sanity_high']
    tol = ctx['tolerance']
    min_std = ctx.get('min_std', 0.001)
    min_corr = ctx.get('min_corr', 0.5)

    # sanity gate: all energies must be positive and within plausible range
    for row in artifact:
        e = float(row['energy_Jm2'])
        if e <= 0 or e < sanity_low or e > sanity_high:
            return 0.0

    # separate by tilt axis
    groups = {'111': [], '100': []}
    for row in artifact:
        axis = row['tilt_axis'].strip()
        angle = float(row['angle_deg'])
        energy = float(row['energy_Jm2'])
        if axis in groups:
            groups[axis].append((angle, energy))
        else:
            return 0.0

    # ensure each axis has at least 6 points
    if len(groups['111']) < 6 or len(groups['100']) < 6:
        return 0.0

    # helper to compute Pearson correlation
    def pearson_r(xs, ys):
        n = len(xs)
        if n < 2:
            return 0.0
        mean_x = sum(xs)/n
        mean_y = sum(ys)/n
        cov = sum((x - mean_x)*(y - mean_y) for x,y in zip(xs,ys))
        sx = math.sqrt(sum((x - mean_x)**2 for x in xs))
        sy = math.sqrt(sum((y - mean_y)**2 for y in ys))
        if sx == 0 or sy == 0:
            return 0.0
        return cov/(sx*sy)

    # check monotonic increasing trend via correlation and avoid flat lines
    for axis in ['111', '100']:
        if len(groups[axis]) < 2:
            return 0.0
        angles = [a for a,e in groups[axis]]
        energies = [e for a,e in groups[axis]]
        r = pearson_r(angles, energies)
        if r < min_corr:
            return 0.0
        if len(energies) > 1:
            std = math.sqrt(sum((e - sum(energies)/len(energies))**2 for e in energies) / (len(energies)-1))
            if std < min_std:
                return 0.0

    # ordering check at common angles
    angle_111 = {a: e for a,e in groups['111']}
    angle_100 = {a: e for a,e in groups['100']}
    common = set(angle_111) & set(angle_100)
    if not common:
        return 0.0
    passed = 0
    for ang in common:
        if angle_111[ang] > angle_100[ang] - tol:
            passed += 1
    return passed / len(common)


_SCORERS = {
    'step_structural_trend': score_0,
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
