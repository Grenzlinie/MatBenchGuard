# CALPHAD Modeling of Re-Y and Ni-Re-Y Phase Equilibria Using First-Principles Calculations

## Problem background
Ni-base superalloys for high-temperature aerospace applications require accurate thermodynamic descriptions of multi-component systems. This task addresses the Re-Y binary and Ni-Re-Y ternary systems, where experimental data are limited. By coupling first-principles density-functional theory (DFT) calculations with the CALculation of PHAse Diagrams (CALPHAD) method, thermodynamic models for these systems can be developed. The goal is to produce a consistent set of thermodynamic database files (TDB) that describe the Gibbs energies of all relevant phases, enabling reliable calculation of phase equilibria and extrapolation to higher-order alloys.

## Approach
The thermodynamic modeling follows the CALPHAD methodology: each phase (liquid, hcp, bcc, fcc, intermetallic) is described by a Gibbs energy expression with temperature- and composition-dependent parameters. Missing thermochemical data are supplied by first-principles calculations. DFT total energy calculations on pure elements, the Re₂Y compound, and special quasi-random structures (SQS) for the solid solutions provide 0 K energies and enthalpies of mixing. Finite-temperature properties of the intermetallic Re₂Y are obtained from phonon calculations under the quasi-harmonic approximation. These DFT-derived quantities, together with the provided experimental phase boundary data (Re-Y and Ni-Re), are used to fit the CALPHAD model parameters via least-squares optimization. For the Ni-Re binary, the same strategy is applied after updating the pure-element Gibbs energy, including a DFT SQS calculation for the bcc phase. Finally, a ternary Ni-Re-Y database is assembled by combining the Re-Y and Ni-Re assessments with a pre-existing Ni-Y binary database, assuming no ternary compounds or ternary interaction parameters. All DFT work is done with the open-source code Quantum ESPRESSO, phonon calculations with phonopy, and CALPHAD modeling with pycalphad.

## Reproduction target
Produce three TDB files: `Re_Y.tdb`, `Ni_Re.tdb`, and `Ni_Re_Y.tdb`. When used with pycalphad, these databases must yield phase diagrams that agree with the bundled experimental data (`Re_Y_exp_data.csv`, `Ni_Re_exp_data.csv`). Concretely, the Re-Y system must reproduce the key invariant reactions (peritectic, eutectic) and phase boundaries; the Ni-Re system must match the liquidus/solidus data; and the Ni-Re-Y isothermal section at 1000 K must exhibit a three-phase region involving fcc, hcp, and the Ni₁₇Y₂ compound as observed in experiments. The liquidus projection should also be computable from the ternary database. The verifier will recalculate these phase equilibria from your TDB files and compare the predicted invariant points and phase boundaries to reference values.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- phonopy: phonopy
- pycalphad: pycalphad
- Re-Y experimental phase boundary data
- Ni-Re experimental phase boundary data
- SGTE unary database v4 (pure elements)
- Ni-Y thermodynamic database

## Workflow steps

### Step 1: DFT static total energy calculations
- Role: process
- Action: Perform DFT static calculations using Quantum ESPRESSO for hcp Re, hcp Y, Re2Y, and SQS supercells for hcp and bcc Re-Y solutions. Obtain relaxed lattice parameters and total energies.
- Evidence: `/app/outputs/dft_energies.json`

### Step 2: Phonon supercell calculations
- Role: process
- Action: Using optimized structures from step_dft, run phonon calculations with phonopy under the quasi-harmonic approximation for hcp Re, hcp Y, and Re2Y. Produce heat capacity, entropy, and enthalpy as functions of temperature.
- Evidence: `/app/outputs/phonon_results.json`

### Step 3: Re-Y enthalpy of mixing calculation
- Role: process
- Action: Compute the enthalpy of mixing for hcp and bcc Re-Y solutions from the total energies of SQS supercells and pure elements (from step_dft) at compositions x_Y=0.25, 0.50, 0.75.
- Evidence: `/app/outputs/mix_enthalpy_ReY.json`

### Step 4: CALPHAD parameter assessment for Re-Y
- Role: scored (load-bearing)
- Action: Using the DFT-derived data (phonon properties of Re2Y, mixing enthalpies of hcp/bcc) and the experimental invariant points from Re_Y_exp_data.csv, fit the Gibbs energy parameters (liquid, hcp, bcc, Re2Y) for the Re-Y system using pycalphad. Output the thermodynamic database file Re_Y.tdb.
- Output file: `/app/outputs/Re_Y.tdb`
- Format: txt
- Contract: TDB text file containing ELEMENTS, SPECIES, PHASES, and PARAMETER sections for the Re-Y system.
- Scoring: scored by hidden verifier

### Step 5: SQS enthalpy of mixing for Ni-Re bcc
- Role: process
- Action: Perform DFT SQS calculation for bcc Ni50Re50 to obtain the enthalpy of mixing. This provides a physically meaningful value for the bcc interaction parameter in Ni-Re.
- Evidence: `/app/outputs/mix_enthalpy_NiRe.json`

