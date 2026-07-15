# Strain tuning of band gaps in 2D tetragonal MgS and MgSe monolayers

## Problem background
Two-dimensional monolayer semiconductors are of great interest for future electronic and optoelectronic devices. First-principles calculations have recently predicted two new 2D group II‑VI monolayers — tetragonal MgS and MgSe — that are stable and possess wide band gaps. A key attraction is that their electronic band gaps can be tuned by applying external biaxial strain, which is essential for strain‑engineered devices. The precise dependence of the band gap on strain, however, must be determined through computational modelling. In this task you will compute the band gap of these monolayers under a range of biaxial strains and characterise the material‑specific strain responses.

## Approach
The approach is based on density functional theory (DFT) using the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional. Each monolayer is modelled as a periodic slab with a vacuum layer to suppress inter‑layer interactions. Starting from sensible initial lattice constants and atomic positions, you will fully relax both the in‑plane lattice parameter and the internal coordinates to obtain the equilibrium structure. Then, for a set of biaxial strain values ranging from −8 % to +8 %, you will scale the in‑plane lattice constant proportionally to the strain, relax the atomic positions while keeping the cell dimensions fixed, and compute the electronic band structure along the high‑symmetry path Γ–X–M–Γ. The band gap is extracted as the difference between the conduction‑band minimum and valence‑band maximum. All calculations are performed with the open‑source plane‑wave code Quantum ESPRESSO using publicly available PBE pseudopotentials. The final outputs are two CSV files, one per material, listing strain and band gap.

## Reproduction target
Using Quantum ESPRESSO (or any PBE‑DFT code that yields consistent results) and standard PBE pseudopotentials, compute the electronic band gap of the tetragonal MgS and MgSe monolayers for biaxial strains ε = 0 %, ±2 %, ±4 %, ±6 %, ±8 %. For each strain, relax the atomic positions and obtain the band gap from the band structure. Write two CSV files, `MgS_bandgap_vs_strain.csv` and `MgSe_bandgap_vs_strain.csv`, each containing the nine rows with columns `strain` (percentage, ordered from −8 to 8) and `bandgap` (electronvolts). The verifier will subsequently check that your strain‑gap curves exhibit the expected physical trends for the two materials.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials for Mg, S, Se: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Build initial atomic structures
- Role: process
- Action: Generate starting atomic coordinates for the tetragonal MgS and MgSe unit cells. Use a buckled structure with two Mg and two X atoms per cell, approximate lattice constants a ≈ 4.41 Å (MgS) and 4.52 Å (MgSe), buckling distances Δ ≈ 2.27 Å (MgS) and 2.67 Å (MgSe), and a vacuum layer ≥ 20 Å. Write the structures as a CIF file.
- Evidence: `/app/outputs/initial_structures.cif`

### Step 2: Optimize structures
- Role: process
- Action: Using Quantum ESPRESSO (pw.x) with PBE pseudopotentials, relax both cell parameters (in-plane lattice constant a) and atomic positions for MgS and MgSe to obtain equilibrium structures. Write a JSON file containing the equilibrium lattice constant a0 and final atomic positions.
- Evidence: `/app/outputs/optimized_structures.json`

### Step 3: Compute band gap vs strain for MgS
- Role: scored (load-bearing)
- Action: Starting from the optimized MgS structure, apply biaxial strains ε = -8%, -6%, -4%, -2%, 0%, 2%, 4%, 6%, 8% by scaling the in-plane lattice constant a = a0·(1+ε). For each strain, relax atomic positions (keeping lattice constant fixed), perform a self-consistent calculation and a band structure calculation along Γ–X–M–Γ, then extract the band gap. Write a CSV file MgS_bandgap_vs_strain.csv with columns strain and bandgap.
- Output file: `/app/outputs/MgS_bandgap_vs_strain.csv`
- Format: csv
- Contract: Two columns: strain (numeric, percentage from -8 to 8), bandgap (numeric, electronvolts). One row for each strain value.
- Scoring: scored by hidden verifier

### Step 4: Compute band gap vs strain for MgSe
- Role: scored (load-bearing)
- Action: Starting from the optimized MgSe structure, apply biaxial strains ε = -8%, -6%, -4%, -2%, 0%, 2%, 4%, 6%, 8% by scaling the in-plane lattice constant a = a0·(1+ε). For each strain, relax atomic positions, perform a self-consistent calculation and a band structure calculation along Γ–X–M–Γ, then extract the band gap. Write a CSV file MgSe_bandgap_vs_strain.csv with columns strain and bandgap.
- Output file: `/app/outputs/MgSe_bandgap_vs_strain.csv`
- Format: csv
- Contract: Two columns: strain (numeric, percentage from -8 to 8), bandgap (numeric, electronvolts). One row for each strain value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/MgS_bandgap_vs_strain.csv`
- `/app/outputs/MgSe_bandgap_vs_strain.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### MgS_bandgap_vs_strain.csv
- path: `/app/outputs/MgS_bandgap_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band gap of MgS monolayer under biaxial strain.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `bandgap`
  - `units`:
    - `strain`: percent
    - `bandgap`: eV

### MgSe_bandgap_vs_strain.csv
- path: `/app/outputs/MgSe_bandgap_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band gap of MgSe monolayer under biaxial strain.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `bandgap`
  - `units`:
    - `strain`: percent
    - `bandgap`: eV

Notes: Structural audit for strain‑bandgap trends (MgS monotonic decrease, MgSe compressive peak near −6%). Additional checks on the zero‑strain band gap will be embedded in the checker logic to verify the wide‑gap nature against the paper’s PBE values without requiring a separate output file. Optical absorption verification is not included because the oracle cannot produce the required heavy DFT output and the solver block mechanism does not support adding new blocks at this stage.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "MgS_bandgap_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "bandgap"
        ],
        "units": {
          "strain": "percent",
          "bandgap": "eV"
        }
      },
      "description": "Band gap of MgS monolayer under biaxial strain."
    },
    {
      "file": "MgSe_bandgap_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "bandgap"
        ],
        "units": {
          "strain": "percent",
          "bandgap": "eV"
        }
      },
      "description": "Band gap of MgSe monolayer under biaxial strain."
    }
  ],
  "notes": "Structural audit for strain‑bandgap trends (MgS monotonic decrease, MgSe compressive peak near −6%). Additional checks on the zero‑strain band gap will be embedded in the checker logic to verify the wide‑gap nature against the paper’s PBE values without requiring a separate output file. Optical absorption verification is not included because the oracle cannot produce the required heavy DFT output and the solver block mechanism does not support adding new blocks at this stage."
}
```

## How you are scored
A hidden verifier will read your CSV files and evaluate the band‑gap values across the strain range using trend‑based criteria that capture the expected physical behaviour (e.g., monotonicity, the location of a peak, or other structural patterns). The verifier does not rely on exact numerical matches to a reference value; instead it checks whether your computed strain‑response curves are consistent with the known characteristics of these materials. Both files contribute to the overall score, with the final reward being a weighted combination. Quoting numbers from the literature without genuine computation will not satisfy the structural checks — you must run the DFT workflow and submit results that naturally pass the hidden trend verification.
