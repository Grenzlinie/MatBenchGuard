import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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
    return {'spec': spec}


# === block: score_0 (check id='properties') ===
def score_0(artifact, step, ctx):
    import csv

    rows = artifact
    config = step.get('config', {})
    gold_dict = config['gold']
    tolerances = config['tolerances']

    # Build lookup by alloy name
    data = {}
    for row in rows:
        name = row.get('alloy', '').strip()
        if name:
            data[name] = row

    quantity_keys = [k for k in tolerances.keys() if k != 'cauchy_pressure_C12_minus_C44']
    total_checks = 0
    hits = 0

    for alloy, gold in gold_dict.items():
        if alloy not in data:
            continue  # skip missing alloy
        row = data[alloy]
        for key in quantity_keys:
            try:
                val = float(row.get(key, 0.0))
            except (ValueError, TypeError):
                continue
            gold_val = gold[key]
            tol = tolerances[key]
            denom = max(abs(gold_val), 1e-6)
            if abs(val - gold_val) / denom <= tol:
                hits += 1
            total_checks += 1
        # Cauchy pressure uses absolute tolerance
        key = 'cauchy_pressure_C12_minus_C44'
        try:
            val = float(row.get(key, 0.0))
            gold_val = gold[key]
            tol = tolerances[key]
            if abs(val - gold_val) <= tol:
                hits += 1
            total_checks += 1
        except:
            continue

    value_score = hits / max(total_checks, 1)

    # Trend checks
    def is_monotonic_increasing(vals):
        return all(vals[i] <= vals[i+1] for i in range(len(vals)-1))

    trend_hits = 0.0
    trend_total = 0.0
    for trend_group in [config.get('trend_period4', []), config.get('trend_period5', [])]:
        if len(trend_group) < 2:
            continue
        bg_vals = []
        cp_vals = []
        for alloy in trend_group:
            if alloy in data:
                try:
                    bg_vals.append(float(data[alloy]['B_G_ratio']))
                except:
                    pass
                try:
                    cp_vals.append(float(data[alloy]['cauchy_pressure_C12_minus_C44']))
                except:
                    pass
        if bg_vals:
            trend_hits += 1.0 if is_monotonic_increasing(bg_vals) else 0.0
            trend_total += 1.0
        if cp_vals:
            trend_hits += 1.0 if is_monotonic_increasing(cp_vals) else 0.0
            trend_total += 1.0

    trend_score = trend_hits / max(trend_total, 1.0)

    # Weights
    w_value = 0.8
    w_trend = 0.2
    return w_value * value_score + w_trend * trend_score


# === block: score_1 (check id='dos') ===
def score_1(artifact, step, ctx):
    rows = artifact
    config = step.get('config', {})
    window = config.get('pseudo_gap_range_eV', 1.0)

    # Group data by alloy
    from collections import defaultdict
    alloy_data = defaultdict(list)
    for r in rows:
        alloy = r.get('alloy', '').strip()
        try:
            e = float(r['energy_eV'])
            td = float(r['total_DOS'])
        except:
            continue
        if alloy:
            alloy_data[alloy].append((e, td))

    # Check pseudo-gap existence per alloy
    def has_pseudo_gap(points):
        # points list of (e, dos)
        points = sorted(points, key=lambda x: x[0])
        subset = [(e,d) for e,d in points if -window <= e <= window]
        if len(subset) < 5:
            return False
        energies = [p[0] for p in subset]
        dos_vals = [p[1] for p in subset]
        min_idx = int(np.argmin(dos_vals))
        # compute mean over the window
        mean_dos = np.mean(dos_vals)
        if mean_dos < 1e-9:
            return False
        # depth check: min should be notably lower
        return dos_vals[min_idx] < 0.7 * mean_dos

    gap_found = 0
    for alloy in config.get('alloys_order', []):
        pts = alloy_data.get(alloy, [])
        if has_pseudo_gap(pts):
            gap_found += 1

    pseudo_score = gap_found / max(1, len(config.get('alloys_order', [])))

    # Fermi level shift: compute pseudo-gap position for trend groups
    def pseudo_gap_position(points):
        points = sorted(points, key=lambda x: x[0])
        subset = [(e,d) for e,d in points if -window <= e <= window]
        if not subset:
            return None
        energies = [p[0] for p in subset]
        dos_vals = [p[1] for p in subset]
        min_idx = int(np.argmin(dos_vals))
        return energies[min_idx]

    shift_hits = 0.0
    shift_total = 0.0
    for trend_key, trend_alloys in [('period4_shift', config.get('period4_shift', [])), 
                                     ('period5_shift', config.get('period5_shift', []))]:
        if len(trend_alloys) < 2:
            continue
        positions = []
        for alloy in trend_alloys:
            pts = alloy_data.get(alloy, [])
            pos = pseudo_gap_position(pts)
            if pos is not None:
                positions.append(pos)
        if len(positions) >= 2:
            # check decreasing (more negative)
            if all(positions[i] >= positions[i+1] for i in range(len(positions)-1)):
                shift_hits += 1.0
            shift_total += 1.0

    shift_score = shift_hits / max(shift_total, 1.0)

    # combine
    return 0.5 * pseudo_score + 0.5 * shift_score


# === block: score_2 (check id='charge') ===
def score_2(artifact, step, ctx):
    data = artifact
    config = step.get('config', {})
    order = config['expected_decreasing_order']

    # For each alloy, extract charge density at midpoint (a/4, a/4)
    mid_densities = []
    for alloy in order:
        if alloy not in data:
            mid_densities.append(0.0)
            continue
        obj = data[alloy]
        xs = obj.get('x_grid', [])
        ys = obj.get('y_grid', [])
        dens = obj.get('density', [])
        if not xs or not ys or not dens:
            mid_densities.append(0.0)
            continue
        L = max(xs)
        mid = L / 4.0
        # find nearest index
        i = int(np.argmin(np.abs(np.array(xs) - mid)))
        j = int(np.argmin(np.abs(np.array(ys) - mid)))
        # density is 2D list with density[i][j]? The contract says density[i][j] corresponds to (x_grid[i], y_grid[j]).
        try:
            val = dens[i][j]
        except (IndexError, TypeError):
            val = 0.0
        mid_densities.append(val)

    # Check monotonic non-increasing
    if len(mid_densities) < 2:
        return 0.0
    non_increasing = all(mid_densities[i] >= mid_densities[i+1] for i in range(len(mid_densities)-1))
    return 1.0 if non_increasing else 0.0


_SCORERS = {
    'properties': score_0,
    'dos': score_1,
    'charge': score_2,
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
