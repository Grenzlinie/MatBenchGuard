import os
import json
import csv

# === author imports / helpers ===
import mpmath as mp
import json, csv, os, math

mp.mp.dps = 50

# Bernoulli and Euler numbers
def bernoulli(n):
    return mp.bernoulli(n)

def euler_num(n):
    return mp.eulernum(n)

# Diagonal ratio (eq 1)
def diagonal_ratio(m):
    return mp.gamma(m)**2 / (mp.gamma(m-0.5) * mp.gamma(m+0.5))

def compute_diagonal_exact(Mmax):
    diag = [mp.mpf(1)]
    for m in range(1, Mmax+1):
        r = diagonal_ratio(m)
        diag.append(diag[-1] * r)
    return diag

def compute_next_diag_exact(Mmax, ch, sh2):
    nd = []
    for m in range(0, Mmax):
        c_diag = compute_diagonal_exact(m+1)[-1]
        val = c_diag * ch * mp.hyp2f1(0.5, m+1, m+1.5, -sh2)
        nd.append(val)
    return nd

def fill_matrix_symmetric(max_n, ch, sh2):
    C = [[mp.mpf(0)]*(max_n+1) for _ in range(max_n+1)]
    diag = compute_diagonal_exact(max_n)
    for m in range(max_n+1):
        C[m][m] = diag[m]
    nd = compute_next_diag_exact(max_n, ch, sh2)
    for m in range(max_n):
        C[m][m+1] = nd[m]
        C[m+1][m] = nd[m]
    for n in range(2, max_n+1):
        for m in range(0, n):
            if m == n-1:
                continue
            c_nm2 = C[m][n-2] if m <= n-2 else C[n-2][m]
            c_nm1 = C[m][n-1] if m <= n-1 else C[n-1][m]
            mm1 = abs(m-1)
            mp1 = m+1
            # C(m±1, n-1) using reflection symmetry
            c_mm1 = C[mm1][n-1]
            if mp1 <= n-1:
                c_mp1 = C[mp1][n-1]
            else:
                c_mp1 = C[n-1][mp1]
            val = (2 * c_nm1**2 - c_mm1 * c_mp1) / c_nm2
            C[m][n] = val
            C[n][m] = val
    return C


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


# === block: score_0 (check id='step_01_exact_symmetric') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # list of dict rows
    ch = mp.sqrt(2)
    sh2 = mp.mpf(1)
    max_n = 5
    C_ref = fill_matrix_symmetric(max_n, ch, sh2)
    tol = float(step.get('tolerance_abs', 1e-12))
    count = 0
    total = 0
    for row in artifact:
        M = int(row['M'])
        N = int(row['N'])
        if 0 <= M <= max_n and 0 <= N <= max_n and M <= N:
            val_ref = float(C_ref[M][N])
            diff = abs(float(row['C']) - val_ref)
            total += 1
            if diff <= tol:
                count += 1
    return count / total if total > 0 else 0.0


# === block: score_1 (check id='step_02_diagonal_asymptotic') ===
def score_1(artifact, step, ctx):
    artifact = artifact
    tol = float(step.get('tolerance_abs', 1e-8))
    Kmax = 30
    count = 0
    total = 0
    for row in artifact:
        M = int(row['M'])
        if M < 1 or M > 20:
            continue
        total += 1
        diag = compute_diagonal_exact(M)
        lnC_exact_ref = mp.log(diag[M])
        # asymptotic series
        A = mp.power(2, mp.mpf(1)/12) * mp.exp(3 * mp.zeta(-1))
        lnA = mp.log(A)
        s = mp.mpf(0)
        for k in range(2, Kmax+1):
            B2k = bernoulli(2*k)
            term = ((2**(2*k) - 1) * B2k) / (k * (k-1) * 2**(2*k) * M**(2*k-2))
            if term == 0:
                break
            s += term
        lnC_asymp_ref = lnA - mp.mpf(0.25) * mp.log(M) + s
        agent_exact = float(row['lnC_exact'])
        agent_asymp = float(row['lnC_asymp'])
        ok_exact = abs(agent_exact - float(lnC_exact_ref)) <= tol
        ok_asymp = abs(agent_asymp - float(lnC_asymp_ref)) <= tol
        if ok_exact and ok_asymp:
            count += 1
    return count / total if total > 0 else 0.0


