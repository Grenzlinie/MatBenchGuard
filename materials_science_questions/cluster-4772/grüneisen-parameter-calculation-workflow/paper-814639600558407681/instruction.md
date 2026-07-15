# RMSD comparison of thermal expansion models for four minerals

## Problem background
Accurate prediction of thermal expansion for geophysical minerals at high temperatures is essential for thermodynamic modeling. Various analytical models have been proposed based on assumptions about the temperature dependence of the product of thermal expansion coefficient α and isothermal bulk modulus B_T. This task computes the root-mean-square deviations (RMSD) of volume ratio V/V0 and volumetric thermal expansion coefficient α between the predictions of three different models and published experimental data for four important minerals: MgO, CaO, Al₂O₃, and Mg₂SiO₄. The RMSD values serve as quantitative measures of model performance.

## Approach
Three analytical models are used to predict V/V0 and α at high temperatures, and their predictions are compared against experimental data.

The **present model** assumes that the product αB_T and the isothermal bulk modulus B_T are both linear functions of temperature T:

```
α(T) B_T(T) = α_r B_r + k (T - T_r)
B_T(T) = B_r + β (T - T_r)
```

where α_r, B_r, and T_r are the thermal expansion coefficient, bulk modulus, and temperature at a chosen reference, k is a mineral‑specific constant, and β = −α_r B_r δ_r (δ_r is the isothermal Anderson–Gruneisen parameter at T_r). Solving for α and integrating α = (1/V) ∂V/∂T gives expressions for α(T) and V/V_r. The volume ratio relative to room temperature (V/V0) is obtained by multiplying V/V_r by the experimental V_r/V0 at the reference temperature. The required input parameters (α_r, δ_r, B_r, k, T_r) for each mineral are listed below.

The **constant‑αB_T model** is the special case with k = 0, i.e. αB_T is assumed constant. This yields simpler formulas for α(T) and V/V_r that depend only on α_r and δ_r.

**Srivastava’s model** is based on two different assumptions: ln(B_T) is a linear function of V/V0, and B_T varies linearly with T. It introduces dimensionless fitting parameters m and d, together with room‑temperature (T₀ = 300 K) values α₀ and δ₀. The resulting expressions give V/V0 and α(T) as functions of T, m, d, α₀, δ₀, and T₀. The parameters m, d, α₀, δ₀ for each mineral are obtained from the cited Srivastava (2006) publication.

For each mineral, at every experimental temperature, the predicted V/V0 and α are computed from each model. The experimental temperature‑dependent V/V0 and α data are taken from Anderson (1995). The root‑mean‑square deviation (RMSD) of V/V0 (R_V, in 10⁻³) and of α (R_α, in 10⁻⁵ K⁻¹) is then calculated between the predictions and the experimental values for each model.

**Input parameters for the present model** (from the original paper):

| Mineral       | T_r (K) | α_r (10⁻⁵ K⁻¹) | δ_r  | B_r (GPa) | k (10⁻⁷ GPa·K⁻¹) |
|---------------|---------|----------------|------|-----------|-------------------|
| MgO           | 900     | 4.38           | 4.78 | 144.3     | −2.95             |
| CaO           | 700     | 3.92           | 5.07 | 102.3     | −1.34             |
| Al₂O₃         | 1000    | 2.73           | 5.42 | 231.4     | 5.03              |
| Mg₂SiO₄       | 800     | 3.59           | 5.47 | 116.3     | 3.16              |

## Reproduction target
Using the provided input parameters (table above) and the experimental data for V/V0 and α from Anderson (1995), for each mineral (MgO, CaO, Al₂O₃, Mg₂SiO₄) compute the RMSD values for the three models as described. Produce a single CSV file at /app/outputs/rmsd_table.csv with exactly four rows, one per mineral in the given order, containing the following columns:

- Mineral (string)
- R_V_Eq6 (float, unit 10⁻³)  → RMSD of V/V0 for the present model
- R_V_Eq10 (float, unit 10⁻³) → RMSD of V/V0 for the constant-αB_T model
- R_V_Eq11 (float, unit 10⁻³) → RMSD of V/V0 for Srivastava's model
- R_alpha_Eq4 (float, unit 10⁻⁵ K⁻¹) → RMSD of α for the present model
- R_alpha_Eq1 (float, unit 10⁻⁵ K⁻¹) → RMSD of α for the constant-αB_T model
- R_alpha_Eq14 (float, unit 10⁻⁵ K⁻¹) → RMSD of α for Srivastava's model

No other files are scored.

## Assets

