# Acoustic and optic temperature parameters of tetragonal BaTiO3

## Problem background
Tetragonal barium titanate (BaTiO₃) is a ferroelectric material whose structural and dynamical properties are often studied via diffraction experiments. The anisotropic mean-square atomic displacements, expressed as temperature parameters B (or Debye‑Waller factors), influence measured intensities and are needed for accurate structure determination. These parameters arise from both acoustic and optic phonon contributions and are expected to differ under two piezoelectric clamping conditions: constant electric field (clamped) and constant polarization (unclamped). This work computes the anisotropic average temperature parameters B₁₁ and B₃₃ from elastic constants and an approximate low‑frequency TO phonon dispersion, providing the theoretical predictions for both clamping regimes at room temperature.

## Approach
The acoustic contribution is computed from the elastic continuum model using the K‑surface method. For each of seven propagation directions, a 3×3 matrix A is constructed from the tetragonal elastic constants (provided for both constant-E and constant-P conditions) and the direction cosines. The inverse matrix yields K_x = (A⁻¹)_11 and K_z = (A⁻¹)_33. A directionally averaged K is obtained by simple averaging. The acoustic temperature parameters are then calculated as Bᵃᶜ = 4 k_B T q_m ⟨K⟩, where the Debye cutoff wavevector q_m is derived from the room-temperature lattice constants (a = 3.992 Å, c = 4.036 Å) and T = 293 K. The optic contribution is obtained from an approximate low‑frequency transverse optic (TO) phonon branch. The TO dispersion is parameterised using three known frequencies at q=0, 0.31 Å⁻¹, and 0.36 Å⁻¹, and the diffuse intensity is assumed to form a sheet of width Δ = a*/11 (a* = 2π/a). The contribution B₁₁ᵒᵖ is computed by numerical integration over the q_x–q_y plane within the Brillouin-zone boundary, while B₃₃ᵒᵖ = 0. Both acoustic and optic parts are added to give the total average temperature parameters B₁₁ = B₁₁ᵃᶜ + B₁₁ᵒᵖ and B₃₃ = B₃₃ᵃᶜ for the two clamping conditions.

## Reproduction target
Compute and output the four total average temperature parameters B₁₁ and B₃₃ (in Å²) for T = 293 K under constant electric field (clamped, E) and constant polarization (unclamped, P) conditions. In addition, produce the separate acoustic contributions (B₁₁ᵃᶜ, B₃₃ᵃᶜ) for both conditions and the optic contribution (B₁₁ᵒᵖ). The final totals must be the sum of the appropriate acoustic and optic parts. The computed values should be physically reasonable and consistent with known theoretical estimates.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Compute K_x and K_z for selected directions
- Role: process
- Action: Construct the 3×3 matrix A for each propagation direction ([100], [010], [001], [110], [011], [101], [111]) using the tetragonal elastic constants (constant E and constant P) and direction cosines, following the explicit expressions for A_{pq} given in the paper's appendix. Invert A to obtain (A^{-1})_{11} and (A^{-1})_{33} as K_x and K_z. Save the full set of per‑direction values for later averaging.
- Evidence: `/app/outputs/table_I_K_values.json`

### Step 2: Average K_x and K_z over directions
- Role: process
- Action: Compute the directionally averaged K_x and K_z by simple equal‑weight averaging of the per‑direction values obtained in step 1. Save the averages for use in the acoustic B calculation.
- Evidence: `/app/outputs/average_K.json`

### Step 3: Compute acoustic temperature parameters
- Role: scored
- Action: Calculate the acoustic contributions B11_ac and B33_ac for both clamping conditions (constant E and constant P) at T=293 K. Use the formula B_ac = 4 k_B T q_m ⟨K⟩ with the Boltzmann constant k_B, the Debye cutoff wavevector q_m = (6π² / V_cell)^{1/3} where V_cell = a² c (a = 3.992 Å, c = 4.036 Å), and the averaged K_x/K_z from step 2. Report the four values in Å².
- Output file: `/app/outputs/acoustic_contributions.json`
- Format: json
- Contract: {"B11_ac_E": number, "B33_ac_E": number, "B11_ac_P": number, "B33_ac_P": number}
- Scoring: scored by hidden verifier

