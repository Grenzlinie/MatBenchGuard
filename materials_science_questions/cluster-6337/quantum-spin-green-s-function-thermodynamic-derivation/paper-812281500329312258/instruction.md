# Iterative graphical reduction for 3D cubic Ising critical point

## Problem background
Ising spin systems on a regular lattice are a fundamental model of phase transitions. An iterative graphical reduction scheme has been proposed to express thermodynamic quantities and correlation functions. By writing the sum of delta functions in a special form, each spin is represented by a large number of points, and the partition sum becomes a sum over diagrams of pairings. Removing points from a reference spin leads to an iterative procedure that relates the partition sum and correlation functions. This work investigates approximate re-writings of the delta-function sum, leading to closed equations for correlation functions that involve coefficient functions L_n(α). For the three-dimensional simple-cubic nearest-neighbour Ising model, the scheme yields a self-consistent condition whose solution determines the critical interaction parameter A_c, i.e., the ratio of exchange coupling to temperature at the phase transition. The task is to compute these coefficient functions L_n(α) and then obtain the critical A_c from the self-consistent equations.

## Approach
The method starts from a continuous representation of the Ising partition sum obtained by expressing each spin's delta-function constraint as a sequence of peaked functions. This yields a Gaussian integral that is evaluated by Wick's theorem, giving a diagrammatic expansion where each vertex corresponds to a spin with a fixed number of points. By choosing one reference spin and iteratively removing its points, one obtains coupled linear recurrences for the partition sum Z'(k) and a correlation sum G'(k), parameterised by an auxiliary integer n (the number of point pairs on the reference spin). In the simplest approximation, the ratios G_ij(k)/Z(k) are taken to be independent of k and equal to the exact correlation functions. The recurrences then decouple and involve a single scalar parameter α that is a quadratic form in the couplings and correlations. From these recurrences one extracts coefficient functions L_n(α) that relate the spin-spin correlation function to the couplings. For finite n (n=1,2) L_n can be obtained by direct iteration or from closed analytic expressions. In the limit n→∞ the recurrences simplify and L_∞(α) is given by tanh(√α)/√α for α≥0 and tan(√|α|)/√|α| for α<0. Using these L_n functions, the Fourier-transformed correlation function on a d-dimensional lattice satisfies a self-consistency equation. For the three-dimensional cubic lattice with near-neighbour interactions, the condition for a diverging susceptibility yields an integral equation in the first Brillouin zone that must be solved numerically to find the critical interaction strength A_c. The required steps are (1) compute and tabulate L_1, L_2, and L_∞ on a suitable α grid, and (2) use L_∞ to solve the Brillouin-zone integral and the self-consistent equation to obtain A_c.

## Reproduction target
Compute the coefficient functions L_1(α), L_2(α), and L_∞(α) on a reasonably dense, uniformly spaced grid of α that covers the domain where these functions exhibit their characteristic behaviour (including any singularities and the limits α→±∞). Write the results to a CSV file `L_functions.csv`. Then, using L_∞(α) and the geometry of the three-dimensional simple-cubic lattice with nearest-neighbour Ising interactions, perform a numerical Brillouin-zone integration and solve the self-consistent system to determine the critical interaction parameter A_c. Write the computed value as a single floating-point number to `critical_point.txt`.

## Assets
No external datasets, pretrained models, or weight files are required. The computation can be carried out using standard open-source numerical libraries freely available from public repositories (e.g., NumPy, SciPy). The agent is responsible for installing any needed packages at runtime.

## Workflow steps

### Step 1: Compute L_n(α) coefficient functions
- Role: scored
- Action: Derive or implement the iterative reduction scheme to obtain the coefficient functions L_1(α), L_2(α), and L_∞(α). Evaluate L_1(α) using its closed-form expression, L_∞(α) as tanh(√α)/√α (and the negative-α branch), and L_2(α) by numeric solution of the recursion. Compute the functions on a sufficiently dense uniform grid of α to show their behaviour, and write the results to L_functions.csv.
- Output file: `/app/outputs/L_functions.csv`
- Format: csv
- Contract: CSV with header: alpha (float), L1 (float), L2 (float), L_inf (float). At least 200 uniformly spaced rows covering a range that includes the singularities and the limits α→±∞.
- Scoring: scored by hidden verifier

### Step 2: Compute critical point A_c for the 3D cubic Ising model
- Role: scored (load-bearing)
- Action: Using L_∞(α)=tanh(√α)/√α and the self-consistent equations for the spin‑spin correlation function, perform a numerical Brillouin‑zone integration for the 3D simple‑cubic lattice with nearest‑neighbour interactions. Solve for the critical interaction parameter A_c (the point where the susceptibility diverges) and write the resulting value to critical_point.txt.
- Output file: `/app/outputs/critical_point.txt`
- Format: txt
- Contract: A single line containing a floating‑point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/L_functions.csv`
- `/app/outputs/critical_point.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### L_functions.csv
- path: `/app/outputs/L_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Coefficient functions L_n(α) for n=1,2,∞ evaluated on a grid of α. The checker verifies L1, L2, L_inf against the paper‑derived analytical expressions within prescribed tolerances.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `L1`, `L2`, `L_inf`
  - `units`:
    - `alpha`: dimensionless
    - `L1`: dimensionless
    - `L2`: dimensionless
    - `L_inf`: dimensionless

### critical_point.txt
- path: `/app/outputs/critical_point.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Critical interaction parameter A_c obtained by solving the self‑consistent equations with L_∞(α). The checker compares the submitted value to the paper‑reported value with absolute tolerance.
- schema:
  - `type`: text
  - `required`:
    - `value`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "L_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "L1",
          "L2",
          "L_inf"
        ],
        "units": {
          "alpha": "dimensionless",
          "L1": "dimensionless",
          "L2": "dimensionless",
          "L_inf": "dimensionless"
        }
      },
      "description": "Coefficient functions L_n(α) for n=1,2,∞ evaluated on a grid of α. The checker verifies L1, L2, L_inf against the paper‑derived analytical expressions within prescribed tolerances."
    },
    {
      "file": "critical_point.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {
          "value": "float"
        }
      },
      "description": "Critical interaction parameter A_c obtained by solving the self‑consistent equations with L_∞(α). The checker compares the submitted value to the paper‑reported value with absolute tolerance."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks each of the two output artifacts against reference values derived from the underlying theory. For `L_functions.csv`, the verifier validates that L_∞(α) satisfies the analytic expression tanh(√α)/√α (and the negative-α branch) within a numerical tolerance, and that L_1(α) and L_2(α) match the values obtained from the iterative scheme (or the corresponding closed forms) to a specified precision. For `critical_point.txt`, the submitted A_c is compared to the expected critical value with an absolute tolerance. The two stages carry weights that are combined into a final reward in [0,1]. Simply reporting a number that happens to match the reference is not sufficient; the verifier may recompute or cross-check internal consistency of the submitted data.
