# Molecular dynamics simulation of γ→α′ transformation rates at fault band intersections

## Problem background
In many ferrous austenitic alloys, deformation‑induced phase transformations are believed to govern the mechanical properties. A central idea is that the nucleation of bcc-α′ martensite occurs at specific intersections of stacking‑fault arrangements, in particular between a perfect hcp‑ε martensite band (stacking faults on every second {111} plane) and a faulted ε band (stacking faults on every third {111} plane). It is an open question whether this exact combination of fault types is uniquely required for rapid transformation, or whether other intersection geometries can also produce fast nucleation, and how the transformation rate depends on the size of the intersection volume. This task uses molecular dynamics simulations to compute and compare the evolution of bcc volume fraction over time for different stacking‑fault intersection configurations.

## Approach
The approach uses classical molecular dynamics with an embedded‑atom method (EAM) potential for iron. A simulation cell of fcc‑Fe is constructed with crystallographic orientations such that stacking faults can be introduced on {111} planes, mimicking the ε‑martensite and faulted ε bands described in the problem. Several distinct intersection configurations are built: one where a perfect ε band (stacking faults on every second plane) crosses a faulted ε band containing a fixed number of stacking faults, one where two perfect ε bands cross, and variants where the faulted ε band contains 1, 2, 4, and 8 stacking faults to vary the intersection volume. For each configuration, an NVT molecular dynamics simulation is run at low temperature to allow the transformation to proceed. From the saved atomic trajectories, the fraction of atoms with a coordination number characteristic of bcc (8 nearest‑neighbor atoms) is computed at each time step. The resulting time series quantify the kinetics of the γ→α′ transformation and allow a direct comparison between the different intersection types and volumes.

## Reproduction target
Reproduce the transformation kinetics for the small simulation cell described above by:
- Constructing the required stacking‑fault configurations (perfect ε band intersecting a faulted ε band with 4 stacking faults, and two intersecting perfect ε bands, plus faulted ε bands with 1, 2, 4, and 8 stacking faults intersecting a perfect ε band).
- Running LAMMPS with the Ackland EAM Fe potential in the NVT ensemble at 50 K with a 1 fs time step for 50 ps, recording atom positions and types every 1 ps.
- Computing for each trajectory the fraction of bcc‑coordinated atoms (coordination number 8) at every stored time step.
- Saving the results as three CSV files under `/app/outputs`:
  1. `olson_cohen_bcc_fraction.csv` – bcc fraction vs. time for the Olson‑Cohen intersection (4 stacking faults in the faulted band).
  2. `perfect_perfect_bcc_fraction.csv` – bcc fraction vs. time for the intersection of two perfect ε bands.
  3. `volume_dependence_bcc_fraction.csv` – bcc fraction vs. time for the four intersection volumes (1, 2, 4, and 8 stacking faults), combined into a single file with a `volume` column.

The goal is to produce these time series as described; the evaluation will check that the curves exhibit physically meaningful structural relationships.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- Ackland EAM Fe potential: https://www.ctcms.nist.gov/potentials/Fe.html

## Workflow steps

### Step 1: Generate atomic configurations
- Role: process
- Action: Create LAMMPS data files for the small simulation cell (10.7 x 9.2 x 1.2 nm, ~10835 atoms) of fcc-Fe with orientations x=[0-11], y=[-100], z=[011]. Introduce stacking faults to construct: (a) a perfect ε band intersecting a faulted ε band with 1, 2, 4, and 8 stacking faults; (b) two intersecting perfect ε bands. Apply periodic boundary conditions in z and fix x,y. Write a summary file listing the generated configurations.
- Evidence: `/app/outputs/configurations_summary.txt`

### Step 2: Run MD simulations
- Role: process
- Action: For each configuration from step_configs, run LAMMPS using the Ackland EAM potential in the NVT ensemble at 50 K with a 1 fs timestep for 50 ps. Dump atomic positions and types every 1 ps. Use periodic boundary condition in z and fix x,y. Record simulation completion.
- Evidence: `/app/outputs/md_complete.txt`

### Step 3: Olson‑Cohen intersection bcc fraction
- Role: scored (load-bearing)
- Action: From the trajectory of the Olson‑Cohen geometry (perfect ε band intersecting faulted ε band with 4 stacking faults), compute for each saved timestep the fraction of atoms with coordination number 8 (bcc) using a suitable cutoff, and output a CSV with columns time_ps and bcc_fraction.
- Output file: `/app/outputs/olson_cohen_bcc_fraction.csv`
- Format: csv
- Contract: column1: time_ps (float, ps); column2: bcc_fraction (float, 0-1)
- Scoring: scored by hidden verifier

