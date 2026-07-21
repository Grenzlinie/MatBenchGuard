# Local Hexagonal Ordering in Tapped Granular Disk Packings

## Problem background
Granular materials subjected to vertical tapping undergo slow density relaxation accompanied by spontaneous local ordering. In two-dimensional packings of monodisperse frictional hard disks, the competition between ordered hexagonal domains and disordered regions controls the macroscopic compaction dynamics. Voronoi tessellation and a dimensionless shape factor ζ = C²/(4πS) — where C and S are the perimeter and area of a Voronoi cell — quantify the local circularity of the cell and serve as sensitive indicators of emerging order. This work investigates whether the fraction of near‑regular hexagonal cells increases during compaction and whether the system exhibits a memory effect: i.e., how the density responds to an abrupt change of the tapping intensity, and whether the response can be linked to the microstructure at the moment of the switch.

## Approach
The core of the approach is an event‑driven molecular dynamics simulation of N=1000 monodisperse, frictional hard disks under gravity. The grains interact through the Walton collision model, capturing normal energy loss (coefficient of normal restitution ε₀), Coulomb friction (μ), and surface roughness (β₀). The dissipative disks are classified as type A (ε₀=0.6, μ=0.4, β₀=0.5, critical velocity v₀=0.02).

A single tap is simulated in two stages: (i) the entire packing is expanded vertically by a factor ξ; (ii) the assembly recompresses dynamically under gravity with randomised initial velocities until it settles into a mechanically stable static packing. Simulations are run at constant tapping intensities ξ=0.7%, 3%, and 0.5% to generate sequences of static configurations.

From the ξ=0.7% sequence, Voronoi tessellations are computed at selected stages using the Quickhull algorithm. For each interior Voronoi cell the shape factor ζ is calculated; the distribution of ζ and the fraction of cells with near‑hexagonal shape (ζ below a defined threshold) are monitored over the compaction history.

The memory‑effect experiments begin from the static configurations saved at the 30th tap of the ξ=3% and ξ=0.5% base runs. At that instant the tapping intensity is switched — scenario 0: ξ drops from 3% to 0.5%; scenario 1: ξ rises from 0.5% to 3% — and tapping continues for at least 20 further cycles. The packing fraction ρ is recorded at every tap to capture the transient response and subsequent relaxation.

## Reproduction target
Produce two scored artifacts:

1. **`shape_factor_cells.json`** — For the ξ=0.7% constant‑intensity simulation, compute the shape factor ζ for every interior Voronoi cell at tap numbers t = 2, 8, 15, 30, 50, and 70. Store the results as a JSON object mapping tap number strings to lists of ζ values.

2. **`memory_effect.csv`** — For the two memory‑effect protocols (scenario 0: 3% → 0.5%; scenario 1: 0.5% → 3% switched at t=30), record the packing fraction ρ for every tap from the start of each scenario (t=0) until at least t=50. Write a CSV with columns `scenario`, `tap`, and `density`.

The correctness of the simulation and analysis will be assessed from these artifacts by a hidden verifier that performs structural audits on the raw data. The verifier will compute summary statistics (e.g., fraction of cells with ζ below a threshold, mean ζ) from `shape_factor_cells.json` and examine the density time series around the intensity switch from `memory_effect.csv`. The scoring criteria are based on whether the observed trends are consistent with the physical phenomena of local ordering and memory effects in tapped granular disk packings, but the exact expected quantitative trends are not disclosed.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Run base tapping simulations
- Role: process
- Action: Implement an event-driven molecular dynamics simulation for N=1000 monodisperse frictional hard disks (diameter d=0.01784 in units where container width L=1, mass m=1, gravity g=1) using the Walton collision model. Set normal restitution coefficient epsilon0=0.6, friction mu=0.4, roughness beta0=0.5, and critical velocity v0=0.02 (type A disks). Run constant-intensity tapping sequences for expansion factors xi = 0.7%, 3%, and 0.5%. A shake cycle consists of a vertical expansion by factor xi followed by dynamical recompression under gravity with random initial velocities. Save the disk centre coordinates at every tap for each sequence.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Compute Voronoi shape factors for xi=0.7% runs
- Role: scored (load-bearing)
- Action: For the xi=0.7% simulation, load the disk positions at taps t = 2, 8, 15, 30, 50, 70. For each tap, compute the Voronoi tessellation using Quickhull (e.g., scipy.spatial.Voronoi). For every interior (non-boundary) cell, compute the shape factor zeta = C^2 / (4 pi S), where C is the cell perimeter and S is its area. Write a JSON object mapping each tap number (as a string) to the list of zeta values for all interior cells at that tap.
- Output file: `/app/outputs/shape_factor_cells.json`
- Format: json
- Contract: A JSON object with keys "2", "8", "15", "30", "50", "70" (tap numbers as strings), each mapping to an array of float numbers representing zeta values for all interior Voronoi cells at that tap.
- Scoring: scored by hidden verifier

