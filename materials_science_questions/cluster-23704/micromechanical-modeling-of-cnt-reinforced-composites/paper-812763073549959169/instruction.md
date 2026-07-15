# Fundamental frequencies of CNT-reinforced composite plates via GDQ method

## Problem background
This work addresses free vibration of square polyethylene plates of thickness h = 0.005 m, reinforced with short- and long-(10,10) single-walled carbon nanotubes. The side length L follows from the aspect ratio L/h as L = 0.005 * (L/h) m. The effective elastic properties of the nanocomposite are determined from a modified rule of mixture using CNT efficiency parameters that account for the scale effect between the matrix and the nanotubes. The governing differential equations of motion for classical plate theory (CLPT), first-order shear deformation theory (FSDT), and higher-order shear deformation theory (HSDT) are discretized via the generalized differential quadrature (GDQ) method and solved as eigenvalue problems to yield the fundamental natural frequencies under simply supported (SSSS) and clamped (CCCC) edge conditions.

## Approach
The analysis proceeds in two stages. First, the effective orthotropic material constants (Young's moduli, shear modulus, Poisson's ratios, and density) are computed for each reinforcement type (short-SWCNT, long-SWCNT) at each CNT volume fraction using the modified rule of mixture, with CNT efficiency parameters provided as fixed inputs. For the pure matrix case, unfilled polyethylene properties are used. Second, the generalized differential quadrature (GDQ) method is applied to discretize the free-vibration governing equations for each plate theory. Grid-point weighting coefficients are computed, boundary conditions are imposed (SSSS or CCCC), and the resulting algebraic eigenvalue problem is solved for the smallest eigenvalue, giving the fundamental frequency. The process is repeated for every combination of reinforcement type, plate theory, boundary condition, aspect ratio (L/h = 10, 20, 40), and CNT volume fraction (0%, 5%, 10%, 15%). A shear correction factor κ = 5/6 is used in the FSDT formulation. The effective composite Poisson's ratios are computed as ν12 = V_CNT ν_CNT + V_m ν_m and ν21 = ν12 E22 / E11.

## Reproduction target
Your task is to compute the fundamental natural frequency (in kHz) for every combination of reinforcement type (short, long), plate theory (CLPT, FSDT, HSDT), boundary condition (SSSS, CCCC), aspect ratio (L/h = 10, 20, 40), and CNT volume fraction (0%, 5%, 10%, 15%). Write the results as a CSV file (frequencies.csv) with one row per combination and columns: reinforcement_type, plate_theory, boundary, aspect_ratio, CNT_volume_fraction, frequency_kHz. The accuracy of your computed frequencies will be evaluated against reference values (hidden from you) using a tolerance-based checker; the fraction of rows that are within tolerance determines your score.

## Assets

- CNT efficiency parameters: provided as fixed constants (table below), with θ3 = θ2 for shear modulus.
- Matrix and CNT material properties: as specified in the material constants table below.

### CNT efficiency parameters

| CNT volume fraction | θ1 (short) | θ2 (short) | θ1 (long) | θ2 (long) |
|---|---|---|---|---|
| 5% | 0.0253 | 1.0354 | 2.1587 | 1.17767 |
| 10% | 0.0444 | 1.2853 | 1.6346 | 1.4775 |
| 15% | 0.0627 | 1.7799 | 1.6877 | 2.0590 |

For 0% CNT (pure matrix), the rule of mixture gives the matrix properties directly; no efficiency parameters are needed.

### Matrix and CNT material properties

| Property | Polyethylene matrix | (10,10) SWCNT |
|---|---|---|
| Young's modulus | Em = 3.22 GPa | E11 = 600 GPa, E22 = 10 GPa |
| Shear modulus | Gm = Em / [2(1+νm)] ≈ 1.238 GPa | G12 = 5 GPa |
| Poisson's ratio | νm = 0.3 | ν_CNT = 0.19 |
| Density | ρm = 925 kg/m³ | ρ_CNT = 2300 kg/m³ |

## Workflow steps

### Step 1: Compute effective material properties
- Role: process
- Action: Using the modified rule of mixture and the provided CNT efficiency parameters, compute the effective orthotropic elastic constants (E11, E22, G12) and Poisson's ratios for each reinforcement type (short, long) and each CNT volume fraction (0%, 5%, 10%, 15%). For 0% CNT, use pure matrix properties. Also compute the composite density from the rule of mixtures using the provided constituent densities. Store these properties for use in the subsequent GDQ analysis.
- Evidence: `/app/outputs/material_properties.csv`

### Step 2: Compute fundamental frequencies via GDQ
- Role: scored (load-bearing)
- Action: Implement the generalized differential quadrature (GDQ) method to discretize the governing differential equations of free vibration for orthotropic square plates according to classical plate theory (CLPT), first-order shear deformation theory (FSDT), and higher-order shear deformation theory (HSDT). For each combination of reinforcement type (short, long), plate theory, boundary condition (simply supported SSSS, clamped CCCC), aspect ratio (L/h = 10, 20, 40), and CNT volume fraction (0%, 5%, 10%, 15%), set up the algebraic eigenvalue problem and solve for the lowest natural frequency (fundamental frequency) in kHz. Output all results to frequencies.csv.
- Output file: `/app/outputs/frequencies.csv`
- Format: csv
- Contract: Columns: reinforcement_type (string, 'short' or 'long'), plate_theory (string, 'CLPT'/'FSDT'/'HSDT'), boundary (string, 'SSSS'/'CCCC'), aspect_ratio (int, 10, 20, or 40), CNT_volume_fraction (float, 0.0, 0.05, 0.10, or 0.15), frequency_kHz (float). One row per unique combination, no header duplication.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### frequencies.csv
- path: `/app/outputs/frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fundamental frequencies of SWCNT-reinforced composite plates for all combinations of reinforcement type, plate theory, boundary condition, aspect ratio, and CNT volume fraction.
- schema:
  - `type`: table
  - `required_columns`: `reinforcement_type`, `plate_theory`, `boundary`, `aspect_ratio`, `CNT_volume_fraction`, `frequency_kHz`
  - `units`:
    - `frequency_kHz`: kHz

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reinforcement_type",
          "plate_theory",
          "boundary",
          "aspect_ratio",
          "CNT_volume_fraction",
          "frequency_kHz"
        ],
        "units": {
          "frequency_kHz": "kHz"
        }
      },
      "description": "Fundamental frequencies of SWCNT-reinforced composite plates for all combinations of reinforcement type, plate theory, boundary condition, aspect ratio, and CNT volume fraction."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your output file (/app/outputs/frequencies.csv) and compares each computed frequency to a reference frequency using a tolerance-based criterion. The tolerance is chosen to accept small numerical differences between independent implementations while still distinguishing correct from incorrect results. Your score is proportional to the number of rows that pass this check. The process-step evidence (material_properties.csv) may be checked for consistency but carries only minor weight.
