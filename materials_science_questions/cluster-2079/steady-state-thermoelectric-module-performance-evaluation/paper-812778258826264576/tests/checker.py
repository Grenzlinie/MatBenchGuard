import os
import json
import csv

# === author imports / helpers ===
import math

def k_n1(T):
    return 0.6586 + 329.63/T + 22145.0/(T*T)
def k_n2(T):
    return -4.6205 + 9.9277e-3*T + 833.7/T + 235636.0/(T*T)
def k_p1(T):
    return 0.56959 + 550.66/T - 47483.0/(T*T)
def k_p2(T):
    return -1.8067 + 5.729e-3*T - 64.639/T + 1.3395e5/(T*T)

def alpha_n1(T):
    return 173.26 - 3.8229*T + 0.011679*T*T - 1.5584e-5*T**3 + 7.6695e-9*T**4
def alpha_n2(T):
    return 443.49 - 4.5121*T + 9.4424e-3*T*T - 5.8362e-6*T**3
def alpha_p1(T):
    return 1450.0 - 10.36*T + 0.03123*T*T - 4.038e-5*T**3 + 1.903e-8*T**4
def alpha_p2(T):
    return -188.2 + 2.2411*T - 3.0075e-3*T*T + 2.4914e-7*T**3

def sigma_n1(T):
    return 1462.0 - 10.419*T + 0.031315*T*T - 4.029e-5*T**3 + 1.9034e-8*T**4
def sigma_n2(T):
    return -2139.4 + 2.5778*T + math.exp(12.795 - 0.89098*math.log(T))
def sigma_p1(T):
    return 179.02 + 12.336*T - 0.042167*T*T + 5.129e-5*T**3 - 2.1435e-8*T**4
def sigma_p2(T):
    return -473.1 + 0.86507*T + math.exp(16.637 - 1.6942*math.log(T))

def compute_teg_one(theta, a, RL_R0, ctx):
    T_low = ctx['T_low']
    T_high = T_low / theta
    mu = 0.5
    A0 = ctx['A0']
    L = ctx['L']
    R0 = ctx['R0']
    K0 = ctx['K0']
    T_int_n = (T_high + T_low) / 2.0
    T_int_p = (T_high + T_low) / 2.0
    for _ in range(30):
        T_n1_avg = (T_high + T_int_n) / 2.0
        T_n2_avg = (T_int_n + T_low) / 2.0
        T_p1_avg = (T_high + T_int_p) / 2.0
        T_p2_avg = (T_int_p + T_low) / 2.0
        k_n1_v = k_n1(T_n1_avg)
        k_n2_v = k_n2(T_n2_avg)
        k_p1_v = k_p1(T_p1_avg)
        k_p2_v = k_p2(T_p2_avg)
        ea = math.exp(a)
        ema = math.exp(-a)
        if abs(a) > 1e-12:
            emu = math.exp(a * mu)
            f1 = (1.0 - ema) * (emu - 1.0) / (a * a)
            f2 = (1.0 - ema) * (ea - emu) / (a * a)
        else:
            f1 = mu
            f2 = 1.0 - mu
        k_n_eff = 1.0 / (f1 / k_n1_v + f2 / k_n2_v)
        k_p_eff = 1.0 / (mu / k_p1_v + (1.0 - mu) / k_p2_v)
        a_n1 = alpha_n1(T_n1_avg)
        a_n2 = alpha_n2(T_n2_avg)
        a_p1 = alpha_p1(T_p1_avg)
        a_p2 = alpha_p2(T_p2_avg)
        alpha_n_eff = a_n1 * k_n_eff / k_n1_v * f1 + a_n2 * k_n_eff / k_n2_v * f2
        alpha_p_eff = a_p1 * k_p_eff / k_p1_v * mu + a_p2 * k_p_eff / k_p2_v * (1.0 - mu)
        alpha_eff = alpha_p_eff - alpha_n_eff
        alpha_eff1 = a_p1 - a_n1
        s_n1 = sigma_n1(T_n1_avg)
        s_n2 = sigma_n2(T_n2_avg)
        s_p1 = sigma_p1(T_p1_avg)
        s_p2 = sigma_p2(T_p2_avg)
        if abs(a) > 1e-12:
            R_n = ((1.0 - ema) * L / (a * a * A0)) * ((emu - 1.0) / s_n1 + (ea - emu) / s_n2)
        else:
            R_n = L * (mu / s_n1 + (1.0 - mu) / s_n2) / A0
        R_p = (1.0 / A0) * (mu * L / s_p1 + (1.0 - mu) * L / s_p2)
        R_TEG = R_n + R_p
        K_eff = (k_n_eff + k_p_eff) * A0 / L
        ZT_avg = (alpha_eff * alpha_eff) * T_high * (1.0 + theta) / (2.0 * R_TEG * K_eff)
        RL = RL_R0 * R0
        term_num = 2.0 * ZT_avg * (1.0 - theta) * RL_R0 * (R_TEG / R0)
        # compute R_n1 and R_p1 for material-1 unsegmented
        T_avg_ml = (T_high + T_low) / 2.0
        s_n1_ml = sigma_n1(T_avg_ml)
        s_p1_ml = sigma_p1(T_avg_ml)
        if abs(a) > 1e-12:
            R_n1_ml = ((1.0 - ema) * L / (a * a * A0)) * (ea - 1.0) / s_n1_ml
        else:
            R_n1_ml = L / (s_n1_ml * A0)
        R_p1_ml = L / (s_p1_ml * A0)
        term_den = (2.0 * (alpha_eff1 / alpha_eff) * (R_TEG / R0 + RL_R0) * (R_TEG / R0) +
                    (1.0 + theta) * (R_TEG / R0 + RL_R0)**2 - 2.0 * ZT_avg * (1.0 - theta) +
                    (R_TEG / R0) * ((R_n1_ml + R_p1_ml) / R0))
        if term_den == 0:
            eff = 0.0
        else:
            eff = term_num / term_den
        I_val = alpha_eff * (T_high - T_low) / (R_TEG + RL)
        power = I_val * I_val * RL
        dT = T_high - T_low
        dT_n1 = k_n_eff / k_n1_v * f1 * dT
        dT_n2 = k_n_eff / k_n2_v * f2 * dT
        dT_p1 = k_p_eff / k_p1_v * mu * dT
        dT_p2 = k_p_eff / k_p2_v * (1.0 - mu) * dT
        T_int_n_new = T_high - dT_n1
        T_int_p_new = T_high - dT_p1
        if abs(T_int_n_new - T_int_n) < 1e-4 and abs(T_int_p_new - T_int_p) < 1e-4:
            break
        T_int_n = T_int_n_new
        T_int_p = T_int_p_new
    return eff, power, I_val

