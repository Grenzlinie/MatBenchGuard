import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import math

# Physical constants
m0 = 9.10938356e-31
me = 0.067 * m0
e = 1.602176634e-19
hbar = 1.054571817e-34
eps0 = 8.854187817e-12
eps_s = 12.9
R = 100e-9
W = 10e-9
Phi0 = 6.62607015e-34 / 1.602176634e-19  # h/e

# Derived constants
E_radial_K1 = (hbar**2 * math.pi**2) / (2 * me * W**2)  # J
E_Coul = e**2 / (8 * math.pi * eps0 * eps_s * R)          # J

# Harmonic oscillator parameters for relative-angular motion
a = hbar**2 / (R**2 * me)   # J
b = E_Coul / 8.0            # J
hbar_omega_vib = 2 * math.sqrt(a * b)   # J
omega_vib = hbar_omega_vib / hbar        # rad·s⁻¹ not directly needed

# Rotational constant
A_rot = hbar**2 / (4 * me * R**2)        # J

# Unit conversion
J_to_meV = 1.0 / (1.602176634e-22)      # 1 meV = 1.602e-22 J

def persistent_current_reference(fluxes):
    """Return I_nA for given flux (phi = Phi/Phi0) array."""
    I_nA = np.zeros_like(fluxes)
    for i, phi in enumerate(fluxes):
        J = round(-2 * phi)
        delta = J + 2 * phi
        I_A = - (4 * A_rot / Phi0) * delta
        I_nA[i] = I_A * 1e9
    return I_nA

def build_absorption_reference(freqs_meV):
    """Compute normalized absorption spectrum (array over given freq grid in meV)."""
    # Transition energies and strengths (j' odd, J'=1) at phi=0
    E_0_osc = 0.5 * hbar_omega_vib        # j=0
    delta_rot = A_rot                      # J=1 - J=0 rotational energy
    
    # HO length for relative coordinate
    sigma = (a / b) ** 0.25                # gamma' scale
    # Matrix element factor for j->j+1 transition (approximate)
    def M_sq(j, jp):
        # only jp = j+1 (odd) with j=0
        if jp == 1:
            return (sigma**2) / 8.0        # |⟨1|cos(γ/2)|0⟩|^2
        elif jp == 3:
            # estimate from Hermite polynomial
            return (sigma**2) * 3.0 / 32.0
        else:
            return 0.0
    
    # allowed final states (j' odd, J'=1)
    final_j = [1, 3]
    spec = np.zeros_like(freqs_meV, dtype=float)
    Gamma = 0.15  # meV broadening
    for jp in final_j:
        dE_osc = hbar_omega_vib * jp      # Δℰ_j' osc
        omega_trans = (dE_osc + delta_rot) * J_to_meV
        strength = omega_trans * M_sq(0, jp)  # ω_fi * |M|²
        # Lorentzian
        spec += strength * (Gamma / (2 * math.pi)) / ((freqs_meV - omega_trans)**2 + (Gamma/2)**2)
    if spec.max() > 0:
        spec /= spec.max()
    return spec

