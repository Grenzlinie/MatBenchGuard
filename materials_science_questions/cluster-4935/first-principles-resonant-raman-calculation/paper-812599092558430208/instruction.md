# Photon-atom bound state and resonance Raman spectra in photonic band-gap and dispersive media

## Problem background
This work studies resonance Raman scattering from a single three-level atom in the Λ configuration embedded in a material whose electromagnetic density of states exhibits a photonic band gap — either an artificially structured photonic band-gap (PBG) material or a natural frequency-dispersive medium (FDM). In such media, propagating photon modes are forbidden inside a frequency gap, which suppresses spontaneous emission and can give rise to a discrete photon-atom bound state (a dressed state with energy inside the gap). The Rayleigh (elastic) and Stokes (inelastic) scattering spectra are sensitive to the positions of the atomic transition frequencies relative to the band edges, leading to modified lineshapes. The computational task is to determine, for a given set of model parameters, whether a bound state exists and to compute the Rayleigh scattering cross-section as a function of the incident photon frequency detuning for both material types — revealing the influence of the photonic band structure on the scattering response.

## Approach
The system is a three-level atom in the Λ configuration: ground state |0⟩, lower excited |1⟩, and upper excited |2⟩. The |2⟩↔|0⟩ and |2⟩↔|1⟩ transitions are dipole-allowed and couple to Rayleigh and Stokes photon reservoirs, respectively. The reservoirs are characterised by an isotropic dispersion relation that exhibits a gap in the photon density of states. Two model dispersions are considered:

  • PBG: ω(k) = √(k₀²+γ²) ± √((k−k₀)²+γ²), gap centred at ωₒ, band edges ωᵥ=ωₒ−γ, ω꜀=ωₒ+γ, width Δ=2γ.
  • FDM: ω±(k) = ½[(Ω+k) ± √((Ω−k)²+4kΔ)], band edges ωᵥ=Ω−Δ, ω꜀=Ω.

The atomic form factor z(ω) = (dω/dk)⁻¹ captures the modified density of states; it vanishes inside the gap and exhibits singularities near band edges. The self-energy of level |2⟩ is

  Σ(ε) = Σ′(ε) + i Σ″(ε),
  Σ″(ε) = ½[γ₂₀ z(ε) + γ₂₁ z(ε−ω₁₀)],
  Σ′(ε) = P ∫ (dω/2π) [γ₂₀ z(ω)/(ω−ε) + γ₂₁ z(ω)/(ω−ε+ω₁₀)],

where P denotes the Cauchy principal value and γ₂₀,γ₂₁ are free-space decay rates. The Rayleigh scattering cross-section is

  σ_R(ω) ∝ γ₂₀² z(ω)² / { [ω₂₀−ω−Σ′(ω)]² + [Σ″(ω)]² }.

We consider the one-excitation sector and study two regimes:

  (i) Bound-state regime (ω₂₀ = 0.95 ω꜀, inside the gap subinterval G′ = (ωᵥ+ω₁₀, ω꜀)). A discrete photon‑atom bound state exists if the equation ω₂₀−ε−Σ′(ε)=0 has a solution inside G′ where Σ″(ε)=0.

  (ii) Continuous-spectrum regime (ω₂₀ = 1.2 ω꜀, far above the gap). We compute σ_R(ω) for various Stokes transition frequencies ω₂₁ to probe how the lineshape changes as ω₂₁ approaches the upper band edge.

The parameters are: ωₒ=1 (midgap), gap ratio r=15% ⇒ Δ=0.15, ωᵥ=0.925, ω꜀=1.075, ω₁₀=Δ/10=0.015, γ₂₀=γ₂₁=Δ/100=0.0015. The approach is to implement the PBG and FDM form factors, numerically compute Σ′(ε) and Σ″(ε) on a dense grid, then perform root-finding for the bound state and evaluate σ_R(ω) over a fine detuning mesh.

