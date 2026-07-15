# Spin-1 Transverse Ising Model Effective-Field Theory Reproduction

## Problem background
The spin-1 transverse Ising model (TIM) describes a system of interacting spin-1 particles subject to a transverse magnetic field. It is a fundamental model for quantum phase transitions, exhibiting a ferromagnetic phase at low temperatures and a paramagnetic phase at higher temperatures, with a critical transverse field that suppresses ordering even at zero temperature. Exact solutions exist only in one dimension, so approximate methods are needed for higher-dimensional lattices. This task concerns the honeycomb lattice (coordination number Z=3) and implements an effective-field theory (EFT) that goes beyond standard mean-field theory by treating the single-ion spin identity exactly while neglecting multi-spin correlations. The goal is to compute the phase boundary and the temperature/field dependence of the order parameters.

## Approach
The effective-field theory starts from an exact Callen-Suzuki-like identity for spin-1, expressed using a differential operator technique and the van der Waerden identity for spin-1. Under the simplest decoupling approximation that replaces any product of spin variables at different sites by the product of their averages, the problem reduces to a set of four self-consistent equations for the longitudinal magnetization m^z, transverse magnetization m^x, longitudinal quadrupolar moment q^z, and transverse quadrupolar moment q^x. These equations depend only on the lattice coordination number Z, the exchange interaction J, the transverse field Ω, and the temperature T. For the honeycomb lattice (Z=3), the critical phase boundary is obtained by linearizing these equations around m^z=0 and solving for the temperature T_c at each Ω such that the linearized system becomes unstable. The full order parameter curves are found by solving the coupled nonlinear equations numerically for the given conditions.

## Reproduction target
Implement the effective-field theory for the spin-1 TIM on a honeycomb lattice (Z=3) and compute the following quantities, which constitute the main results of the study: (1) The ferromagnetic phase boundary, i.e., the critical temperature T_c as a function of the transverse field Ω, from Ω = 0 to above the critical field. (2) The temperature dependence of the magnetizations m^z, m^x and quadrupolar moments q^z, q^x at a fixed transverse field Ω/J = 1.5. (3) The field dependence of m^z and m^x at a fixed low temperature k_B T / J = 0.05. All results are to be output as CSV files with the specified columns.

## Assets

- NumPy: https://numpy.org/
- SciPy: https://scipy.org/

## Workflow steps

### Step 1: Critical temperature curve
- Role: scored (load-bearing)
- Action: Implement the effective-field theory equations for the spin-1 transverse Ising model on a honeycomb lattice (coordination number Z=3) under the simplest decoupling approximation. For a range of transverse field values Ω/J from 0 to above the critical field Ω_c/J, compute the critical temperature k_B T_c / J where the longitudinal magnetization m^z → 0. Output the resulting phase boundary.
- Output file: `/app/outputs/critical_temperature.csv`
- Format: csv
- Contract: Two columns: 'omega_over_J' (Ω/J) and 'kBTc_over_J' (k_B T_c / J). Values are dimensionless.
- Scoring: scored by hidden verifier

### Step 2: Temperature dependence at Ω=1.5J
- Role: scored
- Action: For a fixed transverse field Ω/J = 1.5, solve the full self-consistent effective-field equations for Z=3 to obtain the longitudinal magnetization m^z, transverse magnetization m^x, longitudinal quadrupolar moment q^z, and transverse quadrupolar moment q^x over a range of temperatures from zero to above the critical temperature at this Ω. Output the temperature curves.
- Output file: `/app/outputs/temperature_dependence_omega1.5.csv`
- Format: csv
- Contract: Six columns: 'kBT_over_J', 'mz', 'mx', 'qz', 'qx'. All dimensionless.
- Scoring: scored by hidden verifier

