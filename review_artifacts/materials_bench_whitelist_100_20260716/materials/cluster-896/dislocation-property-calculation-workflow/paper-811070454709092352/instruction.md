# Computing Dislocation Critical Thickness in Anisotropic Heteroepitaxial Growth via Phase-Field Crystal Simulation

## Problem background
Heteroepitaxial growth involves depositing a crystalline film on a substrate with a different lattice parameter. This creates misfit strain, which as the film thickens can relax through the nucleation of misfit dislocations. A key quantity is the critical thickness, the film thickness at which dislocations first form. The anisotropic phase-field crystal (APFC) model extends the standard phase-field crystal approach to describe non-cubic crystal symmetries, allowing the study of how film anisotropy and substrate orientation affect dislocation nucleation. In this task, you will use the APFC model to simulate the growth of thin films on a vicinal substrate (a surface with steps) under positive misfit (ε > 0), and compute the inverse critical thickness P and the free energy derivative change at the point of dislocation formation for isotropic and anisotropic films.

## Approach
You will implement the APFC model in two dimensions. The model consists of a free energy functional that depends on a phase field ϕ and an anisotropic Laplacian operator that encodes the shear of the crystal lattice. The evolution of ϕ is governed by a conserved dynamics equation. For a substrate with an isotropic (shear-free) lattice, you will set up a vicinal surface by rotating the substrate lattice to an angle θ = 6.178°. On top of this substrate, a film grows with an imposed lattice misfit ε and, optionally, a shear anisotropy s_f (zero for isotropic, 0.10825 for anisotropic). The film growth is simulated by solving the APFC equation numerically on a 2D grid with periodic boundary conditions in the lateral direction and a constant mass flux at the top boundary. The simulations are run without noise until misfit dislocations have nucleated. From the time evolution, you will extract the critical film thickness H_c (in unit cells) where dislocations first appear, and then compute the inverse critical thickness P = (1 + log(H_c))/H_c. Additionally, you will compute the free energy derivative averaged over sections normal to the growth direction and determine the change in this derivative that occurs at the critical thickness. The workflow will be carried out for six combinations of misfit ε (0.06, 0.09, 0.12) and film shear s_f (0 and 0.10825).

## Reproduction target
Produce a CSV file `results.csv` with one row for each of the six simulation conditions (ε, s_f). The columns must be: epsilon (float), s_f (float), H_c (integer, critical thickness in unit cells), P (float, computed as (1+log(H_c))/H_c), and free_energy_derivative (float, the change in the section-averaged free energy derivative at the critical thickness). Your results will be evaluated by a hidden verifier that checks how well the reported P and free_energy_derivative agree with reference values and satisfy physical consistency criteria. Note that merely reporting plausible numbers without running the required APFC simulations will not produce values that pass the verification checks.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute model coefficients and equilibrium properties
- Role: process
- Action: Derive anisotropic Laplace operator coefficients a_ij and b_ijkl for the y-shear lattice orientation variant, using the shear parameter s (substrate s=0, film s_f=0.10825). Compute equilibrium wave numbers and equilibrium amplitude A_min by minimizing the coarse-grained free energy, assuming stretch parameter epsilon=0, undercooling r=-0.25, and average density f0=0.285.
- Evidence: `/app/outputs/model_params.json`

### Step 2: Initialize simulation domain with vicinal substrate and film
- Role: process
- Action: Set up a 2D simulation grid of size Lx=1440, Ly=1440 with dx = 4π/(9√3), dy = π/4. Initialize the substrate region (s=0, λ=1) using the rotated vicinal lattice formula with angle θ=6.178°. Initialize the film region with misfit parameter λ_f = 1 + ε (ε = 0.06, 0.09, 0.12) and film shear s_f (0 or 0.10825). Apply periodic boundary conditions in x and constant mass flux at the top boundary.
- Evidence: `/app/outputs/initial_setup.txt`

### Step 3: Run APFC film growth simulations
- Role: process
- Action: For each combination of misfit ε (0.06, 0.09, 0.12) and film anisotropy s_f (0, 0.10825), evolve the phase field φ using the APFC evolution equation with time step Δt=0.0009, no noise, until dislocations have nucleated. Save the time-dependent φ field or sufficient snapshots to later determine the critical thickness.
- Evidence: `/app/outputs/simulation_phi.npy`

### Step 4: Extract critical thickness and free energy derivative, write results.csv
- Role: scored (load-bearing)
- Action: For each simulation condition, determine the critical film thickness H_c (in unit cells) where dislocations first form. Compute inverse critical thickness P = (1 + log(H_c)) / H_c. Compute the change in free energy derivative Δ(∂F/∂φ) at the critical thickness using section-averaged formulas. Write results.csv with one row per (ε, s_f) configuration.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with header: epsilon (float), s_f (float), H_c (integer), P (float), free_energy_derivative (float). One row per (ε, s_f) configuration.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file containing extracted critical thickness and free energy derivative for six configurations of misfit epsilon and film shear s_f.
- schema:
  - `type`: table
  - `required_columns`: `epsilon`, `s_f`, `H_c`, `P`, `free_energy_derivative`
  - `column_types`:
    - `epsilon`: float
    - `s_f`: float
    - `H_c`: integer
    - `P`: float
    - `free_energy_derivative`: float
  - `description`: Each row corresponds to one simulation condition (epsilon, s_f). H_c is critical thickness in unit cells. P is inverse critical thickness computed as (1+log(H_c))/H_c. free_energy_derivative is the change in free energy derivative at critical thickness.

Notes: The checker compares reported P and free_energy_derivative against the paper's published values for the given configurations, with tolerances accounting for implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "epsilon",
          "s_f",
          "H_c",
          "P",
          "free_energy_derivative"
        ],
        "column_types": {
          "epsilon": "float",
          "s_f": "float",
          "H_c": "integer",
          "P": "float",
          "free_energy_derivative": "float"
        },
        "description": "Each row corresponds to one simulation condition (epsilon, s_f). H_c is critical thickness in unit cells. P is inverse critical thickness computed as (1+log(H_c))/H_c. free_energy_derivative is the change in free energy derivative at critical thickness."
      },
      "description": "CSV file containing extracted critical thickness and free energy derivative for six configurations of misfit epsilon and film shear s_f."
    }
  ],
  "notes": "The checker compares reported P and free_energy_derivative against the paper's published values for the given configurations, with tolerances accounting for implementation differences."
}
```

## How you are scored
Your submission is scored by an automated hidden verifier. The verifier reads `results.csv` and compares the P and free_energy_derivative columns against a hidden gold standard—that is, reference values obtained from the paper's findings for the same conditions. The comparison allows for tolerances that account for implementation differences (different code, numerical schemes, but same physical model). Additionally, the verifier checks that the overall qualitative trends of the results (e.g., dependence on misfit and anisotropy) are physically reasonable. The final score is a weighted combination of the accuracy of the P and free_energy_derivative values and the satisfaction of consistency checks. You are not required to match any exact pre‑announced number; instead, the closer your computed values are to the hidden reference, the higher the score, provided the mandatory consistency requirements are met. Simply outputting a guessed value or copying numbers from elsewhere will result in a low score.
