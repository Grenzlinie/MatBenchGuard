# First-Principles Calculation of Electronic and Optical Properties of an Alkali Rare-Earth Phosphate Fluoride NLO Crystal

## Problem background
Na₃Sc₂(PO₄)₂F₃ is an alkali rare‑earth phosphate fluoride that has been proposed as a promising ultraviolet nonlinear optical (NLO) crystal. Its structure is built from [PO₄]³⁻ tetrahedra and [ScO₄F₂] polyhedra, and experiments indicate that this arrangement yields an unusually large birefringence and a short phase‑matching wavelength for second‑harmonic generation. First‑principles DFT calculations were used to explain the origin of these enhanced optical properties. In this task you will reproduce the key DFT‑derived electronic and optical quantities for this crystal: the direct band gap, birefringence at two wavelengths, the independent SHG tensor coefficients, and the dipole moments of the fundamental building units.

## Approach
Use the experimental crystal structure (space group I4mm, obtained from the provided CIF) as the sole input. Perform DFT calculations within the generalized gradient approximation (GGA) using the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and norm‑conserving pseudopotentials, as implemented in an open‑source plane‑wave code (e.g., Quantum ESPRESSO or ABINIT).

First, compute the ground‑state charge density and the electronic band structure; from the band structure determine the direct band gap. Next, compute the complex dielectric function and the resulting refractive‑index dispersion for both ordinary (n_o) and extraordinary (n_e) directions. Because the PBE functional systematically underestimates the band gap, apply a scissor correction to the optical spectra (and to the subsequent SHG calculation) to align the computed band gap with a physically motivated reference. From the corrected refractive indices, extract the birefringence Δn = |n_e − n_o| at the two required wavelengths.

Then evaluate the second‑order nonlinear susceptibility using the velocity‑gauge formalism, also applying the scissor correction, to obtain the independent SHG tensor components d₃₁ and d₃₃ at a fundamental wavelength of 1064 nm.

Finally, using the atomic coordinates from the crystal structure and site charges (e.g., Bader charges or another physically motivated scheme), compute the dipole moment (in Debye) of every [PO₄]³⁻ tetrahedron and every [ScO₄F₂] polyhedron. Sum the z‑components of all [PO₄]³⁻ groups and, separately, all [ScO₄F₂] polyhedra to obtain the net unit‑cell dipole moments along the polar c‑axis.

## Reproduction target
Your goal is to produce four scored JSON files containing the following quantities, all derived from the DFT calculations on the provided crystal structure:

1. **band_gap.json** – the direct band gap (in eV), a boolean indicating whether the gap is direct, and the method label `"GGA-PBE"`.
2. **birefringence.json** – the birefringence Δn at 546.1 nm and at 1064 nm.
3. **shg_coefficients.json** – the independent SHG coefficients d₃₁ and d₃₃ (in pm/V) at a fundamental wavelength of 1064 nm.
4. **dipole_moments.json** – the total z‑component dipole moment (in Debye) of all [PO₄]³⁻ groups and of all [ScO₄F₂] polyhedra in the unit cell.

Each file must follow the schema described in the workflow steps. The exact scheme and required keys are stated in the step contracts. The hidden verifier will compare your submitted values against reference DFT results using predefined tolerances. You must compute these quantities honestly by executing the full computational pipeline; simply reporting the reference numbers without performing the calculations is not sufficient.

## Assets

- Crystal structure of the NLO crystal (CCDC 1973312): https://www.ccdc.cam.ac.uk/structures/search?accession_number=1973312
- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO, ABINIT): https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials for PBE functional: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Prepare DFT input
- Role: process
- Action: Convert the crystal structure (CIF) into input files for a plane-wave DFT code with PBE functional and norm-conserving pseudopotentials. Set up k-point sampling and energy cutoff for SCF and band structure calculations.
- Evidence: `/app/outputs/dft_input.log`

### Step 2: SCF ground-state calculation
- Role: process
- Action: Run a self-consistent field (SCF) calculation to obtain the ground-state electron density and wavefunctions.
- Evidence: `/app/outputs/scf.out`

### Step 3: Band gap extraction
- Role: scored
- Action: Run a non-SCF band structure calculation along high-symmetry k-points. Determine the direct band gap value (eV) and whether the band gap is direct. Write the result to band_gap.json.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: {"band_gap_eV": number, "is_direct": boolean, "method": "GGA-PBE"}
- Scoring: scored by hidden verifier

### Step 4: Optical properties calculation
- Role: process
- Action: Compute the dielectric function (real and imaginary parts) using the ground-state electron density. Apply a scissor correction to account for the DFT band gap underestimation. Obtain the refractive indices n_o and n_e as a function of wavelength.
- Evidence: `/app/outputs/epsilon.dat`

### Step 5: Birefringence reporting
- Role: scored
- Action: From the refractive index dispersion curves, calculate the birefringence Δn = |n_e - n_o| at wavelengths 546.1 nm and 1064 nm. Write the values to birefringence.json.
- Output file: `/app/outputs/birefringence.json`
- Format: json
- Contract: {"birefringence_546nm": number, "birefringence_1064nm": number}
- Scoring: scored by hidden verifier