- Experimental thermal expansion data for MgO, CaO, Al2O3, Mg2SiO4: 10.1093/oso/9780195056068.001.0001
- Present model parameters (α_r, δ_r, B_r, k, T_r) for each mineral
- Srivastava model parameters (m, d, α0, δ0) for each mineral: 10.1016/j.solidstatesciences.2006.02.027

## Workflow steps

### Step 1: Assemble input data
- Role: process
- Action: Collect the experimental thermal expansion data (temperature, V/V0, volumetric thermal expansion coefficient α) for MgO, CaO, Al2O3, and Mg2SiO4 from the public literature (e.g., Anderson 1995). Obtain the present model parameters (α_r, δ_r, B_r, k, T_r) from the instruction (Table 1 values). Obtain the Srivastava model parameters (m, d, α0, δ0) from Srivastava (2006).
- Evidence: none

### Step 2: Compute RMSD table
- Role: scored (load-bearing)
- Action: For each mineral and using the assembled data, compute the volume ratio V/V0 and volumetric thermal expansion coefficient α predicted by three models: (i) the present model (Eqs. 4 and 6), (ii) the constant-αB_T model (k=0, Eqs. 1 and 10), and (iii) Srivastava's model (Eqs. 11 and 14). Calculate the root-mean-square deviation (RMSD) of V/V0 and α between the predicted values and the experimental data for each model. Write the RMSD values in a CSV file with columns Mineral, R_V_Eq6, R_V_Eq10, R_V_Eq11, R_alpha_Eq4, R_alpha_Eq1, R_alpha_Eq14, with one row per mineral in the order MgO, CaO, Al2O3, Mg2SiO4.
- Output file: `/app/outputs/rmsd_table.csv`
- Format: csv
- Contract: CSV with columns Mineral (string), R_V_Eq6 (float, unit 10⁻³), R_V_Eq10 (float, 10⁻³), R_V_Eq11 (float, 10⁻³), R_alpha_Eq4 (float, unit 10⁻⁵ K⁻¹), R_alpha_Eq1 (float, 10⁻⁵ K⁻¹), R_alpha_Eq14 (float, 10⁻⁵ K⁻¹). Exactly 4 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rmsd_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rmsd_table.csv
- path: `/app/outputs/rmsd_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Root-mean-square deviations of volume ratio and thermal expansion coefficient for four minerals under three models, to be compared against the paper's Table 6.
- schema:
  - `type`: table
  - `required_columns`: `Mineral`, `R_V_Eq6`, `R_V_Eq10`, `R_V_Eq11`, `R_alpha_Eq4`, `R_alpha_Eq1`, `R_alpha_Eq14`
  - `row_count`: 4
  - `units`:
    - `R_V_Eq6`: 1e-3
    - `R_V_Eq10`: 1e-3
    - `R_V_Eq11`: 1e-3
    - `R_alpha_Eq4`: 1e-5 K^-1
    - `R_alpha_Eq1`: 1e-5 K^-1
    - `R_alpha_Eq14`: 1e-5 K^-1

Notes: The experimental data and model parameters are assembled by the agent. The hidden checker compares the reported RMSD values to the reference from the paper within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rmsd_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Mineral",
          "R_V_Eq6",
          "R_V_Eq10",
          "R_V_Eq11",
          "R_alpha_Eq4",
          "R_alpha_Eq1",
          "R_alpha_Eq14"
        ],
        "row_count": 4,
        "units": {
          "R_V_Eq6": "1e-3",
          "R_V_Eq10": "1e-3",
          "R_V_Eq11": "1e-3",
          "R_alpha_Eq4": "1e-5 K^-1",
          "R_alpha_Eq1": "1e-5 K^-1",
          "R_alpha_Eq14": "1e-5 K^-1"
        }
      },
      "description": "Root-mean-square deviations of volume ratio and thermal expansion coefficient for four minerals under three models, to be compared against the paper's Table 6."
    }
  ],
  "notes": "The experimental data and model parameters are assembled by the agent. The hidden checker compares the reported RMSD values to the reference from the paper within a tolerance."
}
```

## How you are scored
A hidden verifier will read your rmsd_table.csv and compare each of the 24 RMSD values to a reference derived from the paper's reported results, using a predefined tolerance. The reward is computed as a weighted sum of agreement across all 24 entries, ranging from 0 (no match) to 1 (fully consistent). The verifier does not disclose the tolerance or reference values. This is a reproduction task, so the expected values are those obtained by a correct implementation of the models; simply reporting numbers without actual computation will not yield a high score because the reference is hidden and the tolerance is strict enough to require genuine computation.
