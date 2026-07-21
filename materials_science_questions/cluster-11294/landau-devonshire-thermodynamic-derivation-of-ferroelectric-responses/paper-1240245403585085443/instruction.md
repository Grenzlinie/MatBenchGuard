# Viscoelectric coefficient from HB-network Brownian model

## Problem background
Water exhibits a viscoelectric effect: its viscosity increases under an applied electric field. A recently proposed coarse-grained theory models the slow collective dynamics of hydrogen-bond (HB) network segments as orientable Brownian particles embedded in a molecular lattice-gas electrolyte. The theory yields a dipolar Poisson–Nernst–Planck–Stokes (dPNP–S) continuum model that connects molecular structural information to electrohydrodynamic phenomena. It provides a closed-form expression for the viscoelectric coefficient f_v, which quantifies the field-dependent viscosity change. In this task you will compute f_v from the Brownian-particle model and compare it with the experimental measurement reported by Jin et al. (Proc. Natl. Acad. Sci. 2022).

## Approach
The computation follows two stages. First, determine the parameters of the equivalent Brownian particles (concentration c_B, rotational friction ζ_B^r, effective dipole moment p_0B, coupling factor χ̄, background fluid viscosity η_f, and others) from published experimental and molecular-dynamics data. Second, use these parameters together with the experimental conditions of Jin et al. to compute the viscoelectric coefficient. This requires solving the 1D Poisson–Boltzmann equation to obtain the surface electric field E_s, evaluating the correction factors L_E = (E_s/E₀)² and L_m (which account for the difference between the nominal field and the actual surface field, and for bulk averaging), and then combining them with the Brownian-particle base coefficient f_vB to obtain f_v = L_E L_m f_vB.

## Reproduction target
Compute the viscoelectric coefficient f_v (in m²/V²) from the Brownian-particle model for the specified experimental conditions. Implement the two steps: (1) derive the Brownian-particle parameters from the given data; (2) solve the 1D Poisson–Boltzmann equation, evaluate the correction factors, compute f_vB and f_v, and save the result together with the intermediate quantities (f_vB, L_E, L_m, E_s) in the scored output file step_01_viscoelectric.json. Report f_v as the main quantity; the hidden verifier will compare your computed value against an acceptable range derived from the literature.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Calculate Brownian-particle parameters from literature data
- Role: process
- Action: Using the data and formulas below, compute all necessary parameters for the Brownian-particle model.  Keep these values in memory; they will be used in Step 2.

#### 1.1 Coarse‑graining and concentration
- Coarse‑graining radius of a HB‑network segment: R_B = 2.25 × 10⁻⁹ m (2.25 nm).
- Each Brownian particle occupies a cube of side R_B, so its concentration (number per m³) is
  c_B = 1 / R_B³.
- The equivalent number of water molecules per Brownian particle is n_B ≈ 3020.

#### 1.2 Effective Brownian dipole moment p_0B
- From field‑induced reorganisation experiments (Zong et al.): applying a strong electric field change δ│E│ ≈ 1 V/nm induces a free‑energy shift δ(ΔG) ≈ 600 J/mol in the hydrogen‑bond network.
- The energy per Brownian particle is δ(ΔG) × (n_B / N_A), where N_A = 6.02214076 × 10²³ mol⁻¹.
- This energy is treated as a linear field‑energy coupling: δ(ΔG) (n_B / N_A) ≈ p_0B δ│E│.
- Therefore the magnitude of the virtual Brownian dipole moment is
  p_0B = δ(ΔG) × (n_B / N_A) / δ│E│.
- Evaluating this with the given numbers yields p_0B ≅ 633 Debye.
- Convert to SI: 1 D (Debye) = 3.33564 × 10⁻³⁰ C·m, so p_0B = 633 × 3.33564e-30 C·m.

#### 1.3 Rotational friction coefficient ζ_B^r and shape anisotropy δ_B
- The Debye-like rotational relaxation time of the HB network measured by dielectric spectroscopy is τ_r,B = 29.5 ns (29.5 × 10⁻⁹ s).
- For a Brownian rotator, the first‑order relaxation time relates to the rotational friction via
  τ_r,B = ζ_B^r / (2 k_B T),        (1)
  where k_B = 1.380649 × 10⁻²³ J/K is the Boltzmann constant and T = 298 K.
- Hence the isotropic rotational friction is
  ζ_B^r = 2 k_B T τ_r,B.
- The small geometric anisotropy of the equivalent Brownian particle is quantified by δ_B = 0.0273 (obtained by matching the full rotational diffusion expression to the experimental τ_r,B).
- The coupling factor that enters the viscoelectric coefficient is taken as
  χ̄ = δ_B / 2.

#### 1.4 Other parameters
- Zero‑field solvent viscosity (water): η₀ = 8.9 × 10⁻⁴ Pa·s (at T = 298 K).
- Molecular dipole moment estimate (for completeness only; not directly used in the final expression): │p̄│ ≈ 2.1 D.  This gives α₁ = p_0B / (n_B │p̄│) ≈ 0.1.

