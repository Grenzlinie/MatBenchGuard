# Magnetoelastic coupling analysis of fcc antiferromagnets via symmetry-resolved Hamiltonian

## Problem background
In fcc first-kind antiferromagnets, the magnetic structure is described by three wave vectors Qx, Qy, Qz. The general multiple spin density wave (MSDW) state can couple to lattice distortions through magnetoelastic interactions, yielding a rich finite-temperature phase diagram that may include cubic, tetragonal (c/a < 1 and c/a > 1), and orthorhombic phases. This problem investigates the interplay between MSDW variables and symmetry strains by constructing a microscopic Hamiltonian. The goal is to compute the phase diagram in the coupling–temperature plane and the temperature dependence of the lattice strains and MSDW component amplitudes, providing quantitative insight into the structure and stability of these magnetic phases.

## Approach
The system is modeled by a Hamiltonian consisting of three parts: an MSDW energy expressed in symmetry-adapted variables X2 and X3 (functions of the squared amplitudes Ax², Ay², Az²), a bilinear magnetoelastic coupling between these variables and the symmetry strains ε2, ε3, and a harmonic elastic energy. The partition function Z(ε2, ε3) is obtained by numerically integrating exp(−H/kBT) over the sphere Ax²+Ay²+Az²=1. The free energy F(ε2, ε3) = −kBT ln Z is then minimized with respect to ε2 and ε3 to find equilibrium strains. The stable phase at each (coupling, temperature) point is assigned by examining the signs of the equilibrium strains: both zero → cubic; ε3 ≠ 0 and ε2 = 0 → tetragonal (c/a < 1 for ε3 < 0, c/a > 1 for ε3 > 0); both non-zero → orthorhombic. This procedure is carried out on a grid of coupling strengths √g and temperatures kBT using fixed parameters A=1.0, B=0.5, C=0.5, κ=5000.0.

## Reproduction target
Produce three scored artifacts:

1. `phase_diagram.csv` — A grid over √g (approximately 9.4 to 13) and kBT (0.0 to about 0.15) with columns `sqrt_g`, `kBT`, and `phase_label` (one of `cubic`, `tet_less`, `tet_more`, `ortho`), representing the computed stable phase at each point.

2. `strains_vs_T.csv` — At the representative coupling √g = 11.2, for a range of temperatures kBT from 0.0 to about 0.15, output the equilibrium symmetry strains ε2 and ε3 with columns `kBT`, `epsilon_2`, `epsilon_3`.

3. `msdw_components_vs_T.csv` — At the same coupling √g = 11.2 and temperature grid, compute the Boltzmann-weighted averages ⟨Ax²⟩, ⟨Ay²⟩, ⟨Az²⟩ and output them with columns `kBT`, `Ax2_avg`, `Ay2_avg`, `Az2_avg`.

All outputs must be written to `/app/outputs/` following the exact column schemas specified in the workflow steps.

## Assets

- Python scientific computing stack: numpy scipy

## Workflow steps

### Step 1: Define Hamiltonian and integration method
- Role: process
- Action: Implement the total Hamiltonian H = A(X₂²+X₃²) + B(X₃³−3X₃X₂²) + C(X₃³−3X₃X₂²)² + g(ε₂X₂+ε₃X₃) + (κ/2)(ε₂²+ε₃²) with X₂=(A_x²−A_y²)/√2, X₃=(2A_z²−A_x²−A_y²)/√6, subject to normalization A_x²+A_y²+A_z²=1. Set up numerical integration of the partition function Z(ε₂,ε₃)=∫_{sphere} exp(−H/k_BT) dA. Use the fixed parameters: A=1.0, B=0.5, C=0.5, κ=5000.0, with variable coupling g.
- Evidence: none

### Step 2: Compute phase diagram in the √g–k_BT plane
- Role: scored (load-bearing)
- Action: For a grid of √g values from about 9.4 to 13 and k_BT values from 0.0 to about 0.15, numerically integrate the partition function Z(ε₂,ε₃) and compute the free energy F = −k_BT ln Z. For each (√g, k_BT) point, minimize F with respect to ε₂, ε₃ to obtain equilibrium strains. Classify the stable phase from the signs: both ε₂,ε₃ zero → cubic; ε₃≠0, ε₂=0 → tetragonal (c/a<1 for ε₃<0, c/a>1 for ε₃>0); ε₂≠0 and ε₃≠0 → orthorhombic. Write a CSV with columns (sqrt_g, kBT, phase_label) to phase_diagram.csv.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Columns: sqrt_g (float), kBT (float), phase_label (string, one of: cubic, tet_less, tet_more, ortho).
- Scoring: scored by hidden verifier

