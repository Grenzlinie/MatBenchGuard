# Effective shear modulus and stress concentration factor of random fiber composites via multiparticle effective field method

## Problem background
Predicting how composite materials respond under loads that vary on the scale of the microstructure is essential for reliable design. When the loading is non-uniform, the material's response becomes non-local: the stress at a point depends on the arrangement of surrounding fibers, and classical homogenization is not sufficient. This task addresses a micromechanics-based method that captures these non-local effects and produces quantitative predictions for the effective elastic properties and stress concentration factors in a random short-fiber composite. The concrete system is a two‑dimensional plane‑strain glass‑fiber/epoxy‑matrix composite; the goal is to compute its effective shear modulus at several fiber volume fractions and the stress concentration factor inside the fibers under a smoothly varying uniaxial load.

## Approach
The approach uses the multiparticle effective field method (MEFM). Starting from the exact integral equation for the strain polarization tensor in a random medium, the MEFM introduces an effective field that each inclusion experiences. Under the assumptions of ellipsoidal inclusions, a statistically homogeneous distribution, and a closure hypothesis, the method yields a non-local integral equation for the averaged strain polarization tensor. This equation contains a constant matrix **Y** that encodes the "local" influence of surrounding inclusions on a given one, and a convolution kernel **K** that describes the "non-local" interactions. The effective shear modulus is extracted directly from **Y** via the local effective compliance formula. To handle a non‑uniform applied load, the full non‑local equation is solved by fixed‑point (successive approximation) iteration. Starting from the zero‑order (local) solution, the iteration refines the polarization field. From the converged field one then obtains the stress concentration factor inside the fibers as a function of position.

## Reproduction target
Implement the MEFM for a 2D plane‑strain composite consisting of an epoxy matrix (bulk modulus 4.27 GPa, shear modulus 1.53 GPa) reinforced with identical circular glass fibers (bulk modulus 50.89 GPa, shear modulus 35.04 GPa, radius a = 1). Build the **Y** matrix and convolution kernel **K** using the radial distribution function

g₂(r) = H(r − 2a) × [1 + (4c/π)(π − 2 arcsin(r/(4a)) − (r/(2a))√(1 − r²/(16a²))) H(4a − r)],

where H is the Heaviside step function and c is the fiber volume fraction. Then produce two scored CSV artifacts:
1. **effective_modulus.csv** – the effective shear modulus (GPa) for fiber volume fractions c = 0.15, 0.30, 0.45, 0.60, computed from **Y**.
2. **stress_concentration_f2.csv** – the stress concentration factor ⟨σ₁₁⟩ᵢ(x₁) for the non‑uniform loading ⟨σ₁₁⟩(x₁) = 0.6579 |x₁|^{2.001} exp(−0.2422 x₁²) at c = 0.6, obtained by solving the non‑local integral equation with the iteration method up to the 7th iterate. The factor is normalized by the maximum of its zero‑order approximation. Provide at least 50 grid points covering the x₁ region where the loading is significant, and include a row with x₁ = 'max' that contains the overall maximum value.

## Assets

- Python with numpy, scipy, matplotlib: pypi

## Workflow steps

### Step 1: Build MEFM operators Y and K
- Role: process
- Action: Construct the Y matrix and convolution kernel K(x−y) for the two-phase composite using the multiparticle effective field method (MEFM) formulation with given matrix (epoxy: k=4.27 GPa, μ=1.53 GPa) and fiber (glass: k=50.89 GPa, μ=35.04 GPa) elastic moduli, circular inclusion radius a=1, and the radial distribution function g₂(r) (Eq. (9.2) of the paper). Implement the required T-tensors and Z matrix from the Eshelby solution and binary interaction.
- Evidence: none