### Step 2: Compute the viscoelectric coefficient f_v
- Role: scored (load-bearing)
- Action: Take the Brownian-particle parameters from Step 1.  For the experimental conditions of Jin et al., solve the 1D Poisson–Boltzmann equation to obtain the surface electric field E_s, compute the correction factors L_E and L_m, then calculate the viscoelectric coefficient f_v.  Save the result and all intermediates to the output file.

#### 2.1 Experimental geometry and nominal field
- Electrode potentials: V₁ = −150 mV, V₂ = +100 mV.
- Electrode gap: L = 57.5 nm = 57.5 × 10⁻⁹ m.
- Potential difference: ΔV = V₂ − V₁ = 250 mV = 0.25 V.
- Nominal electric field (uniform‑field approximation): E₀ = ΔV / L.
  Compute E₀ in V/m.

#### 2.2 1D Poisson–Boltzmann equation and surface field E_s
- The aqueous solution is a symmetric 1:1 electrolyte with bulk concentration c₀ = 0.08 mM = 0.08 mol/m³.
- Relative permittivity of water: ε_r = 80.
- Vacuum permittivity: ε₀ = 8.8541878128 × 10⁻¹² F/m.
- Elementary charge: e = 1.602176634 × 10⁻¹⁹ C.
- The 1D Poisson–Boltzmann equation for the electrostatic potential ψ(x) between two planar electrodes is:
  ε₀ ε_r d²ψ / dx² = − 2 e c₀ N_A sinh( e ψ / (k_B T) ).
  with boundary conditions:
    ψ(0) = V₁,   ψ(L) = V₂.
- Solve this ODE numerically (e.g., using finite differences or a shooting method) on the interval 0 ≤ x ≤ L.  From the solution obtain the electric field at the left electrode:
    E_s = − dψ/dx |_{x=0}.
  (The magnitude of the field is │E_s│; use its absolute value in the subsequent formulas.)

#### 2.3 Correction factors
- Field‑magnitude correction:
    L_E = (E_s / E₀)².
- Volumetric averaging factor (MLB model): in the limit of low concentration and symmetric electrodes, the bulk‑averaging factor is
    L_m = 1/3.

#### 2.4 Viscoelectric coefficient
- Thermal energy scale: β = 1 / (k_B T).
- Base viscoelectric coefficient from the Brownian‑particle model:
    f_vB = c_B ζ_B^r χ̄ β² p_0B² / (315 η₀).
- Full viscoelectric coefficient:
    f_v = L_E L_m f_vB.

- Output file: `/app/outputs/step_01_viscoelectric.json`
- Format: json
- Contract: {"f_v": float (m²/V²), "f_vB": float (m²/V²), "L_E": float (dimensionless), "L_m": float (dimensionless), "E_s": float (V/m)}
- Scoring: scored by hidden verifier

## Output files
Write the following artifact under `/app/outputs`:
- `/app/outputs/step_01_viscoelectric.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_viscoelectric.json
- path: `/app/outputs/step_01_viscoelectric.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Viscoelectric coefficient computed from the Brownian-particle model together with intermediate quantities: base coefficient f_vB, correction factors L_E and L_m, and surface electric field E_s. The checker compares f_v against a hidden acceptable range via threshold_or_better.
- schema:
  - `type`: object
  - `required`:
    - `f_v`: float, m²/V²
    - `f_vB`: float, m²/V²
    - `L_E`: float, dimensionless
    - `L_m`: float, dimensionless
    - `E_s`: float, V/m

Notes: Only the viscoelectric coefficient is scored; the electrostrictive pressure and numerical flow simulations are omitted per scope (no exact numerical gold or external mandatory parameters). The output includes intermediate values for completeness and possible consistency checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_viscoelectric.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "f_v": "float, m²/V²",
          "f_vB": "float, m²/V²",
          "L_E": "float, dimensionless",
          "L_m": "float, dimensionless",
          "E_s": "float, V/m"
        }
      },
      "description": "Viscoelectric coefficient computed from the Brownian-particle model together with intermediate quantities: base coefficient f_vB, correction factors L_E and L_m, and surface electric field E_s. The checker compares f_v against a hidden acceptable range via threshold_or_better."
    }
  ],
  "notes": "Only the viscoelectric coefficient is scored; the electrostrictive pressure and numerical flow simulations are omitted per scope (no exact numerical gold or external mandatory parameters). The output includes intermediate values for completeness and possible consistency checks."
}
```

## How you are scored
The hidden verifier reads your output file step_01_viscoelectric.json and compares the reported f_v value against a hidden acceptable range. It may also cross-check internal consistency by recomputing f_v from the intermediate quantities (f_vB, L_E, L_m) that you provided. Your reward is based on how close your result is to the target range; if the value falls within the range you earn full credit, and credit decays if the value lies outside. Simply reporting numbers without actually performing the required computations will not satisfy the consistency checks. The verifier runs automatically and no human judgment is involved.