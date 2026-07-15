# Classical MD simulation of water occupancy and transport in flexible (6,6) carbon nanotube

## Problem background
Carbon nanotubes can serve as simple nonpolar water channels. Understanding how mechanical flexibility influences water filling and transport in such confined hydrophobic pores is crucial for biological channel mimicry and nanoscale fluidic applications. The target is to determine how increasing the flexibility of a (6,6) carbon nanotube affects the equilibrium water occupancy and the dynamics of single‑file water transport. Specifically, this reproduction quantifies the shift in occupancy distributions and transport metrics between a stiff and a flexible nanotube, using classical molecular dynamics simulations.

## Approach
Classical molecular dynamics simulations are performed on a (6,6) armchair carbon nanotube segment (144 atoms, 6 unit cells) solvated in TIP3P water (~1034 molecules) in a periodic cubic box of ~37 Å. The tube's flexibility is controlled by a parameter φ that scales the angular, torsional, and nonbonded carbon–carbon interactions by a factor 10^(−φ). Two conditions are compared: a stiff tube (φ=0) and a flexible tube (φ=1.3). Simulations are run at 298 K and 1 atm for 20 ns each. From the trajectories, the continuous occupancy N_c (a weighted count of water molecules inside the tube) is computed for every saved frame to build normalized probability densities. In addition, the average integer occupancy ⟨N_w⟩, the total number of water exit events (entry, stay ≥5 ps, exit without re‑entry within 5 ps), and the average translocation time t_tr are extracted. The comparison between the two conditions reveals the trend in occupancy and transport properties.

## Reproduction target
Produce three CSV files:

- occupancy_phi_0.csv: normalized probability density of N_c for φ=0, with columns N_c (bin center, dimensionless) and probability_density (dimensionless), bins covering 0–8 uniformly.
- occupancy_phi_1.3.csv: same for φ=1.3.
- transport_summary.csv: a table with columns phi (dimensionless), avg_N_w (dimensionless), N_exit (count), and t_tr_ps (ps), giving the transport metrics for φ=0 and φ=1.3.

The data in these files will be evaluated by the hidden verifier against expected trends; the reproduction succeeds if the measured trends match the expected direction of change with flexibility.

## Assets

- GROMACS: https://www.gromacs.org
- AMBER99 force field: https://ambermd.org/AmberModels.php
- TIP3P water model

## Workflow steps

### Step 1: System construction and equilibration
- Role: process
- Action: Build a (6,6) armchair carbon nanotube (144 atoms, 6 unit cells) using AMBER99 carbon parameters, solvate with TIP3P water (~1034 molecules) in a periodic cubic box of side ~37 Å, add counterions if needed, minimize energy, and equilibrate at NPT (298 K, 1 atm) with the flexibility parameter φ implemented as a scaling factor on angular, torsional, and nonbonded C–C terms.
- Evidence: `/app/outputs/equilibration.log`

### Step 2: Production MD for φ=0
- Role: process
- Action: Run a 20 ns NPT production simulation (298 K, 1 atm) with φ=0, saving atom coordinates every 0.5 ps for occupancy and transport analysis.
- Evidence: `/app/outputs/traj_phi0.xtc`

### Step 3: Production MD for φ=1.3
- Role: process
- Action: Run a 20 ns NPT production simulation (298 K, 1 atm) with φ=1.3, saving atom coordinates every 0.5 ps for occupancy and transport analysis.
- Evidence: `/app/outputs/traj_phi1.3.xtc`

