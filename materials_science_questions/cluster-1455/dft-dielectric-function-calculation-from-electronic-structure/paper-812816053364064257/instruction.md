# DFT dielectric function and optical properties of rutile TiO₂

## Problem background
Rutile titanium dioxide (TiO₂) is a wide-bandgap semiconductor whose high refractive index and optical anisotropy make it a candidate for anti-reflective coatings in photovoltaic devices. A quantitative understanding of its electronic band structure (particularly the direct band gap) and its optical properties — the frequency-dependent dielectric function, high-frequency dielectric constants, and refractive indices for ordinary and extraordinary polarizations — is needed to assess its performance. These quantities can be computed from first-principles density functional theory (DFT). This task requires executing such DFT calculations to determine the electronic and optical properties of rutile TiO₂ without relying on empirical input.

## Approach
The investigation uses plane-wave density functional theory as implemented in Quantum ESPRESSO. The calculations are carried out with norm-conserving pseudopotentials and two exchange-correlation functionals: the Perdew–Burke–Ernzerhof generalized gradient approximation (PBE-GGA) and the Perdew–Wang local density approximation (PW-LDA). The workflow consists of: (1) structural optimization (vc-relax) of the rutile primitive cell to obtain relaxed lattice parameters and atomic positions for each functional; (2) self-consistent field (SCF) and non-SCF band-structure calculations along a high-symmetry k-path to identify the direct band gap at the Γ point; (3) computation of the complex dielectric function ε(ω) for ordinary and extraordinary polarizations from the Kohn-Sham eigenvalues and transition matrix elements via the interband transition formalism (Drude-Lorentz and Kramers-Kronig relations); (4) extraction of the high-frequency (electronic) dielectric constants ε₁₁(∞)=ε₂₂(∞) and ε₃₃(∞) from the real part of ε(ω) at high photon energy; and (5) calculation of ordinary and extraordinary refractive indices from the dielectric function via the Maxwell relation, evaluated at 633 nm (1.96 eV), yielding the optical birefringence Δn = n_e − n_o. The same workflow is repeated independently for both functionals, allowing a comparison of their influence on the predicted optical constants.

## Reproduction target
The objective is to execute the complete DFT pipeline described above and produce three scored output files:  
- `band_gap_results.json`: contains the direct Γ–Γ band gap (in eV) for both PW-LDA and PBE-GGA functionals.  
- `dielectric_constants.json`: contains the high-frequency dielectric constants ε₁₁(∞) and ε₃₃(∞) for both PW-LDA and PBE-GGA.  
- `refractive_indices.json`: contains the ordinary and extraordinary refractive indices at 633 nm and the resulting optical birefringence for both PW-LDA and PBE-GGA.  
All values must be derived from a self-consistent workflow that includes geometry optimization, band structure, and optical post-processing, starting from the standard rutile crystal structure and public pseudopotentials.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials for Ti and O: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Geometry optimization of rutile TiO₂
- Role: process
- Action: Perform structural optimization (vc-relax) of rutile TiO₂ using DFT as implemented in Quantum ESPRESSO. Employ norm-conserving pseudopotentials and run separate optimizations with the PBE-GGA and PW-LDA exchange-correlation functionals. The optimized lattice parameters and atomic positions obtained for each functional are the inputs to all subsequent electronic and optical calculations.
- Evidence: none

### Step 2: Band structure calculation and direct band gap extraction
- Role: scored
- Action: Using the relaxed structures from step s01, perform a self-consistent field (SCF) calculation followed by a non-SCF band-structure calculation along a high-symmetry k-path for both LDA and GGA. Extract the direct band gap at the Γ point (energy difference between the highest occupied valence band and the lowest unoccupied conduction band) for each functional. Write the results to a JSON file.
- Output file: `/app/outputs/band_gap_results.json`
- Format: json
- Contract: {"LDA_direct_gap_eV": <float>, "GGA_direct_gap_eV": <float>}
- Scoring: scored by hidden verifier

### Step 3: Complex dielectric function and high-frequency dielectric constants
- Role: scored (load-bearing)
- Action: From the Kohn-Sham eigenvalues and transition matrix elements obtained in the SCF/band-structure runs, compute the frequency-dependent complex dielectric function ε(ω) for ordinary (indices 1,2) and extraordinary (index 3) polarization. Use the Drude-Lorentz (imaginary part) and Kramers-Kronig (real part) relations to obtain ε₁(ω) and ε₂(ω). From the real part at high photon energy, extract the high-frequency (electronic) dielectric constants ε₁₁(∞)=ε₂₂(∞) and ε₃₃(∞) for both LDA and GGA. Save the results in a JSON file.
- Output file: `/app/outputs/dielectric_constants.json`
- Format: json
- Contract: {"LDA_eps_11_infty": <float>, "LDA_eps_33_infty": <float>, "GGA_eps_11_infty": <float>, "GGA_eps_33_infty": <float>}
- Scoring: scored by hidden verifier

