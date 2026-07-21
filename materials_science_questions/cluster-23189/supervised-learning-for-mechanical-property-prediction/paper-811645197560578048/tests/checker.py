import os
import json
import csv

# === author imports / helpers ===
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
    E_fL = 225.0
    E_fT = 15.8
    E_m = 3.43
    G_f = 19.6
    G_m = 1.27
    nu_fL = 0.3
    nu_fT = 0.021
    nu_m = 0.36

    def compute_forward(Vf_pct):
        Vf = Vf_pct / 100.0
        E11 = E_fL * Vf + E_m * (1.0 - Vf)
        denom_E22 = E_m * Vf + E_fT * (1.0 - Vf)
        E22 = (E_fT * E_m) / denom_E22 if denom_E22 != 0 else 0.0
        nu12 = nu_fL * Vf + nu_m * (1.0 - Vf)
        nu21 = (E22 * nu12) / E11 if E11 != 0 else 0.0
        denom_nu23 = Vf / E_fT + (1.0 - Vf) / E_m
        num_nu23 = nu_fT * Vf / E_fT + nu_m * (1.0 - Vf) / E_m
        nu23 = num_nu23 / denom_nu23 if denom_nu23 != 0 else 0.0
        denom_G12 = 1.0/(G_f - G_m) + (1.0 - Vf)/(2.0*G_m)
        G12 = G_m + Vf / denom_G12 if denom_G12 != 0 else 0.0
        G23 = E22 / (2.0 * (1.0 + nu23)) if (1.0 + nu23) != 0 else 0.0
        return E11, E22, G12, G23, nu12, nu21, nu23

    def compute_laminate(theta_deg):
        Vf_pct = 60
        Vf = Vf_pct / 100.0
        E1 = E_fL * Vf + E_m * (1.0 - Vf)
        denom_E2 = E_m * Vf + E_fT * (1.0 - Vf)
        E2 = (E_fT * E_m) / denom_E2 if denom_E2 != 0 else 0.0
        nu12_lam = nu_fL * Vf + nu_m * (1.0 - Vf)
        nu21_lam = (E2 * nu12_lam) / E1 if E1 != 0 else 0.0
        denom_G12_lam = 1.0/(G_f - G_m) + (1.0 - Vf)/(2.0*G_m)
        G12_lam = G_m + Vf / denom_G12_lam if denom_G12_lam != 0 else 0.0
        denom_Q = 1.0 - nu12_lam * nu21_lam
        Q11 = E1 / denom_Q if denom_Q != 0 else 0.0
        Q22 = E2 / denom_Q if denom_Q != 0 else 0.0
        Q12 = nu12_lam * Q22
        Q66 = G12_lam
        theta = math.radians(theta_deg)
        c = math.cos(theta)
        s = math.sin(theta)
        c2 = c * c
        s2 = s * s
        c4 = c2 * c2
        s4 = s2 * s2
        sc = s * c
        sc2 = sc * sc
        Qbar11 = Q11*c4 + 2.0*(Q12 + 2.0*Q66)*sc2*c2 + Q22*s4
        Qbar22 = Q11*s4 + 2.0*(Q12 + 2.0*Q66)*sc2*s2 + Q22*c4  # actually s4? Wait formula: (Q12+2Q66)*s^2 c^2 added to Q22*c^4. Standard formula: Qbar22 = Q11*s^4 + 2(Q12+2Q66)*s^2*c^2 + Q22*c^4
        Qbar22 = Q11*s4 + 2.0*(Q12 + 2.0*Q66)*sc2 + Q22*c4
        Qbar12 = (Q11+Q22-4.0*Q66)*sc2 + Q12*(c4+s4)
        Qbar66 = (Q11+Q22-2.0*Q12-2.0*Q66)*sc2 + Q66*(c4+s4)
        # For balanced symmetric laminate A_ij = h * Qbar_ij(θ), effective engineering constants:
        h = 1.0  # arbitrary thickness, cancels out
        A11 = h * Qbar11
        A22 = h * Qbar22
        A12 = h * Qbar12
        A66 = h * Qbar66
        denom_A = A11*A22 - A12*A12
        Ex = denom_A / (A22 * h) if A22 != 0 else 0.0
        Ey = denom_A / (A11 * h) if A11 != 0 else 0.0
        Gxy = A66 / h if h != 0 else 0.0
        return Ex, Ey, Gxy

    forward_test = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    forward_gold = {}
    for Vf in forward_test:
        vals = compute_forward(Vf)
        forward_gold[Vf] = {"E11": vals[0], "E22": vals[1], "G12": vals[2], "G23": vals[3], "nu12": vals[4], "nu21": vals[5], "nu23": vals[6]}

    inverse_Vf_test = [35, 45, 55, 65, 75]
    inverse_Vf_gold = {}
    for Vf in inverse_Vf_test:
        vals = compute_forward(Vf)
        inverse_Vf_gold[Vf] = {"E11": vals[0], "E22": vals[1], "G12": vals[2]}

    angle_test = [5, 20, 35, 50, 65, 80]
    angle_gold = {}
    for theta in angle_test:
        Ex, Ey, Gxy = compute_laminate(theta)
        angle_gold[theta] = {"E11": Ex, "E22": Ey, "G12": Gxy}

    ctx = {
        "forward_gold": forward_gold,
        "forward_test_set": set(forward_test),
        "inverse_Vf_gold": inverse_Vf_gold,
        "inverse_Vf_test_set": set(inverse_Vf_test),
        "angle_gold": angle_gold,
        "angle_test_set": set(angle_test)
    }
    return ctx


