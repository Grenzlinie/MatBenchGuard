# Reproduce thermomechanical cycle simulations of a shape memory polymer using a distributed-Tg micromechanical model

## Problem background
Shape memory polymers (SMPs) can be temporarily fixed in a deformed shape and later recover their original shape upon heating. Their mechanical properties change dramatically around a glass transition temperature (Tg): above Tg the material is rubbery, while below Tg it becomes glassy and locks in deformation. The extent of shape fixation and the subsequent recovery are known to depend not only on the current temperature and strain, but also on the temperature and strain history experienced during shape fixation. This task investigates whether a micromechanical model with a distribution of glass transition temperatures can capture such history dependence by simulating two distinct thermomechanical cycles (EXP1 and EXP2) and computing the resulting fixed strain ratios and residual fixed strain ratio curves during reheating.

## Approach
The approach is to implement a micromechanical model that represents the SMP as a collection of 1000 parallel microscopic elements, each governed by an 8-element viscoelastic constitutive model. The model consists of four springs, two dashpots, a thermal expansion element, and a latch that freezes deformation when the element's local temperature drops below its own Tg. A prescribed distribution of glass transition temperatures is assigned to the elements, reflecting the inherent heterogeneity of the material. The distribution used here (CAL1) is given below.

Two shape-fixation protocols are simulated:
- EXP1: the entire specimen is stretched to 10% strain at a constant high temperature (50 °C), then cooled to 0 °C while holding the strain, unloaded, and finally heated back to 50 °C.
- EXP2: strain is applied in stages while the specimen is simultaneously cooled in steps (strain increased from 0% to 10% between 50 °C and 0 °C), then unloaded at 0 °C and heated to 50 °C.

For each protocol the simulation produces time-series of stress, strain, and temperature from which the following derived quantities are extracted (see Workflow steps). Material constants (CAL1, from Table 1 of the source) are:
k = 0.00156, lg = 0.648, lr = 1.59, Eg1 = 1610 MPa, Er1 = 11600 MPa, Eg2 = 1040 MPa, Er2 = 18400 MPa, Er3 = 18.1 MPa, Er4 = 28.8 MPa, μg1 = 85.7 GPa·s, μr1 = 1630 GPa·s, μr2 = 2.54 GPa·s, α = 0.000190 /°C.

Glass transition temperature distribution (CAL1): 1000 elements are assigned to 2 °C wide bins (centre temperature). The counts per bin are:

| Tg centre (°C) | Number of elements |
|----------------|-------------------|
| 1             | 0                |
| 3             | 0                |
| 5             | 1                |
| 7             | 2                |
| 9             | 4                |
| 11            | 8                |
| 13            | 15               |
| 15            | 25               |
| 17            | 38               |
| 19            | 53               |
| 21            | 68               |
| 23            | 80               |
| 25            | 88               |
| 27            | 90               |
| 29            | 87               |
| 31            | 80               |
| 33            | 70               |
| 35            | 58               |
| 37            | 45               |
| 39            | 33               |
| 41            | 22               |
| 43            | 14               |
| 45            | 8                |
| 47            | 4                |
| 49            | 2                |

The model equations are given in the source paper: For T < Tg the strain is fixed (latch engaged) and the stress–strain rate relation involves Eg1, Eg2, μg1; for T ≥ Tg the latch is free and an additional branch (Er3, Er4, μr2) becomes active. The solver must handle the Tg crossing of each element individually.

## Reproduction target
Reproduce the thermomechanical simulations for both EXP1 and EXP2 and deliver two scored artifacts:
1) fixed_strain_ratios.json – the residual strain after unloading (when stress first returns to zero) divided by the maximum applied strain (10%), expressed as a percentage, for each protocol.
2) residual_fixed_strain_ratios.csv – during the reheating phase, the strain at a given temperature divided by the fixed strain after unloading, expressed as a percentage, sampled at 0.5 °C intervals from 0 °C to 50 °C, for both EXP1 and EXP2.

## Assets

- Python 3 scientific stack (numpy, scipy, matplotlib): python3

## Workflow steps