## Reproduction target
Produce the following three output files:

  • /app/outputs/bound_state_result.json: a JSON object with keys pbg_bound_state_exists (boolean), pbg_eigenvalue (float or null), fdm_bound_state_exists (boolean), fdm_eigenvalue (float or null). Use the PBG and FDM self-energies with ω₂₀=0.95 ω꜀. Determine whether a root of ω₂₀−ε−Σ′(ε)=0 exists in G′ and record the eigenvalue if present; otherwise null.

  • /app/outputs/rayleigh_spectrum_pbg.csv: a CSV with columns omega_minus_omega20, omega21, sigma_R. Compute the Rayleigh cross-section σ_R(ω) using the PBG self-energy with ω₂₀=1.2 ω꜀ for four ω₂₁ values: 1.15 ω꜀, 1.05 ω꜀, ω꜀, and ωₒ=1. Evaluate σ_R over a detuning range ω−ω₂₀ from −0.5 to 0.5 with a sufficient point density to capture all spectral features. Each row is one (detuning, ω₂₁, σ_R) point.

  • /app/outputs/rayleigh_spectrum_fdm.csv: similar CSV for the FDM self-energy, same ω₂₀ and ω₂₁ values and same detuning grid.

The target is to numerically reproduce these artifacts. No explicit gold numbers are provided; the checker will recompute the correct values from the same equations and parameters.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute self-energy and form factors for PBG and FDM
- Role: process
- Action: Implement the isotropic photonic band-gap (PBG) dispersion relation and the frequency-dispersive medium (FDM) dispersion relation, together with the corresponding atomic form factors and self-energy formulas. Numerically compute the real and imaginary parts of the self-energy Σ'(ε) and Σ''(ε) over a dense frequency grid covering the relevant range, using gap ratio r=15%, atomic splitting ω10=Δ/10, and free-space decay rates γ20=γ21=Δ/100. Use ω20=0.95ω_c for bound-state determination and ω20=1.2ω_c for the scattering spectra. Save the resulting arrays for later steps.
- Evidence: `/app/outputs/self_energy_data.npz`

### Step 2: Determine photon-atom bound state in PBG and FDM
- Role: scored (load-bearing)
- Action: Using the real part of the self-energy Σ'(ε) for PBG (with ω20=0.95ω_c) and for FDM obtained in step_1, numerically solve the bound-state condition ω20−ε−Σ'(ε)=0 within the subinterval G' = (ω_v+ω10, ω_c). For each medium, record whether a root exists where Σ''(ε)=0 and, if so, the eigenvalue ε_d; otherwise record that no bound state exists. Save the result to bound_state_result.json.
- Output file: `/app/outputs/bound_state_result.json`
- Format: json
- Contract: JSON object: { "pbg_bound_state_exists": boolean, "pbg_eigenvalue": float or null, "fdm_bound_state_exists": boolean, "fdm_eigenvalue": float or null }
- Scoring: scored by hidden verifier

### Step 3: Compute Rayleigh scattering spectrum for PBG
- Role: scored
- Action: Using the self-energy for the PBG model from step_1 with ω20=1.2ω_c, compute the Rayleigh scattering cross-section σ_R(ω) from the formula that expresses it in terms of the real and imaginary parts of the self‑energy and the atomic form factor. Evaluate σ_R over a range of detunings ω−ω20 from -0.5 to 0.5 (or a suitable window capturing the main features) for each of four Stokes transition frequencies: ω21 = 1.15ω_c, 1.05ω_c, ω_c, and ω_o = 1. Save the spectrum as a CSV.
- Output file: `/app/outputs/rayleigh_spectrum_pbg.csv`
- Format: csv
- Contract: CSV with columns: omega_minus_omega20 (float), omega21 (float), sigma_R (float)
- Scoring: scored by hidden verifier

