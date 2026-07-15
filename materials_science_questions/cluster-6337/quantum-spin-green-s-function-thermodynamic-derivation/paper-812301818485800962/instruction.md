# Frustrated Heisenberg Antiferromagnet Correlation Functions and Susceptibility Computation

## Problem background
The two-dimensional S=1/2 Heisenberg antiferromagnet on a square lattice, with competing nearest-neighbour (J₁) and next-nearest-neighbour (J₂) exchange interactions, is a central model for the magnetism of cuprate high-temperature superconductors. The frustration parameter λ = J₂/J₁ is believed to drive a quantum phase transition from a long-range ordered Néel state to a spin liquid state. Computing how the sublattice magnetisation, the spin-excitation gap, the short-range spin correlation functions, and the uniform magnetic susceptibility depend on λ and on temperature is essential to understand the magnetic response of the CuO₂ plane and its possible connection to doping.

## Approach
The spin system is treated with a spherically symmetric Green-function decoupling scheme. Two retarded Green functions are introduced, and their equations of motion are decoupled by keeping local correlations while introducing two phenomenological parameters α₁ and α₂ for nearest-neighbour and more-distant pairs. A self-consistent set of equations for five short-range correlation functions C_g, C_d, C_{2g}, C_{g+d}, C_{2d} and for the spectrum gap δ is obtained; the uniform susceptibility χ follows from the Green function at wavevector q=0.
- **Calibration**: At T=0 and λ=0 the ratio r_α = (α₁−1)/(α₂−1) is adjusted so that the sublattice magnetisation m equals the accepted reference value 0.3.
- **T=0 solutions**: Two branches exist. For small λ the system is in the long-range ordered state (gapless, δ=0) and m is finite, obtained from the condensation part of the Green function. Beyond a critical λ the spectrum opens a gap (δ>0) and m vanishes, signalling a spin liquid state.
- **Finite temperature**: Always δ>0; the self-consistent equations are solved directly without the condensation part, and χ is computed.
The workflow is fully specified: solve the self-consistent equations for the correlation functions, compute the gap and magnetisation, evaluate χ, and write the results to CSV tables.

## Reproduction target
Implement the self-consistent Green-function treatment described above and produce two CSV tables.

1. **T=0 ground state** (file `step_01_t0_results.csv`): For each frustration parameter λ = 0.0, 0.1, 0.2, 0.3, 0.4, 0.5 compute and report the sublattice magnetisation m (0 for the spin liquid phase), the spectrum gap δ, and the five correlation functions C_g, C_d, C_{2g}, C_{g+d}, C_{2d}. The decoupling parameters α₁, α₂ are fixed by the calibration described in Step 1.

2. **Finite temperature** (file `step_02_ft_results.csv`): For each combination of λ ∈ {0.0, 0.1, 0.2, 0.3} and temperature T from 0.0 to 1.5 in steps of 0.1 compute and report the temperature-dependent gap δ, the correlation functions C_g, C_d, C_{2g}, and the uniform susceptibility χ.

All quantities are in units where J₁ = 1. The hidden verifier will numerically compare the reported values against independently derived references; the task is successful when the computed curves reproduce the essential physical behaviour of the model across the parameter ranges.

## Assets

- Python 3: python
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Decoupling parameter calibration
- Role: process
- Action: Solve the self-consistent equations at T=0, frustration λ=0 using the gapless long-range order branch and adjust the decoupling parameter ratio r_α = (α1-1)/(α2-1) until the sublattice magnetization m equals the reference value 0.3. Determine the corresponding α1, α2, and r_α.
- Evidence: `/app/outputs/calibration.json`

### Step 2: T=0 ground state results
- Role: scored (load-bearing)
- Action: For each frustration λ in [0, 0.1, 0.2, 0.3, 0.4, 0.5], solve the self-consistent equations at T=0. Determine whether the system is in the long-range ordered state (δ=0) or the spin liquid state (δ>0) and compute sublattice magnetization m (from condensation part for LROS, 0 otherwise), spectrum gap δ, and correlation functions C_g, C_d, C_{2g}, C_{g+d}, C_{2d}. Write the results to the CSV file.
- Output file: `/app/outputs/step_01_t0_results.csv`
- Format: csv
- Contract: CSV with columns: lambda (float), m (float), delta (float), Cg (float), Cd (float), C2g (float), Cg_plus_d (float), C2d (float)
- Scoring: scored by hidden verifier

