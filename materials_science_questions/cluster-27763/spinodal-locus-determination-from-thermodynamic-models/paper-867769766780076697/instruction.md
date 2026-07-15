# Solidification front speed and bond-angle disorder in soft-core fluids

## Problem background
Dynamical density functional theory (DDFT) provides a dynamical extension of classical density functional theory, allowing simulation of time-dependent density profiles for soft condensed matter. This task investigates solidification fronts advancing into a supercooled two-dimensional fluid of soft penetrable particles. When the uniform fluid is quenched to a state point where a crystalline phase is thermodynamically stable, a solidification front propagates into the metastable/unstable liquid. The front speed reflects the instability mechanism, and the structure left behind can exhibit disorder. For a one-component system of GEM-4 particles, the task measures the steady propagation speed of a front initiated by a line perturbation. For a binary GEM-8 mixture in which competing square and hexagonal motifs can coexist, the task simulates the solidification process and quantifies the resulting bond-angle distribution at long times, providing insight into structural disorder.

## Approach
Implement the DDFT using the random phase approximation (RPA) free energy functional. The pairwise interaction is a generalized exponential model (GEM) potential v(r) = ε exp(-(r/R)^n); consider n=4 for the one-component fluid and n=8 for the binary mixture. The Helmholtz free energy functional consists of the ideal gas part and an excess term given by one half the integral over products of densities and the pair potential (the RPA treatment). The dynamics follows the conserved DDFT equation ∂ρ/∂t = Γ ∇·(ρ ∇ δΩ/δρ), where Ω is the grand potential functional.

For the one-component GEM-4 fluid, set βε=1 and average density ρR²=8. Prepare a uniform initial density with a small random perturbation along a vertical line x=0. Evolve the density field on a 2D grid until a steady solidification front is established. Track the front position over time to extract the dimensionless steady speed c/(Γk_BT).

For the binary GEM-8 mixture, set all interaction energies to βε_ij=1, size ratios R22/R11=1.5, R12/R11=1, total density ρR11²=8, and concentration φ=0.5. Start from uniform densities and perturb along x=0. Integrate the two-component DDFT until the dimensionless time t*=400. From the final total density profile, identify all density peaks exceeding a suitable threshold, construct the Delaunay triangulation of these peak positions, and compute the normalized histogram of bond angles (0–180 degrees, bin width 1°).

## Reproduction target
Produce exactly two scored outputs:
1. **Front speed** for the one-component solidification: a single floating-point number written to `front_speed_one_component.txt`, representing the dimensionless steady front speed c/(Γk_BT) for the GEM-4 fluid at βε=1, ρR²=8.
2. **Bond-angle distribution** for the binary mixture at t*=400: a CSV file `binary_bond_angle_distribution.csv` with columns `angle_degrees` (integer, range 0–180) and `probability_density` (float). The probability density must be normalized so that the sum over all bins equals 1 (bin width is 1°).

## Assets
No external datasets, pre-trained models, or third-party simulation packages are required. All simulations can be implemented from scratch using standard Python scientific computing libraries (e.g., NumPy, SciPy, Matplotlib). You may install these as needed during the workflow.

## Workflow steps

### Step 1: Run one-component DDFT simulation
- Role: process
- Action: Implement DDFT with the RPA free energy functional for a one-component GEM-4 fluid. Initialize uniform density at βε=1, ρR²=8, add a small random perturbation along a line x=0, and evolve the 2D density profile until a steady solidification front is established.
- Evidence: `/app/outputs/one_component_density_snapshot.png`

### Step 2: Report one-component front speed
- Role: scored
- Action: From the DDFT density profiles, track the position of the solidification front over time and compute the steady dimensionless front speed c/(Γk_BT). Write the result as a single floating-point number.
- Output file: `/app/outputs/front_speed_one_component.txt`
- Format: txt
- Contract: A single line containing a floating-point number.
- Scoring: scored by hidden verifier

### Step 3: Run binary mixture DDFT simulation
- Role: process
- Action: Implement the two-component DDFT with the RPA free energy functional for a binary GEM-8 mixture. Set parameters βε_ij=1, R22/R11=1.5, R12/R11=1, total density ρR11²=8, concentration φ=0.5. Initialize uniform densities and perturb along x=0. Evolve the system until dimensionless time t*=400, producing the final 2D density profiles for both species.
- Evidence: `/app/outputs/binary_density_snapshot.png`

### Step 4: Compute binary bond-angle distribution
- Role: scored (load-bearing)
- Action: From the final total density profile at t*=400, locate density peaks. Construct the Delaunay triangulation on these peaks and compute the distribution of bond angles over all triangles. Normalize the histogram to unit probability density. Write a CSV with columns 'angle_degrees' (0-180, bin width 1°) and 'probability_density'.
- Output file: `/app/outputs/binary_bond_angle_distribution.csv`
- Format: csv
- Contract: CSV with columns angle_degrees (int, 0-180) and probability_density (float). The distribution should be normalized to sum to 1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/front_speed_one_component.txt`
- `/app/outputs/binary_bond_angle_distribution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### front_speed_one_component.txt
- path: `/app/outputs/front_speed_one_component.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Solidification front speed for the one-component GEM-4 fluid at ρR²=8, βε=1.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the dimensionless solidification front speed c/(Γk_BT).

### binary_bond_angle_distribution.csv
- path: `/app/outputs/binary_bond_angle_distribution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Bond-angle distribution from Delaunay triangulation of the binary solid at t*=400. Used to verify the presence and persistence of disorder via three-peak structure.
- schema:
  - `type`: table
  - `required_columns`: `angle_degrees`, `probability_density`

Notes: The target for the front speed is compared to the paper-reported value (~90) using a relative tolerance (20%). The bond-angle distribution is checked structurally for local maxima near 45°, 60°, and 90° and for peak widths indicative of persistent disorder. No gold values or tolerances are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "front_speed_one_component.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the dimensionless solidification front speed c/(Γk_BT)."
      },
      "description": "Solidification front speed for the one-component GEM-4 fluid at ρR²=8, βε=1."
    },
    {
      "file": "binary_bond_angle_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_degrees",
          "probability_density"
        ]
      },
      "description": "Bond-angle distribution from Delaunay triangulation of the binary solid at t*=400. Used to verify the presence and persistence of disorder via three-peak structure."
    }
  ],
  "notes": "The target for the front speed is compared to the paper-reported value (~90) using a relative tolerance (20%). The bond-angle distribution is checked structurally for local maxima near 45°, 60°, and 90° and for peak widths indicative of persistent disorder. No gold values or tolerances are revealed here."
}
```

## How you are scored
A hidden verifier scores each output independently. The front speed is compared to a reference value with an appropriate tolerance that accommodates implementation variability. The bond-angle distribution is examined for the presence and location of expected structural features (peak positions and widths) that characterize the solid formed. The two scores are combined into a final reward between 0 and 1. Reporting a number or a histogram without actually performing the DDFT simulations is unlikely to satisfy the verifier's criteria.
