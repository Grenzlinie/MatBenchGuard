# Coherent Phase Diagram Construction for Binary Nanoparticles

## Problem background
The phase stability of isolated binary alloy nanoparticles is modified by surface stress and composition‑dependent lattice strain. For a coherent two‑phase particle with a sharp core‑shell interface, the equilibrium state can be described in terms of temperature, composition, and an effective pressure that arises from the surface stress and external traction. The free energy, based on a regular solution model with isotropic linear elasticity and a quadratic compositional strain, leads to a set of coexistence and stability conditions. The goal is to numerically construct the coherent phase diagram (binodal and spinodal boundaries) in the space spanned by scaled temperature t, composition c, and dimensionless effective external pressure Π, and to locate the consolute critical points. The outcome reveals how the miscibility gap depends on the particle size and the nonlinear compositional strain coefficients.

## Approach
Use a regular solution thermodynamic model together with isotropic linear elasticity that includes a composition‑dependent lattice strain up to quadratic order in composition. Formulate the dimensionless free energy density φ(t, c, Π) that contains the ideal mixing entropy, the regular solution enthalpy, an elastic energy term, and a term coupling the effective pressure to the compositional strain. The key parameters are Λ (relative elastic‑to‑chemical energy strength), η_c (first‑order compositional strain coefficient), and η_cc (second‑order compositional strain coefficient).

For a given alloy composition c_o and dimensionless effective external pressure Π_o, the equilibrium two‑phase state is described by the core composition (c^β), shell composition (c^α), effective pressures in the two phases (Π^β, Π^α), and the volume fraction z of the β phase. These unknowns satisfy mass conservation (for composition and effective pressure), equality of diffusion potential, equality of effective strain, and interfacial equilibrium. The spinodal condition gives a direct relation among t, c, and Π, and the consolute critical point is obtained from an additional second‑derivative condition.

Implement this model for the four parameter sets:
- (Λ=350, η_c=-0.05, η_cc=0.04)
- (Λ=100, η_c=-0.05, η_cc=0.04)
- (Λ=100, η_c=-0.03, η_cc=0)
- (Λ=100, η_c=-0.01, η_cc=-0.04)

Numerically solve the equilibrium equations on a grid of scaled temperatures t and effective external pressures Π to determine the binodal phase boundaries (c^α, c^β, Π^α, Π^β), spinodal compositions, and critical point coordinates. Then extract the phase‑diagram slices at constant Π_o = 0.1 (t–c plane) and constant t = 0.8 (c–Π plane). The required numerical routines can be built with standard open‑source libraries (NumPy, SciPy).

## Reproduction target
For all four parameter sets, compute and write the following data files:

1. **Binodal phase boundaries** (`phase_boundary_data.csv`) at the two slices:
   - constant Π_o = 0.1 (t–c plane)
   - constant t = 0.8 (c–Π plane)
   Columns: param_set, slice_type, t, P_o (the dimensionless effective external pressure), c_alpha, c_beta, P_alpha (effective pressure in α phase), P_beta (effective pressure in β phase), and z (volume fraction of β phase).

2. **Spinodal lines** (`spinodal_data.csv`) for the same two slices:
   Columns: param_set, slice_type, t, P_o, c_spinodal.

3. **Consolute critical points** (`critical_points.csv`) for each parameter set:
   Columns: param_set, t_c (critical temperature), c_c (critical composition), P_o_c (critical external pressure).

All quantities are dimensionless. The data should fully describe the phase boundaries and spinodals on the required slices, and the critical points should satisfy both the spinodal and critical‑point conditions simultaneously.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Numerical solution of equilibrium and spinodal conditions
- Role: process
- Action: Implement the dimensionless free energy based on a regular solution model with linear elasticity and compositional strain. For four parameter sets ((Λ=350, η_c=-0.05, η_cc=0.04), (Λ=100, η_c=-0.05, η_cc=0.04), (Λ=100, η_c=-0.03, η_cc=0), (Λ=100, η_c=-0.01, η_cc=-0.04)), solve the equilibrium conditions (mass conservation, equal diffusion potential, equal effective strain, interfacial equilibrium) and the spinodal condition on grids of scaled temperature t and effective pressure Π. Determine binodal phase densities (c^α, c^β, Π^α, Π^β), spinodal compositions, and consolute critical point coordinates.
- Evidence: none

