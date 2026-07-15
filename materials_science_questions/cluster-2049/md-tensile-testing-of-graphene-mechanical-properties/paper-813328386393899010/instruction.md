# Buckling of Graphene Nanoribbons with Tilt Grain Boundaries via Molecular Dynamics

## Problem background
Graphene nanoribbons (GNRs) under compressive axial load can buckle out of plane, and the buckling threshold and deformation shape depend on boundary conditions and material inhomogeneities. Large-area graphene films grown on metal foils commonly contain grain boundaries — lines of topological defects such as pentagon–heptagon pairs that separate regions of different crystallographic orientation. This study addresses how two specific tilt grain boundaries, LAGBI (misorientation angle θ=21.8°) and LAGBII (θ=32.2°), influence the buckling of rectangular GNRs with armchair and zigzag edges. The work compares the buckling behaviour of perfect graphene (PG) to that of ribbons containing each grain boundary, under both free and supported lateral boundary conditions, and for compression applied either perpendicular or parallel to the grain boundary line. Determining the buckling strains, the free-energy minima, and the resulting out-of-plane deformation profiles will quantify the mechanical effect of these common grain boundaries.

## Approach
The reproduction uses classical molecular dynamics (MD) simulations with Brenner’s bond-order potential to model the carbon‑carbon interactions in graphene. For each of the three systems — perfect graphene (PG) and the two grain-boundary ribbons (LAGBI, LAGBII) — a flat atomic structure is built and equilibrated at 300 K using a Nosé–Hoover thermostat. From the equilibrated configurations, a series of constant-strain‑rate compression runs are performed for every relevant combination of lateral boundary condition (free or supported) and compression direction (along the ribbon length or width). Multiple independent realizations with different initial velocities are run for each condition to obtain statistical averages. The raw MD output — the mean square out-of-plane displacement as a function of strain, the cumulative non-equilibrium work, and the atomic coordinates at specific strains — is then analysed to identify the buckling transition, compute free-energy differences via the Jarzynski equality, and extract the y‑averaged out‑of‑plane deflection profiles. No pre‑computed data are used; all results are derived from the agent’s own simulation runs.

## Reproduction target
Produce three scored CSV files in `/app/outputs` by executing the MD simulation and analysis pipeline described in the Steps:

1. **buckling_strains.csv** – the buckling strain (in percent) for every combination of system (PG, LAGBI, LAGBII), lateral boundary condition (FBC or SBC), and compression direction (α=0 along the ribbon length, α=π/2 across the ribbon width). Nine rows covering all conditions that are experimentally realizable within the protocol.

2. **free_energy_minima.csv** – the minimum free‑energy difference ΔF (in eV) and the equilibrium strain ε_m at the minimum (in percent) for PG and LAGBI under the supported boundary condition (SBC) with compression along α=0. Two rows.

3. **shape_profiles.csv** – the y‑averaged out‑of‑plane atomic displacement z (in nm) as a function of the longitudinal coordinate x (in nm) for the three systems (PG, LAGBI, LAGBII) under SBC with α=0, at an applied compressive strain of 2.45 %. Three separate data series.

All values must be computed from the MD trajectories; the final artifacts are checked for internal consistency with the raw simulation data.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/download.html
- Brenner's bond‑order potential (REBO): LAMMPS pair_style airebo/rebo

## Workflow steps

### Step 1: Build atomic structures
- Role: process
- Action: Construct initial flat atomic coordinates for a perfect graphene nanoribbon (PG) of size a×b = 20×10 nm² with armchair (x) and zigzag (y) edges, and two grain‑boundary variants containing a central array of 5–7 defects along the y‑direction: LAGBI (θ=21.8°) and LAGBII (θ=32.2°) as described by the widely used grain‑boundary model. Use a honeycomb lattice with nearest‑neighbour distance 0.142 nm. Write three LAMMPS‑readable data files.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: Equilibrate at room temperature
- Role: process
- Action: For each of the three structures (PG, LAGBI, LAGBII), run a classical MD equilibration using Brenner’s bond‑order potential, a Nosé–Hoover thermostat at 300 K, a 0.5 fs timestep, and a total of 150 000 steps (75 ps). Save the final equilibrated coordinates as restart files.
- Evidence: `/app/outputs/equilibration.log`

### Step 3: Compression molecular dynamics simulations
- Role: process
- Action: For each system (PG, LAGBI, LAGBII), each lateral boundary condition (free FBC, supported SBC), and each compression direction (α=0 along x, α=π/2 along y), perform compression MD simulations. Use strain rates ν = 0.027/ns (α=0) and 0.054/ns (α=π/2) with a compression step δx = 0.667 pm applied every 5000 MD steps (δt = 0.5 fs). For each condition run 10 independent realisations with different initial velocities. Record ⟨h²⟩ vs strain, atomic trajectories, and the non‑equilibrium work W.
- Evidence: `/app/outputs/compression_summary.log`

### Step 4: Determine buckling strains
- Role: scored
- Action: From the ⟨h²⟩ vs strain data collected in step_03, identify the sudden increase that marks the buckling transition. Extract the buckling strain ε_b for each configuration and write the results to a CSV file covering all conditions that have a reported value.
- Output file: `/app/outputs/buckling_strains.csv`
- Format: csv
- Contract: system (string: PG/LAGBI/LAGBII), boundary_condition (string: FBC/SBC), compression_direction (string: alpha0/alpha_pi_2), buckling_strain_percent (float). 9 rows covering all combinations listed in the paper.
- Scoring: scored by hidden verifier