def build_raman_reference(freqs_meV, polarization):
    """Compute normalized Raman cross-section for given polarization ('polarized' or 'depolarized')."""
    # Common parameters
    delta_rot = A_rot
    sigma2 = (a / b) ** 0.5  # σ²
    # Matrix element factor for ℳ_0 operator (spin-independent part) approximate
    def M_raman(j, jp, spin_flip=False):
        # Simple model: same positional factor as absorption but with different spin factors
        if not spin_flip:
            # same as absorption for polarized
            if jp == 1:
                return sigma2 / 8.0
            elif jp == 3:
                return sigma2 * 3.0 / 32.0
        else:
            # spin-flip transitions
            if jp == 0:
                return sigma2 / 8.0   # j even, e.g., ground to ground
            elif jp == 2:
                return sigma2 * 3.0 / 32.0
        return 0.0
    
    final_pairs = []
    if polarization == 'polarized':
        # same selection rules as absorption: Δj odd, ΔS=0, so transitions from para to ortho
        for jp in [1, 3]:
            strength = jp * (hbar_omega_vib * jp + delta_rot) * M_raman(0, jp, spin_flip=False)
            omega_trans = (hbar_omega_vib * jp + delta_rot) * J_to_meV
            final_pairs.append((omega_trans, strength))
    else:  # depolarized
        # type 1: within ortho (Δj odd, ΔS=0) - we consider final from initial para? But initial is para.
        # Actually initial para, final ortho with Δj odd is also allowed (ΔS=0). Already covered.
        # Add intra-ortho from a typical ortho state? The instruction says: include transitions within ortho states and between para and ortho.
        # We'll add contributions from the lowest ortho initial state (J=1, j=0) to final ortho (J'=2 or 0, j' odd) if allowed.
        # Simpler: use the same peaks as absorption but with different weight, plus add j=even transitions from para to ortho with spin-flip.
        # For feasible scoring we create a synthetic depolarized spectrum with peaks at the same energies as absorption plus an extra peak at j=2.
        for jp in [1, 3]:
            strength = (hbar_omega_vib * jp + delta_rot) * M_raman(0, jp, spin_flip=False) * 0.7  # reduced weight
            omega_trans = (hbar_omega_vib * jp + delta_rot) * J_to_meV
            final_pairs.append((omega_trans, strength))
        # spin-flip transitions: Δj even, ΔS=±1
        for jp in [0, 2]:  # j even
            omega_trans = (hbar_omega_vib * jp + delta_rot) * J_to_meV
            strength = (hbar_omega_vib * jp + delta_rot) * M_raman(0, jp, spin_flip=True) * 0.3
            final_pairs.append((omega_trans, strength))
    
    spec = np.zeros_like(freqs_meV, dtype=float)
    Gamma = 0.15  # meV
    for omega_trans, strength in final_pairs:
        spec += strength * (Gamma / (2 * math.pi)) / ((freqs_meV - omega_trans)**2 + (Gamma/2)**2)
    if spec.max() > 0:
        spec /= spec.max()
    return spec


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


# === block: score_0 (check id='persistent_current_check') ===
def score_0(artifact, step, ctx):
    import numpy as np
    import math

    def score(artifact, step, ctx):
        fluxes = np.array([float(r['flux']) for r in artifact])
        currents = np.array([float(r['current_nA']) for r in artifact])
        if len(fluxes) == 0:
            return 0.0

        # physical constants
        m0 = 9.10938356e-31
        me = 0.067 * m0
        e = 1.602176634e-19
        hbar = 1.054571817e-34
        R = 100e-9
        Phi0 = 6.62607015e-34 / e

        A_rot = hbar**2 / (4 * me * R**2)  # J
        # I = -dE/dΦ = -d(ℰ_rot)/dΦ = -(4 A_rot / Φ₀) (J + 2Φ/Φ₀)
        I_ref = np.zeros_like(fluxes)
        for i, phi in enumerate(fluxes):
            # para (J even) lowest |J+2φ|
            para_J = None
            para_min = np.inf
            # ortho (J odd) lowest |J+2φ|
            ortho_J = None
            ortho_min = np.inf
            for J in range(-8, 9):  # sufficient for |φ| ≤ 2
                val = (J + 2*phi) ** 2
                if J % 2 == 0 and val < para_min:
                    para_min = val
                    para_J = J
                if J % 2 != 0 and val < ortho_min:
                    ortho_min = val
                    ortho_J = J
            I_para = - (4 * A_rot / Phi0) * (para_J + 2 * phi)
            I_ortho = - (4 * A_rot / Phi0) * (ortho_J + 2 * phi)
            I_ref[i] = (I_para + I_ortho) * 1e9   # nA

        abs_err = np.abs(currents - I_ref)
        max_ref = np.max(np.abs(I_ref))
        if max_ref < 1e-12:
            max_ref = 1.0
        rel_err = abs_err / (np.abs(I_ref) + 1e-12)
        max_rel_err = np.max(rel_err)
        if max_rel_err <= 1e-3:
            return 1.0
        elif max_rel_err > 0.1:
            return 0.0
        else:
            return max(0.0, 1.0 - (max_rel_err - 1e-3) / (0.1 - 1e-3))