### Step 1: Run micromechanical model simulations
- Role: process
- Action: Implement the 8-element micromechanical model with 1000 parallel elements using the provided material constants (CAL1) and glass transition temperature distribution, and simulate the thermomechanical cycles EXP1 and EXP2 to obtain time-series of stress, strain, and temperature.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Compute fixed strain ratios
- Role: scored (load-bearing)
- Action: From the simulation results, compute the fixed strain ratio (residual strain after unloading divided by maximum applied strain, expressed as percentage) for EXP1 and EXP2. Write the two values to fixed_strain_ratios.json.
- Output file: `/app/outputs/fixed_strain_ratios.json`
- Format: json
- Contract: JSON object with keys 'EXP1' and 'EXP2', each a float representing the percentage.
- Scoring: scored by hidden verifier

### Step 3: Generate residual fixed strain ratio curves
- Role: scored
- Action: Using the heating-phase simulation data, compute the residual fixed strain ratio (current strain divided by fixed strain after unloading, expressed as percentage) for temperatures from 0 to 50°C at 0.5°C intervals for both EXP1 and EXP2. Write to residual_fixed_strain_ratios.csv with columns: temperature, exp1_ratio, exp2_ratio.
- Output file: `/app/outputs/residual_fixed_strain_ratios.csv`
- Format: csv
- Contract: CSV with header: temperature,exp1_ratio,exp2_ratio. Values at 0.5°C intervals from 0 to 50°C inclusive (101 rows). All columns are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fixed_strain_ratios.json`
- `/app/outputs/residual_fixed_strain_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fixed_strain_ratios.json
- path: `/app/outputs/fixed_strain_ratios.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fixed strain ratio for EXP1 and EXP2, compared to hidden gold values with a tolerance of ±2 percentage points.
- schema:
  - `type`: object
  - `required`:
    - `EXP1`: float
    - `EXP2`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `EXP1`: %
    - `EXP2`: %

### residual_fixed_strain_ratios.csv
- path: `/app/outputs/residual_fixed_strain_ratios.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Residual fixed strain ratio curves for EXP1 and EXP2. Checker verifies that exp1_ratio > exp2_ratio for all temperatures below 40°C and that the curves satisfy monotonicity and crossover properties.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `temperature`, `exp1_ratio`, `exp2_ratio`
  - `units`:
    - `temperature`: °C
    - `exp1_ratio`: %
    - `exp2_ratio`: %

Notes: Fixed strain ratios checked with exact_match (tolerance ±2 pp). Residual curves checked via structural_audit (EXP1 always above EXP2 below 40°C, monotonic, crossover).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fixed_strain_ratios.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "EXP1": "float",
          "EXP2": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "EXP1": "%",
          "EXP2": "%"
        }
      },
      "description": "Fixed strain ratio for EXP1 and EXP2, compared to hidden gold values with a tolerance of ±2 percentage points."
    },
    {
      "file": "residual_fixed_strain_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "temperature",
          "exp1_ratio",
          "exp2_ratio"
        ],
        "units": {
          "temperature": "°C",
          "exp1_ratio": "%",
          "exp2_ratio": "%"
        }
      },
      "description": "Residual fixed strain ratio curves for EXP1 and EXP2. Checker verifies that exp1_ratio > exp2_ratio for all temperatures below 40°C and that the curves satisfy monotonicity and crossover properties."
    }
  ],
  "notes": "Fixed strain ratios checked with exact_match (tolerance ±2 pp). Residual curves checked via structural_audit (EXP1 always above EXP2 below 40°C, monotonic, crossover)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects the two output files. For fixed_strain_ratios.json it checks that the EXP1 and EXP2 values are within an allowed tolerance of independently computed reference values. For residual_fixed_strain_ratios.csv it interpolates your curves onto a common temperature grid, computes the mean absolute error against digitised reference curves, and verifies that the EXP1 residual ratio stays above the EXP2 residual ratio for temperatures below 40 °C. Each artifact contributes to the final reward. Simply reporting numbers without actually running the simulation will not satisfy the scoring criteria.
