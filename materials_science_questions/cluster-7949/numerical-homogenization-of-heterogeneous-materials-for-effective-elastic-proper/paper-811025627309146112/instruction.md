# Effective Elastic Properties of Hexagonal Honeycomb Core via Analytical RVE Homogenization

## Problem background
Determining the effective elastic properties of cellular cores is essential for lightweight structural design. An energetic homogenisation procedure can evaluate the strain energy in a representative volume element (RVE) using closed-form cell-wall element formulations. This enables direct computation of the full elasticity tensor for arbitrary cell geometries without the need for mesh-sensitive finite element analysis. In this task, you will implement such a procedure for a hexagonal honeycomb core to compute the nine independent stiffness components at four different cell-wall angles.

## Approach

### RVE Geometry and Material Parameters
The representative volume element (RVE) of the hexagonal core is a parallelogram of width l (along x̄₁) and height 2l sin Φ (along x̄₂). The following five nodal points define the cell wall vertices in the global (x̄₁, x̄₂) plane (origin at node 1):
- Node 1: (0, 0)
- Node 2: (0, 2l sin Φ)
- Node 3: (l (1 − cos Φ), −l sin Φ)
- Node 4: (l (1 − cos Φ),  l sin Φ)
- Node 5: (l, 0)

These five nodes are connected by five straight cell wall elements (with local x̃ directed from the first to the second node):
- Bottom horizontal wall: node 1 → node 5, thickness t_h = 2 t, length l₅ = l
- Inclined wall: node 1 → node 3, thickness t, length l₁₃ = 2 l sin(Φ/2)
- Inclined wall: node 3 → node 5, thickness t, length l₃₅ = l
- Inclined wall: node 2 → node 4, thickness t, length l₂₄ = 2 l sin(Φ/2)
- Inclined wall: node 4 → node 5, thickness t, length l₄₅ = l

The base cell wall length is l = 1. The cell wall base thickness t is determined from the relative density ρ̅ = 0.02, defined as the ratio of solid volume to total RVE volume. The total solid volume is the sum of (element length) × (its thickness) × h, and the RVE volume is (area of parallelogram) × h = (l · 2l sin Φ) × h = 2 l² h sin Φ. Therefore

ρ̅ = [ t·(l₁₃ + l₃₅ + l₂₄ + l₄₅) + 2t·l₅ ] / (2 l² sin Φ) = t·(4 l sin(Φ/2) + 2 l + 2 l) / (2 l² sin Φ) = (t (4 sin(Φ/2) + 4)) / (2 l sin Φ) = (2 t (1 + sin(Φ/2))) / (l sin Φ).

Solving for t yields

t = (ρ̅ · l sin Φ) / (2 (1 + sin(Φ/2))).

The cell wall material is aluminium-like: Young's modulus E = 72200 MPa, Poisson ratio ν = 0.34. The core height is h = 10 l.

### Timoshenko Beam Element Stiffness Matrix
For a straight cell wall of length l_e, thickness t_e, and height h, the element stiffness matrix in the local coordinate system (x̃₁ along the beam axis, x̃₂ perpendicular in-plane, x̃₃ out-of-plane) is given by

K̃_loc = (E h t_e) / (l_e (1 − ν²)) · M,

with M a dimensionless 8×8 matrix. The nodal degrees of freedom in local ordering are
[ũ(1)₁, ũ(1)₂, ũ(1)₃, Δφ̃(1), ũ(2)₁, ũ(2)₂, ũ(2)₃, Δφ̃(2)].

Using the abbreviation β = (1/(1+α)²)((t_e/l_e)² + ½ α² (1−ν)) and α = (12/5)(1−ν)(t_e/l_e)² (Timoshenko shear parameter), the non‑zero entries of M are:

| row / col         | 0 (ũ₁₁) | 1 (ũ₁₂) | 2 (ũ₁₃) | 3 (Δφ̃₁) | 4 (ũ₂₁) | 5 (ũ₂₂) | 6 (ũ₂₃) | 7 (Δφ̃₂) |
|-------------------|---------|---------|---------|-------------------|---------|---------|---------|-------------------|
| 0 (ũ₁₁)          |  1      |  0      |  0      |  0                | −1      |  0      |  0      |  0                |
| 1 (ũ₁₂)          |  0      |  β      |  0      |  (l_e/2)β        |  0      | −β      |  0      |  (l_e/2)β        |
| 2 (ũ₁₃)          |  0      |  0      | (1−ν)/2 |  0                |  0      |  0      |−(1−ν)/2 |  0                |
| 3 (Δφ̃₁)          |  0      | (l_e/2)β|  0      | (l_e²/4 β + t_e²/12) | 0   |−(l_e/2)β| 0       | (l_e²/4 β − t_e²/12) |
| 4 (ũ₂₁)          | −1      |  0      |  0      |  0                |  1      |  0      |  0      |  0                |
| 5 (ũ₂₂)          |  0      | −β      |  0      |−(l_e/2)β         |  0      |  β      |  0      |−(l_e/2)β         |
| 6 (ũ₂₃)          |  0      |  0      |−(1−ν)/2 |  0                |  0      |  0      | (1−ν)/2 |  0                |
| 7 (Δφ̃₂)          |  0      | (l_e/2)β|  0      | (l_e²/4 β − t_e²/12) | 0   |−(l_e/2)β| 0       | (l_e²/4 β + t_e²/12) |

