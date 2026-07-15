# Dislocation Pile-up Crossover Simulation

## Problem background
In highly concentrated solid solutions, plastic deformation occurs via the propagation of dislocation pile-ups. When two such pile-ups glide in opposite directions on parallel crystallographic planes, their interaction can impede crossover. Understanding the critical applied resolved shear stress required for them to cross over as a function of glide‑plane separation and number of dislocations provides insight into the minimum spacing observed between slip bands and informs work‑hardening models. In this task you will simulate two symmetric dislocation pile‑ups in the γ phase of a nickel‑based superalloy and compute the critical stress needed for them to pass each other.

## Approach
The model consists of two identical pile‑ups, each containing n straight dislocations, gliding on parallel planes separated by a distance d. The dislocations are assumed to be of mixed character, so both edge and screw components of the Burgers vector are considered. Each dislocation experiences: (i) the applied shear stress τ_a, (ii) a frictional stress (300 MPa on the leading dislocation, 30 MPa on all others), and (iii) pairwise interaction forces with every other dislocation in the same pile‑up and in the opposing pile‑up, using the analytic force expressions for edge‑edge and screw‑screw interactions. By symmetry the equilibrium positions of the two pile‑ups are mirror images about the origin. For a given (d, n) the task is to find the smallest applied stress τ_a for which a static equilibrium solution can no longer be found – this critical stress marks the onset of crossover. The simulation uses standard elastic constants for MC2 γ phase: Burgers vector b≈0.176 nm, shear modulus μ≈79 GPa, Poisson’s ratio ν≈0.3.

## Reproduction target
Produce a CSV file `/app/outputs/simulation_results.csv` with columns `d_nm` (separation in nanometres), `n` (integer number of dislocations per pile‑up), and `tau_a_MPa` (critical applied shear stress in MPa). Compute the critical stress for a range of separations d that includes values from about 10 nm up to several hundred nanometres, for at least two distinct pile‑up sizes n (e.g., 5, 10, 15, 20). The table should clearly show the dependence on both d and n; the more d‑points you include the better the quantitative assessment will be.

## Assets

- SciPy numerical library: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Pile-up crossover simulation
- Role: scored
- Action: Implement the force-balance model for two symmetric dislocation pile-ups gliding on parallel planes separated by distance d. Incorporate the edge and screw interaction force formulas as given. Fix the frictional stress on the first head dislocation to τ_f = 300 MPa and use a lattice friction of 30 MPa for all other dislocations. For each combination of glide-plane separation d (cover a range that includes values down to ~10 nm) and pile-up size n (at least two values, e.g., 5, 10, 15, 20), numerically find the critical applied resolved shear stress τ_a at which the pile-ups begin to cross over (i.e., the head dislocations can move past each other). Write the results as a table.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: Columns: d_nm (float, glide-plane separation in nanometres), n (integer, number of dislocations per pile-up), tau_a_MPa (float, critical applied resolved shear stress in MPa). Each row corresponds to one computed condition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The computed critical applied resolved shear stress τ_a for two symmetric dislocation pile-ups to cross over, as a function of glide-plane separation d and number of dislocations per pile-up n. Each row is a (d, n) condition. Two additional structural requirements (monotonicity of τ_a with d for fixed n, and existence of a steep rise at small d) are also checked.
- schema:
  - `type`: table
  - `required_columns`: `d_nm`, `n`, `tau_a_MPa`
  - `units`:
    - `d_nm`: nm
    - `n`: dimensionless
    - `tau_a_MPa`: MPa

Notes: The parameter-estimation stage that derived τ_f=300 MPa from experimental data is intentionally omitted; the task directly uses the reported τ_f. The scoring combines per-point numerical agreement with hidden reference values (digitized from Figure 10) and structural checks (monotonic decrease of τ_a with increasing d for each n, and high τ_a for d ≤ 30 nm).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "d_nm",
          "n",
          "tau_a_MPa"
        ],
        "units": {
          "d_nm": "nm",
          "n": "dimensionless",
          "tau_a_MPa": "MPa"
        }
      },
      "description": "The computed critical applied resolved shear stress τ_a for two symmetric dislocation pile-ups to cross over, as a function of glide-plane separation d and number of dislocations per pile-up n. Each row is a (d, n) condition. Two additional structural requirements (monotonicity of τ_a with d for fixed n, and existence of a steep rise at small d) are also checked."
    }
  ],
  "notes": "The parameter-estimation stage that derived τ_f=300 MPa from experimental data is intentionally omitted; the task directly uses the reported τ_f. The scoring combines per-point numerical agreement with hidden reference values (digitized from Figure 10) and structural checks (monotonic decrease of τ_a with increasing d for each n, and high τ_a for d ≤ 30 nm)."
}
```

## How you are scored
A hidden verifier will read your `simulation_results.csv` and compare each (d, n, τ_a) tuple against a reference table derived from the original simulation results. The scoring function uses a relative tolerance (tighter for small d, wider for large d) and assigns the largest fraction of points for quantitative agreement. Additionally, the verifier checks two structural properties: (a) for each fixed n, τ_a must decrease monotonically with increasing d; (b) for separations d ≤ 30 nm the critical stress must exceed a high hidden threshold (otherwise it is not a physically realistic crossover solution). The exact tolerances and thresholds are not revealed. The final reward is a weighted combination of numerical accuracy (≈70 %) and structural correctness (≈30 %).
