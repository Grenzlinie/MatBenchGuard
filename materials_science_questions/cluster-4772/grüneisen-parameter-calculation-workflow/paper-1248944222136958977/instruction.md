# Computing Quadratic GUP Correction Parameter from Debye Model and Seismic Data

## Problem background
Quantum gravity models often predict deformations of the phase‑space measure that alter the density of states and, consequently, the thermodynamic potentials of crystalline solids. When a quadratic generalized uncertainty principle (GUP) is applied to a Debye crystal, a momentum‑dependent correction parameter α modifies the vibrational Helmholtz free energy and the isothermal bulk modulus. By matching the theoretically modified bulk modulus to an experimentally determined reference value for a well‑characterized material (aluminum), one can constrain α and thereby test gravity‑induced deviations from standard statistical mechanics. This task computes α from the modified bulk modulus expression using published seismic velocity and density data, together with known solid‑state parameters.

## Approach
The core idea is to re‑implement the modified isothermal bulk modulus expression that arises from the anharmonic Debye model with a quadratic phase‑space correction. The correction term depends linearly on α, the temperature T, the Debye temperature θD, the Grüneisen parameter γ, its volume derivative q, and the zero‑temperature bulk modulus K0. The theoretical expression involves the Debye function and polylogarithms, and can be written so that α appears linearly. We use experimental P‑ and S‑wave velocities together with the density for aluminum to compute the mean sound velocity and the Debye temperature via standard solid‑state formulas. The required γ and q are taken from published compilations of material properties. For two target temperatures (300 K and 10 K), the theoretical bulk modulus is set equal to the reference K0 and the resulting linear relation is solved for α. The workflow therefore consists of: collecting the experimental inputs and physical constants, computing the Debye temperature, obtaining γ and q from the literature, and finally solving the bulk‑modulus equation to produce the α values.

## Reproduction target
Compute the quadratic GUP parameter α (in s²) for aluminum at T = 300 K and T = 10 K by implementing the modified isothermal bulk modulus expression, using the Debye temperature derived from the P‑ and S‑wave velocities and density reported by Matsushima et al. (2024), the zero‑temperature bulk modulus K0 = 81.3 GPa from Gaudoin & Foulkes (2002), and standard literature values for the Grüneisen parameter γ and its volume derivative q. The result must be written to a CSV file named alpha_results.csv with columns `temperature_K` and `alpha_s2`, containing one row for each temperature.

## Assets

- Matsushima et al. (2024) P- and S-wave velocities and density for aluminum: 10.1093/gji/ggae260
- Gaudoin & Foulkes (2002) zero-temperature bulk modulus K0 for aluminum: 10.1103/PhysRevB.66.052104
- Grüneisen parameter γ and anharmonic parameter q for aluminum
- scipy: scipy
- numpy: numpy

## Workflow steps

### Step 1: Gather experimental inputs and physical constants
- Role: process
- Action: Collect the P-wave velocity (vP), S-wave velocity (vS), and density (ρ) for aluminum from Matsushima et al. (2024), the reference zero-temperature bulk modulus K0 = 81.3 GPa from Gaudoin & Foulkes (2002), and fundamental constants (gas constant R, Boltzmann constant kB, Planck constant h, Avogadro number NA, molar mass of Al).
- Evidence: none

### Step 2: Compute mean sound velocity and Debye temperature
- Role: process
- Action: Compute mean sound velocity vm from vP and vS using the formula vm = vS * (3/(2+(vS/vP)^3))^(1/3). Then compute the Debye temperature θD using θD = (h*vm/kB)*(6π² n)^(1/3) where n = (NA*ρ)/M, and propagate the density uncertainty to obtain θD uncertainty.
- Evidence: none

### Step 3: Obtain Grüneisen parameter γ and anharmonic parameter q for aluminum
- Role: process
- Action: Look up the Grüneisen parameter γ and its volume derivative q for aluminum from solid-state literature (e.g., Anderson, 1995 or other reputable sources). Use typical values γ ≈ 2.14 and q ≈ 1.1; justify the chosen values.
- Evidence: none

### Step 4: Solve for quadratic GUP parameter α at T=300 K and T=10 K
- Role: scored (load-bearing)
- Action: Implement the theoretical isothermal bulk modulus expression for a Debye crystal with quadratic GUP correction (the modified bulk modulus K(α,T) that involves the Debye function, polylogarithms, and the parameters θD, γ, q, K0, p=3, R). For each temperature T=300 K and T=10 K, set the theoretical K equal to the reference K0 and algebraically invert the linear relation in α to compute α. Write a CSV file with columns temperature_K and alpha_s2 containing the two solved α values in s^2.
- Output file: `/app/outputs/alpha_results.csv`
- Format: csv
- Contract: temperature_K (float, K), alpha_s2 (float, s^2, in scientific notation)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/alpha_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### alpha_results.csv
- path: `/app/outputs/alpha_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed quadratic GUP parameter α for aluminum at T=300 K and T=10 K, derived from the modified isothermal bulk modulus expression.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `alpha_s2`
  - `units`:
    - `temperature_K`: K
    - `alpha_s2`: s^2

Notes: The conversion to the fundamental GUP parameter β0 is not required for the scored target.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "alpha_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "alpha_s2"
        ],
        "units": {
          "temperature_K": "K",
          "alpha_s2": "s^2"
        }
      },
      "description": "Computed quadratic GUP parameter α for aluminum at T=300 K and T=10 K, derived from the modified isothermal bulk modulus expression."
    }
  ],
  "notes": "The conversion to the fundamental GUP parameter β0 is not required for the scored target."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the alpha_results.csv file. The verifier compares the two computed α values against a hidden reference that represents the paper‑reported results. Scoring uses a threshold‑or‑better policy: full credit is awarded if each α lies within the uncertainty interval associated with the reference measurement; otherwise partial credit is given based on the relative deviation from the central value. It is not enough to simply write down an expected number—the verifier checks that your implementation yields values consistent with the model, so your code must genuinely perform the computation described in the workflow steps.