### Step 6: SHG coefficient calculation
- Role: process
- Action: Compute the second-order nonlinear susceptibility components (specifically the d31 and d33 coefficients) at a fundamental wavelength of 1064 nm using the velocity-gauge formula or equivalent post-processing from the ground-state wavefunctions and energies, with a scissor correction.
- Evidence: `/app/outputs/shg_calc.log`

### Step 7: SHG coefficients reporting
- Role: scored (load-bearing)
- Action: Extract the d31 and d33 values (pm/V) at 1064 nm from the SHG calculation and write shg_coefficients.json.
- Output file: `/app/outputs/shg_coefficients.json`
- Format: json
- Contract: {"d31_pm_per_V": number, "d33_pm_per_V": number}
- Scoring: scored by hidden verifier

### Step 8: Dipole moment calculation
- Role: process
- Action: Using the atomic coordinates from the crystal structure and assigned charges (e.g., Bader or formal charges), compute the dipole moments (in Debye) of the [PO4]3- tetrahedra and [ScO4F2] polyhedra in the unit cell.
- Evidence: `/app/outputs/dipole_raw.dat`

### Step 9: Dipole moments reporting
- Role: scored
- Action: Sum the z-components of the dipole moments of all [PO4]3- groups to obtain the total [PO4] dipole moment along the c-axis, and similarly sum for all [ScO4F2] polyhedra. Write dipole_moments.json.
- Output file: `/app/outputs/dipole_moments.json`
- Format: json
- Contract: {"total_PO4_dipole_z_D": number, "total_ScO4F2_dipole_z_D": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.json`
- `/app/outputs/birefringence.json`
- `/app/outputs/shg_coefficients.json`
- `/app/outputs/dipole_moments.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Direct band gap of the crystal computed with GGA-PBE, compared to a hidden reference value.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: number
    - `is_direct`: boolean
    - `method`: string

### birefringence.json
- path: `/app/outputs/birefringence.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Birefringence at 546.1 nm and 1064 nm, compared to hidden reference values.
- schema:
  - `type`: object
  - `required`:
    - `birefringence_546nm`: number
    - `birefringence_1064nm`: number

### shg_coefficients.json
- path: `/app/outputs/shg_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Independent NLO tensor components d31 and d33 at 1064 nm, compared to hidden reference values.
- schema:
  - `type`: object
  - `required`:
    - `d31_pm_per_V`: number
    - `d33_pm_per_V`: number

### dipole_moments.json
- path: `/app/outputs/dipole_moments.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total unit-cell dipole moments (z-component) of the [PO4]3- groups and [ScO4F2] polyhedra, compared to hidden reference values.
- schema:
  - `type`: object
  - `required`:
    - `total_PO4_dipole_z_D`: number
    - `total_ScO4F2_dipole_z_D`: number

Notes: All scored quantities are derived from first-principles DFT using the same functional (PBE) and pseudopotential type as described. The hidden reference values are the corresponding DFT results reported in the original study; the checker compares within predefined tolerances appropriate for DFT method variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "number",
          "is_direct": "boolean",
          "method": "string"
        }
      },
      "description": "Direct band gap of the crystal computed with GGA-PBE, compared to a hidden reference value."
    },
    {
      "file": "birefringence.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "birefringence_546nm": "number",
          "birefringence_1064nm": "number"
        }
      },
      "description": "Birefringence at 546.1 nm and 1064 nm, compared to hidden reference values."
    },
    {
      "file": "shg_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "d31_pm_per_V": "number",
          "d33_pm_per_V": "number"
        }
      },
      "description": "Independent NLO tensor components d31 and d33 at 1064 nm, compared to hidden reference values."
    },
    {
      "file": "dipole_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "total_PO4_dipole_z_D": "number",
          "total_ScO4F2_dipole_z_D": "number"
        }
      },
      "description": "Total unit-cell dipole moments (z-component) of the [PO4]3- groups and [ScO4F2] polyhedra, compared to hidden reference values."
    }
  ],
  "notes": "All scored quantities are derived from first-principles DFT using the same functional (PBE) and pseudopotential type as described. The hidden reference values are the corresponding DFT results reported in the original study; the checker compares within predefined tolerances appropriate for DFT method variations."
}
```

## How you are scored
A hidden verifier independently evaluates each of the four scored output files. For every numeric field, the verifier computes the absolute error between your submitted value and a hidden reference value, then assigns a score per field using an absolute tolerance: full credit (1.0) is given when the error is within the tolerance, and the score decreases linearly to 0 as the error grows to twice the tolerance. The overall reward is a weighted average of the scores from the four artifacts, with the weights reflecting their relative importance. Artifacts that are missing, malformed, or contain invalid values receive a score of 0 for that item. The exact tolerances and weights are not revealed, so you must aim for physically accurate DFT results that are internally consistent and close to the methodology‑expected values.
