import os
import json
import csv

# === author imports / helpers ===
import math

def compute_absorption(nu_array, eps_prism, eps_gap, eps_film, eps_substrate, d_film_cm, l_gap_cm, phi_rad):
    import numpy as np
    A = np.zeros_like(nu_array, dtype=float)
    sin2 = np.sin(phi_rad)**2
    for i, nu in enumerate(nu_array):
        e1 = eps_prism
        e2 = eps_gap
        e3 = eps_film(nu) if callable(eps_film) else eps_film
        e4 = eps_substrate(nu) if callable(eps_substrate) else eps_substrate
        k1 = np.sqrt(e1*sin2 - e1)
        k2 = np.sqrt(e1*sin2 - e2)
        k3 = np.sqrt(e1*sin2 - e3)
        k4 = np.sqrt(e1*sin2 - e4)
        # avoid division by zero; assume non-zero
        d1 = e1/k1
        d2 = e2/k2 if k2 != 0 else 0.0
        d3 = e3/k3 if k3 != 0 else 0.0
        d4 = e4/k4 if k4 != 0 else 0.0
        exp_film = np.exp(-2.0 * k3 * d_film_cm * 2.0 * np.pi * nu)
        if l_gap_cm > 0:
            exp_gap = np.exp(-2.0 * k2 * l_gap_cm * 2.0 * np.pi * nu)
        else:
            exp_gap = 1.0
        M = (d2 + d3)*(d3 + d4) + (d2 - d3)*(d3 - d4)*exp_gap
        N = ((d2 - d3)*(d3 + d4) + (d2 + d3)*(d3 - d4)*exp_gap)*exp_film
        numer = (d1 - d2)*M + (d1 + d2)*N
        denom = (d1 + d2)*M + (d1 - d2)*N
        if denom == 0:
            A_val = 1.0
        else:
            A_val = 1 - np.abs(numer/denom)**2
        A[i] = A_val.real
    return A


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
    return {
        'c_cm_s': 2.99792458e10,
        'phi_deg': 20.0,
    }


# === block: score_0 (check id='dispersion') ===
def score_0(artifact, step, ctx):
        rad_count = 0
        nonrad_count = 0
        correct = 0
        total = 0
        for row in artifact:
            q = float(row['in_plane_wavevector_q'])
            wn = float(row['wavenumber'])
            is_radiative = (q <= 2.0 * math.pi * wn)
            bt = row.get('branch_type', '').strip().lower()
            if bt not in ('radiative', 'nonradiative'):
                continue
            total += 1
            if (bt == 'radiative' and is_radiative) or (bt == 'nonradiative' and not is_radiative):
                correct += 1
            if bt == 'radiative':
                rad_count += 1
            else:
                nonrad_count += 1
        if rad_count == 0 or nonrad_count == 0:
            return 0.0
        if total == 0:
            return 0.0
        return float(correct) / total


# === block: score_1 (check id='absorption_ideal') ===
def score_1(artifact, step, ctx):
    import numpy as np
    from scipy.signal import find_peaks

    def score(artifact, step, ctx):
        d_film_cm = 10e-4  # 10 um -> 0.001 cm
        wp = 120000.0
        gamma = 1000.0
        def eps_sub(nu):
            return 1 - wp**2 / (nu**2 + 1j*gamma*nu)
        eps_film = 5.8
        nu_min = 100.0
        nu_max = 800.0
        nu_step = 0.5
        nu_ref = np.arange(nu_min, nu_max, nu_step)
        ref_abs = compute_absorption(nu_ref, 1.0, 1.0, eps_film, eps_sub, d_film_cm, 0.0, np.deg2rad(ctx['phi_deg']))
        peak_ind, _ = find_peaks(ref_abs, prominence=0.01, distance=10)
        ref_peaks_nu = nu_ref[peak_ind]
        ref_peaks_abs = ref_abs[peak_ind]
        if len(ref_peaks_nu) == 0:
            return 1.0  # no peaks expected; but shouldn't happen
        agent_nu = np.array([float(r['wavenumber']) for r in artifact])
        agent_abs = np.array([float(r['absorption']) for r in artifact])
        idx = np.argsort(agent_nu)
        agent_nu = agent_nu[idx]
        agent_abs = agent_abs[idx]
        agent_prom = 0.01 if np.max(agent_abs) > 0.02 else 0.001
        agent_peaks, _ = find_peaks(agent_abs, prominence=agent_prom, distance=10)
        agent_nu_peaks = agent_nu[agent_peaks]
        agent_abs_peaks = agent_abs[agent_peaks]
        tol = 5.0
        matched = 0
        for r_nu, r_abs in zip(ref_peaks_nu, ref_peaks_abs):
            if len(agent_nu_peaks) == 0:
                break
            diffs = np.abs(agent_nu_peaks - r_nu)
            best_i = np.argmin(diffs)
            if diffs[best_i] <= tol:
                ratio = agent_abs_peaks[best_i] / r_abs if r_abs > 0 else 1.0
                if 0.8 <= ratio <= 1.2:
                    matched += 1
        return matched / float(len(ref_peaks_nu))


