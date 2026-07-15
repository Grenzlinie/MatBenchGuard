# Numerical Computation of Reflection Coefficient for Periodic Metal-Wire Gratings

## Problem background
Standard measures of electromagnetic reflection coefficient are needed to calibrate free-space measurement apparatus. Conventional artefacts such as plane-parallel metal or dielectric plates suffer from systematic errors or material instabilities. Closely periodic gratings of metal wires of rectangular cross section have been proposed as practical, mechanically fabricable standard measures that offer a wide dynamic range of reflectivity and are amenable to both theoretical calculation and experimental verification. This task focuses on the theoretical prediction: computing the power reflection coefficient of such gratings under normal-incidence H‑polarized plane waves for a family of slot widths and wavelengths that define a candidate set of standard measures.

## Approach
The reflection coefficient is obtained via an analytical‑numerical procedure that exploits the grating periodicity and a long‑wavelength approximation. The procedure consists of two stages:

1. For a given grating geometry (period, wire thickness, slot width) the method first solves a coupled nonlinear system to determine two auxiliary parameters, σ and t, that encode the geometry. The system involves definite integrals that are evaluated numerically, and the solution is found by minimizing a squared‑residual objective.

2. Using σ and t, three effective length coefficients (l, l₁, l₂) are computed, again via integrals that depend on the geometry and on the wavelength via the wave number k = 2π/λ. These coefficients appear in a closed‑form expression for the complex reflection and transmission coefficients of a normally incident H‑polarized plane wave. The power reflection coefficient R is the squared magnitude of the reflection coefficient.

The entire computation is repeated for each combination of the six prescribed slot widths δ and four prescribed wavelengths λ, covering the long‑wavelength regime where the approximation is accurate.

## Reproduction target
Compute the power reflection coefficient R (dimensionless, 0 ≤ R ≤ 1) for six slotted gratings with period p = 8 mm, plate thickness 2h = 2 mm, and slot width δ = 1, 2, 3, 4, 5, 6 mm. The computation must be carried out for normal‑incidence H‑polarized plane waves at the wavelengths λ = 50, 70, 90, 120 mm. Produce a single CSV file containing the computed R for every (δ, λ) combination.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute reflection coefficients
- Role: scored (load-bearing)
- Action: For each slot width δ (1, 2, 3, 4, 5, 6 mm) and wavelength λ (50, 70, 90, 120 mm), solve the nonlinear system of equations for σ and t using the given minimization procedure involving elliptic integrals, compute the auxiliary coefficients l, l1, l2, and apply the reflection coefficient formula for normal-incidence H-polarized plane waves (β=1, α=0) to obtain the power reflection coefficient R. Write the results to reflection_coefficients.csv.
- Output file: `/app/outputs/reflection_coefficients.csv`
- Format: csv
- Contract: delta_mm:int, wavelength_mm:float, R:float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reflection_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reflection_coefficients.csv
- path: `/app/outputs/reflection_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed power reflection coefficient R for normal-incidence H-polarized plane waves on metal-wire gratings of period 8 mm, thickness 2 mm, slot width δ ranging from 1 to 6 mm, at wavelengths 50, 70, 90, 120 mm.
- schema:
  - `type`: table
  - `required_columns`: `delta_mm`, `wavelength_mm`, `R`
  - `units`:
    - `delta_mm`: mm
    - `wavelength_mm`: mm
    - `R`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reflection_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta_mm",
          "wavelength_mm",
          "R"
        ],
        "units": {
          "delta_mm": "mm",
          "wavelength_mm": "mm",
          "R": "dimensionless"
        }
      },
      "description": "Computed power reflection coefficient R for normal-incidence H-polarized plane waves on metal-wire gratings of period 8 mm, thickness 2 mm, slot width δ ranging from 1 to 6 mm, at wavelengths 50, 70, 90, 120 mm."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks the produced CSV. It compares each computed R value against an independently derived reference with an appropriate tolerance, and also verifies that for every slot width δ the reflection coefficient decreases monotonically as the wavelength increases. The final reward is a weighted combination of these checks; simply reporting numbers from the paper is insufficient—the verifier assesses the actual computed output.