# === block: score_0 (check id='forward_predictions_check') ===
def score_0(artifact, step, ctx):
    import math
    artifact = artifact  # provided by harness
    step = step
    ctx = ctx
    rows = artifact
    if not rows or not isinstance(rows, list):
        return 0.0
    try:
        # validate test set
        submitted_vfs = set()
        forward_gold = ctx["forward_gold"]
        test_set = ctx["forward_test_set"]
        for row in rows:
            vf = int(float(row["Vf_pct"]))
            submitted_vfs.add(vf)
            if vf not in test_set:
                return 0.0
        if submitted_vfs != test_set:
            return 0.0
        max_rel_err = 0.0
        for row in rows:
            vf = int(float(row["Vf_pct"]))
            gold = forward_gold[vf]
            for col in ["E11_pred", "E22_pred", "G12_pred", "G23_pred", "nu12_pred", "nu21_pred", "nu23_pred"]:
                gold_key = col.replace("_pred", "")
                gold_val = gold[gold_key]
                pred_val = float(row[col])
                if gold_val != 0:
                    rel = abs(pred_val - gold_val) / abs(gold_val)
                else:
                    rel = abs(pred_val)  # treat as absolute
                if rel > max_rel_err:
                    max_rel_err = rel
        threshold = 0.02
        if max_rel_err <= threshold:
            return 1.0
        else:
            decay_range = 5.0 * threshold  # 0.1
            excess = max_rel_err - threshold
            score = max(0.0, 1.0 - excess / decay_range)
            return score
    except Exception:
        return 0.0


# === block: score_1 (check id='inverse_Vf_predictions_check') ===
def score_1(artifact, step, ctx):
    artifact = artifact
    step = step
    ctx = ctx
    rows = artifact
    if not rows or not isinstance(rows, list):
        return 0.0
    try:
        inverse_Vf_gold = ctx["inverse_Vf_gold"]
        test_set = ctx["inverse_Vf_test_set"]
        submitted_vfs = set()
        for row in rows:
            vf = float(row["Vf_true"])
            submitted_vfs.add(vf)
            if vf not in test_set:
                return 0.0
        if submitted_vfs != test_set:
            return 0.0
        max_abs_err = 0.0
        for row in rows:
            vf_true = float(row["Vf_true"])
            vf_pred = float(row["Vf_pred"])
            abs_err = abs(vf_pred - vf_true)
            if abs_err > max_abs_err:
                max_abs_err = abs_err
        threshold = 1.0  # 1%
        if max_abs_err <= threshold:
            return 1.0
        else:
            decay_range = 5.0 * threshold  # 5.0
            excess = max_abs_err - threshold
            score = max(0.0, 1.0 - excess / decay_range)
            return score
    except Exception:
        return 0.0


# === block: score_2 (check id='angle_predictions_check') ===
def score_2(artifact, step, ctx):
    artifact = artifact
    step = step
    ctx = ctx
    rows = artifact
    if not rows or not isinstance(rows, list):
        return 0.0
    try:
        angle_gold = ctx["angle_gold"]
        test_set = ctx["angle_test_set"]
        submitted_theta = set()
        for row in rows:
            th = float(row["theta_true"])
            submitted_theta.add(th)
            if th not in test_set:
                return 0.0
        if submitted_theta != test_set:
            return 0.0
        max_abs_err = 0.0
        for row in rows:
            th_true = float(row["theta_true"])
            th_pred = float(row["theta_pred"])
            abs_err = abs(th_pred - th_true)
            if abs_err > max_abs_err:
                max_abs_err = abs_err
        threshold = 1.0  # 1 degree
        if max_abs_err <= threshold:
            return 1.0
        else:
            decay_range = 5.0 * threshold  # 5 degrees
            excess = max_abs_err - threshold
            score = max(0.0, 1.0 - excess / decay_range)
            return score
    except Exception:
        return 0.0


_SCORERS = {
    'forward_predictions_check': score_0,
    'inverse_Vf_predictions_check': score_1,
    'angle_predictions_check': score_2,
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
