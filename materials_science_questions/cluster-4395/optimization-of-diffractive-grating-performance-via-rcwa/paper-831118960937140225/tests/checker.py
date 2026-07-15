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


# === block: score_0 (check id='s1') ===
def score_0(artifact, step, ctx):
    # Efficiency check at 450 nm: threshold_or_better (higher is better)
    gold = step.get("gold_efficiency", 39.1)
    tol = step.get("gold_efficiency_tolerance", 1.0)
    expected_orders = [
        ("TE", "(-1,0)"),
        ("TE", "(0,-1)"),
        ("TM", "(-1,0)"),
        ("TM", "(0,-1)")
    ]
    n = len(expected_orders)
    threshold = gold - tol
    valid = 0
    for row in artifact:
        pol = str(row.get("polarization", "")).strip()
        ord = str(row.get("order", "")).strip()
        try:
            eff = float(row.get("efficiency", "nan"))
        except:
            eff = None
        if eff is None:
            continue
        if (pol, ord) in expected_orders:
            if eff >= threshold:
                valid += 1
    if n == 0:
        score = 0.0
    else:
        score = valid / n
    return score


# === block: score_1 (check id='s2') ===
def score_1(artifact, step, ctx):
    # Compute wavelength range where both orders exceed threshold for TE and TM
    threshold = step.get("threshold", 35.0)
    gold_lower = step.get("gold_wavelength_lower", 429.0)
    gold_upper = step.get("gold_wavelength_upper", 468.0)
    wavelength_tol = step.get("wavelength_tolerance", 2.0)

    if not artifact:
        return 0.0

    # Parse data
    wavelengths = []
    te_m1 = []
    te_01 = []
    tm_m1 = []
    tm_01 = []
    for row in artifact:
        try:
            wl = float(row["wavelength_nm"])
            te_m1_val = float(row["DE_(-1,0)_TE"])
            te_01_val = float(row["DE_(0,-1)_TE"])
            tm_m1_val = float(row["DE_(-1,0)_TM"])
            tm_01_val = float(row["DE_(0,-1)_TM"])
            wavelengths.append(wl)
            te_m1.append(te_m1_val)
            te_01.append(te_01_val)
            tm_m1.append(tm_m1_val)
            tm_01.append(tm_01_val)
        except:
            continue

    if not wavelengths:
        return 0.0

    # Sort by wavelength
    order = sorted(range(len(wavelengths)), key=lambda i: wavelengths[i])

    def get_range(wl, v1, v2):
        indices = [i for i in order if v1[i] > threshold and v2[i] > threshold]
        if not indices:
            return None, None
        return wl[indices[0]], wl[indices[-1]]

    te_low, te_high = get_range(wavelengths, te_m1, te_01)
    tm_low, tm_high = get_range(wavelengths, tm_m1, tm_01)

    def within(low, high, gl, gh, tol):
        if low is None or high is None:
            return False
        return abs(low - gl) <= tol and abs(high - gh) <= tol

    valid_te = within(te_low, te_high, gold_lower, gold_upper, wavelength_tol)
    valid_tm = within(tm_low, tm_high, gold_lower, gold_upper, wavelength_tol)
    score = (0.5 if valid_te else 0.0) + (0.5 if valid_tm else 0.0)
    return score


# === block: score_2 (check id='s3') ===
def score_2(artifact, step, ctx):
    # Compute incident angle range where both orders exceed threshold for TE and TM
    threshold = step.get("threshold", 30.0)
    gold_lower = step.get("gold_angle_lower", -3.2)
    gold_upper = step.get("gold_angle_upper", 3.2)
    angle_tol = step.get("angle_tolerance", 0.5)

    if not artifact:
        return 0.0

    angles = []
    te_m1 = []
    te_01 = []
    tm_m1 = []
    tm_01 = []
    for row in artifact:
        try:
            ang = float(row["incident_angle_deg"])
            te_m1_val = float(row["DE_(-1,0)_TE"])
            te_01_val = float(row["DE_(0,-1)_TE"])
            tm_m1_val = float(row["DE_(-1,0)_TM"])
            tm_01_val = float(row["DE_(0,-1)_TM"])
            angles.append(ang)
            te_m1.append(te_m1_val)
            te_01.append(te_01_val)
            tm_m1.append(tm_m1_val)
            tm_01.append(tm_01_val)
        except:
            continue

    if not angles:
        return 0.0

    order = sorted(range(len(angles)), key=lambda i: angles[i])

    def get_range(ang, v1, v2):
        indices = [i for i in order if v1[i] > threshold and v2[i] > threshold]
        if not indices:
            return None, None
        return ang[indices[0]], ang[indices[-1]]

    te_low, te_high = get_range(angles, te_m1, te_01)
    tm_low, tm_high = get_range(angles, tm_m1, tm_01)

    def within(low, high, gl, gh, tol):
        if low is None or high is None:
            return False
        return abs(low - gl) <= tol and abs(high - gh) <= tol

    valid_te = within(te_low, te_high, gold_lower, gold_upper, angle_tol)
    valid_tm = within(tm_low, tm_high, gold_lower, gold_upper, angle_tol)
    score = (0.5 if valid_te else 0.0) + (0.5 if valid_tm else 0.0)
    return score


