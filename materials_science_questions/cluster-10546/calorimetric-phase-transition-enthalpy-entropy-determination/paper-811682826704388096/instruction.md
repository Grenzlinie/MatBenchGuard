# BeO Thermodynamic Correlation: Extracting γ⁻ and Computing Volume Compressibility β(T)

## Problem background
Beryllium oxide undergoes a first-order polymorphic transition from its low-temperature hexagonal wurtzite structure to a high-temperature tetragonal rutile structure at a transition temperature near 2100 K. A thermodynamic analysis of this transition predicts a linear relationship between the volumetric thermal expansion coefficient α and the reduced isobaric heat capacity C_p/T in the low-temperature region of the transition. The slope of this relationship is directly connected to the pressure derivative of the transition temperature, γ⁻ = dT_λ⁻/dp. Once γ⁻ is known, the isothermal volume compressibility β can be computed as a function of temperature. This task determines γ⁻ and the temperature-dependent β(T) from published experimental α and C_p/T data.

## Approach
The workflow uses publicly reported experimental α(T) and C_p(T) values for BeO in the temperature range 40–720 K. For every temperature where both α and C_p are available, the reduced heat capacity C_p/T is computed and paired with α. A linear regression of α against C_p/T is performed to extract the slope. The derived quantity γ⁻ is then obtained by multiplying the slope by the standard molar volume V₀ = 8.25×10⁻³ m³/mol. Finally, the volume compressibility β is calculated at each temperature using the relation β = (γ⁻)² / V₀ × (C_p/T). All steps are purely computational; the required input data are extracted from the cited literature.

## Reproduction target
Determine the pressure derivative of the wurtzite–rutile transition temperature, γ⁻, by performing a linear fit of α versus C_p/T on the compiled experimental BeO data. Then compute the isothermal volume compressibility β as a function of temperature using the derived γ⁻ and the C_p/T data.

## Assets

- Isobaric heat capacity data for BeO from Victor & Douglas 1963: 10.6028/jres.067A.032
- Thermophysical properties of BeO from Krzhizhanovskii & Shtern 1973
- Volumetric thermal expansion coefficient α data for BeO from Sirota et al. 1987: 10.1016/0038-1098(87)90818-0
- Standard molar volume V₀ of BeO from Samsonov 1978

## Workflow steps

### Step 1: Compile experimental α and C_p/T data for BeO
- Role: scored
- Action: From the cited literature (Victor & Douglas 1963, Krzhizhanovskii & Shtern 1973, Sirota et al. 1987), collect paired values of temperature (K), volumetric thermal expansion coefficient α (in units of 10⁻⁶ K⁻¹) and isobaric heat capacity C_p (J mol⁻¹ K⁻¹) for BeO in the range 40–720 K. For each temperature where both α and C_p are available, compute C_p/T and record one row. Output a CSV file with columns temperature_K, alpha_ppm_per_K, Cp_over_T_J_per_mol_K2.
- Output file: `/app/outputs/step_01_alpha_cp_data.csv`
- Format: csv
- Contract: Columns: temperature_K (float), alpha_ppm_per_K (float, α×10⁶), Cp_over_T_J_per_mol_K2 (float, C_p/T). Each row is one temperature with both α and C_p/T available.
- Scoring: scored by hidden verifier

### Step 2: Perform linear fit of α vs C_p/T and extract γ⁻
- Role: scored (load-bearing)
- Action: From step_01_alpha_cp_data.csv, perform a linear regression of alpha_ppm_per_K vs Cp_over_T_J_per_mol_K2. Extract the raw slope (in units consistent with the input columns). Compute γ⁻ (K/MPa) as γ⁻ = slope × V₀, where V₀ = 8.25×10⁻³ m³/mol. Also compute the coefficient of determination R². Write a JSON file with keys slope, gamma_minus, r_squared.
- Output file: `/app/outputs/step_02_fit_results.json`
- Format: json
- Contract: JSON object with keys: slope (float, raw regression coefficient), gamma_minus (float, K/MPa), r_squared (float).
- Scoring: scored by hidden verifier

