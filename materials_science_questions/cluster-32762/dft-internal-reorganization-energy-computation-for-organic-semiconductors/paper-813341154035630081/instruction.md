# DFT Reorganization Energy of Pentacene Dimer via Constrained DFT

## Problem background
In organic semiconductors, charge transport often occurs via thermally activated hopping of localized polarons. The reorganization energy λ is a central parameter that determines hopping rates. Standard density functional theory (DFT) with semilocal exchange-correlation functionals suffers from self-interaction error that artificially delocalizes charge, preventing a correct description of localized polarons in molecular dimers. Constrained DFT (CDFT) addresses this by imposing a charge difference between donor and acceptor molecules, enabling the study of polaronic states and the calculation of reorganization energies.

## Approach
The method uses constrained DFT with a Löwdin charge constraint and the PBE-D exchange-correlation functional, combined with ultrasoft pseudopotentials (or equivalent open-source implementations) to compute the electronic structure of a cofacially stacked pentacene dimer. First, the geometries of a neutral pentacene molecule and its monocation are optimized. Then, dimers are constructed at intermolecular distances of 4 Å, 5 Å, and 7 Å by stacking the two geometries. For each dimer, a series of CDFT calculations is performed, scanning the imposed charge difference N_c to find the value that correctly localizes a positive charge on the cation molecule (typically around 1.3 e). At that N_c, the energies of the two localized charge states are computed, and the frozen reorganization energy is evaluated as the energy difference between them. Subsequently, the dimer geometry is relaxed under the same CDFT constraint while keeping the intermolecular distance fixed, capturing the structural response of the neutral molecule to the charged neighbor. Finally, the reorganization energy is recomputed at the relaxed geometry to obtain the relaxed reorganization energy. The primary measurable outcome is the reorganization energy as a function of intermolecular separation, reflecting the combined effects of electronic polarization and geometric relaxation.

## Reproduction target
Compute the reorganization energy λ for the pentacene dimer at intermolecular distances of 4 Å, 5 Å, and 7 Å. For each distance, report two values: λ_frozen (obtained from the fixed isolated-molecule geometries) and λ_relaxed (obtained after geometry relaxation under the CDFT constraint with fixed intermolecular separation). The results must be written to `/app/outputs/reorganization_energies.csv` with columns: distance (float, Å), lambda_frozen (float, Hartree), lambda_relaxed (float, Hartree). The CSV file must contain one row for each of the three distances.

## Assets

- CP2K (open-source DFT code with CDFT support): https://www.cp2k.org

## Workflow steps

### Step 1: Isolated pentacene geometry optimization
- Role: process
- Action: Perform DFT geometry optimization of neutral pentacene molecule (C22H14) and its monocation (C22H14+) using the PBE-D functional and ultrasoft pseudopotentials. Converge the plane-wave cutoff and supercell size to obtain relaxed atomic coordinates.
- Evidence: `/app/outputs/optimized_structures.xyz`

### Step 2: Construction of pentacene dimer structures
- Role: process
- Action: Stack the optimized neutral and cation pentacene molecules cofacially (parallel molecular planes) at intermolecular distances of 4 Å, 5 Å, and 7 Å along the axis perpendicular to the molecular planes. Produce coordinate files for each distance.
- Evidence: `/app/outputs/dimers_initial.xyz`

### Step 3: Frozen-dimer CDFT analysis and frozen reorganization energy
- Role: process
- Action: For each dimer distance, run constrained DFT calculations with Löwdin charge constraint to localize a +1 charge on the cation molecule. Scan the imposed charge difference N_c to find the value (around 1.3e) that yields correct charge localization (spin density concentrated on the cation molecule). Using that N_c, compute the energies of the two charge states (charge on the cation vs. on the neutral molecule) and evaluate the frozen reorganization energy: lambda_frozen = E(-N_c) - E(N_c). Record the chosen N_c and lambda_frozen for each distance.
- Evidence: `/app/outputs/frozen_cdft_scan.csv`

### Step 4: Geometry relaxation of dimers under CDFT constraint
- Role: process
- Action: For each dimer distance, using the N_c value found in step 3, relax the atomic positions via geometry optimization or simulated annealing while keeping the intermolecular distance fixed (e.g., by constraining selected atoms). Use the CDFT Löwdin constraint with the same functional and pseudopotentials. Produce relaxed coordinate files for each distance.
- Evidence: `/app/outputs/relaxed_geometries.xyz`

### Step 5: Reorganization energy evaluation for frozen and relaxed dimers
- Role: scored (load-bearing)
- Action: For each relaxed dimer geometry, compute the energy E(N_c) and E(-N_c) using the same CDFT protocol and calculate the relaxed reorganization energy lambda_relaxed = E(-N_c) - E(N_c). Combine the frozen lambda (from step 3) and relaxed lambda for all three distances into a CSV file.
- Output file: `/app/outputs/reorganization_energies.csv`
- Format: csv
- Contract: Columns: distance (float, Angstrom), lambda_frozen (float, Hartree), lambda_relaxed (float, Hartree). Three rows corresponding to distances 4, 5, 7 Å.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reorganization_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reorganization_energies.csv
- path: `/app/outputs/reorganization_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed reorganization energies of pentacene dimer at distances 4, 5, and 7 Å for both frozen (from isolated geometries) and relaxed (after CDFT geometry relaxation) configurations.
- schema:
  - `type`: table
  - `required_columns`: `distance`, `lambda_frozen`, `lambda_relaxed`
  - `units`:
    - `distance`: Angstrom
    - `lambda_frozen`: Hartree
    - `lambda_relaxed`: Hartree
  - `expected_rows`: 3
  - `notes`: Rows correspond to intermolecular distances of 4, 5, and 7 Å.

Notes: The agent must use an open-source DFT code with constrained DFT capabilities (e.g., CP2K) to perform the calculations. The scored artifact is compared to hidden reference values with a tolerance and must exhibit monotonic trend: lambda_relaxed > lambda_frozen for each distance, and both lambda values increase as distance decreases.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reorganization_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance",
          "lambda_frozen",
          "lambda_relaxed"
        ],
        "units": {
          "distance": "Angstrom",
          "lambda_frozen": "Hartree",
          "lambda_relaxed": "Hartree"
        },
        "expected_rows": 3,
        "notes": "Rows correspond to intermolecular distances of 4, 5, and 7 Å."
      },
      "description": "Computed reorganization energies of pentacene dimer at distances 4, 5, and 7 Å for both frozen (from isolated geometries) and relaxed (after CDFT geometry relaxation) configurations."
    }
  ],
  "notes": "The agent must use an open-source DFT code with constrained DFT capabilities (e.g., CP2K) to perform the calculations. The scored artifact is compared to hidden reference values with a tolerance and must exhibit monotonic trend: lambda_relaxed > lambda_frozen for each distance, and both lambda values increase as distance decreases."
}
```

## How you are scored
The hidden verifier evaluates your submitted `reorganization_energies.csv`. It compares your λ_frozen and λ_relaxed values against reference values using a tolerance appropriate for DFT calculations with different implementations and pseudopotentials. In addition, it checks that the data satisfy two physical trends: (1) for each distance, λ_relaxed > λ_frozen, and (2) both λ_frozen and λ_relaxed increase monotonically as the intermolecular distance decreases (i.e., λ(7 Å) < λ(5 Å) < λ(4 Å)). Full credit requires all values within tolerance and the correct monotonic behavior; partial credit is given if some values are correct but the trends are partially met. The verifier does not require the original paper's numerical values to be known; it compares against a hidden reference and structural expectations.
