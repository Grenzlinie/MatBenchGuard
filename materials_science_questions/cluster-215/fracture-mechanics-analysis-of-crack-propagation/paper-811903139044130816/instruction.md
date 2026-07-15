# Fracture Stress vs. Stress-Strain Curve Exponent

## Problem background
Materials exhibit different elastic stress-strain curve shapes: r‑shaped (common in rubber), linear (e.g., helical springs), and J‑shaped (found in many biological tissues). Whether a J‑shaped curve imparts enhanced crack resistance is debated. This task examines that question using an energy‑balance fracture‑mechanics framework applied to a power‑law constitutive model σ = ε(λ‑1)^n, where the exponent n tunes the curve shape. The analysis focuses on two test geometries – a mode‑II shear‑like setup and a pure‑tension crack – to quantify how fracture stress depends on n and on dimensionless combinations of fracture surface energy, modulus parameter, specimen size, and crack length.

## Approach
The material is described by a power‑law stress‑strain relation with modulus ε and exponent n. In the mode‑II geometry, energy conservation leads to an explicit expression for the fracture stress σ in terms of n and the dimensionless group R/(εd) (fracture energy, modulus, specimen thickness). In the tension test, the Rivlin‑Thomas approximation for the strain‑energy release rate, together with a slowly varying function K(λ)≈k/√λ (k≈3), yields an implicit equation that must be solved numerically to find the critical stretch λ and then σ. For each geometry, fracture stress is computed as a function of n across a series of fixed dimensionless parameters. Two sets of output tables are produced: one for the mode‑II case covering several parameter values, and one for the tension case covering two representative parameter sets. Note that trouser‑tear and lubricated‑cutting tests are not considered here because their cracking force is independent of the stress–strain curve shape.

## Reproduction target
Compute and save, in CSV format, the fracture stress σ (in Pa) as a function of the exponent n (dimensionless) for the two geometries described in the workflow. For the mode‑II case, compute σ for n ranging from 0.2 to 4 at six values of the parameter R/(εd): 0.5, 1e‑5, 1e‑4, 1e‑3, 1e‑2, 1e‑1. For the tension case, compute σ for n ∈ {0.2, 0.5, 1, 2, 4} at two values of the parameter R/(2kcε) that correspond to two physically distinct parameter choices. The output files must follow the exact column schemas given in the workflow steps and output contract.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Mode II fracture stress calculation
- Role: scored (load-bearing)
- Action: Using the energy-balance fracture mechanics and the power-law constitutive model σ = ε(λ-1)^n, derive the fracture stress expression for the mode II test piece (figure 3c) in terms of parameters R (fracture surface energy), ε (modulus parameter), and d (specimen thickness). Compute the fracture stress for exponent n ranging from 0.2 to 4 (at least 20 equispaced points) for six values of the dimensionless parameter R/(εd): 0.5, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1. For the base parameter 0.5, use ε = 1e6 Pa, d = 10 mm. For the other parameters, keep ε = 1e6 Pa and d = 10 mm, and set R accordingly (R = p·ε·d). Output a CSV file with one row per (n, parameter) combination.
- Output file: `/app/outputs/mode_II_fracture_stress.csv`
- Format: csv
- Contract: columns: n (float, dimensionless), sigma_Pa (float, fracture stress in Pa), parameter_R_over_epsilon_d (float, dimensionless). One row per (n, parameter) combination; at least 20 values of n for each of the 6 parameter values, giving ≥120 rows.
- Scoring: scored by hidden verifier

