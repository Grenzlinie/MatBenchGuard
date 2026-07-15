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
    gold_entries = []
    thresholds = {}
    for step in spec.get('steps', []):
        if step.get('id') == 'symmetry_classification':
            gold_entries = step.get('gold_entries', [])
        elif step.get('id') == 'photomagnetism_dynamics':
            thresholds = step.get('thresholds', {})
    return {'gold_entries': gold_entries, 'thresholds': thresholds}


# === block: score_0 (check id='symmetry_classification') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list):
        return 0.0
    gold = ctx['gold_entries']
    if not gold:
        return 0.0
    matched = 0
    for g in gold:
        for a in artifact:
            if (a.get('irreducible_representation') == g['irreducible_representation'] and
                a.get('axial_isotropy_subgroup') == g['axial_isotropy_subgroup'] and
                a.get('abbreviation') == g['abbreviation']):
                matched += 1
                break
    return matched / len(gold)


# === block: score_1 (check id='photomagnetism_dynamics') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    thresh = ctx['thresholds']
    M_ab_thresh = float(thresh.get('M_ab_threshold', 0.1))
    M_c_thresh  = float(thresh.get('M_c_threshold', 0.05))
    double_ratio = float(thresh.get('double_step_ratio', 1.5))
    smooth_w = int(thresh.get('smoothing_window', 3))

    # extract columns as floats
    ts = []
    m_abs = []
    m_cs = []
    e_abs = []
    for row in artifact:
        try:
            ts.append(float(row['t']))
            m_abs.append(abs(float(row['M_ab'])))
            m_cs.append(abs(float(row['M_c'])))
            e_abs.append(float(row['E_ab']))
        except (ValueError, KeyError):
            continue
    n = len(ts)
    if n < 10:
        return 0.0

    # max magnetization
    max_m_ab = max(m_abs) if m_abs else 0.0
    max_m_c  = max(m_cs) if m_cs else 0.0
    score_mag = 0.5 if (max_m_ab > M_ab_thresh and max_m_c < M_c_thresh) else 0.0

    # numeric derivative of E_ab (central difference)
    dt = (ts[-1] - ts[0]) / (n - 1) if n > 1 else 1.0
    dE = []
    for i in range(1, n-1):
        dE.append((e_abs[i+1] - e_abs[i-1]) / (2 * dt))
    if len(dE) < 5:
        return score_mag

    # simple smoothing moving average
    smoothed = []
    for i in range(len(dE)):
        win = dE[max(0, i-smooth_w): min(len(dE), i+smooth_w+1)]
        smoothed.append(sum(win) / len(win))

    # find local maxima (peaks) with positive derivative
    peaks = []
    for i in range(1, len(smoothed)-1):
        if smoothed[i] > max(smoothed[i-1], smoothed[i+1]) and smoothed[i] > 0:
            peaks.append(i)

    if len(peaks) < 2:
        return score_mag

    # take first two major peaks (by time)
    first = peaks[0]
    second = peaks[1]
    # valley = minimum of smoothed between them
    valley = min(smoothed[first:second+1])
    if valley <= 0:
        score_double = 0.0
    else:
        peak_val = smoothed[second]
        if peak_val / valley >= double_ratio:
            score_double = 0.5
        else:
            score_double = 0.0

    return score_mag + score_double


_SCORERS = {
    'symmetry_classification': score_0,
    'photomagnetism_dynamics': score_1,
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
