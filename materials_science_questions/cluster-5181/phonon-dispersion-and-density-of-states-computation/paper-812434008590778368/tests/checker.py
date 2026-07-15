import os
import json
import csv

# === author imports / helpers ===
import math

def compute_dynamical_matrix(kx, ky, kz, R=0.8):
    a = 1.0
    c2x = math.cos(2*kx)
    c2y = math.cos(2*ky)
    c2z = math.cos(2*kz)
    cx = math.cos(kx)
    sx = math.sin(kx)
    cy = math.cos(ky)
    sy = math.sin(ky)
    cz = math.cos(kz)
    sz = math.sin(kz)
    delta = 1.0 + 0.75*R - cx*cy*cz
    A = delta - 0.75*R * c2x
    B = delta - 0.75*R * c2y
    C = delta - 0.75*R * c2z
    E = sx * sy * cz
    F = sx * cy * sz
    G = cx * sy * sz
    return A, B, C, E, F, G

def real_cbrt(x):
    """Real cube root."""
    if x >= 0:
        return x ** (1./3.)
    else:
        return -((-x) ** (1./3.))

def cardan_solve(A, B, C, E, F, G):
    P = -(A+B+C)
    Q = A*B + B*C + C*A - E**2 - F**2 - G**2
    R = -A*B*C - 2*E*F*G + A*G**2 + B*F**2 + C*E**2
    p = Q - (1./3.)*P**2
    q = (2./27.)*P**3 - (1./3.)*P*Q + R
    T = 0.25*q**2 + (1./27.)*p**3
    eps = 1e-9
    if T > eps:
        raise ValueError('T > 1e-9 encountered, unphysical')
    if abs(T) < eps:
        y = -q/2.
        y_cube = real_cbrt(y)
        omega2 = [
            2 * y_cube - P/3.,
            -y_cube - P/3.,
            -y_cube - P/3.
        ]
    else:
        a = -q/2.
        b = math.sqrt(-T)
        r = math.sqrt(a**2 + b**2)
        theta = math.atan2(b, a)
        r13 = r**(1./3.)
        root1 = 2 * r13 * math.cos(theta/3.) - P/3.
        root2 = 2 * r13 * math.cos((theta + 2*math.pi)/3.) - P/3.
        root3 = 2 * r13 * math.cos((theta + 4*math.pi)/3.) - P/3.
        omega2 = [root1, root2, root3]
    omega2.sort(reverse=True)
    return omega2, T

def compute_omegas_100(kxs):
    omegas = []
    Ts = []
    for kx in kxs:
        A, B, C, E, F, G = compute_dynamical_matrix(kx, 0.0, 0.0)
        omega2, T = cardan_solve(A, B, C, E, F, G)
        omegas.append(omega2)
        Ts.append(T)
    return omegas, Ts

def compute_omegas_nonsym(ks):
    omegas = []
    Ts = []
    for kx, ky, kz in ks:
        A, B, C, E, F, G = compute_dynamical_matrix(kx, ky, kz)
        omega2, T = cardan_solve(A, B, C, E, F, G)
        omegas.append(omega2)
        Ts.append(T)
    return omegas, Ts


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


# === block: score_0 (check id='step02_dispersion_100') ===
def score_0(artifact, step, ctx):
    kxs = [float(row['kx']) for row in artifact]
    ref_omegas, ref_Ts = compute_omegas_100(kxs)
    tol = float(step.get('tolerance_relative', 1e-6))
    n_correct = 0
    for i, row in enumerate(artifact):
        agent_omega = [float(row['omega2_1']), float(row['omega2_2']), float(row['omega2_3'])]
        agent_T = float(row['T'])
        ref_omg = ref_omegas[i]
        ref_T = ref_Ts[i]
        match = True
        for j in range(3):
            ref_val = ref_omg[j]
            ag_val = agent_omega[j]
            denom = max(abs(ref_val), 1e-12)
            if abs(ag_val - ref_val) > tol * denom:
                match = False
                break
        denom_T = max(abs(ref_T), 1e-12)
        if abs(agent_T - ref_T) > tol * denom_T:
            match = False
        if match:
            n_correct += 1
    return n_correct / max(len(artifact), 1)


# === block: score_1 (check id='step03_dispersion_nonsym') ===
def score_1(artifact, step, ctx):
    ks = [(float(row['kx']), float(row['ky']), float(row['kz'])) for row in artifact]
    ref_omegas, ref_Ts = compute_omegas_nonsym(ks)
    tol = float(step.get('tolerance_relative', 1e-6))
    n_correct = 0
    for i, row in enumerate(artifact):
        agent_omega = [float(row['omega2_1']), float(row['omega2_2']), float(row['omega2_3'])]
        agent_T = float(row['T'])
        ref_omg = ref_omegas[i]
        ref_T = ref_Ts[i]
        match = True
        for j in range(3):
            ref_val = ref_omg[j]
            ag_val = agent_omega[j]
            denom = max(abs(ref_val), 1e-12)
            if abs(ag_val - ref_val) > tol * denom:
                match = False
                break
        denom_T = max(abs(ref_T), 1e-12)
        if abs(agent_T - ref_T) > tol * denom_T:
            match = False
        if match:
            n_correct += 1
    return n_correct / max(len(artifact), 1)


_SCORERS = {
    'step02_dispersion_100': score_0,
    'step03_dispersion_nonsym': score_1,
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