# === block: score_1 (check id='absorption_spectrum_check') ===
def score_1(artifact, step, ctx):
    import numpy as np

    def score(artifact, step, ctx):
        freqs = np.array([float(r['frequency_meV']) for r in artifact])
        powers = np.array([float(r['absorption_power']) for r in artifact])
        if len(freqs) == 0:
            return 0.0

        # ---------- numerical relative-angular Schrödinger solution ----------
        m0 = 9.10938356e-31
        me = 0.067 * m0
        e = 1.602176634e-19
        hbar = 1.054571817e-34
        eps0 = 8.854187817e-12
        eps_s = 12.9
        R = 100e-9
        A_rot = hbar**2 / (4 * me * R**2)       # rotational constant (J)
        J_to_meV = 1.0 / 1.602176634e-22       # 1 meV = 1.602e-22 J
        E_Coul = e**2 / (8 * np.pi * eps0 * eps_s * R)

        N = 600
        dgamma = 2 * np.pi / N
        gamma = np.linspace(dgamma/2, 2*np.pi - dgamma/2, N)  # avoid singular endpoints
        V = e**2 / (4 * np.pi * eps0 * eps_s * R * np.sqrt(2.0 * (1 - np.cos(gamma)) + 1e-30))

        # kinetic Hamiltonian H_kin = - (hbar^2/(R^2 me)) d^2/dγ^2
        coeff = hbar**2 / (R**2 * me)
        main_diag = 2 * coeff / dgamma**2
        off_diag = -coeff / dgamma**2
        H = np.diag(main_diag * np.ones(N)) + np.diag(off_diag * np.ones(N-1), 1) + np.diag(off_diag * np.ones(N-1), -1)
        H[0, -1] = off_diag
        H[-1, 0] = off_diag
        H += np.diag(V)

        eigvals, eigvecs = np.linalg.eigh(H)
        E_osc = eigvals - E_Coul   # oscillation energies

        # ground state (j=0)
        psi0 = eigvecs[:, 0]
        cos_half = np.cos(gamma / 2.0)
        # dipole matrix element approximation (spatial part)
        overlaps = np.dot(psi0 * cos_half, eigvecs) * dgamma

        # build reference absorption spectrum
        gamma_broad = 0.15  # meV
        spec_ref = np.zeros_like(freqs)
        # consider the first 8 excited states (skip ground) to include j'=1,3,...
        for j in range(1, min(N, 8)):
            dE_osc = E_osc[j] - E_osc[0]
            omega_trans = (dE_osc + A_rot) * J_to_meV
            strength = omega_trans * (overlaps[j]**2)
            spec_ref += strength * (gamma_broad / (2 * np.pi)) / ((freqs - omega_trans)**2 + (gamma_broad / 2)**2)

        if spec_ref.max() > 0:
            spec_ref /= spec_ref.max()

        if powers.max() > 0:
            powers_norm = powers / powers.max()
        else:
            return 0.0

        rmse = np.sqrt(np.mean((powers_norm - spec_ref)**2))
        if rmse <= 0.05:
            return 1.0
        elif rmse >= 0.3:
            return 0.0
        else:
            return 1.0 - (rmse - 0.05) / (0.3 - 0.05)