### Step 2: Tension test fracture stress calculation
- Role: scored
- Action: For the tension test, apply the Rivlin-Thomas approximation for the energy release rate K(λ)=k/√λ with k ≈ 3.0. Using the power-law strain energy density W0 = ε(λ-1)^{n+1}/(n+1), set up the energy balance fracture criterion R = 2 K(λ) c W0. Solve the resulting implicit equation for the critical extension ratio λ at fracture, then compute the fracture stress σ = ε(λ-1)^n. Evaluate for n ∈ {0.2, 0.5, 1, 2, 4} and for two parameter sets: (1) ε = 1e6 Pa, R = 5000 J/m², c = 1 mm → R/(2k c ε) ≈ 0.7958 (k=3.0); (2) ε = 1e6 Pa, R = 500 J/m², c = 10 mm → R/(2k c ε) ≈ 0.007958. Output a CSV file with one row per (n, parameter) combination.
- Output file: `/app/outputs/tension_fracture_stress.csv`
- Format: csv
- Contract: columns: n (float, dimensionless), sigma_Pa (float, fracture stress in Pa), parameter_R_over_2kc_epsilon (float, dimensionless). One row per (n, parameter) combination, yielding 2×5 = 10 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mode_II_fracture_stress.csv`
- `/app/outputs/tension_fracture_stress.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mode_II_fracture_stress.csv
- path: `/app/outputs/mode_II_fracture_stress.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Fracture stress as a function of exponent n for the mode II geometry, for several values of the dimensionless parameter R/(εd). The checker will recompute sigma from the reported n and parameter using the energy-balance formula and compare within relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `n`, `sigma_Pa`, `parameter_R_over_epsilon_d`
  - `units`:
    - `n`: dimensionless
    - `sigma_Pa`: Pa
    - `parameter_R_over_epsilon_d`: dimensionless

### tension_fracture_stress.csv
- path: `/app/outputs/tension_fracture_stress.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Fracture stress as a function of exponent n for the tension test, for two values of the dimensionless parameter R/(2kcε). The checker will solve the implicit equation from the reported n and parameter using the same Rivlin-Thomas approximation, then recompute sigma and compare within relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `n`, `sigma_Pa`, `parameter_R_over_2kc_epsilon`
  - `units`:
    - `n`: dimensionless
    - `sigma_Pa`: Pa
    - `parameter_R_over_2kc_epsilon`: dimensionless

Notes: The trouser tear and lubricated cutting analyses are trivial force-balance equalities and are intentionally omitted from the computational reproduction. The two scored CSV files capture the complete computed headline results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mode_II_fracture_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "sigma_Pa",
          "parameter_R_over_epsilon_d"
        ],
        "units": {
          "n": "dimensionless",
          "sigma_Pa": "Pa",
          "parameter_R_over_epsilon_d": "dimensionless"
        }
      },
      "description": "Fracture stress as a function of exponent n for the mode II geometry, for several values of the dimensionless parameter R/(εd). The checker will recompute sigma from the reported n and parameter using the energy-balance formula and compare within relative tolerance."
    },
    {
      "file": "tension_fracture_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "sigma_Pa",
          "parameter_R_over_2kc_epsilon"
        ],
        "units": {
          "n": "dimensionless",
          "sigma_Pa": "Pa",
          "parameter_R_over_2kc_epsilon": "dimensionless"
        }
      },
      "description": "Fracture stress as a function of exponent n for the tension test, for two values of the dimensionless parameter R/(2kcε). The checker will solve the implicit equation from the reported n and parameter using the same Rivlin-Thomas approximation, then recompute sigma and compare within relative tolerance."
    }
  ],
  "notes": "The trouser tear and lubricated cutting analyses are trivial force-balance equalities and are intentionally omitted from the computational reproduction. The two scored CSV files capture the complete computed headline results."
}
```

## How you are scored
A hidden verifier (not visible to you) independently evaluates each scored artifact. For the mode‑II file, it reads each row’s n and parameter_R_over_epsilon_d and recomputes σ from the energy‑balance formula. For the tension file, it reads each row’s n and parameter_R_over_2kc_epsilon, solves the implicit equation for λ using the same Rivlin‑Thomas approximation, and then recomputes σ. The computed values are compared against a hidden gold within a prescribed tolerance. The two files are weighted equally (50% each) and the final score is a floating‑point number between 0 and 1. Reporting accurate numbers that reflect a correct implementation of the physics is essential; approximate or guessed values will degrade the score.
