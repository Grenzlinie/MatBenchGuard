# Computational Molecular CO3 Ground-State Geometry and Excited States at MBPT and RPA Levels

## Problem background
Carbon trioxide (CO3) is a reactive intermediate formed in the upper atmosphere of Mars and other planetary bodies when CO2 reacts with O(1D). Its equilibrium geometry has been debated: both a cyclic C2v and an open Cs structure have been proposed. Electron correlation plays a central role in determining the true ground-state structure, the stability of CO3 with respect to formation (CO2 + O(1D) → CO3) and decomposition (CO3 + CO → 2CO2), and the nature of its low-lying singlet excited states. Resolving these quantities requires high-level many-body calculations that go beyond simple self-consistent field (SCF) theory.

## Approach
The ground-state geometry of CO3 is determined by performing a geometry optimization at the level of fourth-order many-body perturbation theory restricted to single and double substitutions (SD MBPT(4)) with a frozen-core approximation and a double-zeta plus polarization (DZP) basis set. Using this geometry, total energies of CO3, CO2, CO, and the O(1D) atom are computed at the same SD MBPT(4)/DZP level to obtain the formation and decomposition reaction energies. To characterize the excited states, a larger basis including diffuse functions (DZDP) is employed; the vertical excitation energies and oscillator strengths (length and velocity forms) of the five lowest singlet states are computed within the random-phase approximation (RPA). All calculations are carried out with the open-source quantum chemistry package PySCF.

## Reproduction target
Compute and report the following quantities in the specified output files:
1. The optimized ground-state geometry of CO3 (bond lengths r(C–O1), r(C–O2,3), r(O2–O3) and the O2–C–O3 bond angle) at the SD MBPT(4)/DZP level.
2. The energy released in the formation reaction CO2 + O(1D) → CO3 (δ1) and in the decomposition reaction CO3 + CO → 2CO2 (δ2) at the same SD MBPT(4)/DZP level, expressed in eV.
3. The vertical excitation energies, oscillator strengths (length form f_L and velocity form f_v), and dominant particle-hole excitations for the five lowest singlet excited states of CO3 below 8 eV, evaluated at the RPA/DZDP level using the optimized geometry from step 1.

## Assets

- PySCF: https://pypi.org/project/pyscf/

## Workflow steps

### Step 1: CO3 geometry optimization and record
- Role: scored
- Action: Perform a geometry optimization of neutral CO3 in a singlet C2v electronic state at the SD MBPT(4) level with the DZP basis set (9s5p1d/4s2p1d contraction, polarization exponents α_d^C=0.8, α_d^O=0.9) using the frozen-core approximation. Extract the final bond lengths and angle: C–O1, C–O2,3, O2–O3, and the O2–C–O3 bond angle. Write the results to step_01_geometry.csv.
- Output file: `/app/outputs/step_01_geometry.csv`
- Format: csv
- Contract: label(string),value(float),unit(string) – four rows: r(C-O1) in Å, r(C-O2,3) in Å, r(O2-O3) in Å, angle(O2CO3) in deg
- Scoring: scored by hidden verifier

### Step 2: Reaction energy calculations
- Role: scored
- Action: Compute the formation energy δ1 = E(CO3) − E(CO2) − E(O(1D)) and the decomposition energy δ2 = 2⋅E(CO2) − E(CO3) − E(CO) in eV. For this, optimize CO and CO2 at the SD MBPT(4)/DZP level (same basis and frozen-core approximation) and compute their total energies. Also compute the total energy of the O(1D) atom at the SD MBPT(4)/DZP level. Use the CO3 geometry from step 1 for its total energy. Write the two reaction energies to step_02_formation_energy.csv.
- Output file: `/app/outputs/step_02_formation_energy.csv`
- Format: csv
- Contract: reaction(string),delta_E_eV(float) – two rows: CO2+O1D->CO3 (d1), CO3+CO->2CO2 (d2)
- Scoring: scored by hidden verifier

