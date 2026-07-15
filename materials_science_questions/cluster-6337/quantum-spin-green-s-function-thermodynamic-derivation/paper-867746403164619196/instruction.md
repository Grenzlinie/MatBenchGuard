# Quantum Heisenberg Trimer Time-Averaged Autocorrelation Convergence to Classical Limit

## Problem background
For a system of three identical quantum spins that interact via isotropic Heisenberg exchange (a quantum Heisenberg trimer), thermodynamic functions and time-dependent spin correlation functions are expected to approach their classical counterparts as the spin quantum number s grows large. Unlike the classical trimer, whose spin autocorrelation function decays to a unique non-zero long-time limit, the quantum autocorrelation function is strictly periodic in time. A meaningful comparison between quantum and classical long-time behaviour can be made by examining the time average of the quantum autocorrelation function over one recurrence period, evaluated in the limit of infinite temperature. This task addresses the computation of that time-averaged spin autocorrelation function for quantum trimers with a range of spin values (s from 1/2 to 7, half‑integer up to 13/2), the estimation of the infinite‑s limit through Levin u‑sequence acceleration, and a comparison with the exact classical long‑time limit for the corresponding classical trimer.

## Approach
The core of the calculation rests on the exact spectral decomposition of the Heisenberg trimer Hamiltonian. For a given spin s, the Hamiltonian can be diagonalised by coupling the three spins to a total spin S; the energy eigenvalues depend only on S and the degeneracies arise from the possible intermediate couplings and from the magnetic quantum numbers. At infinite temperature the time‑averaged autocorrelation function reduces to a rational expression in terms of these eigenvalues and their multiplicities. The workflow therefore begins by determining the eigenenergies and degeneracies for each s (using exact rational arithmetic), then evaluates the time‑averaged autocorrelation function as an exact rational number. The results are split into a half‑integer sequence and an integer sequence. To estimate the s→∞ limit, the Levin u‑sequence acceleration method is applied to each sequence (using all available terms of that subsequence). As a benchmark, the classical long‑time limit for the analogous classical trimer (three unit vectors interacting with coupling Jc = J s(s+1)) must be evaluated from the known classical statistical‑mechanical expression, yielding a definite numerical constant.

## Reproduction target
Produce the following two artifacts under `/app/outputs`:

- `step_01_acf_time_averages.json` — the time‑averaged autocorrelation function values at infinite temperature for each s, organised into `half_integer` and `integer` arrays.
- `step_02_levin_estimates.json` — the Levin u‑estimates for the half‑integer and integer sequences, together with the computed classical long‑time limit.

The required keys and data shapes are detailed in the workflow steps and in the output contract below. The numerical values must be obtained from the genuine computation described above; simply copying plausible numbers will not satisfy the verifier.

## Assets

- Python environment with NumPy and SymPy: numpy,sympy

## Workflow steps

### Step 1: Compute Heisenberg trimer eigensystem
- Role: process
- Action: For each spin quantum number s in {1/2, 1, 3/2, 2, 5/2, 3, 7/2, 4, 9/2, 5, 11/2, 6, 13/2, 7}, construct the Heisenberg trimer Hamiltonian and obtain all energy eigenvalues and their degeneracies in the total-spin basis.
- Evidence: none

### Step 2: Time-averaged autocorrelation function
- Role: scored (load-bearing)
- Action: Using the eigensystem from step 1, evaluate the time-averaged autocorrelation function at infinite temperature for each spin s according to the paper's method. Obtain exact rational values and store them as IEEE 754 double-precision floats. Organize results separately for half-integer and integer s.
- Output file: `/app/outputs/step_01_acf_time_averages.json`
- Format: json
- Contract: JSON object with keys "half_integer" (array of objects {"s": number, "average": number}) and "integer" (array of objects {"s": number, "average": number}).
- Scoring: scored by hidden verifier

