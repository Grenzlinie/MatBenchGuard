import os
import json
import csv

# === author imports / helpers ===
import math, cmath


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
    import json

    # Ge n,k table from grading_spec step_05_nonlocal params
    ge_table = []  # will be populated from spec below, but we embed it directly
    for step in spec.get('steps', []):
        if step['id'] == 'step_05_nonlocal':
            ge_table = step['params']['ge_nk_table']
            break

    ctx = {
        't': 0.585,  # slab thickness in microns
        'ge_table': ge_table,  # list of (wl_um, n, k)
        'ag_eps_inf': 5.0,
        'omega_p': 1.38e16,
        'gamma_p': 6.4 * 5.07e13,
        'c': 299792458.0,
        'd1': 15e-9,  # m
        'd2': 85e-9   # m
    }
    return ctx


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact  # list of dicts
    if not artifact_rows:
        return 0.0
    for row in artifact_rows:
        T = float(row['transmission'])
        R = float(row['reflection'])
        if not (0.0 <= T <= 1.0 and 0.0 <= R <= 1.0 and T + R <= 1.0 + 1e-6):
            return 0.0
    # at least 5 rows
    if len(artifact_rows) < 5:
        return 0.0
    return 1.0


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    import os, json, math

    # load spectra
    spec_path = os.path.join('/app/outputs', 'step_01_simulated_spectra.csv')
    if not os.path.exists(spec_path):
        return 0.0
    spec_rows = []
    with open(spec_path, newline='') as f:
        reader = csv.DictReader(f)
        spec_rows = list(reader)
    if not spec_rows:
        return 0.0

    # agent n,k rows
    agent = artifact
    if not agent:
        return 0.0

    t = ctx['t']

    def compute_nk(T, R, lam):
        if T <= 0: T = 1e-12
        inner = T**2 - (1.0 - R)**2
        sqrt_term = math.sqrt(inner**2 + 4.0 * T**2)
        X = (inner + sqrt_term) / (2.0 * T)
        if X <= 0:
            return None, None, None
        k = -lam / (4.0 * math.pi * t) * math.log(X)
        Ras = R / (1.0 + T * X)
        disc = 4.0 * Ras / ((1.0 - Ras)**2) - k**2
        if disc < 0:
            return None, None, None
        sqrt_disc = math.sqrt(disc)
        term = (1.0 + Ras) / (1.0 - Ras)
        n_plus = term + sqrt_disc
        n_minus = term - sqrt_disc
        return k, n_plus, n_minus

    # align wavelengths via interpolation? simple: require same wavelengths and order
    spec_by_wl = {}
    for r in spec_rows:
        wl = float(r['wavelength_micron'])
        spec_by_wl[wl] = (float(r['transmission']), float(r['reflection']))

    agent_by_wl = {}
    for r in agent:
        wl = float(r['wavelength_micron'])
        agent_by_wl[wl] = (float(r['n']), float(r['k']))

    common_wls = [wl for wl in spec_by_wl if wl in agent_by_wl]
    if not common_wls:
        return 0.0

    errors_n = []
    errors_k = []
    for wl in common_wls:
        T, R = spec_by_wl[wl]
        k_ref, n_plus, n_minus = compute_nk(T, R, wl)
        if k_ref is None:
            continue
        agent_n, agent_k = agent_by_wl[wl]
        # choose branch
        error_n = min(abs(agent_n - n_plus), abs(agent_n - n_minus))
        error_k = abs(agent_k - k_ref)
        errors_n.append(error_n)
        errors_k.append(error_k)

    if not errors_n:
        return 0.0
    avg_n = sum(errors_n) / len(errors_n)
    avg_k = sum(errors_k) / len(errors_k)
    tol_n = step['params']['tolerance_n']
    tol_k = step['params']['tolerance_k']
    score_n = max(0.0, 1.0 - avg_n / tol_n)
    score_k = max(0.0, 1.0 - avg_k / tol_k)
    return (score_n + score_k) / 2.0


