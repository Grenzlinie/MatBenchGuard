# Classical MD Simulation of Carbon Nanotube Plastic Deformation

## Problem background
Carbon nanotubes (CNTs) are exceptionally strong due to their sp2-bonded graphene-like structure, but when compressed they can undergo plastic deformation via the formation of sp3 diamond-like bonds or Stone-Wales bond rotations. At zero temperature, classical molecular dynamics (MD) simulations with empirical potentials typically show elastic buckling and “fin” structures without sp3 bond formation, whereas tight-binding calculations indicate that collapse and sp3 bonding can occur. The interplay between thermal fluctuations, strain rate, and the onset of these defects is not fully settled. In particular, it is an open question whether classical MD at finite temperature can access sp3 bond formation that is absent at 0 K, and how the yielding strain for sp3 bonds and bond rotations depends on deformation rate and temperature.

## Approach
The study uses classical MD with the Tersoff-Brenner reactive bond-order potential. Two simulation protocols are employed:

- **Relaxation at fixed strain**: An (8,0) CNT segment ≈40 Å long is held under 12 % uniform compressive strain with both ends fixed, and is relaxed for up to 200 ps at temperatures 0 K, 300 K, 800 K and 1600 K. The radial distribution function (RDF) of carbon–carbon distances is then computed from the final relaxed configuration. A peak in the 1.5–1.6 Å region would signal sp3 bond formation.

- **Continuous compression**: A (10,0) CNT segment ≈60 Å long is compressed at constant strain rates (2 %/ps, 0.1 %/ps and 0.0125 %/ps) up to 15 % total strain, at temperatures 300 K, 800 K and 1600 K. Trajectories are recorded and analysed to detect the first frame in which sp3 bonds (C–C distances ≈1.5–1.6 Å) or Stone-Wales bond rotations appear; the corresponding macroscopic applied strain is taken as the yielding strain for that defect.

By comparing RDFs across temperatures and tracking yielding strains as functions of strain rate and temperature, the reproducibility of the reported trends can be assessed.

## Reproduction target
Produce the following two CSV files:

1. `rdf_data.csv` – RDF of interatomic distances for the relaxed (8,0) CNT at temperatures 0 K, 300 K, 800 K and 1600 K. Columns: `temperature` (K), `distance` (Å), `intensity` (arbitrary). The distance range must cover at least 1.0–2.0 Å.

2. `yielding_strain.csv` – Yielding strain for sp3 bond formation and bond rotation during compression of a (10,0) CNT. Columns: `temperature` (K), `strain_rate` (%/ps), `defect_type` (either `sp3` or `rotation`), `yielding_strain` (%). Data must be supplied for all combinations of temperatures [300, 800, 1600] and strain rates [2.0, 0.1, 0.0125], with separate rows for each defect type.

The goal is to determine, from these two tables, whether the RDF shows a sp3-related peak near 1.5–1.6 Å only at finite temperatures, and whether the yielding strain decreases with increasing temperature at constant strain rate and with decreasing strain rate at constant temperature, for each defect type separately.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- Tersoff-Brenner potential file (CH.airebo): lammps
- Python with numpy, pandas, matplotlib: numpy pandas matplotlib

## Workflow steps

### Step 1: Construct (8,0) CNT with compressive strain
- Role: process
- Action: Generate the atomic configuration of an (8,0) carbon nanotube segment approximately 40 Å long with 12% uniform compressive strain and both ends fixed. Output the initial configuration file for MD.
- Evidence: `/app/outputs/initial_8_0_strained.data`

### Step 2: MD relaxation of (8,0) CNT
- Role: process
- Action: Run classical MD relaxation using the Tersoff-Brenner potential (pair_style airebo, CH.airebo) at temperatures 0K, 300K, 800K, and 1600K with a 0.5 fs timestep for up to 200 ps. Save final relaxed configurations.
- Evidence: `/app/outputs/md_relaxation_complete.txt`

### Step 3: Compute radial distribution function (RDF)
- Role: scored (load-bearing)
- Action: From the final relaxed atomic positions at each temperature, compute the radial distribution function of interatomic carbon-carbon distances. Write the RDF data as CSV with columns: temperature (K), distance (Angstrom), intensity (arbitrary). Ensure the distance range covers at least 1.0–2.0 Å.
- Output file: `/app/outputs/rdf_data.csv`
- Format: csv
- Contract: Columns: temperature (float, K), distance (float, Angstrom), intensity (float).
- Scoring: scored by hidden verifier

