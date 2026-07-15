# Magnetocrystalline Anisotropy Energy of Fe5PB2-based Alloys

## Problem background
Iron-based tetragonal compounds like Fe5PB2 are promising candidates for rare-earth-free permanent magnets because their uniaxial crystal structure can support strong magnetocrystalline anisotropy. The magnetocrystalline anisotropy energy (MAE) determines how difficult it is to reorient the magnetization away from the easy axis, making it a critical parameter for applications. Alloying Fe5PB2 with cobalt (Co) across the full concentration range, or doping it with small amounts of heavy 5d elements (such as W or Re), has been proposed as a route to tune the magnetic properties, but the quantitative effect on the MAE is not obvious because the electronic structure near the Fermi energy changes in a complex way. This task aims to reproduce first-principles calculations that predict the MAE for (Fe1−xCox)5PB2 alloys (x = 0 to 1) and for 5 % doped (Fe0.95X0.05)5PB2 with X = W and Re. The computed values will reveal whether Co substitution induces a systematic variation of the MAE and whether 5d doping can significantly alter it compared to undoped Fe5PB2.

## Approach
The computational approach uses density functional theory (DFT) within the generalized gradient approximation (PBE functional). The workflow consists of three stages. First, the crystal structures of the end-member compounds Fe5PB2 and Co5PB2 (both in space group I4/mcm) are optimized with spin‑polarized scalar‑relativistic calculations. Second, supercell models are constructed to represent the intermediate Co concentrations and the 5d‑doped systems: ordered arrangements of Fe and Co atoms are used for the alloys, while one Fe atom is replaced by W or Re for the doped compounds. Third, for each generated structure, fully relativistic spin‑polarized DFT calculations that explicitly include spin‑orbit coupling are performed with the magnetization oriented first along the [100] crystallographic direction and then along the [001] direction. The magnetocrystalline anisotropy energy is obtained as the total‑energy difference MAE = E[100] − E[001]. The result is a set of MAE values (in MJ/m³) that can be analyzed as a function of Co concentration and compared between the undoped and 5d‑doped cases.

## Reproduction target
Compute the magnetocrystalline anisotropy energy (MAE) for eight systems using the described fully relativistic DFT+SOC procedure:
- (Fe1−xCox)5PB2 with x = 0.0, 0.2, 0.4, 0.6, 0.8, and 1.0 (i.e., Fe5PB2 through Co5PB2)
- (Fe0.95X0.05)5PB2 with X = W and Re

Write the computed MAE values (in MJ/m³) to a CSV file at `/app/outputs/mae_summary.csv` with columns `system` (string) and `MAE_MJpm3` (float). Use the system names exactly as listed: Fe5PB2, Fe0.8Co0.2, Fe0.6Co0.4, Fe0.4Co0.6, Fe0.2Co0.8, Co5PB2, Fe0.95W0.05, Fe0.95Re0.05. The verifier will assess the MAE numbers against reference data and check that they follow a physically meaningful trend across the Co concentration series and that the 5d‑doped results show a consistent difference relative to undoped Fe5PB2. The exact sign and magnitude of the trend are part of the hidden evaluation criteria.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Python 3 with numpy: python3, numpy

## Workflow steps

### Step 1: Structure optimization of Fe5PB2 and Co5PB2
- Role: process
- Action: Perform spin-polarized scalar-relativistic DFT geometry optimization for Fe5PB2 and Co5PB2 using the PBE functional. Use experimental lattice parameters as starting point (Fe5PB2: a=5.492 Å, c=10.365 Å; Co5PB2: a=5.42 Å, c=10.20 Å; space group I4/mcm). Optimize lattice constants and internal positions. Save the optimized structures (e.g., as a JSON file containing lattice vectors and atomic coordinates).
- Evidence: `/app/outputs/optimized_structures.json`

### Step 2: Generate supercell structures for Co- and 5d-substituted systems
- Role: process
- Action: Based on the optimized terminal structures, construct supercell models for intermediate Co concentrations x=0.2, 0.4, 0.6, 0.8 (using ordered Fe/Co arrangements) and for (Fe0.95X0.05)5PB2 with X=W, Re (by replacing one Fe atom in the unit cell). Include the terminal compositions x=0.0 and 1.0 as well. Save a list of atomic structures for all target compositions (e.g., as a JSON or CIF file).
- Evidence: `/app/outputs/supercell_structures.json`

### Step 3: Compute MAE via fully relativistic DFT+SOC
- Role: scored (load-bearing)
- Action: For each structure (Fe5PB2, (Fe1-xCox)5PB2 at x=0.2,0.4,0.6,0.8,1.0, and (Fe0.95X0.05)5PB2 with X=W,Re), perform fully relativistic DFT calculations including spin-orbit coupling with the magnetization oriented along the [100] and [001] axes. Use appropriately converged k-point meshes and energy cutoffs, consistent with the chosen pseudopotentials. Compute MAE = E[100] - E[001] (in MJ/m³). Write the results to mae_summary.csv.
- Output file: `/app/outputs/mae_summary.csv`
- Format: csv
- Contract: Columns: system (string), MAE_MJpm3 (float). System names: Fe5PB2, Fe0.8Co0.2, Fe0.6Co0.4, Fe0.4Co0.6, Fe0.2Co0.8, Co5PB2, Fe0.95W0.05, Fe0.95Re0.05.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mae_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mae_summary.csv
- path: `/app/outputs/mae_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: MAE values for each composition. The checker compares these to hidden reference values and verifies the monotonic decrease of MAE with increasing Co content.
- schema:
  - `type`: table
  - `required_columns`: `system`, `MAE_MJpm3`
  - `units`:
    - `MAE_MJpm3`: MJ/m³

Notes: The hidden checker uses a tolerance around the paper-reported MAE values and checks that successive MAE values for x=0.0..1.0 are non-increasing. The 5d-doped entries (W, Re) must exceed the undoped baseline.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mae_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "MAE_MJpm3"
        ],
        "units": {
          "MAE_MJpm3": "MJ/m³"
        }
      },
      "description": "MAE values for each composition. The checker compares these to hidden reference values and verifies the monotonic decrease of MAE with increasing Co content."
    }
  ],
  "notes": "The hidden checker uses a tolerance around the paper-reported MAE values and checks that successive MAE values for x=0.0..1.0 are non-increasing. The 5d-doped entries (W, Re) must exceed the undoped baseline."
}
```

## How you are scored
An automated hidden verifier will read your output file `mae_summary.csv` and compare the submitted MAE values to a set of reference values obtained from an equivalent calculation, allowing for a tolerance that accounts for legitimate differences between DFT codes and pseudopotential implementations. In addition, the verifier will examine the relative behavior across compositions: it will check whether the MAE exhibits a systematic, monotonic change with increasing Co content (either increasing or decreasing) and whether the 5d‑doped entries show a consistent deviation from the undoped baseline. Your overall reward is based on how well your reported numbers satisfy these hidden checks. Note that simply copying a pre‑known answer, including the numbers reported in the published literature, is not sufficient — you must actually perform the DFT calculations to generate a physically consistent set of results. Only artifacts produced by the described workflow will receive credit.