### Step 3: Finite temperature results
- Role: scored
- Action: For each combination of frustration λ in {0.0, 0.1, 0.2, 0.3} and temperature T from 0.0 to 1.5 in steps of 0.1, solve the finite-temperature self-consistent equations (δ>0) to obtain correlation functions C_g, C_d, C_{2g} and spectrum gap δ. Then compute the uniform magnetic susceptibility χ using the Green's function at q=0. Write all results to the CSV file.
- Output file: `/app/outputs/step_02_ft_results.csv`
- Format: csv
- Contract: CSV with columns: lambda (float), T (float), delta (float), Cg (float), Cd (float), C2g (float), chi (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_t0_results.csv`
- `/app/outputs/step_02_ft_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_t0_results.csv
- path: `/app/outputs/step_01_t0_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Ground-state physical quantities computed from the self-consistent solution at T=0.
- schema:
  - `type`: table
  - `required_columns`: `lambda`, `m`, `delta`, `Cg`, `Cd`, `C2g`, `Cg_plus_d`, `C2d`
  - `column_types`:
    - `lambda`: float
    - `m`: float
    - `delta`: float
    - `Cg`: float
    - `Cd`: float
    - `C2g`: float
    - `Cg_plus_d`: float
    - `C2d`: float
  - `description`: Row per frustration parameter λ.

### step_02_ft_results.csv
- path: `/app/outputs/step_02_ft_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Finite-temperature physical quantities computed from the self-consistent solution.
- schema:
  - `type`: table
  - `required_columns`: `lambda`, `T`, `delta`, `Cg`, `Cd`, `C2g`, `chi`
  - `column_types`:
    - `lambda`: float
    - `T`: float
    - `delta`: float
    - `Cg`: float
    - `Cd`: float
    - `C2g`: float
    - `chi`: float
  - `description`: Row per combination of frustration λ and temperature T.

Notes: All values are in units defined by J1=1. Checker compares agent-reported values against expected quantities derived from the paper's published data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_t0_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda",
          "m",
          "delta",
          "Cg",
          "Cd",
          "C2g",
          "Cg_plus_d",
          "C2d"
        ],
        "column_types": {
          "lambda": "float",
          "m": "float",
          "delta": "float",
          "Cg": "float",
          "Cd": "float",
          "C2g": "float",
          "Cg_plus_d": "float",
          "C2d": "float"
        },
        "description": "Row per frustration parameter λ."
      },
      "description": "Ground-state physical quantities computed from the self-consistent solution at T=0."
    },
    {
      "file": "step_02_ft_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda",
          "T",
          "delta",
          "Cg",
          "Cd",
          "C2g",
          "chi"
        ],
        "column_types": {
          "lambda": "float",
          "T": "float",
          "delta": "float",
          "Cg": "float",
          "Cd": "float",
          "C2g": "float",
          "chi": "float"
        },
        "description": "Row per combination of frustration λ and temperature T."
      },
      "description": "Finite-temperature physical quantities computed from the self-consistent solution."
    }
  ],
  "notes": "All values are in units defined by J1=1. Checker compares agent-reported values against expected quantities derived from the paper's published data."
}
```

## How you are scored
A hidden verifier reads each of your output CSV files and compares every reported numeric value to a hidden gold standard derived from the original publication's data. The comparison uses tolerances appropriate for a numerical re-implementation. The verifier combines the per-stage scores (with the main weight on the T=0 and finite-temperature results) into a final reward between 0 and 1. Full credit requires that the physical trends – such as the vanishing of the magnetisation and the opening of the gap around a critical λ – are correctly captured, not that every decimal digit matches the paper's numbers exactly.