### Step 4: Construct (10,0) CNT for dynamic compression
- Role: process
- Action: Generate the atomic configuration of a (10,0) carbon nanotube segment approximately 60 Å long. No initial strain; ends will be moved to apply compression.
- Evidence: `/app/outputs/initial_10_0.data`

### Step 5: MD compression simulations of (10,0) CNT
- Role: process
- Action: Apply compressive strain at constant rates of 2%/ps, 0.1%/ps, and 0.0125%/ps up to 15% total strain using the Tersoff-Brenner potential at temperatures 300K, 800K, and 1600K. Record trajectories. Use at least a few independent samples per condition.
- Evidence: `/app/outputs/compression_runs_complete.txt`

### Step 6: Determine yielding strain for defects
- Role: scored (load-bearing)
- Action: Analyse the compression trajectories to detect the first appearance of sp3 bonds (C-C bond lengths ~1.5–1.6 Å) and bond rotations (Stone-Wales defects). For each temperature and strain-rate condition, report the macroscopic strain at which each defect type first appears. Write results as CSV with columns: temperature (K), strain_rate (percent/ps), defect_type (string: 'sp3' or 'rotation'), yielding_strain (percent).
- Output file: `/app/outputs/yielding_strain.csv`
- Format: csv
- Contract: Columns: temperature (int, K), strain_rate (float, %/ps), defect_type (str, one of 'sp3' or 'rotation'), yielding_strain (float, %).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rdf_data.csv`
- `/app/outputs/yielding_strain.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rdf_data.csv
- path: `/app/outputs/rdf_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: RDF curves for (8,0) CNT after relaxation at 12% strain. For T=0K the 1.5–1.6 Å region must lack a significant peak; for finite T a distinct peak must appear.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `distance`, `intensity`
  - `units`:
    - `temperature`: K
    - `distance`: Angstrom
    - `intensity`: arbitrary

### yielding_strain.csv
- path: `/app/outputs/yielding_strain.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Yielding strain at which sp3 bonds or bond rotations first appear during compression of a (10,0) CNT under various strain rates and temperatures.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `strain_rate`, `defect_type`, `yielding_strain`
  - `units`:
    - `temperature`: K
    - `strain_rate`: %/ps
    - `yielding_strain`: %

Notes: Scoring evaluates structural trends: for RDF, peak presence in the 1.5–1.6 Å range only at finite temperatures; for yielding strain, monotonic decrease with increasing temperature (fixed strain rate) and with decreasing strain rate (fixed temperature). Exact numeric values are not required; trends must hold per defect type.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rdf_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "distance",
          "intensity"
        ],
        "units": {
          "temperature": "K",
          "distance": "Angstrom",
          "intensity": "arbitrary"
        }
      },
      "description": "RDF curves for (8,0) CNT after relaxation at 12% strain. For T=0K the 1.5–1.6 Å region must lack a significant peak; for finite T a distinct peak must appear."
    },
    {
      "file": "yielding_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "strain_rate",
          "defect_type",
          "yielding_strain"
        ],
        "units": {
          "temperature": "K",
          "strain_rate": "%/ps",
          "yielding_strain": "%"
        }
      },
      "description": "Yielding strain at which sp3 bonds or bond rotations first appear during compression of a (10,0) CNT under various strain rates and temperatures."
    }
  ],
  "notes": "Scoring evaluates structural trends: for RDF, peak presence in the 1.5–1.6 Å range only at finite temperatures; for yielding strain, monotonic decrease with increasing temperature (fixed strain rate) and with decreasing strain rate (fixed temperature). Exact numeric values are not required; trends must hold per defect type."
}
```

## How you are scored
A hidden verifier inspects your submitted CSV artifacts independently. It does not attempt to rerun the MD simulations. Instead, it checks structural trends:

- For `rdf_data.csv`: it verifies that the 0 K curve lacks a significant peak in the 1.5–1.6 Å region (intensity below a threshold relative to the maximum), while the finite-temperature curves each show a distinct peak above that threshold.
- For `yielding_strain.csv`: it checks that for each defect type (`sp3` and `rotation`), the yielding strain decreases monotonically with increasing temperature when strain rate is held constant, and decreases monotonically with decreasing strain rate when temperature is held constant.

The total reward is a weighted combination of how well these two conditions are satisfied. Exact numerical agreement with any published value is not required; only the presence or absence of the RDF peak and the monotonicity of the yielding strain trends matter for scoring.
