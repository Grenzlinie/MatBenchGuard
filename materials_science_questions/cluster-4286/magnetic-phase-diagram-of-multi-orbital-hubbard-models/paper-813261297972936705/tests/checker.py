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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import math

    c1_list, U_met, U_imp = [], [], []
    for row in artifact:
        c1_list.append(float(row['c1']))
        U_met.append(float(row['U_metropolis']))
        U_imp.append(float(row['U_improved']))
    paired = sorted(zip(c1_list, U_imp, U_met), key=lambda x: x[0])
    c1_vals = [p[0] for p in paired]
    U_imp_vals = [p[1] for p in paired]
    U_met_vals = [p[2] for p in paired]

    # differences
    diffs = [U_imp_vals[i+1] - U_imp_vals[i] for i in range(len(U_imp_vals)-1)]
    # find index of max absolute difference
    max_diff = -1.0
    max_idx = 0
    for i, d in enumerate(diffs):
        ad = abs(d)
        if ad > max_diff:
            max_diff = ad
            max_idx = i

    c1_left = c1_vals[max_idx]
    c1_right = c1_vals[max_idx+1]
    crit = (c1_left + c1_right) / 2.0

    if 8.20 <= crit <= 8.35:
        crit_score = 1.0
    elif 8.15 <= crit <= 8.40:
        crit_score = 0.5
    else:
        crit_score = 0.0

    def find_crossing(x_vals, y_vals, threshold):
        for i in range(len(y_vals)-1):
            if (y_vals[i] < threshold <= y_vals[i+1]) or (y_vals[i] > threshold >= y_vals[i+1]):
                frac = (threshold - y_vals[i]) / (y_vals[i+1] - y_vals[i])
                return x_vals[i] + frac * (x_vals[i+1] - x_vals[i])
        return None

    left_imp = U_imp_vals[:max_idx+1]
    right_imp = U_imp_vals[max_idx+1:]
    U_low = sum(left_imp) / len(left_imp)
    U_high = sum(right_imp) / len(right_imp)
    delta = U_high - U_low

    c10 = find_crossing(c1_vals, U_imp_vals, U_low + 0.1 * delta)
    c90 = find_crossing(c1_vals, U_imp_vals, U_low + 0.9 * delta)
    if c10 is not None and c90 is not None:
        width_imp = abs(c90 - c10)
    else:
        width_imp = float('inf')
    imp_hyst_score = 1.0 if width_imp < 0.3 else 0.0

    left_met = U_met_vals[:max_idx+1]
    right_met = U_met_vals[max_idx+1:]
    U_low_met = sum(left_met) / len(left_met)
    U_high_met = sum(right_met) / len(right_met)
    delta_met = U_high_met - U_low_met
    c10_met = find_crossing(c1_vals, U_met_vals, U_low_met + 0.1 * delta_met)
    c90_met = find_crossing(c1_vals, U_met_vals, U_low_met + 0.9 * delta_met)
    if c10_met is not None and c90_met is not None:
        width_met = abs(c90_met - c10_met)
    else:
        width_met = 0.0
    met_hyst_score = 1.0 if width_met > 0.5 else 0.0

    return 0.5 * crit_score + 0.25 * imp_hyst_score + 0.25 * met_hyst_score


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    phases = artifact
    score = 0.0
    low_ok = (str(phases.get('low_c1_phase','')).strip() == 'AF')
    high_ok = (str(phases.get('high_c1_phase','')).strip() == 'FM+SF')
    if low_ok:
        score += 0.25
    if high_ok:
        score += 0.25

    crit_range = phases.get('critical_c1_range', [])
    if isinstance(crit_range, list) and len(crit_range) == 2:
        a, b = float(crit_range[0]), float(crit_range[1])
        width = abs(b - a)
        if width > 0.5:
            crit_score = 0.0
        else:
            if (a <= 8.30 and b >= 8.25):
                crit_score = 0.5
            else:
                crit_score = 0.0
    else:
        crit_score = 0.0
    score += crit_score
    return score


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
