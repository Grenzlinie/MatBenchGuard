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


# === block: score_0 (check id='bulk_gap_direct') ===
def score_0(artifact, step, ctx):
    import math
    rows = artifact
    # identify Gamma point: allow various labels
    gamma_labels = {'Γ','gamma','g','G','GAMMA'}
    vb_energies = []
    cb_energies = []
    for r in rows:
        label = r.get('k_label','').strip()
        if label and label in gamma_labels:
            e = float(r['energy'])
            if e <= 0:
                vb_energies.append(e)
            else:
                cb_energies.append(e)
    if not vb_energies or not cb_energies:
        return 0.0
    gap = min(cb_energies) - max(vb_energies)
    target = float(step['target_gap_eV'])
    tol = float(step['tolerance_eV'])
    err = abs(gap - target)
    if err <= tol:
        return 1.0
    # linear decay from tol to 1.0 eV
    if err >= 1.0:
        return 0.0
    return max(0.0, 1.0 - (err - tol) / (1.0 - tol))


# === block: score_1 (check id='bulk_static_epsilon') ===
def score_1(artifact, step, ctx):
    import math
    rows = artifact
    if not rows:
        return 0.0
    # assume CSV is sorted by energy ascending; take the first row (lowest energy)
    first = rows[0]
    R_perp = float(first.get('R_perp', 0.0))
    R_parallel = float(first.get('R_parallel', 0.0))
    def refl_to_eps(R):
        if R <= 0 or R >= 1:
            return None
        sr = math.sqrt(R)
        return ((1+sr)/(1-sr))**2
    eps_perp = refl_to_eps(R_perp)
    eps_par = refl_to_eps(R_parallel)
    if eps_perp is None and eps_par is None:
        return 0.0
    if eps_perp is None:
        eps = eps_par
    elif eps_par is None:
        eps = eps_perp
    else:
        eps = (eps_perp + eps_par) / 2.0
    target = float(step['target_epsilon'])
    tol = float(step['tolerance'])
    err = abs(eps - target)
    if err <= tol:
        return 1.0
    return max(0.0, 1.0 - err / (2*tol))


# === block: score_2 (check id='surface_state_onset') ===
def score_2(artifact, step, ctx):
    rows = artifact
    # filter empty surface states: energy > 0 and state_type indicates surface
    surface_states = []
    for r in rows:
        st = r.get('state_type','').strip().lower()
        e = float(r['energy'])
        if st in ('surface', 'resonance') and e > 0:
            surface_states.append(e)
    if not surface_states:
        return 0.0
    onset = min(surface_states)
    target = float(step['target_onset_eV'])
    tol = float(step['tolerance_eV'])
    err = abs(onset - target)
    if err <= tol:
        return 1.0
    return max(0.0, 1.0 - err / (2*tol))


# === block: score_3 (check id='surface_dispersion_gamma_j') ===
def score_3(artifact, step, ctx):
    rows = artifact
    # Gamma-J is along x (k_y≈0). Find rows with k_y ≈ 0 and empty surface states
    eps = 1e-6
    empty_surface = []
    for r in rows:
        st = r.get('state_type','').strip().lower()
        e = float(r['energy'])
        if st in ('surface', 'resonance') and e > 0:
            ky = float(r['k_y'])
            if abs(ky) <= eps:
                empty_surface.append(e)
    if not empty_surface:
        return 0.0
    energy_range = max(empty_surface) - min(empty_surface)
    target = float(step['target_dispersion_eV'])
    tol = float(step['tolerance_eV'])
    err = abs(energy_range - target)
    if err <= tol:
        return 1.0
    return max(0.0, 1.0 - err / (2*tol))


