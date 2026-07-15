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
    def prepare(outputs_dir, spec):
        # equilibrium constants from Table 4
        K_DATA = {
            2000: (1.867e-6, 4.595, 3.986),
            2250: (7.255e-5, 5.430, 2.368),
            2500: (1.431e-3, 6.088, 1.571),
            2750: (1.418e-2, 6.650, 1.123),
            3000: (1.143e-1, 7.090, 1.123),
            3500: (2.385, 7.420, 0.8522),
        }
        # fuel parameters
        H_C_fuel = 0.155
        N_C_fuel = 0.001
        M_C = 12.011
        M_H2 = 2.01594
        M_N2 = 28.016
        M_O2 = 32.0
        M_Ar = 39.948
        N2_O2_air = 3.3103
        Ar_O2_air = 0.0552
        a_H2 = H_C_fuel * M_C / M_H2
        P_On = 1.0 + N2_O2_air * M_O2 / M_N2 + Ar_O2_air * M_O2 / M_Ar
        k_NC = (M_C / M_N2) * N_C_fuel

        def compute_n(alpha_k, KpCO2, Kpw, KpOH, p):
            if alpha_k <= 0.0 or alpha_k >= 1.0:
                return None
            beta_k = alpha_k / (1.0 - alpha_k)
            KpCO2_p = KpCO2 / p
            denom_h1 = (a_H2/2.0) * (beta_k**2 - KpCO2_p)
            if abs(denom_h1) < 1e-16:
                return None
            h1 = (KpCO2_p * P_On - beta_k**2) / denom_h1
            denom_h2 = beta_k**2 - KpCO2_p
            if abs(denom_h2) < 1e-16:
                return None
            h2 = (beta_k**2 + KpCO2_p) / denom_h2
            h3 = -alpha_k / a_H2 + h2 + (beta_k**2 + KpCO2_p * k_NC) / ((a_H2/2.0)*denom_h2)
            Kpw_beta = Kpw / beta_k
            common_denom_h4 = 1.0 + h2 * (Kpw_beta + 1.0)
            if abs(common_denom_h4) < 1e-16:
                return None
            h4 = -h1 * (Kpw_beta + 1.0) / common_denom_h4
            h5 = (1.0 - h3 * (Kpw_beta + 1.0)) / common_denom_h4
            h6 = h1 / common_denom_h4
            h7 = (h2 + h3) / common_denom_h4
            h8 = 1.0 + (a_H2/2.0) * (h6 - h4)
            h9 = (a_H2/2.0) * (h7 - h5) + alpha_k/2.0 - a_H2/2.0 - 1.0
            h10 = 8.0 * a_H2 * KpOH * h4 * h5
            h11 = h7*h8 + h6*h9
            h12 = h7*h8 - h6*h9
            h13 = 16.0 * a_H2 * KpOH * h6 * ((Kpw_beta + 1.0)*h6*h9 + h5*h8)
            h14 = 2.0 * (1.0 + a_H2/2.0) * (h6*h8 - 4.0*a_H2*KpOH*h4**2)
            if h14 == 0:
                return None
            disc = h12**2 + h13
            if disc < 0:
                return None
            n_val = (h10 - h11 - math.sqrt(disc)) / h14
            return n_val

        def compute_aw_ah(alpha_k, n, KpCO2, Kpw, KpOH, p):
            beta_k = alpha_k / (1.0 - alpha_k)
            KpCO2_p = KpCO2 / p
            denom_h1 = (a_H2/2.0) * (beta_k**2 - KpCO2_p)
            if abs(denom_h1) < 1e-16:
                return None, None
            h1 = (KpCO2_p * P_On - beta_k**2) / denom_h1
            denom_h2 = beta_k**2 - KpCO2_p
            if abs(denom_h2) < 1e-16:
                return None, None
            h2 = (beta_k**2 + KpCO2_p) / denom_h2
            h3 = -alpha_k / a_H2 + h2 + (beta_k**2 + KpCO2_p * k_NC) / ((a_H2/2.0)*denom_h2)
            Kpw_beta = Kpw / beta_k
            common_denom_h4 = 1.0 + h2 * (Kpw_beta + 1.0)
            if abs(common_denom_h4) < 1e-16:
                return None, None
            h4 = -h1 * (Kpw_beta + 1.0) / common_denom_h4
            h5 = (1.0 - h3 * (Kpw_beta + 1.0)) / common_denom_h4
            h6 = h1 / common_denom_h4
            h7 = (h2 + h3) / common_denom_h4
            aw = n * (1.0 + a_H2/2.0) * h6 + h7
            ah = n * (1.0 + a_H2/2.0) * h4 + h5
            return aw, ah

        def solve_alpha_for_n(n_target, KpCO2, Kpw, KpOH, p):
            lo = 1e-12
            hi = 0.9999
            for _ in range(100):
                mid = (lo+hi)/2.0
                n_val = compute_n(mid, KpCO2, Kpw, KpOH, p)
                if n_val is None:
                    if mid < 0.5: lo = mid
                    else: hi = mid
                    continue
                if abs(n_val - n_target) < 1e-10:
                    return mid
                if n_val < n_target:
                    hi = mid
                else:
                    lo = mid
                if hi-lo < 1e-14:
                    break
            return (lo+hi)/2.0

        T_vals = [2000, 2250, 2500, 2750, 3000, 3500]
        p_dict = {
            2000: [0.05, 0.1, 0.5, 1, 5, 10, 20],
            2250: [0.05, 0.1, 0.5, 1, 5, 10, 20, 50],
            2500: [0.05, 0.1, 0.5, 1, 5, 10, 20, 50, 100],
            2750: [0.1, 0.5, 1, 5, 10, 20, 50, 100],
            3000: [0.1, 0.5, 1, 5, 10, 20, 50, 100, 200],
            3500: [0.1, 0.5, 1, 5, 10, 20, 50, 100, 200],
        }
        n_vals = [1, 1.2, 1.5, 2, 3, 5, 10, float('inf')]

        expected_map = {}
        for T in T_vals:
            KpCO2, Kpw, KpOH = K_DATA[T]
            for p in p_dict[T]:
                for n in n_vals:
                    if n == float('inf'):
                        tmp = math.sqrt((KpCO2/p)*P_On)
                        ak = tmp / (1.0 + tmp)
                        aw = 0.0
                        ah = 1.0
                    else:
                        ak = solve_alpha_for_n(n, KpCO2, Kpw, KpOH, p)
                        aw, ah = compute_aw_ah(ak, n, KpCO2, Kpw, KpOH, p)
                        if aw is None:
                            aw = 0.0
                            ah = 1.0
                    n_str = 'inf' if n == float('inf') else f"{n:.12g}"
                    key = (T, p, n_str)
                    expected_map[key] = (ak, aw, ah)

        return {'expected_map': expected_map}