### Step 4: Compute optic temperature parameter
- Role: scored
- Action: Construct an approximate low‑frequency TO phonon dispersion using the three known frequencies: ν = 0.18×10¹² Hz at q=0, ν = 0.71×10¹² Hz at q=0.31 Å⁻¹, ν = 1.1×10¹² Hz at q=0.36 Å⁻¹. Assume the optic sheet has a width Δ = a*/11, where a* = 2π/a (a = 3.992 Å). Perform a numerical integration over the q_x‑q_y plane up to the Brillouin‑zone boundary to obtain the average optic contribution B11_op; B33_op = 0. Report the result in Å².
- Output file: `/app/outputs/optic_contribution.json`
- Format: json
- Contract: {"B11_op": number}
- Scoring: scored by hidden verifier

### Step 5: Compute total temperature parameters
- Role: scored (load-bearing)
- Action: Combine acoustic and optic contributions: B11_total = B11_ac + B11_op, B33_total = B33_ac (since B33_op = 0) for both clamping conditions. Report the four final values in Å².
- Output file: `/app/outputs/final_results.json`
- Format: json
- Contract: {"B11_E": number, "B33_E": number, "B11_P": number, "B33_P": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/acoustic_contributions.json`
- `/app/outputs/optic_contribution.json`
- `/app/outputs/final_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### acoustic_contributions.json
- path: `/app/outputs/acoustic_contributions.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Acoustic temperature parameters B11 and B33 for constant E and constant P.
- schema:
  - `type`: object
  - `required`:
    - `B11_ac_E`: number (Å²)
    - `B33_ac_E`: number (Å²)
    - `B11_ac_P`: number (Å²)
    - `B33_ac_P`: number (Å²)

### optic_contribution.json
- path: `/app/outputs/optic_contribution.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Optic temperature parameter B11 (B33_op = 0).
- schema:
  - `type`: object
  - `required`:
    - `B11_op`: number (Å²)

### final_results.json
- path: `/app/outputs/final_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Total average temperature parameters. The checker verifies that final B11 = acoustic B11 + optic B11 and final B33 = acoustic B33, then compares the four totals to hidden paper‑reported gold within an absolute tolerance.
- schema:
  - `type`: object
  - `required`:
    - `B11_E`: number (Å²)
    - `B33_E`: number (Å²)
    - `B11_P`: number (Å²)
    - `B33_P`: number (Å²)

Notes: The checker first validates self‑consistency (final = acoustic + optic) and then scores the final totals. Only the final totals carry explicit score weight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "acoustic_contributions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "B11_ac_E": "number (Å²)",
          "B33_ac_E": "number (Å²)",
          "B11_ac_P": "number (Å²)",
          "B33_ac_P": "number (Å²)"
        }
      },
      "description": "Acoustic temperature parameters B11 and B33 for constant E and constant P."
    },
    {
      "file": "optic_contribution.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "B11_op": "number (Å²)"
        }
      },
      "description": "Optic temperature parameter B11 (B33_op = 0)."
    },
    {
      "file": "final_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "B11_E": "number (Å²)",
          "B33_E": "number (Å²)",
          "B11_P": "number (Å²)",
          "B33_P": "number (Å²)"
        }
      },
      "description": "Total average temperature parameters. The checker verifies that final B11 = acoustic B11 + optic B11 and final B33 = acoustic B33, then compares the four totals to hidden paper‑reported gold within an absolute tolerance."
    }
  ],
  "notes": "The checker first validates self‑consistency (final = acoustic + optic) and then scores the final totals. Only the final totals carry explicit score weight."
}
```

## How you are scored
A hidden verifier will read your JSON output files. It will first check that your final results are self-consistent with the intermediate acoustic and optic contributions (final B₁₁ = acoustic B₁₁ + optic B₁₁, final B₃₃ = acoustic B₃₃). It will then compare each of the four total values (B₁₁_E, B₃₃_E, B₁₁_P, B₃₃_P) to a reference set of expected values using an absolute tolerance. Your score is the fraction of the four total values that fall within the allowed range, so a perfect implementation yields the maximum score. Simply copying numbers from any source will not pass because the verifier checks that the submitted totals are consistent with the intermediate contributions that you computed yourself.
