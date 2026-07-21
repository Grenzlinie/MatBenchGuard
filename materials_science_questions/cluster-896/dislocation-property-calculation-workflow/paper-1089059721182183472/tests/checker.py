import os
import json
import csv

# === author imports / helpers ===
import math

def compute_max_min_avg(rows, key_angle, key_strain):
    if not rows:
        return (0.0, 0.0)
    strains = [r[key_strain] for r in rows]
    max_idx = max(range(len(strains)), key=lambda i: strains[i])
    min_idx = min(range(len(strains)), key=lambda i: strains[i])
    max_angle = rows[max_idx][key_angle]
    min_angle = rows[min_idx][key_angle]
    window = math.pi / 8.0
    max_vals = []
    for r in rows:
        diff = abs(r[key_angle] - max_angle)
        diff = min(diff, 2.0 * math.pi - diff)
        if diff <= window:
            max_vals.append(r[key_strain])
    min_vals = []
    for r in rows:
        diff = abs(r[key_angle] - min_angle)
        diff = min(diff, 2.0 * math.pi - diff)
        if diff <= window:
            min_vals.append(r[key_strain])
    if not max_vals or not min_vals:
        return (0.0, 0.0)
    return (sum(max_vals) / len(max_vals), sum(min_vals) / len(min_vals))


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


# === block: score_0 (check id='step_02_structure') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if rows is None:
        return 0.0
    req_cols = step.get("required_columns", [])
    if not all(col in rows[0] for col in req_cols):
        return 0.0
    times = set()
    for r in rows:
        try:
            times.add(float(r["time"]))
        except (ValueError, KeyError):
            pass
    expected_times = set(step.get("expected_times", []))
    if not expected_times.issubset(times):
        return 0.0
    if len(rows) < step.get("min_rows", 360):
        return 0.0
    return 1.0


# === block: score_1 (check id='step_02_theoretical_sign') ===
def score_1(artifact, step, ctx):
    import csv, os

    rows = artifact
    if not rows:
        return 0.0

    # group strain profiles by time
    from collections import defaultdict
    groups = defaultdict(list)
    for r in rows:
        try:
            t = float(r["time"])
            groups[t].append(r)
        except (ValueError, KeyError):
            pass

    # check sign of theoretical strain for each time
    for t, group in groups.items():
        max_avg, min_avg = compute_max_min_avg(group, "angle", "theoretical_eps111")
        if max_avg <= 0.0 or min_avg >= 0.0:
            return 0.0

    # cross-validate against max_min_values.csv
    max_min_path = '/app/outputs/max_min_values.csv'
    try:
        with open(max_min_path, newline='') as f:
            reader = csv.DictReader(f)
            max_min_rows = [row for row in reader]
    except Exception:
        return 0.0

    if not max_min_rows:
        return 0.0

    eps_abs = 1e-10
    rel_tol = 1e-5

    def close(a, b):
        if abs(a) < 1e-12 and abs(b) < 1e-12:
            return abs(a - b) < eps_abs
        return abs(a - b) / max(abs(a), abs(b)) < rel_tol

    for row in max_min_rows:
        try:
            t = float(row['time'])
            max_th = float(row['max_theoretical'])
            min_th = float(row['min_theoretical'])
        except (ValueError, KeyError):
            return 0.0

        group = groups.get(t)
        if group is None:
            return 0.0

        max_th_calc, min_th_calc = compute_max_min_avg(group, 'angle', 'theoretical_eps111')
        if not (close(max_th_calc, max_th) and close(min_th_calc, min_th)):
            return 0.0

    return 1.0


# === block: score_2 (check id='step_02_experimental_reduction') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    from collections import defaultdict
    groups = defaultdict(list)
    for r in rows:
        t = float(r["time"])
        groups[t].append(r)
    if -3.4 not in groups or 3.9 not in groups:
        return 0.0
    max_init, _ = compute_max_min_avg(groups[-3.4], "angle", "experimental_eps111")
    max_final, _ = compute_max_min_avg(groups[3.9], "angle", "experimental_eps111")
    if abs(max_init) < 1e-12:
        return 0.0
    reduction = (max_init - max_final) / abs(max_init)
    ref_min = step.get("reference_reduction_min", 0.25)
    ref_max = step.get("reference_reduction_max", 0.45)
    if ref_min <= reduction <= ref_max:
        return 1.0
    # partial credit: closer to range, up to 0.5
    if reduction < ref_min:
        if reduction < 0.0:
            return 0.0
        return max(0.0, 0.5 * (reduction / ref_min))
    else:
        # reduction > ref_max, cap at 0.5 if not too far
        return max(0.0, 0.5 * (ref_max / reduction)) if reduction < 1.0 else 0.0


