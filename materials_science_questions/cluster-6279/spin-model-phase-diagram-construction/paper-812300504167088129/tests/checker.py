import os
import json
import csv


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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import numpy as np
    from scipy.special import iv
    from scipy.integrate import quad
    from scipy.optimize import bisect

    # fixed parameters
    J1 = 2.0
    J2 = -1.0
    Jz = 0.0
    kB = 1.0
    Tc_XY = (Jz / 2.0 + J1**2 / (8.0 * abs(J2)) + abs(J2)) / kB   # 1.5

    def P1(z):
        """Modified Bessel function ratio I₁(z)/I₀(z)."""
        if z == 0.0:
            return 0.0
        return iv(1, z) / iv(0, z)

    def avg_cos(xi, h):
        """
        Return ⟨cos φ⟩ for a single site with molecular field xi
        and scaled field h = H/(k_B T).
        """
        if h == 0.0:
            # pure XY limit: <cos φ> = I₁(xi)/I₀(xi)
            if xi == 0.0:
                return 0.0
            return iv(1, xi) / iv(0, xi)
        f_num = lambda phi: np.cos(phi) * np.exp(xi * np.cos(phi) - h * (1.0 - np.cos(2.0 * phi)))
        f_den = lambda phi: np.exp(xi * np.cos(phi) - h * (1.0 - np.cos(2.0 * phi)))
        num, _ = quad(f_num, 0.0, 2.0 * np.pi, limit=200)
        den, _ = quad(f_den, 0.0, 2.0 * np.pi, limit=200)
        if den == 0.0:
            return 0.0
        return num / den

    def avg_sin2(xi, h):
        """
        Return ⟨sin² φ⟩ for a single site with molecular field xi
        and scaled field h.
        """
        f_num = lambda phi: (np.sin(phi) ** 2) * np.exp(xi * np.cos(phi) - h * (1.0 - np.cos(2.0 * phi)))
        f_den = lambda phi: np.exp(xi * np.cos(phi) - h * (1.0 - np.cos(2.0 * phi)))
        num, _ = quad(f_num, 0.0, 2.0 * np.pi, limit=200)
        den, _ = quad(f_den, 0.0, 2.0 * np.pi, limit=200)
        if den == 0.0:
            return 0.0
        return num / den

    def solve_mean_field_ising(T, H):
        """
        Solve self-consistent equations for the Ising order parameters
        c₁, c₂ of the period‑6 modulated phase at temperature T and field H.
        Returns (c₁, c₂, ⟨sin² φ₂⟩).
        """
        beta = 1.0 / T
        h_ = H / T
        c1, c2 = 1.0, 0.2   # initial guess
        for _ in range(200):
            # molecular fields (periodic boundary, q=1/6 symmetry)
            xi1 = beta * 2.0 * c2 * (J1 - J2)
            xi2 = beta * (J1 * (c1 - c2) + J2 * (-1.0 + c2))
            c1_new = avg_cos(xi1, h_)
            c2_new = avg_cos(xi2, h_)
            diff = abs(c1_new - c1) + abs(c2_new - c2)
            c1, c2 = c1_new, c2_new
            if diff < 1e-8:
                break
        sin2_2 = avg_sin2(xi2, h_)
        return c1, c2, sin2_2

    def solve_Tc(H):
        """Exact Tc from eq.(12): T = (1 + P₁(H/T)) * Tc_XY."""
        if H == 0.0:
            return Tc_XY
        f = lambda T: T - Tc_XY * (1.0 + P1(H / T))
        low, high = Tc_XY, 10.0
        try:
            return bisect(f, low, high, xtol=1e-8)
        except Exception:
            # fallback: if bisection fails, return a dummy (should not happen)
            return Tc_XY

    def solve_Tc_prime(H, Tc):
        """
        Exact Tc' from eq.(15): find T in (0, Tc) such that
        T = 2 * ⟨sin² φ₂⟩(T,H) * Tc_XY.
        Returns 0.0 if no positive root exists.
        """
        if H == 0.0:
            return 0.0
        f = lambda T: T - 2.0 * solve_mean_field_ising(T, H)[2] * Tc_XY
        low, high = 1e-6, Tc
        try:
            fa, fb = f(low), f(high)
            if fa * fb > 0.0:
                return 0.0
            return bisect(f, low, high, xtol=1e-8)
        except Exception:
            return 0.0

    # --- main scorer body ---
    artifact_rows = artifact[:]
    if not artifact_rows:
        return 0.0

    # build index by H
    agent = {}
    for row in artifact_rows:
        try:
            h_val = round(float(row['H']), 1)
            agent[h_val] = row
        except (ValueError, KeyError):
            return 0.0

    # expected H range
    H_vals = [round(x,1) for x in np.arange(0.0, 2.05, 0.1)]
    if set(agent.keys()) != set(H_vals):
        return 0.0

    # sort rows for monotonicity check
    sorted_rows = [agent[h] for h in H_vals]

    tol_tc = 0.05
    tol_tcp = 0.10

    # compute expected Tc and Tc' on the fly and compare
    Tc_prev = None
    for h in H_vals:
        row = agent[h]
        # exact reference values
        Tc_ref = solve_Tc(h)
        Tc_prime_ref = solve_Tc_prime(h, Tc_ref)
        tc = float(row['Tc'])
        tcp = float(row['Tc_prime'])
        if abs(tc - Tc_ref) > tol_tc:
            return 0.0
        if abs(tcp - Tc_prime_ref) > tol_tcp:
            return 0.0
        # monotonicity of Tc with H (strict for H>0)
        if h > 0.0:
            if Tc_prev is not None and tc < Tc_prev - 1e-9:
                return 0.0
            Tc_prev = tc
        # Tc' < Tc for H <= 0.75
        if h <= 0.75:
            if tcp >= tc - 1e-9:
                return 0.0

    return 1.0


_SCORERS = {
    'step_01': score_0,
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
