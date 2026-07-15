# Dynamic Brittle Crack Propagation: Forbidden Low-Velocity Band in EAM-Ni Strip Geometry

## Problem background
Fast brittle fracture in crystalline solids can exhibit unusual dynamic behaviors at the atomic scale. Classical continuum theories predict that cracks can run at any velocity up to the Rayleigh wave speed, but molecular dynamics (MD) simulations and experiments suggest that steady-state crack propagation may be constrained to a band of velocities, with a lower bound below which the crack cannot propagate steadily—a "forbidden" low-velocity regime. This phenomenon is thought to emerge from lattice trapping and the nonlinear dynamics of atomic bond breaking. The present task investigates this regime by MD simulation of a brittle crack in an FCC nickel crystal, specifically the (100)[001] crack system modelled with an embedded-atom method (EAM) potential, under a thin-strip geometry that provides a constant energy release rate. The goal is to determine the relationship between the applied overload (relative to the Griffith load) and the terminal steady-state crack-tip velocity, and to characterize the onset of propagation at low overloads.

## Approach
We simulate a long crack in a thin strip of an FCC Ni crystal where the crack plane is (100) and the front is along [001]. The top and bottom boundaries are held at fixed displacement, producing a condition of constant energy release rate G that does not depend on crack length. A ramped viscous damping layer is applied near the boundaries and free surfaces to absorb outgoing phonons and prevent wave reflections from disturbing the crack tip. Atomic interactions are described by an EAM potential for nickel, and the system is kept at near-zero temperature with a local viscous damping that mimics an electronic heat bath. The crack is first equilibrated at the Griffith load G0, where the strain energy balances twice the surface energy. From this equilibrated state, the crack is overloaded by instantaneously rescaling all atomic displacements to achieve a new target G/G0. Six overloads are investigated: G/G0 = 1.00, 1.02, 1.04, 1.10, 1.30, and 1.50. For each overload, an MD run is performed under constant energy release rate, and the crack-tip position is tracked over time. The instantaneous crack-tip velocity is obtained from the change in crack-tip position over a suitable output interval and is normalized by the Rayleigh wave speed c_R (which must be precomputed from the elastic constants of the EAM-Ni potential). From the runs we extract the terminal steady-state velocity for each overload above the trapping threshold, classify the crack as stationary or moving at the three lowest overloads, and produce time-resolved velocity curves at 1.04 G0 and 1.10 G0. All simulations can be implemented using open-source MD software such as LAMMPS.

## Reproduction target
Compute from the MD simulations the following artifacts for the EAM-Ni (100)[001] crack in the strip geometry:
- For overloads G/G0 = 1.04, 1.10, 1.30, and 1.50: the terminal steady-state crack-tip velocity, normalized by the Rayleigh wave speed (v/c_R), reported in steady_state_velocities.csv.
- For overloads G/G0 = 1.00, 1.02, and 1.04: whether the crack remains "stationary" or begins to propagate ("moving"), reported in crack_state_low_overload.csv.
- For overload G/G0 = 1.04: the time-resolved crack-tip velocity (in units c_R) as a function of time (in units r0/c_L), reported in time_trace_1.04G0.csv.
- For overload G/G0 = 1.10: the time-resolved crack-tip velocity (in units c_R) as a function of time (in units r0/c_L), reported in time_trace_1.10G0.csv.
All outputs must be placed in /app/outputs.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- EAM potential for nickel (Foiles et al., PRB 33, 7983, 1986): https://www.ctcms.nist.gov/potentials/Ni.html

## Workflow steps

### Step 1: Compute wave speeds
- Role: process
- Action: Determine the isotropic elastic constants of EAM-Ni along the [001] direction and compute the longitudinal (c_L), transverse (c_t), and Rayleigh (c_R) wave speeds.
- Evidence: `/app/outputs/wave_speeds.txt`

### Step 2: Build strip model and equilibrate at Griffith load
- Role: process
- Action: Construct a thin-strip fcc Ni slab with a (100)[001] crack, apply fixed-displacement top/bottom boundaries and ramped viscous damping, then relax the system at boundary displacements corresponding to the Griffith energy release rate G0 (equilibrium at near-zero temperature).
- Evidence: `/app/outputs/equilibration.log`

### Step 3: Run crack propagation simulations at overloads
- Role: process
- Action: For each overload G/G0 = 1.00, 1.02, 1.04, 1.10, 1.30, 1.50, instantaneously rescale atomic displacements to apply the overload and run MD under constant energy release rate, with local viscous damping, logging crack-tip position at intervals.
- Evidence: `/app/outputs/simulation_runs.log`

### Step 4: Steady-state velocities
- Role: scored (load-bearing)
- Action: Extract the terminal steady-state crack-tip velocity (normalized by c_R) from the overload runs at G/G0 = 1.04, 1.10, 1.30, 1.50 and write a CSV file.
- Output file: `/app/outputs/steady_state_velocities.csv`
- Format: csv
- Contract: CSV: overload (float), terminal_velocity (float; ratio v/c_R).
- Scoring: scored by hidden verifier

### Step 5: Crack state at low overloads
- Role: scored
- Action: Classify whether the crack remains stationary or moves during the low overload simulations (G/G0 = 1.00, 1.02, 1.04) and write a CSV file.
- Output file: `/app/outputs/crack_state_low_overload.csv`
- Format: csv
- Contract: CSV: overload (float), state (string, either 'stationary' or 'moving').
- Scoring: scored by hidden verifier

### Step 6: Time trace at G=1.04G0
- Role: scored
- Action: Output the crack-tip velocity vs time for the 1.04 G0 overload run as a CSV file.
- Output file: `/app/outputs/time_trace_1.04G0.csv`
- Format: csv
- Contract: CSV: time (float, r0/c_L), v_tip (float, c_R).
- Scoring: scored by hidden verifier

