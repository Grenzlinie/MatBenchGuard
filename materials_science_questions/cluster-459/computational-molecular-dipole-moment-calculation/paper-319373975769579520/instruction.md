# Dipole Moments of Organotin Donor-Acceptor Complexes by Quantum Chemistry

## Problem background
Phenyltin trichloride (C6H5SnCl3) can potentially form 1:2 donor‑acceptor complexes with small O‑donor molecules such as methanol, ethanol, and tetrahydrofuran. The electronic structure and polarity of these complexes are of interest for understanding the coordination chemistry of organotin chlorides. This task computes the total dipole moment magnitude for each of the three 1:2 complexes using quantum chemical methods, providing a computational counterpart to experimental measurements.

## Approach
Use quantum chemical density functional theory calculations to obtain the ground‑state geometry and electronic dipole moment of each complex in isolation. First, construct initial 3D structures of the three complexes; then perform a full geometry optimization and, at the converged structure, compute the dipole moment from the wavefunction. Because tin is a heavy element, a relativistic effective core potential and a suitable basis set are required. The choice of the specific density functional and basis set is left to the solver, who should aim for a chemically accurate description. Finally, extract the total dipole moment magnitude (in Debye) and compile the results into the required output file.

## Reproduction target
Write a CSV file `step_01_complex_dipoles.csv` with exactly two columns: `complex` (string) and `dipole_moment_D` (float, in Debye). The file must contain one row for each of these three complexes: C6H5SnCl3·2CH3OH, C6H5SnCl3·2C2H5OH, C6H5SnCl3·2C4H8O. The hidden verifier will independently compare the reported dipole moments to the expected values from the original experimental study; meeting or exceeding the accuracy expectation earns full credit.

## Assets

- Psi4 quantum chemistry package: psi4
- Open Babel molecular builder: openbabel-wheel
- Basis sets for Sn and light elements: https://www.basissetexchange.org/

## Workflow steps

### Step 1: Generate initial molecular geometries
- Role: process
- Action: Construct plausible initial 3D structures for the three 1:2 donor-acceptor complexes (phenyltin trichloride with methanol, ethanol, and tetrahydrofuran) using a molecular builder or systematic approach. Save each complex as an XYZ or SDF file.
- Evidence: `/app/outputs/complex_geometries.zip`

### Step 2: Compute dipole moments of complexes
- Role: scored (load-bearing)
- Action: Perform geometry optimization and dipole moment calculation for each complex using a quantum chemistry package. Extract the total dipole moment magnitude (in Debye) from the converged calculation. Write the results to step_01_complex_dipoles.csv.
- Output file: `/app/outputs/step_01_complex_dipoles.csv`
- Format: csv
- Contract: complex (str), dipole_moment_D (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_complex_dipoles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_complex_dipoles.csv
- path: `/app/outputs/step_01_complex_dipoles.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed total dipole moment in Debye for the three 1:2 donor-acceptor complexes of phenyltin trichloride. The agent reports the magnitude and the checker compares it to hidden reference values with a tolerance; meeting or beating the reference earns full credit.
- schema:
  - `type`: table
  - `required_columns`: `complex`, `dipole_moment_D`
  - `units`:
    - `dipole_moment_D`: Debye

Notes: The CSV must contain rows for the three named complexes. The checker will extract the dipole moment for each complex and compare to hidden gold values. No other intermediate data files are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_complex_dipoles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex",
          "dipole_moment_D"
        ],
        "units": {
          "dipole_moment_D": "Debye"
        }
      },
      "description": "Computed total dipole moment in Debye for the three 1:2 donor-acceptor complexes of phenyltin trichloride. The agent reports the magnitude and the checker compares it to hidden reference values with a tolerance; meeting or beating the reference earns full credit."
    }
  ],
  "notes": "The CSV must contain rows for the three named complexes. The checker will extract the dipole moment for each complex and compare to hidden gold values. No other intermediate data files are scored."
}
```

## How you are scored
A hidden checker reads your `step_01_complex_dipoles.csv`. It first validates that the file contains the required columns and exactly the three named complexes. For each complex, the checker compares your reported dipole moment to a hidden experimental reference value using an appropriate tolerance that accounts for differences between computational and experimental methods. The comparison uses a threshold‑or‑better policy: if your computed dipole moment is within the tolerance of the reference (or more accurate, i.e., a smaller absolute difference), you earn full credit for that complex; otherwise, credit decreases as the absolute difference grows. The three complexes are weighted equally. The checker does not penalize results that are closer to the reference than the original experiment; it only penalizes results that deviate further than the tolerance. No prior knowledge of the reference values is needed to solve the task.
