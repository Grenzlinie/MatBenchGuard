# CALPHAD Thermodynamic Modeling of Co–Cr Sigma Phase with Ab Initio Stability Inputs

## Problem background
The CALPHAD method predicts phase diagrams by minimizing the total Gibbs energy of a system. For the sigma phase in the Co–Cr system, the pure-element reference energies cannot be measured experimentally because the sigma phase is unstable for pure Co and Cr. First-principles density-functional theory (DFT) can compute the total-energy differences between the sigma phase and the standard reference (SER) structures for pure Co and Cr, providing physically grounded lattice stabilities. These ab initio values can be used to anchor a CALPHAD model, aiming to improve the agreement of the calculated phase diagram with experimental data, particularly in the Co-rich region where sigma, paramagnetic hcp, and ferromagnetic hcp phases coexist.

## Approach
This task implements a two-sublattice CALPHAD model for the sigma phase. The pure-element Gibbs energy of the sigma phase is fixed by ab initio total-energy differences (sigma minus SER) for Co and Cr. The excess Gibbs energy parameters of the two-sublattice model — describing the mixing behavior — are fitted to publicly available experimental Co–Cr phase-equilibrium data. The thermodynamic descriptions for all other phases (bcc, fcc, hcp, liquid) are taken from a published assessment (Kusoffski and Jansson, 1997) and the SGTE pure-element database. For comparison, the previously published three-sublattice sigma model is also implemented. The full Co–Cr phase diagram is computed for both models, along with the composition dependences of the molar Gibbs energy and enthalpy at 1200 K. The workflow involves DFT total-energy calculations, parameter fitting, and equilibrium calculations.

## Reproduction target
Compute the total-energy differences between the sigma phase and the SER structures for pure Co and Cr using an open-source DFT code. Fit the two-sublattice sigma-phase parameters to experimental Co–Cr phase equilibrium data. Using the fitted model, produce the phase diagram boundaries for both the new two-sublattice model and the old three-sublattice model over the composition range 0–100% Cr and temperature range 300–2000 K. Additionally, compute the Gibbs energy and enthalpy composition dependences at 1200 K for all stable phases (bcc, fcc, hcp, liquid, sigma) under both models. The target is a set of quantitative outputs that can be compared to independent experimental data and to the performance of the previous model.

## Assets

- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org/
- pycalphad (computational thermodynamics library): pycalphad
- Co–Cr thermodynamic assessment (Kusoffski and Jansson, 1997): 10.1016/S0364-5916(97)00029-2
- SGTE pure element database (Dinsdale 1991): pycalphad (bundled)
- Co–Cr experimental phase equilibrium data (literature compilation)

## Workflow steps

### Step 1: Calculate ab initio total-energy differences for pure Co and Cr
- Role: scored
- Action: Perform DFT calculations for pure Co and Cr in sigma and SER structures, obtain equilibrium total energies per atom, and output the total-energy differences (sigma – SER) as a JSON object.
- Output file: `/app/outputs/total_energy_differences.json`
- Format: json
- Contract: {"Co": float, "Cr": float}
- Scoring: scored by hidden verifier

### Step 2: Fit two-sublattice sigma phase parameters using ab initio stabilities
- Role: process
- Action: Using the ab initio energy differences as anchored reference energies, fit the excess Gibbs energy parameters (S^σ for Co and Cr, L^0, L^1, L^2) of the two-sublattice sigma model to published experimental Co–Cr phase equilibrium data. Output the fitted parameters as evidence.
- Evidence: `/app/outputs/sigma_parameters.json`

### Step 3: Calculate phase diagram using the new two-sublattice sigma model
- Role: scored (load-bearing)
- Action: Assemble the full Co–Cr thermodynamic description using the fitted two-sublattice sigma parameters together with published Gibbs energy functions for bcc, fcc, hcp, and liquid phases, then compute the phase boundaries over 0–100% Cr and 300–2000 K.
- Output file: `/app/outputs/new_model_phase_diagram.csv`
- Format: csv
- Contract: required_columns: Temperature_K, Mole_fraction_Cr, Phase
- Scoring: scored by hidden verifier

### Step 4: Calculate phase diagram using the old three-sublattice sigma model
- Role: scored
- Action: Using the published three-sublattice sigma model parameters, compute the phase diagram with the same base-phase descriptions as in step 3.
- Output file: `/app/outputs/old_model_phase_diagram.csv`
- Format: csv
- Contract: required_columns: Temperature_K, Mole_fraction_Cr, Phase
- Scoring: scored by hidden verifier

