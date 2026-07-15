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
    k_file = os.path.join(outputs_dir, 'fitted_k_coefficients.json')
    k_artifact = load_artifact(k_file)
    ref_k = None
    deviation_threshold = None
    steps = spec.get('steps', [])
    for s in steps:
        if s['id'] == 'step_fit_k':
            ref_k = s.get('reference')
        if s['id'] == 'step_deviation':
            deviation_threshold = s.get('threshold')
    return {'k_values': k_artifact, 'ref_k': ref_k, 'deviation_threshold': deviation_threshold}


# === block: score_0 (check id='step_fit_k') ===
def score_0(artifact, step, ctx):
    import os
    import json

    # Model coefficients for the four orientations (100), (110), (111), (210)
    # A = (h2k2 + k2l2 + l2h2) / (h2+k2+l2)^2
    # B = (h2 k2 l2) / (h2+k2+l2)^3
    # C = (h2k2 + k2l2 + l2h2)^2 / (h2+k2+l2)^4
    ORIENTATIONS = [
        (1, 0, 0, 0.0, 0.0, 0.0),   # (100)
        (1, 1, 0, 1.0/4.0, 0.0, 1.0/16.0),  # (110): h2=1,k2=1,l2=0 -> A=1*1+1*0+0*1=1, denom=4^2=16 -> 1/16? Wait need correct formula
        # Let's derive carefully.
    ]
    # Let's precompute using formulas from Eq. (8):
    # h,k,l as integers, square sum s = h2+k2+l2.
    # A = (h2*k2 + k2*l2 + l2*h2) / s^2
    # B = (h2*k2*l2) / s^3
    # C = (h2*k2 + k2*l2 + l2*h2)^2 / s^4

    def _coeff(h, k, l):
        h2 = h*h; k2 = k*k; l2 = l*l
        s = h2 + k2 + l2
        A = (h2*k2 + k2*l2 + l2*h2) / (s*s)
        B = (h2*k2*l2) / (s*s*s)
        C = A * A  # because numerator^2 / s^4 = (A*s^2)^2 / s^4 = A^2
        return A, B, C

    A1,B1,C1 = _coeff(1,0,0)  # (1,0,0)
    A2,B2,C2 = _coeff(1,1,0)  # (1,1,0)
    A3,B3,C3 = _coeff(1,1,1)  # (1,1,1)
    A4,B4,C4 = _coeff(2,1,0)  # (2,1,0)

    # Gaussian elimination solver for 4x4
    def _solve_4x4(M, rhs):
        n = 4
        a = [row[:] for row in M]
        b = rhs[:]
        for col in range(n-1):
            # pivot
            max_row = max(range(col, n), key=lambda r: abs(a[r][col]))
            if max_row != col:
                a[col], a[max_row] = a[max_row], a[col]
                b[col], b[max_row] = b[max_row], b[col]
            if abs(a[col][col]) < 1e-12:
                return None
            for row in range(col+1, n):
                factor = a[row][col] / a[col][col]
                for j in range(col, n):
                    a[row][j] -= factor * a[col][j]
                b[row] -= factor * b[col]
        for col in range(n-1, -1, -1):
            for row in range(col-1, -1, -1):
                factor = a[row][col] / a[col][col]
                for j in range(col, n):
                    a[row][j] -= factor * a[col][j]
                b[row] -= factor * b[col]
        x = [0.0] * n
        for i in range(n):
            if abs(a[i][i]) < 1e-12:
                return None
            x[i] = b[i] / a[i][i]
        return x

    # Load surface energies
    se_path = os.path.join('/app/outputs', 'surface_energies.json')
    try:
        with open(se_path) as f:
            se_data = json.load(f)
    except Exception:
        return 0.0

    # Extract energies for the four orientations (order matters)
    # Try common key formats
    def get_en(data, keys):
        if isinstance(data, dict):
            for k in keys:
                if k in data:
                    return float(data[k])
        return None

    energies = [
        get_en(se_data, ('100','(100)','[100]')),
        get_en(se_data, ('110','(110)','[110]')),
        get_en(se_data, ('111','(111)','[111]')),
        get_en(se_data, ('210','(210)','[210]')),
    ]
    if any(e is None for e in energies):
        return 0.0

    # Build 4x4 system: row_i = [1, A_i, B_i, C_i]
    M = [
        [1.0, A1, B1, C1],
        [1.0, A2, B2, C2],
        [1.0, A3, B3, C3],
        [1.0, A4, B4, C4],
    ]
    k_ref = _solve_4x4(M, energies)
    if k_ref is None:
        return 0.0

    # Agent's coefficients
    if not isinstance(artifact, dict):
        return 0.0
    try:
        k0 = float(artifact['k0'])
        k1 = float(artifact['k1'])
        k2 = float(artifact['k2'])
        k3 = float(artifact['k3'])
    except Exception:
        return 0.0

    # Compare
    tol = 1e-6
    diffs = [
        abs(k0 - k_ref[0]),
        abs(k1 - k_ref[1]),
        abs(k2 - k_ref[2]),
        abs(k3 - k_ref[3]),
    ]
    if max(diffs) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step_epsilon') ===
