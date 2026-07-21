# Electronic Structure and Bonding Analysis of Transition Metal-Doped Boron Clusters

## Problem background
Transition metal (TM) doping is a widely studied strategy for tuning the stability and electronic properties of boron nanoclusters. Understanding how each 3d, 4d, and 5d TM atom influences the quasi-planar B36 cluster is important for designing TM-boron systems. This task investigates the structural stability (average binding energy), kinetic activity (HOMO-LUMO gap), and bonding character (Mulliken net charge) of TM-doped B36 clusters using first-principles DFT calculations. The goal is to determine, for all 30 TMs, how doping changes these quantities relative to pristine B36.

## Approach
Density functional theory (DFT) at the Perdew-Burke-Ernzerhof (PBE) level of the generalized gradient approximation is used. The computational protocol includes: (1) constructing starting structures for B36 (D2h symmetry) and for each TMB36 cluster by placing a single TM atom near the centre of one of the surface hexagonal rings of the B36 cluster (following the approach of a TM atom approaching the hexagonal of the B36 clusters); (2) performing spin-unrestricted, all-electron relativistic geometry optimizations followed by single-point energy calculations with a double-numerical polarized (or equivalent) basis set; (3) extracting total energy, HOMO/LUMO energies, and Mulliken atomic charges for every cluster.

The average binding energy per atom is defined as:

For pristine B36:
`E_b = [36 * E(B) - E(B36)] / 36`   (1)

For TMB36 clusters:
`E_b = [E(TM) + 36 * E(B) - E(TMB36)] / 37`   (2)

where `E(TM)` and `E(B)` are the isolated atomic total energies of the TM and B atoms, respectively, and `E(B36)` and `E(TMB36)` are the total energies of the B36 and TMB36 clusters. The HOMO-LUMO gap is defined as:

`E_g = E_LUMO - E_HOMO`   (3)

Bonding character is assessed through the Mulliken net charge on the TM atom. All 31 systems (pristine B36 + 30 TMB36) are treated with the same functional and basis set, allowing direct comparison of the computed quantities.

## Reproduction target
Compute the average binding energy per atom, the HOMO-LUMO gap, and the Mulliken net charge on the TM atom for each TMB36 cluster (TM = Sc through Zn, Y through Cd, Lu through Hg) and for pristine B36. Report the results in two CSV files: (1) `energies_and_gaps.csv` containing total energy, binding energy, HOMO energy, LUMO energy, and gap for every cluster; (2) `mulliken_charges.csv` containing the TM atom and its net charge for each doped cluster. The calculations must follow the DFT protocol described (PBE functional, spin-unrestricted, all-electron relativistic, DNP or equivalent basis set). You may use any open-source DFT code that supports this methodology.

## Assets

- B36 D2h structure coordinates (available from the literature on planar boron clusters; the structure has D2h symmetry with a central hexagonal hole).
- Open-source DFT code (e.g., CP2K, Quantum ESPRESSO, ORCA).

## Workflow steps

### Step 1: Construct initial TMB36 geometries
- Role: process
- Action: Obtain the published D2h B36 coordinates and generate starting structures for all 30 TMB36 clusters by placing each TM atom near the centre of a surface hexagonal ring of the B36 cluster (not inside the central hole). Record the generated initial geometries for reproducibility (as a text file under `/app/outputs` if desired).

### Step 2: Compute reference atomic energies
- Role: process
- Action: Perform single-point spin-unrestricted, all-electron relativistic DFT calculations for isolated B and each TM atom using the same PBE functional and basis set to obtain the reference total energies E(B) and E(TM) needed for the binding energy formulas. Save these atomic energies for subsequent use.

### Step 3: Run DFT geometry optimizations for all clusters
- Role: process
- Action: For pure B36 and each TMB36 cluster, perform an unconstrained geometry optimization using the PBE functional and a suitable basis set (DNP or equivalent), followed by a single-point calculation to extract the final total energy, HOMO and LUMO energies, and Mulliken atomic charges. All calculations must use spin-unrestricted formalism. Log the optimization outcomes for diagnostics.

### Step 4: Compile energies and HOMO-LUMO gaps
- Role: scored (load-bearing)
- Action: Extract from the DFT outputs the total energy, HOMO and LUMO energies, compute the average binding energy per atom (using equations (1) and (2) and the atomic reference energies) and the HOMO-LUMO gap (equation (3)), and write the results to a CSV table.
- Output file: `/app/outputs/energies_and_gaps.csv`
- Format: csv
- Contract: Columns: cluster (string), total_energy_Hartree (float), binding_energy_eV_per_atom (float), homo_eV (float), lumo_eV (float), gap_eV (float).
- Scoring: scored by hidden verifier

### Step 5: Compile Mulliken net charges
- Role: scored (load-bearing)
- Action: Extract the Mulliken net charge on the TM atom for each doped cluster from the DFT outputs and write a CSV file.
- Output file: `/app/outputs/mulliken_charges.csv`
- Format: csv
- Contract: Columns: cluster (string), tm_atom (string), net_charge_e (float).
- Scoring: scored by hidden verifier

## Output files
Write all scored artifacts under `/app/outputs`:
- `/app/outputs/energies_and_gaps.csv`
- `/app/outputs/mulliken_charges.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies_and_gaps.csv
- path: `/app/outputs/energies_and_gaps.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Total energies, average binding energies, HOMO/LUMO energies and HOMO-LUMO gaps for B36 and all 30 TM-doped clusters.
- schema:
  - `type`: table
  - `required_columns`: `cluster`, `total_energy_Hartree`, `binding_energy_eV_per_atom`, `homo_eV`, `lumo_eV`, `gap_eV`

### mulliken_charges.csv
- path: `/app/outputs/mulliken_charges.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Mulliken net charges on the transition metal atom for each TMB36 cluster.
- schema:
  - `type`: table
  - `required_columns`: `cluster`, `tm_atom`, `net_charge_e`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies_and_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster",
          "total_energy_Hartree",
          "binding_energy_eV_per_atom",
          "homo_eV",
          "lumo_eV",
          "gap_eV"
        ]
      },
      "description": "Total energies, average binding energies, HOMO/LUMO energies and HOMO-LUMO gaps for B36 and all 30 TM-doped clusters."
    },
    {
      "file": "mulliken_charges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster",
          "tm_atom",
          "net_charge_e"
        ]
      },
      "description": "Mulliken net charges on the transition metal atom for each TMB36 cluster."
    }
  ],
  "notes": "Scoring verifies that the computed gaps and binding energies satisfy required trends and thresholds, and net charges indicate covalent character."
}
```

## How you are scored
Your computed results will be automatically compared against reference values obtained from the published study. The evaluation will assess proximity to expected values, check that all doped clusters have a smaller HOMO‑LUMO gap than pristine B36, and verify that certain TM dopants enhance binding energy. No further details on thresholds or specific metals are provided here.