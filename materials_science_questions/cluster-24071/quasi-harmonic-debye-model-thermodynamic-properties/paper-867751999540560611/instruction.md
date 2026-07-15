# Thermodynamic properties of bcc W from a thermal-vacancy Gibbs energy model

## Problem background
Pure metals such as body-centered cubic (bcc) tungsten (W) exhibit a strong nonlinear increase in isobaric heat capacity near their melting point. This departure from simple harmonic and electronic predictions is attributed to thermal vacancies — point defects that become increasingly abundant at high temperatures. In bcc tungsten, the vacancy concentration can reach a few percent at the melting temperature, and its temperature dependence shows curvature in an Arrhenius plot. A thermodynamically consistent model that couples the defect-free host lattice with a thermal vacancy sublattice and a temperature‑dependent interaction parameter is a candidate for quantitatively describing these effects. The target of this task is to compute the heat capacity, heat content, and equilibrium vacancy concentration of bcc tungsten using such a model and a given set of numerical parameters.

## Approach
The total molar Gibbs energy is constructed from contributions of the defect‑free tungsten lattice, a virtual vacancy lattice, an ideal mixing term, and a temperature‑dependent interaction parameter Ω. The equilibrium vacancy concentration is obtained by minimizing the Gibbs energy, which leads to an implicit equation for the vacancy fraction. The interaction parameter is expressed as a quadratic polynomial in temperature, Ω = A + B T + C T², thereby allowing a nonlinear temperature dependence of the effective vacancy formation energy and producing curvature in the log yᵥₐ vs. 1/T plot. The defect‑free isobaric heat capacity is modeled by an Einstein harmonic term (characterized by an Einstein temperature) plus a T + b T² corrections that account for electronic and anharmonic contributions. The total isobaric heat capacity Cₚ then includes additional terms from the temperature derivatives of Ω and the vacancy concentration. The heat content relative to 298.15 K is obtained by integrating Cₚ. The numerical values of all parameters for bcc tungsten are specified in the workflow steps below. The overall temperature grid spans 0 to 3800 K with a step of approximately 1 K.

## Reproduction target
Implement the above Gibbs energy model for bcc tungsten using the parameters listed in the workflow steps. Evaluate the model on a temperature grid from 0 to 3800 K (step ≈ 1 K) and produce the following three curves:

1. Isobaric heat capacity Cₚ (J mol⁻¹ K⁻¹) as a function of temperature.
2. Heat content relative to 298.15 K, H(T) – H(298.15 K) (J mol⁻¹), as a function of temperature.
3. Equilibrium thermal vacancy concentration yᵥₐ (dimensionless) as a function of temperature.

Write each curve to a separate CSV file as detailed in the workflow steps. The three curves will be compared against reference results derived from the same model and parameters; the goal is to compute these quantities accurately over the full temperature range.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute heat capacity of bcc W
- Role: scored (load-bearing)
- Action: Implement the thermodynamic model for bcc W based on a Gibbs energy expression that includes a temperature-dependent vacancy interaction parameter. Use the parameter values: E0 = -1228665.43 J/mol, theta_E = 269.2 K, a = -1.085e-3, b = -1.1835e-7, and interaction parameter Omega = 229615.89 + 12.73 T - 1.1274e-2 T^2 (T in Kelvin). The vacancy Gibbs energy is set to 0.2 R T. For each temperature T from 0 to 3800 K in steps of approximately 1 K, solve for the equilibrium vacancy concentration y_va using a root-finding method applied to the equilibrium condition derived from the Gibbs energy. Compute the total isobaric heat capacity Cp as the sum of the defect-free heat capacity (an Einstein term 3R*(theta_E/T)^2*exp(theta_E/T)/(exp(theta_E/T)-1)^2 plus a T + b T^2) and the vacancy contributions. Output a CSV file with two columns: T (K) and Cp (J/mol-K).
- Output file: `/app/outputs/heat_capacity.csv`
- Format: csv
- Contract: Two columns: 'T' (float, unit: K) and 'Cp' (float, unit: J/mol-K).
- Scoring: scored by hidden verifier

