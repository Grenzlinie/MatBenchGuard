# MD simulation of cylindrical nanoindentation on graphene: extract tensile strengths and test offset insensitivity

## Problem background
Measuring the uniaxial tensile strength of graphene is challenging because clamping atomically thin sheets is difficult. Nanoindentation using a spherical tip has been widely used, but it generates a highly concentrated stress field that can overestimate strength and make the measurement sensitive to the indentation site. This work explores cylindrical nanoindentation as an alternative: a rigid cylindrical indenter produces a uniform in-plane stress distribution similar to that of uniaxial tension, potentially enabling a direct mapping of the measured fracture force to the uniaxial tensile strength. The task investigates whether cylindrical indentation can reliably extract the tensile strength of pristine graphene (zigzag and armchair orientations) and of polycrystalline graphene containing symmetric tilt grain boundaries, and whether the estimated strength for a grain boundary is robust to lateral offset between the indenter axis and the boundary line.

## Approach
Molecular dynamics simulations are performed using LAMMPS with the AIREBO interatomic potential to describe carbon–carbon interactions. Atomic models of graphene sheets (approximately 50 nm × 50 nm) are built: pristine sheets with zigzag and armchair orientations, and bicrystalline sheets containing symmetric tilt grain boundaries (two misorientation angles) centred in the sample. After equilibration at 300 K (NPT followed by NVT), each sample is subjected to virtual cylindrical nanoindentation. A rigid cylindrical indenter of radius 50 Å with a repulsive force constant of 10 eV/Å³ is pressed downward at 0.02 Å/ps. The edges of the sheet are clamped, and a periodic boundary condition is applied along the indenter axis. For one grain-boundary case, additional simulations are run with the indenter axis shifted laterally by 40 Å and 80 Å from the boundary line. From the force–displacement curve of each run, the maximum force (failure force) is recorded and converted to an estimated uniaxial tensile strength using the maximum virial stress at fracture, as described in the underlying study. The estimated strengths are then compared between pristine orientations and between grain-boundary angles, and the scatter of the failure force with lateral offset is examined.

## Reproduction target
Compute and report, in a CSV file, the estimated uniaxial tensile strengths (in GPa) obtained by cylindrical nanoindentation for:

* Pristine graphene with zigzag and armchair orientations.
* Polycrystalline graphene containing symmetric tilt grain boundaries with two different misorientation angles (e.g., 5.7° and 27.8°), indented with the indenter axis aligned on the grain-boundary line.
* For the lower-angle grain boundary, additional runs with the indenter axis laterally offset by 40 Å and 80 Å from the boundary line, to assess the sensitivity of the failure force.

The CSV must contain columns: case (identifier), tilt_angle (degrees, NaN for pristine), offset_S (Å, NaN when no offset is applied), failure_force (nN), and estimated_strength (GPa).

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- AIREBO interatomic potential: https://lammps.sandia.gov/doc/airebo.html

## Workflow steps

### Step 1: Build graphene atomic models
- Role: process
- Action: Generate initial atomic coordinates for pristine graphene sheets (zigzag and armchair orientations, ~50 nm × 50 nm) and for bicrystalline graphene sheets containing symmetric tilt grain boundaries (misorientation angles 5.7° and 27.8°, zigzag-oriented) with the GB line centered.
- Evidence: `/app/outputs/build_models.log`

### Step 2: Equilibrate samples
- Role: process
- Action: Equilibrate each atomic structure at 300 K using the AIREBO potential with a 1.0 fs timestep: first an NPT ensemble for 20 ps, then an NVT ensemble for 10 ps.
- Evidence: `/app/outputs/equilibration.log`

### Step 3: Cylindrical nanoindentation simulations and strength extraction
- Role: scored (load-bearing)
- Action: For each equilibrated sample, perform virtual cylindrical nanoindentation: apply a rigid cylindrical indenter (radius 50 Å, force constant 10 eV/Å³) moving downward at 0.02 Å/ps, with clamped edges and periodic boundary along the indenter axis (except for offset tests where periodic BC is retained but indenter offset is applied). Run pristine zigzag, pristine armchair, GB_5.7° (indenter centered on GB line, S=0, and at lateral offsets S=40 Å and S=80 Å), and GB_27.8° (S=0). Record the maximum force (failure force) from each force–displacement curve. Convert the failure force to estimated uniaxial tensile strength using the stress–force relationship (maximum virial stress at fracture) as described in the paper. Output a CSV file with results for all cases.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: case (string, e.g., pristine_zigzag, pristine_armchair, GB_5.7deg, GB_27.8deg, GB_5.7deg_offset40, GB_5.7deg_offset80), tilt_angle (degrees, NaN for pristine), offset_S (Å, NaN if not offset test), failure_force (nN), estimated_strength (GPa).
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
- target_policy: exact_match
- description: Table containing cylindrical indentation results: case identifier, tilt angle in degrees (NaN for pristine), lateral offset in Å (NaN for non-offset tests), failure force in nN, and estimated tensile strength in GPa. Includes rows for pristine, grain-boundary centered, offset, and angular misalignment tests. The hidden checker will compare the reported strengths to reference values with tolerance, verify the correct ordering of GB strengths, check that the failure force spread for offset tests is ≤10%, and check that the estimated strengths for angular misalignment tests are within 15% of the aligned case.
- schema:
  - `type`: table
  - `required_columns`: `case`, `tilt_angle`, `offset_S`, `failure_force`, `estimated_strength`
  - `units`:
    - `failure_force`: nN
    - `estimated_strength`: GPa

Notes: The results.csv must contain rows for all specified cases including angular misalignment tests. The hidden checker performs multiple checks on this single file.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "tilt_angle",
          "offset_S",
          "failure_force",
          "estimated_strength"
        ],
        "units": {
          "failure_force": "nN",
          "estimated_strength": "GPa"
        }
      },
      "description": "Table containing cylindrical indentation results: case identifier, tilt angle in degrees (NaN for pristine), lateral offset in Å (NaN for non-offset tests), failure force in nN, and estimated tensile strength in GPa. Includes rows for pristine, grain-boundary centered, offset, and angular misalignment tests. The hidden checker will compare the reported strengths to reference values with tolerance, verify the correct ordering of GB strengths, check that the failure force spread for offset tests is ≤10%, and check that the estimated strengths for angular misalignment tests are within 15% of the aligned case."
    }
  ],
  "notes": "The results.csv must contain rows for all specified cases including angular misalignment tests. The hidden checker performs multiple checks on this single file."
}
```

## How you are scored
A hidden verifier will read your results.csv and perform the following checks, each contributing to the final score:

1. **Pristine strengths** – Your estimated strengths for zigzag and armchair pristine graphene are compared to hidden reference values (with a tolerance that accounts for run-to-run and implementation variation).
2. **Grain-boundary ordering** – The verifier checks whether the estimated strength for the lower-angle grain boundary is lower than that for the higher-angle grain boundary.
3. **Offset insensitivity** – For the three offset tests (S = 0, 40, 80 Å) of the lower-angle grain boundary, the relative spread of the reported failure forces (max–min divided by mean) is computed and must be ≤10%.

The final score is a weighted combination of these checks. You must run the full MD workflow; the verifier only inspects the CSV, but manual review may consider the presence of supporting evidence.
