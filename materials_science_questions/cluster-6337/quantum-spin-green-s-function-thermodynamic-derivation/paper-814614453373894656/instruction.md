# Quantum Critical Coupling for Spin-Anisotropic Quantum Spherical Model

## Problem background
The spin‑anisotropic quantum spherical model (SAQSM) is a quantum rotor model on a d‑dimensional hypercubic lattice that generalises the standard quantum spherical model by introducing a spin‑anisotropy parameter λ. This parameter controls an interaction between the momenta, analogous to the spin‑anisotropy in quantum Ising/XY chains. At zero temperature the model may undergo a quantum phase transition at a critical coupling g_c(λ,d). Computing g_c as a function of λ for several spatial dimensions reveals the phase diagram and can expose non‑trivial behaviour, such as a re‑entrant transition where the critical coupling is non‑monotonic in λ. The task is to numerically compute g_c(λ,d) from the ground‑state spherical constraint of the model and to examine its dependence on λ and d.

## Approach
The model is exactly solvable via a canonical transformation that diagonalises the Hamiltonian. The ground‑state thermodynamics is governed by a spherical constraint that relates the coupling g to the spherical parameter s. The quantum critical point occurs when the energy gap closes, which fixes s = s_c = (1+λ)d/2. By inserting this value into the constraint one obtains an expression for the critical coupling g_c(λ,d).

After a suitable change of variables, the constraint can be written as the following double integral:

\[ \sqrt{\frac{8\pi^2}{g_c}} = s_c^{-3/2} \int_0^\infty \!du \int_0^1 \!\frac{dx}{\sqrt{x(1-x)}}\; e^{-u s_c}\, [I_0(\rho)]^d \Bigl\{ s_c^2 - \frac{1-\lambda^2}{4} d(d-1)\Bigl(\frac{I_1(\rho)}{I_0(\rho)}\Bigr)^2 - \frac{d(1-\lambda^2)}{8}\Bigl(1 + \frac{I_2(\rho)}{I_0(\rho)}\Bigr) \Bigr\} \]

with  s_c = d(1+\lambda)/2  and  ρ = u\bigl( x(1+\lambda)/2 + (1-x)(1-\lambda)/2 \bigr).  The units are chosen such that J/\hbar^2 = 1, so g_c is the dimensionless critical coupling.

The task is to implement this integrand, perform the two‑dimensional numerical integration (e.g., using scipy.integrate.quad) for each required (λ,d) pair, and solve for g_c. No external data are needed; the computation is self‑contained.

## Reproduction target
Compute the quantum critical coupling g_c(λ,d) for the following parameter combinations:
- d = 2,  with λ = 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 (step 0.1)
- d = 1.5,  with λ = 0.0 and λ = 0.1
- d = 2.1,  with λ = 0.0 and λ = 0.1

Write the results as a CSV file where each row contains the columns:
lambda, d, g_c

The g_c values should be dimensionless (J/\hbar^2 = 1).  The verifier will check that the computed numbers are physically sound and that they exhibit the expected qualitative trends (e.g., the relative ordering of g_c among the different λ and d values) as predicted by the model.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute quantum critical coupling g_c(λ,d)
- Role: scored (load-bearing)
- Action: Implement the integral representation of the zero-temperature spherical constraint evaluated at the gap-closing point s = (1+λ)d/2. Using numerical integration (e.g., scipy.integrate.quad) compute the critical coupling g_c(λ,d) for d=2 at λ=0.0,0.1,...,1.0, and for d=1.5 and d=2.1 at λ=0.0 and 0.1. Write the results to g_c_values.csv.
- Output file: `/app/outputs/g_c_values.csv`
- Format: csv
- Contract: Columns: lambda (float), d (float), g_c (float). The value of g_c is in units of J/ħ² (reported as the dimensionless number when J/ħ²=1). Rows correspond to the specified parameter combinations.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/g_c_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### g_c_values.csv
- path: `/app/outputs/g_c_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed values of the quantum critical coupling g_c(λ,d) for the specified (λ,d) pairs. The hidden checker compares against paper-reported reference values with tolerance and additionally verifies the non-monotonic trend (minimum for d=2, negative slope at λ=0 for d=1.5, positive slope at λ=0 for d=2.1).
- schema:
  - `type`: table
  - `required_columns`: `lambda`, `d`, `g_c`
  - `units`:
    - `lambda`: dimensionless
    - `d`: dimensionless
    - `g_c`: J/hbar^2

Notes: The checker enforces that the computed values exhibit the expected re-entrant behaviour: for d=2, g_c(0.1) < g_c(0) and g_c(0.9) < g_c(1), with a minimum; for d=1.5, g_c(0.1) < g_c(0); for d=2.1, g_c(0.1) > g_c(0) (unless within a tiny tolerance around the critical dimension).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "g_c_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda",
          "d",
          "g_c"
        ],
        "units": {
          "lambda": "dimensionless",
          "d": "dimensionless",
          "g_c": "J/hbar^2"
        }
      },
      "description": "Computed values of the quantum critical coupling g_c(λ,d) for the specified (λ,d) pairs. The hidden checker compares against paper-reported reference values with tolerance and additionally verifies the non-monotonic trend (minimum for d=2, negative slope at λ=0 for d=1.5, positive slope at λ=0 for d=2.1)."
    }
  ],
  "notes": "The checker enforces that the computed values exhibit the expected re-entrant behaviour: for d=2, g_c(0.1) < g_c(0) and g_c(0.9) < g_c(1), with a minimum; for d=1.5, g_c(0.1) < g_c(0); for d=2.1, g_c(0.1) > g_c(0) (unless within a tiny tolerance around the critical dimension)."
}
```

## How you are scored
A hidden verifier inspects the output file `g_c_values.csv`.  It confirms that the file contains the required columns and the specified (λ,d) rows.  The verifier then scores your submission by comparing each computed g_c value to a reference set (obtained from the exact model solution) with a tolerance that accounts for numerical integration uncertainties.  In addition, the verifier checks that the sequence of g_c values satisfies the expected structural features of the model, such as the correct relative ordering for different λ and d (e.g., whether g_c(0.1) is lower or higher than g_c(0) for a given dimension, and whether the d=2 curve exhibits a minimum).  The final reward is a weighted combination of these checks; reporting a value that is physically consistent with the model’s theory is more important than matching any single reference digit.
