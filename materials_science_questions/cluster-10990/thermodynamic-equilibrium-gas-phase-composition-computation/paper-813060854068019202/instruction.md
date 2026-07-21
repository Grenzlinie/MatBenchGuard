# Thermodynamic Calculation of Iodine Vapor Pressure over Mercuric Iodide

## Problem background
During vapor growth of large α-HgI₂ crystals in closed evacuated ampoules, the solid phase exhibits a nonstoichiometry range, i.e., its composition x = I/Hg can deviate from the exact 2:1 ratio. The composition of the gas phase in equilibrium with such a solid depends on temperature and solid composition. In particular, the partial pressure of molecular iodine (p_I₂) is an indicator that is often monitored during growth. This task reproduces the thermodynamic calculation of the equilibrium iodine partial pressure as a function of temperature for a given (slightly mercury‑rich) solid composition.

## Approach
The system is modeled as solid α-HgI₂ in equilibrium with a gas phase. The iodine partial pressure is set by the solid composition x via the empirical relation

log₁₀ p_I₂(x,T) = z₁ + z₂·x + z₃/T + z₄·x/T

where T is in Kelvin. The four coefficients z₁…z₄ are obtained by a local fitting procedure: for a temperature of interest, two phase‑boundary points at two nearby temperatures (|ΔT| ≤ 5 K) are used to form a linear system from the empirical relation evaluated at those (x,T) pairs. The two temperatures must both be present in the asset data; for each of them two boundary points (iodine‑rich and mercury‑rich) are taken, giving four data points in total—enough to determine the four unknowns. Repeating this fit over the temperature range yields a numerical p_I₂(x,T) relation. Finally, for a fixed composition x = 1.99, the empirical relation directly gives p_I₂ without solving the full reaction equilibrium (other component pressures are not needed for this task).

## Reproduction target
Implement the thermodynamic workflow and produce a CSV file with the equilibrium partial pressure of I₂(g) for the mercury‑rich composition x = 1.99 at temperatures from 100 °C to 150 °C inclusive, in steps of 5 °C. The output must contain columns 'temperature_C' and 'p_I2_mbar' (in mbar). The hidden verifier will compare your computed values against a recomputed reference within a relative tolerance and also validate structural properties of the p_I₂ vs. T curve.

## Assets

1. **Phase‑boundary composition data** – file `/assets/phase_boundary_data.csv`  
   Columns:  
   - `T_C` : temperature in °C  
   - `x_I_rich` : mole ratio I/Hg at the iodine‑rich phase boundary (x > 2)  
   - `x_Hg_rich` : mole ratio I/Hg at the mercury‑rich phase boundary (x < 2)  
   The data have been digitised from Fig. 1 of Hermon et al. (1993), with the scale corrected according to Roth (1995).

2. **Phase‑boundary iodine pressure data** – file `/assets/boundary_p_I2.csv`  
   This file provides the equilibrium iodine partial pressure on both phase boundaries as a function of temperature.  
   Columns:  
   - `T_C` : temperature in °C  
   - `p_I2_I_rich_mbar` : p_I₂ in mbar on the iodine‑rich boundary (coexisting with solid/liquid iodine)  
   - `p_I2_Hg_rich_mbar` : p_I₂ in mbar on the mercury‑rich boundary (coexisting with solid Hg₂I₂, determined by reaction 5)  
   These values have been computed from the thermodynamic data compiled by Knacke et al. (1991), using the method described in the paper. Use this file directly in your code.

## Workflow steps

### Step 1: Fit empirical coefficients z₁–z₄ (internal)
- **Role:** process  
- **Action:** For each target temperature T in the range 100 °C to 150 °C (step 5 °C), select two temperatures T₁ and T₂ from the asset files such that |T₁ − T₂| ≤ 5 K and both T₁ and T₂ exist in the data (e.g., the target temperature T itself and the next higher or lower temperature in the asset tables).  

  For each of the two temperatures, read the following four values from the two asset files:
  - iodine‑rich composition x = x_I_rich (from `/assets/phase_boundary_data.csv`)
  - mercury‑rich composition x = x_Hg_rich (from `/assets/phase_boundary_data.csv`)
  - iodine‑rich boundary pressure p_I₂ = p_I2_I_rich_mbar (from `/assets/boundary_p_I2.csv`)
  - mercury‑rich boundary pressure p_I₂ = p_I2_Hg_rich_mbar (from `/assets/boundary_p_I2.csv`)

  You now have four data points, each of the form (x, T, p_I₂). Using the empirical relation  

  log₁₀ p_I₂ = z₁ + z₂·x + z₃/T + z₄·x/T  

  write one equation per point. This gives a linear system in z₁…z₄:  

  z₁ + z₂·x_i + z₃/T_i + z₄·(x_i/T_i) = log₁₀ p_I₂,i    (i = 1…4)  

  Solve this 4×4 system numerically to obtain z₁, z₂, z₃, z₄.  
  With the coefficients known, evaluate the iodine partial pressure for the mercury‑rich composition x = 1.99 at the target temperature T using  

  p_I₂ = 10^(z₁ + z₂·x + z₃/T + z₄·x/T).  

  Repeat this local fitting for every target temperature T in the set {100, 105, …, 150 °C} to generate the output points.  
  **Note:** you may perform the fit numerically without writing intermediate files; no separate output is required for this step.

### Step 2: Compute equilibrium p_I₂ for Hg‑rich composition
- **Role:** scored (load‑bearing)  
- **Action:** For the mercury‑rich composition x = 1.99, evaluate the equilibrium partial pressure of I₂(g) at each temperature T in the range 100–150 °C (step 5 °C) using the coefficients obtained in Step 1. Write the results to the output CSV file.  
- **Output file:** `/app/outputs/p_I2_vs_T_Hg_rich.csv`  
- **Format:** csv  
- **Contract:** CSV with columns: `temperature_C` (float, °C, covering 100–150 °C with exactly 5 °C step) and `p_I2_mbar` (float, computed equilibrium partial pressure of I₂(g) in mbar).  
- **Scoring:** scored by hidden verifier

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
- description: Equilibrium partial pressure of I₂(g) over mercury‑rich α‑HgI₂ (x=1.99) as a function of temperature. The checker will perform a point‑wise comparison against a recomputed reference and also evaluate the structural shape of the p_I₂ curve.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `p_I2_mbar`
  - `units`:
    - `temperature_C`: °C
    - `p_I2_mbar`: mbar

Notes: The hidden verifier applies additional scoring criteria based on the shape of the p_I₂(T) curve. The agent does not need to output separate files for these checks.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, and CSV tables contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

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
      "description": "Equilibrium partial pressure of I₂(g) over mercury‑rich α‑HgI₂ (x=1.99) as a function of temperature."
    }
  ]
}
```

## How you are scored
A hidden verifier inspects your submitted artifacts. The CSV from Step 2 is the main scored output. The verifier independently recomputes p_I₂ for x=1.99 from the same inputs and scores your values point‑wise within an appropriate tolerance. Additionally, it performs structural checks on the shape of the p_I₂(T) curve (e.g., threshold crossing behaviour and maximum value). The final reward combines these checks. Simply reporting numbers from the literature without running the computation will not satisfy the verifier.