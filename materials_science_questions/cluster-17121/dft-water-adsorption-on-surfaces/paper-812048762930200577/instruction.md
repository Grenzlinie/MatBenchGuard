# Stability of Hydroxylated Diamond (001) Surface Phases from DFT

## Problem background
The oxidation of diamond surfaces is crucial for understanding diamond growth under chemical vapour deposition (CVD) conditions. Oxygen-containing species can influence the stability and termination of diamond (001) surfaces, but the relative stability of different hydroxylated configurations at half and full monolayer (ML) oxygen coverage in the presence of hydrogen remains an open area of investigation. Density functional theory (DFT) can compute total energies and geometries of candidate surface phases, providing insight into the role of hydrogen bonding and electrostatic dipole alignment. This task asks you to determine the relative stability and key geometric parameters of several hydroxylated diamond (001) surface structures using DFT calculations.

## Approach
You will perform first-principles DFT calculations within the generalized gradient approximation (GGA) using a plane-wave pseudopotential code (e.g., Quantum ESPRESSO). You will construct periodic slab models of the diamond (001) surface with a (2x1) reconstruction, 12 carbon layers, the bottom layer fixed and passivated with hydrogen, and at least 15 Å of vacuum. Starting atomic configurations for the following phases must be built:

- Half ML oxygen coverage: (2x1):0.5H&0.5(OH) with hydroxyl groups aligned in one direction, and (2x2):0.5H&0.5(OH) with hydroxyl groups alternating along the dimer-row direction.
- Full ML oxygen coverage: (2x1):OH where all surface carbon atoms are terminated by hydroxyl groups in the same orientation, and (2x2):OH with an antiparallel arrangement of hydroxyl groups.

You will also prepare a bare (2x1) slab for energy referencing. After geometry optimization (keeping bottom layers fixed), extract total energies for the four hydroxylated configurations. Compute two energy differences: (i) E[(2x2):0.5H&0.5(OH)] minus E[(2x1):0.5H&0.5(OH)], per (1x1) unit cell; (ii) E[(2x2):OH antiparallel] minus E[(2x1):OH aligned], per (2x2) unit cell. Also measure the geometric parameters listed in the problem's requirements: C–C dimer lengths, C–O bond lengths, O–H bond lengths, hydrogen bond distances H···OH, and bond angles H–O–C and O–C–C.

## Reproduction target
Produce two scored output files:

1. `energies.json` – containing the total energies (in eV) of the four surface configurations and the two energy differences described in the approach. This file must provide the data needed to assess which phase is more stable at each coverage.

2. `geometries.csv` – a table of bond lengths and angles extracted from the relaxed structures. The required parameters and unit conventions are those stated in the problem background; you must report values for each configuration so that the structural features associated with stability can be examined.

The overall objective is to determine the relative stability ordering between the (2x2) and (2x1) variants at half ML and full ML coverage and to quantity the accompanying geometric changes.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP efficiency pseudopotential library: https://github.com/materialsvirtuallab/sssp

## Workflow steps

### Step 1: Build surface slab models
- Role: process
- Action: Construct periodic slab models for diamond (001) surface with 12 carbon layers, bottom C fixed and H-passivated, (2x1) surface reconstruction, and >15 Å vacuum. Generate initial atomic configurations for (2x1):0.5H&0.5(OH) (aligned), (2x2):0.5H&0.5(OH) (alternating rows), (2x1):OH (aligned), (2x2):OH (antiparallel), and the bare (2x1) slab for energy referencing.
- Evidence: none

### Step 2: Run DFT geometry relaxations and total energy calculations
- Role: process
- Action: For each surface slab model, perform spin-paired DFT calculations with GGA exchange-correlation using plane-wave pseudopotential code. Optimize atomic positions (except bottom two layers fixed) and compute total energies. Use a kinetic energy cutoff of 425 eV and a 2x2x1 k-point mesh.
- Evidence: none

### Step 3: Extract relative energies and energy differences
- Role: scored (load-bearing)
- Action: From the DFT output, retrieve the total energies of the (2x1):0.5H&0.5(OH), (2x2):0.5H&0.5(OH), (2x1):OH (aligned), and (2x2):OH (antiparallel) configurations. Compute the energy difference between (2x2) and (2x1) at half ML per (1x1) unit cell, and the difference between the antiparallel (2x2):OH and aligned (2x1):OH per (2x2) unit cell. Write the total energies and these differences to energies.json.
- Output file: `/app/outputs/energies.json`
- Format: json
- Contract: JSON object with keys: halfML_2x1 (float, eV), halfML_2x2 (float, eV), fullML_2x1_aligned (float, eV), fullML_2x2_antiparallel (float, eV), halfML_energy_diff_per_1x1 (float, eV), fullML_energy_diff_per_2x2 (float, eV)
- Scoring: scored by hidden verifier

### Step 4: Extract geometric parameters
- Role: scored
- Action: From the relaxed atomic coordinates, extract the following geometric parameters for each of the four hydroxylated surface configurations. For halfML_2x1: C-C dimer length, C-C subsurface length (C_H-C), C-C subsurface length (C_OH-C), C-H bond length, C-O bond length, O-H bond length, H···OH hydrogen bond distance, H-O-C angle, H-C_S-C_S angle, O-C_S-C_S angle. For halfML_2x2: C-C dimer length (C_H-C_H), C-C dimer length (C_OH-C_OH), C-C subsurface length (C_H-C), C-C subsurface length (C_OH-C), C-H bond length, C-O bond length (top site), C-O bond length (bridge site), O-H bond length, H···OH hydrogen bond distance (bridge site), H···OH hydrogen bond distance (dimer site), H-O-C angle (bridge site OH), H-O-C angle (dimer site OH), H-C_S-C_S angle, O-C_S-C_S angle (C_H), O-C_S-C_S angle (C_OH). For fullML_2x1_aligned: C-C dimer length, C-C subsurface length, C-O bond length (top site), C-O bond length (bridge site), O-H bond length, H···OH hydrogen bond distance (bridge site), H···OH hydrogen bond distance (dimer site), H-O-C angle (bridge site OH), H-O-C angle (dimer site OH), O-C_S-C_S angle (bridge site), O-C_S-C_S angle (dimer site). For fullML_2x2_antiparallel: C-C dimer length, C-C subsurface length (a), C-C subsurface length (b), C-O bond length (top site), C-O bond length (bridge site), O-H bond length (a), O-H bond length (b), H···OH hydrogen bond distance (bridge site), H···OH hydrogen bond distance (dimer site), H-O-C angle (bridge site OH), H-O-C angle (dimer site OH), O-C_S-C_S angle (bridge site), O-C_S-C_S angle (dimer site). Write the results to geometries.csv with columns: structure, parameter, value, unit. Use units 'Angstrom' for lengths and 'degree' for angles.
- Output file: `/app/outputs/geometries.csv`
- Format: csv
- Contract: CSV with columns: structure (string, e.g. 'halfML_2x2'), parameter (string, e.g. 'C-C dimer length'), value (float), unit (string, e.g. 'Angstrom')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.json`
- `/app/outputs/geometries.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.json
- path: `/app/outputs/energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Total energies and energy differences of hydroxylated surface phases. The checker recomputes the differences and confirms the stability ordering.
- schema:
  - `type`: object
  - `required`:
    - `halfML_2x1`: float (eV)
    - `halfML_2x2`: float (eV)
    - `fullML_2x1_aligned`: float (eV)
    - `fullML_2x2_antiparallel`: float (eV)
    - `halfML_energy_diff_per_1x1`: float (eV)
    - `fullML_energy_diff_per_2x2`: float (eV)

### geometries.csv
- path: `/app/outputs/geometries.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of geometric parameters (bond lengths and angles) for the key surface configurations.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `parameter`, `value`, `unit`

Notes: The task uses Quantum ESPRESSO as the open-source DFT code instead of VASP; energy differences may shift slightly but the stability ordering is expected to be preserved. The chemical-potential analysis is excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "halfML_2x1": "float (eV)",
          "halfML_2x2": "float (eV)",
          "fullML_2x1_aligned": "float (eV)",
          "fullML_2x2_antiparallel": "float (eV)",
          "halfML_energy_diff_per_1x1": "float (eV)",
          "fullML_energy_diff_per_2x2": "float (eV)"
        }
      },
      "description": "Total energies and energy differences of hydroxylated surface phases. The checker recomputes the differences and confirms the stability ordering."
    },
    {
      "file": "geometries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "parameter",
          "value",
          "unit"
        ]
      },
      "description": "Table of geometric parameters (bond lengths and angles) for the key surface configurations."
    }
  ],
  "notes": "The task uses Quantum ESPRESSO as the open-source DFT code instead of VASP; energy differences may shift slightly but the stability ordering is expected to be preserved. The chemical-potential analysis is excluded."
}
```

## How you are scored
A hidden verifier will independently score each of your output files. For `energies.json`, it will read the reported total energies, recompute the energy differences, and compare them to expected reference values (not provided to you). The comparison evaluates both the magnitude and the sign of the energy differences against a correct stability ordering. For `geometries.csv`, each reported geometric parameter is compared to reference values. Both checks use appropriate tolerances; reporting the paper's numbers without actually running the DFT workflow will not yield a high reward. The verifier combines the scores from both artifacts by weight to produce a final reward between 0 and 1. A higher score indicates a more accurate and faithful reproduction of the computed physical quantities.
