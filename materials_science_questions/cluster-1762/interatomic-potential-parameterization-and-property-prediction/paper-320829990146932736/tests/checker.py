import os
import json
import csv

# === author imports / helpers ===
import json
import math

# ---------- physical constants (atomic units) ----------
ANG_TO_BOHR = 1.8897259886
Z_STAR = 0.58   # effective charge
# polarizabilities (cm^3) -> van der Waals constants from Slater-Kirkwood
# paper values: C_XX = -390.14, C_XM = -164.40, C_MM = -69.23 (a.u.)
C_XX = -390.14
C_XM = -164.40
C_MM = -69.23

# lattice parameters (Angstrom)
A_ANG = 4.244
C_ANG = 3.430
GAMMA = C_ANG / A_ANG   # 0.808
A_AU = A_ANG * ANG_TO_BOHR
C_AU = C_ANG * ANG_TO_BOHR

# effective charges in a.u. of e (electron charge)
Z_CD = 2.0 * Z_STAR   # 1.16
Z_I  = -Z_STAR        # -0.58

# triangular lattice basis vectors (in a.u.)
A1 = (A_AU, 0.0)
A2 = (0.5 * A_AU, A_AU * math.sqrt(3.0) / 2.0)

# lateral shift for AB stacking (fractional coordinates (1/3, 2/3))
SHIFT = ((1.0/3.0)*A1[0] + (2.0/3.0)*A2[0],
         (1.0/3.0)*A1[1] + (2.0/3.0)*A2[1])

def _lattice_points(radius, shift):
    """Generate in-plane positions of atoms in a triangular lattice within a disc of given radius."""
    n = int(math.ceil(radius / A_AU)) + 2
    points = []
    sx, sy = shift
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            x = i*A1[0] + j*A2[0] + sx
            y = i*A1[1] + j*A2[1] + sy
            if math.hypot(x, y) <= radius:
                points.append((x, y))
    return points

def deltaV_lattice(exponent, vertical_dist, shift, cutoff_radius=40.0):
    """
    Compute ΔV_ss'(m) = (V* - V)_ss' for a given exponent (6 for vdW, 12 for repulsion).
    vertical_dist = m * c (in a.u.)
    shift: lateral shift (x,y) for AB configuration; (0,0) for AA.
    Returns difference of lattice sums: Σ (R_i'^{-exponent}) - Σ (R_i^{-exponent})
    where R_i' includes shift, R_i does not.
    """
    points_same = _lattice_points(cutoff_radius, (0.0, 0.0))
    points_diff = _lattice_points(cutoff_radius, shift)
    def sum_inv(pts):
        total = 0.0
        vd2 = vertical_dist * vertical_dist
        for x, y in pts:
            r = math.sqrt(x*x + y*y + vd2)
            total += r**(-exponent)
        return total
    v_same = sum_inv(points_same)
    v_diff = sum_inv(points_diff)
    return v_diff - v_same

def coulomb_dv(z_s, z_sprime, m):
    """
    Analytic Coulomb ΔV^z_{ss'}(m) in atomic units, keeping first three exponential terms (Eq.13).
    m: interlayer distance in units of c
    """
    coeff = -9.0 * z_s * z_sprime / (C_AU * GAMMA**3)
    term1 = math.exp(-4*math.pi/math.sqrt(3) * GAMMA * m)
    term2 = 0.5 * math.exp(-8*math.pi/math.sqrt(3) * GAMMA * m)
    term3 = (2.0/math.sqrt(7)) * math.exp(-4*math.pi*math.sqrt(7.0/3.0) * GAMMA * m)
    return coeff * (term1 + term2 + term3)

def compute_vdw_contributions():
    """Return dict of ΔV^C for each required m."""
    res = {}
    res['vC_XM_1.5'] = C_XM * deltaV_lattice(6, (3./2.)*C_AU, SHIFT)
    res['vC_XM_2.5'] = C_XM * deltaV_lattice(6, (5./2.)*C_AU, SHIFT)
    res['vC_XX_2'] = C_XX * deltaV_lattice(6, 2.0*C_AU, SHIFT)
    res['vC_MM_2'] = C_MM * deltaV_lattice(6, 2.0*C_AU, SHIFT)
    res['vC_XX_3'] = C_XX * deltaV_lattice(6, 3.0*C_AU, SHIFT)
    return res

def compute_repulsive_coeffs():
    """Return dict of f_{ss'}(m) = ΔV^B_{ss'}(m)/B_{ss'} for exponent 12."""
    res = {}
    res['f_XM_1.5'] = deltaV_lattice(12, (3./2.)*C_AU, SHIFT)
    res['f_XM_2.5'] = deltaV_lattice(12, (5./2.)*C_AU, SHIFT)
    res['f_XX_2'] = deltaV_lattice(12, 2.0*C_AU, SHIFT)
    res['f_MM_2'] = deltaV_lattice(12, 2.0*C_AU, SHIFT)
    res['f_XX_3'] = deltaV_lattice(12, 3.0*C_AU, SHIFT)
    return res