def compute_unseg_power(theta, a, RL_R0, ctx, mat):
    T_low = ctx['T_low']
    T_high = T_low / theta
    A0 = ctx['A0']
    L = ctx['L']
    R0 = ctx['R0']
    T_avg = (T_high + T_low) / 2.0
    if mat == 1:
        k_n_u = k_n1(T_avg); k_p_u = k_p1(T_avg)
        a_n_u = alpha_n1(T_avg); a_p_u = alpha_p1(T_avg)
        s_n_u = sigma_n1(T_avg); s_p_u = sigma_p1(T_avg)
    else:
        k_n_u = k_n2(T_avg); k_p_u = k_p2(T_avg)
        a_n_u = alpha_n2(T_avg); a_p_u = alpha_p2(T_avg)
        s_n_u = sigma_n2(T_avg); s_p_u = sigma_p2(T_avg)
    if abs(a) > 1e-12:
        ea = math.exp(a); ema = math.exp(-a)
        factor = (1.0 - ema) * (ea - 1.0) / (a * a)
    else:
        factor = 1.0
    k_n_eff_u = k_n_u / factor
    R_n = ((1.0 - ema) * L / (a * a * A0)) * (ea - 1.0) / s_n_u if abs(a) > 1e-12 else L / (s_n_u * A0)
    R_p = L / (s_p_u * A0)
    R_TEG = R_n + R_p
    alpha_eff = a_p_u - a_n_u
    K_eff = (k_n_eff_u + k_p_u) * A0 / L
    ZT_avg = (alpha_eff * alpha_eff) * T_high * (1.0 + theta) / (2.0 * R_TEG * K_eff)
    RL = RL_R0 * R0
    I_val = alpha_eff * (T_high - T_low) / (R_TEG + RL)
    power = I_val * I_val * RL
    return power


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
    A0 = 16e-6
    L = 0.004
    T_low = 300.0
    # Reference properties at 273 K
    k_n1_273 = k_n1(273.0)
    sigma_n1_273 = sigma_n1(273.0)
    R0 = L / (sigma_n1_273 * A0)
    K0 = k_n1_273 * A0 / L
    ctx = {"A0": A0, "L": L, "T_low": T_low, "R0": R0, "K0": K0}
    return ctx


