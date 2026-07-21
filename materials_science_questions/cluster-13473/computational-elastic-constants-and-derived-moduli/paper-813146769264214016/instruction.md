# Percolation Thresholds and Critical Exponent Ratios in Elastic Media

## Problem background
Many heterogeneous solids exhibit a percolation-type transition in their elastic properties: as bonds are removed, the material eventually loses rigidity. The critical behavior near this percolation point can depend on the material's elastic constants, in particular the ratio λ/μ of the Lamé coefficients. This task investigates how the percolation threshold p_c and the critical exponent ratio f/ν_e (denoted δ) vary with λ/μ, using a central‑force model on a specially constructed triangular lattice. The goal is to compute p_c and δ for three distinct λ/μ values, providing insight into the relationship between macroscopic elasticity and percolation phenomena.

## Approach
The simulation uses a triangular lattice with a √3 × √3 unit cell and two bond‑force constants, k_a and k_b. The Lamé coefficient ratio λ/μ is mapped to the force‑constant ratio x = k_a/k_b through the analytic relation λ/μ = (4x² + 3x + 2)/(8x + 1). For a given λ/μ, hexagonal networks of several linear sizes L are generated with random bond occupation probability p. For each configuration the bulk modulus B_L(p) is computed by applying fixed boundary displacements, relaxing the interior nodes iteratively, and extracting the total elastic energy. The critical parameters p_c and δ are then extracted via the generalized phenomenological renormalization method: define ζ_{LL'}(p) = ln(B_L(p)/B_{L'}(p))/ln(L/L') for pairs of system sizes, and locate the intersection of these ζ curves for the largest sizes. This analysis is repeated for three target ratios λ/μ = 1, 5, and 10.

## Reproduction target
Produce a file results.json containing the percolation threshold p_c and the exponent ratio δ = f/ν_e for each of the three Lamé coefficient ratios: λ/μ = 1, 5, and 10. The values must be computed from the bulk modulus simulations and the renormalization analysis described in the workflow steps; simply reporting numbers without performing the simulations will fail the verification. **The verifier reads your intermediate data (`bulk_modulus_data.csv`) and recomputes p_c and δ independently; you must also generate this CSV as described below.**

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Random network bulk modulus simulations
- Role: process
- Action: Implement the central-force model on a √3×√3 triangular lattice with two force constants k_a and k_b. For each target Lamé coefficient ratio λ/μ = 1, 5, 10, determine the force constant ratio x = k_a/k_b using the analytic mapping λ/μ = (4x²+3x+2)/(8x+1) (solve for the positive root x). Simulate hexagonal networks of linear sizes L ranging from 10 to 45 (in bond units) with random bond occupation probability p. For each realization, compute the bulk modulus B_L(p) by applying fixed boundary displacements, relaxing interior nodes iteratively until the discretized equilibrium equations are satisfied, and calculating the total elastic energy. Save the computed bulk modulus values for all (λ/μ, L, p) combinations.
- Evidence: `/app/outputs/bulk_modulus_data.csv`

#### Detailed model description
**Lattice geometry and force constants**
- The underlying triangular lattice is defined by the basis vectors a₁ = (1, 0) and a₂ = (1/2, √3/2).  All lengths are in units of the bond length (lattice constant a = 1).
- The √3 × √3 reconstruction introduces two force constants, k_a and k_b, that are assigned to bonds according to a superimposed honeycomb pattern.
- **Rule for assigning k_a and k_b bonds:**
  - Every node is labelled by an integer pair (i, j) such that its position is r(i,j) = i·a₁ + j·a₂.
  - Define two classes of nodes:
    * Class A: nodes for which i+j is even.
    * Class B: nodes for which i+j is odd.
  - Define the **honeycomb (k_a) bonds** as the following unordered nearest-neighbour pairs:
    * Starting from a Class-A node at (i, j), the three honeycomb neighbours are at:  
      (i+1, j), (i, j+1), (i−1, j+1).
    * Starting from a Class-B node at (i, j), the three honeycomb neighbours are at:  
      (i−1, j), (i, j−1), (i+1, j−1).
    (Each such pair appears once; the rule is symmetric – the reverse link from the neighbour automatically falls into the same definition.)
  - All other nearest-neighbour bonds of the triangular lattice are assigned the force constant **k_b**.
- **Verification**: each node possesses exactly three k_a bonds (forming a honeycomb network) and three k_b bonds.

**Construction of a hexagonal simulation cell**
- Generate a large patch of the infinite lattice.
- Retain only the nodes that lie inside a regular hexagon of side L (in units of the bond length), centered at the origin.  
  The hexagon can be defined as the set of points (x, y) satisfying:
  |y| ≤ √3 L/2,  |x| ≤ L, and |√3 x ± y| ≤ √3 L.
- Mark the nodes whose nearest neighbours lie outside the hexagon as **boundary nodes**; all other retained nodes are **interior nodes**.

**Computing B_L(p) for a given realisation**
- For a given occupation probability p, each bond is independently removed (with probability 1−p) or kept (with probability p). Only kept bonds contribute to the energy.
- Apply a small isotropic compressive strain ε (for example ε = 0.001 or smaller; ensure linear response). Displace the boundary nodes according to the macroscopic strain field:
  **u_boundary(r) = − ε (r − r_center)**, where r_center is the center of the hexagon.
- Free the interior nodes and minimize the potential energy (Eq. (2) of the paper):
  H = ½ Σ_{〈i,j〉} k_{ij} [ (u_i − u_j) · r̂_{ij} ]² ,
  where the sum runs over all kept nearest-neighbour bonds, r̂_{ij} is the unit vector from i to j, and k_{ij} is either k_a or k_b.  
  This minimization is equivalent to solving the discrete equilibrium equations for the interior nodes:
  Σ_{j∈neighbours(i)} k_{ij} [ (u_i − u_j) · r̂_{ij} ] r̂_{ij} = 0  for all interior i.
- Solve the resulting linear system (e.g. by conjugate gradient or direct solver).  
- Compute the total elastic energy E_total = H after relaxation.
- The bulk modulus for this configuration is
  **B = 2 E_total / (A ε²)**,  
  where the area of the hexagon is A = (3√3/2) L².
- For each set of parameters (λ/μ, L, p), perform multiple random realizations (bond occupation patterns) and average the resulting bulk moduli to obtain B_L(p). A typical number of realizations per data point can be chosen in the range 10–30 (fewer for larger L if computationally expensive).

**Saving intermediate data**
- Save the computed averaged B_L(p) values in a CSV file at `/app/outputs/bulk_modulus_data.csv` with columns exactly named:
  `lambda_mu`, `L`, `p`, `B`
  (lambda_mu is the integer 1, 5, or 10; L is the integer side length; p is the occupation probability; B is the bulk modulus).

### Step 2: Generalized phenomenological renormalization analysis
- Role: scored (load-bearing)
- Action: From the bulk modulus data generated in step‑1, compute the function ζ_{LL'}(p) = ln(B_L(p)/B_{L'}(p))/ln(L/L') for all pairs of system sizes. Determine the percolation threshold p_c and the critical exponent ratio δ = f/ν_e from the intersection of ζ curves, using the three largest system sizes. Report the results for λ/μ = 1, 5, and 10.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with string keys '1', '5', '10' mapping to objects with numeric keys 'p_c' (float) and 'delta' (float). Example (structure only): {"1": {"p_c": 0.XX, "delta": Y.YY}, "5": {"p_c": 0.XX, "delta": Y.YY}, "10": {"p_c": 0.XX, "delta": Y.YY}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/bulk_modulus_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Percolation threshold p_c and critical exponent ratio f/ν_e (delta) for λ/μ = 1, 5, and 10. The checker performs its own renormalization analysis on the CSV data; however this file must contain correctly formatted fields.
- schema:
  - `type`: object
  - `required`:
    - `1`:
      - `p_c`: float
      - `delta`: float
    - `5`:
      - `p_c`: float
      - `delta`: float
    - `10`:
      - `p_c`: float
      - `delta`: float
  - `items`: object
  - `required_columns`:
  - `units`: object

### bulk_modulus_data.csv
- path: `/app/outputs/bulk_modulus_data.csv`
- format: csv
- purpose: process (used by the verifier for scoring)
- description: Raw bulk modulus data from the simulations. The verifier reads this file and recomputes p_c and delta using the renormalization method; this is the primary data used for scoring.
- schema:
  - `required_columns`:
    - `lambda_mu`
    - `L`
    - `p`
    - `B`

Notes: The intermediate bulk modulus data (`bulk_modulus_data.csv`) is generated by the process step and is **read by the verifier** to independently compute p_c and δ. The values in `results.json` are not directly used for scoring, but the file must exist and follow the declared schema (shape check). Scoring is therefore determined by the quality of the CSV data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema":