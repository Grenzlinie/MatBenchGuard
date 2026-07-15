# Crystal-phase hydrogen bonding analysis of beta-HMX via LDA-DFT

## Problem background
Beta-HMX (cyclotetramethylene-tetranitramine) is an energetic molecular crystal widely used in explosives. Understanding its hydrogen bonding network is critical for sensitivity. In this task you investigate the structural and electronic properties of the β-phase crystal using density-functional theory (DFT) with the local density approximation (LDA). The goal is to apply periodic DFT to the experimental crystal structure (monoclinic P21/c, 56 atoms per unit cell) and compute quantities that reveal intra- and inter-molecular C–H···O hydrogen bonds.

## Approach
Use an open‑source plane‑wave pseudopotential DFT code (Quantum ESPRESSO) with the LDA functional (CA‑PZ) and ultrasoft pseudopotentials. Start from the experimental crystal geometry (CCDC refcode OCHTET). Perform a full geometry relaxation allowing cell shape/volume and ionic positions to change until forces and stress are converged. On the relaxed structure, first extract key bond lengths and bond angles. Then run a single‑point calculation to obtain Mulliken bond populations and bond distances for specific covalent and hydrogen‑bonded pairs. From the same calculation compute the total density of states (TDOS) and atomic‑orbit‑projected density of states (PDOS) for O‑2p and H‑1s states, which will be examined for orbital hybridization as evidence of hydrogen bonding. All calculations use the same functional and cutoff; no gas‑phase calculation is needed.

## Reproduction target
Produce the relaxed crystal structure (CIF). From it, compute a CSV of selected bond lengths and bond angles that correspond to the crystal‑phase column of the reported molecular geometry. Compute another CSV of Mulliken bond populations and bond distances for the hydrogen bonds and key covalent bonds listed in the workflow steps. Finally, compute a CSV of TDOS and PDOS(O-2p, H-1s) covering the energy range from –20 to +5 eV relative to the Fermi level. Your results should be consistent with a properly executed LDA‑CA‑PZ calculation on this system; the hidden scorer will evaluate each artifact independently.

## Assets

- beta-HMX experimental crystal structure (CCDC OCHTET): CCDC refcode OCHTET
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Atomic Simulation Environment: ase
- Python Materials Genomics: pymatgen

## Workflow steps

### Step 1: Geometry relaxation of beta-HMX crystal
- Role: process
- Action: Perform full DFT geometry relaxation of beta-HMX starting from experimental crystal structure (space group P21/c) using LDA (CA-PZ or equivalent), plane-wave cutoff 400 eV, 2x2x2 k-point grid, ultrasoft pseudopotentials. Allow cell shape/volume and ionic positions to relax. Converge forces below 0.05 eV/Å and stress below 0.1 GPa. Save the relaxed structure.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 2: Extract geometric parameters
- Role: scored (load-bearing)
- Action: From relaxed_structure.cif, compute bond lengths and bond angles for the following geometric parameters. Output a CSV with columns: bond_or_angle, value, unit. The required entries are: bond lengths: N8-C2, N8-C1, N15-C2, N15-C17, N8-N7, N15-N18, N7-O12, N7-O11, N18-O25, N18-O24, C2-H6, C2-H5, C17-H23, C17-H22, H5...O12; bond angles: O12-N7-O11, N8-N7-O12, N8-N7-O11, N7-N8-C1, N7-N8-C2, C2-N8-C1, N8-C2-N15, N8-C2-H6, N8-C2-H5, N15-C2-H6, N15-C2-H5, H6-C2-H5, O25-N18-O24, N15-N18-O25, N15-N18-O24, N18-N15-C2, N18-N15-C17, C2-N15-C17, N21-C17-N15, N15-C17-H22, N15-C17-H23, N21-C17-H22, N21-C17-H23, H23-C17-H22. All values must be in Å or degrees as appropriate.
- Output file: `/app/outputs/bulk_geometric_params.csv`
- Format: csv
- Contract: CSV with columns: bond_or_angle (string), value (float), unit (string: 'Å' or '°')
- Scoring: scored by hidden verifier