# === block: score_4 (check id='surface_dispersion_jk_flat') ===
def score_4(artifact, step, ctx):
    rows = artifact
    # identify J point as maximum k_x (endpoint of Γ-J). Use ± small epsilon.
    if not rows:
        return 0.0
    kxs = [float(r['k_x']) for r in rows]
    kx_j = max(kxs)
    eps = 1e-6
    energies_at_j = []
    for r in rows:
        kx = float(r['k_x'])
        st = r.get('state_type','').strip().lower()
        e = float(r['energy'])
        if st in ('surface', 'resonance') and e > 0:
            if abs(kx - kx_j) <= eps:
                energies_at_j.append(e)
    if not energies_at_j:
        return 0.0
    range_j = max(energies_at_j) - min(energies_at_j)
    max_range = float(step['max_energy_range_eV'])
    if range_j <= max_range:
        return 1.0
    return max(0.0, 1.0 - (range_j - max_range) / (2*max_range))


# === block: score_5 (check id='dos_resonances') ===
def score_5(artifact, step, ctx):
    rows = artifact
    # find peaks in total DOS within [-2.5, -0.5]
    if not rows:
        return 0.0
    energies = [float(r['energy']) for r in rows]
    totals = [float(r['total']) for r in rows]
    # simple peak detection: local maxima where value > neighbours
    peaks = []
    for i in range(1, len(energies)-1):
        if energies[i] < -2.5 or energies[i] > -0.5:
            continue
        if totals[i] > totals[i-1] and totals[i] > totals[i+1]:
            peaks.append(energies[i])
    targets = step['target_peaks_eV']  # list of two target energies
    tol = float(step['tolerance_eV'])
    found = 0
    for t in targets:
        for p in peaks:
            if abs(p - t) <= tol:
                found += 1
                break
    # score: 1.0 if both found, 0.5 if one found, else 0.0
    if found == len(targets):
        return 1.0
    elif found >= 1:
        return 0.5
    return 0.0


# === block: score_6 (check id='dielectric_onset') ===
def score_6(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    energies = [float(r['energy']) for r in rows]
    eps2_x = [float(r['eps2_x']) for r in rows]
    # onset defined as first energy where eps2_x > 0.01
    threshold = 0.01
    onset = None
    for e, ex in zip(energies, eps2_x):
        if ex > threshold:
            onset = e
            break
    if onset is None:
        onset = max(energies) # not meaningful
        return 0.0
    target = float(step['target_onset_eV'])
    tol = float(step['tolerance_eV'])
    err = abs(onset - target)
    if err <= tol:
        return 1.0
    return max(0.0, 1.0 - err / (2*tol))


# === block: score_7 (check id='dielectric_peak_4eV') ===
def score_7(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    energies = [float(r['energy']) for r in rows]
    eps2_x = [float(r['eps2_x']) for r in rows]
    # find maximum eps2_x in energy window [2.5, 5.5]
    best_energy = None
    best_val = -1
    for e, ex in zip(energies, eps2_x):
        if 2.5 <= e <= 5.5:
            if ex > best_val:
                best_val = ex
                best_energy = e
    if best_energy is None:
        return 0.0
    target = float(step['target_peak_eV'])
    tol = float(step['tolerance_eV'])
    err = abs(best_energy - target)
    if err <= tol:
        return 1.0
    return max(0.0, 1.0 - err / (2*tol))


# === block: score_8 (check id='dielectric_anisotropy') ===
def score_8(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    # consider energy range [2.7, 8.0] where both signals expected
    count = 0
    x_larger = 0
    for r in rows:
        e = float(r['energy'])
        if 2.7 <= e <= 8.0:
            ex = float(r['eps2_x'])
            ey = float(r['eps2_y'])
            if ex > ey + 1e-12:
                x_larger += 1
            count += 1
    if count == 0:
        return 0.0
    return x_larger / count


_SCORERS = {
    'bulk_gap_direct': score_0,
    'bulk_static_epsilon': score_1,
    'surface_state_onset': score_2,
    'surface_dispersion_gamma_j': score_3,
    'surface_dispersion_jk_flat': score_4,
    'dos_resonances': score_5,
    'dielectric_onset': score_6,
    'dielectric_peak_4eV': score_7,
    'dielectric_anisotropy': score_8,
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
