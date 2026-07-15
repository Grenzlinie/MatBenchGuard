import os
import json
import csv

# === author imports / helpers ===
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


# === block: score_0 (check id='caloric_structural') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    # Sort by temperature
    try:
        rows_sorted = sorted(rows, key=lambda r: float(r['temperature (K)'])
    )
    except (KeyError, ValueError):
        return 0.0

    if len(rows_sorted) < 2:
        return 0.0

    # Compute slopes
    slopes = []
    for i in range(1, len(rows_sorted)):
        T1 = float(rows_sorted[i-1]['temperature (K)'])
        T2 = float(rows_sorted[i]['temperature (K)'])
        dT = T2 - T1
        if dT <= 0:
            continue
        E1 = float(rows_sorted[i-1]['avg_potential_energy (kcal/mol)'])
        E2 = float(rows_sorted[i]['avg_potential_energy (kcal/mol)'])
        slope = (E2 - E1) / dT
        mid = (T1 + T2) / 2.0
        slopes.append((mid, slope))
    if not slopes:
        return 0.0

    # Find max slope midpoint
    max_slope_mid = max(slopes, key=lambda x: x[1])[0]

    # Energy increase: find closest temperatures to 150 and 350
    T_all = [float(r['temperature (K)']) for r in rows_sorted]
    E_all = [float(r['avg_potential_energy (kcal/mol)']) for r in rows_sorted]
    def find_val(target, temps, values):
        best = None
        best_dist = float('inf')
        for t, v in zip(temps, values):
            dist = abs(t - target)
            if dist < best_dist:
                best_dist = dist
                best = v
        return best
    E150 = find_val(150.0, T_all, E_all)
    E350 = find_val(350.0, T_all, E_all)
    if E150 is None or E350 is None:
        energy_inc = 0.0
    else:
        energy_inc = E350 - E150

    melt_range = step['target']['melting_temp_range']
    min_inc = step['target']['energy_increase_min']
    cond1 = melt_range[0] <= max_slope_mid <= melt_range[1]
    cond2 = energy_inc > min_inc

    if cond1 and cond2:
        return 1.0
    elif cond1 or cond2:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='radial_structural') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0

    # Group by temperature
    data_by_temp = {}
    try:
        for r in rows:
            T = float(r['temperature (K)'])
            radius = float(r['radius (Angstrom)'])
            density = float(r['ion_density (arbitrary units)'])
            data_by_temp.setdefault(T, []).append((radius, density))
    except (KeyError, ValueError):
        return 0.0

    target = step['target']
    low_T = target['low_T']
    high_T = target['high_T']
    def find_peak_radius(temp, data):
        best_r, best_d = None, -1
        for r, d in data:
            if d > best_d:
                best_d = d
                best_r = r
        return best_r

    score = 0.0
    low_ok = False
    if low_T in data_by_temp:
        peak_low = find_peak_radius(low_T, data_by_temp[low_T])
        if peak_low is not None and peak_low > target['low_peak_radius_min']:
            low_ok = True

    high_ok = False
    if high_T in data_by_temp:
        peak_high = find_peak_radius(high_T, data_by_temp[high_T])
        if peak_high is not None and peak_high < target['high_peak_radius_max']:
            high_ok = True

    if low_ok and high_ok:
        score = 1.0
    elif low_ok or high_ok:
        score = 0.5
    else:
        score = 0.0
    return score


_SCORERS = {
    'caloric_structural': score_0,
    'radial_structural': score_1,
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
