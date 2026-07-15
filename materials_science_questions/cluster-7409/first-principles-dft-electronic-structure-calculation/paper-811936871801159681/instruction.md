# DFT electronic structure and magnetic properties of 3d TM-doped anatase TiO2

## Problem background
Dilute magnetic oxides, particularly transition-metal-doped anatase TiO₂, are candidate materials for spintronics. Understanding which 3d dopants induce ferromagnetic order and predicting the chemical trend of magnetic ground states remains a central challenge. First-principles electronic structure calculations can determine the total energy difference between ferromagnetic and antiferromagnetic spin alignments and the associated magnetic moments, providing quantitative insight into the magnetic stability of each dopant. This task reproduces such a DFT study for the 3d series V, Cr, Mn, Fe, Co, and Ni in anatase TiO₂.

## Approach
The approach uses density functional theory within the local spin density approximation (LSDA). A 2×2×2 supercell of anatase TiO₂ is constructed. Single- and double-dopant cells are prepared by replacing Ti atoms with transition metals; ionic positions are relaxed. For each dopant, static total energy calculations are then performed with ferromagnetic and antiferromagnetic spin alignments on the two dopant ions. The energy difference per dopant, ΔE = (E_AFM − E_FM)/2, is extracted, and the magnetic moment per dopant is obtained from the spin‑resolved charge density. The magnetic ground state is determined from the sign of ΔE. A band coupling model based on d‑d level repulsions under the D₂d crystal field of anatase is used to interpret the chemical trend.

## Reproduction target
For each of the six transition metals (V, Cr, Mn, Fe, Co, Ni), compute the total energy difference per dopant between antiferromagnetic and ferromagnetic states (ΔE in meV), the magnetic moment per dopant (in μB), and the magnetic ground state (FM if ΔE > 0, AFM if ΔE < 0, paramagnetic if ΔE ≈ 0). Save these results in a CSV file at `/app/outputs/results.csv` with columns: `dopant` (e.g., V), `delta_E_meV`, `magnetic_moment_muB`, and `ground_state` (one of FM, AFM, PM).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Anatase TiO2 lattice constants

## Workflow steps

### Step 1: Build 2×2×2 anatase TiO2 supercell
- Role: process
- Action: Construct a 48-atom 2×2×2 supercell of anatase TiO2 using lattice constants a=3.768 Å, c=9.458 Å, internal parameter u=0.2085. Save atomic positions in a suitable format.
- Evidence: `/app/outputs/supercell_input.txt`

### Step 2: Relax single-dopant supercells for each 3d TM
- Role: process
- Action: For each 3d transition metal (V, Cr, Mn, Fe, Co, Ni), replace one central Ti atom in the supercell with the TM and perform ionic relaxation using LSDA-DFT (e.g., Quantum ESPRESSO with SSSP pseudopotentials). Save relaxed atomic coordinates.
- Evidence: `/app/outputs/single_dopant_relax.log`

### Step 3: Build and relax double-dopant superlattices
- Role: process
- Action: For each TM, replace two nearest-neighbor Ti atoms with the TM in the 48-atom supercell and perform ionic relaxation using the same DFT settings. Save relaxed coordinates.
- Evidence: `/app/outputs/double_dopant_relax.log`

### Step 4: Compute ΔE and magnetic moments and report results
- Role: scored (load-bearing)
- Action: For each TM's relaxed double-dopant supercell, perform static total energy calculations for ferromagnetic (FM) and antiferromagnetic (AFM) spin alignments. Compute energy difference per dopant ΔE = (E_AFM - E_FM)/2 in meV. Extract magnetic moment per dopant (μB) from spin-resolved charge density. Determine magnetic ground state: FM if ΔE > 0, AFM if ΔE < 0, paramagnetic (PM) if near zero. Output a CSV file with columns: dopant, delta_E_meV, magnetic_moment_muB, ground_state.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: Columns: dopant (string: V/Cr/Mn/Fe/Co/Ni), delta_E_meV (float), magnetic_moment_muB (float), ground_state (string: FM/AFM/PM).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table 2 reproduction: energy difference per dopant and magnetic moment. The hidden checker compares reported values to paper reference with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `dopant`, `delta_E_meV`, `magnetic_moment_muB`, `ground_state`
  - `units`:
    - `delta_E_meV`: meV
    - `magnetic_moment_muB`: μB

Notes: The checker compares reported values to hidden reference values from the paper with tolerances. The ground_state must be consistent with sign of delta_E.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dopant",
          "delta_E_meV",
          "magnetic_moment_muB",
          "ground_state"
        ],
        "units": {
          "delta_E_meV": "meV",
          "magnetic_moment_muB": "μB"
        }
      },
      "description": "Table 2 reproduction: energy difference per dopant and magnetic moment. The hidden checker compares reported values to paper reference with tolerances."
    }
  ],
  "notes": "The checker compares reported values to hidden reference values from the paper with tolerances. The ground_state must be consistent with sign of delta_E."
}
```

## How you are scored
A hidden verifier independently checks your `results.csv`. It compares every row's numeric values to reference data derived from the physical system, and verifies that the declared `ground_state` is consistent with the sign of `delta_E`. The overall score is the fraction of rows that pass all checks, combining accuracy of the three required fields per dopant. Reporting a known result without genuine computation is not sufficient; the verifier validates that your output is a plausible outcome of the described DFT workflow.
