import os
import json
import csv

# === author imports / helpers ===
import csv
import math

# Masses (g/mol) of the supercell compositions
MASS_PRISTINE = 24*47.867 + 8*26.9815 + 16*12.0107   # Ti3AlC2 (48 atoms)
MASS_SUBST = 23*47.867 + 1*178.49 + 8*26.9815 + 16*12.0107   # Ti23Hf1
MASS_INTER = 24*47.867 + 8*26.9815 + 16*12.0107 + 1*178.49   # +1 Hf
NATOMS_PRISTINE = 48
NATOMS_SUBST = 48
NATOMS_INTER = 49

MASS_DICT = {
    'pristine_TAC_results.csv': MASS_PRISTINE,
    'Hf_substitutional_TAC_results.csv': MASS_SUBST,
    'Hf_interstitial_TAC_results.csv': MASS_INTER
}
NATOMS_DICT = {
    'pristine_TAC_results.csv': NATOMS_PRISTINE,
    'Hf_substitutional_TAC_results.csv': NATOMS_SUBST,
    'Hf_interstitial_TAC_results.csv': NATOMS_INTER
}

def invert_3x3_symmetric(m):
    """Explicit inversion of a symmetric 3x3 matrix."""
    a11,a12,a13,a21,a22,a23,a31,a32,a33 = m[0][0],m[1][0],m[2][0],m[0][1],m[1][1],m[2][1],m[0][2],m[1][2],m[2][2]
    # Actually the matrix is:
    # [ a11  a12  a13 ]
    # [ a12  a22  a23 ]
    # [ a13  a23  a33 ]
    # Compute determinant
    det = (a11 * (a22*a33 - a23*a23)
           - a12 * (a12*a33 - a23*a13)
           + a13 * (a12*a23 - a22*a13))
    if abs(det) < 1e-12:
        raise ValueError('Singular matrix')
    inv11 =  (a22*a33 - a23*a23) / det
    inv22 =  (a11*a33 - a13*a13) / det
    inv33 =  (a11*a22 - a12*a12) / det
    inv12 = -(a12*a33 - a13*a23) / det
    inv13 =  (a12*a23 - a13*a22) / det
    inv23 = -(a11*a23 - a12*a13) / det
    return [[inv11, inv12, inv13],
            [inv12, inv22, inv23],
            [inv13, inv23, inv33]]

def compute_derived(row, mass_total_g, n_atoms):
    a = float(row['a0_Ang'])
    c = float(row['c0_Ang'])
    mag = float(row['mag_moment_muB'])
    C11 = float(row['C11_GPa'])
    C12 = float(row['C12_GPa'])
    C13 = float(row['C13_GPa'])
    C33 = float(row['C33_GPa'])
    C44 = float(row['C44_GPa'])
    V = (math.sqrt(3.0)/2.0) * a * a * c   # A^3
    dens_gcm3 = mass_total_g / (V * 0.6022)
    dens_kgm3 = dens_gcm3 * 1000.0
    C66 = (C11 - C12) / 2.0
    # Voigt bulk
    B_V = (2.0/9.0) * (C11 + C12 + 2.0*C13 + 0.5*C33)
    # Reuss bulk
    M_denom = C11 + C12 + 2.0*C33 - 4.0*C13
    C2 = (C11 + C12)*C33 - 2.0*C13*C13
    B_R = C2 / M_denom
    B = (B_V + B_R) / 2.0
    # Voigt shear
    G_V = (1.0/30.0) * (M_denom + 12.0*C44 + 12.0*C66)
    # Reuss shear via compliance matrix inversion
    M3 = [[C11, C12, C13],
          [C12, C11, C13],
          [C13, C13, C33]]
    S = invert_3x3_symmetric(M3)
    S11 = S[0][0]
    S12 = S[0][1]
    S13 = S[0][2]
    S33 = S[2][2]
    S44 = 1.0/C44
    S66 = 1.0/C66
    inv_GR = (4.0/5.0)*(2.0*S44 + S66) + (1.0/5.0)*(2.0*S11 + S33 - 2.0*S12 - 2.0*S13)
    G_R = 1.0 / inv_GR
    G = (G_V + G_R) / 2.0
    E_mod = 9.0*B*G / (3.0*B + G)
    nu = E_mod/(2.0*G) - 1.0
    vt = 1000.0 * math.sqrt(G / dens_gcm3)
    vl = 1000.0 * math.sqrt((B + 4.0*G/3.0) / dens_gcm3)
    vm = ((2.0/vt**3 + 1.0/vl**3)/3.0) ** (-1.0/3.0)
    h_over_k = 4.799243073366221e-11
    N_A = 6.02214076e23
    M_kgpmol = mass_total_g * 1.0e-3
    prefactor = (3.0 * n_atoms * N_A * dens_kgm3 / (4.0 * math.pi * M_kgpmol)) ** (1.0/3.0)
    Theta_D = h_over_k * prefactor * vm
    return {'mag':mag, 'B':B, 'G':G, 'E':E_mod, 'nu':nu, 'vt':vt, 'vl':vl, 'vm':vm, 'Theta_D':Theta_D, 'a':a, 'c':c, 'V':V, 'dens_gcm3':dens_gcm3}

