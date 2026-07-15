# Compute dispersion relation and critical temperature of antiferromagnetic spin chain using Green's function method

## Problem background
The system under study is a one-dimensional antiferromagnetic spin-1/2 chain with long-range interactions whose magnitude decays algebraically as 1/|m−n|^p, where p is a tunable exponent controlling the interaction range. The competing exchange interactions make the existence of magnetic long-range order at finite temperature a subtle question that depends on p. Using the double-time Green's function method, one can derive closed-form expressions for the excitation dispersion and the inverse critical temperature of the system. The task is to compute these quantities numerically for given values of p, thereby characterizing the conditions under which the chain supports antiferromagnetic order.

## Approach
The chain is bipartite; the spin operators are arranged on odd and even sublattices. The retarded Green's functions for the two sublattices satisfy coupled equations of motion that are closed by the Tyablikov decoupling approximation. Fourier transformation to wavevector space yields a compact dispersion relation ω_k = σ_a √((α − f_k)² − g_k²), where:

- f_k = 4 Σ_{n=1}^{∞} 1/(2n)^p (cos(2nk) − 1)
- g_k = 2 Σ_{n=1}^{∞} 1/(2n-1)^p cos((2n-1)k)
- α = 2 Σ_{n=1}^{∞} 1/(2n-1)^p

with σ_a the zero‑temperature sublattice magnetization. From the spectral theorem, the sublattice magnetization at finite temperature is expressed as a sum involving the dispersion, and letting σ_a → 0 gives the inverse critical temperature:

T_N^{-1} = (2/π) ∫_{-π}^{π} (α − f_k) / ((α − f_k)² − g_k²) dk   (k_B = 1).

The infinite series are truncated at a large finite cutoff n_max, and the dispersion and the integral are evaluated numerically. The zero‑temperature sublattice magnetization is fixed to σ_a = 0.5. Two values of p (1.5 and 2.5) are considered to probe different interaction ranges.

## Reproduction target
Produce two output files:

1. `/app/outputs/dispersion_k.csv` — a CSV with 100 rows and two columns: `k` (float, evenly spaced from 0 to π) and `omega_k` (float). Use p=1.5, σ_a=0.5, and truncate the series at n_max=10000.

2. `/app/outputs/critical_temperature.json` — a JSON object with the following keys:
   - `p1.5_TN_inverse`: float, the inverse critical temperature computed for p=1.5 with the same truncation and k_B=1.
   - `p2.5_TN_inverse`: float, the inverse critical temperature computed for p=2.5. If the integral does not converge numerically, set it to a large sentinel value (e.g., 1e10).
   - `p2.5_diverges`: bool, true if the integral for p=2.5 is found to diverge (the large sentinel is used) and false otherwise.

The series sums and the integral must be implemented using the formulas given in the Approach section; the order of operations, quadrature method, and convergence handling are left to you.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Generate antiferromagnetic excitation dispersion curve
- Role: scored
- Action: Implement the closed formulas for f_k, g_k, and α using series summations truncated to n_max=10000. Compute the dispersion ω_k = σ_a √((α - f_k)² - g_k²) for k evenly spaced in [0,π] (100 points), with p=1.5, σ_a=0.5. Write the resulting (k, ω_k) pairs to /app/outputs/dispersion_k.csv.
- Output file: `/app/outputs/dispersion_k.csv`
- Format: csv
- Contract: columns: [k (float), omega_k (float)]
- Scoring: scored by hidden verifier

### Step 2: Compute inverse critical temperature
- Role: scored
- Action: Using the same formulas and truncation n_max=10000, compute the integral T_N^{-1} = (2/π) ∫_{-π}^{π} (α - f_k) / ((α - f_k)² - g_k²) dk for p=1.5 and p=2.5. For p=2.5, if the integral does not converge numerically, set a large sentinel value (e.g., 1e10) and report divergence. Write the results to /app/outputs/critical_temperature.json.
- Output file: `/app/outputs/critical_temperature.json`
- Format: json
- Contract: object: { "p1.5_TN_inverse": float, "p2.5_TN_inverse": float, "p2.5_diverges": bool }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dispersion_k.csv`
- `/app/outputs/critical_temperature.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dispersion_k.csv
- path: `/app/outputs/dispersion_k.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed antiferromagnetic excitation dispersion curve for p=1.5. The checker recomputes the dispersion from the same formulas and compares omega_k values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `k`, `omega_k`

### critical_temperature.json
- path: `/app/outputs/critical_temperature.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Inverse critical temperature values computed for p=1.5 and p=2.5, and a divergence flag. The checker recomputes the integral and checks p1.5_TN_inverse within tolerance, and for p=2.5 verifies the large sentinel and true divergence flag.
- schema:
  - `type`: object
  - `required`: `p1.5_TN_inverse`, `p2.5_TN_inverse`, `p2.5_diverges`
  - `items`:
    - `p1.5_TN_inverse`: float
    - `p2.5_TN_inverse`: float
    - `p2.5_diverges`: bool

Notes: Paper is compute-driven. The scored outputs are the direct numerical evaluation of closed-form expressions derived in the paper. The checker reimplements the same formulas and compares against the agent's outputs within tolerances, confirming the absence of long-range order when p≥2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dispersion_k.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "k",
          "omega_k"
        ]
      },
      "description": "Computed antiferromagnetic excitation dispersion curve for p=1.5. The checker recomputes the dispersion from the same formulas and compares omega_k values within tolerance."
    },
    {
      "file": "critical_temperature.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "p1.5_TN_inverse",
          "p2.5_TN_inverse",
          "p2.5_diverges"
        ],
        "items": {
          "p1.5_TN_inverse": "float",
          "p2.5_TN_inverse": "float",
          "p2.5_diverges": "bool"
        }
      },
      "description": "Inverse critical temperature values computed for p=1.5 and p=2.5, and a divergence flag. The checker recomputes the integral and checks p1.5_TN_inverse within tolerance, and for p=2.5 verifies the large sentinel and true divergence flag."
    }
  ],
  "notes": "Paper is compute-driven. The scored outputs are the direct numerical evaluation of closed-form expressions derived in the paper. The checker reimplements the same formulas and compares against the agent's outputs within tolerances, confirming the absence of long-range order when p≥2."
}
```

## How you are scored
Your submission is automatically checked by a hidden verifier that recomputes the same formulas and compares your results to reference values. The dispersion values are evaluated for accuracy across all k-points, and the inverse critical temperature for p=1.5 is compared to the expected finite value. For p=2.5, the verifier confirms that the integral diverges by checking that the sentinel is large and the divergence flag is true. Each output contributes a weight to the final reward, which is a number between 0 and 1. Simply stating expected numbers without performing the required computations will not pass.
