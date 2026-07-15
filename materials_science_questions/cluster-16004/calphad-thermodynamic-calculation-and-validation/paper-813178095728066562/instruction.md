# CALPHAD Thermodynamic Calculation of Ni-In System

## Problem background
The binary Ni-In system is relevant for electronic contact materials and lead-free solders. A consistent thermodynamic description of all phases is essential for multicomponent database development. The present task focuses on implementing a complete CALPHAD thermodynamic model of the Ni-In system at 1 bar, from room temperature to liquidus temperatures, using Gibbs energy models for five solution phases and five stoichiometric compounds. The goal is to compute the phase diagram and key thermochemical properties from the provided optimized parameters.

## Approach
The CALPHAD method models the Gibbs energy of each phase as a function of temperature and composition. The liquid and fcc solid solution phases are described with a substitutional model and Redlich-Kister excess terms. The ζ-Ni₂In and ζ′-Ni₁₃In₉ phases employ a three-sublattice model with the compound energy formalism, capturing non-stoichiometry via vacancies and anti-site atoms. The δ-NiIn phase is modelled with a two-sublattice triple-defect approach. Five stoichiometric line compounds (Ni₃In, Ni₂In, NiIn, Ni₂In₃, Ni₃In₇) are treated with temperature-dependent Gibbs energies. All pure-element references are taken from the SGTE unary database, and the optimized model parameters are to be determined by fitting the Gibbs energy models to the experimental data provided below.

Using PyCalphad, build a thermodynamic database that includes these models. Compute the full T–x phase diagram at 1 bar, extract all invariant equilibria (reaction types, temperatures, and phase compositions in at% In). For the four two-phase regions ζ/ζ′, ζ′/NiIn, NiIn/Ni₂In₃, and Ni₂In₃/liquid, calculate the equilibrium In partial pressure at 1000 K. Finally, determine the congruent melting temperatures and enthalpies of fusion for ζ-Ni₂In and δ-NiIn from the Gibbs energy difference between the solid phase and the liquid. Output the results as specified in the workflow steps.

## Reproduction target
Produce three CSV files in `/app/outputs`:

- `step_02_invariant_equilibria.csv` – a table of all invariant reactions in the Ni-In system, each with the reaction description, temperature in °C, and In compositions (at%) of the three participating phases. This provides a complete summary of the phase diagram topology.
- `step_03_in_partial_pressures.csv` – the decimal logarithm of the In partial pressure (bar) at 1000 K in each of the four two-phase regions: ζ/ζ′, ζ′/NiIn, NiIn/Ni₂In₃, Ni₂In₃/liquid.
- `step_04_enthalpies_melting.csv` – for ζ-Ni₂In and δ-NiIn, report the melting temperature (°C), the mole fraction of In, and the enthalpy of melting in J mol⁻¹.

These quantities are to be computed directly from the thermodynamic description; no experimental data fitting is required.

## Assets

- PyCalphad: pycalphad

## Experimental data for optimization

### Invariant equilibria experimental data

The following table provides the experimental invariant equilibria data to be used for fitting the model parameters. Each row lists the invariant reaction, the measured temperature (°C), and the compositions (at% In) of the two or three participating phases.

| reaction | T_C | composition_phase1 | composition_phase2 | composition_phase3 |
|----------|-----|--------------------|--------------------|--------------------|
| fcc-(Ni)/ liquid/ζ | 908 | 9.5 | 25.0 | 31.2 |
| fcc-(Ni)/ Ni₃In/ζ | 845 | 7.0 | 25.0 | 31.2 |
| Ni₃In/ Ni₂In/ζ | 665 | 25.0 | 32.5 | 33.5 |
| Ni₂In/ ζ/ζ' | 470 | 32.5 | 34.0 | 39.0 |
| ζ/liquid/ δ | 908 | 42.0 | 48.5 | 49.5 |
| ζ/ζ'/δ | 853 | 41.0 | 42.0 | 52.7 |
| ζ'/NiIn/ δ | 845 | 42.0 | 50.5 | 53.3 |
| NiIn/δ/ Ni₂In₃ | 779 | 50.0 | 55.4 | 60.5 |
| δ/Ni₂In₃/ liquid | 865 | 58.8 | 60.0 | 70.0 |
| Ni₂In₃/ Ni₃In₇/ liquid | 404 | 60.0 | 70.0 | 95.0 |
| Ni₃In₇/ liquid/ In(s) | 156 | 70.0 | 100.0 | 100.0 |
| ζ/liquid | 950 | 36.0 | 36.0 | – |
| δ/liquid | 930 | 55.0 | 55.0 | – |
| Ni(s)/ liquid | 1455 | 0.0 | 0.0 | – |
| In(s)/ liquid | 157 | 100.0 | 100.0 | – |

### In partial pressure experimental data at 1000 K

| two_phase_region | log_p_In |
|------------------|----------|
| ζ/ζ' | -7.787 |
| ζ'/NiIn | -7.759 |
| NiIn/Ni₂In₃ | -7.484 |
| Ni₂In₃/liquid | -7.082 |

## Workflow steps

