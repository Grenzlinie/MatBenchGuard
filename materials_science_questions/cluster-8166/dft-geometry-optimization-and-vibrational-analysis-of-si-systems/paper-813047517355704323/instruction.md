# DFT Vibrational Modes of Si Pentamer-Pair and Hexagonal Cluster Models on Ag(110)

## Problem background
Self-assembled silicon nanostructures on Ag(110) are studied for potential nanoelectronic applications. The atomic structure of Si magic clusters that coexist with nanoribbons has been controversial. Two main structural models have been proposed: a hexagonal Si ring with adatoms, and a pentamer-pair model consisting of adjacent Si pentagons with adatoms placed on a Ag di-vacancy. DFT-calculated vibrational frequencies can serve as fingerprints to distinguish these models because the two geometries are expected to give different dominant out-of-plane vibrational modes. This task reproduces the computed main out-of-plane vibrational frequencies for both competing cluster models, providing the computational evidence required for structural identification.

## Approach
Density functional theory (DFT) is used to model the two cluster structures on an Ag(110) substrate. Initial atomic coordinates are built from the published structural descriptions: one model with a hexagonal Si ring and four Si adatoms on a Ag di-vacancy, and another with two adjacent Si pentagons (pentamer-pair) plus four Si adatoms on a Ag di-vacancy. Each model is geometry-optimized with a plane-wave DFT code using GGA-PBE exchange-correlation and appropriate pseudopotentials. After relaxation, a Γ-point phonon calculation computes the vibrational frequencies. The main out-of-plane mode is identified by the largest vertical displacement component, and its frequency is extracted for each model.

## Reproduction target
Reproduce the DFT-calculated main out-of-plane vibrational frequencies for the hexagonal-ring+adatoms cluster model and the pentamer-pair-on-Ag-di-vacancy model on Ag(110). The results are written to a JSON file containing the two frequencies. The aim is to confirm the frequency difference between the two structural models, which is the key computational signature used to discriminate the cluster geometry.

## Assets

- Quantum ESPRESSO open-source DFT package: https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials for Ag and Si: https://pseudopotentials.quantum-espresso.org/legacy_tables/ps-library

## Workflow steps

### Step 1: Build initial atomic structures
- Role: process
- Action: Construct initial atomic coordinates for two cluster models on Ag(110): (a) hexagonal Si ring + 4 Si adatoms placed on a Ag di-vacancy; (b) two adjacent Si pentagons (pentamer-pair) + 4 Si adatoms on a Ag di-vacancy. Use the known Ag lattice constant (4.085 Å) and the structural descriptions of the models. Save the DFT input files for geometry relaxation.
- Evidence: `/app/outputs/initial_structures.zip`

### Step 2: DFT geometry relaxation of hexagonal-ring model
- Role: process
- Action: Perform DFT geometry optimization of the hexagonal-ring cluster model on Ag(110) using a plane-wave DFT code. Relax ionic positions until forces converge to an energy minimum.
- Evidence: `/app/outputs/hex_relax.out`

### Step 3: DFT geometry relaxation of pentamer-pair model
- Role: process
- Action: Perform DFT geometry optimization of the pentamer-pair cluster model on Ag(110) analogously to the previous step, obtaining a relaxed structure.
- Evidence: `/app/outputs/pent_relax.out`

### Step 4: Vibrational frequency calculation and extraction
- Role: scored (load-bearing)
- Action: For both relaxed cluster models, run a phonon calculation (Γ‑point) to compute vibrational frequencies. Identify the dominant out-of-plane mode for each model (largest vertical displacement component). Write the two mode frequencies in cm⁻¹ to frequencies.json.
- Output file: `/app/outputs/frequencies.json`
- Format: json
- Contract: {"hexagonal_out_of_plane_cm-1": <float>, "pentamer_pair_out_of_plane_cm-1": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### frequencies.json
- path: `/app/outputs/frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Main out-of-plane vibrational mode frequencies for the hexagonal-ring model and the pentamer-pair model. The checker compares each frequency to a hidden expected range.
- schema:
  - `type`: object
  - `required`:
    - `hexagonal_out_of_plane_cm-1`: float
    - `pentamer_pair_out_of_plane_cm-1`: float
  - `units`:
    - `hexagonal_out_of_plane_cm-1`: cm⁻¹
    - `pentamer_pair_out_of_plane_cm-1`: cm⁻¹

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "hexagonal_out_of_plane_cm-1": "float",
          "pentamer_pair_out_of_plane_cm-1": "float"
        },
        "units": {
          "hexagonal_out_of_plane_cm-1": "cm⁻¹",
          "pentamer_pair_out_of_plane_cm-1": "cm⁻¹"
        }
      },
      "description": "Main out-of-plane vibrational mode frequencies for the hexagonal-ring model and the pentamer-pair model. The checker compares each frequency to a hidden expected range."
    }
  ],
  "notes": ""
}
```

## How you are scored
The submission is scored by a hidden verifier that reads the `frequencies.json` file you produce. The verifier compares your reported `hexagonal_out_of_plane_cm-1` and `pentamer_pair_out_of_plane_cm-1` each to a hidden expected range derived from reference DFT calculations. Both frequencies must fall within the accepted tolerances to pass. The final reward combines the outcomes of the two independent checks. You do not need to know the reference values; the verifier handles the comparison automatically.
