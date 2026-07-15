# CALPHAD Thermodynamic Modeling of Ge-Bi Liquid Phase

## Problem background
The binary Ge-Bi system exhibits a simple eutectic transformation very close to pure Bi, but its liquidus boundaries are strongly asymmetric, with the Ge-rich side showing steep temperature-composition dependence. Reliable thermodynamic descriptions are essential for semiconductor processing, alloy design, and understanding liquid-phase behavior in germanium-based systems. The CALPHAD (CALculation of PHAse Diagrams) approach models the excess Gibbs energy of the liquid solution as a polynomial in composition and temperature, enabling prediction of phase boundaries from limited experimental data. This task requires determining a subregular solution model for the Ge-Bi liquid from experimental liquidus temperatures and enthalpy-of-mixing measurements, and using it to compute the eutectic point.

## Approach
The liquid phase is modeled as a substitutional solution with ideal mixing of Ge and Bi atoms, plus an excess Gibbs energy term. The excess Gibbs energy is expressed as a Redlich-Kister (subregular) polynomial:

  G^ex = X_Ge * X_Bi [ (A - C*T) + (B - D*T) * X_Bi ]

where X_Ge and X_Bi are mole fractions, T is temperature in Kelvin, and A, B, C, D are coefficients to be determined. The enthalpy of mixing ΔmixH = X_Ge X_Bi (A + B X_Bi) and the excess entropy S^ex = X_Ge X_Bi (C + D X_Bi) are assumed temperature independent.

The determination proceeds in two stages:
1. Least-squares regression of direct calorimetric enthalpy-of-mixing data (at high temperature) to obtain the enthalpy coefficients A and B.
2. Nonlinear optimization of the entropy coefficients C and D against the full set of experimental liquidus points, using the known pure-component Gibbs energy of fusion functions. At each trial (C, D), the liquidus temperature is computed by solving the equality of chemical potentials between liquid and the pure solid phase, assuming negligible solid solubility. The objective is to minimize the sum of squared differences between calculated and experimental liquidus temperatures.

With the full thermodynamic model (ideal + excess), the liquidus boundaries are calculated as the locus of temperatures where the liquid composition is in equilibrium with pure solid Ge or pure solid Bi. The eutectic point is identified as the intersection of the two liquidus branches.

## Reproduction target
Using the provided experimental liquidus data (composition vs temperature) and enthalpy-of-mixing data for the Ge-Bi liquid, together with the pure-element Gibbs energy of fusion functions for Ge and Bi (see Assets), perform the least-squares regression and optimization to determine the four subregular solution parameters (A, B, C, D) that define the excess Gibbs energy of the liquid. Then compute the liquidus boundaries and determine the eutectic temperature (in °C) and eutectic composition (in at.% Bi). Output the optimized parameters in a CSV file (`excess_gibbs_parameters.csv`) and the eutectic coordinates in a separate CSV file (`eutectic_point.csv`). Your result is the thermodynamic model derived from the data; it must be consistent with the input experimental points and the phase equilibrium equations.

## Assets

### Experimental liquidus data (Table 1)

| Temperature (°C) | Composition (at.% Bi) | Reference |
|------------------|----------------------|-----------|
| 910 | 8 | [40Rut] |
| 900 | 13 | [40Rut] |
| 900 | 11 | [40Sto] |
| 890 | 19 | [40Rut] |
| 885 | 23 | [40Sto] |
| 875 | 26 | [40Rut] |
| 870 | 37 | [40Sto] |
| 860 | 34 | [40Rut] |
| 860 | 50 | [40Sto] |
| 850 | 45 | [40Rut] |
| 850 | 63 | [40Sto] |
| 830 | 58 | [40Rut] |
| 800 | 75 | [40Sto] |
| 800 | 79.9 | [60Thu] |
| 755 | 84 | [40Sto] |
| 750 | 76 | [40Rut]  **(outlier – EXCLUDE)** |
| 750 | 88.2 | [60Thu] |
| 700 | 92.72 | [60Thu] |
| 700 | 93.44 | [60Thu] |
| 680 | 92 | [40Sto] |
| 660 | 94.56 | [61Sch] |
| 650 | 95.60 | [60Thu] |
| 600 | 97.27 | [60Thu] |
| 590 | 96 | [40Sto] |
| 580 | 97.63 | [61Sch] |
| 485 | 99.254 | [61Sch] |
| 450 | 99.457 | [61Sch] |
| 435 | 99.501 | [61Sch] |
| 410 | 99.702 | [61Sch] |
| 380 | 99.783 | [61Sch] |
| 365 | 99.843 | [61Sch] |
| 340 | 99.885 | [61Sch] |
| 305 | 99.942 | [61Sch] |
| 285 | 99.954 | [61Sch] |
| 275 | 99.970 | [61Sch] |

**Important:** The point at 750 °C, 76 at.% Bi from [40Rut] is an outlier that must be excluded from all regressions and optimizations. Use all other points.

### Experimental enthalpy of mixing data ([71Pre])

| Composition (at.% Bi) | ΔH_mix (kJ/mol) |
|----------------------|------------------|
| 19.9 | 2.06 |
| 30.0 | 2.70 |
| 39.5 | 3.04 |
| 49.8 | 3.19 |
| 59.9 | 3.06 |
| 69.9 | 2.61 |
| 79.8 | 2.28 |
| 89.5 | 1.37 |

### Pure-component Gibbs energy of fusion functions

The following functions (J/mol, T in Kelvin) from Barin et al. (1977) must be used:

