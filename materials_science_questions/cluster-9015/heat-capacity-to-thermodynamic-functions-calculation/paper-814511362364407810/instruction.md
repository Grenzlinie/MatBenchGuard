# Compute Thermodynamic Functions from Exponential Heat Capacity Model

## Problem background
Isobaric heat capacity (Cp) as a function of temperature is a fundamental thermodynamic property needed to compute enthalpy, entropy, and Gibbs free energy. Widely used empirical polynomial models approximate Cp over limited temperature ranges but the fitted coefficients lack physical meaning and can diverge when extrapolated to high temperatures (beyond ~1500 K). An alternative model that remains accurate from room temperature up to 6000 K and whose parameters relate to molecular characteristics – such as the number of atoms – would allow more reliable high‑temperature thermochemical calculations without increasing the number of fitted constants. This task re‑creates a three‑parameter exponential Cp expression that aims to meet these requirements for light hydrocarbons and common gases.

## Approach
A three‑parameter exponential model is constructed for the isobaric heat capacity:  Cp(T) = Cp0 + Cp∞ [1 + ln(T) (1 + Ti/T)] exp(–Ti/T).  The parameters Cp0 (low‑temperature limit), Cp∞ (growth rate at high temperature), and Ti (a temperature related to the inflection point of the Cp curve) are the only free parameters.  Fitting is performed indirectly – rather than a direct non‑linear least‑squares fit of Cp, an enthalpy functional form  H*(T) = Cp0 T + Cp∞ T ln(T) exp(–Ti/T)  is fitted to a set of numerically generated H*(T) points.  Those points come from a baseline fit of the Yuan–Mok Cp model (C = A + B exp(–C/T) ) and subsequent numerical integration.  The differentiation of the fitted enthalpy gives the desired Cp(T) expression.  By evaluating the fitted Cp(T) against experimental data, two standard quality metrics are computed: the average absolute deviation (AAD) and the correlation coefficient (R²).  The same three parameters are then used in an approximate entropy expression  S(T) ≈ Cp0 ln(T) + Cp∞ ln(T) [(1 + (5/3)(T/Ti)) / (1 + (2/3)(T/Ti))] exp(–Ti/T) + S0  (without additional fitting), and the entropy predictions are compared with experimental entropy values.  Finally, for the linear alkanes, linear regressions of the fitted Cp0, Cp∞, and Ti against the number of atoms per molecule are performed to examine whether the parameters capture simple structural trends.

## Reproduction target
For the following compounds – methane, ethane, propane, butane, pentane, hexane, heptane, O2, H2O, H2, CO2, CO, N2, and C2H4 – collect experimental Cp and entropy data from the designated public sources.  Fit the three‑parameter exponential Cp model through the enthalpy‑fitting route, and for each compound report the fitted parameters (Cp0, Cp∞, Ti), the AAD (%), and R² for the Cp predictions.  Using the same parameters, evaluate the approximate entropy model and report the AAD (%) and R² for the entropy comparison.  For the linear hydrocarbons C2–C7, perform linear regressions of Cp0, Cp∞, and Ti against the number of atoms nA, and output the slope, intercept, and R² of each regression.  Also note whether the fitted Cp0 for the diatomic gases (O2, N2, CO, H2) is close to the ideal‑diatomic value 7R/2 (this is a check, not a separate scored artifact).  All numerical results must be written to the specified CSV files with the columns described in the workflow steps.

## Assets

- NASA SP-3001 Thermodynamic properties to 6000 K: https://ntrs.nasa.gov/citations/19630009382
- US Bureau of Mines Bulletin 666 (Scott): https://digital.library.unt.edu/ark:/67531/metadc12825/
- SciPy: scipy
- NumPy: numpy
- pandas: pandas

## Workflow steps

### Step 1: Collect and parse experimental data
- Role: process
- Action: Retrieve experimental Cp and entropy data for target compounds (C1-C7 linear hydrocarbons, O2, H2O, H2, CO2, CO, N2, C2H4) from NASA SP-3001 and US Bureau of Mines Bulletin 666. Parse tabulated data into structured arrays.
- Evidence: `/app/outputs/data_summary.txt`

### Step 2: Fit Yuan-Mok Cp model and generate H* reference
- Role: process
- Action: Implement the Yuan-Mok exponential Cp expression (Eq. 1 with n=1) and fit it to each compound's Cp data using nonlinear least squares (Marquardt-Levenberg). Numerically integrate the fitted curves over temperature to obtain H*(T) points that serve as the reference for the new model's enthalpy fit.
- Evidence: `/app/outputs/yuan_mok_params.csv`

### Step 3: Fit new three-parameter model and evaluate Cp accuracy
- Role: scored (load-bearing)
- Action: Fit the enthalpy functional form H*(T)=a T + b T ln(T) exp(-Ti/T) to the H*(T) data for each compound. Relabel a as Cp0 and b as Cp∞. Differentiate to obtain the Cp(T) model. Compute predicted Cp values for the experimental temperature points, calculate the average absolute deviation (AAD) and correlation coefficient (R²). Write the fitted parameters (Cp0, Cp∞, Ti), AAD_Cp, and R² for every compound to fitted_parameters.csv.
- Output file: `/app/outputs/fitted_parameters.csv`
- Format: csv
- Contract: gas_name (string), n_A (int), Cp0 (float, J mol^{-1} K^{-1}), Cp_inf (float, J mol^{-1} K^{-1}), Ti (float, K), AAD_Cp (float, %), R2_Cp (float)
- Scoring: scored by hidden verifier

