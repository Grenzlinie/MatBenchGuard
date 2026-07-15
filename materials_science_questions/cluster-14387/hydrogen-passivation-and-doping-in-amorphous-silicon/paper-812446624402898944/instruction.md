# Doping energy changes upon hydrogenation of amorphous silicon clusters

## Problem background
Amorphous hydrogenated silicon (a-Si:H) is a technologically important material used in thin-film solar cells and other optoelectronic devices. Unlike pure amorphous silicon, a-Si:H can be doped efficiently to create n-type and p-type conductivity, enabling electronic device functionality. The role of hydrogen in enabling substitutional doping is not fully understood at an atomic level. Computational studies that model atomic clusters of silicon with and without hydrogen, and with phosphorus (donor) or boron (acceptor) impurities, can quantify the energetic cost of inserting dopants and reveal how hydrogenation changes the doping energy landscape. In this task you will use semi-empirical quantum chemistry (CNDO/2) to compute total energies for six specific cluster models and then derive doping energy differences that characterize the effect of hydrogen on the doping process.

## Approach
The method uses cluster models to represent local atomic environments in pure silicon and hydrogenated silicon. Each cluster is built with tetrahedral coordination (Si-Si bond length 2.35 Å) and dangling bonds are saturated by hydrogen (Si-H bond length 1.48 Å). The clusters include a bare Si17, its hydrogenated form Si17H36, and doped variants where two first-nearest-neighbour silicon atoms are replaced by phosphorus or boron, both with and without hydrogen saturation (Si15P2, Si15B2, Si15P2H36, Si15B2H36).

You will perform CNDO/2 single-point energy calculations on each cluster. From the obtained total energies, you will compute doping energy differences using the definitions:
- ΔE1(X) = E(Si15X2) − E(Si17)
- ΔE2(X) = E(Si15X2H36) − E(Si17H36)
- ΔEE(X) = ΔE2(X) − ΔE1(X)
where X denotes the impurity (P or B). These quantities directly measure how the energy cost of substitutional doping changes upon hydrogenation, without relying on any external empirical data.

## Reproduction target
Produce two CSV files under `/app/outputs`:
1. `total_energies.csv` – containing the CNDO/2 total electronic energy (in eV) for each of the six clusters (Si17, Si17H36, Si15P2, Si15B2, Si15P2H36, Si15B2H36).
2. `doping_energies.csv` – containing the derived ΔE1, ΔE2, and ΔEE (in eV) for phosphorus and for boron, computed from the total energies with the formulas given above.

Your reproduction target is to produce these files with correct total energies and derived doping energetics that match the expected results from a faithful CNDO/2 implementation. A hidden verifier will compare your derived ΔE1, ΔE2, ΔEE values (six numbers) against reference results; no qualitative interpretation or figure reproduction is required.

## Assets

- CNDO/2 quantum chemistry implementation: pyscf

## Workflow steps

### Step 1: Build cluster models
- Role: process
- Action: Construct atomic coordinates for the six clusters (Si17, Si17H36, Si15P2, Si15B2, Si15P2H36, Si15B2H36) following the described tetrahedral coordination: central Si, four first-nearest-neighbour Si, twelve second-nearest-neighbour Si; Si-Si bond length 2.35 Å. Hydrogen saturate dangling bonds with Si-H 1.48 Å. For doped clusters, replace two first-nearest-neighbour Si atoms with P or B.
- Evidence: `/app/outputs/cluster_geometries.xyz`

### Step 2: Compute CNDO/2 total energies
- Role: scored (load-bearing)
- Action: Perform CNDO/2 single-point energy calculations for each of the six clusters using an open-source package that supports CNDO/2 (e.g., PySCF). For each cluster, extract the final total electronic energy in eV and write the results to total_energies.csv.
- Output file: `/app/outputs/total_energies.csv`
- Format: csv
- Contract: columns: cluster_name (string), total_energy_eV (float). Row order not enforced.
- Scoring: scored by hidden verifier

### Step 3: Compute doping energy differences
- Role: scored
- Action: From the total energies in total_energies.csv, compute ΔE1 = E(Si15X2) - E(Si17), ΔE2 = E(Si15X2H36) - E(Si17H36), and ΔEE = ΔE2 - ΔE1 for X = P and X = B. Write the derived values to doping_energies.csv.
- Output file: `/app/outputs/doping_energies.csv`
- Format: csv
- Contract: columns: impurity (string, one of 'P' or 'B'), ΔE1_eV (float), ΔE2_eV (float), ΔEE_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.csv`
- `/app/outputs/doping_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.csv
- path: `/app/outputs/total_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total CNDO/2 energies of the six clusters. The checker will recompute doping energy differences from this file and compare against hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `cluster_name`, `total_energy_eV`
  - `units`:
    - `total_energy_eV`: eV

### doping_energies.csv
- path: `/app/outputs/doping_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Derived doping energy differences. The checker will verify internal consistency with total_energies.csv (low weight).
- schema:
  - `type`: table
  - `required_columns`: `impurity`, `ΔE1_eV`, `ΔE2_eV`, `ΔEE_eV`
  - `units`:
    - `ΔE1_eV`: eV
    - `ΔE2_eV`: eV
    - `ΔEE_eV`: eV

Notes: All energies in eV. The checker recomputes ΔE1, ΔE2, ΔEE for phosphorus and boron from the provided total energies and compares them against hidden paper reference values with appropriate tolerances. Consistency of doping_energies.csv with total_energies.csv is also checked with lower weight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster_name",
          "total_energy_eV"
        ],
        "units": {
          "total_energy_eV": "eV"
        }
      },
      "description": "Total CNDO/2 energies of the six clusters. The checker will recompute doping energy differences from this file and compare against hidden reference values."
    },
    {
      "file": "doping_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity",
          "ΔE1_eV",
          "ΔE2_eV",
          "ΔEE_eV"
        ],
        "units": {
          "ΔE1_eV": "eV",
          "ΔE2_eV": "eV",
          "ΔEE_eV": "eV"
        }
      },
      "description": "Derived doping energy differences. The checker will verify internal consistency with total_energies.csv (low weight)."
    }
  ],
  "notes": "All energies in eV. The checker recomputes ΔE1, ΔE2, ΔEE for phosphorus and boron from the provided total energies and compares them against hidden paper reference values with appropriate tolerances. Consistency of doping_energies.csv with total_energies.csv is also checked with lower weight."
}
```

## How you are scored
A hidden verifier will read your `total_energies.csv` and independently recompute the doping energy differences ΔE1, ΔE2, ΔEE for phosphorus and boron. It will then compare these six derived values against hidden reference values using an absolute tolerance. Your reward is monotonic in the error: if all six values fall within the tolerance you receive full credit; as any value deviates beyond the tolerance, the score decreases smoothly, rewarding honest computational work that gets close. Additionally, the verifier may check that the values in `doping_energies.csv` are self-consistent with the total energies you provided (lower weight). You do not need to guess the tolerance – it is set to accommodate legitimate differences between CNDO/2 implementations while penalising obviously incorrect results.