### Step 3: Compute Mulliken bond populations
- Role: scored (load-bearing)
- Action: Perform a single-point DFT calculation on relaxed_structure.cif using the same settings (LDA, 400 eV, 2x2x2). Compute Mulliken bond populations and bond lengths for the following bonds: N8-N7, N7-O12, N7-O11, N8-C2, C2-H5, C2-H6, C2-N15, N15-N18, N18-O24, N18-O25, N15-C17, C17-H23, C17-H22, C17-N21, H5...O12, H19...O24. Output a CSV with columns: bond, population, length.
- Output file: `/app/outputs/mulliken_bond_populations.csv`
- Format: csv
- Contract: CSV with columns: bond (string), population (float), length (float, Å)
- Scoring: scored by hidden verifier

### Step 4: Compute total and projected density of states
- Role: scored (load-bearing)
- Action: From the same single-point calculation, compute total DOS and projected DOS for O-2p and H-1s states. Output a CSV with columns: energy, tdos, pdos_O_2p, pdos_H_1s, covering an energy range of -20 to 5 eV relative to the Fermi level.
- Output file: `/app/outputs/pdos_data.csv`
- Format: csv
- Contract: CSV with columns: energy (eV, relative to Fermi level), tdos (states/eV), pdos_O_2p (states/eV), pdos_H_1s (states/eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_geometric_params.csv`
- `/app/outputs/mulliken_bond_populations.csv`
- `/app/outputs/pdos_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_geometric_params.csv
- path: `/app/outputs/bulk_geometric_params.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed bond lengths and bond angles of the relaxed crystal; checker compares each entry to hidden reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `bond_or_angle`, `value`, `unit`
  - `units`:
    - `value`: unit is given by the 'unit' column: 'Å' for lengths, '°' for angles

### mulliken_bond_populations.csv
- path: `/app/outputs/mulliken_bond_populations.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mulliken bond populations and bond distances; checker compares each bond's population and length to hidden reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `bond`, `population`, `length`
  - `units`:
    - `population`: dimensionless
    - `length`: Å

### pdos_data.csv
- path: `/app/outputs/pdos_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total and projected density of states; checker verifies that both pdos_O_2p and pdos_H_1s exhibit a local maximum in the energy range [-7, -6] eV relative to the Fermi level, confirming O-2p/H-1s hybridization.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `tdos`, `pdos_O_2p`, `pdos_H_1s`
  - `units`:
    - `energy`: eV
    - `tdos`: states/eV
    - `pdos_O_2p`: states/eV
    - `pdos_H_1s`: states/eV

Notes: The gas-phase B3LYP/6-31G(d,p) calculation from the paper is omitted because the main claim rests on crystal-phase hydrogen bonding; only the crystal DFT results are reproduced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_geometric_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "bond_or_angle",
          "value",
          "unit"
        ],
        "units": {
          "value": "unit is given by the 'unit' column: 'Å' for lengths, '°' for angles"
        }
      },
      "description": "Computed bond lengths and bond angles of the relaxed crystal; checker compares each entry to hidden reference values within tolerance."
    },
    {
      "file": "mulliken_bond_populations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "bond",
          "population",
          "length"
        ],
        "units": {
          "population": "dimensionless",
          "length": "Å"
        }
      },
      "description": "Mulliken bond populations and bond distances; checker compares each bond's population and length to hidden reference values within tolerance."
    },
    {
      "file": "pdos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "tdos",
          "pdos_O_2p",
          "pdos_H_1s"
        ],
        "units": {
          "energy": "eV",
          "tdos": "states/eV",
          "pdos_O_2p": "states/eV",
          "pdos_H_1s": "states/eV"
        }
      },
      "description": "Total and projected density of states; checker verifies that both pdos_O_2p and pdos_H_1s exhibit a local maximum in the energy range [-7, -6] eV relative to the Fermi level, confirming O-2p/H-1s hybridization."
    }
  ],
  "notes": "The gas-phase B3LYP/6-31G(d,p) calculation from the paper is omitted because the main claim rests on crystal-phase hydrogen bonding; only the crystal DFT results are reproduced."
}
```

## How you are scored
A hidden verifier scores each of the three output CSV files independently against hidden references or structural criteria. The geometric parameters are compared to the expected bond lengths and angles (within tolerances). Mulliken bond populations and lengths are compared to reference values for the specified bonds. The PDOS file is checked for the existence of a simultaneous local maximum in the O‑2p and H‑1s channels in a designated energy window, confirming orbital hybridization. The three scores are combined into a final reward with weights reflecting their importance: geometry (majority weight), bond populations (moderate weight), and PDOS structural check (low weight). Reporting numbers alone is not enough; the verifier reads the submitted CSV files and applies the checks.
