# DFT Calculation of Halopentacene Electronic Properties for Semiconductor Screening

## Problem background
Organic semiconductors are essential for flexible electronics. Pentacene exhibits high charge-carrier mobility but is poorly soluble in common organic solvents, making solution-based processing difficult. Introducing halogen substituents (F, Cl, Br) at specific positions can improve solubility while retaining high mobility. This work uses density functional theory (DFT) to compute molecular properties of pentacene and a series of halopentacenes and evaluate their potential as organic semiconductors. The main quantities of interest are dipole moments (related to solubility), HOMO-LUMO gaps, ionization potentials, electron affinities, and internal reorganization energies (which govern charge-carrier mobility).

## Approach
The computational protocol uses Kohn-Sham DFT with the B3LYP hybrid functional. For each molecule, gas-phase geometry optimizations and harmonic vibrational frequency calculations are performed at the B3LYP/6-31G(d) level for the neutral, cationic, and anionic states to obtain equilibrium geometries (Q0, Q+, Q−). Single-point energies are then computed at the B3LYP/6-311+G(d,p) level on all optimized structures to obtain accurate total energies and molecular orbital eigenvalues. From these results, the following are derived: dipole moment (from the neutral wavefunction), HOMO-LUMO gap (from orbital eigenvalues), vertical and adiabatic ionization potentials and electron affinities (from total energy differences), and reorganization energies for hole (λ+) and electron (λ−) transport, computed from four energy components as defined in the workflow steps. The set of molecules studied includes pentacene (P) and six halopentacenes: P_F, P_Cl, P_Br (one halogen at position 2), and P_2F, P_2Cl, P_2Br (two halogens at positions 2 and 9).

## Reproduction target
Perform the DFT calculations for all seven molecules and produce the two CSV output files containing the computed properties and reorganization energies. The calculated dipole moments for molecules with substituents at position 2 or 2 and 9 should be clearly non-zero, and the reorganization energies should be small (below 0.2 eV is generally considered indicative of high carrier mobility).

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/app.php/portal
- Python with numpy, pandas: numpy pandas
- RDKit: rdkit-pypi

## Workflow steps

### Step 1: Geometry optimizations
- Role: process
- Action: For each of the seven molecules (P, P_F, P_Cl, P_Br, P_2F, P_2Cl, P_2Br): build a nearly planar initial structure and perform gas-phase geometry optimization and harmonic vibrational frequency calculation at the B3LYP/6-31G(d) level for the neutral, cationic, and anionic states. Verify that all stationary points have no imaginary frequencies. Save the optimized coordinates.
- Evidence: none

### Step 2: Single-point energy calculations
- Role: process
- Action: For each optimized geometry from step_opt, compute a single-point energy at the B3LYP/6-311+G(d,p) level. Record the total energies (E0(Q0), E0(Q+), E0(Q−), E+(Q+), E+(Q0), E−(Q−), E−(Q0)) and the HOMO/LUMO orbital eigenvalues.
- Evidence: none

### Step 3: Molecular properties
- Role: scored
- Action: From the neutral optimized structures, extract the dipole moment (in Debye). From the HOMO/LUMO eigenvalues, compute the HOMO-LUMO gap (eV). Using the total energies, compute vertical and adiabatic ionization potentials (VIP, AIP) and vertical and adiabatic electron affinities (VEA, AEA) according to the standard definitions: VIP = E+(Q0) - E0(Q0), AIP = E+(Q+) - E0(Q0), VEA = E0(Q0) - E−(Q0), AEA = E0(Q0) - E−(Q−). Write all results for the seven molecules to step_01_molecular_properties.csv.
- Output file: `/app/outputs/step_01_molecular_properties.csv`
- Format: csv
- Contract: columns: molecule (str), dipole_moment_D (float), homolumo_gap_eV (float), vip_eV (float), aip_eV (float), vea_eV (float), aea_eV (float). Exactly 7 rows.
- Scoring: scored by hidden verifier

