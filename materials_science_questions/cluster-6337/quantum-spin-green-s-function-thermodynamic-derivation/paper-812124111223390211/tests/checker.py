import os
import json
import csv

# === author imports / helpers ===
import csv, math, os

try:
    import numpy as np
except ImportError:
    class _np:
        @staticmethod
        def array(seq):
            return list(seq)
        @staticmethod
        def argsort(seq):
            return sorted(range(len(seq)), key=lambda i: seq[i])
        @staticmethod
        def isclose(a, b, rtol=1e-05, atol=1e-08):
            return abs(a - b) <= atol + rtol * max(abs(a), abs(b))
        @staticmethod
        def any(iterable):
            return any(iterable)
        @staticmethod
        def where(condition):
            return [i for i, v in enumerate(condition) if v]
        class linalg:
            @staticmethod
            def solve(A, B):
                n = len(A)
                if n == 3:
                    a, b, c = A[0]
                    d, e, f = A[1]
                    g, h, i = A[2]
                    detA = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
                    if detA == 0:
                        return [0.0, 0.0, 0.0]
                    x = (B[0]*(e*i - f*h) - b*(B[1]*i - B[2]*f) + c*(B[1]*h - B[2]*e)) / detA
                    y = (a*(B[1]*i - B[2]*f) - B[0]*(d*i - f*g) + c*(d*B[2] - B[1]*g)) / detA
                    z = (a*(e*B[2] - B[1]*h) - b*(d*B[2] - B[1]*g) + B[0]*(d*h - e*g)) / detA
                    return [x, y, z]
                elif n == 2:
                    a, b = A[0]
                    c, d = A[1]
                    detA = a*d - b*c
                    if detA == 0:
                        return [0.0, 0.0]
                    x = (B[0]*d - b*B[1]) / detA
                    y = (a*B[1] - B[0]*c) / detA
                    return [x, y]
                else:
                    raise ValueError('Only 2x2 or 3x3 systems supported in fallback')
        @staticmethod
        def mean(seq):
            return sum(seq)/len(seq) if seq else 0.0
    np = _np()


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


# === block: score_0 (check id='chi_qzz_check') ===
def score_0(artifact, step, ctx):
    import csv, math
    import numpy as np

    def load_csv(path):
        if not os.path.exists(path):
            return []
        with open(path, newline='') as f:
            return list(csv.DictReader(f))

    # Load omega_x_values.csv
    omega_rows = load_csv('/app/outputs/omega_x_values.csv')
    if not omega_rows:
        return 0.0

    # Extract x and Omega, find indices near zero
    xs = np.array([float(r['x']) for r in omega_rows])
    omegas = np.array([float(r['Omega']) for r in omega_rows])

    # Sort by x
    order = np.argsort(xs)
    xs = xs[order]
    omegas = omegas[order]

    # Find x=0 point; if not present, we need close points
    idx0 = np.where(np.isclose(xs, 0.0))[0]
    if len(idx0) == 0:
        # find nearest to 0
        idx0 = [np.argmin(np.abs(xs))]
    else:
        idx0 = idx0[0]

    # Get points around zero for finite differences
    dx = 0.1  # expected step
    # find indices for -0.1 and 0.1
    mask_p = np.isclose(xs, 0.1, atol=0.015)
    mask_m = np.isclose(xs, -0.1, atol=0.015)
    if np.any(mask_p) and np.any(mask_m):
        Omega_p = omegas[mask_p][0]
        Omega_m = omegas[mask_m][0]
        Omega_0 = omegas[idx0]
        # first derivative dOmega/dx at x=0
        dOmega = (Omega_p - Omega_m) / (0.2)   # (0.1 - (-0.1)) = 0.2
        # second derivative
        d2Omega = (Omega_p - 2*Omega_0 + Omega_m) / (0.01)
    else:
        # fallback: use nearby points
        indices = np.argsort(np.abs(xs))
        x0 = xs[indices[0]]
        x1 = xs[indices[1]]
        x2 = xs[indices[2]]
        y0 = omegas[indices[0]]
        y1 = omegas[indices[1]]
        y2 = omegas[indices[2]]
        # fit quadratic y = a + b*x + c*x^2
        A = np.array([[1, x0, x0**2],
                      [1, x1, x1**2],
                      [1, x2, x2**2]])
        coeffs = np.linalg.solve(A, [y0, y1, y2])
        dOmega = coeffs[1]
        d2Omega = 2*coeffs[2]

    # Moments
    S_z = dOmega
    S2_z = d2Omega

    # Check for reasonable magnitude (S=1 case)
    if abs(S_z) > 1.1 or S2_z < 0 or S2_z > 2.1:
        # unphysical, set to zero?
        S_z = 0.0
        S2_z = 0.0

    T = 10.0
    k_B = 1.0
    beta = 1.0 / T
    chi_0 = beta * (S2_z - S_z**2)
    if chi_0 <= 0:
        chi_0 = 1e-6

    # Load chi_qzz_values.csv
    chi_rows = load_csv('/app/outputs/chi_qzz_values.csv')
    if not chi_rows:
        return 0.0

    J_val = 1.0
    rel_tol = 0.15
    max_dev = 0.5

    scores = []

    for row in chi_rows:
        qx = float(row['q_x'])
        qy = float(row['q_y'])
        chi_agent = float(row['chi_qzz'])
        # Compute J(0)-J(q): for square lattice J(k)=2J(cos(kx)+cos(ky))
        J_q = 2*J_val*(math.cos(qx) + math.cos(qy))
        J_0 = 4*J_val
        diff_J = J_0 - J_q
        # paramagnetic limit approx
        chi_approx = k_B * T / (1.0/chi_0 + 2*diff_J)
        if chi_approx <= 0:
            chi_approx = 1e-6
        rel_err = abs(chi_agent - chi_approx) / abs(chi_approx) if abs(chi_approx) > 1e-10 else 0.0
        # score: linear decay from 1.0 at rel_err <= rel_tol to 0 at max_dev
        if rel_err <= rel_tol:
            score = 1.0
        elif rel_err >= max_dev:
            score = 0.0
        else:
            score = 1.0 - (rel_err - rel_tol) / (max_dev - rel_tol)
        scores.append(score)

    if not scores:
        return 0.0
    return float(np.mean(scores))


_SCORERS = {
    'chi_qzz_check': score_0,
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
