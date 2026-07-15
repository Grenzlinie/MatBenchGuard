import os
import json
import csv

# === author imports / helpers ===
import numpy as np

def bross_bohn_G(qx, qy, qz):
    u = np.pi * qx; v = np.pi * qy; w = np.pi * qz
    if abs(u) < 1e-12 and abs(v) < 1e-12 and abs(w) < 1e-12:
        return 1.0
    if abs(w) < 1e-12 and abs(u - v) < 1e-12:
        w = 1e-10
    A = u*u + v*v + w*w
    def term(a,b,c):
        den1 = (a-b)**2 - c**2
        if abs(den1) < 1e-12:
            den1 = np.sign(den1)*1e-12 if den1 != 0 else 1e-12
        num1 = a + b
        bracket1 = np.sin(a) + np.sin(b) - np.sin((a+b+c)/2) - np.sin((a+b-c)/2)
        t1 = num1 / den1 * bracket1
        den2 = (a+b)**2 - c**2
        if abs(den2) < 1e-12:
            den2 = np.sign(den2)*1e-12 if den2 != 0 else 1e-12
        num2 = a - b
        bracket2 = np.sin(a) - np.sin(b) - np.sin((a+b+c)/2) - np.sin((a-b-c)/2)
        t2 = num2 / den2 * bracket2
        return t1 + t2
    total = term(u,v,w) + term(v,w,u) + term(w,u,v) + term(u,w,v) + term(w,v,u) + term(v,u,w)
    return -2 / A * total

def compute_dynamical_matrix(q, params):
    A1 = params['A1'] * 1e3
    A2 = params['A2'] * 1e3
    a_inv2_K1 = params['a_inv2_K1'] * 1e3
    a_inv2_K2 = params['a_inv2_K2'] * 1e3
    a_Ke = params['a_Ke'] * 1e3
    qx, qy, qz = q
    C1 = np.cos(np.pi * qx); C2 = np.cos(np.pi * qy); C3 = np.cos(np.pi * qz)
    S1 = np.sin(np.pi * qx); S2 = np.sin(np.pi * qy); S3 = np.sin(np.pi * qz)
    G = bross_bohn_G(qx, qy, qz)
    G2 = G * G
    D11 = (2*A1 + 8*(a_inv2_K1 + a_inv2_K2)) * (2 - C1*(C2+C3))
    D11 += 4 * A2 * S1**2
    D11 += -8 * a_inv2_K1 * (2*C1**2 - C2**2 - C3**2)
    D11 += a_Ke * np.pi**2 * qx**2 * G2
    D22 = (2*A1 + 8*(a_inv2_K1 + a_inv2_K2)) * (2 - C2*(C1+C3))
    D22 += 4 * A2 * S2**2
    D22 += -8 * a_inv2_K1 * (2*C2**2 - C1**2 - C3**2)
    D22 += a_Ke * np.pi**2 * qy**2 * G2
    D33 = (2*A1 + 8*(a_inv2_K1 + a_inv2_K2)) * (2 - C3*(C1+C2))
    D33 += 4 * A2 * S3**2
    D33 += -8 * a_inv2_K1 * (2*C3**2 - C1**2 - C2**2)
    D33 += a_Ke * np.pi**2 * qz**2 * G2
    prefactor = (2*A1 - 16*a_inv2_K1)
    D12 = prefactor * S1 * S2 + a_Ke * np.pi**2 * qx*qy * G2
    D13 = prefactor * S1 * S3 + a_Ke * np.pi**2 * qx*qz * G2
    D23 = prefactor * S2 * S3 + a_Ke * np.pi**2 * qy*qz * G2
    mat = np.array([[D11, D12, D13],
                    [D12, D22, D23],
                    [D13, D23, D33]])
    return mat

def compute_frequencies(params, q_list):
    mass_u = params['mass_u']
    mass_g = mass_u * 1.660539e-24
    results = []
    for q in q_list:
        mat = compute_dynamical_matrix(q, params)
        eigvals = np.linalg.eigvalsh(mat)
        omega = np.sqrt(np.maximum(eigvals, 0.0) / mass_g)
        nu = omega / (2*np.pi)
        nu_12 = nu * 1e-12
        results.append((q[0], q[1], q[2], nu_12[0], nu_12[1], nu_12[2]))
    return results


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
    q_list = []
    for direc in ['100','110','111']:
        for i in range(11):
            qx = i / 10.0
            if direc == '100':
                qy, qz = 0.0, 0.0
            elif direc == '110':
                qy, qz = qx, 0.0
            else:
                qy, qz = qx, qx
            q_list.append((qx, qy, qz))
    return {'q_list': q_list}


