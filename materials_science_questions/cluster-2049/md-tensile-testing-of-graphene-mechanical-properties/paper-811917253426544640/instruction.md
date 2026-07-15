# DFT simulation of graphene-aluminium interface dispersion relations

## Problem background
Lightweight high-strength nanocomposites rely on the interface between carbon nanoreinforcements and an aluminium matrix to transfer load and resist chemical degradation. It is therefore critical to characterise the interfacial bonding when a single graphene sheet is placed on an Al(111) layer. The interactions depend on how the atoms are arranged (the interface registry) and on the interlayer distance; a quantitative understanding of these interactions is needed to guide the processing of metal-matrix nanocomposites. This task investigates two specific registries using first-principles density functional theory, with the goal of computing the potential energy of the interface as a function of the graphene–aluminium separation distance.

## Approach
The calculation uses plane-wave-based density functional theory within the local density approximation (LDA), as implemented in the open-source code ABINIT. Norm-conserving Troullier–Martins pseudopotentials are employed for carbon and aluminium. The model system consists of a single graphene sheet and a single Al(111) layer placed in a supercell with sufficient vacuum space. Two interface registries are studied:  
1. **SFR-1** – a strain-free matching of the Al(111) layer to the graphene lattice, without in-plane strain.  
2. **H-1** – a coherent registry where the Al layer is compressively strained by approximately 14.4% so that Al atoms sit over hollow sites of the graphene sheet.  
For each registry, a series of static total-energy calculations is performed at interlayer distances ranging from 2.0 to 18.0 bohr in steps of 0.1 bohr. The total energy at the largest separation (18 bohr) is taken as the reference energy of effectively isolated layers, and the relative energy at each distance is obtained by subtracting this reference. The resulting potential-energy curve – the dispersion relation – reveals the depth of the potential well (the cohesive energy) and the distance at which the minimum occurs (the equilibrium separation).

## Reproduction target
Produce a single CSV file that contains the potential-energy curves for both the SFR-1 and H-1 registries. The file must cover interlayer distances from 2.0 to 18.0 bohr in steps of 0.1 bohr, with the energy reported relative to that at 18 bohr. The columns must be:  
- `registry` (string, one of `SFR-1` or `H-1`),  
- `distance_bohr` (float, the interlayer distance in bohr),  
- `energy_relative_eV` (float, the relative energy in eV).  
A hidden verifier will later read this file, determine for each registry the distance at which the relative energy is minimised, and from that derive the cohesive energy (the negative of the minimum) and the equilibrium separation.

## Assets

- ABINIT DFT code (open-source): https://www.abinit.org/downloads
- Troullier-Martins LDA pseudopotentials for C and Al: https://www.abinit.org/downloads/psp-links/lda_tm

## Workflow steps

### Step 1: Build atomic models for SFR-1 and H-1 registries
- Role: process
- Action: Construct the unit cells for the graphene/Al(111) system in the SFR-1 (strain-free matching) and H-1 (14.4% compressive strain, Al over hollow sites) registries as described in the paper. Include sufficient vacuum gap. Optionally perform a brief geometry relaxation; treat final in-plane positions as fixed for the energy scan.
- Evidence: `/app/outputs/structures.cif`

### Step 2: Compute potential energy curves for SFR-1 and H-1
- Role: scored (load-bearing)
- Action: For each registry, run a series of DFT total-energy calculations at interlayer distances from 2.0 to 18.0 bohr in steps of 0.1 bohr using ABINIT with LDA and Troullier-Martins pseudopotentials. Use the total energy at 18 bohr as the reference energy. Output all relative energies to a single CSV file.
- Output file: `/app/outputs/potential_energy_curves.csv`
- Format: csv
- Contract: registry: string (one of SFR-1, H-1); distance_bohr: float; energy_relative_eV: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/potential_energy_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### potential_energy_curves.csv
- path: `/app/outputs/potential_energy_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw potential energy curves for the strain-free (SFR-1) and strained coherent (H-1) graphene/Al(111) interfaces. The checker will find the minimum of each curve to derive cohesive energy and equilibrium separation and compare them to hidden paper reference values.
- schema:
  - `type`: table
  - `required_columns`: `registry`, `distance_bohr`, `energy_relative_eV`
  - `units`:
    - `distance_bohr`: bohr
    - `energy_relative_eV`: eV

Notes: The scored artifact is the raw energy curve CSV. The checker recomputes cohesive energy and equilibrium distance from the curve minimums and compares to the paper's reported values with tolerances, giving full reward only when both registries pass. The process steps (model building) are enforced by requiring the load-bearing scored step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "potential_energy_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "registry",
          "distance_bohr",
          "energy_relative_eV"
        ],
        "units": {
          "distance_bohr": "bohr",
          "energy_relative_eV": "eV"
        }
      },
      "description": "Raw potential energy curves for the strain-free (SFR-1) and strained coherent (H-1) graphene/Al(111) interfaces. The checker will find the minimum of each curve to derive cohesive energy and equilibrium separation and compare them to hidden paper reference values."
    }
  ],
  "notes": "The scored artifact is the raw energy curve CSV. The checker recomputes cohesive energy and equilibrium distance from the curve minimums and compares to the paper's reported values with tolerances, giving full reward only when both registries pass. The process steps (model building) are enforced by requiring the load-bearing scored step."
}
```

## How you are scored
A hidden verifier will read your submitted CSV file and, independently of your own code, compute the cohesive energy and equilibrium distance for each of the two registries. It does this by grouping the rows by registry, finding the row with the smallest `energy_relative_eV`, and taking the negative of that energy as the cohesive energy and the corresponding `distance_bohr` as the equilibrium separation. These values are then compared to hidden reference values (the paper’s reported results) with pre-set tolerances. Each registry that passes both the cohesive-energy and equilibrium-distance checks contributes half of the total reward. If only one registry passes, you receive half the maximum reward; if both pass, you receive the full reward. Simply reporting a number without providing the raw CSV curve is not sufficient – the verifier recomputes everything from the raw data you supply.