### Step 1: Optimize thermodynamic model parameters
- Role: process
- Action: Using PyCalphad, construct the Gibbs energy models for all phases (fcc, liquid, ζ, ζ', δ, Ni₃In, Ni₂In, NiIn, Ni₂In₃, Ni₃In₇) as described in the Approach. Perform a simultaneous least-squares optimization of the model parameters against the provided experimental invariant equilibria and In partial pressure data. This yields the set of optimized thermodynamic parameters that define the working database for the subsequent calculations.
- Evidence: none

### Step 2: Compute invariant equilibria
- Role: scored (load-bearing)
- Action: Compute the full T-x phase diagram of the Ni-In system at 1 bar and extract the list of invariant reactions: reaction type, temperature (°C), and compositions (at% In) of the participating phases.
- Output file: `/app/outputs/step_02_invariant_equilibria.csv`
- Format: csv
- Contract: Columns: reaction (string), T_C (float), composition_phase1 (float, at% In), composition_phase2 (float, at% In), composition_phase3 (float, at% In). Each row corresponds to one invariant reaction.
- Scoring: scored by hidden verifier

### Step 3: Compute In partial pressures
- Role: scored
- Action: For the four two-phase regions (ζ/ζ', ζ'/NiIn, NiIn/Ni₂In₃, Ni₂In₃/liquid), calculate the equilibrium partial pressure of In at 1000 K.
- Output file: `/app/outputs/step_03_in_partial_pressures.csv`
- Format: csv
- Contract: Columns: two_phase_region (string), log_p_In (float). Rows: ζ/ζ', ζ'/NiIn, NiIn/Ni₂In₃, Ni₂In₃/liquid.
- Scoring: scored by hidden verifier

### Step 4: Compute enthalpies of melting
- Role: scored
- Action: Determine the congruent melting points and enthalpies of fusion for the ζ-Ni₂In and δ-NiIn phases.
- Output file: `/app/outputs/step_04_enthalpies_melting.csv`
- Format: csv
- Contract: Columns: phase (string), melting_T_C (float), composition (float, atomic fraction In), enthalpy_melting (float, J/mol). Rows for ζ-Ni₂In and δ-NiIn.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_invariant_equilibria.csv`
- `/app/outputs/step_03_in_partial_pressures.csv`
- `/app/outputs/step_04_enthalpies_melting.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_invariant_equilibria.csv
- path: `/app/outputs/step_02_invariant_equilibria.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Invariant equilibria temperatures and phase compositions calculated from the Ni-In thermodynamic description.
- schema:
  - `type`: table
  - `required_columns`: `reaction`, `T_C`, `composition_phase1`, `composition_phase2`, `composition_phase3`
  - `units`:
    - `T_C`: °C
    - `composition_phase1`: at% In
    - `composition_phase2`: at% In
    - `composition_phase3`: at% In

### step_03_in_partial_pressures.csv
- path: `/app/outputs/step_03_in_partial_pressures.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Indium partial pressures (log10 scale) in four two-phase regions at 1000 K.
- schema:
  - `type`: table
  - `required_columns`: `two_phase_region`, `log_p_In`
  - `units`:
    - `log_p_In`: log10(p/bar)

### step_04_enthalpies_melting.csv
- path: `/app/outputs/step_04_enthalpies_melting.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Enthalpies of melting and congruent melting points for ζ-Ni₂In and δ-NiIn.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `melting_T_C`, `composition`, `enthalpy_melting`
  - `units`:
    - `melting_T_C`: °C
    - `composition`: mole fraction In
    - `enthalpy_melting`: J/mol

Notes: All values are computed from the provided Gibbs energy parameters using PyCalphad equilibrium calculations. The checker compares each scalar to the paper-reported reference values within hidden tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_invariant_equilibria.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction",
          "T_C",
          "composition_phase1",
          "composition_phase2",
          "composition_phase3"
        ],
        "units": {
          "T_C": "°C",
          "composition_phase1": "at% In",
          "composition_phase2": "at% In",
          "composition_phase3": "at% In"
        }
      },
      "description": "Invariant equilibria temperatures and phase compositions calculated from the Ni-In thermodynamic description."
    },
    {
      "file": "step_03_in_partial_pressures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "two_phase_region",
          "log_p_In"
        ],
        "units": {
          "log_p_In": "log10(p/bar)"
        }
      },
      "description": "Indium partial pressures (log10 scale) in four two-phase regions at 1000 K."
    },
    {
      "file": "step_04_enthalpies_melting.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "melting_T_C",
          "composition",
          "enthalpy_melting"
        ],
        "units": {
          "melting_T_C": "°C",
          "composition": "mole fraction In",
          "enthalpy_melting": "J/mol"
        }
      },
      "description": "Enthalpies of melting and congruent melting points for ζ-Ni₂In and δ-NiIn."
    }
  ],
  "notes": "All values are computed from the provided Gibbs energy parameters using PyCalphad equilibrium calculations. The checker compares each scalar to the paper-reported reference values within hidden tolerances."
}
```

## How you are scored
A hidden verifier will compare each scalar in your CSV files (temperatures, compositions, log₁₀ pressures, enthalpies) to a set of reference values using appropriate tolerances. Each scored stage contributes to a total reward between 0 and 1. A correct execution of the workflow, faithfully implementing the provided thermodynamic models, is required to obtain values that fall within the allowed tolerances and earn full credit.