# === block: score_3 (check id='s4') ===
def score_3(artifact, step, ctx):
    # Find region where total effective efficiency exceeds threshold
    threshold = step.get("total_eff_threshold", 75.0)
    h1_low_gold = step["gold_h1_lower"]
    h1_high_gold = step["gold_h1_upper"]
    h2_low_gold = step["gold_h2_lower"]
    h2_high_gold = step["gold_h2_upper"]
    tol = step.get("thickness_tolerance", 5.0)

    rows_ok = []
    for row in artifact:
        try:
            h1 = float(row["h1_nm"])
            h2 = float(row["h2_nm"])
            te = float(row["total_eff_TE"])
            tm = float(row["total_eff_TM"])
            if te > threshold and tm > threshold:
                rows_ok.append((h1, h2))
        except:
            continue

    if not rows_ok:
        return 0.0

    h1_vals = [r[0] for r in rows_ok]
    h2_vals = [r[1] for r in rows_ok]
    ok = (abs(min(h1_vals) - h1_low_gold) <= tol and
          abs(max(h1_vals) - h1_high_gold) <= tol and
          abs(min(h2_vals) - h2_low_gold) <= tol and
          abs(max(h2_vals) - h2_high_gold) <= tol)
    return 1.0 if ok else 0.0


# === block: score_4 (check id='s5') ===
def score_4(artifact, step, ctx):
    # Compute period and slanted angle ranges where all four order efficiencies exceed threshold
    threshold = step.get("order_threshold", 35.0)
    p_low_gold = step["gold_period_lower"]
    p_high_gold = step["gold_period_upper"]
    p_tol = step.get("period_tolerance", 2.0)
    a_low_gold = step["gold_angle_lower"]
    a_high_gold = step["gold_angle_upper"]
    a_tol = step.get("angle_tolerance", 0.5)

    rows_ok = []
    for row in artifact:
        try:
            p = float(row["period_nm"])
            a = float(row["slanted_angle_deg"])
            de_te_m1 = float(row["DE_(-1,0)_TE"])
            de_te_01 = float(row["DE_(0,-1)_TE"])
            de_tm_m1 = float(row["DE_(-1,0)_TM"])
            de_tm_01 = float(row["DE_(0,-1)_TM"])
            if (de_te_m1 > threshold and de_te_01 > threshold and
                de_tm_m1 > threshold and de_tm_01 > threshold):
                rows_ok.append((p, a))
        except:
            continue

    if not rows_ok:
        return 0.0

    p_min = min(r[0] for r in rows_ok)
    p_max = max(r[0] for r in rows_ok)
    a_min = min(r[1] for r in rows_ok)
    a_max = max(r[1] for r in rows_ok)
    ok_period = abs(p_min - p_low_gold) <= p_tol and abs(p_max - p_high_gold) <= p_tol
    ok_angle = abs(a_min - a_low_gold) <= a_tol and abs(a_max - a_high_gold) <= a_tol
    if ok_period and ok_angle:
        return 1.0
    elif ok_period != ok_angle:
        return 0.5
    else:
        return 0.0


# === block: score_5 (check id='s6') ===
def score_5(artifact, step, ctx):
    # Compute duty cycle range where all four order efficiencies exceed threshold
    threshold = step.get("order_threshold", 35.0)
    d_low_gold = step["gold_duty_lower"]
    d_high_gold = step["gold_duty_upper"]
    d_tol = step.get("duty_tolerance", 0.01)

    rows_ok = []
    for row in artifact:
        try:
            d = float(row["duty_cycle"])
            de_te_m1 = float(row["DE_(-1,0)_TE"])
            de_te_01 = float(row["DE_(0,-1)_TE"])
            de_tm_m1 = float(row["DE_(-1,0)_TM"])
            de_tm_01 = float(row["DE_(0,-1)_TM"])
            if (de_te_m1 > threshold and de_te_01 > threshold and
                de_tm_m1 > threshold and de_tm_01 > threshold):
                rows_ok.append(d)
        except:
            continue

    if not rows_ok:
        return 0.0

    d_min = min(rows_ok)
    d_max = max(rows_ok)
    ok = abs(d_min - d_low_gold) <= d_tol and abs(d_max - d_high_gold) <= d_tol
    return 1.0 if ok else 0.0


_SCORERS = {
    's1': score_0,
    's2': score_1,
    's3': score_2,
    's4': score_3,
    's5': score_4,
    's6': score_5,
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
