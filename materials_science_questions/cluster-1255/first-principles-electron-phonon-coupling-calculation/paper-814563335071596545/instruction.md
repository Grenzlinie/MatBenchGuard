# Phonon-softening model for Tc enhancement in 2D superconductors

## Problem background
Superconductivity in low-dimensional systems is sensitive to phonon softening at surfaces and edges, which can alter the electron‑phonon coupling and, in turn, the superconducting transition temperature. In this task, we investigate how the geometry of a two‑dimensional superconducting layer — flat sheet, hollow sphere, hollow cylinder — influences the average transition temperature relative to the bulk, using a classical spring‑network model of collective lattice vibrations within coherence volumes.

## Approach
The superconducting layer is discretized into a grid of coherence volumes, each assigned a collective spring constant. For each grid point, an effective spring constant is computed by combining the springs of its nearest neighbours according to classical series and parallel rules, both in the 2D plane and in a thick 3D block that serves as a bulk reference. The ratio of the bulk reference stiffness to the 2D stiffness quantifies the local phonon softening. This softening is mapped to an enhancement of the electron‑phonon coupling (proportional to the inverse stiffness ratio raised to the power 0.25). Under the assumption of a position‑independent Debye frequency, BCS proportionality relates this enhancement to a local superconducting transition temperature ratio. For the curved geometries (hollow sphere, hollow cylinder), the ionic charge is first corrected by the ratio of the Coulomb potential in the curved geometry to that in the flat sheet, using a vector‑sum approach. Averaging the local Tc ratios over the surface yields the macroscopic average Tc/Tc_bulk ratio for each geometry.

## Reproduction target
Produce a JSON file `tc_ratios.json` containing the five average Tc/Tc_bulk ratios: the entire 800×800 rectangular film (`rectangle_mean`), its four edges (`rectangle_edges`), its four corners (`rectangle_corners`), a hollow sphere of radius 127 coherence lengths and thickness 1 (`sphere`), and a hollow cylinder of length 800, radius 127, thickness 1 (`cylinder`).

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Define 2D grid for flat sheet
- Role: process
- Action: Set up an 800x800 grid of coherence volumes to represent the 2D rectangular superconducting film, with nearest-neighbour connectivity.
- Evidence: none

### Step 2: Compute k(x,y) for flat sheet
- Role: process
- Action: For each grid point, compute the net effective spring constant k(x,y) by summing contributions from the four nearest in-plane neighbours using classical series and parallel rules.
- Evidence: none

### Step 3: Compute 3D reference k_3D(x,y)
- Role: process
- Action: Extend the grid into a 3D block of size 800x800x400 with 6-neighbour connectivity and compute the effective spring constant k(x,y,400) for each (x,y) column, acting as the bulk-like stiffness reference.
- Evidence: none

### Step 4: Compute R(x,y) and local Tc ratio map
- Role: process
- Action: Calculate the stiffness ratio R(x,y) = k(x,y,400)/k(x,y). Derive the local electron-phonon interaction enhancement proportional to R^(-0.25) and, using BCS proportionality under the assumption of a position-independent Debye frequency, compute a spatial map of local Tc ratios.
- Evidence: none

### Step 5: Compute Tc ratio for hollow sphere
- Role: process
- Action: For a hollow sphere of radius 127 coherence lengths and thickness 1 coherence length, compute the curvature-corrected ionic charge number using the potential-energy vector sum U_sphere/U_flat, then repeat the spring-network and electron-phonon coupling analysis to obtain the average Tc ratio.
- Evidence: none

### Step 6: Compute Tc ratio for hollow cylinder
- Role: process
- Action: For a hollow cylinder of length 800, radius 127, thickness 1 coherence length, compute the curvature-corrected charge (U_cylinder/U_flat) and repeat the spring-network and electron-phonon coupling analysis to obtain the average Tc ratio.
- Evidence: none

### Step 7: Write Tc ratios to tc_ratios.json
- Role: scored (load-bearing)
- Action: Extract from the computed Tc maps the average Tc ratios for the entire 800x800 rectangular film, its edges, its corners, the hollow sphere, and the hollow cylinder. Write these five ratios to tc_ratios.json as a JSON object with keys 'rectangle_mean', 'rectangle_edges', 'rectangle_corners', 'sphere', 'cylinder'.
- Output file: `/app/outputs/tc_ratios.json`
- Format: json
- Contract: A JSON object with five keys: rectangle_mean (float), rectangle_edges (float), rectangle_corners (float), sphere (float), cylinder (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_ratios.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_ratios.json
- path: `/app/outputs/tc_ratios.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Average superconducting transition temperature ratios for the rectangular film (mean, edges, corners), hollow sphere, and hollow cylinder, relative to bulk Tc.
- schema:
  - `type`: object
  - `required_keys`:
    - `rectangle_mean`: float
    - `rectangle_edges`: float
    - `rectangle_corners`: float
    - `sphere`: float
    - `cylinder`: float

Notes: The ratios are computed from the local Tc distribution derived from the spring-network model. Exact reproduced values depend on the correct implementation of series/parallel rules and curvature corrections; the checker will compare against the paper's reported ratios with an appropriate hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_ratios.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": {
          "rectangle_mean": "float",
          "rectangle_edges": "float",
          "rectangle_corners": "float",
          "sphere": "float",
          "cylinder": "float"
        }
      },
      "description": "Average superconducting transition temperature ratios for the rectangular film (mean, edges, corners), hollow sphere, and hollow cylinder, relative to bulk Tc."
    }
  ],
  "notes": "The ratios are computed from the local Tc distribution derived from the spring-network model. Exact reproduced values depend on the correct implementation of series/parallel rules and curvature corrections; the checker will compare against the paper's reported ratios with an appropriate hidden tolerance."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/tc_ratios.json` and compare each of the five ratio values against independently determined reference values using a hidden tolerance. Your final reward is proportional to the number of ratios that fall within the tolerance (each ratio contributes equally). You must obtain the ratios by running the computational pipeline described in the workflow; the verifier’s tolerance is set to distinguish a correct reproduction from a generic guess. Ensure your output file is well‑formed JSON and contains all five keys with numeric values.
