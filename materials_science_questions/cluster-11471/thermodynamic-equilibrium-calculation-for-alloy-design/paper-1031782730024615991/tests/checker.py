import os
import json
import csv

# === author imports / helpers ===
import json, math

def eval_quad(x, coeffs):
    return coeffs[0] + coeffs[1]*x + coeffs[2]*x*x

def eval_alloy_T0(t0, wSi, wCu, wMn, wCr, wP):
    base = t0['const'] + t0['Si']*wSi + t0['Si2']*wSi*wSi
    base += (t0['Cu'] + t0['Cu_Si']*wSi + t0['Cu_Si2']*wSi*wSi) * wCu
    base += (t0['Mn'] + t0['Mn_Si']*wSi) * wMn
    base += t0['Cr'] * wCr + t0['P'] * wP
    return base

def eval_alloy_mC(mc, wSi, wCu):
    base = mc['const'] + mc['Si']*wSi + mc['Si2']*wSi*wSi
    base += (mc['Cu'] + mc['Cu_Si']*wSi + mc['Cu_Si2']*wSi*wSi) * wCu
    return base

def eval_eutectic_numer(numer, wSi, wCu, wMn, wCr, wP):
    # numer order: [c00, c10, c20, c01, c11, c21, c02, c12, c03, c04]
    v = numer[0] + numer[1]*wSi + numer[2]*wSi*wSi
    v += (numer[3] + numer[4]*wSi + numer[5]*wSi*wSi) * wCu
    v += (numer[6] + numer[7]*wSi) * wMn
    v += numer[8] * wCr + numer[9] * wP
    return v

def eval_eutectic_denom(denom, wSi, wCu):
    # denom order: [d00, d10, d20, d01, d11, d21]
    v = denom[0] + denom[1]*wSi + denom[2]*wSi*wSi
    v += (denom[3] + denom[4]*wSi + denom[5]*wSi*wSi) * wCu
    return v


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


# === block: score_0 (check id='ternary_coefficients') ===
def score_0(artifact, step, ctx):
    try:
        data = artifact
        T0_g = data['T0_gamma']
        mC_g = data['mC_gamma']
        T0_gra = data['T0_gra']
        mC_gra = data['mC_gra']
        tests = step.get('test_data',{}).get('ternary_test_points',[])
        tol_g = step['test_data']['tolerance_T_gamma']
        tol_gr = step['test_data']['tolerance_T_gra']
        ok = 0
        for p in tests:
            wSi = p['wSi']
            wC = p['wC']
            Tlg = eval_quad(wSi, T0_g) + eval_quad(wSi, mC_g)*wC
            Tlgr = eval_quad(wSi, T0_gra) + eval_quad(wSi, mC_gra)*wC
            if abs(Tlg - p['T_L_gamma_gold']) <= tol_g:
                ok += 1
            if abs(Tlgr - p['T_L_gra_gold']) <= tol_gr:
                ok += 1
        total = len(tests)*2
        return ok / total if total>0 else 0.0
    except Exception:
        return 0.0


# === block: score_1 (check id='alloy_coefficients') ===
def score_1(artifact, step, ctx):
    try:
        data = artifact
        t0 = data['T0_gamma_alloy']
        mc = data['mC_gamma_alloy']
        t0_gra = data['T0_gra_alloy']
        mC_gra_coefs = step['test_data']['mC_gra_ternary_coefs']
        tests = step.get('test_data',{}).get('alloy_test_configs',[])
        tol_g = step['test_data']['tolerance_gamma']
        tol_gr = step['test_data']['tolerance_gra']
        ok = 0
        for p in tests:
            wSi = p['wSi']
            wCu = p['wCu']
            wMn = p['wMn']
            wCr = p['wCr']
            wP = p['wP']
            wC = p['wC']
            Tlg = eval_alloy_T0(t0, wSi, wCu, wMn, wCr, wP) + eval_alloy_mC(mc, wSi, wCu)*wC
            T0g_val = eval_quad(wSi, mC_gra_coefs)
            # graphite T0_gra using alloy T0_gra_alloy
            t0_gra_val = t0_gra['const'] + t0_gra['Si']*wSi + t0_gra['Si2']*wSi*wSi
            t0_gra_val += t0_gra['Cu']*wCu + t0_gra['Mn']*wMn + t0_gra['Cr']*wCr + t0_gra['P']*wP
            Tlgr = t0_gra_val + T0g_val * wC
            if abs(Tlg - p['T_L_gamma_gold']) <= tol_g:
                ok += 1
            if abs(Tlgr - p['T_L_gra_gold']) <= tol_gr:
                ok += 1
        total = len(tests)*2
        return ok / total if total>0 else 0.0
    except Exception:
        return 0.0


