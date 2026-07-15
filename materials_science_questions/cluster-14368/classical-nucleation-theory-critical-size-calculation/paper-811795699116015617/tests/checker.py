import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    # Validate artifact keys
    required = ['dry_diameters_nm', 'Sc_kohler_pct', 'Sdel_lower_pct', 'Sdel_upper_pct', 'gamma_w', 'crossover_diameter_nm']
    for k in required:
        if k not in artifact:
            return 0.0
    if abs(artifact['gamma_w'] - 0.990) > 1e-9:
        return 0.0

    d_list = artifact['dry_diameters_nm']
    sc = artifact['Sc_kohler_pct']
    sl = artifact['Sdel_lower_pct']
    su = artifact['Sdel_upper_pct']
    cross = artifact['crossover_diameter_nm']

    if len(d_list) < 2:
        return 0.0
    if len(d_list) != len(sc) or len(d_list) != len(sl) or len(d_list) != len(su):
        return 0.0

    # ---------- Constants ----------
    R = 8.314
    M_w = 0.018
    rho_w = 1000.0
    sigma_w = 0.072
    T = 298.15
    M_aa = 0.14614
    rho_aa = 1360.0
    a_sz = 0.0106
    b_sz = 11.836
    gamma_w_del = 0.990
    sigma_del_low = 0.060
    sigma_del_high = 0.072
    sigma_del_mid = 0.066

    # ---------- Helper functions ----------
    def compute_S_pct(d_nm, sigma_use=None):
        d_d = d_nm * 1e-9
        def S_pct_for_dp(d_p):
            V_dry = math.pi / 6.0 * d_d**3
            m_aa = V_dry * rho_aa
            n_aa = m_aa / M_aa
            V_drop = math.pi / 6.0 * d_p**3
            m_w = V_drop * rho_w - m_aa
            if m_w <= 0:
                return -1e9
            n_w = m_w / M_w
            x_w = n_w / (n_w + n_aa)
            C = (n_aa * 6.0) / m_w
            if sigma_use is None:
                sigma = sigma_w - a_sz * T * math.log(1.0 + b_sz * C)
                if sigma < 0:
                    sigma = 0.0
            else:
                sigma = sigma_use
            kelvin = (4.0 * M_w * sigma) / (R * T * rho_w * d_p)
            S_w = x_w * math.exp(kelvin)
            return (S_w - 1.0) * 100.0

        if sigma_use is not None:
            kelvin = (4.0 * M_w * sigma_use) / (d_d * rho_w * R * T)
            S_w_del = gamma_w_del * math.exp(kelvin)
            return (S_w_del - 1.0) * 100.0

        # Golden-section search for maximum of S_pct_for_dp
        a = d_d * 1.001
        b = d_d * 20.0
        phi = (math.sqrt(5.0) - 1.0) / 2.0
        resphi = 2.0 - phi
        c = a + resphi * (b - a)
        d = a + phi * (b - a)
        fc = S_pct_for_dp(c)
        fd = S_pct_for_dp(d)
        tol_d = d_d * 1e-6
        while (b - a) > tol_d:
            if fc > fd:
                b = d
                d = c
                fd = fc
                c = a + resphi * (b - a)
                fc = S_pct_for_dp(c)
            else:
                a = c
                c = d
                fc = fd
                d = a + phi * (b - a)
                fd = S_pct_for_dp(d)
        x_max = 0.5 * (a + b)
        return S_pct_for_dp(x_max)

    # ---------- Recompute reference values at agent's diameters ----------
    ref_sc = []
    ref_sl = []
    ref_su = []
    for d_nm in d_list:
        ref_sc.append(compute_S_pct(d_nm, sigma_use=None))
        ref_sl.append(compute_S_pct(d_nm, sigma_use=sigma_del_low))
        ref_su.append(compute_S_pct(d_nm, sigma_use=sigma_del_high))

    # ---------- Compute reference crossover diameter ----------
    def f_cross(d_nm):
        return compute_S_pct(d_nm, sigma_use=None) - compute_S_pct(d_nm, sigma_use=sigma_del_mid)

    a_c = 50.0
    b_c = 300.0
    fa = f_cross(a_c)
    fb = f_cross(b_c)
    ref_cross = None
    if fa * fb <= 0:
        while (b_c - a_c) > 1e-6:
            mid = (a_c + b_c) / 2.0
            fmid = f_cross(mid)
            if fa * fmid <= 0:
                b_c = mid
                fb = fmid
            else:
                a_c = mid
                fa = fmid
        ref_cross = (a_c + b_c) / 2.0

    # ---------- Compare and score ----------
    tols = step.get('tolerances', {})
    # enforce a reasonable minimum absolute tolerance (0.01% for supersaturation, 5 nm for crossover)
    tol_sc = max(tols.get('Sc_atol', 0.01), 0.01)
    tol_sl = max(tols.get('Sdel_atol', 0.01), 0.01)
    tol_su = max(tols.get('Sdel_atol', 0.01), 0.01)
    tol_cross = max(tols.get('crossover_atol', 5.0), 5.0)

    max_err_sc = max(abs(ref_sc[i] - sc[i]) for i in range(len(sc)))
    max_err_sl = max(abs(ref_sl[i] - sl[i]) for i in range(len(sl)))
    max_err_su = max(abs(ref_su[i] - su[i]) for i in range(len(su)))

    def score_from_maxerr(max_err, tol):
        if max_err <= tol:
            return 1.0
        decay = tol * 10.0
        score = 1.0 - (max_err - tol) / decay
        return max(0.0, score)

    score_sc = score_from_maxerr(max_err_sc, tol_sc)
    score_sl = score_from_maxerr(max_err_sl, tol_sl)
    score_su = score_from_maxerr(max_err_su, tol_su)

    if ref_cross is not None:
        cross_err = abs(cross - ref_cross)
        score_cross = score_from_maxerr(cross_err, tol_cross)
    else:
        score_cross = 0.0

    weights = step.get('scoring_weights', {'Sc': 0.25, 'Sdel_lower': 0.25, 'Sdel_upper': 0.25, 'crossover': 0.25})
    total = weights['Sc'] * score_sc + weights['Sdel_lower'] * score_sl + weights['Sdel_upper'] * score_su + weights['crossover'] * score_cross
    return total


_SCORERS = {
    'step_01': score_0,
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
