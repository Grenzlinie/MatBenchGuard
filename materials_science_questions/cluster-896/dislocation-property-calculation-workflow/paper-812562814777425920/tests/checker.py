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
    import math

    R_J = 8.314
    P_TT = 14.2
    Q_P = 9.4
    P_TN = 12.3
    R_OVER_P = 0.0

    els = {
        'Cu': {'phi':4.55, 'nws':1.47, 'Vm':7.11,  'G':48,  'K':140, 'Tm':1358, 'M':63.546,  'Z':1},
        'Cr': {'phi':4.65, 'nws':1.73, 'Vm':7.23,  'G':80,  'K':160, 'Tm':2180, 'M':51.996,  'Z':6},
        'Mo': {'phi':4.60, 'nws':1.77, 'Vm':9.40,  'G':120, 'K':230, 'Tm':2896, 'M':95.94,   'Z':6},
        'Ti': {'phi':3.80, 'nws':1.47, 'Vm':10.64, 'G':44,  'K':110, 'Tm':1941, 'M':47.867,  'Z':4},
        'Ta': {'phi':4.05, 'nws':1.63, 'Vm':10.90, 'G':69,  'K':200, 'Tm':3290, 'M':180.947, 'Z':5},
        'Sn': {'phi':4.15, 'nws':1.24, 'Vm':16.30, 'G':18.4,'K':58,  'Tm':505,  'M':118.71,  'Z':4},
        'Nb': {'phi':4.05, 'nws':1.62, 'Vm':10.80, 'G':38,  'K':170, 'Tm':2750, 'M':92.91,   'Z':5},
        'Co': {'phi':5.10, 'nws':1.75, 'Vm':6.67,  'G':76,  'K':180, 'Tm':1768, 'M':58.933,  'Z':9}
    }

    def is_transition(sym):
        return sym != 'Sn'

    def chemical(xA, xB, eA, eB, M):
        Vm2_3A = eA['Vm'] ** (2/3)
        Vm2_3B = eB['Vm'] ** (2/3)
        nws_invA = eA['nws'] ** (-1/3)
        nws_invB = eB['nws'] ** (-1/3)
        CAS = xA * Vm2_3A / (xA * Vm2_3A + xB * Vm2_3B)
        CBS = 1 - CAS
        f_CS = CAS * CBS
        VA = eA['Vm']
        VB = eB['Vm']
        denom_S = xA**2 * VA + xB**2 * VB
        Sx = 1 - M * xA * xB * abs(VA - VB) / denom_S if denom_S != 0 else 1
        num = xA * Vm2_3A + xB * Vm2_3B
        denom_n = nws_invA + nws_invB
        dphi = eA['phi'] - eB['phi']
        dnws = eA['nws'] - eB['nws']
        bracket = - dphi**2 + Q_P * dnws**2 - R_OVER_P
        P_val = P_TT if (is_transition(eA) and is_transition(eB)) else P_TN
        return 2 * P_val * f_CS * Sx * num / denom_n * bracket

    def elastic(xA, xB, eA, eB):
        VA = eA['Vm']
        VB = eB['Vm']
        KA = eA['K']
        GA = eA['G']
        KB = eB['K']
        GB = eB['G']
        denom_AB = 3*KA*VB + 4*GB*VA
        dE_A_in_B = (2*KA*GB*(VB-VA)**2)/denom_AB if denom_AB != 0 else 0
        denom_BA = 3*KB*VA + 4*GA*VB
        dE_B_in_A = (2*KB*GA*(VA-VB)**2)/denom_BA if denom_BA != 0 else 0
        return xA * xB * (xA * dE_A_in_B + xB * dE_B_in_A)

    def structural(xA, xB, eA, eB):
        return 0.0

    def binary_mix(xA, xB, eA, eB, M=1):
        return chemical(xA, xB, eA, eB, M) + elastic(xA, xB, eA, eB) + structural(xA, xB, eA, eB)

    def hillert(x1, x2, x3, e1, e2, e3, M, include_elastic=True):
        dH_AB = chemical(x1, 1-x1, e1, e2, M) + (elastic(x1, 1-x1, e1, e2) if include_elastic else 0)
        dH_AC = chemical(x1, 1-x1, e1, e3, M) + (elastic(x1, 1-x1, e1, e3) if include_elastic else 0)
        C_BC = (1 + x2 - x3) / 2
        C_CB = (1 + x3 - x2) / 2
        dH_BC = chemical(C_BC, C_CB, e2, e3, M) + (elastic(C_BC, C_CB, e2, e3) if include_elastic else 0)
        H = (x2/(1-x1)) * dH_AB + (x3/(1-x1)) * dH_AC + (x2*x3/(C_BC*C_CB)) * dH_BC
        return H

    def S_config(*xs):
        s = 0.0
        for x in xs:
            if x > 0:
                s -= x * math.log(x)
        return s * R_J

    x_Cu1, x_Cr, x_Mo = 0.86, 0.07, 0.07
    T1 = 298
    H_mix_1 = hillert(x_Cu1, x_Cr, x_Mo, els['Cu'], els['Cr'], els['Mo'], M=1, include_elastic=True)
    S1 = S_config(x_Cu1, x_Cr, x_Mo)
    dGm_CuCrMo = H_mix_1 - T1 * S1 / 1000

    x_Ti, x_Ta, x_Sn = 0.75, 0.13, 0.12
    T2 = 298
    H_mix_ss = hillert(x_Ti, x_Ta, x_Sn, els['Ti'], els['Ta'], els['Sn'], M=1, include_elastic=True)
    S2 = S_config(x_Ti, x_Ta, x_Sn)
    dGm_TiTaSn = H_mix_ss - T2 * S2 / 1000
    H_chem_am = hillert(x_Ti, x_Ta, x_Sn, els['Ti'], els['Ta'], els['Sn'], M=1, include_elastic=False)
    H_topo = 3.5 * (x_Ti*els['Ti']['Tm'] + x_Ta*els['Ta']['Tm'] + x_Sn*els['Sn']['Tm']) / 1000
    H_am = H_chem_am + H_topo
    dGam_TiTaSn = H_am - T2 * S2 / 1000

    x_Cu3, x_Nb, x_Co = 0.86, 0.07, 0.07
    T3 = 298
    H_mix_3 = hillert(x_Cu3, x_Nb, x_Co, els['Cu'], els['Nb'], els['Co'], M=1, include_elastic=True)
    S3 = S_config(x_Cu3, x_Nb, x_Co)
    dGm_CuNbCo = H_mix_3 - T3 * S3 / 1000
    Hf = hillert(x_Cu3, x_Nb, x_Co, els['Cu'], els['Nb'], els['Co'], M=2, include_elastic=False)

    M_Cu = els['Cu']['M']
    M_Cr = els['Cr']['M']
    w_Cu = 0.5
    w_Cr = 0.5
    mol_Cu = 50 / M_Cu
    mol_Cr = 50 / M_Cr
    tot = mol_Cu + mol_Cr
    x_Cu_4 = mol_Cu / tot
    x_Cr_4 = mol_Cr / tot
    H_mix_4 = binary_mix(x_Cu_4, x_Cr_4, els['Cu'], els['Cr'], M=1)
    S4 = S_config(x_Cu_4, x_Cr_4)
    dGm_298 = H_mix_4 - 298 * S4 / 1000
    dGm_503 = H_mix_4 - 503 * S4 / 1000
    rho_m = 0.15
    omega = 628
    M_avg_g = x_Cu_4 * M_Cu + x_Cr_4 * M_Cr
    M_avg_kg = M_avg_g / 1000.0
    G_ef_J = 0.5 * M_avg_kg * rho_m**2 * omega**2
    G_ef = G_ef_J / 1000.0
    dGm_453_no = H_mix_4 - 453 * S4 / 1000
    dGm_cf_453 = dGm_453_no - G_ef
    dGm_cf_503 = dGm_503 - G_ef

    ref = {
        "Cu_7Cr_7Mo": {"dGm": dGm_CuCrMo},
        "Ti_13Ta_12Sn": {"dGm": dGm_TiTaSn, "dGam": dGam_TiTaSn},
        "Cu_7Nb_7Co": {"dGm": dGm_CuNbCo, "dHf": Hf},
        "Cu_50Cr": {
            "dGm_298K": dGm_298,
            "dGm_503K": dGm_503,
            "dGm_cf_453K": dGm_cf_453,
            "dGm_cf_503K": dGm_cf_503
        }
    }
    return {"reference": ref}


# === block: score_0 (check id='compute_target_properties') ===
def score_0(artifact, step, ctx):
    import math

    # Use a larger tolerance to absorb differences from structural enthalpy term
    # since the reference may neglect it while the solver includes it as per instructions.
    tol = 0.5  # kJ/mol
    ref = ctx.get("reference")
    if ref is None:
        return 0.0

    entries = [
        ("Cu_7Cr_7Mo", "dGm"),
        ("Ti_13Ta_12Sn", "dGm"),
        ("Ti_13Ta_12Sn", "dGam"),
        ("Cu_7Nb_7Co", "dGm"),
        ("Cu_7Nb_7Co", "dHf"),
        ("Cu_50Cr", "dGm_298K"),
        ("Cu_50Cr", "dGm_503K"),
        ("Cu_50Cr", "dGm_cf_453K"),
        ("Cu_50Cr", "dGm_cf_503K")
    ]
    total = len(entries)
    correct = 0
    for sys, field in entries:
        try:
            agent_val = artifact[sys][field]
            ref_val = ref[sys][field]
            if abs(agent_val - ref_val) <= tol:
                correct += 1
        except (KeyError, TypeError):
            pass
    return correct / total


_SCORERS = {
    'compute_target_properties': score_0,
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
