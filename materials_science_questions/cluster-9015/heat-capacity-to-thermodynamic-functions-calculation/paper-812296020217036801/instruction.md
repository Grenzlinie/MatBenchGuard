# Recovering thermodynamic coefficients from equilibrium constants using method of intervals

## Problem background
Experimental equilibrium constants (R ln K) as a function of temperature can be used to derive thermodynamic properties such as entropy, enthalpy, and heat capacity. However, directly fitting an arbitrary function of temperature to R ln K often leads to statistical rejection of higher‑order heat‑capacity terms (a temperature‑linear term Δb and a quadratic term Δc) that may be physically present. The studied work addresses this by reversing the usual priority: a flexible empirical form for ΔCp° (T) is chosen first, and then integrated to obtain an explicit linear expression for R ln K. A method of intervals is developed that uses finite differences to compute a diagnostic Z function; this makes it possible to recover the full set of thermodynamic coefficients — ΔS°298, ΔH°298, ΔCp°298, Δb, and Δc — even when conventional regression would omit the higher‑order terms. The task is to implement this procedure on two synthetic parameter sets and demonstrate recovery of the five coefficients.

## Approach
The treatment is based on the Planck function and the empirical form ΔCp°(T) = Δa + Δb T + Δc T². Algebraic manipulation yields a linear‑in‑parameters equation:
R ln K°(m) = ΔS°298 − ΔH°298·K₁ + ΔCp°298·K₂ + Δb·K₃ + Δc·K₄,
where K₁, K₂, K₃, K₄ are temperature‑dependent variables (TDV) that depend only on T and the reference temperature 298.15 K; their definitions are standard and can be implemented directly.

The method of intervals operates on this equation as follows:
1. Divide the temperature range into fixed intervals (here 20 °C from 0 to 100 °C).
2. Compute finite differences ΔR ln K and Δ of the TDV over each interval. From these form the ratio ΔR ln K / ΔK₁.
3. Take second differences to construct a Z function, which can be shown to have the form Z = ΔCp°298 + Δb·x + Δc·y, where x and y are known combinations of interval TDV differences.
4. Fit Z values against x and y (multiple linear regression) to obtain ΔCp°298, Δb, and Δc.
5. Use the obtained coefficients to correct the original R ln K values: R ln K' = R ln K − (ΔCp°298·K₂ + Δb·K₃ + Δc·K₄).
6. Finally, fit R ln K' = ΔS°298 − ΔH°298·K₁ to recover ΔS°298 and ΔH°298.

This procedure is applied to two distinct parameter sets (Set A and Set B) that exhibit different temperature‑dependence patterns of ΔCp°.

## Reproduction target
Produce the file recovered_parameters.csv containing the five thermodynamic coefficients for both Set A and Set B, recovered by the method of intervals.

Generating parameters (use these to create the exact R ln K data):
- Set A:  ΔS°298 = −20.0 cal K⁻¹ mol⁻¹, ΔH°298 = −1000.0 cal mol⁻¹, ΔCp°298 = −15.0 cal K⁻¹ mol⁻¹, Δb = 4.0 cal K⁻² mol⁻¹, Δc = −0.0055 cal K⁻³ mol⁻¹.
- Set B:  same base parameters except Δb = 0.6 and Δc = −0.0008.

Procedure:
1. Compute exact R ln K°(m) at 21 temperatures from 0 °C to 100 °C in steps of 5 °C (i.e., 0, 5, 10, …, 100 °C) using the linear equation with the given parameters.
2. Add independent Gaussian noise to each exact value using standard deviation σ = |R ln K| / 1500. Use a fixed random seed of 42 for reproducibility.
3. Apply the method of intervals (20 °C intervals: 0‑20, 20‑40, …, 80‑100) to recover the five parameters for each set, as described in the Approach.
4. Write `recovered_parameters.csv` with columns: set (A or B), DeltaS (cal/K/mol), DeltaH (cal/mol), DeltaCp (cal/K/mol), Delta_b (cal/K²/mol), Delta_c (cal/K³/mol). One row for Set A, one row for Set B.

## Assets

