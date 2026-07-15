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
    for s in spec.get('steps', []):
        if s['id'] == 'thermo_check':
            return {'gold': s['gold']}
    return {}


# === block: score_0 (check id='thermo_check') ===
def score_0(artifact, step, ctx):
    try:
        gold = ctx['gold']
        rel_tol = gold.get('relative_tolerance', 0.05)
        theta_gamma_points = gold['Theta_gamma_points']
        alpha_points = gold['alpha_points']
        cv_target = gold['CV_dulong']['target']
        cv_t_k = gold['CV_dulong']['T_K']
    except Exception:
        return 0.0

    data = {}
    for row in artifact:
        try:
            compound = row['compound'].strip()
            t = round(float(row['T_K']))
            p = round(float(row['P_GPa']))
            key = (compound, t, p)
            data[key] = {
                'Theta_K': float(row['Theta_K']),
                'gamma': float(row['gamma']),
                'alpha_1e5_perK': float(row['alpha_1e5_perK']),
                'B_T_GPa': float(row['B_T_GPa']),
                'C_V_JmolK': float(row['C_V_JmolK']),
                'C_P_JmolK': float(row['C_P_JmolK'])
            }
        except Exception:
            continue

    def rel_err(val, ref):
        if ref == 0:
            return abs(val)
        return abs(val - ref) / abs(ref)

    num_passes = 0
    num_checks = 0

    for pnt in theta_gamma_points:
        key = (pnt['compound'], pnt['T_K'], pnt['P_GPa'])
        if key in data:
            d = data[key]
            err_theta = rel_err(d['Theta_K'], pnt['Theta_K'])
            err_gamma = rel_err(d['gamma'], pnt['gamma'])
            if err_theta <= rel_tol:
                num_passes += 1
            if err_gamma <= rel_tol:
                num_passes += 1
            num_checks += 2

    for a in alpha_points:
        key = (a['compound'], a['T_K'], a['P_GPa'])
        if key in data:
            d = data[key]
            err_alpha = rel_err(d['alpha_1e5_perK'], a['alpha_1e5_perK'])
            if err_alpha <= rel_tol:
                num_passes += 1
            num_checks += 1

    for comp in ['RuMnTe', 'CoMnTe']:
        cvs = []
        for key, d in data.items():
            if key[0] == comp and key[1] == cv_t_k:
                cvs.append(d['C_V_JmolK'])
        if cvs:
            mean_cv = sum(cvs) / len(cvs)
            err_cv = rel_err(mean_cv, cv_target)
            if err_cv <= rel_tol:
                num_passes += 1
            num_checks += 1

    numerical_score = num_passes / max(num_checks, 1) if num_checks > 0 else 0.0

    trends = gold.get('trends', {})
    trend_checks = 0
    trend_passes = 0

    def is_non_decreasing(lst):
        return all(lst[i] <= lst[i+1] + 1e-12 for i in range(len(lst)-1))

    def is_non_increasing(lst):
        return all(lst[i] >= lst[i+1] - 1e-12 for i in range(len(lst)-1))

    for comp in trends.get('BT_increase_with_P', {}).get('compounds', []):
        T = trends['BT_increase_with_P']['T_K']
        vals = []
        for p in [0,5,10,15,20,25,30,35,40,45]:
            key = (comp, T, p)
            if key in data:
                vals.append(data[key]['B_T_GPa'])
        if vals and is_non_decreasing(vals):
            trend_passes += 1
        trend_checks += 1

    for comp in trends.get('BT_decrease_with_T', {}).get('compounds', []):
        P = trends['BT_decrease_with_T']['P_GPa']
        vals = []
        for T in range(0, 1300, 100):
            key = (comp, T, P)
            if key in data:
                vals.append(data[key]['B_T_GPa'])
        if vals and is_non_increasing(vals):
            trend_passes += 1
        trend_checks += 1

    for comp in trends.get('Theta_increase_with_P', {}).get('compounds', []):
        T = trends['Theta_increase_with_P']['T_K']
        vals = []
        for p in [0,5,10,15,20,25,30,35,40,45]:
            key = (comp, T, p)
            if key in data:
                vals.append(data[key]['Theta_K'])
        if vals and is_non_decreasing(vals):
            trend_passes += 1
        trend_checks += 1

    for comp in trends.get('Theta_decrease_with_T', {}).get('compounds', []):
        P = trends['Theta_decrease_with_T']['P_GPa']
        vals = []
        for T in range(0, 1300, 100):
            key = (comp, T, P)
            if key in data:
                vals.append(data[key]['Theta_K'])
        if vals and is_non_increasing(vals):
            trend_passes += 1
        trend_checks += 1

    for comp in trends.get('gamma_decrease_with_P', {}).get('compounds', []):
        T = trends['gamma_decrease_with_P']['T_K']
        vals = []
        for p in [0,5,10,15,20,25,30,35,40,45]:
            key = (comp, T, p)
            if key in data:
                vals.append(data[key]['gamma'])
        if vals and is_non_increasing(vals):
            trend_passes += 1
        trend_checks += 1

    for comp in trends.get('gamma_increase_with_T', {}).get('compounds', []):
        P = trends['gamma_increase_with_T']['P_GPa']
        vals = []
        for T in range(0, 1300, 100):
            key = (comp, T, P)
            if key in data:
                vals.append(data[key]['gamma'])
        if vals and is_non_decreasing(vals):
            trend_passes += 1
        trend_checks += 1

    for comp in trends.get('alpha_decrease_with_P', {}).get('compounds', []):
        T = trends['alpha_decrease_with_P']['T_K']
        vals = []
        for p in [0,5,10,15,20,25,30,35,40,45]:
            key = (comp, T, p)
            if key in data:
                vals.append(data[key]['alpha_1e5_perK'])
        if vals and is_non_increasing(vals):
            trend_passes += 1
        trend_checks += 1

    trend_score = trend_passes / max(trend_checks, 1) if trend_checks > 0 else 0.0

    total = 0.5 * numerical_score + 0.5 * trend_score
    return total


_SCORERS = {
    'thermo_check': score_0,
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