### Step 6: Remodeling of Ni-Re binary system
- Role: scored
- Action: Using the updated pure Re Gibbs energy from pure_elements.tdb, the mixing enthalpy of bcc Ni-Re from step_nire_sqs, the liquid interaction estimate from de Boer, and experimental data in Ni_Re_exp_data.csv, fit the Gibbs energy interaction parameters for liquid, fcc, hcp, and bcc phases in the Ni-Re system using pycalphad. Output the database file Ni_Re.tdb.
- Output file: `/app/outputs/Ni_Re.tdb`
- Format: txt
- Contract: TDB text file containing ELEMENTS, SPECIES, PHASES, and PARAMETER sections for the Ni-Re system.
- Scoring: scored by hidden verifier

### Step 7: Assembly of Ni-Re-Y ternary database
- Role: scored
- Action: Combine the Re_Y.tdb, Ni_Re.tdb, and the provided Ni_Y.tdb into a single Ni-Re-Y ternary thermodynamic database. Assume no ternary compounds and no ternary interaction parameters. Output the file Ni_Re_Y.tdb.
- Output file: `/app/outputs/Ni_Re_Y.tdb`
- Format: txt
- Contract: TDB text file containing merged element, species, phase, and parameter sections from the three binary databases.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/Re_Y.tdb`
- `/app/outputs/Ni_Re.tdb`
- `/app/outputs/Ni_Re_Y.tdb`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### Re_Y.tdb
- path: `/app/outputs/Re_Y.tdb`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Assessed thermodynamic database for the Re-Y binary system.
- schema:
  - `type`: text
  - `description`: Thermo-Calc TDB format text file containing thermodynamic parameters for the Re-Y system (liquid, hcp, bcc, Re2Y). The checker will parse this TDB and recompute the phase diagram to compare invariant points (eutectic temperature/composition, peritectic temperature) to the paper-reported hidden gold.

### Ni_Re.tdb
- path: `/app/outputs/Ni_Re.tdb`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Remodeled thermodynamic database for the Ni-Re binary system.
- schema:
  - `type`: text
  - `description`: Thermo-Calc TDB format text file containing thermodynamic parameters for the Ni-Re system (liquid, hcp, fcc, bcc). The checker will parse this TDB and recompute the phase diagram to compare liquidus/solidus against hidden reference data.

### Ni_Re_Y.tdb
- path: `/app/outputs/Ni_Re_Y.tdb`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Ternary thermodynamic database for the Ni-Re-Y system.
- schema:
  - `type`: text
  - `description`: Thermo-Calc TDB format text file combining Re-Y, Ni-Re, and Ni-Y binaries for ternary calculations. The checker will parse this TDB and compute the isothermal section at 1000 K and liquidus projection, verifying the fcc+hcp+Ni17Y2 three-phase region and invariant reactions against hidden reference data.

Notes: Scored TDB files are verified by recomputing phase equilibria with pycalphad and comparing invariant reaction temperatures/compositions and phase boundaries to the paper's reported experimental values. Tolerances are set to account for toolchain differences (DFT code, CALPHAD implementation) and are not disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "Re_Y.tdb",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Thermo-Calc TDB format text file containing thermodynamic parameters for the Re-Y system (liquid, hcp, bcc, Re2Y). The checker will parse this TDB and recompute the phase diagram to compare invariant points (eutectic temperature/composition, peritectic temperature) to the paper-reported hidden gold."
      },
      "description": "Assessed thermodynamic database for the Re-Y binary system."
    },
    {
      "file": "Ni_Re.tdb",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Thermo-Calc TDB format text file containing thermodynamic parameters for the Ni-Re system (liquid, hcp, fcc, bcc). The checker will parse this TDB and recompute the phase diagram to compare liquidus/solidus against hidden reference data."
      },
      "description": "Remodeled thermodynamic database for the Ni-Re binary system."
    },
    {
      "file": "Ni_Re_Y.tdb",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Thermo-Calc TDB format text file combining Re-Y, Ni-Re, and Ni-Y binaries for ternary calculations. The checker will parse this TDB and compute the isothermal section at 1000 K and liquidus projection, verifying the fcc+hcp+Ni17Y2 three-phase region and invariant reactions against hidden reference data."
      },
      "description": "Ternary thermodynamic database for the Ni-Re-Y system."
    }
  ],
  "notes": "Scored TDB files are verified by recomputing phase equilibria with pycalphad and comparing invariant reaction temperatures/compositions and phase boundaries to the paper's reported experimental values. Tolerances are set to account for toolchain differences (DFT code, CALPHAD implementation) and are not disclosed to the agent."
}
```

## How you are scored
A hidden verifier independently evaluates each of your three TDB files. For each database, the verifier uses pycalphad to compute the equilibrium phase diagram under the conditions described in the workflow. It extracts relevant quantities (invariant reaction temperatures, liquid compositions, phase field boundaries) and compares them to a set of reference values derived from the experimental literature. Each system (Re-Y, Ni-Re, Ni-Re-Y) is scored separately, and the final reward is a weighted combination. To earn credit you must submit valid, self-consistent TDB files that compute correctly under pycalphad; simply reporting numbers without producing the databases is not sufficient.