### Step 4: Compute and evaluate entropy approximation
- Role: scored
- Action: Using the fitted parameters (Cp0, Cp∞, Ti), compute the approximate entropy S(T) via the base expression (without fitted ε). Compare the predicted entropy values to the experimental entropy data for each compound and compute AAD_S and R²_S. Write the results to entropy_results.csv.
- Output file: `/app/outputs/entropy_results.csv`
- Format: csv
- Contract: gas_name (string), n_A (int), AAD_S (float, %), R2_S (float)
- Scoring: scored by hidden verifier

### Step 5: Analyze parameter correlations with atom count
- Role: scored
- Action: For linear hydrocarbons C2-C7, perform linear regressions of the fitted parameters Cp0, Cp∞, and Ti against the number of atoms n_A. Report the slope, intercept, and R² of each regression.  Write the regression results to linear_trends.csv.
- Output file: `/app/outputs/linear_trends.csv`
- Format: csv
- Contract: parameter (string), slope (float), intercept (float), R2 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.csv`
- `/app/outputs/entropy_results.csv`
- `/app/outputs/linear_trends.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.csv
- path: `/app/outputs/fitted_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fitted parameters of the three-parameter exponential Cp model (Cp0, Cp∞, Ti) and the associated fitting quality metrics (AAD, R²) for each compound.
- schema:
  - `type`: table
  - `required_columns`: `gas_name`, `n_A`, `Cp0`, `Cp_inf`, `Ti`, `AAD_Cp`, `R2_Cp`
  - `units`:
    - `Cp0`: J mol^{-1} K^{-1}
    - `Cp_inf`: J mol^{-1} K^{-1}
    - `Ti`: K
    - `AAD_Cp`: %
    - `R2_Cp`: dimensionless

### entropy_results.csv
- path: `/app/outputs/entropy_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Evaluation of the approximate entropy expression derived from the Cp model parameters: AAD and R² per compound compared to experimental entropy.
- schema:
  - `type`: table
  - `required_columns`: `gas_name`, `n_A`, `AAD_S`, `R2_S`
  - `units`:
    - `AAD_S`: %
    - `R2_S`: dimensionless

### linear_trends.csv
- path: `/app/outputs/linear_trends.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Linear regression results of fitted parameters (Cp0, Cp∞, Ti) versus number of atoms for linear hydrocarbons C2-C7.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `slope`, `intercept`, `R2`
  - `units`:
    - `slope`: depends on parameter
    - `intercept`: depends on parameter
    - `R2`: dimensionless

Notes: All hidden comparison thresholds, tolerances, and reference values are omitted; the checker uses the paper's reported quantities (SI Tables 2, 3, Fig. 5) with appropriate tolerances as described in the verification plan.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "gas_name",
          "n_A",
          "Cp0",
          "Cp_inf",
          "Ti",
          "AAD_Cp",
          "R2_Cp"
        ],
        "units": {
          "Cp0": "J mol^{-1} K^{-1}",
          "Cp_inf": "J mol^{-1} K^{-1}",
          "Ti": "K",
          "AAD_Cp": "%",
          "R2_Cp": "dimensionless"
        }
      },
      "description": "Fitted parameters of the three-parameter exponential Cp model (Cp0, Cp∞, Ti) and the associated fitting quality metrics (AAD, R²) for each compound."
    },
    {
      "file": "entropy_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "gas_name",
          "n_A",
          "AAD_S",
          "R2_S"
        ],
        "units": {
          "AAD_S": "%",
          "R2_S": "dimensionless"
        }
      },
      "description": "Evaluation of the approximate entropy expression derived from the Cp model parameters: AAD and R² per compound compared to experimental entropy."
    },
    {
      "file": "linear_trends.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "slope",
          "intercept",
          "R2"
        ],
        "units": {
          "slope": "depends on parameter",
          "intercept": "depends on parameter",
          "R2": "dimensionless"
        }
      },
      "description": "Linear regression results of fitted parameters (Cp0, Cp∞, Ti) versus number of atoms for linear hydrocarbons C2-C7."
    }
  ],
  "notes": "All hidden comparison thresholds, tolerances, and reference values are omitted; the checker uses the paper's reported quantities (SI Tables 2, 3, Fig. 5) with appropriate tolerances as described in the verification plan."
}
```

## How you are scored
A hidden verifier independently evaluates the three required output files – fitted_parameters.csv, entropy_results.csv, and linear_trends.csv.  For each file, the verifier compares your computed values (fitted parameters, AAD, R², regression slopes/intercepts) against reference quantities that are derived from the original study's reported results.  The comparison uses pre‑defined tolerances appropriate for each metric; better‑than‑reference performance (lower AAD, higher R², etc.) is never penalised.  Each of the three artifacts carries a weight; the final reward is the weighted sum of per‑artifact scores, ranging from 0 to 1.  Simply reporting numbers that happen to match the reference without a correct computational pipeline is not sufficient – the verifier may also check internal consistency of the submitted results.  The verifier does not reveal the reference values or tolerances; it only outputs the combined reward.