# === block: score_0 (check id='eff') ===
def score_0(artifact, step, ctx):
    tol = step.get("tolerance_relative", 0.05)
    rows = artifact
    total = len(rows)
    if total == 0:
        return 0.0
    ok = 0
    for r in rows:
        try:
            theta = float(r["theta"])
            RL_R0 = int(r["RL_R0"])
            a_val = float(r["a"])
            agent_val = float(r["efficiency_percent"]) / 100.0
            eff, _, _ = compute_teg_one(theta, a_val, RL_R0, ctx)
            if eff == 0.0 and agent_val == 0.0:
                ok += 1
            elif eff != 0.0:
                rel_err = abs(agent_val - eff) / max(1e-12, abs(eff))
                if rel_err <= tol:
                    ok += 1
        except Exception:
            pass
    return ok / total


# === block: score_1 (check id='pow') ===
def score_1(artifact, step, ctx):
    tol = step.get("tolerance_relative", 0.10)
    tol_abs = step.get("tolerance_abs", 1e-9)
    rows = artifact
    total = len(rows)
    if total == 0:
        return 0.0
    ok = 0
    for r in rows:
        try:
            theta = float(r["theta"])
            RL_R0 = int(r["RL_R0"])
            a_val = float(r["a"])
            agent_pow = float(r["power_W"])
            _, pow_calc, _ = compute_teg_one(theta, a_val, RL_R0, ctx)
            if pow_calc == 0.0 and agent_pow == 0.0:
                ok += 1
            elif pow_calc != 0.0:
                rel_err = abs(agent_pow - pow_calc) / max(1e-12, abs(pow_calc))
                if rel_err <= tol or abs(agent_pow - pow_calc) <= tol_abs:
                    ok += 1
        except Exception:
            pass
    return ok / total


# === block: score_2 (check id='cur') ===
def score_2(artifact, step, ctx):
    tol = step.get("tolerance_relative", 0.10)
    tol_abs = step.get("tolerance_abs", 1e-9)
    rows = artifact
    total = len(rows)
    if total == 0:
        return 0.0
    ok = 0
    for r in rows:
        try:
            theta = float(r["theta"])
            RL_R0 = int(r["RL_R0"])
            a_val = float(r["a"])
            agent_cur = float(r["current_A"])
            _, _, cur_calc = compute_teg_one(theta, a_val, RL_R0, ctx)
            if cur_calc == 0.0 and agent_cur == 0.0:
                ok += 1
            elif cur_calc != 0.0:
                rel_err = abs(agent_cur - cur_calc) / max(1e-12, abs(cur_calc))
                if rel_err <= tol or abs(agent_cur - cur_calc) <= tol_abs:
                    ok += 1
        except Exception:
            pass
    return ok / total


