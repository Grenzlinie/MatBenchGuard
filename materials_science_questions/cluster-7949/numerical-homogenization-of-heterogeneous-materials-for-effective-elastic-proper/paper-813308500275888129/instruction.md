# Effective out-of-plane piezoelectric coefficients of 2-1-2 composites by double asymptotic homogenization and FFT numerical homogenization

## Problem background
The effective electroelastic behaviour of hybrid “fibrous-laminate” (2-1-2) piezoelectric composites is investigated. The composite consists of alternating homogeneous piezoelectric layers and heterogeneous layers that contain a square array of unidirectional piezoelectric fibres embedded in an elastic matrix. The out-of-plane effective piezoelectric coefficients (e31 and e33) are key quantities for sensing and actuation applications. Two homogenisation approaches are used to estimate these coefficients for such a composite: a decoupled analytical procedure called double asymptotic homogenisation (DAH) and a full-field numerical method based on fast Fourier transforms (FFT). The task is to compute these coefficients for a specific material system and compare the predictions of the two methods.

## Approach
The workflow compares two homogenisation strategies for the same 2-1-2 composite made of an elastic epoxy matrix and piezoelectric PZT fibres/layers.

1. **DAH (analytical)**: This is a two-step approximate method. First, the heterogeneous fibre-reinforced layer is homogenised using closed-form analytical formulas for 1-3 fibre composites with square fibre packing. Second, the overall 2-1-2 composite is treated as a two-phase laminate composed of the already-homogenised fibrous layer and the homogeneous piezoelectric layer. Overall effective coefficients are obtained from laminate formulas.

2. **FFT (numerical)**: This method solves the full-field electroelastic problem on a periodic unit cell directly. Using electroelastic Green's operators in Fourier space, the method iterates until the strain, stress, electric field, and electric displacement fields satisfy the constitutive laws, equilibrium, and compatibility conditions. No decoupling approximation is made, so the procedure accounts for all interactions between the elastic matrix and the piezoelectric inclusions.

The composite is studied at a fixed fibre volume fraction (λ_f = 0.5) in the heterogeneous layers and at several homogeneous-layer volume fractions λ. Material properties of epoxy and PZT are taken from Pettermann & Suresh (2000) and are listed in the provided resources.

## Reproduction target
For a 2-1-2 epoxy/PZT composite with fibre volume fraction λ_f = 0.5, compute the effective out-of-plane piezoelectric coefficients e31 and e33 at four homogeneous-layer volume fractions: λ = 0, 0.25, 0.5, 0.75.

Use both the DAH closed-form formulas and an FFT-based numerical homogenisation procedure. Report all computed values in a single CSV file with columns:

- λ (float)
- e31_DAH (float, C/m²)
- e33_DAH (float, C/m²)
- e31_FFT (float, C/m²)
- e33_FFT (float, C/m²)

The final CSV is the scored artifact.

## Assets

- Material properties of epoxy and PZT (from Pettermann & Suresh, 2000): 10.1016/S0020-7683(99)00120-1

## Workflow steps

### Step 1: DAH analytical coefficient computation
- Role: process
- Action: Implement the double asymptotic homogenization (DAH) analytical formulas using the provided material properties of epoxy and PZT to compute the effective out-of-plane piezoelectric coefficients e31 and e33 for a 2-1-2 composite with fiber volume fraction λ_f = 0.5 and homogeneous piezoelectric layer volume fractions λ = 0, 0.25, 0.5, 0.75. Store the computed values per λ in an intermediate file.
- Evidence: `/app/outputs/dah_results.json`

### Step 2: FFT numerical homogenization
- Role: process
- Action: Implement a numerical fast Fourier transform (FFT) based homogenization scheme using electroelastic Green's operators and periodic boundary conditions to compute the effective out-of-plane piezoelectric coefficients e31 and e33 for the same 2-1-2 composite and volume fractions, using the provided material properties. Store the results per λ in an intermediate file.
- Evidence: `/app/outputs/fft_results.json`

### Step 3: Assemble and output final CSV
- Role: scored (load-bearing)
- Action: Combine the DAH and FFT results and write a CSV file with columns λ, e31_DAH, e33_DAH, e31_FFT, e33_FFT for λ = 0, 0.25, 0.5, 0.75.
- Output file: `/app/outputs/piezoelectric_coefficients.csv`
- Format: csv
- Contract: λ (float), e31_DAH (float, C/m^2), e33_DAH (float, C/m^2), e31_FFT (float, C/m^2), e33_FFT (float, C/m^2)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/piezoelectric_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### piezoelectric_coefficients.csv
- path: `/app/outputs/piezoelectric_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective out-of-plane piezoelectric coefficients computed by the double asymptotic homogenization (DAH) method and the fast Fourier transform (FFT) numerical method for a 2-1-2 epoxy/PZT composite with fixed fiber volume fraction 0.5 and piezoelectric layer volume fractions 0, 0.25, 0.5, 0.75.
- schema:
  - `type`: table
  - `required_columns`: `λ`, `e31_DAH`, `e33_DAH`, `e31_FFT`, `e33_FFT`
  - `units`:
    - `λ`: none
    - `e31_DAH`: C/m^2
    - `e33_DAH`: C/m^2
    - `e31_FFT`: C/m^2
    - `e33_FFT`: C/m^2

Notes: The checker compares the DAH values to exact analytical results and the FFT values to paper reference values within specified tolerances, and verifies the sign trend e_DAH > e_FFT at each λ.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "piezoelectric_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "λ",
          "e31_DAH",
          "e33_DAH",
          "e31_FFT",
          "e33_FFT"
        ],
        "units": {
          "λ": "none",
          "e31_DAH": "C/m^2",
          "e33_DAH": "C/m^2",
          "e31_FFT": "C/m^2",
          "e33_FFT": "C/m^2"
        }
      },
      "description": "Effective out-of-plane piezoelectric coefficients computed by the double asymptotic homogenization (DAH) method and the fast Fourier transform (FFT) numerical method for a 2-1-2 epoxy/PZT composite with fixed fiber volume fraction 0.5 and piezoelectric layer volume fractions 0, 0.25, 0.5, 0.75."
    }
  ],
  "notes": "The checker compares the DAH values to exact analytical results and the FFT values to paper reference values within specified tolerances, and verifies the sign trend e_DAH > e_FFT at each λ."
}
```

## How you are scored
A hidden verifier independently examines the required output files. For the DAH values, it checks that the reported coefficients closely match the values obtained by directly evaluating the analytical formulas with the same material properties and parameters. For the FFT values, it compares the reported coefficients to expected numerical estimates, allowing a tolerance that accounts for legitimate differences in implementation, discretisation, and convergence criteria. The verifier also inspects whether the predictions of the two methods satisfy certain expected structural relationships (for example, relative magnitudes between the DAH and FFT results at each λ). Each part contributes a reward; the total reward is a weighted sum of these components. The precise tolerances and weights are not disclosed, but full credit is earned when the computed coefficients are both numerically accurate and consistent with the expected structural trends.
