# Periodic DFT Lattice Energies and Sublimation Enthalpies of Cyclic Hydride Crystals

## Problem background
Cyclic hydride compounds such as [H2GaNH2]3, [H2BNH2]3, and [H2GeCH2]3 are potential precursors for chemical vapor deposition. Their volatility depends on the cohesive forces in the solid state, which are quantified by the lattice energy and the enthalpy of sublimation. Understanding these energies requires accurately modeling the intermolecular interactions (including dihydrogen bonds) that hold the crystals together. This task computes these quantities from first principles using periodic density functional theory, providing insight into how the experimental crystal packing affects the thermodynamic stability of each compound.

## Approach
The approach is a periodic DFT workflow. First, the experimental crystal structures of the three compounds are obtained from the Cambridge Structural Database. For each compound, the gas‑phase molecule in the chair conformation (the form found in the solid) is optimized to obtain its energy. Because two of the compounds may prefer a different conformation in the gas phase, the energy difference between the chair and twist‑boat conformers is calculated as a correction. Then, periodic DFT optimizations are performed for every compound in its experimentally observed space group and in the two alternative space groups, yielding optimized lattice parameters and atomic positions. Basis set superposition error (BSSE) is estimated via counterpoise corrections. Lattice energies are derived from the crystal and gas‑phase energies, corrected for BSSE, and written to a CSV file. For the native space groups only, vibrational frequency calculations provide zero‑point and thermal contributions, which are combined with the lattice energies to yield sublimation enthalpies at 298 K. Every step uses the B3LYP‑D3 functional with the pob‑TZVP basis set.

## Reproduction target
Produce two scored CSV files under `/app/outputs`:

- `lattice_energies.csv` containing the lattice energy (in kJ/mol) for each of the three compounds in each of the three space groups: P2₁/m, Pmn2₁, and Pbcm. This yields 9 rows total.
- `sublimation_enthalpies.csv` containing the sublimation enthalpy at 298 K (in kJ/mol) for each compound in its experimentally observed space group only.

Additionally, for each compound the lattice energy in its native (experimentally observed) space group must be larger than the lattice energies computed in the two alternative space groups.

## Assets

- Experimental crystal structures of [H2GaNH2]3, [H2BNH2]3, [H2GeCH2]3: https://www.ccdc.cam.ac.uk/structures/
- pob-TZVP basis set: https://www.basissetexchange.org
- Periodic DFT code: https://www.crystal.unito.it/

## Workflow steps

### Step 1: Obtain experimental crystal structures
- Role: process
- Action: Retrieve the crystal structures of [H2GaNH2]3 (space group P2₁/m), [H2BNH2]3 (Pbcm), and [H2GeCH2]3 (Pmn2₁) from the Cambridge Structural Database. Extract lattice parameters, atomic positions, and symmetry operations.
- Evidence: `/app/outputs/structure_files.txt`

### Step 2: Gas-phase molecule optimization and energy calculation
- Role: process
- Action: For each compound, optimize the isolated gas-phase molecule in the chair conformation using DFT (B3LYP-D3/pob‑TZVP) to obtain the gas-phase energy, zero-point vibrational energy (ZPVE), and vibrational contributions at 298 K.
- Evidence: `/app/outputs/gas_phase_energies.log`

### Step 3: Conformational energy calculation
- Role: process
- Action: For [H2GaNH2]3 and [H2BNH2]3, optimize the twist-boat conformer and compute the energy difference ΔE(conf) relative to the chair conformer. For [H2GeCH2]3 the chair is more stable; ΔE(conf)=0.
- Evidence: `/app/outputs/conf_energies.txt`

### Step 4: Periodic crystal structure optimization and property calculation
- Role: process
- Action: For each compound, perform periodic DFT optimization (atomic positions and lattice parameters) in its native space group and in the two alternative space groups (P2₁/m, Pmn2₁, Pbcm) using B3LYP-D3/pob‑TZVP. For the native space groups only, also compute zero-point vibrational energy (crystal) and vibrational contributions at 298 K.
- Evidence: `/app/outputs/periodic_opt.log`