- Python 3.8+: python
- NumPy: numpy
- SciPy: scipy
- pandas: pandas

## Workflow steps

### Step 1: Compute temperature-dependent variables (TDV) and auxiliary variables
- Role: process
- Action: Compute the temperature-dependent variables K1, K2, K3, K4 from the method's formulas (using temperature T and reference temperature 298.15 K). Then compute the derived auxiliary variables ΔK1, x, and y for 20 °C intervals (0–20, 20–40, ..., 80–100) needed for the method of intervals.
- Evidence: `/app/outputs/tdv_values.csv`

### Step 2: Generate exact R ln K°(m) values
- Role: process
- Action: Using the linear equation (eq 8 from the method) and the specified generating parameters for Set A and Set B, compute exact R ln K°(m) values at 21 evenly spaced temperatures from 0 °C to 100 °C (step 5 °C). Save the exact values.
- Evidence: `/app/outputs/exact_RlnK.csv`

### Step 3: Add noise to simulate experimental uncertainties
- Role: process
- Action: For each exact R ln K value, add Gaussian noise with standard deviation σ = |R ln K| / 1500. Use a fixed random seed 42 for reproducibility. The result is the simulated experimental R ln K°(m) dataset.
- Evidence: `/app/outputs/simulated_RlnK.csv`

### Step 4: Recover thermodynamic parameters via method of intervals
- Role: scored (load-bearing)
- Action: For Set A and Set B separately, apply the method of intervals: (a) compute ΔR ln K / ΔK1 for consecutive 20 °C intervals; (b) form second differences to obtain Z values; (c) fit Z = ΔCp°298 + Δb · x + Δc · y using linear regression to obtain ΔCp°298, Δb, Δc; (d) compute corrected R ln K' and fit R ln K' = ΔS°298 − ΔH°298 · K1 to obtain ΔS°298 and ΔH°298. Output the five recovered parameters for both sets.
- Output file: `/app/outputs/recovered_parameters.csv`
- Format: csv
- Contract: Columns: set (string, A or B), DeltaS (float, cal/K/mol), DeltaH (float, cal/mol), DeltaCp (float, cal/K/mol), Delta_b (float, cal/K^2/mol), Delta_c (float, cal/K^3/mol). One row per set.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/recovered_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### recovered_parameters.csv
- path: `/app/outputs/recovered_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Recovered thermodynamic parameters for Set A and Set B using the method of intervals.
- schema:
  - `type`: table
  - `required_columns`: `set`, `DeltaS`, `DeltaH`, `DeltaCp`, `Delta_b`, `Delta_c`
  - `units`:
    - `DeltaS`: cal/K/mol
    - `DeltaH`: cal/mol
    - `DeltaCp`: cal/K/mol
    - `Delta_b`: cal/K^2/mol
    - `Delta_c`: cal/K^3/mol

Notes: The checker recomputes the reference parameters using the same generating parameters, noise model, and seed, then compares element-wise against the agent's submission.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "recovered_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "set",
          "DeltaS",
          "DeltaH",
          "DeltaCp",
          "Delta_b",
          "Delta_c"
        ],
        "units": {
          "DeltaS": "cal/K/mol",
          "DeltaH": "cal/mol",
          "DeltaCp": "cal/K/mol",
          "Delta_b": "cal/K^2/mol",
          "Delta_c": "cal/K^3/mol"
        }
      },
      "description": "Recovered thermodynamic parameters for Set A and Set B using the method of intervals."
    }
  ],
  "notes": "The checker recomputes the reference parameters using the same generating parameters, noise model, and seed, then compares element-wise against the agent's submission."
}
```

## How you are scored
A hidden verifier independently recomputes the exact same pipeline (same equations, same generating parameters, same noise model and seed) to produce a reference set of recovered parameters. It then reads your `recovered_parameters.csv` and compares each parameter for Set A and Set B element‑wise against this reference. The reward is based on how close your submitted values are to the reference; the closer they are, the higher the score, up to a maximum of 1.0. Tolerances are not disclosed, but the task is designed so that a faithful implementation of the described method will pass.
