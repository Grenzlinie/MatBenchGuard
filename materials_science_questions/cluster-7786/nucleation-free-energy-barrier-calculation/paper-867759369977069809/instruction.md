# Helium-4 glass transition and residual entropy from nucleation model

## Problem background
Liquid helium-4 confined in nanoporous media under pressure can form an ultra-stable glass phase, exhibiting a latent heat and a reduced glass transition temperature. A thermodynamic model that extends classical nucleation theory with a universal enthalpy saving coefficient predicts the frozen enthalpy fraction (H2/ΔHm), the endothermic latent heat fraction (H1/ΔHm), the reduced glass transition temperature (θ_g2), and the residual entropy of the glass. The model's predictions are compared with experimental specific-heat measurements to test its validity.

## Approach
The model describes the enthalpy saving coefficients for liquid–solid and glass–solid transformations as functions of reduced temperature θ, using universal parameters ε_ls0 = ε_gs0 = 0.217, θ_0m = -2/3, θ_0g = -1, and an enthalpy excess coefficient Δε = 0.105. Solving a quadratic equation derived from these coefficients yields the reduced glass transition temperature θ_g2. The predicted frozen enthalpy fraction is given by Δε, and the endothermic latent heat fraction is obtained from the enthalpy expressions at θ_g2. Using the experimental data from Yamamoto et al. for the pressure of 3.58 MPa (provided as constants: T_m, ΔS_m, S_m, γ, T_K, T_geff), the residual entropy of the glass S_Rg is computed from the predicted H1/ΔHm and H2/ΔHm, and its fraction S_Rg/S_m is compared to the expected value.

## Reproduction target
Implement the model in Python. Write two JSON output files under /app/outputs: 

(1) model_predictions.json containing the computed reduced glass transition temperature θ_g2, the predicted frozen enthalpy fraction H2/ΔHm, the predicted endothermic latent heat fraction H1/ΔHm, the supplied experimental mean fractions (H2/ΔHm = 0.11, H1/ΔHm = 0.0932), and a statement (a string) indicating whether the predictions agree with these experimental means. 

(2) residual_entropy.json containing the calculated glass residual entropy S_Rg (in J·K⁻¹·mol⁻¹), the melting entropy S_m (in J·K⁻¹·mol⁻¹), and their ratio S_Rg/S_m (dimensionless). 

The target is to produce both files with the necessary numeric values derived from the model equations and the given experimental constants.

## Assets

