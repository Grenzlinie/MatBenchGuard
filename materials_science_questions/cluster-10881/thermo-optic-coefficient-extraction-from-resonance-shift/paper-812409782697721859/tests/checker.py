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


# === block: score_0 (check id='step_baseline') ===
def score_0(artifact, step, ctx):
    rows = artifact
    gold = step.get("gold_peak_loss", {})
    tol_pct = step.get("peak_loss_tolerance_pct", 5.0)
    tol_abs = step.get("peak_loss_tolerance_abs", 1.0)
    wl_range = step.get("res_wl_range", [500.0, 800.0])
    peak_scores = 0
    wl_in_range = True
    temps_ordered = []
    for r in rows:
        tk = float(r["temperature_K"])
        if tk in (270.0, 320.0, 370.0):
            gold_val = gold.get(str(int(tk)))
            if gold_val is not None:
                val = float(r["peak_loss_dB_per_cm"])
                diff = abs(val - gold_val)
                if diff <= max(gold_val * tol_pct / 100.0, tol_abs):
                    peak_scores += 1
            wl = float(r["resonance_wavelength_nm"])
            if not (wl_range[0] <= wl <= wl_range[1]):
                wl_in_range = False
            temps_ordered.append((tk, wl))
    wl_increasing = True
    if len(temps_ordered) == 3:
        temps_ordered.sort()
        wls = [w for _, w in temps_ordered]
        if not (wls[0] < wls[1] < wls[2]):
            wl_increasing = False
    score = (peak_scores / 3.0) * 0.7 + (0.15 if wl_in_range else 0) + (0.15 if wl_increasing else 0)
    return min(max(score, 0.0), 1.0)


# === block: score_1 (check id='step_ri_dependence') ===
def score_1(artifact, step, ctx):
    rows = artifact
    gold_slopes = step.get("gold_slopes", {})
    tol_pct = step.get("slope_tolerance_pct", 10.0)
    tol_abs = step.get("slope_tolerance_abs", 0.02)
    temp_slopes = {}
    for r in rows:
        t = float(r["temperature_K"])
        ri = float(r["ri"])
        loss = float(r["peak_loss_dB_per_cm"])
        temp_slopes.setdefault(t, []).append((ri, loss))
    scores = []
    for t, points in temp_slopes.items():
        if len(points) < 2:
            continue
        points.sort()
        n = len(points)
        sum_x = sum(p[0] for p in points)
        sum_y = sum(p[1] for p in points)
        sum_xy = sum(p[0]*p[1] for p in points)
        sum_xx = sum(p[0]**2 for p in points)
        slope = (n*sum_xy - sum_x*sum_y) / (n*sum_xx - sum_x**2)
        gold_slope = gold_slopes.get(str(int(t)))
        if gold_slope is None:
            continue
        diff = abs(slope - gold_slope)
        tol = max(abs(gold_slope) * tol_pct / 100.0, tol_abs)
        if diff <= tol:
            scores.append(1.0)
        else:
            rel_err = (diff - tol) / abs(gold_slope)
            scores.append(max(0.0, 1.0 - rel_err))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='step_temp_dependence') ===
def score_2(artifact, step, ctx):
    rows = artifact
    temps = []
    losses = []
    for r in rows:
        temps.append(float(r["temperature_K"]))
        losses.append(float(r["peak_loss_dB_per_cm"]))
    if len(temps) < 2:
        return 0.0
    n = len(temps)
    sum_x = sum(temps)
    sum_y = sum(losses)
    sum_xy = sum(t*l for t,l in zip(temps, losses))
    sum_xx = sum(t*t for t in temps)
    slope = (n*sum_xy - sum_x*sum_y) / (n*sum_xx - sum_x*sum_x)
    intercept = (sum_y - slope*sum_x) / n
    ss_res = sum((l - (slope*t + intercept))**2 for t,l in zip(temps, losses))
    mean_y = sum_y/n
    ss_tot = sum((l - mean_y)**2 for l in losses)
    r_sq = 1 - ss_res/ss_tot if ss_tot > 0 else 0.0
    r2_thresh = step.get("r2_threshold", 0.95)
    slope_range = step.get("slope_range", [0.05, 0.25])
    r2_score = min(1.0, r_sq / r2_thresh) if r_sq > 0 else 0.0
    slope_ok = (slope <= 0) and (slope_range[0] <= abs(slope) <= slope_range[1])
    score = r2_score * 0.5 + (0.5 if slope_ok else 0.0)
    return min(max(score, 0.0), 1.0)


# === block: score_3 (check id='step_structural_variation') ===
def score_3(artifact, step, ctx):
    rows = artifact
    all_wl_by_temp = {}
    for r in rows:
        t = float(r["temperature_K"])
        wl = float(r["resonance_wavelength_nm"])
        all_wl_by_temp.setdefault(t, []).append(wl)
    max_allow = step.get("res_wl_variation_max_nm", 5.0)
    wl_score = 0.0
    temp_count = len(all_wl_by_temp)
    if temp_count > 0:
        for t, wls in all_wl_by_temp.items():
            rng = max(wls) - min(wls)
            wl_score += 1.0 if rng <= max_allow else max(0.0, 1.0 - (rng - max_allow)/max_allow)
        wl_score /= temp_count
    # ordering checks
    duty_rows = []
    lattice_rows = []
    for r in rows:
        if r["parameter"] == "duty_ratio":
            duty_rows.append(r)
        elif r["parameter"] == "lattice_pitch":
            lattice_rows.append(r)
    ordering_score = 0.0
    checks = 0
    # duty_ratio: 0.6 > 0.4
    by_temp = {}
    for r in duty_rows:
        t = float(r["temperature_K"])
        if t not in by_temp:
            by_temp[t] = {}
        by_temp[t][float(r["parameter_value"])] = float(r["peak_loss_dB_per_cm"])
    for t, val_dict in by_temp.items():
        if 0.6 in val_dict and 0.4 in val_dict:
            checks += 1
            if val_dict[0.6] > val_dict[0.4]:
                ordering_score += 1
    # lattice_pitch: 5 > 10
    by_temp2 = {}
    for r in lattice_rows:
        t = float(r["temperature_K"])
        if t not in by_temp2:
            by_temp2[t] = {}
        by_temp2[t][float(r["parameter_value"])] = float(r["peak_loss_dB_per_cm"])
    for t, val_dict in by_temp2.items():
        if 5.0 in val_dict and 10.0 in val_dict:
            checks += 1
            if val_dict[5.0] > val_dict[10.0]:
                ordering_score += 1
    ordering_score = ordering_score / checks if checks > 0 else 0.0
    return 0.5 * wl_score + 0.5 * ordering_score


_SCORERS = {
    'step_baseline': score_0,
    'step_ri_dependence': score_1,
    'step_temp_dependence': score_2,
    'step_structural_variation': score_3,
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
