# Thermodynamic Calculation of Iodine Vapor Pressure over Mercuric Iodide

## Problem background
During vapor growth of large α-HgI₂ crystals in closed evacuated ampoules, the solid phase exhibits a nonstoichiometry range, i.e., its composition x = I/Hg can deviate from the exact 2:1 ratio. The composition of the gas phase in equilibrium with such a solid depends on temperature and solid composition. In particular, the partial pressure of molecular iodine (p_I₂) is an indicator that is often monitored during growth. This task reproduces the thermodynamic calculation of the equilibrium iodine partial pressure as a function of temperature for a given (slightly mercury‑rich) solid composition. The computed p_I₂(T) can then be compared to a known visibility threshold to infer the possible solid stoichiometry.

## Approach
The system is modeled as solid α-HgI₂ in equilibrium with a five‑species gas phase (HgI₂, I₂, Hg, HgI, I). The gas‑phase composition is determined by four independent reactions with temperature‑dependent equilibrium constants Kp₁…Kp₄ (provided from the Knacke et al. thermochemical compilation). The iodine partial pressure is not free but is set by the solid composition x via the empirical relation log₁₀ p_I₂(x,T) = z₁ + z₂·x + z₃/T + z₄·x/T. The four coefficients z₁…z₄ are obtained by a local fitting procedure: for a temperature of interest, two phase‑boundary points at nearby temperatures (|ΔT| ≤ 5 K) are used to form a linear system from the empirical relation evaluated at those (x,T) pairs. Repeating this over the temperature range yields a numerical p_I₂(x,T) relation. Finally, for a fixed composition, the equilibrium equations are solved to obtain all partial pressures, in particular p_I₂. The visibility threshold of iodine vapour (0.04 mbar) is a known physical reference used by the hidden checker to validate the computed p_I₂ behaviour.

## Reproduction target
Implement the thermodynamic workflow and produce a CSV file with the equilibrium partial pressure of I₂(g) for the mercury‑rich composition x = 1.99 at temperatures from 100 °C to 150 °C inclusive, in steps of 5 °C. The output must contain columns 'temperature_C' and 'p_I2_mbar' (in mbar). The hidden verifier will compare your computed values against a recomputed reference and also verify that the p_I₂ values exhibit the correct behaviour relative to the known visibility threshold of 0.04 mbar.

## Assets

- Phase-boundary (x,T) data for α-HgI₂ homogeneity range
- Equilibrium constants Kp₁–Kp₄ from Knacke et al. thermochemical data

## Workflow steps

### Step 1: Fit empirical coefficients z₁–z₄
- Role: process
- Action: Fit the coefficients z₁, z₂, z₃, z₄ of the empirical relation log10 p_I₂(x,T) = z₁ + z₂·x + z₃/T + z₄·x/T using the provided phase-boundary (x,T) data. Apply the local fitting procedure: for each temperature of interest, solve the linear system formed by two nearby temperatures (|ΔT| ≤ 5 K) and their phase-boundary compositions. Store the resulting numerical relationship for use in Step 2.
- Evidence: `/app/outputs/fitted_z_values.csv`

### Step 2: Compute equilibrium p_I₂ for Hg-rich composition
- Role: scored (load-bearing)
- Action: For the mercury-rich composition x = 1.99, evaluate the equilibrium partial pressure of I₂(g) at each temperature T in the range 100–150 °C (step 5 °C). Use the empirical relation from Step 1 for p_I₂(x,T) together with the provided equilibrium constants Kp₁–Kp₄ to solve the coupled reaction equilibria. Write the results to the output CSV file.
- Output file: `/app/outputs/p_I2_vs_T_Hg_rich.csv`
- Format: csv
- Contract: CSV with columns: temperature_C (float, °C, covering 100–150 °C with step ≤ 5 K), p_I2_mbar (float, computed equilibrium partial pressure of I₂(g) in mbar).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/p_I2_vs_T_Hg_rich.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### p_I2_vs_T_Hg_rich.csv
- path: `/app/outputs/p_I2_vs_T_Hg_rich.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium partial pressure of I₂(g) over mercury-rich α-HgI₂ (x=1.99) as a function of temperature. The checker will compare each value against a recomputed reference within a relative tolerance and also validate the structural property that p_I2 > 0.04 mbar only in the narrow temperature range around 120 °C and that the maximum is approximately 0.1 mbar.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `p_I2_mbar`
  - `units`:
    - `temperature_C`: °C
    - `p_I2_mbar`: mbar

Notes: The structural checks (threshold-crossing interval and maximum value) are additional scoring criteria applied by the hidden checker on the submitted CSV. The agent does not need to output separate files for them.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "p_I2_vs_T_Hg_rich.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "p_I2_mbar"
        ],
        "units": {
          "temperature_C": "°C",
          "p_I2_mbar": "mbar"
        }
      },
      "description": "Equilibrium partial pressure of I₂(g) over mercury-rich α-HgI₂ (x=1.99) as a function of temperature. The checker will compare each value against a recomputed reference within a relative tolerance and also validate the structural property that p_I2 > 0.04 mbar only in the narrow temperature range around 120 °C and that the maximum is approximately 0.1 mbar."
    }
  ],
  "notes": "The structural checks (threshold-crossing interval and maximum value) are additional scoring criteria applied by the hidden checker on the submitted CSV. The agent does not need to output separate files for them."
}
```

## How you are scored
A hidden verifier inspects your submitted artifacts. The CSV from Step 2 is the main scored output. The verifier independently recomputes p_I₂ for x=1.99 from the same inputs and scores your values point‑wise within an appropriate tolerance. Additionally, it performs structural checks: it verifies that your p_I₂ values cross the 0.04 mbar visibility threshold in a temperature interval that matches the correct thermodynamic result, and that the maximum p_I₂ in the scanned range is within a tolerance of the expected peak. The final reward combines these checks. Simply reporting numbers from the literature without running the computation will not satisfy the verifier.