### Step 4: Compute Rayleigh scattering spectrum for FDM
- Role: scored
- Action: Using the self-energy for the FDM model from step_1 with ω20=1.2ω_c, compute the Rayleigh scattering cross-section σ_R(ω) for the same four ω21 values and the same detuning grid as in step_3. Save the result as a CSV.
- Output file: `/app/outputs/rayleigh_spectrum_fdm.csv`
- Format: csv
- Contract: CSV with columns: omega_minus_omega20 (float), omega21 (float), sigma_R (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bound_state_result.json`
- `/app/outputs/rayleigh_spectrum_pbg.csv`
- `/app/outputs/rayleigh_spectrum_fdm.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bound_state_result.json
- path: `/app/outputs/bound_state_result.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Existence and eigenvalue of the photon‑atom bound state for PBG and FDM. The eigenvalue is a deterministic number; checking uses an exact match within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `pbg_bound_state_exists`: boolean
    - `pbg_eigenvalue`: float or null
    - `fdm_bound_state_exists`: boolean
    - `fdm_eigenvalue`: float or null

### rayleigh_spectrum_pbg.csv
- path: `/app/outputs/rayleigh_spectrum_pbg.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Rayleigh scattering cross‑section for PBG at four ω21 values. The hidden reference spectrum is recomputed from the same formulas; the agent's spectrum must match within a relative error threshold.
- schema:
  - `type`: table
  - `required_columns`: `omega_minus_omega20`, `omega21`, `sigma_R`

### rayleigh_spectrum_fdm.csv
- path: `/app/outputs/rayleigh_spectrum_fdm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Rayleigh scattering cross‑section for FDM at four ω21 values. The hidden reference spectrum is recomputed from the same formulas; the agent's spectrum must match within a relative error threshold.
- schema:
  - `type`: table
  - `required_columns`: `omega_minus_omega20`, `omega21`, `sigma_R`

Notes: The bound-state result is a fixed deterministic quantity (the energy ε_d), checked within a tolerance. The spectra are arrays; the verifier recomputes the reference from the same public parameters and formulas, then compares via relative L2 norm in the relevant detuning window. The PBG spectrum is expected to exhibit doublet/triplet splitting when ω21 is near the band edge, while the FDM spectrum should show a single peak and no splitting.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bound_state_result.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pbg_bound_state_exists": "boolean",
          "pbg_eigenvalue": "float or null",
          "fdm_bound_state_exists": "boolean",
          "fdm_eigenvalue": "float or null"
        }
      },
      "description": "Existence and eigenvalue of the photon‑atom bound state for PBG and FDM. The eigenvalue is a deterministic number; checking uses an exact match within tolerance."
    },
    {
      "file": "rayleigh_spectrum_pbg.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega_minus_omega20",
          "omega21",
          "sigma_R"
        ]
      },
      "description": "Rayleigh scattering cross‑section for PBG at four ω21 values. The hidden reference spectrum is recomputed from the same formulas; the agent's spectrum must match within a relative error threshold."
    },
    {
      "file": "rayleigh_spectrum_fdm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega_minus_omega20",
          "omega21",
          "sigma_R"
        ]
      },
      "description": "Rayleigh scattering cross‑section for FDM at four ω21 values. The hidden reference spectrum is recomputed from the same formulas; the agent's spectrum must match within a relative error threshold."
    }
  ],
  "notes": "The bound-state result is a fixed deterministic quantity (the energy ε_d), checked within a tolerance. The spectra are arrays; the verifier recomputes the reference from the same public parameters and formulas, then compares via relative L2 norm in the relevant detuning window. The PBG spectrum is expected to exhibit doublet/triplet splitting when ω21 is near the band edge, while the FDM spectrum should show a single peak and no splitting."
}
```

## How you are scored
A hidden verifier will independently recompute the bound-state condition and the Rayleigh spectra from the same public formulas and input parameters. It will then compare your submitted files to its own recomputed references:

  • For bound_state_result.json, the verifier checks whether the existence flags and eigenvalues (if any) match its reference within a hidden tolerance. Both PBG and FDM cases are evaluated.
  • For the two CSV files, the verifier computes reference sigma_R arrays on a finer hidden grid and compares your arrays via a relative L2 norm, separately for each ω₂₁ value. A combined spectral score is derived.
  • Additional lightweight structural checks ensure that the spectra vanish inside the photonic band gap and exhibit physically reasonable lineshapes.

The final score is a weighted sum (approximate weights: bound state 0.3, PBG spectrum 0.35, FDM spectrum 0.35). You do not need to match any pre‑known numeric target; implementing the model equations and integration accurately is sufficient to obtain a high score.
