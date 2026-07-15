# Compute spherical growth parabolic rate constants under paraequilibrium

## Problem background
The growth of ferrite in steels, particularly intragranular idiomorphs nucleated on inclusions, is often treated as a diffusion-controlled phase transformation. In Fe–C–Mn alloys, the measured growth rates are frequently lower than those predicted by simple carbon-diffusion models. This task quantifies the theoretical side of that discrepancy: you will compute the paraequilibrium spherical growth parabolic rate constants for intragranular ferrite at three reaction temperatures, using alloy composition, a public thermodynamic database, and the standard carbon diffusivity in austenite. The computed values will be used (by a hidden verifier) to test whether they follow a preregistered trend relative to experimental observations.

## Approach
The growth is modeled as shape-preserving spherical growth under paraequilibrium, where carbon partitions but substitutional elements do not. The calculation proceeds in two stages. First, use CALPHAD (via pycalphad and an Fe–C–Mn thermodynamic database) to determine the paraequilibrium carbon concentrations in austenite and ferrite at 650, 670, and 690 °C, from which the dimensionless carbon supersaturation S is obtained. Second, for each temperature, compute the carbon diffusivity D in austenite from a standard Arrhenius expression, solve the Sekerka–Wang integral equation for spheres numerically to find the parabolic rate parameter λ, and convert to the dimensional parabolic growth rate constant k = λ √D (half‑diameter growth constant, cm/s<sup>1/2</sup>). No experimental measurements are needed; all inputs are public.

## Reproduction target
Produce a CSV file (`calculated_parabolic_constants.csv`) containing the theoretical parabolic growth rate constants k (in cm/s<sup>1/2</sup>) for spherical growth under paraequilibrium at 650, 670, and 690 °C. Exactly three rows, with columns `temperature_C` (integer) and `parabolic_rate_constant_cm_sqrt_s` (float). The verifier will independently recompute these constants and compare them to hidden experimental values to check that they satisfy a preregistered directional relationship.

## Assets

- pycalphad: pip install pycalphad (Tsinghua mirror: https://pypi.tuna.tsinghua.edu.cn/simple)
- Fe-C-Mn thermodynamic database (TDB file): Publicly available Fe-C-Mn thermodynamic database (e.g., from the pycalphad sample database collection or the NIST SRD database). The agent must locate and load an appropriate TDB file for the Fe-C-Mn system.
- Carbon diffusivity in austenite: Standard Arrhenius expression from literature (e.g., D = 0.02 exp(-Q/RT) cm²/s with Q ≈ 122 kJ/mol). The agent may use a well-established literature value; no specific reference is mandated.

## Workflow steps

### Step 1: Compute paraequilibrium carbon supersaturation
- Role: process
- Action: Using the alloy composition (0.09 wt% C, 1.48 wt% Mn, 0.20 wt% Si, 0.011 wt% S, 0.05 wt% V, 0.0066 wt% N, 0.0012 wt% O, balance Fe) and a public Fe-C-Mn thermodynamic database (loaded via pycalphad), compute the paraequilibrium carbon concentrations in austenite and ferrite at 650, 670, and 690 °C. Calculate the supersaturation S = (C_gamma_bulk - C_gamma_para) / (C_gamma_para - C_alpha_para) for each temperature. Save the computed supersaturations to a JSON evidence file.
- Evidence: `/app/outputs/supersaturation_data.json`

### Step 2: Compute and output spherical parabolic growth constants
- Role: scored (load-bearing)
- Action: For each temperature (650, 670, 690 °C): (a) obtain the carbon diffusivity in austenite from a standard Arrhenius expression (units cm²/s); (b) solve the spherical growth integral equation S = 2 λ² exp(λ²) ∫_1^∞ exp(-λ² u²)/u² du numerically to find the parabolic rate parameter λ; (c) compute the parabolic growth rate constant k = λ √D (units cm/s^{1/2}), which corresponds to the half-diameter growth constant defined in the paper. Write the three constants to a CSV file.
- Output file: `/app/outputs/calculated_parabolic_constants.csv`
- Format: csv
- Contract: CSV with columns: temperature_C (integer), parabolic_rate_constant_cm_sqrt_s (float, in cm/s^{1/2}). Exactly three rows for temperatures 650, 670, 690.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_parabolic_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_parabolic_constants.csv
- path: `/app/outputs/calculated_parabolic_constants.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Theoretical parabolic growth-rate constants for spherical growth under paraequilibrium at 650, 670, and 690°C.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `parabolic_rate_constant_cm_sqrt_s`
  - `units`:
    - `parabolic_rate_constant_cm_sqrt_s`: cm/s^(1/2)

Notes: The agent must use the provided alloy composition, a public Fe-C-Mn TDB, and a standard carbon diffusivity in austenite. The spherical growth integral equation must be solved numerically. The checker will recompute the constants independently and verify that they exceed the hidden experimental values from the paper, within a relative tolerance (trend + recompute).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_parabolic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "parabolic_rate_constant_cm_sqrt_s"
        ],
        "units": {
          "parabolic_rate_constant_cm_sqrt_s": "cm/s^(1/2)"
        }
      },
      "description": "Theoretical parabolic growth-rate constants for spherical growth under paraequilibrium at 650, 670, and 690°C."
    }
  ],
  "notes": "The agent must use the provided alloy composition, a public Fe-C-Mn TDB, and a standard carbon diffusivity in austenite. The spherical growth integral equation must be solved numerically. The checker will recompute the constants independently and verify that they exceed the hidden experimental values from the paper, within a relative tolerance (trend + recompute)."
}
```

## How you are scored
A hidden verifier inspects each workflow stage. For the intermediate supersaturation step, it verifies that the computation was executed and records the result for provenance; no direct weight is assigned. For the scored output, the verifier re‑implements the spherical growth model using the same thermodynamic database and diffusivity expression, recomputes the parabolic rate constants independently, and compares them to your submitted values within a tolerance. Additionally, it checks that the computed constants satisfy a preregistered trend against the paper’s experimental values, which are hidden. Both checks must pass for full credit. Reporting the published numbers without executing the procedure is insufficient.