### Step 2: Compute heat content of bcc W
- Role: scored
- Action: Using the same model and the same temperature grid (0–3800 K), compute the heat content H(T) – H(298.15 K). Integrate the total heat capacity Cp obtained in the previous step from 298.15 K to each temperature T. For T < 298.15 K the result will be negative; integrate consistently. Output a CSV file with two columns: T (K) and H_minus_H298 (J/mol).
- Output file: `/app/outputs/heat_content.csv`
- Format: csv
- Contract: Two columns: 'T' (float, unit: K) and 'H_minus_H298' (float, unit: J/mol).
- Scoring: scored by hidden verifier

### Step 3: Compute thermal vacancy concentration of bcc W
- Role: scored
- Action: Output the equilibrium vacancy concentration y_va (dimensionless) obtained from the same model at the same temperature grid (0–3800 K). This is the y_va solved during the heat capacity computation; write it to a CSV file with two columns: T (K) and y_va (dimensionless).
- Output file: `/app/outputs/vacancy_concentration.csv`
- Format: csv
- Contract: Two columns: 'T' (float, unit: K) and 'y_va' (float, dimensionless, expected range 0 to ~0.03).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heat_capacity.csv`
- `/app/outputs/heat_content.csv`
- `/app/outputs/vacancy_concentration.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heat_capacity.csv
- path: `/app/outputs/heat_capacity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Isobaric heat capacity of bcc W including vacancy effects as a function of temperature. Compared against paper-derived reference values at selected temperatures with an appropriate tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Cp`
  - `units`:
    - `T`: K
    - `Cp`: J/mol-K

### heat_content.csv
- path: `/app/outputs/heat_content.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Heat content (enthalpy increment) of bcc W relative to 298.15 K. Checked by comparing values at hidden temperatures against reference data.
- schema:
  - `type`: table
  - `required_columns`: `T`, `H_minus_H298`
  - `units`:
    - `T`: K
    - `H_minus_H298`: J/mol

### vacancy_concentration.csv
- path: `/app/outputs/vacancy_concentration.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium thermal vacancy concentration in bcc W, computed from the model. Verified against paper-derived values at selected temperatures.
- schema:
  - `type`: table
  - `required_columns`: `T`, `y_va`
  - `units`:
    - `T`: K
    - `y_va`: dimensionless

Notes: All three artifacts are produced by the same underlying model evaluation. The hidden checker extracts values at a small set of temperatures and compares them to pre-computed reference values from the paper's own model; tolerances account for numerical differences in root-finding and integration.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heat_capacity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Cp"
        ],
        "units": {
          "T": "K",
          "Cp": "J/mol-K"
        }
      },
      "description": "Isobaric heat capacity of bcc W including vacancy effects as a function of temperature. Compared against paper-derived reference values at selected temperatures with an appropriate tolerance."
    },
    {
      "file": "heat_content.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "H_minus_H298"
        ],
        "units": {
          "T": "K",
          "H_minus_H298": "J/mol"
        }
      },
      "description": "Heat content (enthalpy increment) of bcc W relative to 298.15 K. Checked by comparing values at hidden temperatures against reference data."
    },
    {
      "file": "vacancy_concentration.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "y_va"
        ],
        "units": {
          "T": "K",
          "y_va": "dimensionless"
        }
      },
      "description": "Equilibrium thermal vacancy concentration in bcc W, computed from the model. Verified against paper-derived values at selected temperatures."
    }
  ],
  "notes": "All three artifacts are produced by the same underlying model evaluation. The hidden checker extracts values at a small set of temperatures and compares them to pre-computed reference values from the paper's own model; tolerances account for numerical differences in root-finding and integration."
}
```

## How you are scored
A hidden verifier will independently examine each of the three output CSV files. For each scored output, the verifier extracts values at a set of undisclosed temperatures and compares them to pre‑computed reference values obtained from the model with the given parameters. The comparisons use appropriate numerical tolerances (relative or absolute, depending on the quantity). The three stages are weighted and combined into a final reward in the range [0, 1]. In addition to pointwise comparisons, the verifier may check structural properties, such as the monotonic increase of Cₚ and H – H298 with temperature and the curvature in the Arrhenius plot of log yᵥₐ vs. 1/T. The task is to perform the honest computation described in the steps; reporting correct numbers that match the model's output is required to obtain a high score.