### Step 3: Compute temperature-dependent volume compressibility β
- Role: scored
- Action: Using γ⁻ from step_02_fit_results.json and the C_p/T column from step_01_alpha_cp_data.csv, compute β = (γ⁻)² / V₀ × (C_p/T) at each temperature. Output a CSV with columns temperature_K and beta_GPa_minus_one (β in GPa⁻¹, where β = (γ⁻)² / (8.25e-3 m³/mol) × (C_p/T) with γ⁻ in K/MPa and C_p/T in J mol⁻¹ K⁻²).
- Output file: `/app/outputs/step_03_beta_vs_t.csv`
- Format: csv
- Contract: Columns: temperature_K (float), beta_GPa_minus_one (float, β in GPa⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_alpha_cp_data.csv`
- `/app/outputs/step_02_fit_results.json`
- `/app/outputs/step_03_beta_vs_t.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_alpha_cp_data.csv
- path: `/app/outputs/step_01_alpha_cp_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Curated paired experimental α and C_p/T data; the checker will verify its structure and use it to recompute the slope.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `alpha_ppm_per_K`, `Cp_over_T_J_per_mol_K2`
  - `units`:
    - `temperature_K`: K
    - `alpha_ppm_per_K`: 10⁻⁶ K⁻¹
    - `Cp_over_T_J_per_mol_K2`: J mol⁻¹ K⁻²

### step_02_fit_results.json
- path: `/app/outputs/step_02_fit_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted slope, derived γ⁻, and R². The checker compares γ⁻ against the paper's hidden reference.
- schema:
  - `type`: object
  - `required`:
    - `slope`: float
    - `gamma_minus`: float
    - `r_squared`: float
  - `units`:
    - `gamma_minus`: K/MPa

### step_03_beta_vs_t.csv
- path: `/app/outputs/step_03_beta_vs_t.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed isothermal volume compressibility β(T). The checker recomputes β from the agent's own γ⁻ and C_p data to verify self-consistency.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `beta_GPa_minus_one`
  - `units`:
    - `temperature_K`: K
    - `beta_GPa_minus_one`: GPa⁻¹

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_alpha_cp_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "alpha_ppm_per_K",
          "Cp_over_T_J_per_mol_K2"
        ],
        "units": {
          "temperature_K": "K",
          "alpha_ppm_per_K": "10⁻⁶ K⁻¹",
          "Cp_over_T_J_per_mol_K2": "J mol⁻¹ K⁻²"
        }
      },
      "description": "Curated paired experimental α and C_p/T data; the checker will verify its structure and use it to recompute the slope."
    },
    {
      "file": "step_02_fit_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "slope": "float",
          "gamma_minus": "float",
          "r_squared": "float"
        },
        "units": {
          "gamma_minus": "K/MPa"
        }
      },
      "description": "Fitted slope, derived γ⁻, and R². The checker compares γ⁻ against the paper's hidden reference."
    },
    {
      "file": "step_03_beta_vs_t.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "beta_GPa_minus_one"
        ],
        "units": {
          "temperature_K": "K",
          "beta_GPa_minus_one": "GPa⁻¹"
        }
      },
      "description": "Computed isothermal volume compressibility β(T). The checker recomputes β from the agent's own γ⁻ and C_p data to verify self-consistency."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier inspects each output artifact. For the compiled data table, it checks structure and completeness. It re-performs the linear regression on the agent's submitted α and C_p/T values, re-derives γ⁻ from the slope, and compares the result against a hidden reference. It also verifies that the coefficient of determination R² is reported. For the β(T) table, the verifier recomputes β from the agent's own γ⁻ and C_p/T data and checks self-consistency. Each stage contributes a weighted portion of the final score; reporting the final numbers alone is insufficient—the intermediate artifacts and their internal consistency must be correct.
