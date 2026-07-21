import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import os


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
    import os
    import csv
    import json

    outputs_dir = os.environ.get('OUTPUT_DIR', '/app/outputs')

    # Load diagnostics.csv
    diag_path = os.path.join(outputs_dir, 'diagnostics.csv')
    diagnostics = []
    with open(diag_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['temperature'] = float(row['temperature'])
            row['x_i'] = float(row['x_i'])
            row['y_i'] = float(row['y_i'])
            row['R_squared'] = float(row['R_squared'])
            row['slope'] = float(row['slope'])
            row['intercept'] = float(row['intercept'])
            diagnostics.append(row)

    # Load results.json
    res_path = os.path.join(outputs_dir, 'results.json')
    with open(res_path) as f:
        results = json.load(f)

    # Gold from spec
    gold = spec.get('gold', {})

    # Physical constants
    k_boltzmann_eV = 8.617333262145e-5
    kcal_per_eV = 23.0605
    k_kcal = k_boltzmann_eV * kcal_per_eV  # ~0.001987204 kcal/(mol·K)

    ctx = {
        'diagnostics': diagnostics,
        'results': results,
        'gold': gold,
        'k_kcal': k_kcal
    }
    return ctx


# === block: score_0 (check id='diagnostics_shape') ===
def score_0(artifact, step, ctx):
    from collections import defaultdict

    gold = ctx.get('gold', {})
    diag = ctx['diagnostics']
    res = ctx.get('results', {})
    if not diag:
        return 0.0

    # --- column check ---
    required_cols = {'system', 'defect_model', 'temperature', 'x_i', 'y_i', 'R_squared', 'slope', 'intercept'}
    cols = set(diag[0].keys())
    if not required_cols.issubset(cols):
        return 0.0

    # --- systems present ---
    systems = set(r['system'] for r in diag)
    required_systems = {'YH2', 'CeH2', 'ThC'}
    if not required_systems.issubset(systems):
        return 0.0

    # --- expected temperatures per system (from hidden gold) ---
    system_temp_keys = {
        'YH2': gold.get('YH2', {}).get('temperatures_C', []),
        'CeH2': gold.get('CeH2', {}).get('temperatures_C', []),
        'ThC': gold.get('ThC', {}).get('temperatures_K', []),
    }

    # For each system and each expected temperature, ensure at least three distinct
    # defect models are present (the agent may name them any way, as long as three
    # candidate models are covered).  We also keep the consistency rule that the
    # reported defect must agree with the highest‑R² model in the diagnostics.

    for sys, exp_temps in system_temp_keys.items():
        exp_temp_set = set(exp_temps)
        diag_temps = set()
        models_per_temp = defaultdict(set)
        for r in diag:
            if r['system'] != sys:
                continue
            temp = r['temperature']
            diag_temps.add(temp)
            models_per_temp[temp].add(r['defect_model'])
        # all expected temperatures must be present
        if not exp_temp_set.issubset(diag_temps):
            return 0.0
        # each expected temperature must have at least three distinct defect models
        for temp in exp_temp_set:
            if len(models_per_temp[temp]) < 3:
                return 0.0

    # --- consistency: reported defect type must match the best model (by R²)
    #     for every temperature of that system ---
    system_res_keys = {
        'YH2': res.get('YH2', {}),
        'CeH2': res.get('CeH2', {}),
        'ThC': res.get('ThC', {}),
    }
    for sys, sys_res in system_res_keys.items():
        reported_defect = sys_res.get('identified_defect')
        if not reported_defect:
            continue   # shape check only, missing is not a shape failure
        # group rows by temperature
        temp_groups = defaultdict(list)
        for r in diag:
            if r['system'] == sys:
                temp_groups[r['temperature']].append(r)
        # for each temperature, the highest‑R² model must equal the reported defect
        for temp, rows in temp_groups.items():
            best = max(rows, key=lambda r: r['R_squared'])
            if best['defect_model'] != reported_defect:
                return 0.0

    return 1.0


# === block: score_1 (check id='defect_identification') ===
def score_1(artifact, step, ctx):
    gold = ctx['gold']
    expected_defects = gold['expected_defects']
    diag = ctx['diagnostics']

    # Group by (system, temperature) and find highest R² model
    from collections import defaultdict
    groups = defaultdict(list)
    for r in diag:
        groups[(r['system'], r['temperature'])].append(r)

    # For each system we need expected temperatures from gold
    system_temps = {
        'YH2': gold['YH2']['temperatures_C'],
        'CeH2': gold['CeH2']['temperatures_C'],
        'ThC': gold['ThC']['temperatures_K']
    }
    correct = 0
    total = 0
    for sys, temps in system_temps.items():
        for tmp in temps:
            key = (sys, tmp)
            if key not in groups:
                continue
            best = max(groups[key], key=lambda r: r['R_squared'])
            if best['defect_model'] == expected_defects[sys]:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_2 (check id='xi_ceh2') ===
def score_2(artifact, step, ctx):
    gold = ctx['gold']['CeH2']
    res = ctx['results'].get('CeH2', {})
    reported_temps = res.get('temperatures_C', [])
    reported_xi = res.get('xi_H_values_kcal_per_mol', [])
    if len(reported_temps) != len(reported_xi):
        return 0.0

    # Build mapping from temperature to xi
    xi_map = {}
    for T, xi in zip(reported_temps, reported_xi):
        xi_map[T] = xi

    tol = gold['tolerance_xi']
    correct = 0
    total = 0
    for T_gold, xi_gold in zip(gold['temperatures_C'], gold['xi_kcal_per_mol']):
        if T_gold not in xi_map:
            continue
        if abs(xi_map[T_gold] - xi_gold) <= tol:
            correct += 1
        total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_3 (check id='xi_thc') ===
def score_3(artifact, step, ctx):
    gold = ctx['gold']['ThC']
    res = ctx['results'].get('ThC', {})
    reported_temps = res.get('temperatures_K', [])
    reported_xi = res.get('xi_C_values_kcal_per_mol', [])
    if len(reported_temps) != len(reported_xi):
        return 0.0

    xi_map = {}
    for T, xi in zip(reported_temps, reported_xi):
        xi_map[T] = xi

    tol = gold['tolerance_xi']
    correct = 0
    total = 0
    for T_gold, xi_gold in zip(gold['temperatures_K'], gold['xi_kcal_per_mol']):
        if T_gold not in xi_map:
            continue
        if abs(xi_map[T_gold] - xi_gold) <= tol:
            correct += 1
        total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_4 (check id='yh2_formation') ===
def score_4(artifact, step, ctx):
    gold = ctx['gold']['YH2']
    yh2 = ctx['results'].get('YH2', {})
    if not yh2:
        return 0.0

    enthalpy = yh2.get('formation_enthalpy_kcal_per_mol')
    entropy = yh2.get('formation_entropy_cal_per_deg_mol')
    if enthalpy is None or entropy is None:
        return 0.0

    tol_h = gold['tolerance_enthalpy']
    tol_s = gold['tolerance_entropy']
    score = 0.0
    if abs(enthalpy - gold['formation_enthalpy_kcal_per_mol']) <= tol_h:
        score += 0.5
    if abs(entropy - gold['formation_entropy_cal_per_deg_mol']) <= tol_s:
        score += 0.5
    return score


# === block: score_5 (check id='consistency') ===
def score_5(artifact, step, ctx):
    diag = ctx['diagnostics']
    res = ctx['results']
    k_kcal = ctx['k_kcal']
    gold = ctx['gold']

    # Helper to extract best slope for a system at a temperature from diagnostics
    def best_slope(sys, temp):
        candidates = [r for r in diag if r['system'] == sys and r['temperature'] == temp]
        if not candidates:
            return None
        best = max(candidates, key=lambda r: r['R_squared'])
        return best['slope']

    # Check CeH2
    ceh2_res = res.get('CeH2', {})
    reported_xi = ceh2_res.get('xi_H_values_kcal_per_mol', [])
    reported_temps = ceh2_res.get('temperatures_C', [])
    if len(reported_xi) != len(reported_temps):
        return 0.0
    alpha, z_I = 2.0, 12.0
    for T_C, xi_reported in zip(reported_temps, reported_xi):
        slope = best_slope('CeH2', T_C)
        if slope is None:
            return 0.0
        T_K = T_C + 273.15
        xi_calc = alpha * k_kcal * T_K * slope / z_I
        if abs(xi_calc - xi_reported) > 1e-6 * max(1.0, abs(xi_reported)):
            return 0.0

    # Check ThC
    thc_res = res.get('ThC', {})
    reported_xi = thc_res.get('xi_C_values_kcal_per_mol', [])
    reported_temps = thc_res.get('temperatures_K', [])
    if len(reported_xi) != len(reported_temps):
        return 0.0
    s, z_M = 1.0, 6.0
    for T_K, xi_reported in zip(reported_temps, reported_xi):
        slope = best_slope('ThC', T_K)
        if slope is None:
            return 0.0
        xi_calc = 2.0 * s * k_kcal * T_K * slope / z_M
        if abs(xi_calc - xi_reported) > 1e-6 * max(1.0, abs(xi_reported)):
            return 0.0

    # Check YH2
    yh2_res = res.get('YH2', {})
    reported_xi = yh2_res.get('xi_H_values_kcal_per_mol', [])
    reported_temps = yh2_res.get('temperatures_C', [])
    if len(reported_xi) != len(reported_temps):
        return 0.0
    s, z_X = 2.0, 6.0
    for T_C, xi_reported in zip(reported_temps, reported_xi):
        slope = best_slope('YH2', T_C)
        if slope is None:
            return 0.0
        T_K = T_C + 273.15
        # For X vacancies: xi = - s * kT * slope / z_X
        xi_calc = - s * k_kcal * T_K * slope / z_X
        if abs(xi_calc - xi_reported) > 1e-6 * max(1.0, abs(xi_reported)):
            return 0.0

    return 1.0


_SCORERS = {
    'diagnostics_shape': score_0,
    'defect_identification': score_1,
    'xi_ceh2': score_2,
    'xi_thc': score_3,
    'yh2_formation': score_4,
    'consistency': score_5,
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