### Step 3: Field dependence at T=0.05J
- Role: scored
- Action: For a fixed temperature k_B T / J = 0.05, solve the self-consistent effective-field equations for Z=3 to obtain m^z and m^x as functions of Ω. Use Ω/J from 0 to above the critical field. Output the field curves.
- Output file: `/app/outputs/field_dependence_T0.05.csv`
- Format: csv
- Contract: Three columns: 'omega_over_J', 'mz', 'mx'. All dimensionless.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_temperature.csv`
- `/app/outputs/temperature_dependence_omega1.5.csv`
- `/app/outputs/field_dependence_T0.05.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_temperature.csv
- path: `/app/outputs/critical_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical temperature as a function of transverse field for the spin-1 TIM on a honeycomb lattice within EFT. Compared against the paper's published phase boundary.
- schema:
  - `type`: table
  - `required_columns`: `omega_over_J`, `kBTc_over_J`
  - `units`:
    - `omega_over_J`: dimensionless
    - `kBTc_over_J`: dimensionless

### temperature_dependence_omega1.5.csv
- path: `/app/outputs/temperature_dependence_omega1.5.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature dependence of magnetizations and quadrupolar moments at Ω/J=1.5. Compared against paper-reported quantities.
- schema:
  - `type`: table
  - `required_columns`: `kBT_over_J`, `mz`, `mx`, `qz`, `qx`
  - `units`:
    - `kBT_over_J`: dimensionless
    - `mz`: dimensionless
    - `mx`: dimensionless
    - `qz`: dimensionless
    - `qx`: dimensionless

### field_dependence_T0.05.csv
- path: `/app/outputs/field_dependence_T0.05.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Transverse field dependence of magnetizations at kBT/J=0.05. Compared against paper-reported curves.
- schema:
  - `type`: table
  - `required_columns`: `omega_over_J`, `mz`, `mx`
  - `units`:
    - `omega_over_J`: dimensionless
    - `mz`: dimensionless
    - `mx`: dimensionless

Notes: All outputs are generated by numerically solving the EFT self-consistent equations for the spin-1 TIM on a honeycomb lattice. The hidden reference values are the paper's reported results, used for tolerance-based scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega_over_J",
          "kBTc_over_J"
        ],
        "units": {
          "omega_over_J": "dimensionless",
          "kBTc_over_J": "dimensionless"
        }
      },
      "description": "Critical temperature as a function of transverse field for the spin-1 TIM on a honeycomb lattice within EFT. Compared against the paper's published phase boundary."
    },
    {
      "file": "temperature_dependence_omega1.5.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "kBT_over_J",
          "mz",
          "mx",
          "qz",
          "qx"
        ],
        "units": {
          "kBT_over_J": "dimensionless",
          "mz": "dimensionless",
          "mx": "dimensionless",
          "qz": "dimensionless",
          "qx": "dimensionless"
        }
      },
      "description": "Temperature dependence of magnetizations and quadrupolar moments at Ω/J=1.5. Compared against paper-reported quantities."
    },
    {
      "file": "field_dependence_T0.05.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega_over_J",
          "mz",
          "mx"
        ],
        "units": {
          "omega_over_J": "dimensionless",
          "mz": "dimensionless",
          "mx": "dimensionless"
        }
      },
      "description": "Transverse field dependence of magnetizations at kBT/J=0.05. Compared against paper-reported curves."
    }
  ],
  "notes": "All outputs are generated by numerically solving the EFT self-consistent equations for the spin-1 TIM on a honeycomb lattice. The hidden reference values are the paper's reported results, used for tolerance-based scoring."
}
```

## How you are scored
Your solution is scored by a hidden verifier that evaluates each of the three scored CSV artifacts independently and combines their scores by weight into a final reward in [0,1]. The verifier compares the computed curves against a set of hidden reference values (derived from the original study) using appropriate tolerances. It also checks key structural properties, such as the longitudinal magnetization decreasing to zero at the critical temperature and the transverse magnetization exhibiting a kink there. Simply reporting a number that matches a published result is not sufficient; you must genuinely implement the theory and produce the curves through the computational workflow described. The hidden reference values are not disclosed, so you must rely on the physics to achieve a successful reproduction.