def score_1(artifact, step, ctx):
    k = ctx.get('k_values')
    if not k or not isinstance(artifact, dict):
        return 0.0
    eps0 = artifact.get('epsilon0')
    eps1 = artifact.get('epsilon1')
    eps2 = artifact.get('epsilon2')
    eps3 = artifact.get('epsilon3')
    if None in (eps0, eps1, eps2, eps3):
        return 0.0
    k0_erg = k['k0']
    k1 = k['k1']
    k2 = k['k2']
    k3 = k['k3']
    k0_J = k0_erg * 0.001
    lam = 14.3e-9
    lam0 = math.sqrt(3 * lam / 1.1)
    eps0_exp = lam0 * math.sqrt(k0_J)
    r1_exp = k1 / (2 * k0_erg)
    r2_exp = k2 / (2 * k0_erg)
    r3_exp = (k3 / (2 * k0_erg)) - (k1**2) / (8 * k0_erg**2)
    r1_agent = eps1 / eps0
    r2_agent = eps2 / eps0
    r3_agent = eps3 / eps0
    tol_eps0_rel = step.get('tolerance_eps0_relative', 0.05)
    tol_ratio_abs = step.get('tolerance_ratio_absolute', 0.05)
    s_eps0 = max(0.0, 1.0 - abs(eps0 - eps0_exp) / (tol_eps0_rel * abs(eps0_exp))) if eps0_exp != 0 else 0.0
    s_r1 = max(0.0, 1.0 - abs(r1_agent - r1_exp) / tol_ratio_abs)
    s_r2 = max(0.0, 1.0 - abs(r2_agent - r2_exp) / tol_ratio_abs)
    s_r3 = max(0.0, 1.0 - abs(r3_agent - r3_exp) / tol_ratio_abs)
    total = 0.5 * s_eps0 + 0.5 * ((s_r1 + s_r2 + s_r3) / 3.0)
    return min(1.0, max(0.0, total))


# === block: score_2 (check id='step_deviation') ===
def score_2(artifact, step, ctx):
    dev = None
    try:
        if isinstance(artifact, str):
            dev = float(artifact.strip())
        else:
            dev = float(artifact)
    except Exception:
        return 0.0
    threshold = ctx.get('deviation_threshold', 5.0)
    decay = step.get('decay_max', 10.0)
    if dev <= threshold:
        return 1.0
    score = max(0.0, 1.0 - (dev - threshold) / decay)
    return round(score, 4)


_SCORERS = {
    'step_fit_k': score_0,
    'step_epsilon': score_1,
    'step_deviation': score_2,
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
