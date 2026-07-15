# Elastic Energy Screening by Multi-Disclination Configuration

## Problem background
In an infinite isotropic elastic cylinder, a central wedge disclination of power Ω stores elastic energy. When N peripheral wedge disclinations of opposite sign and total power Nω = Ω are placed on a circle of radius r < R, the total system energy changes. The relative change ΔW/W_in depends on the dimensionless radial parameter ξ = r/R and the number N of peripheral disclinations. This task computes ΔW/W_in for several N numerically and examines the resulting values.

## Approach
The elastic energy of the multi-disclination configuration is derived analytically. For the fully compensated case (Nω = Ω), the relative energy change is given by an explicit formula involving a sum over m=1 to N−1 of terms Υ ln(1+1/Υ) with Υ = 4 ξ² sin²(π m/N) / (1−ξ²)². You will implement this formula in code, evaluate it for N = 2, 3, 4, 5 and for 100 equally spaced ξ values in (0,1) (excluding the singular endpoints), and output the computed ΔW/W_in values.

## Reproduction target
Produce a single tab-separated file, deltaW_values.tsv, containing the relative elastic energy change for each combination of N (2, 3, 4, 5) and ξ (100 equally spaced values in the open interval (0,1), e.g. linspace(0.01, 0.99, 100)). The file must have a header row with columns xi, N, deltaW.

## Assets

- Python scientific computing environment (numpy, scipy): numpy, scipy

## Workflow steps

### Step 1: Compute relative elastic energy change and output data
- Role: scored (load-bearing)
- Action: Implement the formula for the relative elastic energy change ΔW/W_in of the fully compensated multi-disclination configuration: ΔW/W_in = ξ⁴ − 4ξ² ln ξ − 1 − (1−ξ²)² × (1/N) Σ_{m=1}^{N−1} [ Υ(ξ,m,N) ln(1 + 1/Υ(ξ,m,N)) ], where Υ(ξ,m,N) = 4 ξ² sin²(π m/N) / (1−ξ²)². Compute this quantity for N = 2, 3, 4, 5 and for 100 equally spaced ξ values in the open interval (0,1) (avoid ξ=0,1 to prevent singularities). Output a tab-separated file with the computed results.
- Output file: `/app/outputs/deltaW_values.tsv`
- Format: tsv
- Contract: TSV file with header: xi\tN\tdeltaW. xi is a float in (0,1); N is an integer 2,3,4,5; deltaW is a float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/deltaW_values.tsv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### deltaW_values.tsv
- path: `/app/outputs/deltaW_values.tsv`
- format: tsv
- purpose: scored
- target_policy: metric_recompute
- description: Tab-separated file containing computed relative elastic energy change for N=2,3,4,5 and xi sampled in (0,1).
- schema:
  - `type`: table
  - `required_columns`: `xi`, `N`, `deltaW`
  - `units`:
    - `xi`: dimensionless ratio r/R in (0,1)
    - `N`: integer number of peripheral disclinations
    - `deltaW`: dimensionless relative elastic energy change

Notes: This artifact is the sole scored output of the reproduction. The checker will independently recompute ΔW/W_in at a hidden set of (xi,N) points using the same formula and perform a structural check on all reported deltaW values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "deltaW_values.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "xi",
          "N",
          "deltaW"
        ],
        "units": {
          "xi": "dimensionless ratio r/R in (0,1)",
          "N": "integer number of peripheral disclinations",
          "deltaW": "dimensionless relative elastic energy change"
        }
      },
      "description": "Tab-separated file containing computed relative elastic energy change for N=2,3,4,5 and xi sampled in (0,1)."
    }
  ],
  "notes": "This artifact is the sole scored output of the reproduction. The checker will independently recompute ΔW/W_in at a hidden set of (xi,N) points using the same formula and perform a structural check on all reported deltaW values."
}
```

## How you are scored
The hidden verifier will re-implement the same expression and recompute ΔW/W_in at a set of (ξ,N) pairs not disclosed to you. It will compare your reported values at those points with a relative tolerance; accuracy on these hidden points determines 80% of the total reward. The verifier will also perform a structural check on your output (e.g., verifying that all computed values adhere to an expected mathematical property).