### Step 3: Run memory-effect simulations
- Role: process
- Action: From the states saved at t=30 of the xi=3% and xi=0.5% base runs, continue tapping with the switched intensities: scenario 0 — change from xi=3% to xi=0.5% at t=30; scenario 1 — change from xi=0.5% to xi=3% at t=30. Continue each simulation for at least 20 additional taps, saving the disk positions at each tap.
- Evidence: `/app/outputs/memory_simulation_log.txt`

### Step 4: Output memory-effect packing fractions
- Role: scored (load-bearing)
- Action: From the memory-effect simulation states, compute the packing fraction rho(t) = (N * pi * (d/2)^2) / (L^2) for both scenarios. For each scenario, include a row for tap=30 (the density at the moment of the switch, taken from the base run before the intensity change) and a row for each subsequent tap (31, 32, ...) up to at least tap=50. Write the CSV with columns: scenario (integer 0 or 1), tap (integer), density (float).
- Output file: `/app/outputs/memory_effect.csv`
- Format: csv
- Contract: CSV with columns: scenario (integer, 0 for 3%→0.5%, 1 for 0.5%→3%), tap (integer), density (float). For each scenario, include a row for tap=30 and a row for each subsequent tap 31, 32, ... up to at least tap=50. The tap numbers correspond to the absolute tap count from the beginning of the base run.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/shape_factor_cells.json`
- `/app/outputs/memory_effect.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### shape_factor_cells.json
- path: `/app/outputs/shape_factor_cells.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Shape factor zeta values for interior Voronoi cells at six selected tapping stages. Used to verify microstructural evolution during compaction.
- schema:
  - `type`: object
  - `required`: `2`, `8`, `15`, `30`, `50`, `70`
  - `items`:
    - `type`: array
    - `items`:
      - `type`: number

### memory_effect.csv
- path: `/app/outputs/memory_effect.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Packing density evolution under two memory-effect protocols. The CSV must include tap 30 (pre-switch density) and taps 31,32,... up to at least 50, with scenario labels. Used to verify the system's density response under abrupt intensity changes.
- schema:
  - `type`: table
  - `required_columns`: `scenario`, `tap`, `density`
  - `units`:
    - `scenario`: integer (0 or 1)
    - `tap`: integer
    - `density`: float

Notes: The checker will perform structural audits: for shape_factor_cells.json it will compute summary statistics (e.g., fraction of cells with zeta below a threshold, mean zeta) and check for trends consistent with physical compaction; for memory_effect.csv it will examine the density evolution around the intensity switch (taps 30, 31, 32) to assess the memory effect. Specific trend directions are not disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "shape_factor_cells.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "2",
          "8",
          "15",
          "30",
          "50",
          "70"
        ],
        "items": {
          "type": "array",
          "items": {
            "type": "number"
          }
        }
      },
      "description": "Shape factor zeta values for interior Voronoi cells at six selected tapping stages. Used to verify microstructural evolution during compaction."
    },
    {
      "file": "memory_effect.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "scenario",
          "tap",
          "density"
        ],
        "units": {
          "scenario": "integer (0 or 1)",
          "tap": "integer",
          "density": "float"
        }
      },
      "description": "Packing density evolution under two memory-effect protocols. The CSV must include tap 30 (pre-switch density) and taps 31,32,... up to at least 50, with scenario labels. Used to verify the system's density response under abrupt intensity changes."
    }
  ],
  "notes": "The checker will perform structural audits: for shape_factor_cells.json it will compute summary statistics (e.g., fraction of cells with zeta below a threshold, mean zeta) and check for trends consistent with physical compaction; for memory_effect.csv it will examine the density evolution around the intensity switch (taps 30, 31, 32) to assess the memory effect. Specific trend directions are not disclosed."
}
```

## How you are scored
A hidden verifier will read your `shape_factor_cells.json` and `memory_effect.csv` and perform structural audits. It will compute summary statistics (e.g., fraction of cells with ζ below a threshold, mean ζ) for the shape‑factor data and inspect the density time series around the tapping intensity switch for the memory‑effect data. The verifier's scoring criteria are based on whether these statistics exhibit behavior consistent with the physical phenomena of local ordering and memory effects in a tapped granular packing. The exact expected trends are not disclosed. The two stages contribute to the overall reward with the memory‑effect stage carrying a higher weight; passing only shape/format checks without exhibiting the required trends will yield a low score. Reporting a self‑computed summary is not sufficient — the verifier recomputes the trends from the raw cell‑level ζ values and per‑tap densities you provide.
