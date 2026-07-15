# DFT Analysis of Carbon Cluster Formation and Coalescence on Cu and Ni Surfaces

## Problem background
The growth of high-quality monolayer graphene via chemical vapor deposition (CVD) on transition metal surfaces depends sensitively on substrate choice and the presence of hydrogen. Copper surfaces (Cu(111), Cu(100)) tend to produce large-area single-layer graphene, while nickel surfaces (Ni(111)) often yield defective, multi-layer films. A microscopic understanding of the initial nucleation of carbon clusters on these surfaces, and the role of hydrogen in controlling cluster structure and coalescence, is essential for improving graphene synthesis. First-principles density functional theory (DFT) can provide atomic-scale insight into the thermodynamics and kinetics of carbon and hydrocarbon clusters on metal surfaces.

## Approach
This task re-implements a DFT-based computational study of carbon cluster formation and coalescence on Cu and Ni surfaces. The approach involves: (1) constructing slab models of Cu(111) and Ni(111) surfaces, (2) relaxing the geometries of the clean surfaces and adsorbed C6 (pure carbon chain) and C6H6 (hydrogenated ring and chain) clusters, (3) evaluating the thermodynamic stability of these clusters by computing formation energies per carbon atom as a function of hydrogen chemical potential (μ_H), using the energy of graphene as the carbon reference, (4) determining the relative stability of ring vs chain configurations for C6H6 on each surface at high μ_H, and (5) computing the energy barrier for two partly hydrogenated C6H5 rings to coalesce on Cu(111) using the climbing-image nudged elastic band (CI-NEB) method.

All DFT calculations are performed with an open-source plane-wave code (Quantum ESPRESSO), employing the PBE exchange-correlation functional and standard pseudopotentials. The key physical inputs are the atomic structures of the clusters, the surface slab periodicity to achieve a carbon coverage of 0.074 monolayers, and the use of graphene's energy per atom as the carbon chemical potential (μ_C). The formation energy formula is E_f = E_a - E_metal - n \* μ_C - m \* μ_H, where n=6 and m=0 or 6 for C6 and C6H6, respectively, and μ_H is treated as a tunable parameter representing the growth conditions. The coalescence barrier is obtained from the CI-NEB energy profile between two separated C6H5 rings and the merged C12H10 product.

## Reproduction target
The goal is to produce three scored artifacts:
- A CSV file (formation_energies.csv) containing formation energies per carbon atom for C6 (pure carbon) and C6H6 (hydrogenated) clusters on Cu(111) and Ni(111) at two μ_H values: -1.6 eV (low hydrogen chemical potential) and -0.6 eV (high hydrogen chemical potential). Each row also indicates whether the cluster is hydrogenated and its structure type (ring or chain).
- A CSV file (structural_preference.csv) specifying which structure (ring or chain) has lower formation energy for C6H6 on Cu(111) and Ni(111) at μ_H = -0.6 eV.
- A plain text file (coalescence_barrier.txt) containing the CI-NEB energy barrier (in eV) for two C6H5 rings to coalesce into a C12H10 cluster on Cu(111).

These artifacts are computed entirely from the DFT workflow; the scoring is based on comparison to a hidden reference derived from the original study.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- SSSP library of PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Bulk fcc Cu crystal structure: https://materialsproject.org/materials/mp-30/
- Bulk fcc Ni crystal structure: https://materialsproject.org/materials/mp-23/
- Graphene unit cell for carbon chemical potential: https://materialsproject.org/materials/mp-48/
- Atomic Simulation Environment (ASE): ase
- NumPy: numpy

## Workflow steps

### Step 1: Clean metal surface geometry optimization
- Role: process
- Action: Build a 4-layer slab model of Cu(111) and Ni(111) with 9×9 surface periodicity (carbon coverage Θ=0.074 ML). Relax the atomic positions using DFT (PBE functional, PAW pseudopotentials, plane-wave cutoff 500 eV) to obtain reference total energies.
- Evidence: `/app/outputs/clean_surface_energies.json`

### Step 2: Adsorbed cluster relaxations
- Role: process
- Action: Build and relax DFT models for all required clusters on both surfaces: (a) pure carbon C6 chain on Cu(111) and Ni(111); (b) C6H6 ring and chain configurations on Cu(111) and Ni(111); (c) two separated C6H5 ring clusters on Cu(111) as reactant for coalescence. Keep slab settings consistent with step 01. Relax geometries until forces <0.02 eV/Å. Collect total energies.
- Evidence: `/app/outputs/cluster_energies.json`

### Step 3: Formation energy analysis
- Role: scored (load-bearing)
- Action: Using the clean surface energies and cluster energies from previous steps, compute formation energies per carbon atom via E_f = E_a - E_metal - n*μ_C - m*μ_H, where n=6, μ_C is the energy per atom in graphene (computed separately via DFT), and μ_H takes values -1.6 eV (low) and -0.6 eV (high). For each combination (surface, cluster, μ_H), write a row with formation energy and structure type (ring/chain).
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: required_columns: [surface, cluster, is_hydrogenated, mu_H, formation_energy_per_C, structure_type]; unit for formation_energy_per_C: eV/atom
- Scoring: scored by hidden verifier