### Step 3: RPA excitation energies and oscillator strengths
- Role: scored
- Action: Using the CO3 geometry from step 1, perform an SCF calculation with the DZDP basis set (11s6p1d/6s3p1d, diffuse exponents: α_s^O=0.08,0.026, α_p^O=0.064, α_s^C=0.048,0.015, α_p^C=0.036). Then compute the vertical excitation energies and oscillator strengths (length form f_L and velocity form f_v) of the five lowest singlet excited states below 8 eV within the random-phase approximation (RPA). Include the dominant particle-hole excitation for each state. For dipole-forbidden A2 transitions, write a dash ('–') in the f_L and f_v columns instead of a numeric value. Write the results to step_03_excited_states.csv.
- Output file: `/app/outputs/step_03_excited_states.csv`
- Format: csv
- Contract: state(string),delta_E_eV(float),f_L(float or '-' for forbidden),f_v(float or '-' for forbidden),dominant_excitation(string) – five rows: B1(x), A1(z), A2, B2(y), A2
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_geometry.csv`
- `/app/outputs/step_02_formation_energy.csv`
- `/app/outputs/step_03_excited_states.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_geometry.csv
- path: `/app/outputs/step_01_geometry.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimized ground-state geometry of CO3 at SD MBPT(4)/DZP level: four rows for bond lengths and angle.
- schema:
  - `type`: table
  - `required_columns`: `label`, `value`, `unit`
  - `units`:
    - `value`: Å or deg

### step_02_formation_energy.csv
- path: `/app/outputs/step_02_formation_energy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Formation and decomposition energies of CO3 at SD MBPT(4)/DZP level.
- schema:
  - `type`: table
  - `required_columns`: `reaction`, `delta_E_eV`
  - `units`:
    - `delta_E_eV`: eV

### step_03_excited_states.csv
- path: `/app/outputs/step_03_excited_states.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: RPA vertical excitation energies and oscillator strengths for five lowest singlet states of CO3 (DZDP basis). For dipole-forbidden A2 states, f_L and f_v are given as dash ('–').
- schema:
  - `type`: table
  - `required_columns`: `state`, `delta_E_eV`, `f_L`, `f_v`, `dominant_excitation`
  - `units`:
    - `delta_E_eV`: eV
    - `f_L`: dimensionless or dash for forbidden
    - `f_v`: dimensionless or dash for forbidden

Notes: All calculations use the specified basis sets and method levels. The hidden checker compares the computed numeric values against paper-reported values with tolerances that account for implementation differences. For forbidden transitions, oscillator strengths are expected as dashes ('–').

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_geometry.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "label",
          "value",
          "unit"
        ],
        "units": {
          "value": "Å or deg"
        }
      },
      "description": "Optimized ground-state geometry of CO3 at SD MBPT(4)/DZP level: four rows for bond lengths and angle."
    },
    {
      "file": "step_02_formation_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction",
          "delta_E_eV"
        ],
        "units": {
          "delta_E_eV": "eV"
        }
      },
      "description": "Formation and decomposition energies of CO3 at SD MBPT(4)/DZP level."
    },
    {
      "file": "step_03_excited_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "state",
          "delta_E_eV",
          "f_L",
          "f_v",
          "dominant_excitation"
        ],
        "units": {
          "delta_E_eV": "eV",
          "f_L": "dimensionless or dash for forbidden",
          "f_v": "dimensionless or dash for forbidden"
        }
      },
      "description": "RPA vertical excitation energies and oscillator strengths for five lowest singlet states of CO3 (DZDP basis). For dipole-forbidden A2 states, f_L and f_v are given as dash ('–')."
    }
  ],
  "notes": "All calculations use the specified basis sets and method levels. The hidden checker compares the computed numeric values against paper-reported values with tolerances that account for implementation differences. For forbidden transitions, oscillator strengths are expected as dashes ('–')."
}
```

## How you are scored
Each scored workflow step produces a CSV file under `/app/outputs`. A hidden verifier independently reads these files and compares every numeric field against a set of reference values. The comparison uses tolerances that account for expected numerical differences between different quantum chemistry implementations while remaining tight enough to require a correct computation. The verifier assigns a score per step and combines them into a single final reward between 0 and 1. Reporting a number by itself without actually performing the computation will not pass the tolerance checks.
