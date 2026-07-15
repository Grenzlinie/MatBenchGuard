import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, math


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
    # No shared precomputation needed
    return {}


# === block: score_0 (check id='step_binary_eutectic') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    row = artifact[0]
    T = float(row.get('eutectic_temperature_K', float('nan')))
    x = float(row.get('eutectic_Zn_mole_fraction', float('nan')))
    T_ref = step.get('reference_eutectic_temperature_K')
    x_ref = step.get('reference_eutectic_Zn_mole_fraction')
    if T_ref is None or x_ref is None:
        return 0.0
    dT = abs(T - T_ref)
    dx = abs(x - x_ref)
    if dT <= step.get('tolerance_temp_full', 5.0) and dx <= step.get('tolerance_comp_full', 0.01):
        return 1.0
    elif dT <= step.get('tolerance_temp_partial', 10.0) and dx <= step.get('tolerance_comp_partial', 0.02):
        return 0.6
    else:
        return 0.0


# === block: score_1 (check id='step_ternary_liquidus') ===
def score_1(artifact, step, ctx):
    mole_fracs = step.get('mole_fractions_ZnSe', [])
    if not artifact or not mole_fracs:
        return 0.0
    agent = {}
    for row in artifact:
        try:
            x = float(row['mole_fraction_ZnSe'])
            T = float(row['temperature_K'])
            agent[x] = T
        except:
            pass

    R = 8.314e-3  # kJ/(mol K)
    T_F_ZnSe = 1788.0
    S_F_ZnSe = 4.47e-3  # kJ/(K mol)
    G_solid = lambda T: S_F_ZnSe * (T - T_F_ZnSe)

    def G_liq(x1, x2, T):
        x3 = 1 - x1 - x2
        if x3 <= 0 or x1 <= 0 or x2 <= 0:
            return 0.0
        # ideal
        G_id = R*T*(x1*math.log(x1)+x2*math.log(x2)+x3*math.log(x3))
        # Zn-Sn
        d12 = x1 - x2
        H12 = x1*x2*(2.360 + 0.907*d12 + 0.216*d12*d12)*4.184
        S12 = x1*x2*(1.42 + 0.58*d12 + 0.12*d12*d12)*4.184/1000.0*T
        # Zn-Se (x1, x3)
        d13 = x1 - x3
        H13 = x1*x3*(17.663 - 8.782*d13 + 8.525*d13*d13)*4.184
        S13 = x1*x3*(4.10 - 0.73*d13)*4.184/1000.0*T
        # Sn-Se (x2, x3)
        d23 = x2 - x3
        H23 = x2*x3*(5.086 + 2.936*d23 - 3.846*d23*d23)*4.184
        S23 = x2*x3*(-0.05 + 0.63*d23)*4.184/1000.0*T
        # ternary
        alpha_Zn = 2742*4.184
        alpha_Sn = 3787*4.184
        alpha_Se = -3885*4.184
        beta_Zn = -60.6*4.184
        beta_Sn = 2.9*4.184
        beta_Se = 55.8*4.184
        tsum = x1*x2*x3*( (alpha_Zn*x1+alpha_Sn*x2+alpha_Se*x3) - T*(beta_Zn*x1+beta_Sn*x2+beta_Se*x3) )
        return G_id + H12 - S12 + H13 - S13 + H23 - S23 + tsum

    def mu_sum(x1, x2, T):
        h = 1e-6
        G = G_liq(x1, x2, T)
        Gp1 = G_liq(x1+h, x2, T)
        Gm1 = G_liq(x1-h, x2, T)
        g1 = (Gp1 - Gm1)/(2*h)
        Gp2 = G_liq(x1, x2+h, T)
        Gm2 = G_liq(x1, x2-h, T)
        g2 = (Gp2 - Gm2)/(2*h)
        mu1 = G + (1-x1)*g1 - x2*g2
        mu3 = G - x1*g1 - x2*g2
        return mu1 + mu3

    def liquidus_T(y):
        x2 = 1 - 2*y
        if x2 <= 0 or y <= 0:
            return 0.0
        f = lambda T: mu_sum(y, x2, T) - G_solid(T)
        lo, hi = 800.0, 1500.0
        if f(lo) * f(hi) > 0:
            # widen
            lo, hi = 600.0, 2000.0
        for _ in range(60):
            mid = (lo+hi)/2
            fm = f(mid)
            if abs(fm) < 1e-5:
                return mid
            if f(lo)*fm <= 0:
                hi = mid
            else:
                lo = mid
        return (lo+hi)/2

    sq = 0.0
    cnt = 0
    for xr in mole_fracs:
        if xr not in agent:
            return 0.0
        T_pred = agent[xr]
        T_exp = liquidus_T(xr)
        sq += (T_pred - T_exp)**2
        cnt += 1
    if cnt == 0:
        return 0.0
    rmse = math.sqrt(sq/cnt)
    if rmse <= step.get('rmse_full_credit', 15.0):
        return 1.0
    elif rmse <= step.get('rmse_partial_credit', 30.0):
        return 0.7
    elif rmse <= 50.0:
        return 0.3
    else:
        return 0.0


_SCORERS = {
    'step_binary_eutectic': score_0,
    'step_ternary_liquidus': score_1,
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