def compute_coulomb_contributions():
    """Return dict of ΔV^z for each required m."""
    res = {}
    res['vz_XM_1.5'] = coulomb_dv(Z_CD, Z_I, 3./2.)
    res['vz_XM_2.5'] = coulomb_dv(Z_CD, Z_I, 5./2.)
    res['vz_XX_2']   = coulomb_dv(Z_I, Z_I, 2.0)
    res['vz_MM_2']   = coulomb_dv(Z_CD, Z_CD, 2.0)
    res['vz_XX_3']   = coulomb_dv(Z_I, Z_I, 3.0)
    return res

def compute_J_from_dV(dV_XM15, dV_XM25, dV_XX2, dV_MM2, dV_XX3):
    """Compute J1, J2, K from ΔV differences (Eq. 3)."""
    J1 = 0.5 * (dV_XM15 - dV_XX2 - 0.5*dV_MM2 + dV_XX3)
    J2 = 0.25 * dV_XX3
    K  = 0.25 * dV_MM2 - 0.5 * dV_XM25
    return J1, J2, K


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


# === block: score_0 (check id='check_coulomb') ===
def score_0(artifact, step, ctx):
    step_fields = step.get('fields', [])
    scores = []
    for fdef in step_fields:
        name = fdef['name']
        gold = fdef['gold']
        tol = fdef.get('tolerance_rel', 0.0)
        val = artifact.get(name)
        err = abs(val - gold) / max(abs(gold), 1e-30) if gold != 0 else abs(val)
        s = 1.0 if err <= tol else 0.0
        scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_1 (check id='check_vdw') ===
def score_1(artifact, step, ctx):
    # recompute van der Waals contributions with a converged lattice sum
    import math, numpy as np

    cutoff = 150.0  # a.u. – sufficient for convergence within 1%
    cv = {
        'vC_XM_1.5': C_XM * deltaV_lattice(6, (3./2.)*C_AU, SHIFT, cutoff_radius=cutoff),
        'vC_XM_2.5': C_XM * deltaV_lattice(6, (5./2.)*C_AU, SHIFT, cutoff_radius=cutoff),
        'vC_XX_2': C_XX * deltaV_lattice(6, 2.0*C_AU, SHIFT, cutoff_radius=cutoff),
        'vC_MM_2': C_MM * deltaV_lattice(6, 2.0*C_AU, SHIFT, cutoff_radius=cutoff),
        'vC_XX_3': C_XX * deltaV_lattice(6, 3.0*C_AU, SHIFT, cutoff_radius=cutoff),
    }
    zv = compute_coulomb_contributions()
    d_XM15 = zv['vz_XM_1.5'] + cv['vC_XM_1.5']
    d_XM25 = zv['vz_XM_2.5'] + cv['vC_XM_2.5']
    d_XX2  = zv['vz_XX_2']  + cv['vC_XX_2']
    d_MM2  = zv['vz_MM_2']  + cv['vC_MM_2']
    d_XX3  = zv['vz_XX_3']  + cv['vC_XX_3']
    J1, J2, K = compute_J_from_dV(d_XM15, d_XM25, d_XX2, d_MM2, d_XX3)
    expected = {
        'J1_a.u.': J1,
        'J2_a.u.': J2,
        'K_a.u.': K,
        'J2_over_J1': J2 / J1 if J1 != 0 else 0.0,
        'K_over_J1': K / J1 if J1 != 0 else 0.0,
    }
    field_names = step.get('fields', [])
    tol = step.get('tolerance_rel', 0.01)
    scores = []
    for name in field_names:
        val = artifact.get(name)
        target = expected.get(name)
        if target is None:
            scores.append(0.0)
        else:
            err = abs(val - target) / max(abs(target), 1e-30) if target != 0 else abs(val)
            s = 1.0 if err <= tol else 0.0
            scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_2 (check id='check_full') ===
def score_2(artifact, step, ctx):
    step_fields = step.get('fields', [])
    scores = []
    for fdef in step_fields:
        name = fdef['name']
        gold = fdef['gold']
        val = artifact.get(name)
        if 'tolerance_abs' in fdef:
            tol_abs = fdef['tolerance_abs']
            s = 1.0 if abs(val - gold) <= tol_abs else 0.0
        else:
            tol_rel = fdef.get('tolerance_rel', 0.01)
            err = abs(val - gold) / max(abs(gold), 1e-30) if gold != 0 else abs(val)
            s = 1.0 if err <= tol_rel else 0.0
        scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


_SCORERS = {
    'check_coulomb': score_0,
    'check_vdw': score_1,
    'check_full': score_2,
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