### Step 7: Time trace at G=1.10G0
- Role: scored
- Action: Output the crack-tip velocity vs time for the 1.10 G0 overload run as a CSV file.
- Output file: `/app/outputs/time_trace_1.10G0.csv`
- Format: csv
- Contract: CSV: time (float, r0/c_L), v_tip (float, c_R).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/steady_state_velocities.csv`
- `/app/outputs/crack_state_low_overload.csv`
- `/app/outputs/time_trace_1.04G0.csv`
- `/app/outputs/time_trace_1.10G0.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### steady_state_velocities.csv
- path: `/app/outputs/steady_state_velocities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Terminal steady-state crack-tip velocities at overloads 1.04, 1.10, 1.30, 1.50 relative to the Griffith load. Checker compares to hidden paper-reported values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `overload`, `terminal_velocity`
  - `units`:
    - `overload`: G/G0 (dimensionless)
    - `terminal_velocity`: v/c_R (dimensionless)

### crack_state_low_overload.csv
- path: `/app/outputs/crack_state_low_overload.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Crack motion state at low overloads 1.00, 1.02, 1.04 and at high overload 2.00 where branching is expected. States are 'stationary', 'moving', or 'branching'. Checker expects exact string match with hidden paper result for all rows.
- schema:
  - `type`: table
  - `required_columns`: `overload`, `state`

### time_trace_1.04G0.csv
- path: `/app/outputs/time_trace_1.04G0.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Crack-tip velocity vs time for overload 1.04 G0. Checker verifies velocity is non-zero, increases from near zero, and reaches a plateau consistent with the terminal velocity for this overload.
- schema:
  - `type`: table
  - `required_columns`: `time`, `v_tip`
  - `units`:
    - `time`: r0/c_L
    - `v_tip`: c_R

### time_trace_1.10G0.csv
- path: `/app/outputs/time_trace_1.10G0.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Crack-tip velocity vs time for overload 1.10 G0. Checker verifies velocity is non-zero, increases, and reaches a plateau consistent with the terminal velocity for this overload.
- schema:
  - `type`: table
  - `required_columns`: `time`, `v_tip`
  - `units`:
    - `time`: r0/c_L
    - `v_tip`: c_R

Notes: All outputs must be placed under /app/outputs. The process steps generate the simulation data needed to produce the scored artifacts. The hidden checker compares terminal velocities to paper-reported values (±0.05 c_R), checks crack state strings exactly for all overloads including branching at 2.00, performs a qualitative shape check on time traces.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "steady_state_velocities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "overload",
          "terminal_velocity"
        ],
        "units": {
          "overload": "G/G0 (dimensionless)",
          "terminal_velocity": "v/c_R (dimensionless)"
        }
      },
      "description": "Terminal steady-state crack-tip velocities at overloads 1.04, 1.10, 1.30, 1.50 relative to the Griffith load. Checker compares to hidden paper-reported values within tolerance."
    },
    {
      "file": "crack_state_low_overload.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "overload",
          "state"
        ]
      },
      "description": "Crack motion state at low overloads 1.00, 1.02, 1.04 and at high overload 2.00 where branching is expected. States are 'stationary', 'moving', or 'branching'. Checker expects exact string match with hidden paper result for all rows."
    },
    {
      "file": "time_trace_1.04G0.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "v_tip"
        ],
        "units": {
          "time": "r0/c_L",
          "v_tip": "c_R"
        }
      },
      "description": "Crack-tip velocity vs time for overload 1.04 G0. Checker verifies velocity is non-zero, increases from near zero, and reaches a plateau consistent with the terminal velocity for this overload."
    },
    {
      "file": "time_trace_1.10G0.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "v_tip"
        ],
        "units": {
          "time": "r0/c_L",
          "v_tip": "c_R"
        }
      },
      "description": "Crack-tip velocity vs time for overload 1.10 G0. Checker verifies velocity is non-zero, increases, and reaches a plateau consistent with the terminal velocity for this overload."
    }
  ],
  "notes": "All outputs must be placed under /app/outputs. The process steps generate the simulation data needed to produce the scored artifacts. The hidden checker compares terminal velocities to paper-reported values (±0.05 c_R), checks crack state strings exactly for all overloads including branching at 2.00, performs a qualitative shape check on time traces."
}
```

## How you are scored
A hidden verifier independently inspects each of your workflow outputs and combines reward fractions into a final score between 0 and 1. The scoring of each artifact proceeds as follows:

- **steady_state_velocities.csv**: The reported terminal velocities (v/c_R) for overloads 1.04, 1.10, 1.30, and 1.50 are compared to reference values for the EAM-Ni (100)[001] system within a prescribed tolerance. Velocities that match the expected reference within tolerance earn credit; credit decreases the further the reported value deviates.

- **crack_state_low_overload.csv**: The state labels ("stationary" or "moving") for overloads 1.00, 1.02, and 1.04 are compared to the expected labels. An exact match is required for each overload; an incorrect label earns no credit for that row.

- **time_trace_1.04G0.csv** and **time_trace_1.10G0.csv**: The verifier performs a structural audit: it checks that the velocity is non-zero, increases from near-zero early in the trace, and reaches a plateau whose average level is consistent with the terminal velocity reported in steady_state_velocities.csv for that overload. Traces that are flat, monotonically decreasing, or have a plateau value grossly inconsistent with the corresponding terminal velocity receive lower credit.

The verifier also confirms that all required output files are present and correctly formatted before scoring content. You must produce artefacts that result from genuinely running the MD simulation; simply guessing or hardcoding known answers is detected by structural checks and will not earn full credit.