### Step 4: Structural preference determination
- Role: scored
- Action: From the formation energies of C6H6 on each surface at μ_H = -0.6 eV, determine which structure (ring or chain) has lower formation energy. Write one row per surface indicating the lower-energy structure.
- Output file: `/app/outputs/structural_preference.csv`
- Format: csv
- Contract: required_columns: [surface, lower_energy_structure]; lower_energy_structure must be 'ring' or 'chain'
- Scoring: scored by hidden verifier

### Step 5: CI-NEB coalescence barrier calculation
- Role: process
- Action: Using the climbing-image nudged elastic band (CI-NEB) method, find the minimum energy path between two separated C6H5 rings (reactant) and the coalesced C12H10 product on Cu(111). Use the same slab settings. Determine the transition state energy and compute the energy barrier.
- Evidence: `/app/outputs/neb_profile.json`

### Step 6: Coalescence barrier reporting
- Role: scored
- Action: Extract the energy barrier (activation energy) from the NEB energy profile of step 05 as the difference between the transition state energy and the reactant energy. Write a single numeric value in eV.
- Output file: `/app/outputs/coalescence_barrier.txt`
- Format: txt
- Contract: type: text; single numeric value (positive float) in eV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/structural_preference.csv`
- `/app/outputs/coalescence_barrier.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Formation energy per carbon atom for C6 and C6H6 clusters on Cu(111) and Ni(111) at mu_H = -1.6 eV and -0.6 eV. Lower formation energy indicates greater thermodynamic stability.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `cluster`, `is_hydrogenated`, `mu_H`, `formation_energy_per_C`, `structure_type`
  - `units`:
    - `formation_energy_per_C`: eV/atom
    - `mu_H`: eV

### structural_preference.csv
- path: `/app/outputs/structural_preference.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Indicates whether the C6H6 cluster prefers a ring or chain structure on Cu(111) and Ni(111) at high mu_H (-0.6 eV).
- schema:
  - `type`: table
  - `required_columns`: `surface`, `lower_energy_structure`

### coalescence_barrier.txt
- path: `/app/outputs/coalescence_barrier.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Energy barrier (activation energy) for two C6H5 rings to coalesce on Cu(111), in eV. Lower is easier.
- schema:
  - `type`: text

Notes: All formation energies are per carbon atom. The coalescence barrier is the difference between the transition state and the reactant energies from the CI-NEB calculation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "cluster",
          "is_hydrogenated",
          "mu_H",
          "formation_energy_per_C",
          "structure_type"
        ],
        "units": {
          "formation_energy_per_C": "eV/atom",
          "mu_H": "eV"
        }
      },
      "description": "Formation energy per carbon atom for C6 and C6H6 clusters on Cu(111) and Ni(111) at mu_H = -1.6 eV and -0.6 eV. Lower formation energy indicates greater thermodynamic stability."
    },
    {
      "file": "structural_preference.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "lower_energy_structure"
        ]
      },
      "description": "Indicates whether the C6H6 cluster prefers a ring or chain structure on Cu(111) and Ni(111) at high mu_H (-0.6 eV)."
    },
    {
      "file": "coalescence_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text"
      },
      "description": "Energy barrier (activation energy) for two C6H5 rings to coalesce on Cu(111), in eV. Lower is easier."
    }
  ],
  "notes": "All formation energies are per carbon atom. The coalescence barrier is the difference between the transition state and the reactant energies from the CI-NEB calculation."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that inspects each of the three scored output files. The verifier checks that each file is present and correctly formatted, then extracts the reported values and compares them against reference values using a scoring function appropriate to each artifact.

For the formation energies (formation_energies.csv), the verifier checks whether each reported formation energy meets a quality threshold relative to the reference — lower formation energy (more stable) is better, and values that equal or surpass the reference threshold earn full credit; worse values are graded on a sliding scale. For the structural preference (structural_preference.csv), the verifier requires an exact match of the 'ring' or 'chain' label on each surface. For the coalescence barrier (coalescence_barrier.txt), the verifier checks whether the reported barrier is at most a certain acceptable value — a lower barrier (easier coalescence) is better.

The three scored stages are weighted to produce a final reward between 0 and 1, with the formation energy stage carrying the largest weight because it is the primary thermodynamic result. The verifier does not require you to reproduce the exact numbers from the reference; it is designed to reward physically correct trends and values that fall within the expected range of a correct independent DFT calculation with these settings. You must execute the complete DFT pipeline to obtain these numbers; simply reporting plausible guesses will not satisfy the formatting and self-consistency checks embedded in the verifier.