### Step 3: Levin u-acceleration and classical limit
- Role: scored
- Action: Form sequences of ACF time-averages for half-integer and integer s separately. Apply Levin u-sequence acceleration with M = 7 to obtain estimates of the infinite-s limit. Compute the exact classical long-time limit (9/40)ln(3) + 7/30 as a float. Output the two Levin estimates and the classical result.
- Output file: `/app/outputs/step_02_levin_estimates.json`
- Format: json
- Contract: JSON object with keys "half_integer_estimate" (float), "integer_estimate" (float), "classical_result" (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_acf_time_averages.json`
- `/app/outputs/step_02_levin_estimates.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_acf_time_averages.json
- path: `/app/outputs/step_01_acf_time_averages.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Time-averaged spin autocorrelation function values for half-integer and integer spin quantum numbers at infinite temperature. Compared against the exact rational values from the paper (Table 1) converted to double-precision floats.
- schema:
  - `type`: object
  - `required`: `half_integer`, `integer`
  - `properties`:
    - `half_integer`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `s`, `average`
        - `properties`:
          - `s`:
            - `type`: number
            - `description`: spin quantum number
          - `average`:
            - `type`: number
            - `description`: time-averaged autocorrelation function value
    - `integer`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `s`, `average`
        - `properties`:
          - `s`:
            - `type`: number
          - `average`:
            - `type`: number

### step_02_levin_estimates.json
- path: `/app/outputs/step_02_levin_estimates.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Levin u-acceleration estimates for the infinite-spin limit and the exact classical result, compared to the paper's reported U[7] values and the exact classical constant.
- schema:
  - `type`: object
  - `required`: `half_integer_estimate`, `integer_estimate`, `classical_result`
  - `properties`:
    - `half_integer_estimate`:
      - `type`: number
      - `description`: Levin u-estimate for the half-integer sequence
    - `integer_estimate`:
      - `type`: number
      - `description`: Levin u-estimate for the integer sequence
    - `classical_result`:
      - `type`: number
      - `description`: Exact classical long-time limit (9/40)ln(3) + 7/30

Notes: The partition function and zero-field susceptibility convergence stages are not scored because the paper does not provide exact numeric gold for those. Only the time-averaged autocorrelation function and the Levin acceleration results are required. The agent must compute the eigensystem as a process step; no pre-computed spectra are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_acf_time_averages.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "half_integer",
          "integer"
        ],
        "properties": {
          "half_integer": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "s",
                "average"
              ],
              "properties": {
                "s": {
                  "type": "number",
                  "description": "spin quantum number"
                },
                "average": {
                  "type": "number",
                  "description": "time-averaged autocorrelation function value"
                }
              }
            }
          },
          "integer": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "s",
                "average"
              ],
              "properties": {
                "s": {
                  "type": "number"
                },
                "average": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Time-averaged spin autocorrelation function values for half-integer and integer spin quantum numbers at infinite temperature. Compared against the exact rational values from the paper (Table 1) converted to double-precision floats."
    },
    {
      "file": "step_02_levin_estimates.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "half_integer_estimate",
          "integer_estimate",
          "classical_result"
        ],
        "properties": {
          "half_integer_estimate": {
            "type": "number",
            "description": "Levin u-estimate for the half-integer sequence"
          },
          "integer_estimate": {
            "type": "number",
            "description": "Levin u-estimate for the integer sequence"
          },
          "classical_result": {
            "type": "number",
            "description": "Exact classical long-time limit (9/40)ln(3) + 7/30"
          }
        }
      },
      "description": "Levin u-acceleration estimates for the infinite-spin limit and the exact classical result, compared to the paper's reported U[7] values and the exact classical constant."
    }
  ],
  "notes": "The partition function and zero-field susceptibility convergence stages are not scored because the paper does not provide exact numeric gold for those. Only the time-averaged autocorrelation function and the Levin acceleration results are required. The agent must compute the eigensystem as a process step; no pre-computed spectra are provided."
}
```

## How you are scored
A hidden verifier independently reads the submitted JSON files and compares every required entry against the expected reference values (derived from the theoretical results of the original study) using appropriate numerical tolerances. Each scored output contributes a fraction of the total reward. The intermediate eigensystem computation is required because the later scored steps depend on its output; the verifier checks the final numbers, and an attempt to bypass the computation by guessing the answers will not match the hidden references. The reward is a single number in [0,1] that reflects how well the computed quantities reproduce the expected results.
