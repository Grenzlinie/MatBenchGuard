import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='ca_mg_numeric') ===
def score_0(artifact, step, ctx):
    import csv
    import os

    digitized_path = os.path.join('/tests', 'ca_mg_digitized.csv')
    gold_points = []
    with open(digitized_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            gold_points.append((float(row['temperature_K']), float(row['C_Omega_kB'])))
    gold_points.sort(key=lambda x: x[0])

    def interpolate(t):
        if t <= gold_points[0][0]:
            return gold_points[0][1]
        if t >= gold_points[-1][0]:
            return gold_points[-1][1]
        for i in range(len(gold_points) - 1):
            if gold_points[i][0] <= t <= gold_points[i+1][0]:
                t0, v0 = gold_points[i]
                t1, v1 = gold_points[i+1]
                return v0 + (v1 - v0) * (t - t0) / (t1 - t0)
        return gold_points[-1][1]

    rows = artifact
    if not rows:
        return 0.0
    rel_errors = []
    for r in rows:
        T = float(r['temperature_K'])
        C = float(r['C_Omega_kB'])
        expected = interpolate(T)
        rel_errors.append(abs(C - expected) / (abs(expected) + 1e-12))
    max_err = max(rel_errors)
    tol = 0.3
    if max_err <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (max_err - tol) / 0.5)


# === block: score_1 (check id='ca_mg_monotonic') ===
def score_1(artifact, step, ctx):
    rows = artifact
    # Sort by temperature ascending
    sorted_rows = sorted(rows, key=lambda r: float(r['temperature_K']))
    C = [float(r['C_Omega_kB']) for r in sorted_rows]
    if len(C) < 2:
        return 0.0
    diffs = [C[i+1] - C[i] for i in range(len(C)-1)]
    # Should be non-positive (decreasing) with tolerance for numerical noise
    if all(d <= 1e-6 for d in diffs):
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='ca_mg_omega_alpha') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    def vol_gold(T):
        return 39.5 + 0.002 * (T - 780.0)
    # We'll compute alpha gold as finite difference for same T set, but we just check volume and reported alpha.
    vol_errs = []
    alpha_errs = []
    for r in rows:
        T = float(r['temperature_K'])
        v_exp = vol_gold(T)
        v_report = float(r['atomic_volume_A3'])
        vol_errs.append(abs(v_report - v_exp) / (abs(v_exp) + 1e-12))
        # Gold alpha: use finite difference from gold volumes at nearest neighbours? 
        # For simplicity, compute alpha_gold as 0.002 / v_exp (since slope 0.002)
        # Actually alpha = dvol/dT/vol, slope is 0.002, so alpha = 0.002 / v_exp
        a_exp = 0.002 / v_exp
        a_report = float(r['alpha_p_K-1'])
        alpha_errs.append(abs(a_report - a_exp) / (abs(a_exp) + 1e-12))
    max_vol = max(vol_errs) if vol_errs else 0.0
    max_alpha = max(alpha_errs) if alpha_errs else 0.0
    tol = 0.3
    score_v = 1.0 if max_vol <= tol else max(0.0, 1.0 - (max_vol - tol) / 0.5)
    score_a = 1.0 if max_alpha <= tol else max(0.0, 1.0 - (max_alpha - tol) / 0.5)
    return 0.5 * score_v + 0.5 * score_a


# === block: score_3 (check id='na_numeric') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    def C_gold_na(T):
        if T <= 200:
            return 4.2 + (3.0 - 4.2) / (200 - 140) * (T - 140)
        elif T <= 250:
            return 3.0 + (3.2 - 3.0) / (250 - 200) * (T - 200)
        else:
            return 4.0 + (3.5 - 4.0) / (312 - 250) * (T - 250)
    rel_errors = []
    for r in rows:
        T = float(r['temperature_K'])
        C = float(r['C_Omega_kB'])
        expected = C_gold_na(T)
        rel_errors.append(abs(C - expected) / (abs(expected) + 1e-12))
    max_err = max(rel_errors)
    tol = 0.3
    if max_err <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (max_err - tol) / 0.5)


# === block: score_4 (check id='na_nonmonotonic') ===
def score_4(artifact, step, ctx):
    rows = artifact
    sorted_rows = sorted(rows, key=lambda r: float(r['temperature_K']))
    C = [float(r['C_Omega_kB']) for r in sorted_rows]
    n = len(C)
    if n < 3:
        return 0.0
    diffs = [C[i+1] - C[i] for i in range(n-1)]
    # non-monotonic if at least one positive and at least one negative
    pos = any(d > 1e-6 for d in diffs)
    neg = any(d < -1e-6 for d in diffs)
    score = 1.0 if pos and neg else 0.0
    # Extra check: the pattern should not be purely noise; require minimum variation
    if (max(C) - min(C)) < 0.01:
        score = 0.0
    return score


# === block: score_5 (check id='na_omega_alpha') ===
def score_5(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    def vol_gold_na(T):
        if T <= 250:
            return 38.2 + 0.008 * (T - 140)
        else:
            return 39.0 + 0.016 * (T - 250)
    vol_errs = []
    alpha_errs = []
    for r in rows:
        T = float(r['temperature_K'])
        v_exp = vol_gold_na(T)
        v_report = float(r['atomic_volume_A3'])
        vol_errs.append(abs(v_report - v_exp) / (abs(v_exp) + 1e-12))
        # slope: below 250 slope=0.008, above slope=0.016
        slope = 0.008 if T <= 250 else 0.016
        a_exp = slope / v_exp
        a_report = float(r['alpha_p_K-1'])
        alpha_errs.append(abs(a_report - a_exp) / (abs(a_exp) + 1e-12))
    max_vol = max(vol_errs) if vol_errs else 0.0
    max_alpha = max(alpha_errs) if alpha_errs else 0.0
    tol = 0.3
    score_v = 1.0 if max_vol <= tol else max(0.0, 1.0 - (max_vol - tol) / 0.5)
    score_a = 1.0 if max_alpha <= tol else max(0.0, 1.0 - (max_alpha - tol) / 0.5)
    return 0.5 * score_v + 0.5 * score_a


_SCORERS = {
    'ca_mg_numeric': score_0,
    'ca_mg_monotonic': score_1,
    'ca_mg_omega_alpha': score_2,
    'na_numeric': score_3,
    'na_nonmonotonic': score_4,
    'na_omega_alpha': score_5,
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