### Step 5: Compute free energy minima
- Role: scored (load-bearing)
- Action: Apply the Jarzynski equality to the work data from step_03 to obtain ΔF(ε) for PG and LAGBI under SBC with α=0. Locate the equilibrium strain ε_m at the free‑energy minimum and record the corresponding ΔF value. Write one CSV row per system.
- Output file: `/app/outputs/free_energy_minima.csv`
- Format: csv
- Contract: system (string), boundary_condition (string), compression_direction (string), free_energy_min_eV (float), equilibrium_strain_percent (float). Two rows.
- Scoring: scored by hidden verifier

### Step 6: Analyze deformation shape
- Role: scored (load-bearing)
- Action: From the compression trajectories at strain ε = 2.45 % under SBC with α=0, extract the out‑of‑plane atomic positions. Compute the y‑averaged z‑deviation profile as a function of x for PG, LAGBI, and LAGBII. Write the profiles to a CSV file.
- Output file: `/app/outputs/shape_profiles.csv`
- Format: csv
- Contract: system (string), x_position_nm (float), average_z_deviation_nm (float). Three sets of data.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/buckling_strains.csv`
- `/app/outputs/free_energy_minima.csv`
- `/app/outputs/shape_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### buckling_strains.csv
- path: `/app/outputs/buckling_strains.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Buckling strains for perfect graphene, LAGBI, and LAGBII under free and supported lateral boundary conditions for compression along x and y. The checker recomputes strain values from the paper’s Table I within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `system`, `boundary_condition`, `compression_direction`, `buckling_strain_percent`
  - `units`:
    - `buckling_strain_percent`: percent

### free_energy_minima.csv
- path: `/app/outputs/free_energy_minima.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Free energy minima ΔF and equilibrium strains ε_m for PG and LAGBI under SBC α=0. Checker compares ΔF to the paper‑reported values with tolerance ±0.5 eV.
- schema:
  - `type`: table
  - `required_columns`: `system`, `boundary_condition`, `compression_direction`, `free_energy_min_eV`, `equilibrium_strain_percent`
  - `units`:
    - `free_energy_min_eV`: electron volt
    - `equilibrium_strain_percent`: percent

### shape_profiles.csv
- path: `/app/outputs/shape_profiles.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: y‑averaged out‑of‑plane deflection for PG, LAGBI, LAGBII under SBC α=0 at ε=2.45 %. The checker fits a sine function A·sin(πx/a) and evaluates R² for each system; PG must exhibit a good fit (R²>0.9) while grain‑boundary systems must deviate (R²<0.7) and show a significant residual near the centre.
- schema:
  - `type`: table
  - `required_columns`: `system`, `x_position_nm`, `average_z_deviation_nm`
  - `units`:
    - `x_position_nm`: nm
    - `average_z_deviation_nm`: nm

Notes: Scored artifacts cover buckling strains, free‑energy minima, and deformation shape profiles. All gold values and tolerances are hidden. The load‑bearing steps (free energy minima and shape profiles) ensure the MD simulation stages cannot be bypassed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "buckling_strains.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "boundary_condition",
          "compression_direction",
          "buckling_strain_percent"
        ],
        "units": {
          "buckling_strain_percent": "percent"
        }
      },
      "description": "Buckling strains for perfect graphene, LAGBI, and LAGBII under free and supported lateral boundary conditions for compression along x and y. The checker recomputes strain values from the paper’s Table I within tolerance."
    },
    {
      "file": "free_energy_minima.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "boundary_condition",
          "compression_direction",
          "free_energy_min_eV",
          "equilibrium_strain_percent"
        ],
        "units": {
          "free_energy_min_eV": "electron volt",
          "equilibrium_strain_percent": "percent"
        }
      },
      "description": "Free energy minima ΔF and equilibrium strains ε_m for PG and LAGBI under SBC α=0. Checker compares ΔF to the paper‑reported values with tolerance ±0.5 eV."
    },
    {
      "file": "shape_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "x_position_nm",
          "average_z_deviation_nm"
        ],
        "units": {
          "x_position_nm": "nm",
          "average_z_deviation_nm": "nm"
        }
      },
      "description": "y‑averaged out‑of‑plane deflection for PG, LAGBI, LAGBII under SBC α=0 at ε=2.45 %. The checker fits a sine function A·sin(πx/a) and evaluates R² for each system; PG must exhibit a good fit (R²>0.9) while grain‑boundary systems must deviate (R²<0.7) and show a significant residual near the centre."
    }
  ],
  "notes": "Scored artifacts cover buckling strains, free‑energy minima, and deformation shape profiles. All gold values and tolerances are hidden. The load‑bearing steps (free energy minima and shape profiles) ensure the MD simulation stages cannot be bypassed."
}
```

## How you are scored
A hidden verifier runs after the task and evaluates each of the three scored files independently. The verifier has access to hidden reference values and quality criteria, but not to your raw simulation output except where needed for recomputation. Scoring works as follows:

- **Buckling strains**: the verifier may recompute the buckling strain from your ⟨h²⟩ data and compare your reported values to a reference with an appropriate tolerance. Consistent identification of the sudden increase in out‑of‑plane displacement is required.
- **Free‑energy minima**: the verifier may recompute ΔF from the work traces you provide (or that you used) and compare the minimum value and location to expected values within a given tolerance.
- **Deformation shape**: the verifier fits a single sine‑wave model A·sin(πx/a) to the PG profile and evaluates the goodness‑of‑fit; for the grain‑boundary systems it checks that the same sine model is a poor fit and that a significant residual exists near the ribbon centre. The shape analysis tests whether the buckled deformation deviates from a simple harmonic mode in the presence of grain boundaries.

The final reward (a number between 0 and 1) is a weighted sum of the scores from the three stages, with the largest weight on the free‑energy and shape stages. Simply reporting the correct numbers from the literature without running the full simulation pipeline will not produce the required supporting evidence and will receive a low score.