def rel_score(val, target, tol_rel):
    if target == 0.0:
        return 1.0 if abs(val) < 1e-6 else 0.0
    err = abs(val - target) / abs(target)
    if err <= tol_rel:
        return 1.0
    else:
        return max(0.0, 1.0 - (err - tol_rel) / tol_rel)

def score_derived(artifact_rows, step, ctx):
    if not artifact_rows or len(artifact_rows)==0:
        return 0.0
    row = artifact_rows[0]
    fname = step['output_file']
    mass_info = MASS_DICT.get(fname, 0)
    n_atoms = NATOMS_DICT.get(fname, 0)
    if mass_info == 0:
        return 0.0
    try:
        deriv = compute_derived(row, mass_info, n_atoms)
    except Exception as e:
        return 0.0
    gold = step['gold']
    tol_mod = step['tol_rel_moduli']
    tol_debye = step['tol_rel_debye']
    tol_mag = step['tol_abs_mag']
    sB = rel_score(deriv['B'], gold['B'], tol_mod)
    sG = rel_score(deriv['G'], gold['G'], tol_mod)
    sE = rel_score(deriv['E'], gold['E'], tol_mod)
    sTheta = rel_score(deriv['Theta_D'], gold['Theta_D'], tol_debye)
    sMag = 1.0 if abs(deriv['mag'] - gold['mag']) <= tol_mag else max(0.0, 1.0 - (abs(deriv['mag']-gold['mag'])-tol_mag)/tol_mag)
    base = 0.3*sB + 0.3*sG + 0.2*sE + 0.1*sTheta + 0.1*sMag
    # Trend checks
    step_id = step['id']
    pristine_derived = ctx.get('pristine_derived')
    if pristine_derived is None:
        trend = 0.0
    else:
        if step_id == 'step_1':
            trend = 1.0
        elif step_id == 'step_2':
            within = 0
            for key in ['B','G','E','Theta_D']:
                if abs(deriv[key] - pristine_derived[key]) / pristine_derived[key] <= 0.05:
                    within += 1
            trend = within / 4.0
        elif step_id == 'step_3':
            good = 0
            for key in ['B','G','E','Theta_D']:
                if (pristine_derived[key] - deriv[key]) / pristine_derived[key] > 0.10:
                    good += 1
            trend = good / 4.0
        else:
            trend = 1.0
    return 0.8 * base + 0.2 * trend


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
    artifacts = {}
    for step in spec.get('steps', []):
        fname = step.get('output_file', '')
        if fname:
            path = os.path.join(outputs_dir, fname)
            if os.path.exists(path):
                with open(path, newline='') as f:
                    reader = csv.DictReader(f)
                    rows = list(reader)
                    if rows:
                        artifacts[fname] = rows
    pristine_derived = None
    if 'pristine_TAC_results.csv' in artifacts and artifacts['pristine_TAC_results.csv']:
        mass = MASS_PRINTINE = 1556.8405
        n_atoms = 48
        row = artifacts['pristine_TAC_results.csv'][0]
        try:
            pristine_derived = compute_derived(row, mass, n_atoms)
        except:
            pristine_derived = None
    ctx = {}
    ctx['artifacts'] = artifacts
    ctx['pristine_derived'] = pristine_derived
    return ctx


# === block: score_0 (check id='step_1') ===
def score_0(artifact, step, ctx):
    art = ctx.get('artifacts', {}).get('pristine_TAC_results.csv', [])
    return score_derived(art, step, ctx)


# === block: score_1 (check id='step_2') ===
def score_1(artifact, step, ctx):
    art = ctx.get('artifacts', {}).get('Hf_substitutional_TAC_results.csv', [])
    return score_derived(art, step, ctx)


# === block: score_2 (check id='step_3') ===
def score_2(artifact, step, ctx):
    art = ctx.get('artifacts', {}).get('Hf_interstitial_TAC_results.csv', [])
    return score_derived(art, step, ctx)


_SCORERS = {
    'step_1': score_0,
    'step_2': score_1,
    'step_3': score_2,
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
