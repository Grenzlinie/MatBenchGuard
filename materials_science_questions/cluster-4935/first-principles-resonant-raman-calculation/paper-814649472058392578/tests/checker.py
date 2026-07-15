import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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


# === block: score_0 (check id='consistency_audit') ===
def score_0(artifact, step, ctx):
    # Recompute first-order Raman spectra from φ and check normalized RMSE
    import numpy as np

    energy = np.array(artifact['energy_grid'])
    phi = np.array(artifact['response_function'])
    spectra_dict = artifact['Raman_spectra']

    eps = 1e-8
    energy_safe = np.where(np.abs(energy) < eps, eps, energy)

    # Compute S = ∫ φ(E)/E² dE
    S = np.trapz(phi / (energy_safe**2), energy)

    # Time grid (positive)
    tmax = 10.0
    dt = 0.01
    t_pos = np.arange(0, tmax, dt)
    Nt = len(t_pos)
    g_pos = np.zeros(Nt, dtype=complex)
    for i, t_val in enumerate(t_pos):
        integrand = phi * (np.exp(1j * t_val * energy) - 1) / (energy_safe**2)
        g_pos[i] = np.trapz(integrand, energy)
    # Symmetrize t and g
    t_full = np.concatenate((-t_pos[::-1], t_pos))
    g_full = np.concatenate((np.conj(g_pos[::-1]), g_pos))
    gamma = 0.5
    # Absorption spectrum I(ω) on same energy grid
    omega = np.linspace(energy.min(), energy.max(), len(energy))
    I_omega = np.zeros_like(omega)
    for i, w in enumerate(omega):
        integrand = np.exp(g_full + (-1j) * w * t_full - gamma * np.abs(t_full) - S)
        I_omega[i] = np.trapz(integrand.real, t_full)
    # Complex refractive index Φ(ω) = P∫ I(ω')/(ω'−ω) dω'  − iπ I(ω)
    dw = omega[1] - omega[0]
    phi_real = np.zeros_like(omega)
    for i, w in enumerate(omega):
        kernel = np.where(np.abs(omega - w) > 1e-12, 1.0/(omega - w), 0.0)
        phi_real[i] = np.trapz(I_omega * kernel, omega)
    phi_imag = -np.pi * I_omega
    # Interpolator helpers
    def phi_func(x):
        real = np.interp(x, omega, phi_real, left=0.0, right=0.0)
        imag = np.interp(x, omega, phi_imag, left=0.0, right=0.0)
        return real + 1j * imag

    # For each excitation, compute W1, compare with submitted, and collect NMSE
    nmse_list = []
    exc_freqs = step.get('excitation_frequencies', {})
    for key, offset in exc_freqs.items():
        if key not in spectra_dict:
            continue
        orig = np.array(spectra_dict[key])
        # W1(E) = φ(E) / E² * |Φ(offset−E) − Φ(offset)|²   (B=1)
        E = energy_safe  # use safe grid
        phi_val = phi
        # Φ(offset−E) for all E
        args = offset - energy
        phi_at_arg = phi_func(args)
        phi_at_offset = phi_func(offset)
        delta = phi_at_arg - phi_at_offset
        w1_recomp = phi_val / (E**2) * (delta.real**2 + delta.imag**2)
        # normalize both to range for comparison
        scale_orig = orig.max() - orig.min()
        if scale_orig < 1e-12:
            scale_orig = 1.0
        scale_recomp = w1_recomp.max() - w1_recomp.min()
        if scale_recomp < 1e-12:
            scale_recomp = 1.0
        norm_orig = orig / scale_orig
        norm_recomp = w1_recomp / scale_recomp
        mse = np.mean((norm_orig - norm_recomp)**2)
        nmse = np.sqrt(mse)  # already normalized; range ≈1
        nmse_list.append(nmse)

    if len(nmse_list) == 0:
        score = 0.0
    else:
        max_nmse = max(nmse_list)
        if max_nmse < 0.001:
            score = 1.0
        elif max_nmse < 0.01:
            score = 0.5
        else:
            score = 0.0
    return score


# === block: score_1 (check id='shape_correlation') ===
def score_1(artifact, step, ctx):
    import numpy as np

    energy = np.array(artifact['energy_grid'])
    phi = np.array(artifact['response_function'])
    spectra = artifact['Raman_spectra']

    keys = step.get('spectra_keys', [])
    if len(keys) == 0:
        return 0.0

    corrs = []
    for key in keys:
        arr = np.array(spectra[key])
        if len(arr) != len(phi):
            return 0.0
        # compute Pearson r
        r = np.corrcoef(arr, phi)[0, 1]
        corrs.append(r)

    min_r = min(corrs)
    min_corr_target = step.get('min_correlation', 0.95)
    if min_r >= min_corr_target:
        score = 1.0
    else:
        # linear ramp from 0.5 to target
        score = max(0.0, (min_r - 0.5) / (min_corr_target - 0.5))
    return score


# === block: score_2 (check id='peak_position') ===
def score_2(artifact, step, ctx):
    import numpy as np

    energy = np.array(artifact['energy_grid'])
    spectra = artifact['Raman_spectra']
    expected = step.get('expected_shifts', {})
    tol = step.get('tolerance_cm', 2.0)

    correct = 0
    total = 0
    for key, target in expected.items():
        if key not in spectra:
            continue
        arr = np.array(spectra[key])
        idx = np.argmax(arr)
        pos = energy[idx]
        if abs(pos - target) <= tol:
            correct += 1
        total += 1

    if total == 0:
        return 0.0
    score = correct / total
    return score


# === block: score_3 (check id='intensity_ratio') ===
def score_3(artifact, step, ctx):
    import numpy as np

    spectra = artifact['Raman_spectra']
    key1 = 'E0_plus_30'
    key2 = 'E0_plus_50'
    if key1 not in spectra or key2 not in spectra:
        return 0.0

    max1 = np.max(np.array(spectra[key1]))
    max2 = np.max(np.array(spectra[key2]))
    if max2 == 0.0:
        return 0.0
    ratio = max1 / max2
    max_allowed = step.get('max_ratio', 500)
    score = 1.0 if ratio < max_allowed else 0.0
    return score


_SCORERS = {
    'consistency_audit': score_0,
    'shape_correlation': score_1,
    'peak_position': score_2,
    'intensity_ratio': score_3,
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
