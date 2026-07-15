import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    boiling_path = '/app/outputs/boiling_curve.csv'
    import os
    if os.path.exists(boiling_path):
        with open(boiling_path, newline='') as f:
            boiling = list(csv.DictReader(f))
    else:
        boiling = None
    return {'boiling_data': boiling}


# === block: score_0 (check id='check_static_interface') ===
def score_0(artifact, step, ctx):
    q_hot = None
    q_cold = None
    for row in artifact:
        if row.get('boundary','').strip().lower() == 'hot':
            q_hot = float(row['heat_flux'])
        elif row.get('boundary','').strip().lower() == 'cold':
            q_cold = float(row['heat_flux'])
    if q_hot is None or q_cold is None or (q_hot + q_cold) == 0:
        return 0.0
    rel_diff = 2.0 * abs(q_hot - q_cold) / (q_hot + q_cold)
    return 1.0 if rel_diff <= 1e-10 else 0.0


# === block: score_1 (check id='check_film_evaporation') ===
def score_1(artifact, step, ctx):
    threshold = 0.05
    for row in artifact:
        m = float(row['mass_flux'])
        a = float(row['analytical_mass_flux'])
        if a == 0:
            return 0.0
        err = abs(m - a) / a
        if err > threshold:
            return 0.0
    return 1.0


# === block: score_2 (check id='check_boiling_curve') ===
def score_2(artifact, step, ctx):
    points = [(float(r['Ja']), float(r['q_star'])) for r in artifact]
    if len(points) < 6:
        return 0.0
    peak_idx = max(range(len(points)), key=lambda i: points[i][1])
    # check monotonic increase before peak
    for i in range(1, peak_idx+1):
        if points[i][1] < points[i-1][1] - 1e-15:
            return 0.0
    # check decrease after peak
    for i in range(peak_idx+1, len(points)):
        if points[i][1] > points[i-1][1] + 1e-15:
            return 0.0
    Ja_peak, q_peak = points[peak_idx]
    gold_Ja = 0.186
    gold_q = 0.0032
    tol_Ja = 0.02
    tol_q = 0.0005
    score = 0.0
    if len(points) >= 6:
        score += 0.2
    # shape passed (already enforced above)
    score += 0.3
    if abs(Ja_peak - gold_Ja) <= tol_Ja:
        score += 0.25
    if abs(q_peak - gold_q) <= tol_q:
        score += 0.25
    return score


# === block: score_3 (check id='check_critical_heat_flux') ===
def score_3(artifact, step, ctx):
    if not artifact:
        return 0.0
    row = artifact[0]
    try:
        Ja_chf = float(row['Ja_CHF'])
        q_chf = float(row['q_star_CHF'])
    except:
        return 0.0
    if not (abs(Ja_chf - 0.186) <= 0.02 and abs(q_chf - 0.0032) <= 0.0005):
        return 0.0
    boiling = ctx.get('boiling_data')
    if boiling is None:
        return 0.0
    peaks = [(float(r['Ja']), float(r['q_star'])) for r in boiling]
    if not peaks:
        return 0.0
    peak_idx = max(range(len(peaks)), key=lambda i: peaks[i][1])
    peak_Ja, peak_q = peaks[peak_idx]
    if abs(Ja_chf - peak_Ja) > 1e-6 or abs(q_chf - peak_q) > 1e-6:
        return 0.0
    return 1.0


_SCORERS = {
    'check_static_interface': score_0,
    'check_film_evaporation': score_1,
    'check_boiling_curve': score_2,
    'check_critical_heat_flux': score_3,
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