### Step 4: Occupancy probability density for φ=0
- Role: scored (load-bearing)
- Action: From the φ=0 trajectory, compute the continuous occupancy N_c for every saved frame (using the weighted counting function described in the paper's appendix), bin the values uniformly over the range 0–8, normalize to obtain a probability density, and save as CSV.
- Output file: `/app/outputs/occupancy_phi_0.csv`
- Format: csv
- Contract: Columns: N_c (float, histogram bin center), probability_density (float). Histogram bins covering N_c range 0–8 with uniform width. Includes header.
- Scoring: scored by hidden verifier

### Step 5: Occupancy probability density for φ=1.3
- Role: scored (load-bearing)
- Action: From the φ=1.3 trajectory, compute the continuous occupancy N_c for every saved frame, bin uniformly over 0–8, normalize to a probability density, and save as CSV.
- Output file: `/app/outputs/occupancy_phi_1.3.csv`
- Format: csv
- Contract: Columns: N_c (float, histogram bin center), probability_density (float). Histogram bins covering N_c range 0–8 with uniform width. Includes header.
- Scoring: scored by hidden verifier

### Step 6: Transport property analysis
- Role: scored (load-bearing)
- Action: From the same 20 ns trajectories (φ=0 and φ=1.3), determine the average integer water occupancy ⟨N_w⟩, count the total number of water exit events (molecules that enter, stay inside for ≥5 ps, and exit without re‑entering within 5 ps), and compute the average translocation time t_tr for crossing the tube. Save the results in a summary CSV file.
- Output file: `/app/outputs/transport_summary.csv`
- Format: csv
- Contract: Columns: phi (float), avg_N_w (float), N_exit (integer), t_tr_ps (float). Two rows for φ=0 and φ=1.3. Includes header.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/occupancy_phi_0.csv`
- `/app/outputs/occupancy_phi_1.3.csv`
- `/app/outputs/transport_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### occupancy_phi_0.csv
- path: `/app/outputs/occupancy_phi_0.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized probability density of the continuous occupancy N_c for flexibility parameter φ=0.
- schema:
  - `type`: table
  - `required_columns`: `N_c`, `probability_density`
  - `units`:
    - `N_c`: dimensionless
    - `probability_density`: dimensionless

### occupancy_phi_1.3.csv
- path: `/app/outputs/occupancy_phi_1.3.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized probability density of the continuous occupancy N_c for flexibility parameter φ=1.3.
- schema:
  - `type`: table
  - `required_columns`: `N_c`, `probability_density`
  - `units`:
    - `N_c`: dimensionless
    - `probability_density`: dimensionless

### transport_summary.csv
- path: `/app/outputs/transport_summary.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Summary table of water transport metrics for φ=0 and φ=1.3.
- schema:
  - `type`: table
  - `required_columns`: `phi`, `avg_N_w`, `N_exit`, `t_tr_ps`
  - `units`:
    - `phi`: dimensionless
    - `avg_N_w`: dimensionless
    - `N_exit`: count
    - `t_tr_ps`: ps

Notes: The checker will compute the mean N_c from each occupancy histogram and verify that mean(φ=1.3) < mean(φ=0), and from the transport summary verify that avg_N_w(1.3) < avg_N_w(0), N_exit(1.3) < N_exit(0), and t_tr(1.3) > t_tr(0). Absolute numerical agreement is not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "occupancy_phi_0.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "N_c",
          "probability_density"
        ],
        "units": {
          "N_c": "dimensionless",
          "probability_density": "dimensionless"
        }
      },
      "description": "Normalized probability density of the continuous occupancy N_c for flexibility parameter φ=0."
    },
    {
      "file": "occupancy_phi_1.3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "N_c",
          "probability_density"
        ],
        "units": {
          "N_c": "dimensionless",
          "probability_density": "dimensionless"
        }
      },
      "description": "Normalized probability density of the continuous occupancy N_c for flexibility parameter φ=1.3."
    },
    {
      "file": "transport_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi",
          "avg_N_w",
          "N_exit",
          "t_tr_ps"
        ],
        "units": {
          "phi": "dimensionless",
          "avg_N_w": "dimensionless",
          "N_exit": "count",
          "t_tr_ps": "ps"
        }
      },
      "description": "Summary table of water transport metrics for φ=0 and φ=1.3."
    }
  ],
  "notes": "The checker will compute the mean N_c from each occupancy histogram and verify that mean(φ=1.3) < mean(φ=0), and from the transport summary verify that avg_N_w(1.3) < avg_N_w(0), N_exit(1.3) < N_exit(0), and t_tr(1.3) > t_tr(0). Absolute numerical agreement is not required."
}
```

## How you are scored
After you submit the three CSV files, a hidden verifier will independently score them. For occupancy, it will compute the weighted mean N_c from each histogram and compare the two means to check for a monotonic shift consistent with the expected effect of flexibility. For transport, it will compare the average occupancy, number of exit events, and translocation time between the two flexibility conditions. The checker evaluates each of these four trends; all must be satisfied for full credit. If any trend is opposite to the expected direction, the score for that stage is zero. The final reward is a weighted combination of the stage scores. Reporting numbers that look plausible but do not follow the expected trends will not pass.
