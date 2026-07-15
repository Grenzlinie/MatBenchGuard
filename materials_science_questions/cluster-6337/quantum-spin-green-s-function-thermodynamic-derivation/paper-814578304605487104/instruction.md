# Compute High-Temperature Series Coefficients for Diagonal Spin Correlation in 2D Ising Model

## Problem background
The two-dimensional Ising model is an exactly soluble many-body system whose diagonal spin-spin correlation functions are of fundamental interest. Computing their high-temperature series expansions via graphical methods becomes very difficult for larger spin separations. A recent approach uses a nonlinear ordinary differential equation satisfied by these correlation functions to derive the series coefficients algebraically, turning the problem into a purely computational recursion.

## Approach
The method substitutes a power-series ansatz for the high-temperature correlation into the known nonlinear ODE. By transforming from the ODE's natural variable to the standard high-temperature expansion variable, one obtains a polynomial equation after series expansion. Equating coefficients of each power to zero yields a sequence of algebraic equations that are solved recursively for the unknown integer coefficients. The recursion starts from the lowest-order coefficient given by the combinatorial formula c_{n,n} = (2n)!/(n!)^2; for the required spin separation n=2 this coefficient is computed first. No external datasets are needed — the entire computation is self-contained symbolic algebra.

## Reproduction target
Compute the high-temperature series coefficients c_{2,k} for the diagonal correlation S_{2,+} in the isotropic 2D Ising model above the critical temperature, for orders k=2 through 9. Output the integer coefficients as a JSON object with string keys "2", "3", ..., "9" mapping to their respective integer values. The JSON must be written to `/app/outputs/c_n_k.json`.

## Assets

- SymPy: sympy

## Workflow steps

### Step 1: Compute high-temperature series coefficients c_{2,k}
- Role: scored (load-bearing)
- Action: Implement the ODE-based recursive algebraic procedure to compute the high-temperature series coefficients c_{2,k} for the diagonal correlation S_{2,+} in the isotropic 2D Ising model above the critical temperature, for orders k=2 through 9. Use the series ansatz S_{2,+} = Σ_{k=2}^{9} c_{2,k} x^k, the relation t = (1-x)^4/(16x^2), the definition of σ_{2,+} in terms of S_{2,+} and its t-derivative, the nonlinear ODE for σ_2, and the known lowest-order coefficient c_{2,2} from the combinatorial formula. Substitute, expand in x, equate powers to obtain algebraic equations, solve sequentially, and output the integer coefficients as a JSON file.
- Output file: `/app/outputs/c_n_k.json`
- Format: json
- Contract: A JSON object with string keys "2", "3", ..., "9" mapping to integer coefficient values. Example: {"2": <integer>, "3": <integer>, ...}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/c_n_k.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### c_n_k.json
- path: `/app/outputs/c_n_k.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The high-temperature series coefficients c_{2,k} (k=2..9) for the diagonal spin correlation S_{2,+} in the 2D Ising model, computed via the ODE-based recursive method.
- schema:
  - `type`: object
  - `keys`:
    - `2`: integer
    - `3`: integer
    - `4`: integer
    - `5`: integer
    - `6`: integer
    - `7`: integer
    - `8`: integer
    - `9`: integer

Notes: Only n=2 is required. The coefficients are exact integers derived from the ODE power-series expansion starting from the known lowest-order coefficient c_{2,2}=6 obtained from the formula c_{n,n}=(2n)!/(n!)^2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "c_n_k.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "keys": {
          "2": "integer",
          "3": "integer",
          "4": "integer",
          "5": "integer",
          "6": "integer",
          "7": "integer",
          "8": "integer",
          "9": "integer"
        }
      },
      "description": "The high-temperature series coefficients c_{2,k} (k=2..9) for the diagonal spin correlation S_{2,+} in the 2D Ising model, computed via the ODE-based recursive method."
    }
  ],
  "notes": "Only n=2 is required. The coefficients are exact integers derived from the ODE power-series expansion starting from the known lowest-order coefficient c_{2,2}=6 obtained from the formula c_{n,n}=(2n)!/(n!)^2."
}
```

## How you are scored
A hidden verifier independently checks each coefficient in your submitted JSON against exact, correct reference values derived from the deterministic method. Because the recursion yields exact integers, an exact integer match is required for each coefficient. The verifier awards full credit when all coefficients are correct, and partial credit proportional to the number of correct coefficients otherwise. Importantly, reporting externally looked-up numbers is not accepted — you must implement and run the algebraic procedure to compute the coefficients.
