# Faceted grain boundary energy difference computation

## Problem background
Polycrystalline films often contain grain boundaries that affect stress relaxation.  This task investigates a model where a faceted grain boundary – composed of alternating asymmetric tilt boundary facets – may become energetically favourable relative to a planar symmetric tilt boundary.  The model treats each facet as a superdislocation and derives the total energy difference ΔW between the two states, including elastic self- and interaction energies, surface energy, and the coupling between the superdislocations and the misfit‑stress field in the film.  Your goal is to compute ΔW for a specific set of parameter combinations to determine when the faceted configuration is preferred.

## Approach
The faceted grain boundary is modelled as a vertical wall of N edge superdislocations with alternating Burgers vectors.  The energy difference ΔW has three contributions:

1. **Elastic energy** – the self‑energy of each superdislocation plus the pairwise interaction energy between every pair of dislocations in the wall.  The formulas involve the shear modulus G, Poisson ratio ν, facet geometry (L, N, α), the superdislocation Burgers vector B = n·b (b is the lattice Burgers vector), and the dislocation core radius r₀ = B.

2. **Surface energy** – the difference in grain‑boundary area between the faceted and the planar boundary, which depends on the surface energy density γ.

3. **Misfit‑stress coupling** – the work done by the superdislocation array against the uniform misfit stress in the film, a term that depends on the misfit parameter f, the film thickness H (or equivalently the number of facets N and their length L), the facet angle α, and the elastic constants.

You must implement the complete analytical expression for ΔW (all three terms) using the material constants provided below.  The film thickness H is not held fixed; for a given H you should adjust the number of facets N so that H ≈ N·L·sin(α/2), with L = 10 nm and α = 90° (unless varied).  Compute ΔW for the specified sweeps and store the results in a CSV file.

## Reproduction target
Compute the energy difference ΔW (in joules) for the following parameter sweeps:

1. Misfit parameter sweep:  f ∈ {0.001, 0.002, 0.003, 0.004, 0.005} with superdislocation Burgers vector B = n·b for n = 1, 2, 3.  Use the default values H ≈ 700 nm (N = 100, L = 10 nm, α = 90°).

2. Film thickness sweep:  H ∈ {200, 400, 600, 800, 1000} **nm**.  For each thickness adjust the number of facets N while keeping L = 10 nm and α = 90°; use fixed f = 0.004 and B = b (n = 1).

3. Facet angle sweep:  α ∈ {60°, 90°, 120°, 150°} (in degrees).  Use fixed f = 0.003 and B = b (n = 1) with the default N = 100 (L = 10 nm, so H ≈ 700 nm).

Write all computed ΔW values to `/app/outputs/delta_W_results.csv`.  The CSV must have exactly these columns (case‑sensitive, order may vary): `misfit_parameter`, `Burgers_vector_n`, `film_thickness_nm`, `angle_deg`, `delta_W_J`.  Each row corresponds to one parameter combination.  Do not include any extra rows or summary statistics.

## Assets
The only required assets are standard scientific computing libraries (Python with NumPy is recommended).  No external datasets, models, or configuration files are needed; all necessary model equations and parameter values are described in this instruction.

## Workflow steps

### Step 1: Compute energy difference ΔW for all parameter sweeps
- Role: scored (load-bearing)
- Action: Implement the energy-difference model for a faceted grain boundary represented as a wall of alternating superdislocations. Use the given material constants (G=100 GPa, ν=0.3, γ=0.6 J/m², b=0.4 nm, L=10 nm, N=100, r0=B) and the analytical expression for ΔW that includes elastic self-energy, pairwise dislocation interactions, surface energy, and misfit-stress coupling. Evaluate ΔW for the following parameter combinations: (1) misfit parameter f ∈ {0.001, 0.002, 0.003, 0.004, 0.005} with superdislocation Burgers vector B = n*b for n=1,2,3; (2) film thickness H ∈ {200, 400, 600, 800, 1000} nm (adjust N accordingly) at f=0.004, n=1; (3) facet angle α ∈ {60°, 90°, 120°, 150°} at f=0.003, n=1. Write the computed ΔW for each combination to delta_W_results.csv.
- Output file: `/app/outputs/delta_W_results.csv`
- Format: csv
- Contract: CSV with columns: misfit_parameter (float, dimensionless), Burgers_vector_n (int, multiplier of b), film_thickness_nm (float, nm), angle_deg (float, degrees), delta_W_J (float, Joules). Each row corresponds to one parameter combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_W_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_W_results.csv
- path: `/app/outputs/delta_W_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed energy difference ΔW for each parameter combination listed in the task. The hidden checker will compare each value to a digitized reference from the paper and verify monotonic trends (ΔW decreases with f, increases with B for small f, decreases with H in the favorable range, and exhibits a minimum in α).
- schema:
  - `type`: table
  - `required_columns`: `misfit_parameter`, `Burgers_vector_n`, `film_thickness_nm`, `angle_deg`, `delta_W_J`
  - `units`:
    - `misfit_parameter`: dimensionless
    - `Burgers_vector_n`: integer
    - `film_thickness_nm`: nm
    - `angle_deg`: degrees
    - `delta_W_J`: J

Notes: The task is pure computation using only the public material constants and the analytical expression. No external data or files are required. The agent must implement the formula in code (Python with numpy/scipy is appropriate). All parameter sweeps are explicit. The hidden gold values are approximate digitizations from the paper's figures; tolerances absorb implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_W_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "misfit_parameter",
          "Burgers_vector_n",
          "film_thickness_nm",
          "angle_deg",
          "delta_W_J"
        ],
        "units": {
          "misfit_parameter": "dimensionless",
          "Burgers_vector_n": "integer",
          "film_thickness_nm": "nm",
          "angle_deg": "degrees",
          "delta_W_J": "J"
        }
      },
      "description": "Computed energy difference ΔW for each parameter combination listed in the task. The hidden checker will compare each value to a digitized reference from the paper and verify monotonic trends (ΔW decreases with f, increases with B for small f, decreases with H in the favorable range, and exhibits a minimum in α)."
    }
  ],
  "notes": "The task is pure computation using only the public material constants and the analytical expression. No external data or files are required. The agent must implement the formula in code (Python with numpy/scipy is appropriate). All parameter sweeps are explicit. The hidden gold values are approximate digitizations from the paper's figures; tolerances absorb implementation differences."
}
```

## How you are scored
A hidden verifier will evaluate your submitted `delta_W_results.csv`.  The verifier compares each computed ΔW value against a hidden reference answer derived from the physical model and assesses the numerical accuracy of your implementation.  In addition, the verifier performs high‑level consistency checks on the patterns of your results to ensure the computed values conform to physically expected monotonic trends.  To obtain full credit you must faithfully implement the analytical expression for ΔW and compute it for every specified parameter combination.  There is no need to guess the answer; simply implement the model as described.