# === block: score_3 (check id='wr') ===
def score_3(artifact, step, ctx):
    def compute_unseg_power_iter(theta, a, RL_R0, ctx, mat):
        T_low = ctx['T_low']
        T_high = T_low / theta
        mu = 0.5
        A0 = ctx['A0']
        L = ctx['L']
        R0 = ctx['R0']
        if mat == 1:
            k_n_u = lambda T: k_n1(T)
            k_p_u = lambda T: k_p1(T)
            a_n_u = lambda T: alpha_n1(T)
            a_p_u = lambda T: alpha_p1(T)
            s_n_u = lambda T: sigma_n1(T)
            s_p_u = lambda T: sigma_p1(T)
        else:
            k_n_u = lambda T: k_n2(T)
            k_p_u = lambda T: k_p2(T)
            a_n_u = lambda T: alpha_n2(T)
            a_p_u = lambda T: alpha_p2(T)
            s_n_u = lambda T: sigma_n2(T)
            s_p_u = lambda T: sigma_p2(T)
        T_int_n = (T_high + T_low) / 2.0
        T_int_p = (T_high + T_low) / 2.0
        for _ in range(30):
            T_n1_avg = (T_high + T_int_n) / 2.0
            T_n2_avg = (T_int_n + T_low) / 2.0
            T_p1_avg = (T_high + T_int_p) / 2.0
            T_p2_avg = (T_int_p + T_low) / 2.0
            k_n1_v = k_n_u(T_n1_avg)
            k_n2_v = k_n_u(T_n2_avg)
            k_p1_v = k_p_u(T_p1_avg)
            k_p2_v = k_p_u(T_p2_avg)
            ea = math.exp(a)
            ema = math.exp(-a)
            if abs(a) > 1e-12:
                emu = math.exp(a * mu)
                f1 = (1.0 - ema) * (emu - 1.0) / (a * a)
                f2 = (1.0 - ema) * (ea - emu) / (a * a)
            else:
                f1 = mu
                f2 = 1.0 - mu
            k_n_eff = 1.0 / (f1 / k_n1_v + f2 / k_n2_v)
            k_p_eff = 1.0 / (mu / k_p1_v + (1.0 - mu) / k_p2_v)
            alpha_n_eff = a_n_u(T_n1_avg) * k_n_eff / k_n1_v * f1 + a_n_u(T_n2_avg) * k_n_eff / k_n2_v * f2
            alpha_p_eff = a_p_u(T_p1_avg) * k_p_eff / k_p1_v * mu + a_p_u(T_p2_avg) * k_p_eff / k_p2_v * (1.0 - mu)
            alpha_eff = alpha_p_eff - alpha_n_eff
            s_n1 = s_n_u(T_n1_avg)
            s_n2 = s_n_u(T_n2_avg)
            s_p1 = s_p_u(T_p1_avg)
            s_p2 = s_p_u(T_p2_avg)
            if abs(a) > 1e-12:
                R_n = ((1.0 - ema) * L / (a * a * A0)) * ((emu - 1.0) / s_n1 + (ea - emu) / s_n2)
            else:
                R_n = L * (mu / s_n1 + (1.0 - mu) / s_n2) / A0
            R_p = (1.0 / A0) * (mu * L / s_p1 + (1.0 - mu) * L / s_p2)
            R_TEG = R_n + R_p
            RL = RL_R0 * R0
            I_val = alpha_eff * (T_high - T_low) / (R_TEG + RL)
            power = I_val * I_val * RL
            dT_n1 = k_n_eff / k_n1_v * f1 * (T_high - T_low)
            dT_n2 = k_n_eff / k_n2_v * f2 * (T_high - T_low)
            dT_p1 = k_p_eff / k_p1_v * mu * (T_high - T_low)
            dT_p2 = k_p_eff / k_p2_v * (1.0 - mu) * (T_high - T_low)
            T_int_n_new = T_high - dT_n1
            T_int_p_new = T_high - dT_p1
            if abs(T_int_n_new - T_int_n) < 1e-4 and abs(T_int_p_new - T_int_p) < 1e-4:
                break
            T_int_n = T_int_n_new
            T_int_p = T_int_p_new
        return power

    tol = step.get('tolerance_relative', 0.05)
    rows = artifact
    total = len(rows)
    if total == 0:
        return 0.0
    groups = {}
    for r in rows:
        key = (float(r['theta']), int(r['RL_R0']))
        groups.setdefault(key, []).append(r)
    ok = 0
    for (theta, rl), group in groups.items():
        seg_pows = []
        for r in group:
            a_val = float(r['a'])
            _, pow_seg, _ = compute_teg_one(theta, a_val, rl, ctx)
            seg_pows.append(pow_seg)
        if not seg_pows:
            continue
        Wmax = max(seg_pows)
        for r in group:
            try:
                a_val = float(r['a'])
                agent_xi1 = float(r['xi1'])
                agent_xi2 = float(r['xi2'])
                W1 = compute_unseg_power_iter(theta, a_val, rl, ctx, 1)
                W2 = compute_unseg_power_iter(theta, a_val, rl, ctx, 2)
                xi1_calc = W1 / Wmax if Wmax != 0 else 0.0
                xi2_calc = W2 / Wmax if Wmax != 0 else 0.0
                ok1 = False
                if xi1_calc == 0.0 and agent_xi1 == 0.0:
                    ok1 = True
                elif xi1_calc != 0.0 and abs(agent_xi1 - xi1_calc) / max(1e-12, abs(xi1_calc)) <= tol:
                    ok1 = True
                ok2 = False
                if xi2_calc == 0.0 and agent_xi2 == 0.0:
                    ok2 = True
                elif xi2_calc != 0.0 and abs(agent_xi2 - xi2_calc) / max(1e-12, abs(xi2_calc)) <= tol:
                    ok2 = True
                if ok1 and ok2:
                    ok += 1
            except Exception:
                pass
    return ok / total if total else 0.0


_SCORERS = {
    'eff': score_0,
    'pow': score_1,
    'cur': score_2,
    'wr': score_3,
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