### Step 4: Perfect‑perfect intersection bcc fraction
- Role: scored (load-bearing)
- Action: From the trajectory of two intersecting perfect ε bands, compute the fraction of bcc-coordinated atoms over time and output a CSV with columns time_ps and bcc_fraction.
- Output file: `/app/outputs/perfect_perfect_bcc_fraction.csv`
- Format: csv
- Contract: column1: time_ps (float, ps); column2: bcc_fraction (float, 0-1)
- Scoring: scored by hidden verifier

### Step 5: Volume dependence of transformation
- Role: scored (load-bearing)
- Action: For the four simulations where the faulted ε band contains 1, 2, 4, and 8 stacking faults intersecting a perfect ε band, compute the bcc fraction over time from each trajectory. Concatenate into a single CSV with columns volume (int), time_ps (float), bcc_fraction (float).
- Output file: `/app/outputs/volume_dependence_bcc_fraction.csv`
- Format: csv
- Contract: column1: volume (int); column2: time_ps (float); column3: bcc_fraction (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/olson_cohen_bcc_fraction.csv`
- `/app/outputs/perfect_perfect_bcc_fraction.csv`
- `/app/outputs/volume_dependence_bcc_fraction.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### olson_cohen_bcc_fraction.csv
- path: `/app/outputs/olson_cohen_bcc_fraction.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time series of bcc fraction for the Olson‑Cohen intersection geometry.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `bcc_fraction`
  - `units`:
    - `time_ps`: picosecond
    - `bcc_fraction`: dimensionless

### perfect_perfect_bcc_fraction.csv
- path: `/app/outputs/perfect_perfect_bcc_fraction.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time series of bcc fraction for the intersection of two perfect ε bands.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `bcc_fraction`
  - `units`:
    - `time_ps`: picosecond
    - `bcc_fraction`: dimensionless

### volume_dependence_bcc_fraction.csv
- path: `/app/outputs/volume_dependence_bcc_fraction.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Volume dependence data: bcc fraction vs time for four different intersection volumes.
- schema:
  - `type`: table
  - `required_columns`: `volume`, `time_ps`, `bcc_fraction`
  - `units`:
    - `volume`: number of stacking faults
    - `time_ps`: picosecond
    - `bcc_fraction`: dimensionless

Notes: Checker will verify structural trends and threshold criteria derived from the paper's claims: comparison of bcc fractions at t=30 ps for the two intersection types and monotonic increase with volume.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "olson_cohen_bcc_fraction.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "bcc_fraction"
        ],
        "units": {
          "time_ps": "picosecond",
          "bcc_fraction": "dimensionless"
        }
      },
      "description": "Time series of bcc fraction for the Olson‑Cohen intersection geometry."
    },
    {
      "file": "perfect_perfect_bcc_fraction.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "bcc_fraction"
        ],
        "units": {
          "time_ps": "picosecond",
          "bcc_fraction": "dimensionless"
        }
      },
      "description": "Time series of bcc fraction for the intersection of two perfect ε bands."
    },
    {
      "file": "volume_dependence_bcc_fraction.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "volume",
          "time_ps",
          "bcc_fraction"
        ],
        "units": {
          "volume": "number of stacking faults",
          "time_ps": "picosecond",
          "bcc_fraction": "dimensionless"
        }
      },
      "description": "Volume dependence data: bcc fraction vs time for four different intersection volumes."
    }
  ],
  "notes": "Checker will verify structural trends and threshold criteria derived from the paper's claims: comparison of bcc fractions at t=30 ps for the two intersection types and monotonic increase with volume."
}
```

## How you are scored
A hidden verifier will examine each of the three scored CSV files independently. It checks that the files contain the expected columns, that values fall within sensible physical ranges, and that the time series satisfy certain structural properties that are expected for a correctly executed simulation pipeline – for example, trends in the fraction over time, relative ordering between different intersection types, and the dependence of the transformation on the intersection volume. The verifier does not require matching any specific numerical value from the literature; it rewards solutions that exhibit the physically expected patterns. The total reward is a weighted sum over the three artifacts, with the main comparison curves (`olson_cohen_*.csv` and `perfect_perfect_*.csv`) carrying the largest individual weight. No gold values or tolerances are provided to the solver; the simulation must be run and the analysis performed from the instructions alone to obtain the correct structural signatures.
