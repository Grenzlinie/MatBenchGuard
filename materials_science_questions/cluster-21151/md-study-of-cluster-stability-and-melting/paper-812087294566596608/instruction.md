# MD Equilibration of a Molecular Cluster and Extraction of Lattice Parameters and Orientational Tilt

## Problem background
Adamantane (tricyclo[3.3.1.1]decane) is a prototypical plastic crystal that undergoes an order–disorder phase transition from a low‑temperature tetragonal phase to a high‑temperature cubic plastic phase. This task investigates the low‑temperature structure of a cluster of deuterated adamantane (C10D16) using molecular dynamics (MD) with a simplified rigid‑molecule model and a modified hydrogen–hydrogen pair potential. The goal is to simulate a free spherical cluster of 256 molecules at 100 K and determine whether the system equilibrates into a structure consistent with the P‾42₁c space group, extracting the resulting unit cell parameters and the molecular orientational tilt.

## Approach
The simulation treats each molecule as a 16‑site rigid body with T d symmetry. Inter‑molecular forces are computed from a 6‑exp pair potential that has been reduced to a single H–H term, with parameters provided in the assets. The initial cluster is built by placing molecules on the low‑temperature P‾42₁c crystal lattice (converted to a cubic axial system) and is given random linear and angular velocities at 100 K. The system is then relaxed by zero‑pressure MD using a time step of 0.015 ps; an initial velocity‑scaling phase brings the cluster to the desired temperature, and equilibration continues until the potential energy stabilises. Structural analysis uses the molecule centre‑of‑mass radial distribution function to identify nearest‑neighbour peaks along the a, b, and c directions, from which the unit cell parameters are derived. The orientational state is analysed by projecting the tetrahedral vertex vectors onto a unit sphere (equal‑area projection) and measuring the mean angular deviation of the molecular orientations from the tetragonal axes.

## Reproduction target
Produce two CSV files under `/app/outputs`:

- `lattice_params.csv`: a single row listing `cluster_size` (256) and the equilibrated unit cell parameters `a`, `b`, and `c` (in Å) for the 256‑molecule cluster at 100 K.
- `tilt_angle.csv`: a single row listing `cluster_size` (256) and the mean orientational tilt angle `tilt_angle` (in degrees) of the molecules relative to the tetragonal axes.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/
- Modified H-H potential parameters
- Deuterated adamantane molecular geometry (C10D16)
- Low-temperature P-42_1c crystal structure

## Workflow steps

### Step 1: Generate reduced molecular model
- Role: process
- Action: Construct the rigid 16‑site deuterated adamantane molecule with Td symmetry using the specified C–C and C–D bond lengths. The molecule will be treated as a rigid body in the MD simulation.
- Evidence: `/app/outputs/molecule_geometry.dat`

### Step 2: Build initial spherical cluster
- Role: process
- Action: Create a spherical cluster of 256 molecules by placing the rigid molecules in the P-42_1c crystal lattice (cubic axial convention: a=b=9.33 Å, c=8.81 Å). Assign random linear and angular velocities drawn from a Gaussian distribution consistent with 100 K. The cluster has free boundaries (stress‑free).
- Evidence: `/app/outputs/initial_cluster.data`

### Step 3: MD equilibration at 100 K
- Role: process
- Action: Run a zero‑pressure molecular dynamics simulation at 100 K using the modified H‑H potential and a time step of 0.015 ps. Apply temperature scaling during an initial equilibration phase until the potential energy stabilizes (5–10 ps). The trajectory should include the equilibrated configuration.
- Evidence: `/app/outputs/equilibrated_trajectory.dcd`

### Step 4: Extract lattice parameters from RDF
- Role: scored (load-bearing)
- Action: From the equilibrated trajectory, compute the molecule centre‑of‑mass radial distribution function g(r). Identify the peaks corresponding to the nearest‑neighbour distances along the tetragonal a, b, and c axes (in the cubic convention). Convert the peak positions to unit cell parameters a, b, c and write them to lattice_params.csv.
- Output file: `/app/outputs/lattice_params.csv`
- Format: csv
- Contract: CSV with header: cluster_size,a,b,c. Single data row with integer cluster_size=256, floats a,b,c in Å.
- Scoring: scored by hidden verifier

