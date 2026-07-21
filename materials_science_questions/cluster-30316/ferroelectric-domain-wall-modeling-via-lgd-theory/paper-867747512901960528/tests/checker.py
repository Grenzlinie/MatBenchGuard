import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, os


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
    kappa = 0.2
    lam = 1e-9
    Tk = 1e-3
    a = 1e-10
    A = 2e-17
    Ms = 2e6
    gam = 1.76e11
    alpha = 0.01

    # Analytic gold velocities
    k_torque = 5.0 / lam
    tau_analytic = 1.0 - math.cos(5.0 * math.log(1.0 - kappa))
    tau_phys = Tk * (a**2) * k_torque * tau_analytic
    s = (Ms / gam) * A
    V_FM_gold = tau_phys / (2.0 * s)

    k_force = 0.5 / lam
    F_analytic = (kappa**2) * (0.5**2)
    F_phys = Tk * (a**2) * (k_force**2) * F_analytic
    V_AFM_gold = lam * F_phys / (2.0 * alpha * s)

    # Analytic reference curves for torque_force check
    kl_vals = [0.1 * i for i in range(1, 101)]  # 0.1,0.2,...,10.0
    tau_approx_gold = {kl: 1.0 - math.cos(kl * math.log(1.0 - kappa)) for kl in kl_vals}
    F_approx_gold = {kl: (kappa**2) * (kl**2) for kl in kl_vals}

    ctx = {
        "V_FM_gold": V_FM_gold,
        "V_AFM_gold": V_AFM_gold,
        "gold_tau_approx": tau_approx_gold,
        "gold_F_approx": F_approx_gold
    }
    return ctx


# === block: score_0 (check id='scattering_params') ===
def score_0(artifact, step, ctx):
    data = artifact
    required_keys = ["k_lambda","u_trans_amplitude","u_refl_amplitude","v_trans_amplitude","v_refl_amplitude"]
    if not all(k in data for k in required_keys):
        return 0.0
    n = len(data["k_lambda"])
    if n < 2:
        return 0.0
    devs = []
    pairs = [("u_trans_amplitude","u_refl_amplitude"), ("v_trans_amplitude","v_refl_amplitude")]
    for t_key, r_key in pairs:
        t = data[t_key]
        r = data[r_key]
        for i in range(n):
            val = t[i]**2 + r[i]**2
            devs.append(abs(val - 1.0))
    if not devs:
        return 0.0
    avg_dev = sum(devs) / len(devs)
    score = max(0.0, min(1.0, 1.0 - (avg_dev - 0.02) / 0.08))
    return score


# === block: score_1 (check id='torque_force') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    cols = ["k_lambda","tau_dimless","F_dimless","tau_approx_dimless","F_approx_dimless"]
    if not all(c in rows[0] for c in cols):
        return 0.0
    kl_vals = [float(r["k_lambda"]) for r in rows]
    tau_num = [float(r["tau_dimless"]) for r in rows]
    F_num = [float(r["F_dimless"]) for r in rows]

    gold_tau = ctx["gold_tau_approx"]
    gold_F  = ctx["gold_F_approx"]

    errors_tau = []
    for kl, tau in zip(kl_vals, tau_num):
        if kl >= 2.0:
            g = gold_tau.get(kl, None)
            if g is not None:
                errors_tau.append(abs(tau - g))
    tau_rmse = (sum(e**2 for e in errors_tau) / max(1, len(errors_tau))) ** 0.5 if errors_tau else 1e9
    tau_score = max(0.0, 1.0 - tau_rmse / 0.5)   # tau ≈ 0..2

    errors_F = []
    for kl, F in zip(kl_vals, F_num):
        if kl <= 1.0:
            g = gold_F.get(kl, None)
            if g is not None:
                errors_F.append(abs(F - g))
    F_rmse = (sum(e**2 for e in errors_F) / max(1, len(errors_F))) ** 0.5 if errors_F else 1e9
    F_score = max(0.0, 1.0 - F_rmse / 0.01)   # F ≈ 0..0.01

    score = 0.6 * tau_score + 0.4 * F_score
    return score


# === block: score_2 (check id='velocities') ===
def score_2(artifact, step, ctx):
    torque_csv = os.path.join("/app/outputs", "torque_force_values.csv")
    if not os.path.exists(torque_csv):
        return 0.0
    with open(torque_csv, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    tau_at_5 = None
    F_at_05 = None
    for r in rows:
        kl = float(r["k_lambda"])
        if abs(kl - 5.0) < 1e-6:
            tau_at_5 = float(r["tau_dimless"])
        if abs(kl - 0.5) < 1e-6:
            F_at_05 = float(r["F_dimless"])
    if tau_at_5 is None or F_at_05 is None:
        return 0.0

    T_kappa = 1e-3
    a = 1e-10
    lam = 1e-9
    k_torque = 5.0 / lam
    tau_phys = T_kappa * (a**2) * k_torque * tau_at_5
    M_s = 2e6
    gamma = 1.76e11
    A = 2e-17
    s = (M_s / gamma) * A
    V_FM = tau_phys / (2.0 * s)

    k_force = 0.5 / lam
    F_phys = T_kappa * (a**2) * (k_force**2) * F_at_05
    alpha = 0.01
    V_AFM = lam * F_phys / (2.0 * alpha * s)

    V_FM_gold = ctx["V_FM_gold"]
    V_AFM_gold = ctx["V_AFM_gold"]
    tol_rel = 0.05
    score_FM = max(0.0, 1.0 - abs(V_FM - V_FM_gold) / (tol_rel * V_FM_gold))
    score_AFM = max(0.0, 1.0 - abs(V_AFM - V_AFM_gold) / (tol_rel * V_AFM_gold))
    score = 0.5 * score_FM + 0.5 * score_AFM
    return score


_SCORERS = {
    'scattering_params': score_0,
    'torque_force': score_1,
    'velocities': score_2,
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