```
Δ_fusG_Ge(T) = 32940 + 23.4575 T + 3.6777e-3 T^2 - 7.7613 T ln T

Δ_fusG_Bi(T) = 4198 + 108.96 T + 15.234e-3 T^2 - 19.9493 T ln T + 2.05e5 T^{-1}
```

### Python libraries

- Python with numpy and scipy (install via pip).

## Workflow steps

### Step 1: Prepare experimental data arrays
- Role: process
- Action: Parse the provided inline experimental liquidus data (temperature, composition) and enthalpy-of-mixing data (composition, enthalpy) into structured numeric arrays. Exclude the one liquidus point that was marked as an outlier in the original evaluation.
- Evidence: none

### Step 2: Fit enthalpy-of-mixing polynomial
- Role: process
- Action: Perform a least-squares regression on the enthalpy data of [71Pre] (the higher-accuracy calorimetric dataset) to determine the coefficients A and B in the subregular solution model ΔmixH = X_Ge * X_Bi (A + B X_Bi). Use the full composition range data.
- Evidence: none

### Step 3: Optimize excess entropy parameters using full liquidus data
- Role: process
- Action: Using the fitted enthalpy polynomial from step_02, the pure-component fusion Gibbs energy functions, and the complete liquidus dataset (all included data points), perform a nonlinear regression/optimization to determine the excess entropy polynomial coefficients C and D in the model S^ex = X_Ge X_Bi (C + D X_Bi) (J/mol·K). Assume temperature independence of the excess entropy. The objective is to minimize the sum of squared deviations between calculated and experimental liquidus temperatures across all data points. This step requires a phase equilibrium solver within the optimization loop.
- Evidence: none

### Step 4: Output Redlich-Kister parameters for the liquid excess Gibbs energy
- Role: scored (load-bearing)
- Action: Write the four subregular solution parameters that define the excess Gibbs energy of the liquid: A, B (from step_02) and C, D (from step_03).
- Output file: `/app/outputs/excess_gibbs_parameters.csv`
- Format: csv
- Contract: CSV with columns: parameter (string, one of 'A', 'B', 'C', 'D'), value (float, units: A and B in J/mol; C and D in J/(mol·K)). Example row: 'A', 12350
- Scoring: scored by hidden verifier

### Step 5: Compute liquidus boundaries and eutectic point
- Role: scored
- Action: Using the complete thermodynamic model for the liquid (excess + ideal) and the pure solid references (assume negligible solid solubility), compute the liquidus boundaries by solving equal chemical potentials along the two-phase regions. Determine the eutectic temperature and composition where the two liquidus branches intersect.
- Output file: `/app/outputs/eutectic_point.csv`
- Format: csv
- Contract: CSV with columns: property (string, one of 'temperature_C', 'composition_at_percent_Bi'), value (float, units: °C or at.% Bi). Example row: 'temperature_C', 271.35
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/excess_gibbs_parameters.csv`
- `/app/outputs/eutectic_point.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### excess_gibbs_parameters.csv
- path: `/app/outputs/excess_gibbs_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Redlich-Kister parameters (A, B, C, D) defining the excess Gibbs energy of the Ge-Bi liquid.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `value`
  - `units`:
    - `parameter`: one of 'A','B','C','D'
    - `value`: float; for A,B: J/mol; for C,D: J/(mol·K)

### eutectic_point.csv
- path: `/app/outputs/eutectic_point.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Assessed eutectic temperature and composition for the Ge-Bi system.
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`
  - `units`:
    - `property`: one of 'temperature_C', 'composition_at_percent_Bi'
    - `value`: float; temperature in °C, composition in at.% Bi

Notes: Both artifacts are compared against hidden reference values from the assessment within prescribed tolerances. The check may also recompute liquidus points from the submitted parameters to verify internal consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "excess_gibbs_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "value"
        ],
        "units": {
          "parameter": "one of 'A','B','C','D'",
          "value": "float; for A,B: J/mol; for C,D: J/(mol·K)"
        }
      },
      "description": "Redlich-Kister parameters (A, B, C, D) defining the excess Gibbs energy of the Ge-Bi liquid."
    },
    {
      "file": "eutectic_point.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value"
        ],
        "units": {
          "property": "one of 'temperature_C', 'composition_at_percent_Bi'",
          "value": "float; temperature in °C, composition in at.% Bi"
        }
      },
      "description": "Assessed eutectic temperature and composition for the Ge-Bi system."
    }
  ],
  "notes": "Both artifacts are compared against hidden reference values from the assessment within prescribed tolerances. The check may also recompute liquidus points from the submitted parameters to verify internal consistency."
}
```

## How you are scored
A hidden verifier will independently check your submitted artifacts after your run completes. For `excess_gibbs_parameters.csv`, it will compare your reported A, B, C, D values to reference values derived from the original thermodynamic assessment, within an appropriate tolerance that accounts for numerical implementation differences. For `eutectic_point.csv`, it will compare your reported eutectic temperature and composition to the assessed eutectic point using a similarly calibrated tolerance. The verifier may also perform a consistency check by computing the liquidus curve from your submitted parameters at a set of hidden compositions and verifying that it passes through the pure component melting points and that the predicted liquidus temperatures are close to those implied by the original assessment. The final score is a weighted combination of the scores for these two artifacts, with the excess Gibbs parameters carrying the primary weight. Reporting paper-known numbers without genuinely executing the described regression and equilibrium solver will not pass these checks.
