# Electronic Thermoelectric Figure of Merit of SnSe-based Hybrids and Nanostructured CsPbI3

## Problem background
Tin selenide (SnSe) in its high-temperature Cmcm phase has attracted significant interest as a thermoelectric material due to its exceptionally low thermal conductivity and high figure of merit. A promising strategy to further improve thermoelectric performance is to hybridize SnSe with other two-dimensional materials, such as hexagonal boron nitride (h-BN) or the perovskite CsPbI₃, or to nanostructure CsPbI₃ into few-layer forms. This task computes the electronic figure of merit ZT_elec for SnSe-hBN and SnSe-CsPbI₃ hybrid superlattices and for layered CsPbI₃ systems using first-principles electronic structure methods and semiclassical Boltzmann transport, to assess whether these design strategies enhance thermoelectric performance.

## Approach
The calculation proceeds in two stages. First, density functional theory (DFT) with the PBE exchange-correlation functional and van der Waals correction is employed in Quantum Espresso to relax the crystal structures of SnSe-hBN, SnSe-CsPbI₃, and 1–4 layer CsPbI₃, and to compute their Kohn-Sham band structures on a fine k-point grid. Second, the band eigenvalues are processed with the BoltzTraP code under the constant scattering time approximation (CSTA) to obtain the temperature-dependent Seebeck coefficient S, electrical conductivity σ/τ, and electronic thermal conductivity κ₀/τ. The electronic figure of merit ZT_elec = S²σT/κ₀ is evaluated as a function of temperature, and the maximum ZT_elec and corresponding temperature are identified for each layer count. The workflow compares the performance of the hybrid and layered systems to provide a quantitative measure of their thermoelectric potential.

## Reproduction target
Produce two CSV files that contain the computed ZT_elec values.
1. hybrid_ZT.csv: contains ZT_elec for the SnSe-hBN and SnSe-CsPbI₃ hybrid superlattices at temperatures 100, 200, 300, …, 1000 K. Columns: `Temperature (K)`, `ZT_SnSe_hBN`, `ZT_SnSe_CsPbI3`. Each ZT cell is a floating-point number.
2. layered_ZT.csv: contains the maximum ZT_elec and the temperature at which it occurs for monolayer, bilayer, three-layer, and four-layer CsPbI₃. Columns: `Layer` (one of 'monolayer', 'bilayer', 'three-layer', 'four-layer'), `Temperature_K` (temperature of maximum ZT), `ZT_elec` (the maximum ZT value). Each row corresponds to one layer count.
The ZT_elec values must be calculated via the full DFT+BoltzTraP pipeline as described in the workflow steps, using the public crystal structures and the specified open-source codes.

## Assets

- Crystal structures of SnSe hybrids and CsPbI₃ layers: https://data.mendeley.com/datasets/py638t2nmg/1
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTraP: https://www.boltzTrap.org/
- SSSP pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Obtain crystal structures
- Role: process
- Action: Download CIF/input structure files for SnSe‑hBN, SnSe‑CsPbI₃, and layered CsPbI₃ (1–4 layers) from the Mendeley Data repository (doi:10.17632/py638t2nmg.1).
- Evidence: `/app/outputs/structures.json`

### Step 2: DFT relaxation of hybrid structures
- Role: process
- Action: Using Quantum ESPRESSO with PBE functional and van der Waals correction, relax the atomic positions of the SnSe‑hBN and SnSe‑CsPbI₃ hybrid superlattices until forces are below a suitable threshold.
- Evidence: `/app/outputs/relaxed_hybrids.out`

### Step 3: Band structure of hybrid systems
- Role: process
- Action: Perform non‑self‑consistent DFT calculations on each relaxed hybrid to obtain Kohn‑Sham eigenvalues on a fine k‑point grid suitable for transport calculations.
- Evidence: `/app/outputs/hybrids_bands.dat`

### Step 4: Transport calculation and ZT_elec for hybrids
- Role: scored (load-bearing)
- Action: Feed the DFT eigenvalues into BoltzTraP within the constant scattering time approximation and compute the temperature‑dependent transport coefficients. Use them to calculate ZT_elec = S²σT/κ₀ for temperatures 100, 200, …, 1000 K for both SnSe‑hBN and SnSe‑CsPbI₃. Write the results to `hybrid_ZT.csv`.
- Output file: `/app/outputs/hybrid_ZT.csv`
- Format: csv
- Contract: CSV with header: Temperature (K), ZT_SnSe_hBN, ZT_SnSe_CsPbI3. Ten rows for temperatures 100–1000 K in 100 K steps. Each ZT cell is a floating‑point number.
- Scoring: scored by hidden verifier

