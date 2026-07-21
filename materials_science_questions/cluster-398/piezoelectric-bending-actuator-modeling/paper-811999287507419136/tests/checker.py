import os
import json
import csv

# === author imports / helpers ===
import numpy as np

# ---------- HYBAS solver ----------
L0 = 5.5e-3  # m

# original inactive-layer geometry (same for all computations)
INACTIVE_LAYERS = [
    # name, E (Pa), t (m), b (m), count
    ('inactive_EAP',  1.0e9, 15e-6, 4.5e-3, 1),
    ('epoxy',         5.0e9,  1e-6, 4.5e-3, 1),
    ('gold_electrode',74.0e9, 0.1e-6, 3.0e-3, 2),  # two electrodes
    ('unelectroded_margin', 1.0e9, 16e-6, 0.75e-3, 2),
]

# active EAP reference geometry (original); thickness and width are fixed for trade study
ACTIVE_EAP_THICK = 16e-6   # m
ACTIVE_EAP_WIDTH = 4.5e-3   # total width, but effective width for clamping? Actually active layer effective width for stiffness is 3 mm (electroded width). The clamping ratio uses effective width of active layer = 3 mm.
ACTIVE_EAP_EFF_WIDTH = 3e-3  # m (electroded width)

# negative component original geometry (fixed for trade study)
ESC_THICK = 470e-6   # m
ESC_WIDTH = 3e-3     # m

# original material properties
ORIG_d31_neg = -970e-12   # m/V
ORIG_E_neg   = 20e9       # Pa
ORIG_d31_pos = 20e-12
ORIG_E_pos   = 1e9

# trade‑study materials
trade_neg_materials = [
    ('Hard PZT (TRS100HD)', -150e-12, 79e9),
    ('Soft PZT (TRSHK1HD)', -360e-12, 67e9),
    ('PZN-4.5%PT single crystal', -970e-12, 12e9),
]
trade_pos_materials = [
    ('Uni-axial PVDF', 20e-12, 2e9),
    ('Bi-axial PVDF',   8e-12, 2e9),
]

# Integration: left‑hand Riemann sum, 1000 subintervals
def riemann_lhs(c, Ld, N=1000):
    xs = np.linspace(-Ld/2, Ld/2, N+1)[:N]  # left endpoints
    f = np.sqrt(c**2 * (4*xs**3 - Ld**2 * xs)**2 + 1.0)
    return np.sum(f) * (Ld / N)

# binary search for c; assume LHS increases with c
SOLVER_PERCENT_ERROR_TOL = 0.001e-2  # 0.001% relative error
def find_c(Ld, RHS, N=1000):
    c_lo = 0.0
    # find an upper bound where lhs > RHS
    c_up = 1e3   # start small
    while riemann_lhs(c_up, Ld, N) < RHS:
        c_up *= 10
        if c_up > 1e15:
            break
    for _ in range(80):
        c_mid = (c_lo + c_up) / 2.0
        lhs = riemann_lhs(c_mid, Ld, N)
        err = abs(lhs / RHS - 1.0)
        if err < SOLVER_PERCENT_ERROR_TOL:
            return c_mid, 100.0 * err
        if lhs > RHS:
            c_up = c_mid
        else:
            c_lo = c_mid
    c_final = (c_lo + c_up) / 2.0
    lhs = riemann_lhs(c_final, Ld, N)
    err = abs(lhs / RHS - 1.0)
    return c_final, 100.0 * err

# clamp ratio for given active EAP Young's modulus
def compute_clamping_ratio(E_active):
    stiff_inactive = sum(cnt * E * t * b for (_, E, t, b, cnt) in INACTIVE_LAYERS)
    stiff_active = E_active * ACTIVE_EAP_THICK * ACTIVE_EAP_EFF_WIDTH
    return stiff_inactive / stiff_active

# effective positive strain
def pos_eff_strain(V, d31_pos, t_pos, k):
    s0 = d31_pos * V / t_pos   # free strain (do not sign‑wrap; assume positive d31)
    return s0 / (1.0 + k)

