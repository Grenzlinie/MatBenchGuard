# Compute lattice heat capacity from low-frequency phonon spectrum

## Problem background
Indium exhibits an anomalously low lattice heat capacity at very low temperatures, falling below the Debye T³ prediction. This anomaly has been attributed in part to phonon dispersion effects that reduce the density of states at low frequencies. In a computational study, a low-frequency vibrational spectrum g(ν) was derived from the elastic constants, and the corresponding lattice heat capacity was computed. Your task is to reproduce that computation: given the analytical low-frequency spectrum g(ν) and the Debye temperature, compute the lattice heat capacity C_v/3R at several sub‑1 K temperatures and prepare a result that can be compared to the Debye prediction and to experimental lattice heat capacity measurements for superconducting indium. This will test whether the given spectrum can account for some of the observed anomaly.

## Approach
The full reproduction follows the paper’s procedure:  
1. Evaluate the force constants for a monatomic body-centered tetragonal lattice from the six independent elastic constants of indium at 0 K.  
2. Set up the dynamical matrix and solve the secular equation on a fine mesh of wave vectors in the neighborhood of the Γ point to obtain phonon frequencies.  
3. Compute the vibrational density of states g(ν) from the resulting frequencies, normalized to 3N, and fit a low-energy polynomial approximation of the form g(ν) = a ν² + b ν⁴ in the range 0–2.5×10¹¹ Hz.  
4. Finally, numerically integrate the standard phonon heat capacity formula using the fitted g(ν) to obtain C_v/3R at five temperatures between 0.2 K and 1.0 K.  
The results will be compared against the Debye T³ law (Θ_D = 111.3 K) and experimental lattice heat capacity data for superconducting indium (which the verifier will use, but you do not need to retrieve). This sequence tests whether the elastic constants and harmonic lattice dynamics can account for the observed low‑temperature heat capacity anomaly.

## Reproduction target
Starting from the six independent elastic constants of indium at 0 K (C₁₁, C₁₂, C₁₃, C₃₃, C₄₄, C₆₆) and the crystallographic lattice parameters (a, c), derive the short‑range force constants up to second‑nearest neighbors, solve the secular equation on a grid of k‑points near the Γ point, obtain the low‑frequency phonon density of states g(ν), and finally compute the dimensionless lattice heat capacity C_v/3R at temperatures T = 0.2, 0.4, 0.6, 0.8, 1.0 K. Output a CSV file `/app/outputs/heat_capacity.csv` with columns `temperature_K` and `C_v_over_3R`. The file must contain exactly five rows, one per temperature, with a header. The required elastic constants and lattice parameters are listed in the Assets section.

## Assets
The elastic constants of indium at 0 K (in units of 10¹⁰ N m⁻²) as reported by Chandrasekhar and Rayne (1961):  
C₁₁ = 5.38,  C₁₂ = 2.42,  C₁₃ = 2.30,  C₃₃ = 5.09,  C₄₄ = 2.01,  C₆₆ = 1.51.  
The lattice parameters at 0 K: a = 3.25 Å, c = 4.95 Å (body‑centered tetragonal, two atoms per conventional cell).  
The force‑constant model and secular equation are described by Slutsky and Livingston (J. Chem. Phys. 32, 1093 (1960)); you should implement the dynamical matrix for first‑ and second‑nearest‑neighbor interactions. No other external datasets are required. The computation can be performed using standard Python numerical packages (numpy, scipy).

## Workflow steps

### Step 1: Evaluate force constants
- Role: process
- Action: Using the elastic constants and lattice parameters, compute the independent force constants for first‑ and second‑nearest‑neighbor interactions following the Slutsky–Livingston model. Output the force constants as evidence to `/app/outputs/force_constants.txt`.
- Evidence: `force_constants.txt`

### Step 2: Solve secular equation and compute g(ν)
- Role: process
- Action: Set up the dynamical matrix for the two‑atom body‑centered tetragonal cell, solve the eigenvalue problem for wave vectors (y₁, y₂, y₃) in the range 0 to 0.2 with step 0.004 as in the paper, and collect the 2×Nₖ frequencies. Normalize the distribution to 3 Nₐ per mole and fit a polynomial g(ν) = a ν² + b ν⁴ over 0–2.5×10¹¹ Hz. Write the fitted coefficients a and b to `/app/outputs/g_fit.csv` (two columns: coefficient, value).  
- Evidence: `g_fit.csv`

### Step 3: Compute lattice heat capacity
- Role: scored (load-bearing)
- Action: Using the fitted g(ν) = a ν² + b ν⁴ from Step 2 and the Debye temperature Θ_D = 111.3 K, numerically integrate the standard phonon heat capacity formula to obtain C_v/3R at T = 0.2, 0.4, 0.6, 0.8, 1.0 K. Save the results as a CSV file at `/app/outputs/heat_capacity.csv` with columns temperature_K and C_v_over_3R.
- Output file: `/app/outputs/heat_capacity.csv`
- Format: csv
- Contract: Columns: temperature_K (float, temperatures 0.2,0.4,0.6,0.8,1.0), C_v_over_3R (float, dimensionless). Header row included. Exactly five rows, one per temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heat_capacity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heat_capacity.csv
- path: `/app/outputs/heat_capacity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed lattice heat capacity per mole divided by 3R at five low temperatures, demonstrating the intermediate position relative to Debye prediction and experimental data.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `C_v_over_3R`
  - `units`:
    - `temperature_K`: Kelvin
    - `C_v_over_3R`: dimensionless

Notes: The low-frequency phonon spectrum g(ν) and Debye temperature are provided directly in the task instruction. The checker will recompute the reference C_v/3R values by integrating the same expression and compare the agent's values using a relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heat_capacity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "C_v_over_3R"
        ],
        "units": {
          "temperature_K": "Kelvin",
          "C_v_over_3R": "dimensionless"
        }
      },
      "description": "Computed lattice heat capacity per mole divided by 3R at five low temperatures, demonstrating the intermediate position relative to Debye prediction and experimental data."
    }
  ],
  "notes": "The low-frequency phonon spectrum g(ν) and Debye temperature are provided directly in the task instruction. The checker will recompute the reference C_v/3R values by integrating the same expression and compare the agent's values using a relative tolerance."
}
```

## How you are scored
A hidden verifier will evaluate your submission. It will recompute the reference C_v/3R values by carrying out the same force‑constant, phonon, and integration steps from the same inputs. Your submitted values will be compared to these references using a relative tolerance. Additional structural checks ensure the results are physically plausible. The final reward, a number between 0 and 1, combines these checks.
