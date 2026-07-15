# DFT Free-Energy Barriers for γ‑H Abstraction by Titanium Alkylidene Intermediates

## Problem background
Dinuclear titanium complexes can promote selective intramolecular cleavage of unactivated C–H bonds. This task focuses on the γ‑H abstraction step by Ti‑alkylidene intermediates, which DFT calculations identify as a key step that determines the observed reactivity order. Reproducing the free‑energy barriers for three different alkyl ligands will validate the proposed mechanism and the influence of ligand identity on the C–H activation barrier.

## Approach
Use density functional theory (DFT) to compute Gibbs free energies at 298.15 K and 1 atm for the intermediate and transition state structures of each ligand system. The B3LYP functional is used with LANL2DZ pseudopotentials (f polarization for Ti, d polarization for Si) and the 6‑31G(d,p) basis set for all other atoms; an equivalent open‑source implementation is acceptable. For each ligand (CH2SiMe3, CH2CMe3, CH2Ph), calculate the activation barrier ΔG‡ = G(transition state) – G(alkylidene intermediate) from single‑point energies and harmonic vibrational frequencies. The structures are provided as optimized XYZ coordinates in the Supporting Information.

## Reproduction target
Compute the three Gibbs free‑energy barriers (kcal·mol⁻¹) for the γ‑H abstraction step and write them to `gammaH_barriers.csv` with columns `ligand` (CH2SiMe3, CH2CMe3, CH2Ph) and `barrier_kcal_per_mol`. The computed barriers and their relative ordering will be evaluated against a reference (hidden). No other quantities are required.

## Assets

- XYZ coordinate file of calculated structures from the Supporting Information: https://pubs.acs.org/doi/suppl/10.1021/acs.organomet.7b00416/suppl_file/om7b00416_si_002.xyz
- DFT quantum chemistry code (e.g., ORCA, PySCF, Gaussian): orca / pyscf

## Workflow steps

### Step 1: Retrieve and identify input structures
- Role: process
- Action: Download the XYZ coordinate file from the Supporting Information and extract the Cartesian coordinates of the Ti‑alkylidene intermediates (2′, 3′, 5′) and the corresponding γ‑H abstraction transition states. Write the list of structures used to 'input_structures.txt'.
- Evidence: `/app/outputs/input_structures.txt`

### Step 2: Recompute γ‑H abstraction barriers
- Role: scored (load-bearing)
- Action: For each of the three ligand systems, perform a single-point energy calculation and vibrational frequency analysis on the extracted structures (intermediate and TS) using DFT with the B3LYP functional and appropriate basis sets (LANL2DZ with f polarization for Ti, LANL2DZ with d polarization for Si, 6‑31G(d,p) for H, C, O, or an equivalent open‑source implementation). Compute the Gibbs free energy at 298.15 K and 1 atm. Then calculate the activation barrier as ΔG‡ = G(TS) − G(intermediate). Output the results to 'gammaH_barriers.csv'.
- Output file: `/app/outputs/gammaH_barriers.csv`
- Format: csv
- Contract: Two columns: 'ligand' (string, one of CH2SiMe3, CH2CMe3, CH2Ph) and 'barrier_kcal_per_mol' (float, positive).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gammaH_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gammaH_barriers.csv
- path: `/app/outputs/gammaH_barriers.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed Gibbs free-energy barriers for γ‑H abstraction by Ti-alkylidene intermediates for three ligand systems. The ordering of barriers is also compared to the expected trend.
- schema:
  - `type`: table
  - `required_columns`: `ligand`, `barrier_kcal_per_mol`
  - `units`:
    - `barrier_kcal_per_mol`: kcal/mol

Notes: The scoring checks each barrier against a target value within a tolerance and verifies the trend CH2SiMe3 < CH2CMe3 <= CH2Ph. The specific targets and tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gammaH_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ligand",
          "barrier_kcal_per_mol"
        ],
        "units": {
          "barrier_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Computed Gibbs free-energy barriers for γ‑H abstraction by Ti-alkylidene intermediates for three ligand systems. The ordering of barriers is also compared to the expected trend."
    }
  ],
  "notes": "The scoring checks each barrier against a target value within a tolerance and verifies the trend CH2SiMe3 < CH2CMe3 <= CH2Ph. The specific targets and tolerances are hidden."
}
```

## How you are scored
The hidden verifier reads `gammaH_barriers.csv` and scores the task. It checks that the computed barriers are within a tolerance around reference values and that the ordering among the three ligands matches the expected trend. Full credit is awarded when all absolute barriers meet the tolerance and the trend is correct; partial credit may be given if only the trend holds. Only the scored artifact (step 2) contributes to the final reward.