Note: the indices above correspond to Python 0‑based numbering; the physical ordering is as stated. The matrix is symmetric.

Additionally, an initial strain load due to a macroscopic through-thickness strain ε̅₃₃ appears as a force vector on the nodes:

K̃_ε33_loc = (E h t_e) / (l_e (1 − ν²)) · [−l_e ν, 0, 0, 0, +l_e ν, 0, 0, 0]ᵀ.

This vector must be added to the global force vector when the loading case includes ε̅₃₃.

### Global Assembly and Solution
Each element stiffness matrix K̃_loc is rotated from its local coordinates to the global (x̄₁, x̄₂) system before assembly. The rotation matrix R is a block-diagonal 8×8 matrix with four identical 2×2 blocks for the in‑plane displacement components (x̄₁, x̄₂) and identity blocks for the out‑of‑plane displacement and rotation. The global stiffness matrix K_glob is assembled by adding the contributions of all elements.

Periodic boundary conditions (Eq. 15 in the paper) and rigid‑body constraints (Eq. 18) are applied to the global system by eliminating redundant degrees of freedom. The independent macroscopic strain states are chosen as the six elementary tensors: (ε₁₁=1, others 0), (ε₂₂=1), (ε₃₃=1), (2ε₁₂=1), (2ε₁₃=1), (2ε₂₃=1). For each strain state the corresponding displacement boundary conditions are enforced according to Eq. (17), and the system is solved for the unknown nodal degrees of freedom. The total strain energy W of the RVE is computed as W = ½ Σ_element (u_locᵀ K_loc u_loc) (for the appropriate loading), where u_loc includes the solved nodal displacements and the prescribed macroscopic strain contributions. The strain energy density w = W / (RVE reference volume). The effective elasticity tensor components C_ijkl are then obtained by numerical differentiation (Eq. 5) using the energy densities from the six single‑strain cases and the 15 pairwise‑strain cases (needed for mixed derivatives). For simple orthotropic response, only the 21 combinations are needed.

You will carry out this process for each of the four angles Φ = 60°, 90°, 120°, 150°. The computed nine independent components (C₁₁₁₁, C₂₂₂₂, C₁₁₂₂, C₁₁₃₃, C₂₂₃₃, C₃₃₃₃, C₁₂₁₂, C₁₃₁₃, C₂₃₂₃) must be written to /app/outputs/effective_properties.csv.

## Reproduction target
Implement the analytical RVE homogenisation procedure described above and compute, for each of the four cell-wall angles, the nine independent components of the effective elasticity tensor: C1111, C2222, C1122, C1133, C2233, C3333, C1212, C1313, C2323. The results must be written to /app/outputs/effective_properties.csv in the format: angle_deg (integer), component (string, e.g. C1111), value_MPa (float). The file must contain 4 angles × 9 components = 36 rows. Use the specified geometry (cell wall length l = 1, core height h = 10 l, relative density 0.02 giving the cell wall thickness) and material parameters (E = 72200 MPa, ν = 0.34). Your computed values will be compared against hidden trusted reference values derived from the original analysis.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute effective elastic properties via analytical RVE homogenization
- Role: scored (load-bearing)
- Action: Implement the analytical homogenization procedure for a hexagonal honeycomb core. For each cell wall angle Φ=60°, 90°, 120°, 150°: define the RVE geometry (nodal coordinates given in the Approach section, with l=1, cell wall thickness t derived from relative density 0.02, core height h=10*l, material constants E=72200 MPa, ν=0.34). For each straight cell wall element, compute the 8×8 element stiffness matrix using the closed-form expressions provided in the Approach section (with Timoshenko beam theory, α as defined there). Assemble the global stiffness matrix, apply periodic boundary conditions and rigid-body motion constraints. For each of the six independent macroscopic strain states, solve for nodal deflections. Compute the total strain energy of the RVE for each strain state and extract the nine independent elasticity tensor components via numerical differentiation. Write the results for all four angles to /app/outputs/effective_properties.csv.
- Output file: `/app/outputs/effective_properties.csv`
- Format: csv
- Contract: Columns: angle_deg (int), component (string), value_MPa (float). Rows: 4 angles × 9 components = 36 rows. Components: C1111, C2222, C1122, C1133, C2233, C3333, C1212, C1313, C2323.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_properties.csv
- path: `/app/outputs/effective_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nine independent components of the effective elasticity tensor for each cell wall angle.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `component`, `value_MPa`

Notes: The hidden checker compares each value to paper-reported gold values digitized from Fig. 10, scoring via relative error with full credit within 5% tolerance. The 9 components are C1111, C2222, C1122, C1133, C2233, C3333, C1212, C1313, C2323.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "component",
          "value_MPa"
        ]
      },
      "description": "Nine independent components of the effective elasticity tensor for each cell wall angle."
    }
  ],
  "notes": "The hidden checker compares each value to paper-reported gold values digitized from Fig. 10, scoring via relative error with full credit within 5% tolerance. The 9 components are C1111, C2222, C1122, C1133, C2233, C3333, C1212, C1313, C2323."
}
```

## How you are scored
Your submitted CSV file will be read by an automated verifier. For each component at each angle, the verifier computes a relative error between your reported value and the hidden reference value. The component-level score is then determined by a function that decreases from 1.0 (perfect match) to 0.0 as the error increases beyond an acceptable threshold. The overall task score is the average over all 36 component–angle pairs. You must run the genuine homogenisation procedure; simply guessing or hardcoding values will not produce the correct results.