# === block: score_2 (check id='step_03') ===
def score_2(artifact, step, ctx):
    agent_eps = artifact
    if not agent_eps:
        return 0.0
    # load n,k
    import os
    nk_path = os.path.join('/app/outputs', 'step_02_retrieved_nk.csv')
    if not os.path.exists(nk_path):
        return 0.0
    nk_rows = []
    with open(nk_path, newline='') as f:
        nk_rows = list(csv.DictReader(f))
    if not nk_rows:
        return 0.0
    nk_by_wl = {}
    for r in nk_rows:
        wl = float(r['wavelength_micron'])
        nk_by_wl[wl] = (float(r['n']), float(r['k']))

    agent_by_wl = {}
    for r in agent_eps:
        wl = float(r['wavelength_micron'])
        agent_by_wl[wl] = (float(r['real_epsilon']), float(r['imag_epsilon']))

    common = [wl for wl in nk_by_wl if wl in agent_by_wl]
    if not common:
        return 0.0

    errors_real = []
    errors_imag = []
    for wl in common:
        n, k = nk_by_wl[wl]
        ref_real = n**2 - k**2
        ref_imag = 2 * n * k
        sub_real, sub_imag = agent_by_wl[wl]
        errors_real.append(abs(sub_real - ref_real))
        errors_imag.append(abs(sub_imag - ref_imag))

    avg_real = sum(errors_real) / len(errors_real)
    avg_imag = sum(errors_imag) / len(errors_imag)
    tol_r = step['params']['tolerance_real']
    tol_i = step['params']['tolerance_imag']
    score_r = max(0.0, 1.0 - avg_real / tol_r)
    score_i = max(0.0, 1.0 - avg_imag / tol_i)
    return (score_r + score_i) / 2.0


# === block: score_3 (check id='step_04') ===
def score_3(artifact, step, ctx):
    import os, json

    # load epsilon from step_03
    eps_path = os.path.join('/app/outputs', 'step_03_retrieved_epsilon.csv')
    if not os.path.exists(eps_path):
        return 0.0
    eps_rows = []
    with open(eps_path, newline='') as f:
        eps_rows = list(csv.DictReader(f))
    if len(eps_rows) < 2:
        return 0.0

    # load n,k from step_02
    nk_path = os.path.join('/app/outputs', 'step_02_retrieved_nk.csv')
    if not os.path.exists(nk_path):
        return 0.0
    nk_rows = []
    with open(nk_path, newline='') as f:
        nk_rows = list(csv.DictReader(f))
    if len(nk_rows) < 2:
        return 0.0

    # build sorted arrays
    eps_wl = []
    eps_real = []
    for r in eps_rows:
        eps_wl.append(float(r['wavelength_micron']))
        eps_real.append(float(r['real_epsilon']))

    nk_wl = []
    nk_n = []
    nk_k = []
    for r in nk_rows:
        nk_wl.append(float(r['wavelength_micron']))
        nk_n.append(float(r['n']))
        nk_k.append(float(r['k']))

    # sort by wavelength
    eps_wl, eps_real = zip(*sorted(zip(eps_wl, eps_real)))
    nk_wl, nk_n, nk_k = zip(*sorted(zip(nk_wl, nk_n, nk_k)))

    # find crossing
    idx = None
    for i in range(len(eps_real)-1):
        if eps_real[i] * eps_real[i+1] <= 0:
            idx = i
            break
    if idx is None:
        # no crossing => 0
        return 0.0

    # linear interpolation
    f0 = eps_real[idx]
    f1 = eps_real[idx+1]
    lam0 = eps_wl[idx]
    lam1 = eps_wl[idx+1]
    enz_wl = lam0 - f0 * (lam1 - lam0) / (f1 - f0)

    ref = step['params']['enz_wavelength_ref']
    tol_wl = step['params']['tol_wavelength']
    score_wl = 1.0 if abs(enz_wl - ref) <= tol_wl else 0.0

    # interpolate n,k at enz_wl
    # find indices surrounding enz_wl in nk array
    idx_nk = None
    for i in range(len(nk_wl)-1):
        if nk_wl[i] <= enz_wl <= nk_wl[i+1]:
            idx_nk = i
            break
    if idx_nk is None:
        score_nk = 0.0
    else:
        w0 = nk_wl[idx_nk]
        w1 = nk_wl[idx_nk+1]
        frac = (enz_wl - w0) / (w1 - w0)
        n_interp = nk_n[idx_nk] + frac * (nk_n[idx_nk+1] - nk_n[idx_nk])
        k_interp = nk_k[idx_nk] + frac * (nk_k[idx_nk+1] - nk_k[idx_nk])
        diff = abs(n_interp - k_interp)
        score_nk = 1.0 if diff <= step['params']['nk_diff_tol'] else 0.0

    return 0.5 * score_wl + 0.5 * score_nk


