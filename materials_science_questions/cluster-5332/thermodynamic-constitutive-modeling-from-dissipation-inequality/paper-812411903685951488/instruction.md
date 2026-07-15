# Prediction of Austenite/Ferrite Transformation Start Temperatures Using a Generalized Additivity Rule

## Problem background
Prediction of the onset of diffusion-controlled phase transformations under non‑isothermal conditions is essential for designing heat treatment schedules. The classical Scheil–Cahn additivity rule relates the isothermal incubation time τ_in(T) to a cumulative integral condition that marks the transformation start during cooling. However, this traditional rule often shows significant disagreement with experimentally measured continuous‑cooling‑transformation (CCT) diagrams. A non‑linear extension of the additivity concept has been proposed that introduces a temperature‑dependent exponent S(T) into the integral, aiming to better capture the influence of the thermal path on the onset of transformation. The task is to implement the generalized additivity rule and compute the transformation start temperatures for a series of Newtonian cooling curves, comparing the predictions with those of the classical rule.

## Approach
The isothermal incubation time for austenite/ferrite transformation is given by the empirical function
τ_in(T) = 10^(0.16095 + 70.2299/(825−T) + 10.0144/(825−T)^2),
where T is temperature in °C and τ_in is in seconds.
Cooling is assumed to follow Newtonian cooling: T(t)=20+780 exp(−α t), with cooling coefficient α (s⁻¹).
The additivity integral is defined as
G(t) = ∫_0^t S(T(t_u)) · t_u^{S(T(t_u))−1} / [τ_in(T(t_u))]^{S(T(t_u))} dt_u.
When S ≡ 1, this reduces to the traditional Scheil–Cahn rule. The generalized rule uses the temperature‑dependent function
S(T) = 1.083 − 0.00106·T.
For each α in {1e-6, 5e-6, 1e-5, 5e-5, 1e-4, 5e-4, 1e-3, 5e-3, 1e-2, 2e-2} s⁻¹, numerically find the root t_f satisfying G(t_f)=1, and record the corresponding start temperature T_start = T(t_f). Compute t_f twice per α: once with S=1 (traditional) and once with S=S(T) (generalized). Use numerical integration and root‑finding, e.g., via `scipy.integrate.quad` and `scipy.optimize.brentq`. Output the ten rows to the specified CSV file.

## Reproduction target
For each of the ten cooling coefficients α listed above, compute the transformation start temperature using both the traditional (S=1) and the generalized (S(T) as given) additivity rules. Write a CSV file with exactly ten rows, three comma‑separated float fields per row: alpha (s⁻¹), T_start_traditional (°C), T_start_generalized (°C). The file must have no header line.

## Assets

- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Compute transformation start temperatures
- Role: scored (load-bearing)
- Action: Implement the generalized additivity integral G(t)=∫_0^t s(T(t_u)) t_u^{s(T(t_u))−1} / [τ_in(T(t_u))]^{s(T(t_u))} dt_u with τ_in(T)=10^(0.16095 + 70.2299/(825−T) + 10.0144/(825−T)^2). Cooling is Newtonian: T(t)=20+780 exp(−α t). For each α in [1e-6, 5e-6, 1e-5, 5e-5, 1e-4, 5e-4, 1e-3, 5e-3, 1e-2, 2e-2] s⁻¹, numerically find the root t_f such that G(t_f)=1. Compute the start temperature T_start = T(t_f) once with S=1 (traditional) and once with S(T)=1.083−0.00106·T (generalized). Write the ten rows into /app/outputs/transformation_start_temperatures.csv as three floats (alpha, T_start_traditional, T_start_generalized, no header). Use numerical integration (e.g., scipy.integrate.quad) and a root-finding method.
- Output file: `/app/outputs/transformation_start_temperatures.csv`
- Format: csv
- Contract: Ten rows, each with three comma-separated float fields in the order: alpha (s⁻¹), T_start_traditional (°C), T_start_generalized (°C). No header line.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transformation_start_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transformation_start_temperatures.csv
- path: `/app/outputs/transformation_start_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed transformation start temperatures for ten cooling rates. The checker independently recomputes T_start_generalized for each alpha using the same formulas and numerical integration, and compares within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `T_start_traditional`, `T_start_generalized`
  - `header`: False
  - `units`:
    - `alpha`: s^-1
    - `T_start_traditional`: °C
    - `T_start_generalized`: °C

Notes: The generalized rule uses S(T)=1.083−0.00106·T. The traditional rule uses S=1. The file must have exactly ten rows; no header.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transformation_start_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "T_start_traditional",
          "T_start_generalized"
        ],
        "header": false,
        "units": {
          "alpha": "s^-1",
          "T_start_traditional": "°C",
          "T_start_generalized": "°C"
        }
      },
      "description": "Computed transformation start temperatures for ten cooling rates. The checker independently recomputes T_start_generalized for each alpha using the same formulas and numerical integration, and compares within a tolerance."
    }
  ],
  "notes": "The generalized rule uses S(T)=1.083−0.00106·T. The traditional rule uses S=1. The file must have exactly ten rows; no header."
}
```

## How you are scored
A hidden verifier will independently re‑implement the same formulas and numerical integration to recompute the transformation start temperatures. It compares your computed T_start_generalized values to its own recomputed values for each α. Lines where the difference is within a hidden numerical tolerance earn partial credit; the full score is obtained when all generalized‑rule temperatures agree with the recomputation. The traditional‑rule values (T_start_traditional) are checked only for plausibility and do not directly carry credit, but they must be present and correctly computed for the task to be considered complete. The verifier also validates the file format and row count. Only a correct implementation of the integral and root‑finding will match the hidden recomputation; reporting values you may have encountered elsewhere will not pass.
