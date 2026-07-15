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


# === block: score_0 (check id='fiber_strain_threshold') ===
def score_0(artifact, step, ctx):
    strains = [float(row['fiber_mechanical_strain']) for row in artifact if abs(float(row['stretch_xx'])-1.2)<1e-4]
    if not strains:
        return 0.0
    max_strain = max(strains)
    return 1.0 if max_strain <= 0.02 else 0.0


# === block: score_1 (check id='stress_stretch_check') ===
def score_1(artifact, step, ctx):
    stretch = [float(r['stretch_xx']) for r in artifact]
    stress = [float(r['stress_xx']) for r in artifact]
    if not stretch:
        return 0.0
    # monotonic (non-decreasing)
    for i in range(1,len(stress)):
        if stress[i] < stress[i-1] - 1.0:
            return 0.0
    # find index closest to 1.2
    d = [abs(s-1.2) for s in stretch]
    idx = d.index(min(d))
    if stress[idx] < 50000.0 or stress[idx] > 5000000.0:
        return 0.0
    # check near zero at stretch 1.0
    d0 = [abs(s-1.0) for s in stretch]
    idx0 = d0.index(min(d0))
    if abs(stress[idx0]) > 1000.0:
        return 0.0
    return 1.0


# === block: score_2 (check id='cycle_fixity_recompute') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    last_stretch = float(artifact[-1]['stretch_xx'])
    fixity = (last_stretch / 1.2) * 100.0
    target = float(step.get('target', 85.1))
    tol = float(step.get('tolerance_abs', 5.0))
    return 1.0 if abs(fixity - target) <= tol else 0.0


# === block: score_3 (check id='fixity_crosscheck') ===
def score_3(artifact, step, ctx):
    import csv, os
    cycle_path = '/app/outputs/stress_stretch_cycle_first3.csv'
    if not os.path.exists(cycle_path):
        return 0.0
    with open(cycle_path, newline='') as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return 0.0
    last_stretch = float(rows[-1]['stretch_xx'])
    recomputed = (last_stretch / 1.2) * 100.0
    reported = float(artifact[0]['fixity_ratio'])
    return 1.0 if abs(reported - recomputed) <= 0.5 else 0.0


# === block: score_4 (check id='constrained_peak_stress') ===
def score_4(artifact, step, ctx):
    peak = max(float(r['stress_xx']) for r in artifact)
    low, high = step.get('range', [200000.0, 2000000.0])
    return 1.0 if low <= peak <= high else 0.0


# === block: score_5 (check id='constrained_onset_temp') ===
def score_5(artifact, step, ctx):
    threshold = float(step.get('stress_threshold', 10000.0))
    low, high = step.get('range', [35.0, 45.0])
    for r in artifact:
        if float(r['stress_xx']) > threshold:
            onset = float(r['temperature'])
            return 1.0 if low <= onset <= high else 0.0
    return 0.0


# === block: score_6 (check id='free_recovery_temp') ===
def score_6(artifact, step, ctx):
    low, high = step.get('range', [40.0, 50.0])
    for r in artifact:
        if float(r['stretch_xx']) <= 1.01:
            temp = float(r['temperature'])
            return 1.0 if low <= temp <= high else 0.0
    return 0.0


_SCORERS = {
    'fiber_strain_threshold': score_0,
    'stress_stretch_check': score_1,
    'cycle_fixity_recompute': score_2,
    'fixity_crosscheck': score_3,
    'constrained_peak_stress': score_4,
    'constrained_onset_temp': score_5,
    'free_recovery_temp': score_6,
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