# === block: score_4 (check id='step_05_nonlocal') ===
def score_4(artifact, step, ctx):
    agent = artifact
    if not agent:
        return 0.0

    ge_table = ctx['ge_table']
    eps_inf = ctx['ag_eps_inf']
    omega_p = ctx['omega_p']
    gamma_p = ctx['gamma_p']
    c = ctx['c']
    d1 = ctx['d1']
    d2 = ctx['d2']

    # ge interpolation
    def ge_eps(wl_um):
        # wl in microns
        # linear interpolation from ge_table
        wls = [p[0] for p in ge_table]
        ns = [p[1] for p in ge_table]
        ks = [p[2] for p in ge_table]
        # find interval
        if wl_um <= wls[0]:
            n, k = ns[0], ks[0]
        elif wl_um >= wls[-1]:
            n, k = ns[-1], ks[-1]
        else:
            for i in range(len(wls)-1):
                if wls[i] <= wl_um <= wls[i+1]:
                    frac = (wl_um - wls[i]) / (wls[i+1] - wls[i])
                    n = ns[i] + frac*(ns[i+1] - ns[i])
                    k = ks[i] + frac*(ks[i+1] - ks[i])
                    break
            else:
                n, k = ns[0], ks[0]
        return n, k

    errors_real = []
    errors_imag = []
    for row in agent:
        wl_um = float(row['wavelength_micron'])
        wl_m = wl_um * 1e-6
        omega = 2 * math.pi * c / wl_m
        k0 = 2 * math.pi / wl_m
        eps_ag = eps_inf - omega_p**2 / (omega * (omega - 1j * gamma_p))
        nge, kge = ge_eps(wl_um)
        eps_ge = (nge + 1j * kge)**2
        sq1 = cmath.sqrt(eps_ag)
        sq2 = cmath.sqrt(eps_ge)
        cos1 = cmath.cos(sq1 * k0 * d1)
        cos2 = cmath.cos(sq2 * k0 * d2)
        sin1 = cmath.sin(sq1 * k0 * d1)
        sin2 = cmath.sin(sq2 * k0 * d2)
        term1 = cos1 * cos2
        term2 = 0.5 * (sq1/sq2 + sq2/sq1) * sin1 * sin2
        arg = term1 - term2
        theta = cmath.acos(arg)
        eps_y = theta**2 / (k0**2 * (d1 + d2)**2)
        real_ref = eps_y.real
        imag_ref = eps_y.imag
        real_sub = float(row['real_epsilon'])
        imag_sub = float(row['imag_epsilon'])
        errors_real.append(abs(real_sub - real_ref))
        errors_imag.append(abs(imag_sub - imag_ref))

    if not errors_real:
        return 0.0
    max_err = max(max(errors_real), max(errors_imag))
    tol = step['params']['tolerance_eps']
    score = max(0.0, 1.0 - max_err / tol)
    return score


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
    'step_03': score_2,
    'step_04': score_3,
    'step_05_nonlocal': score_4,
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
