# Dielectric constant computation from a one-dimensional Ising model

## Problem background
CaCu3Ti4O12 (CCTO) is a perovskite-related ceramic that exhibits an unusually large dielectric constant at room temperature. Understanding its dielectric response is of scientific and technological interest. This task reproduces a theoretical model — a one-dimensional Ising model under a static electric field — used to study the temperature dependence of the dielectric constant of CCTO. The objective is to compute and output the relative dielectric constant ε as a function of temperature T from this model.

## Approach
The model represents a periodic one-dimensional chain of N dipoles, each with moment μ, interacting via nearest-neighbor coupling J and placed in a uniform electric field E. The partition function is evaluated using the transfer-matrix method. Diagonalizing the transfer matrix yields two eigenvalues, and in the large‑N limit the total polarization P simplifies to a closed-form expression. From the relation P = ε₀ ε E, the relative dielectric constant ε is obtained as a function of temperature T. The required physical constants are the Boltzmann constant k_B and the vacuum permittivity ε₀. The model parameters are specified in the reproduction target below.

### Closed-form expression for the dielectric constant
In the large‑N limit, the relative dielectric constant is given by the explicit formula (equation (17) in the reference paper):

```
ε(T) = (μ N) / (ε₀ E) * sinh(x) / √( exp(-4y) + sinh²(x) )
```

where the dimensionless variables are defined as:

```
x = μ E / (k_B T)
y = J / (k_B T)
```

and:
- μ: electric dipole moment
- N: number of dipoles
- E: magnitude of the applied static electric field
- ε₀: vacuum permittivity
- k_B: Boltzmann constant
- J: nearest‑neighbor coupling energy (J > 0 favours parallel alignment; here J is negative, as given in the parameter list)
- sinh: hyperbolic sine
- exp: exponential function

Use this formula **exactly** to compute ε(T) for the temperature range specified below. No other expression or approximation should be used.

## Reproduction target
Compute the relative dielectric constant ε for temperatures T = 100, 110, …, 300 K (every 10 K) using the 1D Ising model with the large‑N approximation. Use the following parameters: N = 3×10²¹, E = 100 V/m, μ = 0.6309×10⁻²³ J·m·V⁻¹, J = −0.9315×10⁻²⁰ J, k_B = 1.380649×10⁻²³ J/K, ε₀ = 8.854187817×10⁻¹² F/m. Output the results as a CSV file with columns `T (K)` and `epsilon` (unitless).

## Assets

- Python environment with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Compute epsilon versus temperature
- Role: scored (load-bearing)
- Action: Compute the relative dielectric constant ε for a range of temperatures using the closed-form expression given above. Use the parameters listed in the reproduction target. Evaluate ε at every 10 K from 100 K to 300 K (inclusive) and write the results to a CSV file with columns 'T (K)' and 'epsilon'.
- Output file: `/app/outputs/epsilon_vs_T.csv`
- Format: csv
- Contract: CSV file with header: T (K), epsilon. 'T (K)' is the temperature in Kelvin (numeric), 'epsilon' is the dimensionless relative dielectric constant (numeric). The file must contain rows for T = 100, 110, …, 300 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/epsilon_vs_T.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### epsilon_vs_T.csv
- path: `/app/outputs/epsilon_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The temperature-dependent relative dielectric constant computed from the one‑dimensional Ising model with the given parameters. The hidden checker recomputes ε for each temperature using the same closed‑form expression and compares the submitted values within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T (K)`, `epsilon`
  - `units`:
    - `T (K)`: K
    - `epsilon`: dimensionless

Notes: The agent must use the numeric parameters and physical constants listed in the step. The checker recomputes the reference ε values with the same formula; any implementation that correctly evaluates the expression within 1% relative tolerance will pass.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "epsilon_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T (K)",
          "epsilon"
        ],
        "units": {
          "T (K)": "K",
          "epsilon": "dimensionless"
        }
      },
      "description": "The temperature-dependent relative dielectric constant computed from the one‑dimensional Ising model with the given parameters. The hidden checker recomputes ε for each temperature using the same closed‑form expression and compares the submitted values within a relative tolerance."
    }
  ],
  "notes": "The agent must use the numeric parameters and physical constants listed in the step. The checker recomputes the reference ε values with the same formula; any implementation that correctly evaluates the expression within 1% relative tolerance will pass."
}
```

## How you are scored
A hidden verifier independently recomputes ε for each temperature using the same closed‑form expression and parameters. It reads your submitted `epsilon_vs_T.csv` and compares your computed ε values against its own recomputed reference. The reward is based on the numerical agreement across all temperature points; the better the agreement, the higher the score. Simply reporting the expected result is not sufficient — the verifier checks the actual computed values.