### Step 2: Compute effective shear modulus
- Role: scored
- Action: From the Y matrix computed earlier, compute the effective shear modulus via the local MEFM effective compliance formula (Eq. (6.6) of the paper) for fiber volume fractions c=0.15, 0.30, 0.45, 0.60. Report the results in GPa.
- Output file: `/app/outputs/effective_modulus.csv`
- Format: csv
- Contract: concentration, shear_modulus_GPa
- Scoring: scored by hidden verifier

### Step 3: Compute stress concentration factor under f2 loading
- Role: scored (load-bearing)
- Action: Solve the non-local integral equation by the iteration method (fixed-point, successive approximations) with initial guess from zero-order solution using the kernel K built earlier and the non-uniform loading ⟨σ₁₁⟩(x₁)=f₂(x₁) with f₂(x₁)=0.6579|x₁|^{2.001} e^{-0.2422 x₁²}. Apply iterations up to the 7th iterate and obtain the stress concentration factor ⟨σ₁₁⟩ᵢ(x₁) normalized by the maximum of its zero-order approximation. Produce a CSV with at least 50 grid points covering the x₁ domain where the loading is appreciable, and include a row with x₁='max' and the overall maximum value.
- Output file: `/app/outputs/stress_concentration_f2.csv`
- Format: csv
- Contract: x1, stress_concentration_11
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_modulus.csv`
- `/app/outputs/stress_concentration_f2.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_modulus.csv
- path: `/app/outputs/effective_modulus.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective shear modulus computed via MEFM for fiber volume fractions c=0.15, 0.30, 0.45, 0.60.
- schema:
  - `type`: table
  - `required_columns`: `concentration`, `shear_modulus_GPa`
  - `units`:
    - `concentration`: dimensionless
    - `shear_modulus_GPa`: GPa

### stress_concentration_f2.csv
- path: `/app/outputs/stress_concentration_f2.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Stress concentration factor ⟨σ₁₁⟩ᵢ(x₁) for loading f₂(x₁) at c=0.6, computed via MEFM iteration method, with a 'max' row indicating the overall maximum.
- schema:
  - `type`: table
  - `required_columns`: `x1`, `stress_concentration_11`
  - `notes`: The column x1 contains numeric values and one row with the string 'max'.

Notes: The task requires reproducing the effective shear modulus and stress concentration factor using the multiparticle effective field method (MEFM) for a glass-fiber/epoxy composite. All necessary material parameters and loading function are given. The hidden gold values are extracted from the paper's Figure 1 and Table 1.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_modulus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "concentration",
          "shear_modulus_GPa"
        ],
        "units": {
          "concentration": "dimensionless",
          "shear_modulus_GPa": "GPa"
        }
      },
      "description": "Effective shear modulus computed via MEFM for fiber volume fractions c=0.15, 0.30, 0.45, 0.60."
    },
    {
      "file": "stress_concentration_f2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x1",
          "stress_concentration_11"
        ],
        "notes": "The column x1 contains numeric values and one row with the string 'max'."
      },
      "description": "Stress concentration factor ⟨σ₁₁⟩ᵢ(x₁) for loading f₂(x₁) at c=0.6, computed via MEFM iteration method, with a 'max' row indicating the overall maximum."
    }
  ],
  "notes": "The task requires reproducing the effective shear modulus and stress concentration factor using the multiparticle effective field method (MEFM) for a glass-fiber/epoxy composite. All necessary material parameters and loading function are given. The hidden gold values are extracted from the paper's Figure 1 and Table 1."
}
```

## How you are scored
A hidden verifier independently checks each scored artifact. For `effective_modulus.csv` the verifier compares the shear modulus values for each concentration against reference values with an appropriate tolerance. For `stress_concentration_f2.csv` the verifier checks the stress concentration factor at x₁ = 0 and the reported maximum, and also audits the overall shape of the curve to ensure it is physically reasonable. The final reward is a weighted combination of the scores from the two artifacts. Merely reporting numbers without executing the required steps will not produce a correct submission and will not earn credit.