### Step 5: BSSE correction calculation
- Role: process
- Action: For each optimized configuration, compute the counterpoise basis set superposition error correction E(BSSE) using the same functional and basis set.
- Evidence: `/app/outputs/bsse.log`

### Step 6: Lattice energy calculation
- Role: scored (load-bearing)
- Action: From the crystal energies, gas-phase chair energies, and BSSE corrections, compute the lattice energy for each of the 9 configurations using the relation E(lattice) = E(Cs) − E(crystal)/Z − E(BSSE). Write the results to lattice_energies.csv.
- Output file: `/app/outputs/lattice_energies.csv`
- Format: csv
- Contract: CSV with columns: compound (string), space_group (string), lattice_energy_kJ_mol (float). One row per configuration.
- Scoring: scored by hidden verifier

### Step 7: Sublimation enthalpy calculation
- Role: scored (load-bearing)
- Action: For each compound in its native space group, compute the sublimation enthalpy at 298 K using ΔH_sub(298) = E(lattice) + ΔE(conf) + ΔE_ZPVE + ΔE_vib(298) + 4RT. Use the lattice energy from step 6, conformational correction from step 3, and vibrational data from steps 2 and 4. Write the results to sublimation_enthalpies.csv.
- Output file: `/app/outputs/sublimation_enthalpies.csv`
- Format: csv
- Contract: CSV with columns: compound (string), space_group (string), sublimation_enthalpy_298K_kJ_mol (float). One row per compound.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_energies.csv`
- `/app/outputs/sublimation_enthalpies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_energies.csv
- path: `/app/outputs/lattice_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Lattice energies at 0 K for every compound‑space‑group combination. The native space group should yield the largest lattice energy for each compound.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `space_group`, `lattice_energy_kJ_mol`
  - `items`:
    - `lattice_energy_kJ_mol`: float

### sublimation_enthalpies.csv
- path: `/app/outputs/sublimation_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Enthalpies of sublimation at 298 K for each compound in its experimentally observed space group.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `space_group`, `sublimation_enthalpy_298K_kJ_mol`
  - `items`:
    - `sublimation_enthalpy_298K_kJ_mol`: float

Notes: Both artifacts are derived from periodic DFT calculations. The checker compares each value to hidden reference values (paper Table 6 for lattice energies; Table 7 for sublimation enthalpies) with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "space_group",
          "lattice_energy_kJ_mol"
        ],
        "items": {
          "lattice_energy_kJ_mol": "float"
        }
      },
      "description": "Lattice energies at 0 K for every compound‑space‑group combination. The native space group should yield the largest lattice energy for each compound."
    },
    {
      "file": "sublimation_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "space_group",
          "sublimation_enthalpy_298K_kJ_mol"
        ],
        "items": {
          "sublimation_enthalpy_298K_kJ_mol": "float"
        }
      },
      "description": "Enthalpies of sublimation at 298 K for each compound in its experimentally observed space group."
    }
  ],
  "notes": "Both artifacts are derived from periodic DFT calculations. The checker compares each value to hidden reference values (paper Table 6 for lattice energies; Table 7 for sublimation enthalpies) with appropriate tolerances."
}
```

## How you are scored
A hidden verifier assesses each CSV file independently. For `lattice_energies.csv`, every entry is compared to a set of reference values derived from the original study, using tolerances that account for small differences in DFT codes and basis sets. The verifier also checks that for each compound the native space group yields the highest lattice energy among the three groups tested. For `sublimation_enthalpies.csv`, the value for [H2BNH2]3 is compared to an independently measured experimental reference; the other two compounds are checked to ensure the computed enthalpies are physically reasonable. The final reward is a weighted sum of these checks.