# === block: score_3 (check id='step_02_experimental_min_reduction') ===
def score_3(artifact, step, ctx):
    rows = artifact  # strain_profiles.csv rows
    if not rows:
        return 0.0

    # Load max_min_values.csv for cross-validation
    import csv, os
    max_min_path = '/app/outputs/max_min_values.csv'
    try:
        with open(max_min_path, newline='') as f:
            reader = csv.DictReader(f)
            max_min_rows = [row for row in reader]
    except Exception:
        return 0.0
    if not max_min_rows:
        return 0.0

    from collections import defaultdict
    groups = defaultdict(list)
    for r in rows:
        try:
            t = float(r["time"])
            groups[t].append(r)
        except (ValueError, KeyError):
            pass

    eps_abs = 1e-10
    rel_tol = 1e-5
    def close(a, b):
        if abs(a) < 1e-12 and abs(b) < 1e-12:
            return abs(a - b) < eps_abs
        return abs(a - b) / max(abs(a), abs(b)) < rel_tol

    for row in max_min_rows:
        try:
            t = float(row['time'])
            max_th = float(row['max_theoretical'])
            min_th = float(row['min_theoretical'])
            max_exp = float(row['max_experimental'])
            min_exp = float(row['min_experimental'])
        except (ValueError, KeyError):
            return 0.0
        strain_group = groups.get(t)
        if strain_group is None:
            return 0.0
        max_th_calc, min_th_calc = compute_max_min_avg(strain_group, 'angle', 'theoretical_eps111')
        max_exp_calc, min_exp_calc = compute_max_min_avg(strain_group, 'angle', 'experimental_eps111')
        if not (close(max_th_calc, max_th) and close(min_th_calc, min_th) and
                close(max_exp_calc, max_exp) and close(min_exp_calc, min_exp)):
            return 0.0

    # Experimental min reduction check
    if -3.4 not in groups or 3.9 not in groups:
        return 0.0
    _, min_init = compute_max_min_avg(groups[-3.4], "angle", "experimental_eps111")
    _, min_final = compute_max_min_avg(groups[3.9], "angle", "experimental_eps111")
    if abs(min_init) < 1e-12:
        return 0.0
    reduction = (abs(min_init) - abs(min_final)) / abs(min_init)
    ref_min = step.get("reference_reduction_min", 0.25)
    ref_max = step.get("reference_reduction_max", 0.45)
    if ref_min <= reduction <= ref_max:
        return 1.0
    if reduction < ref_min:
        if reduction < 0.0:
            return 0.0
        return max(0.0, 0.5 * (reduction / ref_min))
    else:
        return max(0.0, 0.5 * (ref_max / reduction)) if reduction < 1.0 else 0.0


# === block: score_4 (check id='step_03_consistency') ===
def score_4(artifact, step, ctx):
    import os, csv

    profile_path = '/app/outputs/strain_profiles.csv'
    try:
        with open(profile_path, newline='') as f:
            reader = csv.DictReader(f)
            profiles = [row for row in reader]
    except Exception:
        return 0.0

    if not profiles:
        return 0.0

    from collections import defaultdict
    groups = defaultdict(list)
    for r in profiles:
        try:
            t = float(r['time'])
            groups[t].append(r)
        except (ValueError, KeyError):
            pass

    csv_rows = artifact  # max_min_values.csv rows
    if not csv_rows:
        return 0.0

    eps_abs = 1e-10
    rel_tol = 1e-5

    def close(a, b):
        if abs(a) < 1e-12 and abs(b) < 1e-12:
            return abs(a - b) < eps_abs
        return abs(a - b) / max(abs(a), abs(b)) < rel_tol

    for row in csv_rows:
        try:
            t = float(row['time'])
            max_th = float(row['max_theoretical'])
            min_th = float(row['min_theoretical'])
            max_exp = float(row['max_experimental'])
            min_exp = float(row['min_experimental'])
        except (ValueError, KeyError):
            return 0.0

        strain_group = groups.get(t)
        if strain_group is None:
            return 0.0

        max_th_calc, min_th_calc = compute_max_min_avg(strain_group, 'angle', 'theoretical_eps111')
        max_exp_calc, min_exp_calc = compute_max_min_avg(strain_group, 'angle', 'experimental_eps111')

        if not (close(max_th_calc, max_th) and close(min_th_calc, min_th) and
                close(max_exp_calc, max_exp) and close(min_exp_calc, min_exp)):
            return 0.0

    return 1.0


# === block: score_5 (check id='step_03_theoretical_bounds') ===
def score_5(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    gold_max = step.get("gold_max_theoretical", 1.80e-4)
    gold_min = step.get("gold_min_theoretical", -1.80e-4)
    tol = step.get("tolerance_relative", 0.25)
    for r in rows:
        try:
            max_th = float(r["max_theoretical"])
            min_th = float(r["min_theoretical"])
            if max_th <= 0.0 or min_th >= 0.0:
                return 0.0
            if abs(max_th - gold_max) > tol * abs(gold_max):
                return 0.0
            if abs(min_th - gold_min) > tol * abs(gold_min):
                return 0.0
        except (ValueError, KeyError):
            return 0.0
    return 1.0


_SCORERS = {
    'step_02_structure': score_0,
    'step_02_theoretical_sign': score_1,
    'step_02_experimental_reduction': score_2,
    'step_02_experimental_min_reduction': score_3,
    'step_03_consistency': score_4,
    'step_03_theoretical_bounds': score_5,
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