# solve one case for original configuration (mode determines active components)
def solve_original_case(V, mode, d31_neg=ORIG_d31_neg, E_neg=ORIG_E_neg, d31_pos=ORIG_d31_pos, E_pos=ORIG_E_pos):
    # L_d from negative component; if ESC active, strain is free strain
    if mode in ('ESC', 'HYBAS'):
        s_neg = d31_neg * V / ESC_THICK   # negative
    else:
        s_neg = 0.0
    Ld = L0 * (1.0 + s_neg)
    # right‑hand side
    if mode in ('EAP', 'HYBAS'):
        k = compute_clamping_ratio(E_pos)
        s_eff = pos_eff_strain(V, d31_pos, ACTIVE_EAP_THICK, k)
    else:
        s_eff = 0.0
    RHS = L0 * (1.0 + s_eff)
    # find c
    c_raw, pct_err = find_c(Ld, RHS, 1000)
    c_10p6 = c_raw * 1e-6   # convert to 10^6/m^3
    return c_10p6, pct_err

# solve one trade‑study case (both active, given negative/positive material props)
def solve_trade_case(V, d31_neg, E_neg, d31_pos, E_pos):
    s_neg = d31_neg * V / ESC_THICK
    Ld = L0 * (1.0 + s_neg)
    k = compute_clamping_ratio(E_pos)
    s_eff = pos_eff_strain(V, d31_pos, ACTIVE_EAP_THICK, k)
    RHS = L0 * (1.0 + s_eff)
    c_raw, _ = find_c(Ld, RHS, 1000)
    w_max = c_raw * Ld**4 / 16.0   # meters
    return w_max * 1e6   # micrometers


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
        # Compute reference c_values
        voltages = [200, 400, 800, 1600]
        modes = ['EAP', 'ESC', 'HYBAS']
        c_ref = []
        for V in voltages:
            for mode in modes:
                c_val, pct_err = solve_original_case(V, mode)
                c_ref.append({
                    'voltage': V,
                    'active_elements': mode,
                    'c': round(c_val, 6),
                    'percent_error': round(pct_err, 8)
                })
        # Compute reference max_displacements
        voltages_trade = [100, 650]
        max_d_ref = []
        for V in voltages_trade:
            for neg_name, d31_neg, E_neg in trade_neg_materials:
                for pos_name, d31_pos, E_pos in trade_pos_materials:
                    w = solve_trade_case(V, d31_neg, E_neg, d31_pos, E_pos)
                    max_d_ref.append({
                        'negative_strain_material': neg_name,
                        'positive_strain_material': pos_name,
                        'voltage': V,
                        'max_displacement': round(w, 6)
                    })
        return {'c_ref': c_ref, 'max_d_ref': max_d_ref}


# === block: score_0 (check id='step_01_compute_c_values') ===
def score_0(artifact, step, ctx):
        ref = ctx['c_ref']
        if not isinstance(artifact, list) or len(artifact) != len(ref):
            return 0.0
        # Build lookup key: (voltage, active_elements)
        def key(e):
            return (e.get('voltage'), e.get('active_elements'))
        art_map = {key(e): e for e in artifact}
        score_sum = 0.0
        c_tol = 0.05   # tolerance in 10^6/m^3 units
        pct_tol = 0.0015  # 0.0015% max allowed
        count = len(ref)
        for r in ref:
            k = key(r)
            a = art_map.get(k)
            if a is None:
                continue
            a_c = a.get('c')
            a_pct = a.get('percent_error')
            if a_c is None or a_pct is None:
                continue
            c_diff = abs(a_c - r['c'])
            pct_ok = a_pct <= pct_tol
            if c_diff <= c_tol and pct_ok:
                score_sum += 1.0
            elif c_diff <= 2*c_tol and pct_ok:
                score_sum += 0.5
            # else 0
        return score_sum / count


# === block: score_1 (check id='step_02_compute_max_displacements') ===
def score_1(artifact, step, ctx):
        ref = ctx['max_d_ref']
        if not isinstance(artifact, list) or len(artifact) != len(ref):
            return 0.0
        def key(e):
            return (e.get('negative_strain_material'), e.get('positive_strain_material'), e.get('voltage'))
        art_map = {key(e): e for e in artifact}
        tol = 0.2   # µm
        scores = []
        for r in ref:
            k = key(r)
            a = art_map.get(k)
            if a is None:
                scores.append(0.0)
                continue
            a_val = a.get('max_displacement')
            if a_val is None:
                scores.append(0.0)
                continue
            diff = abs(a_val - r['max_displacement'])
            if diff <= tol:
                scores.append(1.0)
            else:
                # linear decay beyond tolerance
                s = max(0.0, 1.0 - (diff - tol) / (5*tol))
                scores.append(s)
        return sum(scores) / len(scores)


_SCORERS = {
    'step_01_compute_c_values': score_0,
    'step_02_compute_max_displacements': score_1,
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