### Step 5: Calculate Gibbs energy and enthalpy composition dependences at 1200 K
- Role: scored
- Action: Compute molar Gibbs energy and enthalpy for each stable phase (bcc, fcc, hcp, liquid, sigma) as a function of composition across the full range at a fixed temperature of 1200 K, for both the new two-sublattice and the old three-sublattice sigma models.
- Output file: `/app/outputs/gibbs_enthalpy_1200K.csv`
- Format: csv
- Contract: required_columns: Model, Phase, Mole_fraction_Cr, Gibbs_energy_J_per_mol, Enthalpy_J_per_mol
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energy_differences.json`
- `/app/outputs/new_model_phase_diagram.csv`
- `/app/outputs/old_model_phase_diagram.csv`
- `/app/outputs/gibbs_enthalpy_1200K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energy_differences.json
- path: `/app/outputs/total_energy_differences.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ab initio total energy differences (sigma – SER) for pure Co and Cr.
- schema:
  - `type`: object
  - `required`:
    - `Co`: number
    - `Cr`: number
  - `units`:
    - `Co`: Ry/atom
    - `Cr`: Ry/atom

### new_model_phase_diagram.csv
- path: `/app/outputs/new_model_phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Co–Cr phase diagram boundaries computed with the new two-sublattice sigma model.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Mole_fraction_Cr`, `Phase`
  - `units`:
    - `Temperature_K`: K
    - `Mole_fraction_Cr`: mole fraction

### old_model_phase_diagram.csv
- path: `/app/outputs/old_model_phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Co–Cr phase diagram boundaries computed with the old three-sublattice sigma model for comparison.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Mole_fraction_Cr`, `Phase`
  - `units`:
    - `Temperature_K`: K
    - `Mole_fraction_Cr`: mole fraction

### gibbs_enthalpy_1200K.csv
- path: `/app/outputs/gibbs_enthalpy_1200K.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Gibbs energy and enthalpy composition dependences at 1200 K for each stable phase, for both old and new sigma models. Used to verify full composition coverage and smoothness.
- schema:
  - `type`: table
  - `required_columns`: `Model`, `Phase`, `Mole_fraction_Cr`, `Gibbs_energy_J_per_mol`, `Enthalpy_J_per_mol`
  - `units`:
    - `Gibbs_energy_J_per_mol`: J/mol
    - `Enthalpy_J_per_mol`: J/mol

Notes: The checker compares the DFT energy differences to hidden reference values with tolerance, evaluates phase diagram accuracy by average absolute temperature deviation against digitised gold boundaries, and verifies structural properties of the thermodynamic curves (full range coverage, absence of unphysical discontinuities).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energy_differences.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Co": "number",
          "Cr": "number"
        },
        "units": {
          "Co": "Ry/atom",
          "Cr": "Ry/atom"
        }
      },
      "description": "Ab initio total energy differences (sigma – SER) for pure Co and Cr."
    },
    {
      "file": "new_model_phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Mole_fraction_Cr",
          "Phase"
        ],
        "units": {
          "Temperature_K": "K",
          "Mole_fraction_Cr": "mole fraction"
        }
      },
      "description": "Co–Cr phase diagram boundaries computed with the new two-sublattice sigma model."
    },
    {
      "file": "old_model_phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Mole_fraction_Cr",
          "Phase"
        ],
        "units": {
          "Temperature_K": "K",
          "Mole_fraction_Cr": "mole fraction"
        }
      },
      "description": "Co–Cr phase diagram boundaries computed with the old three-sublattice sigma model for comparison."
    },
    {
      "file": "gibbs_enthalpy_1200K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Model",
          "Phase",
          "Mole_fraction_Cr",
          "Gibbs_energy_J_per_mol",
          "Enthalpy_J_per_mol"
        ],
        "units": {
          "Gibbs_energy_J_per_mol": "J/mol",
          "Enthalpy_J_per_mol": "J/mol"
        }
      },
      "description": "Gibbs energy and enthalpy composition dependences at 1200 K for each stable phase, for both old and new sigma models. Used to verify full composition coverage and smoothness."
    }
  ],
  "notes": "The checker compares the DFT energy differences to hidden reference values with tolerance, evaluates phase diagram accuracy by average absolute temperature deviation against digitised gold boundaries, and verifies structural properties of the thermodynamic curves (full range coverage, absence of unphysical discontinuities)."
}
```

## How you are scored
A hidden automatic verifier independently scores each artifact from the workflow steps. Your submitted DFT total-energy differences are compared to reference values; the accuracy of your phase diagram boundaries is evaluated against digitized experimental data; and the thermodynamic curves are checked for completeness over the full composition range and for physical smoothness. The final reward is a weighted combination of the individual scores: DFT energy differences contribute about 30%, phase diagram accuracy about 50%, and thermodynamic curves about 20%. To earn credit, you must execute the entire workflow and produce the required output files; merely reporting known literature numbers is not sufficient.
