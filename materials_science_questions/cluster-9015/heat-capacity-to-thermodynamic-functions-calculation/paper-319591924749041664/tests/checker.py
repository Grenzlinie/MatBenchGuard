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
    return {'spec': spec}


# === block: score_0 (check id='step-1') ===
def score_0(artifact, step, ctx):
    expected = step.get('expected_Cp', [])
    tol_Cp = 1e-3
    tol_dH_rel = 0.005
    tol_dS_rel = 0.01
    tol_Phi_rel = 0.01

    T_vals = []
    Cp_vals = []
    dH_vals = []
    dS_vals = []
    Phi_vals = []
    for row in artifact:
        T_vals.append(float(row['T (K)']))
        Cp_vals.append(float(row['Cp (J/(mol·K))']))
        dH_vals.append(float(row['delta_H (kJ/mol)']))
        dS_vals.append(float(row['delta_S (J/(mol·K))']))
        Phi_vals.append(float(row['Phi (J/(mol·K))']))

    exp_t_to_cp = {t: cp for t, cp in expected}
    for t, cp in zip(T_vals, Cp_vals):
        if t not in exp_t_to_cp or abs(cp - exp_t_to_cp[t]) > tol_Cp:
            return 0.0

    calc_dH = [0.0]
    calc_dS = [0.0]
    for i in range(1, len(T_vals)):
        dt = T_vals[i] - T_vals[i-1]
        area_H = 0.5 * (Cp_vals[i-1] + Cp_vals[i]) * dt
        area_S = 0.5 * (Cp_vals[i-1]/T_vals[i-1] + Cp_vals[i]/T_vals[i]) * dt
        calc_dH.append(calc_dH[-1] + area_H/1000.0)
        calc_dS.append(calc_dS[-1] + area_S)

    calc_Phi = [calc_dS[i] - (calc_dH[i] * 1000.0) / T_vals[i] for i in range(len(T_vals))]

    max_err_dH = 0.0
    max_err_dS = 0.0
    max_err_Phi = 0.0
    eps = 1e-12
    for i in range(len(T_vals)):
        a_dh = dH_vals[i]
        c_dh = calc_dH[i]
        denom_dh = max(abs(a_dh), abs(c_dh))
        if denom_dh > eps:
            err_dh = abs(a_dh - c_dh) / denom_dh
        else:
            err_dh = 0.0
        max_err_dH = max(max_err_dH, err_dh)

        a_ds = dS_vals[i]
        c_ds = calc_dS[i]
        denom_ds = max(abs(a_ds), abs(c_ds))
        if denom_ds > eps:
            err_ds = abs(a_ds - c_ds) / denom_ds
        else:
            err_ds = 0.0
        max_err_dS = max(max_err_dS, err_ds)

        a_phi = Phi_vals[i]
        c_phi = calc_Phi[i]
        denom_phi = max(abs(a_phi), abs(c_phi))
        if denom_phi > eps:
            err_phi = abs(a_phi - c_phi) / denom_phi
        else:
            err_phi = 0.0
        max_err_Phi = max(max_err_Phi, err_phi)

    dH_ok = max_err_dH <= tol_dH_rel
    dS_ok = max_err_dS <= tol_dS_rel
    Phi_ok = max_err_Phi <= tol_Phi_rel
    if dH_ok and dS_ok and Phi_ok:
        return 1.0

    excess_dH = max(0.0, max_err_dH - tol_dH_rel)
    excess_dS = max(0.0, max_err_dS - tol_dS_rel)
    excess_Phi = max(0.0, max_err_Phi - tol_Phi_rel)

    penalty_dH = min(excess_dH / tol_dH_rel, 1.0) if tol_dH_rel > 0 else 0.0
    penalty_dS = min(excess_dS / tol_dS_rel, 1.0) if tol_dS_rel > 0 else 0.0
    penalty_Phi = min(excess_Phi / tol_Phi_rel, 1.0) if tol_Phi_rel > 0 else 0.0

    penalty = max(penalty_dH, penalty_dS, penalty_Phi)
    return max(0.0, 1.0 - penalty)


# === block: score_1 (check id='step-2') ===
def score_1(artifact, step, ctx):
    expected = step.get('expected_Cp', [])
    tol_Cp = 1e-3
    tol_dH_rel = 0.005
    tol_dS_rel = 0.01

    T_vals = []
    Cp_vals = []
    dH_vals = []
    dS_vals = []
    for row in artifact:
        T_vals.append(float(row['T (K)']))
        Cp_vals.append(float(row['Cp (J/(mol·K))']))
        dH_vals.append(float(row['delta_H (kJ/mol)']))
        dS_vals.append(float(row['delta_S (J/(mol·K))']))

    exp_t_to_cp = {t: cp for t, cp in expected}
    for t, cp in zip(T_vals, Cp_vals):
        if t not in exp_t_to_cp or abs(cp - exp_t_to_cp[t]) > tol_Cp:
            return 0.0

    calc_dH = [0.0]
    calc_dS = [0.0]
    for i in range(1, len(T_vals)):
        dt = T_vals[i] - T_vals[i-1]
        area_H = 0.5 * (Cp_vals[i-1] + Cp_vals[i]) * dt
        area_S = 0.5 * (Cp_vals[i-1]/T_vals[i-1] + Cp_vals[i]/T_vals[i]) * dt
        calc_dH.append(calc_dH[-1] + area_H/1000.0)
        calc_dS.append(calc_dS[-1] + area_S)

    max_err_dH = 0.0
    max_err_dS = 0.0
    eps = 1e-12
    for i in range(len(T_vals)):
        a_dh = dH_vals[i]
        c_dh = calc_dH[i]
        denom_dh = max(abs(a_dh), abs(c_dh))
        if denom_dh > eps:
            err_dh = abs(a_dh - c_dh) / denom_dh
        else:
            err_dh = 0.0
        max_err_dH = max(max_err_dH, err_dh)
        a_ds = dS_vals[i]
        c_ds = calc_dS[i]
        denom_ds = max(abs(a_ds), abs(c_ds))
        if denom_ds > eps:
            err_ds = abs(a_ds - c_ds) / denom_ds
        else:
            err_ds = 0.0
        max_err_dS = max(max_err_dS, err_ds)

    dH_ok = max_err_dH <= tol_dH_rel
    dS_ok = max_err_dS <= tol_dS_rel
    if dH_ok and dS_ok:
        return 1.0

    excess_dH = max(0.0, max_err_dH - tol_dH_rel)
    excess_dS = max(0.0, max_err_dS - tol_dS_rel)
    penalty_dH = min(excess_dH / tol_dH_rel, 1.0) if tol_dH_rel > 0 else 0.0
    penalty_dS = min(excess_dS / tol_dS_rel, 1.0) if tol_dS_rel > 0 else 0.0
    penalty = max(penalty_dH, penalty_dS)
    return max(0.0, 1.0 - penalty)


_SCORERS = {
    'step-1': score_0,
    'step-2': score_1,
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