### Step 4: Refractive indices and birefringence at 633 nm
- Role: scored
- Action: Using the real and imaginary parts of the dielectric function computed in step s03, calculate the ordinary and extraordinary refractive indices n(ω) via the Maxwell model relation. Evaluate the refractive indices at a photon energy corresponding to 633 nm (1.96 eV). Compute the optical birefringence Δn = n_e − n_o for both LDA and GGA. Write the results to a JSON file.
- Output file: `/app/outputs/refractive_indices.json`
- Format: json
- Contract: {"LDA_ordinary_n_at633nm": <float>, "LDA_extraordinary_n_at633nm": <float>, "GGA_ordinary_n_at633nm": <float>, "GGA_extraordinary_n_at633nm": <float>, "LDA_birefringence_at633nm": <float>, "GGA_birefringence_at633nm": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_results.json`
- `/app/outputs/dielectric_constants.json`
- `/app/outputs/refractive_indices.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_results.json
- path: `/app/outputs/band_gap_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Direct Γ-Γ band gap (eV) from LDA and GGA band‑structure calculations.
- schema:
  - `type`: object
  - `required`:
    - `LDA_direct_gap_eV`: number
    - `GGA_direct_gap_eV`: number

### dielectric_constants.json
- path: `/app/outputs/dielectric_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: High-frequency (electronic) dielectric constants ε_∞ for ordinary (11/22) and extraordinary (33) directions, extracted from the real part of the dielectric function.
- schema:
  - `type`: object
  - `required`:
    - `LDA_eps_11_infty`: number
    - `LDA_eps_33_infty`: number
    - `GGA_eps_11_infty`: number
    - `GGA_eps_33_infty`: number

### refractive_indices.json
- path: `/app/outputs/refractive_indices.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Ordinary and extraordinary refractive indices and optical birefringence at 633 nm.
- schema:
  - `type`: object
  - `required`:
    - `LDA_ordinary_n_at633nm`: number
    - `LDA_extraordinary_n_at633nm`: number
    - `GGA_ordinary_n_at633nm`: number
    - `GGA_extraordinary_n_at633nm`: number
    - `LDA_birefringence_at633nm`: number
    - `GGA_birefringence_at633nm`: number

Notes: All scored values are compared against hidden reference numbers from the paper with tolerances that account for legitimate toolchain spread. The agent must perform the full DFT pipeline; a lazy guess does not meet the tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "LDA_direct_gap_eV": "number",
          "GGA_direct_gap_eV": "number"
        }
      },
      "description": "Direct Γ-Γ band gap (eV) from LDA and GGA band‑structure calculations."
    },
    {
      "file": "dielectric_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "LDA_eps_11_infty": "number",
          "LDA_eps_33_infty": "number",
          "GGA_eps_11_infty": "number",
          "GGA_eps_33_infty": "number"
        }
      },
      "description": "High-frequency (electronic) dielectric constants ε_∞ for ordinary (11/22) and extraordinary (33) directions, extracted from the real part of the dielectric function."
    },
    {
      "file": "refractive_indices.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "LDA_ordinary_n_at633nm": "number",
          "LDA_extraordinary_n_at633nm": "number",
          "GGA_ordinary_n_at633nm": "number",
          "GGA_extraordinary_n_at633nm": "number",
          "LDA_birefringence_at633nm": "number",
          "GGA_birefringence_at633nm": "number"
        }
      },
      "description": "Ordinary and extraordinary refractive indices and optical birefringence at 633 nm."
    }
  ],
  "notes": "All scored values are compared against hidden reference numbers from the paper with tolerances that account for legitimate toolchain spread. The agent must perform the full DFT pipeline; a lazy guess does not meet the tolerances."
}
```

## How you are scored
A hidden verifier independently inspects each of the three output files and compares the reported numbers against a reference. Each file contributes a weighted fraction to the overall reward (band_gap_results.json, dielectric_constants.json, and refractive_indices.json). It is not enough to supply plausible or approximately correct numbers; the values must be the genuine outcome of the specified DFT pipeline, and the verifier uses tolerances that distinguish properly converged computations from shortcuts or guesses. Failing to run the actual calculations will result in a low score, even if the submitted numbers superficially resemble typical values for rutile TiO₂.
