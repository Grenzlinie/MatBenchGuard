import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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
    gold = spec.get('hidden_gold', {})
    # Also extract gold from steps if needed
    steps = spec.get('steps', [])
    gold_params = {}
    for step in steps:
        out = step.get('output_file', '')
        if out == 'fitted_parameters.json':
            gold_params['A'] = step['params'].get('A_gold', 2.9e-8)
            gold_params['B'] = step['params'].get('B_gold', 3.3e-3)
            gold_params['Theta'] = step['params'].get('Theta_BG_gold', 50.0)
            gold_params['A_rel_tol'] = step['params'].get('A_rel_tol', 0.20)
            gold_params['B_rel_tol'] = step['params'].get('B_rel_tol', 0.20)
            gold_params['Theta_abs_tol'] = step['params'].get('Theta_abs_tol', 10.0)
            gold_params['low_T_max'] = step['params'].get('low_T_max', 30.0)
            gold_params['high_T_min'] = step['params'].get('high_T_min', 100.0)
        elif out == 'lorenz_number_300K.txt':
            gold_params['L_gold'] = step['params'].get('L_gold', 2.41e-8)
            gold_params['L_rel_tol'] = step['params'].get('rel_tol', 0.10)
    return gold_params


# === block: score_0 (check id='06_resistivity_csv') ===
def score_0(artifact, step, ctx):
    path = os.path.join('/app/outputs', 'resistivity_temperature.csv')
    if not os.path.exists(path):
        return 0.0
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if len(rows) < 10:
        return 0.0
    temps = []
    rhos_abs = []
    rhos_norm = []
    for row in rows:
        try:
            t = float(row['T_K'])
            ra = float(row['rho_abs_microOhm_cm'])
            rn = float(row['rho_normalized'])
        except (ValueError, KeyError):
            return 0.0
        temps.append(t)
        rhos_abs.append(ra)
        rhos_norm.append(rn)
    if any(ra <= 0 for ra in rhos_abs):
        return 0.0
    if any(rn <= 0 for rn in rhos_norm):
        return 0.0
    if not all(temps[i] < temps[i+1] for i in range(len(temps)-1)):
        return 0.0
    # check normalized at 300K ~ 1.0
    idx_300 = None
    for i, t in enumerate(temps):
        if abs(t - 300.0) < 0.1:
            idx_300 = i
            break
    if idx_300 is None:
        # find nearest
        idx_300 = min(range(len(temps)), key=lambda i: abs(temps[i]-300.0))
    if abs(rhos_norm[idx_300] - 1.0) > 0.02:
        return 0.0
    return 1.0


# === block: score_1 (check id='07_fitted_params') ===
def score_1(artifact, step, ctx):
    import json
    path = os.path.join('/app/outputs', 'fitted_parameters.json')
    if not os.path.exists(path):
        return 0.0
    try:
        with open(path) as f:
            data = json.load(f)
        A = float(data['A_K_minus4'])
        B = float(data['B_K_minus1'])
        Theta = float(data['Theta_BG_K'])
    except (ValueError, KeyError, TypeError, json.JSONDecodeError):
        return 0.0

    A_gold = ctx.get('A', 2.9e-8)
    B_gold = ctx.get('B', 3.3e-3)
    Theta_gold = ctx.get('Theta', 50.0)
    A_rel_tol = ctx.get('A_rel_tol', 0.20)
    B_rel_tol = ctx.get('B_rel_tol', 0.20)
    Theta_abs_tol = ctx.get('Theta_abs_tol', 10.0)

    if A_gold == 0:
        score_A = 1.0 if A == 0 else 0.0
    else:
        err_A = abs(A - A_gold) / (A_gold * A_rel_tol + 1e-12)
        score_A = max(0.0, 1.0 - err_A)
    if B_gold == 0:
        score_B = 1.0 if B == 0 else 0.0
    else:
        err_B = abs(B - B_gold) / (B_gold * B_rel_tol + 1e-12)
        score_B = max(0.0, 1.0 - err_B)
    err_Th = abs(Theta - Theta_gold) / (Theta_abs_tol + 1e-12)
    score_Th = max(0.0, 1.0 - err_Th)
    return (score_A + score_B + score_Th) / 3.0


# === block: score_2 (check id='08_lorenz_number') ===
def score_2(artifact, step, ctx):
    path = os.path.join('/app/outputs', 'lorenz_number_300K.txt')
    if not os.path.exists(path):
        return 0.0
    try:
        with open(path) as f:
            text = f.read().strip()
        L = float(text)
    except (ValueError, TypeError):
        return 0.0
    L_gold = ctx.get('L_gold', 2.41e-8)
    rel_tol = ctx.get('L_rel_tol', 0.10)
    if L_gold == 0:
        return 1.0 if L == 0 else 0.0
    err = abs(L - L_gold) / (L_gold * rel_tol + 1e-12)
    return max(0.0, 1.0 - err)


_SCORERS = {
    '06_resistivity_csv': score_0,
    '07_fitted_params': score_1,
    '08_lorenz_number': score_2,
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
