# Energetic Model of Dislocation Loop Nucleation by Shear Stress

## Problem background
In field-ion microscopy, high evaporation fields subject specimens to shear stresses approaching the theoretical shear strength. Such stresses could homogeneously nucleate dislocation loops. This task implements an energetic model that calculates the activation energy (energy barrier) for the homogeneous nucleation of dislocation loops under a uniform applied shear stress, comparing perfect loops and faulted (Shockley) loops. The model is applied to iridium using specified material constants. The key outcome is a set of activation energy values as a function of normalized shear stress and stacking-fault energy ratio, from which one can determine the critical stress where faulted loops become the thermodynamically favored configuration.

## Approach
The total energy change of forming a circular dislocation loop of radius R under a uniform shear stress σ includes the dislocation line energy (∝ G b² ln(R/b0)), a stacking-fault energy term (π R² γ) when the loop encloses a fault, and the work done by the stress (−π R² σ b). The critical radius R_c is obtained from the condition that the energy is stationary, yielding an implicit transcendental equation for R_c. The activation energy U_c is the energy barrier evaluated at R_c. For perfect loops the stacking-fault term is zero; for faulted (Shockley) partial loops the stacking-fault energy is parameterized through the ratio f = γ/(G b_p). The computation loops over a grid of normalized shear stresses σ/G and several f values, using numerical root-finding to solve the implicit equation for R_c and then computing U_c. From the resulting table, the threshold stress at which faulted loops become energetically favoured is extracted by comparing activation energies between perfect and faulted loops at the same stress.

## Reproduction target
Compute the critical radius and activation energy for homogeneous nucleation of dislocation loops under uniform shear stress in iridium, as described above. For normalized shear stresses σ/G from 0.05 to 0.15 in steps of 0.01, and for stacking-fault energy ratios f = 0.0 (perfect loops), 0.01, 0.02, 0.03 (faulted loops), produce a CSV file (“/app/outputs/results.csv”) with columns: `loop_type`, `f`, `sigma_over_G`, `R_c_angstrom`, `U_c_eV`, `U_c_normalized`. Then, using this table, find the smallest σ/G at which the activation energy of the faulted loop with f = 0.01 is strictly less than that of the perfect loop, and write that threshold as a single line to “/app/outputs/critical_stress.txt” in the format `sigma_over_G = X.XXX` (three decimal digits).

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Define model and material parameters
- Role: process
- Action: Set up the analytical expressions for loop energy, work, barrier, critical radius, and activation energy. Derive iridium material constants: shear modulus G = 21.3e11 dyn/cm²; total Burgers vector b_t from G b_t³ = 25 eV; partial Burgers vector b_p = b_t / √3; core parameter b0 = b/2. Record the derived parameters in a log file.
- Evidence: `/app/outputs/params_log.txt`

### Step 2: Compute activation energies for loop nucleation
- Role: scored (load-bearing)
- Action: For each combination of loop type (perfect or faulted), stacking-fault energy ratio f (0.0, 0.01, 0.02, 0.03) and normalized shear stress sigma/G from 0.05 to 0.15 (step 0.01), solve the implicit equation for critical radius R_c. For perfect loops, gamma=0 and b=b_t; for faulted loops, gamma = f * G * b_p and b=b_p. Compute activation energy U_c and its normalized value. Write results to a CSV file.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: loop_type (string), f (float), sigma_over_G (float), R_c_angstrom (float), U_c_eV (float), U_c_normalized (float). No missing values.
- Scoring: scored by hidden verifier

### Step 3: Determine critical stress for faulted loop favorability
- Role: scored (load-bearing)
- Action: Using the computed table, for f=0.01, find the smallest sigma_over_G at which U_c for the faulted loop is strictly less than U_c for the perfect loop. Write the threshold to a text file.
- Output file: `/app/outputs/critical_stress.txt`
- Format: txt
- Contract: A single text line with format 'sigma_over_G = X.XXX' (three decimal digits).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`
- `/app/outputs/critical_stress.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of computed critical radii and activation energies for perfect and faulted loops across a grid of normalized shear stresses and stacking-fault energy ratios.
- schema:
  - `type`: table
  - `required_columns`: `loop_type`, `f`, `sigma_over_G`, `R_c_angstrom`, `U_c_eV`, `U_c_normalized`
  - `units`:
    - `R_c_angstrom`: angstrom
    - `U_c_eV`: eV
    - `U_c_normalized`: unitless (U_c / G b_t^3)

### critical_stress.txt
- path: `/app/outputs/critical_stress.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Reported critical normalized shear stress threshold where faulted loops (f=0.01) become favored over perfect loops.
- schema:
  - `type`: text
  - `required`: Single line matching the pattern 'sigma_over_G = <float>'

Notes: The agent must implement the dislocation nucleation model using the analytical expressions provided in the action descriptions. All material parameters and formulas are specified; no external datasets are required. The root-finding and subsequent derivation of the critical stress are deterministic and reproducible.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "loop_type",
          "f",
          "sigma_over_G",
          "R_c_angstrom",
          "U_c_eV",
          "U_c_normalized"
        ],
        "units": {
          "R_c_angstrom": "angstrom",
          "U_c_eV": "eV",
          "U_c_normalized": "unitless (U_c / G b_t^3)"
        }
      },
      "description": "Table of computed critical radii and activation energies for perfect and faulted loops across a grid of normalized shear stresses and stacking-fault energy ratios."
    },
    {
      "file": "critical_stress.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": "Single line matching the pattern 'sigma_over_G = <float>'"
      },
      "description": "Reported critical normalized shear stress threshold where faulted loops (f=0.01) become favored over perfect loops."
    }
  ],
  "notes": "The agent must implement the dislocation nucleation model using the analytical expressions provided in the action descriptions. All material parameters and formulas are specified; no external datasets are required. The root-finding and subsequent derivation of the critical stress are deterministic and reproducible."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently recomputes the critical radius and activation energy from the same analytical model and checks whether your reported values match within numerical tolerance. The verifier evaluates each output artifact: it reads “/app/outputs/results.csv”, recomputes selected rows and compares; it reads “/app/outputs/critical_stress.txt” and compares the threshold. The final score (a number between 0 and 1) is a weighted combination of the correctness of each artifact. The results.csv table carries the largest weight; the critical_stress.txt file carries a smaller but still meaningful weight. Exact reproduction of the paper's reported numbers is not required — the scoring tolerances account for numerical root‑finding variance — but you must implement the correct physics and compute the quantities honestly from the given equations and constants.