# === block: score_2 (check id='step_03_nextdiagonal_asymptotic') ===
def score_2(artifact, step, ctx):
    artifact = artifact
    tol = float(step.get('tolerance_abs', 1e-8))
    ch = mp.sqrt(2)
    sh2 = mp.mpf(1)
    Kmax = 30
    count = 0
    total = 0
    for row in artifact:
        M = int(row['M'])
        if M < 1 or M > 20:
            continue
        total += 1
        # exact next-diag
        diag_next = compute_diagonal_exact(M+1)[-1]
        val_exact = diag_next * ch * mp.hyp2f1(0.5, M+1, M+1.5, -sh2)
        lnC_exact_ref = mp.log(val_exact)
        # asymptotic lnC(M,M)
        A = mp.power(2, mp.mpf(1)/12) * mp.exp(3 * mp.zeta(-1))
        lnA = mp.log(A)
        s_diag = mp.mpf(0)
        for k in range(2, Kmax+1):
            B2k = bernoulli(2*k)
            term = ((2**(2*k) - 1) * B2k) / (k * (k-1) * 2**(2*k) * M**(2*k-2))
            if term == 0:
                break
            s_diag += term
        lnCmm = lnA - mp.mpf(0.25) * mp.log(M) + s_diag
        # odd series (eq 7)
        s_odd = mp.mpf(0)
        for k in range(1, Kmax+1):
            B2k = bernoulli(2*k)
            term = ((2**(2*k) - 1) * (2**(2*k-1) - 1) * B2k) / (2*k * (2*k-1) * (2*M)**(2*k - 1))
            if term == 0:
                break
            s_odd += term
        lnC_asymp_ref = lnCmm - s_odd
        agent_exact = float(row['lnC_exact'])
        agent_asymp = float(row['lnC_asymp'])
        if abs(agent_exact - float(lnC_exact_ref)) <= tol and abs(agent_asymp - float(lnC_asymp_ref)) <= tol:
            count += 1
    return count / total if total > 0 else 0.0


# === block: score_3 (check id='step_04_anisotropic_coefficients') ===
def score_3(artifact, step, ctx):
    artifact = artifact
    tol = float(step.get('tolerance_abs', 1e-12))
    count = 0
    total = 0
    for entry in artifact:
        alpha = float(entry['alpha'])
        theta = float(entry['theta'])
        total += 1
        u = mp.cos(2*alpha)
        A1_ref = mp.power(2, -8) * (-1 + 3*mp.cos(4*theta) - 6*u*mp.cos(2*theta))
        A2_ref = mp.power(2, -13) * (5 + 36*mp.cos(4*theta) + 63*mp.cos(8*theta)
                + 18*u*mp.cos(2*theta) - 162*u*mp.cos(6*theta) + 72*u**2*mp.cos(4*theta))
        A3_ref = mp.power(3, -1) * mp.power(2, -19) * (
                -524 - 324*mp.cos(4*theta) + 24732*mp.cos(8*theta) + 28884*mp.cos(12*theta)
                - 1566*u*mp.cos(2*theta) - 24003*u*mp.cos(6*theta) - 95679*u*mp.cos(10*theta)
                - 486*u**2 - 3672*u**2*mp.cos(4*theta) + 83358*u**2*mp.cos(8*theta)
                - 15072*u**3*mp.cos(6*theta))
        ok = (abs(float(entry['A1']) - float(A1_ref)) <= tol and
              abs(float(entry['A2']) - float(A2_ref)) <= tol and
              abs(float(entry['A3']) - float(A3_ref)) <= tol)
        if ok:
            count += 1
    return count / total if total > 0 else 0.0


_SCORERS = {
    'step_01_exact_symmetric': score_0,
    'step_02_diagonal_asymptotic': score_1,
    'step_03_nextdiagonal_asymptotic': score_2,
    'step_04_anisotropic_coefficients': score_3,
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
