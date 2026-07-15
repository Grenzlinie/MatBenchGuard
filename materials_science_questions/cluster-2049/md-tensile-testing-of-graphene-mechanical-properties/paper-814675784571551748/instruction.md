# Joule Heating Hot Spot Simulation in Graphene with Cracks

## Problem background
When a graphene layer is Joule-heated, its temperature distribution depends sensitively on the layer's geometry. Mechanical defects such as cracks disrupt the current flow and can lead to localised regions of higher power dissipation. This task investigates the steady‑state Joule heating pattern that develops in a graphene sheet with two different crack configurations: a rectangular crack that lies entirely within the interior (not touching any boundary) and a crack that extends inward from one of the sample's edges. The goal is to compute, by finite‑element simulation, the resulting power‑density field for each configuration so that the effect of the crack on the heating pattern can be examined.

## Approach
The simulation is performed with the finite‑element method under the static‑current approximation of Maxwell's equations. The model represents a rectangular graphene layer with two opposing edges treated as conductive plates held at a constant voltage; the remaining boundaries are electrically insulating. Two geometries are meshed and solved: one containing an interior rectangular crack, and one containing a crack that begins at the left boundary and penetrates into the layer. Open‑source tools are used throughout: NETGEN (version 5.1) for mesh generation and ELMER FEM for solving the partial differential equations, yielding the steady‑state Joule heating power density (W/m²) at every point of the domain. The computed fields are then exported as regular‑grid CSV files for subsequent analysis.

## Reproduction target
Produce two output files:

- `interior_crack_heat.csv` – power density field for the layer with a rectangular interior crack.
- `border_crack_heat.csv` – power density field for the layer with a crack starting from the left border.

Each file is a CSV with columns `x`, `y`, `power_density` (in SI units). The grid spacing must be fine enough to resolve local features. The deliverable is these two raw fields; a hidden verifier will analyze the local‑maxima patterns (number and spatial location of the largest power‑density peaks) to determine whether the simulated heating distribution exhibits the physically expected behavior for each crack type.

## Assets

- NETGEN: https://ngsolve.org/
- ELMER FEM: https://www.csc.fi/web/elmer

## Workflow steps

### Step 1: Generate finite element meshes
- Role: process
- Action: Using NETGEN, create two finite element meshes: one for a graphene layer with a rectangular interior crack (not touching boundaries), and one with a crack starting from the left border and extending inward. The meshes must resolve the crack geometry and include the full domain with conductive contacts on two opposite edges.
- Evidence: none

### Step 2: FEM simulation for interior rectangular crack
- Role: scored (load-bearing)
- Action: Run ELMER FEM on the interior crack mesh. Apply boundary conditions corresponding to a constant voltage (e.g., 40 V) between two opposite conductive plates, and solve the static current approximation to obtain the steady‑state Joule heating distribution (power density, W/m²). Export the resulting field to a CSV with columns x, y, power_density.
- Output file: `/app/outputs/interior_crack_heat.csv`
- Format: csv
- Contract: CSV with columns x (float), y (float), power_density (float, W/m^2).
- Scoring: scored by hidden verifier

### Step 3: FEM simulation for border crack
- Role: scored (load-bearing)
- Action: Run ELMER FEM on the border crack mesh with the same voltage and boundary conditions, and compute the Joule heating distribution. Export the result to a CSV with columns x, y, power_density. The border crack starts from the left border of the domain.
- Output file: `/app/outputs/border_crack_heat.csv`
- Format: csv
- Contract: CSV with columns x (float), y (float), power_density (float, W/m^2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interior_crack_heat.csv`
- `/app/outputs/border_crack_heat.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interior_crack_heat.csv
- path: `/app/outputs/interior_crack_heat.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Steady-state Joule heating distribution field for the graphene layer with a rectangular interior crack. The checker will analyze the field to verify exactly two hot spots (local maxima) are present at the crack ends.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `power_density`
  - `units`:
    - `x`: m
    - `y`: m
    - `power_density`: W/m^2

### border_crack_heat.csv
- path: `/app/outputs/border_crack_heat.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Steady-state Joule heating distribution field for the graphene layer with a crack starting from the left border. The checker will verify exactly one hot spot (local maximum) near the crack tip.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `power_density`
  - `units`:
    - `x`: m
    - `y`: m
    - `power_density`: W/m^2

Notes: The checker will perform a structural audit: for interior_crack_heat.csv, it identifies local maxima and verifies exactly two exist with locations near the crack ends; for border_crack_heat.csv, exactly one local maximum near the crack tip. The agent may choose reasonable domain dimensions and material properties; the hot spot patterns should be robust to these choices.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interior_crack_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "power_density"
        ],
        "units": {
          "x": "m",
          "y": "m",
          "power_density": "W/m^2"
        }
      },
      "description": "Steady-state Joule heating distribution field for the graphene layer with a rectangular interior crack. The checker will analyze the field to verify exactly two hot spots (local maxima) are present at the crack ends."
    },
    {
      "file": "border_crack_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "power_density"
        ],
        "units": {
          "x": "m",
          "y": "m",
          "power_density": "W/m^2"
        }
      },
      "description": "Steady-state Joule heating distribution field for the graphene layer with a crack starting from the left border. The checker will verify exactly one hot spot (local maximum) near the crack tip."
    }
  ],
  "notes": "The checker will perform a structural audit: for interior_crack_heat.csv, it identifies local maxima and verifies exactly two exist with locations near the crack ends; for border_crack_heat.csv, exactly one local maximum near the crack tip. The agent may choose reasonable domain dimensions and material properties; the hot spot patterns should be robust to these choices."
}
```

## How you are scored
A hidden verifier independently loads each CSV file and identifies local maxima of the `power_density` field (points where the value exceeds all four nearest neighbours on the regular grid). For each crack case, the verifier checks structural properties of the detected hot spots — specifically, how many local maxima exist and where they lie relative to the crack — and awards a partial score for each correct pattern. The final reward is the weighted sum of these partial scores. Reporting a single summary number is not sufficient; the verifier works directly with the raw output fields.