### Step 4: Reorganization energies
- Role: scored (load-bearing)
- Action: Using the total energies from step_sp, compute the four components and the reorganization energies for hole (λ+) and electron (λ−) transport: λ1 = E0(Q+) - E0(Q0), λ2 = E+(Q0) - E+(Q+), λ+ = λ1 + λ2; λ3 = E0(Q−) - E0(Q0), λ4 = E−(Q0) - E−(Q−), λ− = λ3 + λ4. Convert all values to eV. Write results for the seven molecules to step_02_reorganization_energies.csv.
- Output file: `/app/outputs/step_02_reorganization_energies.csv`
- Format: csv
- Contract: columns: molecule (str), lambda1_eV (float), lambda2_eV (float), lambda3_eV (float), lambda4_eV (float), lambda_plus_eV (float), lambda_minus_eV (float). Exactly 7 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_molecular_properties.csv`
- `/app/outputs/step_02_reorganization_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_molecular_properties.csv
- path: `/app/outputs/step_01_molecular_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed molecular properties for the 7 molecules (P, P_F, P_Cl, P_Br, P_2F, P_2Cl, P_2Br). Values are compared to hidden reference data with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `dipole_moment_D`, `homolumo_gap_eV`, `vip_eV`, `aip_eV`, `vea_eV`, `aea_eV`
  - `units`:
    - `dipole_moment_D`: Debye
    - `homolumo_gap_eV`: eV
    - `vip_eV`: eV
    - `aip_eV`: eV
    - `vea_eV`: eV
    - `aea_eV`: eV

### step_02_reorganization_energies.csv
- path: `/app/outputs/step_02_reorganization_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reorganization energy components and total λ+ and λ− for the same 7 molecules. Values are compared to hidden reference data; a threshold check ensures all λ+ and λ− are < 0.2 eV.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `lambda1_eV`, `lambda2_eV`, `lambda3_eV`, `lambda4_eV`, `lambda_plus_eV`, `lambda_minus_eV`
  - `units`:
    - `lambda1_eV`: eV
    - `lambda2_eV`: eV
    - `lambda3_eV`: eV
    - `lambda4_eV`: eV
    - `lambda_plus_eV`: eV
    - `lambda_minus_eV`: eV

Notes: The checker compares the agent's computed values to hidden reference values (from the paper's Tables 1 and 2) with generous tolerances to account for toolchain differences. Additional global threshold checks are applied: all λ+ and λ− must be < 0.2 eV, and for substituted molecules dipole moment > 0.5 D. Full credit requires passing both tolerance and threshold checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_molecular_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "dipole_moment_D",
          "homolumo_gap_eV",
          "vip_eV",
          "aip_eV",
          "vea_eV",
          "aea_eV"
        ],
        "units": {
          "dipole_moment_D": "Debye",
          "homolumo_gap_eV": "eV",
          "vip_eV": "eV",
          "aip_eV": "eV",
          "vea_eV": "eV",
          "aea_eV": "eV"
        }
      },
      "description": "Computed molecular properties for the 7 molecules (P, P_F, P_Cl, P_Br, P_2F, P_2Cl, P_2Br). Values are compared to hidden reference data with tolerances."
    },
    {
      "file": "step_02_reorganization_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "lambda1_eV",
          "lambda2_eV",
          "lambda3_eV",
          "lambda4_eV",
          "lambda_plus_eV",
          "lambda_minus_eV"
        ],
        "units": {
          "lambda1_eV": "eV",
          "lambda2_eV": "eV",
          "lambda3_eV": "eV",
          "lambda4_eV": "eV",
          "lambda_plus_eV": "eV",
          "lambda_minus_eV": "eV"
        }
      },
      "description": "Reorganization energy components and total λ+ and λ− for the same 7 molecules. Values are compared to hidden reference data; a threshold check ensures all λ+ and λ− are < 0.2 eV."
    }
  ],
  "notes": "The checker compares the agent's computed values to hidden reference values (from the paper's Tables 1 and 2) with generous tolerances to account for toolchain differences. Additional global threshold checks are applied: all λ+ and λ− must be < 0.2 eV, and for substituted molecules dipole moment > 0.5 D. Full credit requires passing both tolerance and threshold checks."
}
```

## How you are scored
Each scored output file is independently evaluated by a hidden verifier. The verifier first checks that the files exist, have the correct format, columns, and row count. It then compares your reported values against a hidden reference set and applies structural checks, such as threshold conditions on reorganization energies and dipole moments. The final reward is a weighted sum of the scores from the individual stages. The more accurately your computed values align with the expected physical trends and satisfy the known performance criteria, the higher your score. Small numerical differences due to different quantum chemistry codes are expected and are accounted for in the evaluation.