### Step 5: Extract orientational tilt angle
- Role: scored
- Action: Analyse the molecular orientations in the equilibrated cluster. For each molecule, project the four tetrahedral vertex vectors onto a unit sphere to create a dot‑plot (equal‑area projection). Measure the angular tilt of the molecular orientations relative to the tetragonal axes and compute the mean tilt angle. Write the result to tilt_angle.csv.
- Output file: `/app/outputs/tilt_angle.csv`
- Format: csv
- Contract: CSV with header: cluster_size,tilt_angle. Single data row with integer cluster_size=256, float tilt_angle in degrees.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_params.csv`
- `/app/outputs/tilt_angle.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_params.csv
- path: `/app/outputs/lattice_params.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrated unit cell parameters a, b, c for the 256-molecule cluster at 100 K.
- schema:
  - `type`: table
  - `required_columns`: `cluster_size`, `a`, `b`, `c`
  - `units`:
    - `a`: Å
    - `b`: Å
    - `c`: Å

### tilt_angle.csv
- path: `/app/outputs/tilt_angle.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mean molecular orientation tilt angle relative to the tetragonal axes for the 256-molecule cluster at 100 K.
- schema:
  - `type`: table
  - `required_columns`: `cluster_size`, `tilt_angle`
  - `units`:
    - `tilt_angle`: degrees

Notes: The transition temperature (210 ± 10 K), disordering temperature (240 ± 15 K), and cooling‑induced local order are not included as scored stages. The transition and disordering temperatures are strongly dependent on system size and heating protocol (as noted by the authors) and cannot be reduced to a single deterministic gold that fairly scores an independent re‑implementation. The cooled local order is qualitative and the paper provides no single numeric value suitable for exact‑match scoring. Hence the task focuses on the low‑temperature equilibrated structure (lattice parameters and tilt angle) which are the primary validatable results of the original work. Both outputs are fixed physical quantities determined by the model and protocol; they are compared to the paper’s reported values within hidden tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster_size",
          "a",
          "b",
          "c"
        ],
        "units": {
          "a": "Å",
          "b": "Å",
          "c": "Å"
        }
      },
      "description": "Equilibrated unit cell parameters a, b, c for the 256-molecule cluster at 100 K."
    },
    {
      "file": "tilt_angle.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster_size",
          "tilt_angle"
        ],
        "units": {
          "tilt_angle": "degrees"
        }
      },
      "description": "Mean molecular orientation tilt angle relative to the tetragonal axes for the 256-molecule cluster at 100 K."
    }
  ],
  "notes": "The transition temperature (210 ± 10 K), disordering temperature (240 ± 15 K), and cooling‑induced local order are not included as scored stages. The transition and disordering temperatures are strongly dependent on system size and heating protocol (as noted by the authors) and cannot be reduced to a single deterministic gold that fairly scores an independent re‑implementation. The cooled local order is qualitative and the paper provides no single numeric value suitable for exact‑match scoring. Hence the task focuses on the low‑temperature equilibrated structure (lattice parameters and tilt angle) which are the primary validatable results of the original work. Both outputs are fixed physical quantities determined by the model and protocol; they are compared to the paper’s reported values within hidden tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your `lattice_params.csv` and `tilt_angle.csv` files. The verifier extracts your reported numbers and compares them to hidden expected values within predetermined tolerances. The overall reward is a weighted combination of the two scored artifacts. Meeting the tolerances earns full credit; the reward decreases as the values deviate further. The verifier's tolerances and exact weights are not disclosed. Simply reporting numbers that seem plausible is not enough—the values must agree with the hidden gold to receive credit.
