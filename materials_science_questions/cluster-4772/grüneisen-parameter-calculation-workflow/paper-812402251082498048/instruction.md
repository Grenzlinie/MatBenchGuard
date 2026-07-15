# Grüneisen Parameter Calculation for Fused Silica

## Problem background
In dielectric solids, the anharmonic interaction between an ultrasonic wave and the thermal phonon bath (the Akhiezer mechanism) leads to sound absorption. The coupling strength is characterized by effective ultrasonic Grüneisen parameters Γ_j^2, which are averages of mode-specific Grüneisen parameters γ_{ij} derived from second- and third-order elastic constants. Computing Γ_j^2 from the known elastic constants of a material is the first step toward assessing whether the Akhiezer mechanism can account for observed acoustic attenuation. This task computes the effective Grüneisen parameters for fused silica, a prototypical glass, using two common averaging schemes: Mason’s principal‑axis approximation and a numerical angular average over the phonon wavevector hemisphere.

## Approach
The mode Grüneisen parameter γ_{ij}(θ,φ) for a phonon mode i and sound‑wave polarization j in a cubic crystal is expressed in terms of the second‑order elastic constants C_11, C_44 and the third‑order constants C_111, C_144, C_456. At high temperatures all phonon modes contribute equally to the specific heat, so the effective squared Grüneisen parameter Γ_j^2 is obtained from the spherical averages of γ and γ^2, with an additional term for longitudinal waves that involves the projection of the phonon velocity. Two approximations are evaluated: (i) Mason’s scheme, which replaces the isotropic solid by a cubic crystal and evaluates the formulae for sound propagation along a high‑symmetry (100) axis, thereby using only the few high‑symmetry phonon directions; (ii) a numerical q‑space integration that samples propagation directions uniformly over the forward hemisphere, computing γ for the three acoustic branches (one longitudinal, two degenerate transverse) and performing the angular average to account for the full elastic anisotropy. Both methods yield Γ_L^2 and Γ_T^2. No experimental data are needed; the required elastic constants are supplied directly in the workflow steps.

## Reproduction target
Produce two CSV files containing the effective ultrasonic Grüneisen parameters Γ_L^2 and Γ_T^2 for fused silica, computed by the two averaging schemes. The first file (step_01_mason.csv) reports the values from Mason’s principal‑axis approximation; the second (step_02_numerical.csv) reports the values from numerical q‑space averaging. Each file must contain two rows, with columns 'polarization' (string 'L' or 'T') and 'gamma_squared' (float). The output parameters quantify the anharmonic coupling strength for longitudinal and transverse sound waves in the elastic‑continuum model of fused silica.

## Assets
The required second‑ and third‑order elastic constants of fused silica are given directly in the workflow step descriptions (C11 = 7.85×10¹¹, C44 = 3.12×10¹¹, C111 = 64.8×10¹¹, C144 = 5.4×10¹¹, C456 = −1.32×10¹¹ dyn cm⁻²). No external datasets, models, or tools beyond standard scientific computing libraries (e.g., NumPy) are required.

## Workflow steps

### Step 1: Compute Grüneisen parameters via Mason's scheme
- Role: scored
- Action: Using Mason's principal-axis approximation for an isotropic solid, compute the effective ultrasonic Grüneisen parameters Γ_L^2 and Γ_T^2 for fused silica. For propagation along a cubic (100) axis, evaluate the mode-dependent Grüneisen parameters for the longitudinal and transverse branches using the standard formulas that express γ in terms of second-order elastic constants (SOEC: C11, C44) and third-order elastic constants (TOEC: C111, C144, C456) for cubic crystals. Then perform specific-heat-weighted averages assuming equal weight for all modes at high temperature. Output a CSV with the polarization and the squared effective Grüneisen parameter.
- Output file: `/app/outputs/step_01_mason.csv`
- Format: csv
- Contract: Two rows, columns: polarization (str), gamma_squared (float).
- Scoring: scored by hidden verifier

### Step 2: Compute Grüneisen parameters by numerical q-space averaging
- Role: scored (load-bearing)
- Action: Perform a numerical angular average over the forward hemisphere of the mode-dependent Grüneisen parameters to obtain Γ_L^2 and Γ_T^2. For each sampled propagation direction (θ, φ), compute the mode-dependent parameters for the one longitudinal and two degenerate transverse phonon branches using the same cubic-crystal formulas as in Mason's scheme, but evaluated for arbitrary directions. Use a uniform angular weighting (equal weight for all directions) to compute the specific-heat-weighted averages of γ and γ^2. Output a CSV with the polarization and the squared effective Grüneisen parameter.
- Output file: `/app/outputs/step_02_numerical.csv`
- Format: csv
- Contract: Two rows, columns: polarization (str), gamma_squared (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_mason.csv`
- `/app/outputs/step_02_numerical.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_mason.csv
- path: `/app/outputs/step_01_mason.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective ultrasonic Grüneisen parameters computed via Mason's scheme.
- schema:
  - `type`: table
  - `required_columns`: `polarization`, `gamma_squared`
  - `units`:
    - `gamma_squared`: dimensionless

### step_02_numerical.csv
- path: `/app/outputs/step_02_numerical.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective ultrasonic Grüneisen parameters computed via numerical q-space averaging.
- schema:
  - `type`: table
  - `required_columns`: `polarization`, `gamma_squared`
  - `units`:
    - `gamma_squared`: dimensionless

Notes: The Grüneisen parameters are computed from provided SOEC and TOEC. The checker compares the agent's reported gamma_squared values for both polarizations and both schemes to hidden paper reference values, accepting results within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_mason.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "polarization",
          "gamma_squared"
        ],
        "units": {
          "gamma_squared": "dimensionless"
        }
      },
      "description": "Effective ultrasonic Grüneisen parameters computed via Mason's scheme."
    },
    {
      "file": "step_02_numerical.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "polarization",
          "gamma_squared"
        ],
        "units": {
          "gamma_squared": "dimensionless"
        }
      },
      "description": "Effective ultrasonic Grüneisen parameters computed via numerical q-space averaging."
    }
  ],
  "notes": "The Grüneisen parameters are computed from provided SOEC and TOEC. The checker compares the agent's reported gamma_squared values for both polarizations and both schemes to hidden paper reference values, accepting results within a tolerance."
}
```

## How you are scored
A hidden verifier reads your two CSV files and extracts the gamma_squared values for longitudinal and transverse polarizations. For each of the four values (Mason L, Mason T, integration L, integration T), the verifier compares it to a reference value using a relative tolerance that accounts for minor numerical differences from independent implementations. You receive credit for each value that falls within the tolerance band. The final reward is the fraction of the four values that meet the tolerance, scaled to the interval [0, 1] (four values within tolerance → 1.0, three → 0.75, two → 0.5, one → 0.25). Submitting arbitrary numbers without performing the physical calculation is unlikely to satisfy the tolerance.
