import os
import json
import csv

# === author imports / helpers ===
import math
import statistics

def find_nearest_row(rows, target_strain):
    # rows are pre-sorted; return row with strain nearest to target
    best = None
    best_diff = float('inf')
    for r in rows:
        diff = abs(float(r['strain']) - target_strain)
        if diff < best_diff:
            best_diff = diff
            best = r
    return best

def stress_at_strain(rows, target_strain):
    row = find_nearest_row(rows, target_strain)
    if row is None:
        raise ValueError(f"No strain near {target_strain}")
    return float(row['stress_MPa'])

def temp_at_strain(rows, target_strain):
    row = find_nearest_row(rows, target_strain)
    return float(row['temperature_K'])

def xiM_at_strain(rows, target_strain):
    row = find_nearest_row(rows, target_strain)
    return float(row['xi_M'])

def beta_at_strain(rows, target_strain):
    row = find_nearest_row(rows, target_strain)
    return float(row['beta'])

def stress_ratio(rows, strain_a, strain_b):
    s_a = stress_at_strain(rows, strain_a)
    s_b = stress_at_strain(rows, strain_b)
    if s_a == 0:
        return float('inf')
    return (s_b - s_a) / s_a

def max_relative_deviation(rows1, rows2, strain_col='strain', value_col='stress_MPa', eps=1e-12):
    strains1 = [float(r[strain_col]) for r in rows1]
    strains2 = [float(r[strain_col]) for r in rows2]
    def closest_index(strain, ref_strains):
        return min(range(len(ref_strains)), key=lambda i: abs(ref_strains[i] - strain))
    max_rel = 0.0
    for i, r1 in enumerate(rows1):
        j = closest_index(strains1[i], strains2)
        v1 = float(r1[value_col])
        v2 = float(rows2[j][value_col])
        denom = abs(v1) + abs(v2) + eps
        rel = abs(v1 - v2) / denom if denom > 0 else 0.0
        if rel > max_rel:
            max_rel = rel
    return max_rel


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


# === block: score_0 (check id='csv_structural') ===
def score_0(artifact, step, ctx):
    rows = artifact
    required_cases = step.get('required_cases', [])
    min_points = step.get('min_points_per_case', 200)
    checks = step.get('checks', [])
    check_map = {c['name']: c for c in checks}

    def score_check(name):
        return check_map.get(name, {}).get('weight', 0.0)

    # group by case
    groups = {}
    for row in rows:
        key = (row['orientation'], int(row['initial_temp_K']), row['thermal_boundary'])
        groups.setdefault(key, []).append(row)

    for k in groups:
        groups[k].sort(key=lambda r: float(r['strain']))

    total = 0.0

    # 1. case presence and point count
    presence_ok = True
    for case in required_cases:
        if case not in groups:
            presence_ok = False
            break
        if len(groups[case]) < min_points:
            presence_ok = False
            break
    if presence_ok:
        total += score_check('case_presence_and_points')

    # 2. strain coverage
    coverage_ok = True
    for case in required_cases:
        data = groups[case]
        strains = [float(r['strain']) for r in data]
        if not strains:
            coverage_ok = False
            break
        if min(strains) > 0.01 or max(strains) < 0.19:
            coverage_ok = False
            break
    if coverage_ok:
        total += score_check('strain_coverage')

    def get_case_data(ori, temp, bound):
        return groups.get((ori, temp, bound), [])

    # helper to safely get thresholds
    thr = lambda check_name, key, default=0.0: check_map.get(check_name, {}).get('thresholds', {}).get(key, default)

    # 3. iso_100_300_plateau
    iso_100_300 = get_case_data('100', 300, 'iso')
    if iso_100_300:
        plateau_ok = True
        if xiM_at_strain(iso_100_300, 0.2) < thr('iso_100_300_plateau', 'final_xi_M_min', 0.9):
            plateau_ok = False
        # Use strain points within the plateau region (0.02 and 0.08) to avoid
        # penalizing the post‑transformation elastic stress rise after strain ≈0.12.
        ratio = stress_ratio(iso_100_300, 0.02, 0.08)
        if abs(ratio) > thr('iso_100_300_plateau', 'stress_plateau_ratio_max', 0.05):
            plateau_ok = False
        if plateau_ok:
            total += score_check('iso_100_300_plateau')

    # 4. thermo_100_300_monotonic_and_temp
    th_100_300 = get_case_data('100', 300, 'thermo')
    if th_100_300:
        ok = True
        if stress_ratio(th_100_300, 0.1, 0.2) < thr('thermo_100_300_monotonic_and_temp', 'stress_increase_ratio_min', 0.1):
            ok = False
        if temp_at_strain(th_100_300, 0.2) < thr('thermo_100_300_monotonic_and_temp', 'temp_final_min', 310):
            ok = False
        if xiM_at_strain(th_100_300, 0.2) > thr('thermo_100_300_monotonic_and_temp', 'xi_M_final_max', 0.8):
            ok = False
        if ok:
            total += score_check('thermo_100_300_monotonic_and_temp')

    # 5. thermo_100_350_higher
    iso_100_350 = get_case_data('100', 350, 'iso')
    th_100_350 = get_case_data('100', 350, 'thermo')
    if iso_100_350 and th_100_350:
        ok = True
        s_iso = stress_at_strain(iso_100_350, 0.2)
        s_th = stress_at_strain(th_100_350, 0.2)
        if s_iso <= 0:
            ok = False
        else:
            if (s_th / s_iso) < thr('thermo_100_350_higher', 'stress_ratio_min', 1.01):
                ok = False
        if beta_at_strain(iso_100_350, 0.2) <= 0 or beta_at_strain(th_100_350, 0.2) <= 0:
            ok = False
        if ok:
            total += score_check('thermo_100_350_higher')

    # 6. iso_111_350_similar
    iso_111_350 = get_case_data('111', 350, 'iso')
    th_111_350 = get_case_data('111', 350, 'thermo')
    if iso_111_350 and th_111_350:
        ok = True
        dev = max_relative_deviation(iso_111_350, th_111_350, 'strain', 'stress_MPa')
        if dev > thr('iso_111_350_similar', 'max_relative_deviation', 0.05):
            ok = False
        xi_iso_max = max(float(r['xi_M']) for r in iso_111_350)
        xi_th_max = max(float(r['xi_M']) for r in th_111_350)
        if xi_iso_max > thr('iso_111_350_similar', 'xi_M_max', 0.2) or xi_th_max > thr('iso_111_350_similar', 'xi_M_max', 0.2):
            ok = False
        if beta_at_strain(iso_111_350, 0.2) <= 0 or beta_at_strain(th_111_350, 0.2) <= 0:
            ok = False
        if ok:
            total += score_check('iso_111_350_similar')

    return min(max(total, 0.0), 1.0)


_SCORERS = {
    'csv_structural': score_0,
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