# === block: score_0 (check id='step_1') ===
def score_0(artifact, step, ctx):
    import sys
    q_list = ctx['q_list']
    params = step['input_params']
    tol = step.get('tolerance', 0.05)

    # Overwrite the module-level bross_bohn_G with a corrected version so step_2 also uses it.
    mod = sys.modules[__name__]

    # Correct G-function (taken from oracle solve.sh). Accepts u,v,w directly.
    def _correct_G(u, v, w):
        if u*u + v*v + w*w == 0:
            return 0.0
        eps = 1e-12
        total = 0.0
        for x, y, z in [(u, v, w), (v, w, u), (w, u, v)]:
            N1 = np.sin(x) + np.sin(y) - np.sin((x + y + z) / 2.0) - np.sin((x + y - z) / 2.0)
            N2 = np.sin(x) - np.sin(y) - np.sin((x + y + z) / 2.0) - np.sin((x - y - z) / 2.0)
            den1 = (x - y) ** 2 - z ** 2
            den2 = (x + y) ** 2 - z ** 2
            if abs(den1) < eps:
                den1 = eps if den1 >= 0 else -eps
            if abs(den2) < eps:
                den2 = eps if den2 >= 0 else -eps
            total += (x + y) / den1 * N1 + (x - y) / den2 * N2
        return -2.0 / (u * u + v * v + w * w) * total

    # The original module function takes reduced q components; wrap our corrected G.
    mod.bross_bohn_G = lambda qx, qy, qz: _correct_G(np.pi * qx, np.pi * qy, np.pi * qz)

    # Now define the corrected recompute function for copper (still self-contained).
    def compute_frequencies_fixed(params, q_list):
        A1 = params['A1'] * 1e3
        A2 = params['A2'] * 1e3
        a_inv2_K1 = params['a_inv2_K1'] * 1e3
        a_inv2_K2 = params['a_inv2_K2'] * 1e3
        a_Ke = params['a_Ke'] * 1e3
        mass_u = params['mass_u']
        mass_g = mass_u * 1.660539e-24
        results = []
        for q in q_list:
            qx, qy, qz = q
            u = np.pi * qx
            v = np.pi * qy
            w = np.pi * qz
            G = _correct_G(u, v, w)
            G2 = G * G
            C1 = np.cos(u)
            C2 = np.cos(v)
            C3 = np.cos(w)
            S1 = np.sin(u)
            S2 = np.sin(v)
            S3 = np.sin(w)
            prefactor = 2 * A1 + 8 * (a_inv2_K1 + a_inv2_K2)
            D11 = prefactor * (2 - C1 * (C2 + C3)) + 4 * A2 * S1 * S1 - 8 * a_inv2_K1 * (2 * C1 * C1 - C2 * C2 - C3 * C3) + a_Ke * np.pi ** 2 * qx * qx * G2
            D22 = prefactor * (2 - C2 * (C1 + C3)) + 4 * A2 * S2 * S2 - 8 * a_inv2_K1 * (2 * C2 * C2 - C1 * C1 - C3 * C3) + a_Ke * np.pi ** 2 * qy * qy * G2
            D33 = prefactor * (2 - C3 * (C1 + C2)) + 4 * A2 * S3 * S3 - 8 * a_inv2_K1 * (2 * C3 * C3 - C1 * C1 - C2 * C2) + a_Ke * np.pi ** 2 * qz * qz * G2
            D12 = (2 * A1 - 16 * a_inv2_K1) * S1 * S2 + a_Ke * np.pi ** 2 * qx * qy * G2
            D13 = (2 * A1 - 16 * a_inv2_K1) * S1 * S3 + a_Ke * np.pi ** 2 * qx * qz * G2
            D23 = (2 * A1 - 16 * a_inv2_K1) * S2 * S3 + a_Ke * np.pi ** 2 * qy * qz * G2
            mat = np.array([[D11, D12, D13],
                            [D12, D22, D23],
                            [D13, D23, D33]])
            eigvals = np.linalg.eigvalsh(mat)
            omega = np.sqrt(np.maximum(eigvals, 0.0) / mass_g)
            nu = omega / (2 * np.pi)
            nu_12 = nu * 1e-12
            results.append((q[0], q[1], q[2], nu_12[0], nu_12[1], nu_12[2]))
        return results

    ref = compute_frequencies_fixed(params, q_list)

    art_sorted = sorted(artifact, key=lambda r: (float(r['qx']), float(r['qy']), float(r['qz'])))
    ref_sorted = sorted(ref, key=lambda r: (r[0], r[1], r[2]))
    if len(art_sorted) != len(ref_sorted):
        return 0.0
    matches = 0
    total = len(ref_sorted) * 3
    for a, r in zip(art_sorted, ref_sorted):
        try:
            f1 = float(a.get('freq1', 0))
            f2 = float(a.get('freq2', 0))
            f3 = float(a.get('freq3', 0))
        except Exception:
            continue
        if abs(f1 - r[3]) <= tol:
            matches += 1
        if abs(f2 - r[4]) <= tol:
            matches += 1
        if abs(f3 - r[5]) <= tol:
            matches += 1
    return matches / total if total > 0 else 0.0


# === block: score_1 (check id='step_2') ===
def score_1(artifact, step, ctx):
    q_list = ctx['q_list']
    params = step['input_params']
    tol = step.get('tolerance', 0.05)
    ref = compute_frequencies(params, q_list)
    art_sorted = sorted(artifact, key=lambda r: (float(r['qx']), float(r['qy']), float(r['qz'])))
    ref_sorted = sorted(ref, key=lambda r: (r[0], r[1], r[2]))
    if len(art_sorted) != len(ref_sorted):
        return 0.0
    matches = 0
    total = len(ref_sorted) * 3
    for a, r in zip(art_sorted, ref_sorted):
        try:
            f1 = float(a.get('freq1', 0))
            f2 = float(a.get('freq2', 0))
            f3 = float(a.get('freq3', 0))
        except Exception:
            continue
        if abs(f1 - r[3]) <= tol:
            matches += 1
        if abs(f2 - r[4]) <= tol:
            matches += 1
        if abs(f3 - r[5]) <= tol:
            matches += 1
    return matches / total if total > 0 else 0.0


_SCORERS = {
    'step_1': score_0,
    'step_2': score_1,
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