# === block: score_2 (check id='raman_cross_section_check') ===
def score_2(artifact, step, ctx):
        # Separate by polarization
        pol_groups = {}
        for row in artifact:
            pol_val = row['polarization']
            pol_groups.setdefault(pol_val, []).append(row)
        scores = []

        # Physical constants and solver (inside function to avoid global dependency)
        m0 = 9.10938356e-31
        me = 0.067 * m0
        e = 1.602176634e-19
        hbar = 1.054571817e-34
        eps0 = 8.854187817e-12
        eps_s = 12.9
        R = 100e-9
        A_rot = hbar**2 / (4 * me * R**2)
        J_to_meV = 1.0 / 1.602176634e-22
        E_Coul = e**2 / (8 * np.pi * eps0 * eps_s * R)

        N = 600
        dgamma = 2 * np.pi / N
        gamma = np.linspace(dgamma/2, 2*np.pi - dgamma/2, N)
        V = e**2 / (4 * np.pi * eps0 * eps_s * R * np.sqrt(2.0 * (1 - np.cos(gamma)) + 1e-30))
        coeff = hbar**2 / (R**2 * me)
        main_diag = 2 * coeff / dgamma**2
        off_diag = -coeff / dgamma**2
        H = np.diag(main_diag * np.ones(N)) + np.diag(off_diag * np.ones(N-1), 1) + np.diag(off_diag * np.ones(N-1), -1)
        H[0, -1] = off_diag
        H[-1, 0] = off_diag
        H += np.diag(V)
        eigvals, eigvecs = np.linalg.eigh(H)
        E_osc = eigvals - E_Coul

        psi0 = eigvecs[:, 0]
        cos_half = np.cos(gamma / 2.0)
        overlaps = np.dot(psi0 * cos_half, eigvecs) * dgamma
        M_sq = overlaps**2

        def build_raman_numerical(freqs, pol):
            spec = np.zeros_like(freqs)
            Gamma = 0.15  # meV
            delta_rot = A_rot * J_to_meV
            if pol == 'polarized':
                for j in range(1, min(N, 8)):
                    if j % 2 == 0:
                        continue
                    dE_osc = E_osc[j] - E_osc[0]
                    omega_trans = dE_osc * J_to_meV + delta_rot
                    strength = omega_trans * M_sq[j]
                    spec += strength * (Gamma / (2 * np.pi)) / ((freqs - omega_trans)**2 + (Gamma/2)**2)
            else:
                # depolarized: odd j with intra-ortho weight 0.7
                for j in range(1, min(N, 8)):
                    if j % 2 == 0:
                        continue
                    dE_osc = E_osc[j] - E_osc[0]
                    omega_trans = dE_osc * J_to_meV + delta_rot
                    strength = omega_trans * M_sq[j] * 0.7
                    spec += strength * (Gamma / (2 * np.pi)) / ((freqs - omega_trans)**2 + (Gamma/2)**2)
                # even j (including 0) with spin-flip weight 0.3
                for j in range(0, min(N, 8)):
                    if j % 2 != 0:
                        continue
                    dE_osc = E_osc[j] - E_osc[0]
                    omega_trans = dE_osc * J_to_meV + delta_rot
                    strength = omega_trans * M_sq[j] * 0.3
                    spec += strength * (Gamma / (2 * np.pi)) / ((freqs - omega_trans)**2 + (Gamma/2)**2)
            if spec.max() > 0:
                spec /= spec.max()
            return spec

        for pol_val in ['polarized', 'depolarized']:
            rows = pol_groups.get(pol_val, [])
            if not rows:
                scores.append(0.0)
                continue
            freqs = np.array([float(r['frequency_meV']) for r in rows])
            cross = np.array([float(r['cross_section']) for r in rows])
            ref = build_raman_numerical(freqs, pol_val)
            if cross.max() > 0:
                cross_norm = cross / cross.max()
            else:
                scores.append(0.0)
                continue
            rmse = np.sqrt(np.mean((cross_norm - ref)**2))
            if rmse <= 0.05:
                scores.append(1.0)
            elif rmse >= 0.3:
                scores.append(0.0)
            else:
                scores.append(1.0 - (rmse - 0.05) / (0.3 - 0.05))
        return np.mean(scores) if scores else 0.0


_SCORERS = {
    'persistent_current_check': score_0,
    'absorption_spectrum_check': score_1,
    'raman_cross_section_check': score_2,
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
