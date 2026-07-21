# Mean-Field Critical Temperature for Cylindrical Ising Nanowires and Nanotubes

## Problem background
Cylindrical Ising nanowires and nanotubes exhibit a core-shell magnetic structure. Core spins carry magnitude S_c and are coupled by exchange J, while surface spins carry magnitude S_s and are coupled by a surface exchange J_s = J(1 + Δ_s). Core and surface spins interact via a coupling J_1. Near the critical temperature, the mean-field (Brillouin) function linearizes, leading to a homogeneous linear system A m = 0. The matrix A is 4×4 for a nanowire (four distinct spin types) and 3×3 for a nanotube (three distinct spin types). The critical temperature T_c (in units of J/k) is the temperature that satisfies det A = 0. Understanding how T_c varies with surface enhancement Δ_s, core-surface coupling J_1/J, and spin magnitudes is key to assessing surface effects on magnetic ordering in these nanostructures.

## Approach
Implement the mean-field formalism. For a chosen geometry (nanowire or nanotube) and given values of S_c, S_s, J_1/J, and Δ_s, construct the linearized matrix A from the molecular-field equations. Then numerically solve the determinantal equation det A(T) = 0 to obtain the critical temperature T_c (expressed in units of J/k). This is repeated for all required parameter combinations, yielding a CSV of T_c values.

## Reproduction target
Compute T_c for the following parameter sets, for both the nanowire and nanotube geometries:
- (S_c = 0.5, S_s = 1, J_1/J = 1.0, Δ_s = 0.0, 0.5, 1.0)
- (S_c = 0.5, S_s = 0.5, J_1/J = 1.0, Δ_s = 0.0, 0.5, 1.0)
- (S_c = 0.5, S_s = 1, J_1/J = 1.5, Δ_s = 0.0, 0.5, 1.0)
Report the results as a CSV file with columns: geometry ("nanowire" or "nanotube"), Sc, Ss, J1_div_J, delta_s, Tc (in units of J/k). One row per combination.

## Assets

- Python 3: https://www.python.org
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement mean-field matrix construction
- Role: process
- Action: Translate the molecular-field equations into code. For each geometry (nanowire or nanotube), define a function that builds the linearized matrix A(T) given S_c, S_s, J, J1_div_J, and Δ_s. Fill the matrix elements according to the Brillouin function linearization derived from the Ising model on a cylindrical core-shell structure. Ensure the function returns the correct matrix dimension (4x4 for nanowire, 3x3 for nanotube).
- Evidence: `/app/outputs/matrix_implementation_log.txt`

### Step 2: Compute critical temperatures for all parameter sets
- Role: scored
- Action: For every combination in the following parameter grid: (S_c=0.5, S_s=1, J1_div_J=1.0, Δ_s in [0.0,0.5,1.0]), (S_c=0.5, S_s=0.5, J1_div_J=1.0, Δ_s in [0.0,0.5,1.0]), and (S_c=0.5, S_s=1, J1_div_J=1.5, Δ_s in [0.0,0.5,1.0]), for both geometries (nanowire, nanotube), construct the linearized matrix A(T), numerically solve det A(T)=0 for T, and report the critical temperature Tc (in units of J/k). Output one row per combination.
- Output file: `/app/outputs/tc_results.csv`
- Format: csv
- Contract: Columns: geometry (string: 'nanowire' or 'nanotube'), Sc (float), Ss (float), J1_div_J (float), delta_s (float), Tc (float in units of J/k).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_results.csv
- path: `/app/outputs/tc_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical temperature Tc computed from the mean-field matrix determinant condition for each (geometry, spin magnitudes, exchange ratio, surface enhancement) combination.
- schema:
  - `type`: table
  - `required_columns`: `geometry`, `Sc`, `Ss`, `J1_div_J`, `delta_s`, `Tc`
  - `units`:
    - `Tc`: J/k

Notes: The checker will independently recompute Tc for each row using the same matrix formalism and compare values with a small relative tolerance. The agent must implement the solver from scratch; the output should reflect accurate numeric root-finding.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "geometry",
          "Sc",
          "Ss",
          "J1_div_J",
          "delta_s",
          "Tc"
        ],
        "units": {
          "Tc": "J/k"
        }
      },
      "description": "Critical temperature Tc computed from the mean-field matrix determinant condition for each (geometry, spin magnitudes, exchange ratio, surface enhancement) combination."
    }
  ],
  "notes": "The checker will independently recompute Tc for each row using the same matrix formalism and compare values with a small relative tolerance. The agent must implement the solver from scratch; the output should reflect accurate numeric root-finding."
}
```

## How you are scored
A hidden verifier independently recomputes the critical temperature for each row in your CSV using the same mean-field matrix formalism and a high-precision numerical solver. Your reported Tc values are compared to the verifier's values within a relative tolerance. Additionally, the verifier checks a structural ordering: for identical spin magnitudes, J_1/J, and Δ_s, the Tc for a nanowire must be strictly greater than the Tc for a nanotube. Your final reward is 1.0 if all numeric values fall within tolerance and the ordering constraint holds. Partial credit is granted if either the numeric accuracy or the ordering requirement is satisfied alone.