### Step 2: Phase boundary data
- Role: scored (load-bearing)
- Action: Write the binodal phase boundary data for all parameter sets at the slices constant effective pressure Π=0.1 (t–c plane) and constant temperature t=0.8 (c–P plane) to phase_boundary_data.csv.
- Output file: `/app/outputs/phase_boundary_data.csv`
- Format: csv
- Contract: Columns: param_set, slice_type, t, P_o, c_alpha, c_beta, P_alpha, P_beta, z
- Scoring: scored by hidden verifier

### Step 3: Spinodal data
- Role: scored
- Action: Write the spinodal line data for all parameter sets at the slices constant Π=0.1 (t–c) and constant t=0.8 (c–P) to spinodal_data.csv.
- Output file: `/app/outputs/spinodal_data.csv`
- Format: csv
- Contract: Columns: param_set, slice_type, t, P_o, c_spinodal
- Scoring: scored by hidden verifier

### Step 4: Critical points
- Role: scored
- Action: Write the consolute critical point coordinates (t_c, c_c, P_o_c) for each parameter set to critical_points.csv.
- Output file: `/app/outputs/critical_points.csv`
- Format: csv
- Contract: Columns: param_set, t_c, c_c, P_o_c
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_boundary_data.csv`
- `/app/outputs/spinodal_data.csv`
- `/app/outputs/critical_points.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_boundary_data.csv
- path: `/app/outputs/phase_boundary_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Binodal phase boundary coordinates for slices at constant effective pressure Π=0.1 and constant temperature t=0.8.
- schema:
  - `type`: table
  - `required_columns`: `param_set`, `slice_type`, `t`, `P_o`, `c_alpha`, `c_beta`, `P_alpha`, `P_beta`, `z`
  - `units`: object

### spinodal_data.csv
- path: `/app/outputs/spinodal_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Spinodal compositions for the isobaric and isothermal slices.
- schema:
  - `type`: table
  - `required_columns`: `param_set`, `slice_type`, `t`, `P_o`, `c_spinodal`
  - `units`: object

### critical_points.csv
- path: `/app/outputs/critical_points.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Consolute critical point coordinates for each parameter set.
- schema:
  - `type`: table
  - `required_columns`: `param_set`, `t_c`, `c_c`, `P_o_c`
  - `units`: object

Notes: All values are dimensionless. The checker recomputes the same thermodynamic model and compares coordinates within absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_boundary_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "param_set",
          "slice_type",
          "t",
          "P_o",
          "c_alpha",
          "c_beta",
          "P_alpha",
          "P_beta",
          "z"
        ],
        "units": {}
      },
      "description": "Binodal phase boundary coordinates for slices at constant effective pressure Π=0.1 and constant temperature t=0.8."
    },
    {
      "file": "spinodal_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "param_set",
          "slice_type",
          "t",
          "P_o",
          "c_spinodal"
        ],
        "units": {}
      },
      "description": "Spinodal compositions for the isobaric and isothermal slices."
    },
    {
      "file": "critical_points.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "param_set",
          "t_c",
          "c_c",
          "P_o_c"
        ],
        "units": {}
      },
      "description": "Consolute critical point coordinates for each parameter set."
    }
  ],
  "notes": "All values are dimensionless. The checker recomputes the same thermodynamic model and compares coordinates within absolute tolerances."
}
```

## How you are scored
A hidden verifier independently implements the same dimensionless thermodynamic model and equations with the identical parameter sets. It recomputes the phase boundary coordinates, spinodal compositions, and critical point coordinates for the exact conditions (Π_o = 0.1 and t = 0.8) that you are asked to produce. The verifier then compares each value you submitted in `phase_boundary_data.csv`, `spinodal_data.csv`, and `critical_points.csv` to its own recomputed reference. Your reward is a weighted average of the agreement across these three artifact files. Note that simply reporting known values from the literature is not sufficient — the verifier recomputes the results from scratch, so your scores reflect the correctness of your numerical implementation.