# === block: score_0 (check id='dissociation_degrees') ===
def score_0(artifact, step, ctx):
    import math

    tolerance_rel = step.get('tolerance_rel', 0.05)
    tolerance_abs = step.get('tolerance_abs', 0.005)

    # Hardcoded equilibrium constants from paper Table 4 (corrected KpOH for 3500 K)
    K_DATA = {
        2000: (1.867e-6, 4.595, 3.986),
        2250: (7.255e-5, 5.430, 2.368),
        2500: (1.431e-3, 6.088, 1.571),
        2750: (1.418e-2, 6.650, 1.123),
        3000: (1.143e-1, 7.090, 1.123),
        3500: (2.385, 7.420, 0.8522),
    }

    # Fuel parameters
    H_C_fuel = 0.155
    N_C_fuel = 0.001
    M_C = 12.011
    M_H2 = 2.01594
    M_N2 = 28.016
    M_O2 = 32.0
    M_Ar = 39.948
    N2_O2_air = 3.3103
    Ar_O2_air = 0.0552

    a_H2 = H_C_fuel * M_C / M_H2
    P_On = 1.0 + N2_O2_air * M_O2 / M_N2 + Ar_O2_air * M_O2 / M_Ar
    k_NC = (M_C / M_N2) * N_C_fuel

    def compute_n(alpha_k, KpCO2, Kpw, KpOH, p):
        if alpha_k <= 0.0 or alpha_k >= 1.0:
            return None
        beta_k = alpha_k / (1.0 - alpha_k)
        KpCO2_p = KpCO2 / p
        denom_h1 = (a_H2/2.0) * (beta_k**2 - KpCO2_p)
        if abs(denom_h1) < 1e-16:
            return None
        h1 = (KpCO2_p * P_On - beta_k**2) / denom_h1
        denom_h2 = beta_k**2 - KpCO2_p
        if abs(denom_h2) < 1e-16:
            return None
        h2 = (beta_k**2 + KpCO2_p) / denom_h2
        h3 = -alpha_k / a_H2 + h2 + (beta_k**2 + KpCO2_p * k_NC) / ((a_H2/2.0)*denom_h2)
        Kpw_beta = Kpw / beta_k
        common_denom_h4 = 1.0 + h2 * (Kpw_beta + 1.0)
        if abs(common_denom_h4) < 1e-16:
            return None
        h4 = -h1 * (Kpw_beta + 1.0) / common_denom_h4
        h5 = (1.0 - h3 * (Kpw_beta + 1.0)) / common_denom_h4
        h6 = h1 / common_denom_h4
        h7 = (h2 + h3) / common_denom_h4
        h8 = 1.0 + (a_H2/2.0) * (h6 - h4)
        h9 = (a_H2/2.0) * (h7 - h5) + alpha_k/2.0 - a_H2/2.0 - 1.0
        h10 = 8.0 * a_H2 * KpOH * h4 * h5
        h11 = h7*h8 + h6*h9
        h12 = h7*h8 - h6*h9
        h13 = 16.0 * a_H2 * KpOH * h6 * ((Kpw_beta + 1.0)*h6*h9 + h5*h8)
        h14 = 2.0 * (1.0 + a_H2/2.0) * (h6*h8 - 4.0*a_H2*KpOH*h4**2)
        if h14 == 0:
            return None
        disc = h12**2 + h13
        if disc < 0:
            return None
        n_val = (h10 - h11 - math.sqrt(disc)) / h14
        return n_val

    def compute_aw_ah(alpha_k, n, KpCO2, Kpw, KpOH, p):
        if alpha_k <= 0.0 or alpha_k >= 1.0:
            return None, None
        beta_k = alpha_k / (1.0 - alpha_k)
        KpCO2_p = KpCO2 / p
        denom_h1 = (a_H2/2.0) * (beta_k**2 - KpCO2_p)
        if abs(denom_h1) < 1e-16:
            return None, None
        h1 = (KpCO2_p * P_On - beta_k**2) / denom_h1
        denom_h2 = beta_k**2 - KpCO2_p
        if abs(denom_h2) < 1e-16:
            return None, None
        h2 = (beta_k**2 + KpCO2_p) / denom_h2
        h3 = -alpha_k / a_H2 + h2 + (beta_k**2 + KpCO2_p * k_NC) / ((a_H2/2.0)*denom_h2)
        Kpw_beta = Kpw / beta_k
        common_denom_h4 = 1.0 + h2 * (Kpw_beta + 1.0)
        if abs(common_denom_h4) < 1e-16:
            return None, None
        h4 = -h1 * (Kpw_beta + 1.0) / common_denom_h4
        h5 = (1.0 - h3 * (Kpw_beta + 1.0)) / common_denom_h4
        h6 = h1 / common_denom_h4
        h7 = (h2 + h3) / common_denom_h4
        aw = n * (1.0 + a_H2/2.0) * h6 + h7
        ah = n * (1.0 + a_H2/2.0) * h4 + h5
        return aw, ah

    def solve_alpha_for_n(n_target, KpCO2, Kpw, KpOH, p):
        lo = 1e-12
        hi = 0.9999
        for _ in range(100):
            mid = (lo+hi)/2.0
            n_val = compute_n(mid, KpCO2, Kpw, KpOH, p)
            if n_val is None:
                if mid < 0.5: lo = mid
                else: hi = mid
                continue
            if abs(n_val - n_target) < 1e-10:
                return mid
            if n_val < n_target:
                hi = mid
            else:
                lo = mid
            if hi-lo < 1e-14:
                break
        return (lo+hi)/2.0

    # Conditions identical to the public contract
    T_vals = [2000, 2250, 2500, 2750, 3000, 3500]
    p_dict = {
        2000: [0.05, 0.1, 0.5, 1, 5, 10, 20],
        2250: [0.05, 0.1, 0.5, 1, 5, 10, 20, 50],
        2500: [0.05, 0.1, 0.5, 1, 5, 10, 20, 50, 100],
        2750: [0.1, 0.5, 1, 5, 10, 20, 50, 100],
        3000: [0.1, 0.5, 1, 5, 10, 20, 50, 100, 200],
        3500: [0.1, 0.5, 1, 5, 10, 20, 50, 100, 200],
    }
    n_vals = [1, 1.2, 1.5, 2, 3, 5, 10, float('inf')]

    expected_map = {}
    for T in T_vals:
        KpCO2, Kpw, KpOH = K_DATA[T]
        for p in p_dict[T]:
            for n in n_vals:
                if n == float('inf'):
                    tmp = math.sqrt((KpCO2/p)*P_On)
                    ak = tmp / (1.0 + tmp)
                    aw = 0.0
                    ah = 1.0
                else:
                    ak = solve_alpha_for_n(n, KpCO2, Kpw, KpOH, p)
                    aw, ah = compute_aw_ah(ak, n, KpCO2, Kpw, KpOH, p)
                    if aw is None:
                        aw = 0.0
                        ah = 1.0
                n_str = 'inf' if n == float('inf') else f"{n:.12g}"
                key = (T, p, n_str)
                expected_map[key] = (ak, aw, ah)

    # Match agent rows
    agent_rows = {}
    for row in artifact:
        try:
            T = float(row['T_K'])
            p = float(row['p_kgcm2'])
            n_raw = row['n'].strip()
            if n_raw.lower() == 'inf':
                n_str = 'inf'
            else:
                n_float = float(n_raw)
                n_str = f"{n_float:.12g}"
        except:
            continue
        try:
            ak = float(row['alpha_k'])
            aw = float(row['alpha_w'])
            ah = float(row['alpha_h'])
        except:
            continue
        agent_rows[(T, p, n_str)] = (ak, aw, ah)

    passed = 0
    total = len(expected_map)
    for key, (exp_ak, exp_aw, exp_ah) in expected_map.items():
        if key not in agent_rows:
            continue
        ak_a, aw_a, ah_a = agent_rows[key]
        ok_ak = abs(ak_a - exp_ak) <= max(tolerance_rel*abs(exp_ak), tolerance_abs)
        ok_aw = abs(aw_a - exp_aw) <= max(tolerance_rel*abs(exp_aw), tolerance_abs)
        ok_ah = abs(ah_a - exp_ah) <= max(tolerance_rel*abs(exp_ah), tolerance_abs)
        if ok_ak and ok_aw and ok_ah:
            passed += 1

    return passed / total if total > 0 else 0.0


_SCORERS = {
    'dissociation_degrees': score_0,
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
