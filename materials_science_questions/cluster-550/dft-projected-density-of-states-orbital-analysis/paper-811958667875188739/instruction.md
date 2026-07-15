# DFT Structural Analysis of Si(001) Doped with P and As Heterodimers

## Problem background
Single phosphorus or arsenic dopants incorporated into the Si(001) surface form Si–P and Si–As heterodimers. Two distinct buckling configurations, denoted HD1 and HD2, have been proposed for these heterodimers. Scanning tunneling microscopy (STM) measurements on n‑type Si(001) reveal a bias‑voltage‑dependent appearance for the Si–P heterodimer, suggesting that surface electron accumulation may alter the dimer structure and spin population. The relationship between charging state, geometry, and magnetic moment for the two configurations, however, is not yet established a priori. The present work aims to determine the structural parameters and magnetic moments of Si–P and Si–As heterodimers for both configurations at neutral and charged states, and to analyze how these properties evolve with surface charging.

## Approach
Use density functional theory (DFT) to model a Si(001) surface slab with a single substitutional P or As atom. Build a 4×4 periodic slab of six Si layers, terminating the bottom layer with hydrogen and leaving a vacuum region of approximately 10 Å. The heterodimer is constructed in both HD1 (buckling angle in the same direction as the two neighboring Si–Si dimers in the same row) and HD2 (buckling angle in the opposite direction). Perform spin‑polarized geometry optimization with the PW91 exchange‑correlation functional and appropriate pseudopotentials for Si, P, and As. For each dopant (P and As) and each configuration (HD1, HD2), carry out calculations for three charge states: neutral (Ne), one extra electron (Ne+1), and two extra electrons (Ne+2). For the charged systems, use a uniform background compensating charge. After each optimization, extract the buckling angle of the heterodimer, its bond length, the total energy, and the net magnetic moment. These quantities serve as the basis for comparing the behavior of the two configurations under progressive charging.

## Reproduction target
Produce a CSV file `step_01_structural_params.csv` containing the computed structural and magnetic properties for every combination of dopant, configuration, and charge state. The file must have columns: dopant (P or As), configuration (HD1 or HD2), charge_state (Ne, Ne+1, Ne+2), buckling_angle_deg (in degrees), bond_length_angstrom (in Å), total_energy_eV (in eV), and magnetic_moment_muB (in Bohr magnetons). Each row represents one completed geometry optimization. The collection of data should span all twelve cases (Si–P and Si–As, HD1 and HD2, each in the three charge states).

## Assets

- DFT code (e.g., VASP or Quantum ESPRESSO)
- Pseudopotentials for Si, P, As

## Workflow steps

### Step 1: DFT Geometry Optimizations
- Role: process
- Action: Build a Si(001) 4x4 surface slab (six Si layers, bottom H-terminated, ~10 Å vacuum) with a single substitutional P or As atom forming a Si-P or Si-As heterodimer in both HD1 and HD2 buckling configurations. Perform spin-polarized DFT geometry optimization using the PW91 functional for the neutral (Ne) and charged (Ne+1, Ne+2) states for both dopants. For charged systems, use a uniform background compensating charge. Extract buckling angle, bond length, total energy, and net magnetic moment of the heterodimer for each case.
- Evidence: `/app/outputs/dft_logs.txt`

### Step 2: Structural Parameters and Magnetic Moments
- Role: scored (load-bearing)
- Action: Collect the structural parameters and magnetic moments from the DFT calculations and write them to step_01_structural_params.csv.
- Output file: `/app/outputs/step_01_structural_params.csv`
- Format: csv
- Contract: Columns: dopant (P or As), configuration (HD1 or HD2), charge_state (Ne, Ne+1, Ne+2), buckling_angle_deg (float), bond_length_angstrom (float), total_energy_eV (float), magnetic_moment_muB (float). Each row corresponds to one geometry optimization.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structural_params.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structural_params.csv
- path: `/app/outputs/step_01_structural_params.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of heterodimer structural properties and magnetic moments for all configurations and charge states. Values are compared against hidden reference data from the paper with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `dopant`, `configuration`, `charge_state`, `buckling_angle_deg`, `bond_length_angstrom`, `total_energy_eV`, `magnetic_moment_muB`
  - `units`:
    - `buckling_angle_deg`: degrees
    - `bond_length_angstrom`: angstrom
    - `total_energy_eV`: eV
    - `magnetic_moment_muB`: Bohr magneton

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structural_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dopant",
          "configuration",
          "charge_state",
          "buckling_angle_deg",
          "bond_length_angstrom",
          "total_energy_eV",
          "magnetic_moment_muB"
        ],
        "units": {
          "buckling_angle_deg": "degrees",
          "bond_length_angstrom": "angstrom",
          "total_energy_eV": "eV",
          "magnetic_moment_muB": "Bohr magneton"
        }
      },
      "description": "Table of heterodimer structural properties and magnetic moments for all configurations and charge states. Values are compared against hidden reference data from the paper with appropriate tolerances."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently evaluate the artifacts produced by each workflow step. For the scored CSV file, the verifier compares your reported buckling angles, bond lengths, total energies, and magnetic moments to reference values obtained from the original study. It checks both numerical agreement (within an appropriate tolerance that accounts for differences in DFT implementations) and physical consistency – for example, whether the buckling angle changes progressively with added charge only for the expected configuration. The verifier also confirms that the magnetic moments adopt physically meaningful discrete values. A final reward is computed as a weighted combination of the scores across all scored artifacts. Reporting the paper’s numbers in the CSV without performing the required calculations is not sufficient to pass the checks.
