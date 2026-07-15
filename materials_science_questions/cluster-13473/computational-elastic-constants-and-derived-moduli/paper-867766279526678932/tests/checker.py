import os
import json
import csv

# === author imports / helpers ===
import math, statistics


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


# === block: score_0 (check id='step_stress_strain') ===
def score_0(artifact, step, ctx):
    try:
        strains = [float(r['strain']) for r in artifact if 'strain' in r and 'stress' in r]
        stresses = [float(r['stress']) for r in artifact if 'strain' in r and 'stress' in r]
    except (ValueError, KeyError):
        return 0.0
    if len(strains) < 10:
        return 0.0
    # Find peak
    max_idx = max(range(len(stresses)), key=lambda i: stresses[i])
    peak_strain = strains[max_idx]
    peak_stress = stresses[max_idx]
    # Define plateau region: last 20% of points
    plateau_start_idx = int(0.8 * len(strains))
    if plateau_start_idx >= len(strains): plateau_start_idx = len(strains)-1
    plateau_mean = statistics.mean(stresses[plateau_start_idx:])
    # Sub-scores
    score = 0.0
    # 1. Peak existence (0.4): peak strain between 0.02 and 0.6, peak > plateau * 1.03
    if 0.02 <= peak_strain <= 0.6 and peak_stress > 1.03 * plateau_mean:
        score += 0.4
    # 2. Post-peak trend (0.3): after peak, stresses should not exceed peak * 1.02
    post_peak_stresses = stresses[max_idx+1:]
    if post_peak_stresses:
        if max(post_peak_stresses) <= 1.02 * peak_stress:
            score += 0.3
    else:
        score += 0.3  # no points after peak; treat as ok
    # 3. Plateau range (0.3): plateau_mean between 0.3 and 2.0
    if 0.3 <= plateau_mean <= 2.0:
        score += 0.3
    return min(score, 1.0)


# === block: score_1 (check id='step_mean_yield_stress') ===
def score_1(artifact, step, ctx):
    try:
        strains = [float(r['strain']) for r in artifact if 'strain' in r and 'mean_threshold' in r]
        thresholds = [float(r['mean_threshold']) for r in artifact if 'strain' in r and 'mean_threshold' in r]
    except (ValueError, KeyError):
        return 0.0
    if len(strains) < 10:
        return 0.0
    # Helper: simple linear slope over a specified strain range
    # Returns slope (if enough points) else None
    def slope_over_range(strains_list, thresholds_list, low_strain, high_strain):
        x = [s for s, t in zip(strains_list, thresholds_list) if low_strain <= s <= high_strain]
        y = [t for s, t in zip(strains_list, thresholds_list) if low_strain <= s <= high_strain]
        if len(x) < 3:
            return None
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xx = sum(xi*xi for xi in x)
        sum_xy = sum(xi*yi for xi, yi in zip(x, y))
        denom = n*sum_xx - sum_x*sum_x
        if abs(denom) < 1e-12:
            return None
        slope = (n*sum_xy - sum_x*sum_y) / denom
        return slope
    early_slope = slope_over_range(strains, thresholds, 0.0, 0.5)
    late_slope = slope_over_range(strains, thresholds, 3.0, 5.0)
    start_val = thresholds[0]
    end_val = thresholds[-1]
    max_idx = max(range(len(thresholds)), key=lambda i: thresholds[i])
    max_strain = strains[max_idx]
    max_val = thresholds[max_idx]
    score = 0.0
    # 1. initial increase then decrease (0.5): early slope > 0 and late slope < 0
    if early_slope is not None and late_slope is not None and early_slope > 0 and late_slope < 0:
        score += 0.5
    # 2. start > end (0.3): end_val < start_val * 0.995 (slight decrease)
    if end_val < start_val * 0.995:
        score += 0.3
    # 3. max occurs in strain range [0.05, 1.5] (0.2)
    if 0.05 <= max_strain <= 1.5:
        score += 0.2
    return min(score, 1.0)


# === block: score_2 (check id='step_localization_index') ===
def score_2(artifact, step, ctx):
    try:
        strains = [float(r['strain']) for r in artifact if 'strain' in r and 'LOC' in r]
        locs = [float(r['LOC']) for r in artifact if 'strain' in r and 'LOC' in r]
    except (ValueError, KeyError):
        return 0.0
    if len(strains) < 10:
        return 0.0
    max_idx = max(range(len(locs)), key=lambda i: locs[i])
    max_strain = strains[max_idx]
    max_loc = locs[max_idx]
    final_loc = locs[-1]
    score = 0.0
    # 1. peak strain between 0.1 and 2.0 (0.3)
    if 0.1 <= max_strain <= 2.0:
        score += 0.3
    # 2. final LOC < max LOC (0.3)
    if final_loc < max_loc:
        score += 0.3
    # 3. max LOC between 0.08 and 0.8 (0.4)
    if 0.08 <= max_loc <= 0.8:
        score += 0.4
    # additional sanity: all LOC between 0 and 1
    if any(l < 0 or l > 1 for l in locs):
        score = 0.0
    return min(score, 1.0)


_SCORERS = {
    'step_stress_strain': score_0,
    'step_mean_yield_stress': score_1,
    'step_localization_index': score_2,
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