# === block: score_2 (check id='eutectic_relation') ===
def score_2(artifact, step, ctx):
    try:
        data = artifact
        num = data['numerator_coefficients']
        den = data['denominator_coefficients']
        tests = step.get('test_data',{}).get('eutectic_test_points',[])
        tol = step['test_data']['tolerance']
        ok = 0
        for p in tests:
            wSi = p['wSi']
            wCu = p['wCu']
            wMn = p['wMn']
            wCr = p['wCr']
            wP = p['wP']
            nval = eval_eutectic_numer(num, wSi, wCu, wMn, wCr, wP)
            dval = eval_eutectic_denom(den, wSi, wCu)
            if dval != 0:
                wC_eut = 4.333 * nval / dval
                if abs(wC_eut - p['wC_eut_gold']) <= tol:
                    ok += 1
        return ok / len(tests) if tests else 0.0
    except Exception:
        return 0.0


# === block: score_3 (check id='ce_approximation') ===
def score_3(artifact, step, ctx):
    try:
        data = artifact
        wC_arr = data['wC_eut_approx']
        CE_arr = data['CE_approx']
        tests = step.get('test_data',{}).get('approx_test_points',[])
        tol_wc = step['test_data']['tolerance_wC']
        tol_ce = step['test_data']['tolerance_CE']
        ok = 0
        total = 0
        for p in tests:
            wSi = p['wSi']
            wCu = p['wCu']
            wCr = p['wCr']
            wP = p['wP']
            wC_eut_val = wC_arr[0] + wC_arr[1]*wSi + wC_arr[2]*wSi*wSi + wC_arr[3]*wCu + wC_arr[4]*wCr + wC_arr[5]*wP
            ce_val = CE_arr[0]*wSi + CE_arr[1]*wSi*wSi + CE_arr[2]*wCu + CE_arr[3]*wCr + CE_arr[4]*wP
            if abs(wC_eut_val - p['wC_eut_gold']) <= tol_wc:
                ok += 1
            if abs(ce_val - p['CE_gold']) <= tol_ce:
                ok += 1
            total += 2
        return ok / total if total>0 else 0.0
    except Exception:
        return 0.0


# === block: score_4 (check id='partition_coefficient') ===
def score_4(artifact, step, ctx):
    try:
        data = artifact
        tests = step.get('test_data',{})
        tol = tests.get('tolerance_k',0.03)
        ok = 0
        total = 0
        # k_C
        kC = data['k_C']
        for p in tests['k_C_points']:
            wSi = p['wSi']
            dT = p['dT']
            val = kC['const'] + kC['Si']*wSi + (kC['dT'] + kC['Si_dT']*wSi)*dT + kC['dT2']*dT*dT
            if abs(val - p['gold']) <= tol:
                ok += 1
            total += 1
        # k_Si
        kSi = data['k_Si']
        for p in tests['k_Si_points']:
            wSi = p['wSi']
            dT = p['dT']
            val = kSi['const'] + kSi['Si']*wSi + (kSi['dT'] + kSi['Si_dT']*wSi)*dT
            if abs(val - p['gold']) <= tol:
                ok += 1
            total += 1
        # k_Cu
        kCu = data['k_Cu']
        for p in tests['k_Cu_points']:
            wSi = p['wSi']
            dT = p['dT']
            val = kCu['const'] + kCu['Si']*wSi + (kCu['dT'] + kCu['Si_dT']*wSi)*dT
            if abs(val - p['gold']) <= tol:
                ok += 1
            total += 1
        # k_Mn
        kMn = data['k_Mn']
        for p in tests['k_Mn_points']:
            wSi = p['wSi']
            dT = p['dT']
            val = kMn['const'] + kMn['Si']*wSi + (kMn['dT'] + kMn['Si2_dT']*wSi*wSi)*dT
            if abs(val - p['gold']) <= tol:
                ok += 1
            total += 1
        # k_Cr
        kCr = data['k_Cr']
        for p in tests['k_Cr_points']:
            dT = p['dT']
            val = kCr['const'] + kCr['dT']*dT
            if abs(val - p['gold']) <= tol:
                ok += 1
            total += 1
        # k_P
        kP = data['k_P']
        for p in tests['k_P_points']:
            dT = p['dT']
            val = kP['const'] + kP['dT']*dT
            if abs(val - p['gold']) <= tol:
                ok += 1
            total += 1
        return ok / total if total>0 else 0.0
    except Exception:
        return 0.0


_SCORERS = {
    'ternary_coefficients': score_0,
    'alloy_coefficients': score_1,
    'eutectic_relation': score_2,
    'ce_approximation': score_3,
    'partition_coefficient': score_4,
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
