## Problem background

Germanane is a two-dimensional hydrogenated germanene nanosheet exhibiting a semiconducting band gap, making it a candidate for chemical sensing applications. Understanding how the adsorption of volatile organic molecules, particularly alcohols and aldehydes, modifies the electronic structure of germanane is essential for assessing its sensor performance. This task investigates the change in band gap and adsorption strength when a series of aldehyde (formaldehyde, acetaldehyde, propionaldehyde) and alcohol (methanol, ethanol, 1-propanol) molecules adsorb on a germanane surface.

## Approach

Use density functional theory (DFT) as implemented in the SIESTA package with the generalized gradient approximation (GGA) and the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional. Construct a 5×5 supercell of hydrogenated germanene (germanane) with the buckled structure. First, fully relax the geometry of the pristine germanane sheet. Then, for each of the six adsorbates, place the molecule on the relaxed germanane surface, perform full geometry optimization, and compute:
- The adsorption energy including basis set superposition error (BSSE) correction.
- Mulliken and Atoms-in-Molecules (AIM) charge transfer.
- The band structure, from which the band gap is extracted.

Also compute the band gap of the isolated relaxed germanane. Collect all computed quantities into a CSV file and verify that alcohol adsorption induces a larger reduction of the band gap than aldehyde adsorption.

## Reproduction target

Produce a single CSV file, `/app/outputs/adsorption_results.csv`, containing rows for the isolated germanane and for each of the six adsorbate systems. The file must include the band gap (eV) and adsorption energy (eV) for every system, as well as the Mulliken and AIM charge transfer and the average energy gap variation (%). The hidden verifier will compare the computed band gap and adsorption energy values to reference criteria and verify that the band gaps of the alcohol-adsorbed systems are lower than those of the aldehyde-adsorbed systems and that all are lower than the isolated germanane band gap. No intermediate figures or band structure plots are required; only the numeric CSV is scored.

## Assets

- **SIESTA DFT package** – open-source first-principles code (https://departments.icmab.es/leem/siesta/). Standard norm-conserving pseudopotentials and basis sets are publicly available. No other external data or models are needed; all structural inputs are constructed from standard bulk crystal parameters.

## Workflow steps

### Step 0: Geometry Relaxation of Germanane
- Role: process
- Action: Construct a 5×5×1 supercell of hydrogenated germanene (germanane) with the buckled structure (Ge–H bond length ≈ 1.56 Å, Ge–Ge ≈ 2.47 Å). Perform full geometry relaxation using SIESTA with GGA/PBE and a double-zeta polarized (DZP) basis set until forces are converged. The relaxed geometry will be used in subsequent steps.
- Evidence: `/app/outputs/germanane_relaxed.xyz`

### Step 1: Adsorption Calculations and Band Structure Analysis (load-bearing)
- Role: scored (load-bearing)
- Action: Take the relaxed germanane slab from Step 0. For each of the six adsorbates—formaldehyde, acetaldehyde, propionaldehyde (aldehyde group) and methanol, ethanol, 1-propanol (alcohol group)—build the adsorbed system, fully optimize the combined geometry, and compute:
  * Adsorption energy with BSSE correction.
  * Mulliken and AIM charge transfer.
  * Band structure and the corresponding band gap.
Also compute the band gap of the isolated relaxed germanane. Calculate the average energy gap variation (in percent) relative to the isolated germanane band gap for each adsorbed system. Compile all results into the CSV file described below.
- Output file: `/app/outputs/adsorption_results.csv`
- Format: csv
- Contract: A table with exactly 7 rows (1 isolated germanane row and 6 adsorbate rows) and the following columns:
  * `system` (string): identifier, e.g., "Ge_isolated", "A1" (formaldehyde), "A2" (acetaldehyde), "A3" (propionaldehyde), "B1" (methanol), "B2" (ethanol), "B3" (1-propanol).
  * `band_gap_eV` (float): band gap in eV.
  * `adsorption_energy_eV` (float): adsorption energy in eV; for the isolated row this cell must be empty or NaN.
  * `mulliken_charge_e` (float): Mulliken charge transfer in e; empty/NaN for isolated row.
  * `aim_charge_e` (float): AIM charge transfer in e; empty/NaN for isolated row.
  * `average_energy_gap_variation_percent` (float): average energy gap variation in %; empty/NaN for isolated row.
- Scoring: scored by hidden verifier

## Output files

All artifacts must be placed under `/app/outputs`:
- `germanane_relaxed.xyz` – relaxed geometry from Step 0 (evidence).
- `adsorption_results.csv` – the final CSV file with all computed quantities (scored).

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_results.csv
- path: `/app/outputs/adsorption_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Tabular file with computed properties for isolated germanane and six adsorption systems. The hidden verifier checks band gap and adsorption energy values within tolerances and verifies the trend that alcohol band gaps < aldehyde band gaps < isolated band gap.
- schema:
  - `type`: table
  - `required_columns`: `system`, `band_gap_eV`, `adsorption_energy_eV`, `mulliken_charge_e`, `aim_charge_e`, `average_energy_gap_variation_percent`
  - `units`:
    - `band_gap_eV`: eV
    - `adsorption_energy_eV`: eV
    - `mulliken_charge_e`: e
    - `aim_charge_e`: e
    - `average_energy_gap_variation_percent`: %

Notes: The isolated germanane row has empty/NaN for adsorption_energy_eV, mulliken_charge_e, aim_charge_e, and average_energy_gap_variation_percent. The verifier additionally validates that the band_gap_eV values for B1, B2, B3 are all lower than those for A1, A2, A3, and that all adsorbed band gaps are lower than the isolated germanane band gap.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "band_gap_eV",
          "adsorption_energy_eV",
          "mulliken_charge_e",
          "aim_charge_e",
          "average_energy_gap_variation_percent"
        ],
        "units": {
          "band_gap_eV": "eV",
          "adsorption_energy_eV": "eV",
          "mulliken_charge_e": "e",
          "aim_charge_e": "e",
          "average_energy_gap_variation_percent": "%"
        }
      },
      "description": "Tabular file with computed properties for isolated germanane and six adsorption systems. The hidden verifier checks band gap and adsorption energy values within tolerances and verifies the trend that alcohol band gaps < aldehyde band gaps < isolated band gap."
    }
  ],
  "notes": "The isolated germanane row has empty/NaN for adsorption_energy_eV, mulliken_charge_e, aim_charge_e, and average_energy_gap_variation_percent. The verifier additionally validates that the band_gap_eV values for B1, B2, B3 are all lower than those for A1, A2, A3, and that all adsorbed band gaps are lower than the isolated germanane band gap."
}
```

## How you are scored

A hidden verifier reads your `adsorption_results.csv` and compares the `band_gap_eV` and `adsorption_energy_eV` columns to reference criteria using appropriate tolerances. It also verifies the structural trend: the band gaps for the alcohol-adsorbed rows (B1, B2, B3) must be lower than those of the aldehyde-adsorbed rows (A1, A2, A3), and all must be lower than the isolated germanane band gap. The score is based on how many values fall within the allowed ranges and whether the required trend is satisfied. Reporting a number without the underlying computation will not earn credit.
