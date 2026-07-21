import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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


# === block: score_0 (check id='step_03_transport_t300') ===
def score_0(artifact, step, ctx):
    def find_closest_row(rows, key_col, target):
        best = None
        best_diff = float('inf')
        for row in rows:
            v = float(row.get(key_col, 0))
            diff = abs(v - target)
            if diff < best_diff:
                best_diff = diff
                best = row
        return best

    transport_rows = artifact  # list of dicts, already validated
    zt_path = os.path.join('/app/outputs', 'temperature_dependence_ZT.csv')
    if not os.path.exists(zt_path):
        return 0.0
    with open(zt_path, newline='') as f:
        zt_rows = list(csv.DictReader(f))
    target_T = step.get('parameters', {}).get('T_K', 300)
    row_T = None
    for row in zt_rows:
        if str(row.get('T_K', '')).strip() == str(target_T):
            row_T = row
            break
    if row_T is None:
        return 0.0
    n_H = float(step.get('parameters', {}).get('doping_n_H', 6.5e18))
    n_W = float(step.get('parameters', {}).get('doping_n_W', 7.1e18))
    kappa_ph_H = float(step.get('parameters', {}).get('kappa_ph_H', 10.1))
    kappa_ph_W = float(step.get('parameters', {}).get('kappa_ph_W', 8.3))
    tol_rel = float(step.get('parameters', {}).get('zt_tolerance_rel', 1e-5))
    row_H = find_closest_row(transport_rows, 'n_cm3', n_H)
    row_W = find_closest_row(transport_rows, 'n_cm3', n_W)
    if row_H is None or row_W is None:
        return 0.0
    def compute_ZT(S_uVK, sigma_Sm, kappa_e_WmK, kappa_ph, T):
        S_VK = float(S_uVK) * 1e-6
        sigma = float(sigma_Sm)
        PF = (S_VK ** 2) * sigma
        kappa_total = float(kappa_e_WmK) + kappa_ph
        return (PF * T) / kappa_total
    ZT_H_calc = compute_ZT(row_H['S_H_uVK'], row_H['sigma_H_Sm'], row_H['kappa_e_H_WmK'], kappa_ph_H, target_T)
    ZT_W_calc = compute_ZT(row_W['S_W_uVK'], row_W['sigma_W_Sm'], row_W['kappa_e_W_WmK'], kappa_ph_W, target_T)
    ZT_H_ref = float(row_T['ZT_H'])
    ZT_W_ref = float(row_T['ZT_W'])
    ok_H = abs(ZT_H_calc - ZT_H_ref) / (ZT_H_ref + 1e-12) < tol_rel
    ok_W = abs(ZT_W_calc - ZT_W_ref) / (ZT_W_ref + 1e-12) < tol_rel
    return 1.0 if (ok_H and ok_W) else 0.0


# === block: score_1 (check id='step_05_zt_and_phase_comparison') ===
def score_1(artifact, step, ctx):
    params = step.get('parameters', {})
    gold_300 = float(params.get('gold_ratio_300K', 1.1))
    gold_1000 = float(params.get('gold_ratio_1000K', 1.18))
    tol_rel = float(params.get('tolerance_relative', 0.10))
    min_ratio = float(params.get('ratio_threshold_min', 1.0))
    rows = artifact
    targets = {300: gold_300, 1000: gold_1000}
    ratio_scores = []
    for row in rows:
        T_key = int(float(row.get('T_K', 0)))
        if T_key in targets:
            ratio = float(row.get('ratio_ZT_HW', 0))
            gold = targets[T_key]
            if abs(ratio - gold) / (gold + 1e-12) <= tol_rel:
                ratio_scores.append(1.0)
            else:
                ratio_scores.append(0.0)
    if len(ratio_scores) < 2:
        ratio_score = 0.0
    else:
        ratio_score = sum(ratio_scores) / len(ratio_scores)
    points = []
    for row in rows:
        T = float(row.get('T_K', 0))
        r = float(row.get('ratio_ZT_HW', 0))
        points.append((T, r))
    points.sort(key=lambda x: x[0])
    if not points:
        trend_score = 0.0
    else:
        all_above_one = all(r > min_ratio for _, r in points)
        diffs = [points[i+1][1] - points[i][1] for i in range(len(points)-1)]
        if len(diffs) < 2:
            trend_correct = False
        else:
            # find index where diff sign changes from non-positive to non-negative
            p = None
            for i, d in enumerate(diffs):
                if d < -1e-9:
                    continue
                # first non-negative after a negative?
                if any(dd < -1e-9 for dd in diffs[:i]):
                    p = i
                    break
            if p is None:
                trend_correct = False
            else:
                # before p: all diffs <= 1e-9, after p: all >= -1e-9
                before = all(d <= 1e-9 for d in diffs[:p])
                after = all(d >= -1e-9 for d in diffs[p:])
                trend_correct = before and after
        trend_score = 1.0 if (all_above_one and trend_correct) else 0.0
    total = 0.7 * ratio_score + 0.3 * trend_score
    return total


_SCORERS = {
    'step_03_transport_t300': score_0,
    'step_05_zt_and_phase_comparison': score_1,
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
