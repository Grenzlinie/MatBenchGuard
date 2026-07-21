import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import csv
import io


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
    ctx = {}

    # Parameters (all in nm-s units)
    S0 = 1.0
    lam_sf = 5.0  # nm
    lam_phi = 1.0  # nm
    lam_J = 1.0   # nm
    d = 8.0        # nm for step_01
    D = 5e14       # nm^2/s (5 cm^2/s)
    v_F = 5e14     # nm/s (5e5 m/s)

    # Derived quantities
    lam_par_inv2 = 1.0/lam_sf**2 + 1.0/lam_phi**2
    k_hat = np.sqrt(lam_par_inv2 - 1j/lam_J**2)

    # ----- Step 01: spin density profile -----
    z_vals_01 = np.linspace(0, d, 100)
    S_hat = S0 * np.cosh(k_hat * (z_vals_01 - d)) / np.cosh(k_hat * d)
    S_perp_01 = np.real(S_hat)
    S_z_01 = -np.imag(S_hat)   # task defines S_z = -Im(S_hat)
    ctx["step_01_z"] = z_vals_01.tolist()
    ctx["step_01_S_perp"] = S_perp_01.tolist()
    ctx["step_01_S_z"] = S_z_01.tolist()

    # ----- Step 02: torque vs d -----
    d_vals_02 = np.arange(0.5, 20.001, 0.5)  # 40 points
    T_hat_02 = S0 * (1.0/lam_phi**2 - 1j/lam_J**2) * D / k_hat * np.tanh(k_hat * d_vals_02)
    T_perp_02 = np.real(T_hat_02)
    T_z_02 = np.imag(T_hat_02)
    ctx["step_02_d"] = d_vals_02.tolist()
    ctx["step_02_T_perp"] = T_perp_02.tolist()
    ctx["step_02_T_z"] = T_z_02.tolist()

    # ----- Step 03: torque efficiency -----
    theta_hat = -np.sqrt(2)/2 * (D / (v_F * k_hat)) * (1.0/lam_phi**2 - 1j/lam_J**2)
    theta_perp_03 = float(np.real(theta_hat))
    theta_z_03 = float(np.imag(theta_hat))
    ctx["theta_perp"] = theta_perp_03
    ctx["theta_z"] = theta_z_03

    # ----- Helper for two-layer problem -----
    def solve_two_layer(d1, S1, S2, d2=6.0, lam_sf=5.0, lam_phi=1.0, lam_J=1.0, D=D):
        # k for mdTI (with precession)
        k_md = np.sqrt(1.0/lam_sf**2 + 1.0/lam_phi**2 - 1j/lam_J**2)
        # k for TI (no magnetization: precession and decoherence absent -> infinite tau -> zero contribution, 
        # leading to diffusion equation: d^2S/dz^2 = (1/lam_sf^2) S, i.e., k_ti = 1/lam_sf)
        k_ti = 1.0/lam_sf
    
        if d1 <= 0:
            # single layer of mdTI
            A = S1
            B = (S2 - S1*np.cosh(k_md*d2)) / np.sinh(k_md*d2) if np.abs(np.sinh(k_md*d2))>1e-12 else 0
            # integrate over [0,d2]
            z_int = np.linspace(0, d2, 1001)
            S_int = A*np.cosh(k_md*z_int) + B*np.sinh(k_md*z_int)
            # manual trapezoidal integration instead of deprecated np.trapz
            dx = np.diff(z_int)
            integral = np.sum(0.5 * (S_int[:-1] + S_int[1:]) * dx)
            T = D * (1.0/lam_phi**2 - 1j/lam_J**2) * integral
            return float(np.real(T)), float(np.imag(T))
    
        # Set up linear system for coefficients A1,B1 (TI) and A2,B2 (mdTI)
        # Region 1 (TI): S1(z) = A1*cosh(k_ti*z) + B1*sinh(k_ti*z)
        # Region 2 (mdTI): S2(z) = A2*cosh(k_md*z) + B2*sinh(k_md*z)
        # Boundary conditions:
        # S1(0) = S1            -> A1 = S1
        A1 = S1
        # S2(d1+d2) = S2
        L = d1 + d2
        # Continuity at z=d1:
        # S1(d1) = S2(d1)
        # J1(d1) = J2(d1)  ->  -D dS1/dz = -D dS2/dz  => dS1/dz(d1) = dS2/dz(d1)
        # Unknowns: B1, A2, B2 (A1 known)
        # Equations:
        # (1) A1*cosh(k_ti*d1) + B1*sinh(k_ti*d1) = A2*cosh(k_md*d1) + B2*sinh(k_md*d1)
        # (2) A2*cosh(k_md*L) + B2*sinh(k_md*L) = S2
        # (3) k_ti*(A1*sinh(k_ti*d1) + B1*cosh(k_ti*d1)) = k_md*(A2*sinh(k_md*d1) + B2*cosh(k_md*d1))
        # Matrix form M * x = v
        M = np.zeros((3,3), dtype=complex)
        v = np.zeros(3, dtype=complex)
        M[0,0] = np.sinh(k_ti*d1)
        M[0,1] = -np.cosh(k_md*d1)
        M[0,2] = -np.sinh(k_md*d1)
        v[0] = -A1 * np.cosh(k_ti*d1)
    
        M[1,0] = 0
        M[1,1] = np.cosh(k_md*L)
        M[1,2] = np.sinh(k_md*L)
        v[1] = S2
    
        M[2,0] = k_ti * np.cosh(k_ti*d1)
        M[2,1] = -k_md * np.sinh(k_md*d1)
        M[2,2] = -k_md * np.cosh(k_md*d1)
        v[2] = -k_ti * A1 * np.sinh(k_ti*d1)
    
        sol = np.linalg.solve(M, v)
        B1 = sol[0]
        A2 = sol[1]
        B2 = sol[2]
    
        # Integrate S2 over mdTI region [d1, L]
        z_md = np.linspace(d1, L, 1001)
        S_md = A2 * np.cosh(k_md * z_md) + B2 * np.sinh(k_md * z_md)
        # manual trapezoidal integration instead of deprecated np.trapz
        dx = np.diff(z_md)
        integral = np.sum(0.5 * (S_md[:-1] + S_md[1:]) * dx)
        T = D * (1.0/lam_phi**2 - 1j/lam_J**2) * integral
        return float(np.real(T)), float(np.imag(T))

    # ----- Step 04: torque vs d1 -----
    d1_vals_04 = np.arange(0, 10.01, 0.1)  # 101 points
    S1_04 = 1.0
    S2_04 = -1.0
    T_perp_04 = []
    T_z_04 = []
    for d1_val in d1_vals_04:
        tp, tz = solve_two_layer(d1_val, S1_04, S2_04, d2=6.0, lam_sf=lam_sf, lam_phi=lam_phi, lam_J=lam_J, D=D)
        T_perp_04.append(tp)
        T_z_04.append(tz)
    ctx["step_04_d1"] = d1_vals_04.tolist()
    ctx["step_04_T_perp"] = T_perp_04
    ctx["step_04_T_z"] = T_z_04

    # ----- Step 05: torque vs ratio -----
    ratios = np.arange(0.1, 1.91, 0.1)  # 19 points
    d1_fix = 3.0
    d2_fix = 6.0
    total_mag = 2.0
    T_perp_05 = []
    T_z_05 = []
    for r in ratios:
        mag2 = total_mag / (r + 1.0)
        mag1 = total_mag * r / (r + 1.0)
        S1_val = mag1
        S2_val = -mag2   # opposite sign
        tp, tz = solve_two_layer(d1_fix, S1_val, S2_val, d2=d2_fix, lam_sf=lam_sf, lam_phi=lam_phi, lam_J=lam_J, D=D)
        T_perp_05.append(tp)
        T_z_05.append(tz)
    ctx["step_05_ratios"] = ratios.tolist()
    ctx["step_05_T_perp"] = T_perp_05
    ctx["step_05_T_z"] = T_z_05

    # Generic comparator functions
    ctx["compare_func"] = None  # kept for interface compatibility; actual functions are below
    # Define helper inline and store closure
    import types
    def make_comparator():
        def compare_arrays(gold_x, gold_y, agent_x, agent_y, abs_tol=1e-4, rel_tol=0.001):
            if len(gold_x) != len(agent_x):
                return 0.0
            scores = []
            for g, a in zip(gold_y, agent_y):
                tol = max(abs_tol, rel_tol * abs(g))
                err = abs(g - a)
                if err <= tol:
                    scores.append(1.0)
                else:
                    scores.append(max(0.0, 1.0 - (err - tol)/tol))
            return float(np.mean(scores))
        def compare_scalars(gold, agent, abs_tol=1e-4, rel_tol=0.01):
            return compare_arrays([0], [gold], [0], [agent], abs_tol, rel_tol)
        return compare_arrays, compare_scalars
    comp_arr, comp_scal = make_comparator()
    ctx["comp_arr"] = comp_arr
    ctx["comp_scal"] = comp_scal

    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import csv
    import io
    ctx = ctx
    compare = ctx["comp_arr"]
    z_gold = np.array(ctx["step_01_z"])
    S_perp_gold = np.array(ctx["step_01_S_perp"])
    S_z_gold = np.array(ctx["step_01_S_z"])

    rows = artifact
    if not rows:
        return 0.0
    z_agent = np.array([float(r["z"]) for r in rows])
    S_perp_agent = np.array([float(r["S_perp"]) for r in rows])
    S_z_agent = np.array([float(r["S_z"]) for r in rows])
    # sort by z
    sort_idx = np.argsort(z_agent)
    z_agent = z_agent[sort_idx]
    S_perp_agent = S_perp_agent[sort_idx]
    S_z_agent = S_z_agent[sort_idx]

    # Ensure same length (should be 100)
    if len(z_agent) != len(z_gold):
        return 0.0
    score_perp = compare(z_gold, S_perp_gold, z_agent, S_perp_agent, abs_tol=1e-4, rel_tol=0.001)
    score_z = compare(z_gold, S_z_gold, z_agent, S_z_agent, abs_tol=1e-4, rel_tol=0.001)
    return 0.5*score_perp + 0.5*score_z


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    compare = ctx["comp_arr"]
    d_gold = np.array(ctx["step_02_d"])
    Tp_gold = np.array(ctx["step_02_T_perp"])
    Tz_gold = np.array(ctx["step_02_T_z"])

    rows = artifact
    if not rows:
        return 0.0
    d_agent = np.array([float(r["d"]) for r in rows])
    Tp_agent = np.array([float(r["T_perp"]) for r in rows])
    Tz_agent = np.array([float(r["T_z"]) for r in rows])
    sort_idx = np.argsort(d_agent)
    d_agent = d_agent[sort_idx]
    Tp_agent = Tp_agent[sort_idx]
    Tz_agent = Tz_agent[sort_idx]
    if len(d_agent) != len(d_gold):
        return 0.0
    score_p = compare(d_gold, Tp_gold, d_agent, Tp_agent, abs_tol=1e-4, rel_tol=0.001)
    score_z = compare(d_gold, Tz_gold, d_agent, Tz_agent, abs_tol=1e-4, rel_tol=0.001)
    return 0.5*score_p + 0.5*score_z


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    compare = ctx["comp_scal"]
    rows = artifact
    if not rows or len(rows) != 1:
        return 0.0
    row = rows[0]
    theta_perp_agent = float(row["theta_perp"])
    theta_z_agent = float(row["theta_z"])
    theta_perp_gold = ctx["theta_perp"]
    theta_z_gold = ctx["theta_z"]
    score_p = compare(theta_perp_gold, theta_perp_agent, abs_tol=1e-4, rel_tol=0.01)
    score_z = compare(theta_z_gold, theta_z_agent, abs_tol=1e-4, rel_tol=0.01)
    return 0.5*score_p + 0.5*score_z


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    compare = ctx["comp_arr"]
    d1_gold = np.array(ctx["step_04_d1"])
    Tp_gold = np.array(ctx["step_04_T_perp"])
    Tz_gold = np.array(ctx["step_04_T_z"])
    rows = artifact
    if not rows:
        return 0.0
    d1_agent = np.array([float(r["d1"]) for r in rows])
    Tp_agent = np.array([float(r["T_perp"]) for r in rows])
    Tz_agent = np.array([float(r["T_z"]) for r in rows])
    sort_idx = np.argsort(d1_agent)
    d1_agent = d1_agent[sort_idx]
    Tp_agent = Tp_agent[sort_idx]
    Tz_agent = Tz_agent[sort_idx]
    if len(d1_agent) != len(d1_gold):
        return 0.0
    score_p = compare(d1_gold, Tp_gold, d1_agent, Tp_agent, abs_tol=1e-4, rel_tol=0.001)
    score_z = compare(d1_gold, Tz_gold, d1_agent, Tz_agent, abs_tol=1e-4, rel_tol=0.001)
    return 0.5*score_p + 0.5*score_z


# === block: score_4 (check id='step_05') ===
def score_4(artifact, step, ctx):
    compare = ctx["comp_arr"]
    ratios_gold = np.array(ctx["step_05_ratios"])
    Tp_gold = np.array(ctx["step_05_T_perp"])
    Tz_gold = np.array(ctx["step_05_T_z"])
    rows = artifact
    if not rows:
        return 0.0
    ratios_agent = np.array([float(r["ratio"]) for r in rows])
    Tp_agent = np.array([float(r["T_perp"]) for r in rows])
    Tz_agent = np.array([float(r["T_z"]) for r in rows])
    sort_idx = np.argsort(ratios_agent)
    ratios_agent = ratios_agent[sort_idx]
    Tp_agent = Tp_agent[sort_idx]
    Tz_agent = Tz_agent[sort_idx]
    if len(ratios_agent) != len(ratios_gold):
        return 0.0
    score_p = compare(ratios_gold, Tp_gold, ratios_agent, Tp_agent, abs_tol=1e-4, rel_tol=0.001)
    score_z = compare(ratios_gold, Tz_gold, ratios_agent, Tz_agent, abs_tol=1e-4, rel_tol=0.001)
    return 0.5*score_p + 0.5*score_z


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
    'step_05': score_4,
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