### Step 5: DFT relaxation of layered CsPbI₃
- Role: process
- Action: For each of the four layer counts (monolayer, bilayer, three‑layer, four‑layer), relax the atomic positions using the same DFT settings as for the hybrids.
- Evidence: `/app/outputs/relaxed_CsPbI3_layers.out`

### Step 6: Band structure of layered CsPbI₃
- Role: process
- Action: For each relaxed layer, compute the Kohn‑Sham eigenvalues on a dense k‑point grid suitable for BoltzTraP.
- Evidence: `/app/outputs/layered_CsPbI3_bands.dat`

### Step 7: Transport calculation and ZT_elec for layered CsPbI₃
- Role: scored (load-bearing)
- Action: Run BoltzTraP on the eigenvalues of each layer to obtain temperature‑dependent transport coefficients. Determine the maximum ZT_elec and the temperature at which it occurs for each layer (monolayer, bilayer, three‑layer, four‑layer). Write the results to `layered_ZT.csv`.
- Output file: `/app/outputs/layered_ZT.csv`
- Format: csv
- Contract: CSV with header: Layer, Temperature_K, ZT_elec. Four rows: 'monolayer', 'bilayer', 'three-layer', 'four-layer'. Temperature_K is the temperature (integer or float) at which maximum ZT occurs. ZT_elec is the maximum floating‑point value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hybrid_ZT.csv`
- `/app/outputs/layered_ZT.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hybrid_ZT.csv
- path: `/app/outputs/hybrid_ZT.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: ZT_elec values for the SnSe‑hBN and SnSe‑CsPbI₃ hybrids at temperatures 100–1000 K, as computed by DFT+BoltzTraP. The checker compares each value to the paper's Table 1 within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `Temperature (K)`, `ZT_SnSe_hBN`, `ZT_SnSe_CsPbI3`
  - `units`: object

### layered_ZT.csv
- path: `/app/outputs/layered_ZT.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Maximum ZT_elec and the corresponding temperature for monolayer, bilayer, three‑layer, and four‑layer CsPbI₃. The checker compares the reported values to those extracted from the paper's Figure 10 within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `Layer`, `Temperature_K`, `ZT_elec`
  - `units`: object

Notes: The scored artifacts are obtained from full DFT+BoltzTraP runs on the public crystal structures. The checker performs a result‑level comparison against the paper's reported values using absolute and relative tolerances that account for toolchain spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hybrid_ZT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature (K)",
          "ZT_SnSe_hBN",
          "ZT_SnSe_CsPbI3"
        ],
        "units": {}
      },
      "description": "ZT_elec values for the SnSe‑hBN and SnSe‑CsPbI₃ hybrids at temperatures 100–1000 K, as computed by DFT+BoltzTraP. The checker compares each value to the paper's Table 1 within tolerances."
    },
    {
      "file": "layered_ZT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Layer",
          "Temperature_K",
          "ZT_elec"
        ],
        "units": {}
      },
      "description": "Maximum ZT_elec and the corresponding temperature for monolayer, bilayer, three‑layer, and four‑layer CsPbI₃. The checker compares the reported values to those extracted from the paper's Figure 10 within tolerances."
    }
  ],
  "notes": "The scored artifacts are obtained from full DFT+BoltzTraP runs on the public crystal structures. The checker performs a result‑level comparison against the paper's reported values using absolute and relative tolerances that account for toolchain spread."
}
```

## How you are scored
Your submitted hybrid_ZT.csv and layered_ZT.csv will be checked by an automated verifier. The verifier compares each computed ZT_elec value, as well as the temperature for the maximum ZT in layered_ZT.csv, against a hidden reference expected from a correct execution of the method. Tolerances are applied to account for the expected spread across different computational setups. The hybrid_ZT.csv file contributes a set of checks (one for each temperature and system), and layered_ZT.csv contributes checks for each layer. The final score is a weighted sum of these individual checks, with each check successful if its value falls within the acceptable range. You must run the complete DFT+BoltzTraP pipeline; simply reporting numbers that coincidentally match the hidden reference will not suffice, as the verifier may also examine structural consistency across the outputs.