### Step 3: Compute temperature dependence of symmetry strains at √g=11.2
- Role: scored
- Action: At the representative coupling √g=11.2, for a range of temperatures k_BT from 0.0 to about 0.15, compute the equilibrium strains ε₂ and ε₃ by minimizing the free energy F(ε₂,ε₃) obtained from the partition function integration. Write a CSV with columns (kBT, epsilon_2, epsilon_3) to strains_vs_T.csv.
- Output file: `/app/outputs/strains_vs_T.csv`
- Format: csv
- Contract: Columns: kBT (float), epsilon_2 (float), epsilon_3 (float).
- Scoring: scored by hidden verifier

### Step 4: Compute temperature dependence of MSDW component averages at √g=11.2
- Role: scored
- Action: At √g=11.2 and using the same temperature grid as the previous step, compute the Boltzmann-weighted averages ⟨A_x²⟩, ⟨A_y²⟩, ⟨A_z²⟩ by integrating A_i² exp(−H/k_BT) over the sphere A_x²+A_y²+A_z²=1 with the equilibrium strains (from the free energy minimization). Write a CSV with columns (kBT, Ax2_avg, Ay2_avg, Az2_avg) to msdw_components_vs_T.csv.
- Output file: `/app/outputs/msdw_components_vs_T.csv`
- Format: csv
- Contract: Columns: kBT (float), Ax2_avg (float), Ay2_avg (float), Az2_avg (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/strains_vs_T.csv`
- `/app/outputs/msdw_components_vs_T.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Grid of (√g, k_BT) points with the computed stable phase label. The checker recomputes phase boundaries from these labels and compares them to hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `sqrt_g`, `kBT`, `phase_label`
  - `items`: object
  - `units`: object

### strains_vs_T.csv
- path: `/app/outputs/strains_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature dependence of equilibrium symmetry strains ε₂ and ε₃ at √g=11.2. The checker compares the values at selected temperatures to hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `kBT`, `epsilon_2`, `epsilon_3`
  - `items`: object
  - `units`: object

### msdw_components_vs_T.csv
- path: `/app/outputs/msdw_components_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature dependence of the MSDW component squared averages ⟨A_x²⟩, ⟨A_y²⟩, ⟨A_z²⟩ at √g=11.2. The checker compares the values at selected temperatures to hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `kBT`, `Ax2_avg`, `Ay2_avg`, `Az2_avg`
  - `items`: object
  - `units`: object

Notes: No solver internals or gold values are disclosed. The output files contain the computed grid points and quantities; the hidden checker extracts and compares the relevant features with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "sqrt_g",
          "kBT",
          "phase_label"
        ],
        "items": {},
        "units": {}
      },
      "description": "Grid of (√g, k_BT) points with the computed stable phase label. The checker recomputes phase boundaries from these labels and compares them to hidden reference values."
    },
    {
      "file": "strains_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "kBT",
          "epsilon_2",
          "epsilon_3"
        ],
        "items": {},
        "units": {}
      },
      "description": "Temperature dependence of equilibrium symmetry strains ε₂ and ε₃ at √g=11.2. The checker compares the values at selected temperatures to hidden gold values."
    },
    {
      "file": "msdw_components_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "kBT",
          "Ax2_avg",
          "Ay2_avg",
          "Az2_avg"
        ],
        "items": {},
        "units": {}
      },
      "description": "Temperature dependence of the MSDW component squared averages ⟨A_x²⟩, ⟨A_y²⟩, ⟨A_z²⟩ at √g=11.2. The checker compares the values at selected temperatures to hidden gold values."
    }
  ],
  "notes": "No solver internals or gold values are disclosed. The output files contain the computed grid points and quantities; the hidden checker extracts and compares the relevant features with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three scored artifacts. It extracts phase boundaries from your `phase_diagram.csv` and compares them to reference boundaries, and checks the strain and MSDW average values at selected temperature points against reference curves. The evaluation rewards reproduction of the correct physical trends and quantitative predictions; reporting numbers alone is not sufficient—the verifier re-derives quantities from your output. The final reward is a weighted combination of the scores from the individual artifacts.
