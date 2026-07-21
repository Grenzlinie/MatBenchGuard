# Compute Curie temperature and ferromagnetic instability for mixed‑spin Ising model via Bethe–Peierls equations

## Problem background
On a two-dimensional square lattice, alternate spins of magnitude S=1/2 and S=1 form a mixed Ising ferromagnet. The spins are coupled by several exchange interactions: a nearest-neighbour (n.n.) bilinear exchange J1 between distinct spins, two kinds of next-nearest-neighbour (n.n.n.) bilinear exchanges J2 (between S=1 spins) and J3 (between S=1/2 spins), and two biquadratic exchanges — J1' between n.n. spins (both S=1 and S=1/2) and J2' between n.n.n. S=1 spins. The Curie temperature Tc and the ratio of the effective molecular fields on the two spin species (μ1/λ1) are determined by solving the linearized Bethe-Peierls self-consistency equations. The central open task is to compute the dependence of the reduced Curie temperature k_B T_c / J_1 and of μ1/λ1 on the exchange parameters, and to locate any regime where ferromagnetic order becomes unstable (Tc → 0).

## Approach
The Bethe-Peierls cluster approximation is applied to two complementary clusters: one centered on an S=1 spin and its four S=1/2 neighbours, the other centered on an S=1/2 spin and its four S=1 neighbours. Expanding the partition functions and imposing self-consistency at the critical point yields a pair of coupled transcendental equations for the reduced temperature variables (K1 = J1/k_B T, etc.) and for the ratio μ1/λ1. These equations, given below in their final form, involve exponential terms with linear coefficients that depend on the bilinear and biquadratic exchange parameters K1, K2, K3, K1', K2'. The complete set of integer and rational coefficients is supplied in two coefficient tables (one table per equation). To obtain a solution point, one chooses numerical values for the exchange parameters (e.g., J1'/J1, J2'/J1, J2/J1, J3/J1), sets all parameters not being scanned to zero, and solves the two simultaneous equations for K1 and μ1/λ1 using a standard numerical root-finding method. The physical reduced Curie temperature is then k_B T_c / J_1 = 1 / K1. No external data or model files are required — only the coefficient tables and the equation forms provided here.

## Reproduction target
Compute k_B T_c / J_1 and μ1/λ1 by solving the pair of transcendental equations for a dense grid of values covering the following independent-parameter scans (all other exchange parameters set to zero):
- J1' from −2.0 J1 to +2.0 J1 (step ≤ 0.05 for fine resolution near the instability; elsewhere step ≤ 0.1)
- J2' from −2.0 to +2.0 in steps of ≤ 0.1
- J2  from −1.0 to +1.0 in steps of ≤ 0.05
- J3  from −2.0 to +2.0 in steps of ≤ 0.2

For each scan point produce a row with the parameter name, its value (in units of J1), kB_Tc_over_J1, and mu1_over_lambda1. Write the full scan as `parameter_scans.csv`.
From the J1' scan, identify the first parameter value (starting from zero and moving toward negative values) where kB_Tc_over_J1 drops to ≤ 1×10⁻⁶; report this critical value and the corresponding mu1_over_lambda1 in a single-row file `instability_point.csv`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Parameter scans for reduced Curie temperature and molecular‑field ratio
- Role: scored (load-bearing)
- Action: For discrete values of each exchange parameter J1′, J2′, J2, and J3 (with all other parameters set to zero) covering the ranges specified in the task, numerically solve the two linearized Bethe–Peierls self‑consistency equations to obtain the reduced Curie temperature k_B T_c / J_1 and the molecular‑field ratio μ_1/λ_1. Write the full scan results as a CSV.
- Output file: `/app/outputs/parameter_scans.csv`
- Format: csv
- Contract: Columns: parameter (string, one of 'J1′', 'J2′', 'J2', 'J3'), parameter_value (float, in units of J1), kB_Tc_over_J1 (float), mu1_over_lambda1 (float). Rows ordered by parameter name and ascending parameter_value.
- Scoring: scored by hidden verifier

### Step 2: Ferromagnetic instability point from J1′ scan
- Role: scored
- Action: Using the J1′ scan results, identify the critical value of J1′/J1 at which the reduced Curie temperature k_B T_c / J_1 first drops to negligible (≤ 1e‑6), indicating the loss of ferromagnetic order, and report this critical value together with the corresponding μ_1/λ_1 in a single‑row CSV.
- Output file: `/app/outputs/instability_point.csv`
- Format: csv
- Contract: Columns: parameter (string: 'J1′'), critical_value (float), kB_Tc_over_J1 (float, expected ≈ 0), mu1_over_lambda1 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/parameter_scans.csv`
- `/app/outputs/instability_point.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### parameter_scans.csv
- path: `/app/outputs/parameter_scans.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Parameter scan of the reduced Curie temperature and molecular‑field ratio, computed by solving the Bethe–Peierls linearized equations for one varying exchange parameter while keeping the other three zero.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `parameter_value`, `kB_Tc_over_J1`, `mu1_over_lambda1`
  - `units`:
    - `parameter_value`: units of J1
    - `kB_Tc_over_J1`: dimensionless
    - `mu1_over_lambda1`: dimensionless

### instability_point.csv
- path: `/app/outputs/instability_point.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical biquadratic exchange ratio J1′/J1 at which ferromagnetic order becomes unstable (Tc → 0).
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `critical_value`, `kB_Tc_over_J1`, `mu1_over_lambda1`
  - `units`:
    - `critical_value`: units of J1
    - `kB_Tc_over_J1`: dimensionless
    - `mu1_over_lambda1`: dimensionless

Notes: The agent must derive the equations from the provided Bethe‑Peierls linearized forms and the coefficient tables. The checker will verify the reported values against independently recomputed hidden references using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "parameter_scans.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "parameter_value",
          "kB_Tc_over_J1",
          "mu1_over_lambda1"
        ],
        "units": {
          "parameter_value": "units of J1",
          "kB_Tc_over_J1": "dimensionless",
          "mu1_over_lambda1": "dimensionless"
        }
      },
      "description": "Parameter scan of the reduced Curie temperature and molecular‑field ratio, computed by solving the Bethe–Peierls linearized equations for one varying exchange parameter while keeping the other three zero."
    },
    {
      "file": "instability_point.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "critical_value",
          "kB_Tc_over_J1",
          "mu1_over_lambda1"
        ],
        "units": {
          "critical_value": "units of J1",
          "kB_Tc_over_J1": "dimensionless",
          "mu1_over_lambda1": "dimensionless"
        }
      },
      "description": "Critical biquadratic exchange ratio J1′/J1 at which ferromagnetic order becomes unstable (Tc → 0)."
    }
  ],
  "notes": "The agent must derive the equations from the provided Bethe‑Peierls linearized forms and the coefficient tables. The checker will verify the reported values against independently recomputed hidden references using appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently recomputes the solutions of the same transcendental equations for a selected subset of parameter points and for the instability detection, using hardcoded reference implementations of the coefficient tables. The verifier compares your reported kB_Tc_over_J1 and mu1_over_lambda1 against these independently evaluated values, awarding full credit for agreement within tolerance ranges that absorb legitimate numerical differences between solvers. The two output artifacts are scored separately and the scores are combined into a final reward. Merely reproducing the paper’s published numbers is not sufficient; your numerical solver must correctly implement the equations and tables provided in this task description.
