# Finite dislocation network elastic interaction and zero-torque puckering calculation

## Problem background
Small-angle grain boundaries consist of arrays of dislocations that accommodate the misorientation between two crystals. For boundaries of mixed character—neither pure tilt nor pure twist—the dislocations do not necessarily lie in a single plane. Elastic interaction forces between the dislocation segments can distort the network, causing the boundary to pucker into two planes. Understanding how these interaction forces depend on the boundary character and how the resulting puckered configuration affects the elastic energy is important for predicting stable grain boundary structures.

## Approach
The analysis uses a finite network of straight dislocation segments constructed according to O‑lattice theory. For a given mean boundary plane, rotation axis, and pucker parameter, the network geometry is built such that segments lie in O‑cell walls and obey node rules. The stress field of the network is obtained by summing the stress contributions from every segment using the closed‑form expressions for a straight dislocation (Hirth and Lothe). The Peach–Koehler formula converts the local stress into forces on dislocations, and the torque on a central segment is computed. The zero‑torque pucker parameter is found by adjusting the pucker amplitude until the net torque on the central segment vanishes. This zero‑torque configuration is taken as a low‑energy proxy. To compare energies, the stress tensor is evaluated on a grid of points in planes parallel to the mean boundary plane, the elastic energy density is computed, and the mean planar energy density is obtained by averaging within each layer. A comparison is performed between the planar (flat) configuration and the puckered configuration at a fixed boundary character.

## Reproduction target
For deviation angles φ from 0° to 90° (in steps of at most 5°), compute the torque acting on a planar dislocation network (pucker parameter P/D = 0) of 89 segments and report torque versus φ. For the same φ range, determine the pucker parameter P/D that gives zero net torque on the central segment and report P/D versus φ. Then, for φ = 45°, evaluate the mean planar elastic energy density as a function of distance from the mean boundary plane (in units of the dislocation spacing D) for both the flat configuration (P/D = 0) and the zero‑torque puckered configuration, using a 72‑segment network and 100 sampling points per layer. Output three CSV files containing these results.

## Assets

- Hirth and Lothe straight-dislocation stress field formulas
- O-lattice theory

## Workflow steps

### Step 1: Generate dislocation network geometry
- Role: process
- Action: Implement a routine to construct a finite dislocation network of straight segments for given misorientation geometry (rotation axis, rotation angle, mean boundary plane normal, pucker parameter P). Segments must lie in O cell walls and obey node rules. Produce arrays of segment endpoints, line directions, and Burgers vectors for specified network sizes (89 segments for torque analysis, 72 segments for energy analysis).
- Evidence: `/app/outputs/network_geometry.pkl`

### Step 2: Compute torque vs deviation angle
- Role: scored
- Action: For phi from 0° to 90° in steps of at most 5°, generate a planar network (P/D=0) with 89 segments. At each phi, compute the stress tensor at two points near the ends of the central segment by summing the Hirth–Lothe stress contributions from all segments. Apply the Peach–Koehler formula to obtain the torque on the central segment. Output a CSV with phi and computed torque.
- Output file: `/app/outputs/torque_vs_phi.csv`
- Format: csv
- Contract: phi (degrees), torque (arbitrary linear elastic units)
- Scoring: scored by hidden verifier

### Step 3: Determine zero-torque pucker parameter
- Role: scored
- Action: For the same phi range, adjust P/D to find the configuration that yields zero net torque on the central segment using the same 89-segment network and torque calculation. Output the zero-torque value of P/D for each phi.
- Output file: `/app/outputs/pucker_vs_phi.csv`
- Format: csv
- Contract: phi (degrees), P/D (dimensionless)
- Scoring: scored by hidden verifier

### Step 4: Compare energy density profiles for flat and puckered boundaries at phi=45°
- Role: scored (load-bearing)
- Action: For phi=45°, generate a 72-segment network for the flat (P/D=0) and the zero-torque puckered (P/D from step_03) configurations. Compute the stress tensor on a grid of 100 points per layer in planes parallel to the mean boundary plane spanning the boundary thickness. From the stress, compute the elastic energy density at each point, average within each layer, and output the mean planar energy density as a function of distance (in units of D).
- Output file: `/app/outputs/energy_density_profiles_phi45.csv`
- Format: csv
- Contract: x_b_D (distance in units of D), flat_energy_density (arbitrary units), puckered_energy_density (arbitrary units)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/torque_vs_phi.csv`
- `/app/outputs/pucker_vs_phi.csv`
- `/app/outputs/energy_density_profiles_phi45.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### torque_vs_phi.csv
- path: `/app/outputs/torque_vs_phi.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Torque acting in a planar dislocation network as a function of deviation from pure twist character.
- schema:
  - `type`: table
  - `required_columns`: `phi`, `torque`
  - `units`:
    - `phi`: degrees
    - `torque`: arbitrary linear elastic units

### pucker_vs_phi.csv
- path: `/app/outputs/pucker_vs_phi.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zero-torque pucker parameter P/D as a function of phi.
- schema:
  - `type`: table
  - `required_columns`: `phi`, `P/D`
  - `units`:
    - `phi`: degrees
    - `P/D`: dimensionless

### energy_density_profiles_phi45.csv
- path: `/app/outputs/energy_density_profiles_phi45.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Mean planar energy density as a function of distance from the mean boundary plane for flat and puckered boundaries at phi=45°.
- schema:
  - `type`: table
  - `required_columns`: `x_b_D`, `flat_energy_density`, `puckered_energy_density`
  - `units`:
    - `x_b_D`: distance in units of D
    - `flat_energy_density`: arbitrary linear elastic energy density units
    - `puckered_energy_density`: arbitrary linear elastic energy density units

Notes: All computations use isotropic linear elasticity and publicly known formulas. No proprietary data or code required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "torque_vs_phi.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi",
          "torque"
        ],
        "units": {
          "phi": "degrees",
          "torque": "arbitrary linear elastic units"
        }
      },
      "description": "Torque acting in a planar dislocation network as a function of deviation from pure twist character."
    },
    {
      "file": "pucker_vs_phi.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi",
          "P/D"
        ],
        "units": {
          "phi": "degrees",
          "P/D": "dimensionless"
        }
      },
      "description": "Zero-torque pucker parameter P/D as a function of phi."
    },
    {
      "file": "energy_density_profiles_phi45.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_b_D",
          "flat_energy_density",
          "puckered_energy_density"
        ],
        "units": {
          "x_b_D": "distance in units of D",
          "flat_energy_density": "arbitrary linear elastic energy density units",
          "puckered_energy_density": "arbitrary linear elastic energy density units"
        }
      },
      "description": "Mean planar energy density as a function of distance from the mean boundary plane for flat and puckered boundaries at phi=45°."
    }
  ],
  "notes": "All computations use isotropic linear elasticity and publicly known formulas. No proprietary data or code required."
}
```

## How you are scored
Each scored CSV file is independently checked by a hidden verifier. The verifier compares the reported torque vs φ curve to hidden reference values; it checks the magnitude, monotonic trend, and peak location within an appropriate tolerance. The pucker parameter vs φ curve is compared to hidden reference P/D values; the verifier assesses whether the curve behaves as expected (e.g., zero at pure twist and increasing for mixed character). The energy density profiles at φ = 45° are evaluated by checking that the flat and puckered curves have the correct relative magnitude, shape, and decay behavior. The verifier assigns a weight to each stage and combines the stage scores into a single reward. Reporting only the paper’s numbers without correctly executing the computational workflow will not yield the correct reward because the reference values are hidden.