- Python scientific stack (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Model predictions: glass transition temperature and enthalpy fractions
- Role: scored (load-bearing)
- Action: Implement the glass transition model equations with the given universal parameters (ε_ls0 = ε_gs0 = 0.217, θ_0m = -2/3, θ_0g = -1, Δε = 0.105). Solve the quadratic for the reduced glass transition temperature θ_g2. Compute the predicted frozen enthalpy fraction H2/ΔHm and the endothermic latent heat fraction H1/ΔHm at θ_g2. Also include the experimental mean values of H2/ΔHm = 0.11 and H1/ΔHm = 0.0932 (supplied as inputs) and state whether the predictions agree with these means.
- Output file: `/app/outputs/model_predictions.json`
- Format: json
- Contract: {"theta_g2": number, "H2_over_dHm_predicted": number, "H1_over_dHm_predicted": number, "experimental_mean_H2_over_dHm": number, "experimental_mean_H1_over_dHm": number, "agreement_statement": "string"}
- Scoring: scored by hidden verifier

### Step 2: Glass residual entropy fraction
- Role: scored
- Action: Using the given experimental data for pressure 3.58 MPa (T_m = 1.937 K, ΔS_m = 2.75 J·K⁻¹·mol⁻¹, S_m = 4.72 J·K⁻¹·mol⁻¹, γ = 2.13 J·K⁻²·mol⁻¹, T_K = 0.497 K, T_geff = 1.164 K) and the predicted H1/ΔHm and H2/ΔHm from step_01, compute the glass residual entropy S_Rg via the formula S_Rg = (H1/ΔHm + H2/ΔHm) × ΔHm / T_geff where ΔHm = ΔS_m × T_m. Then calculate the residual entropy fraction S_Rg / S_m.
- Output file: `/app/outputs/residual_entropy.json`
- Format: json
- Contract: {"S_Rg": number, "S_m": number, "S_Rg_over_S_m": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model_predictions.json`
- `/app/outputs/residual_entropy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model_predictions.json
- path: `/app/outputs/model_predictions.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Predicted model quantities (θ_g2, frozen enthalpy fraction, endothermic latent heat fraction), the supplied experimental mean fractions, and an agreement statement.
- schema:
  - `type`: object
  - `required`:
    - `theta_g2`: number
    - `H2_over_dHm_predicted`: number
    - `H1_over_dHm_predicted`: number
    - `experimental_mean_H2_over_dHm`: number
    - `experimental_mean_H1_over_dHm`: number
    - `agreement_statement`: string
  - `items`: object
  - `units`:
    - `theta_g2`: dimensionless
    - `H2_over_dHm_predicted`: dimensionless
    - `H1_over_dHm_predicted`: dimensionless
    - `experimental_mean_H2_over_dHm`: dimensionless
    - `experimental_mean_H1_over_dHm`: dimensionless
    - `agreement_statement`: text

### residual_entropy.json
- path: `/app/outputs/residual_entropy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed glass residual entropy S_Rg, melting entropy S_m, and their ratio, compared to the paper's hidden reference value (23.6%).
- schema:
  - `type`: object
  - `required`:
    - `S_Rg`: number
    - `S_m`: number
    - `S_Rg_over_S_m`: number
  - `items`: object
  - `units`:
    - `S_Rg`: J.K⁻¹.mol⁻¹
    - `S_m`: J.K⁻¹.mol⁻¹
    - `S_Rg_over_S_m`: dimensionless

Notes: The experimental constants needed for step_02 are fully provided in the step's action; no external datasets need to be fetched. The predicted quantities from step_01 must be used consistently in step_02.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model_predictions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "theta_g2": "number",
          "H2_over_dHm_predicted": "number",
          "H1_over_dHm_predicted": "number",
          "experimental_mean_H2_over_dHm": "number",
          "experimental_mean_H1_over_dHm": "number",
          "agreement_statement": "string"
        },
        "items": {},
        "units": {
          "theta_g2": "dimensionless",
          "H2_over_dHm_predicted": "dimensionless",
          "H1_over_dHm_predicted": "dimensionless",
          "experimental_mean_H2_over_dHm": "dimensionless",
          "experimental_mean_H1_over_dHm": "dimensionless",
          "agreement_statement": "text"
        }
      },
      "description": "Predicted model quantities (θ_g2, frozen enthalpy fraction, endothermic latent heat fraction), the supplied experimental mean fractions, and an agreement statement."
    },
    {
      "file": "residual_entropy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "S_Rg": "number",
          "S_m": "number",
          "S_Rg_over_S_m": "number"
        },
        "items": {},
        "units": {
          "S_Rg": "J.K⁻¹.mol⁻¹",
          "S_m": "J.K⁻¹.mol⁻¹",
          "S_Rg_over_S_m": "dimensionless"
        }
      },
      "description": "Computed glass residual entropy S_Rg, melting entropy S_m, and their ratio, compared to the paper's hidden reference value (23.6%)."
    }
  ],
  "notes": "The experimental constants needed for step_02 are fully provided in the step's action; no external datasets need to be fetched. The predicted quantities from step_01 must be used consistently in step_02."
}
```

## How you are scored
A hidden verifier reads your output files independently. For model_predictions.json, it compares the reported predicted values (θ_g2, H2/ΔHm, H1/ΔHm) to the correct model-predicted values with a relative tolerance. It also checks that the experimental means are correctly recorded and that the agreement statement is present. For residual_entropy.json, it compares the computed S_Rg/S_m to the expected value. The verifier may also perform a consistency check to ensure θ_g2 satisfies the quadratic equation. Each artifact receives a weighted score, and the total reward is the sum of these scores. Reporting the paper's numbers without correct computation will not pass the tolerance checks.