# === block: score_2 (check id='absorption_ZnTe') ===
def score_2(artifact, step, ctx):
    import numpy as np
    from scipy.signal import find_peaks

    def score(artifact, step, ctx):
        d_film_cm = 2e-4  # 2 um
        w_TO = 177.0
        w_LO = 205.0
        eps0 = 9.6
        eps_inf = 7.0
        gamma_zn = 5.0
        def eps_film(nu):
            return eps_inf + (eps0 - eps_inf) * w_TO**2 / (w_TO**2 - nu**2 - 1j*gamma_zn*nu)
        wp = 120000.0
        ga = 1000.0
        def eps_sub(nu):
            return 1 - wp**2 / (nu**2 + 1j*ga*nu)
        nu_min = 100.0
        nu_max = 500.0
        nu_step = 0.5
        nu_ref = np.arange(nu_min, nu_max, nu_step)
        ref_abs = compute_absorption(nu_ref, 1.0, 1.0, eps_film, eps_sub, d_film_cm, 0.0, np.deg2rad(ctx['phi_deg']))
        peak_ind, _ = find_peaks(ref_abs, prominence=0.02, distance=10)
        ref_peaks_nu = nu_ref[peak_ind]
        ref_peaks_abs = ref_abs[peak_ind]
        if len(ref_peaks_nu) == 0:
            return 1.0
        agent_nu = np.array([float(r['wavenumber']) for r in artifact])
        agent_abs = np.array([float(r['absorption']) for r in artifact])
        idx = np.argsort(agent_nu)
        agent_nu = agent_nu[idx]
        agent_abs = agent_abs[idx]
        agent_prom = 0.01 if np.max(agent_abs) > 0.02 else 0.001
        agent_peaks, _ = find_peaks(agent_abs, prominence=agent_prom, distance=10)
        agent_nu_peaks = agent_nu[agent_peaks]
        agent_abs_peaks = agent_abs[agent_peaks]
        tol = 5.0
        matched = 0
        for r_nu, r_abs in zip(ref_peaks_nu, ref_peaks_abs):
            if len(agent_nu_peaks) == 0:
                break
            diffs = np.abs(agent_nu_peaks - r_nu)
            best_i = np.argmin(diffs)
            if diffs[best_i] <= tol:
                ratio = agent_abs_peaks[best_i] / r_abs if r_abs > 0 else 1.0
                if 0.8 <= ratio <= 1.2:
                    matched += 1
        return matched / float(len(ref_peaks_nu))


# === block: score_3 (check id='absorption_CdZnTe') ===
def score_3(artifact, step, ctx):
    import numpy as np
    from scipy.signal import find_peaks

    def score(artifact, step, ctx):
        d_film_cm = 2e-4
        w_TO = 177.0
        w_LO = 205.0
        eps0 = 9.6
        eps_inf = 7.0
        gamma_zn = 5.0
        def eps_film_pure(nu):
            return eps_inf + (eps0 - eps_inf) * w_TO**2 / (w_TO**2 - nu**2 - 1j*gamma_zn*nu)
        wp = 120000.0
        ga = 1000.0
        def eps_sub(nu):
            return 1 - wp**2 / (nu**2 + 1j*ga*nu)
        nu_min = 100.0
        nu_max = 500.0
        nu_step = 0.5
        nu_ref = np.arange(nu_min, nu_max, nu_step)
        ref_abs = compute_absorption(nu_ref, 1.0, 1.0, eps_film_pure, eps_sub, d_film_cm, 0.0, np.deg2rad(ctx['phi_deg']))
        peak_ind, _ = find_peaks(ref_abs, prominence=0.02, distance=10)
        ref_peaks_nu = nu_ref[peak_ind]
        ref_peaks_abs = ref_abs[peak_ind]
        if len(ref_peaks_nu) == 0:
            return 0.0
        target_nu = 170.0
        diffs_target = np.abs(ref_peaks_nu - target_nu)
        closest_i = np.argmin(diffs_target)
        ref_nu_im = ref_peaks_nu[closest_i]
        ref_abs_im = ref_peaks_abs[closest_i]
        agent_nu = np.array([float(r['wavenumber']) for r in artifact])
        agent_abs = np.array([float(r['absorption']) for r in artifact])
        idx = np.argsort(agent_nu)
        agent_nu = agent_nu[idx]
        agent_abs = agent_abs[idx]
        agent_prom = 0.02 if np.max(agent_abs) > 0.05 else 0.005
        agent_peaks, _ = find_peaks(agent_abs, prominence=agent_prom, distance=10)
        agent_peaks_nu = agent_nu[agent_peaks]
        agent_peaks_abs = agent_abs[agent_peaks]
        if len(agent_peaks_nu) == 0:
            return 0.0
        diffs = np.abs(agent_peaks_nu - ref_nu_im)
        best_i = np.argmin(diffs)
        if diffs[best_i] > 5.0:
            return 0.0
        agent_abs_im = agent_peaks_abs[best_i]
        if agent_abs_im >= 1.2 * ref_abs_im and agent_abs_im > 0.2:
            return 1.0
        elif agent_abs_im > 0.1:
            return 0.5
        return 0.0


_SCORERS = {
    'dispersion': score_0,
    'absorption_ideal': score_1,
    'absorption_ZnTe': score_2,
    'absorption_CdZnTe': score_3,
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
