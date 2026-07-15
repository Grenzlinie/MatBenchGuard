# Enthalpy-Saving Model of Glass Transition: Compute Thermodynamic Parameters and Nucleation Rates

## Problem background
The glass transition lacks a fully accepted thermodynamic origin. This task implements an "enthalpy saving" model in which a crystal nucleus formation Gibbs free energy is supplemented with a temperature-dependent energy saving term. The model requires only the melting temperature, glass transition temperature, fusion enthalpy, and experimental specific heat jump as inputs, and predicts the glass transition, specific heat jump, Kauzmann temperature, equilibrium enthalpy, and stable-glass nucleation rate maximum. Here, you will compute these thermodynamic quantities and nucleation rates for three representative glass-forming melts.

## Approach
The enthalpy saving model provides a set of algebraic relations that connect the measured material properties to derived thermodynamic quantities. The computation proceeds in two stages. First, using scaling laws, you determine the energy saving coefficients ε_ls0, ε_lgs0, their difference Δε_0, the VFT temperatures T_0m and T_0g, the specific heat jump ΔC_p(T_g), and the Kauzmann temperature T_K for each material. Second, using the derived thermodynamic parameters and given kinetic constants (ln K_lg and B/(T_g−T_0g)), you compute the steady-state nucleation rate logarithm ln J_n at the Kauzmann temperature for superclusters containing a specified magic number of atoms. All required material-specific input values (Tm, Tg, ΔHm, ΔC_plg(exp) and kinetic constants) are listed for each material in the workflow steps below.

## Reproduction target
Implement the enthalpy saving model to compute: (1) the energy saving coefficients ε_ls0, ε_lgs0, the difference Δε_0, the VFT temperatures T_0m, T_0g, the specific heat jump ΔC_p(T_g), and the Kauzmann temperature T_K for the three fragile glass-forming melts: Pd43Ni10Cu27P20, indomethacin, and As2Se3; (2) the steady‑state nucleation rate logarithm ln J_n at the Kauzmann temperature T_K for the specified n‑atom superclusters in these three materials. Write the results to /app/outputs/step_01_thermodynamic_params.json and /app/outputs/step_02_nucleation_rates.json.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute thermodynamic parameters
- Role: scored
- Action: Implement the enthalpy saving model for three fragile glass-forming melts (Pd43Ni10Cu27P20, indomethacin, As2Se3) using provided melting temperature Tm, glass transition temperature Tg, fusion enthalpy ΔHm, and experimental specific heat jump ΔC_plg(exp). Use the scaling laws to obtain the energy saving coefficients ε_ls0, ε_lgs0, their difference Δε_0, the VFT temperatures T_0m, T_0g, the specific heat jump ΔC_p(T_g), and the Kauzmann temperature T_K. Write results to /app/outputs/step_01_thermodynamic_params.json.
- Output file: `/app/outputs/step_01_thermodynamic_params.json`
- Format: json
- Contract: {"material_name": {"epsilon_ls0": float, "epsilon_lgs0": float, "delta_epsilon_0": float, "T_0m": float, "T_0g": float, "Delta_Cp_Tg": float, "T_K": float}}
- Scoring: scored by hidden verifier

### Step 2: Compute stable-glass nucleation rates
- Role: scored (load-bearing)
- Action: Using the thermodynamic parameters from step_01 and the model equations for supercluster nucleation (with given kinetic constants ln K_lg and B/(T_g-T_0g) for each material, and physical constants), compute the steady-state nucleation rate logarithm ln J_n at the Kauzmann temperature T_K for the specified n-atom clusters. Write results to /app/outputs/step_02_nucleation_rates.json.
- Output file: `/app/outputs/step_02_nucleation_rates.json`
- Format: json
- Contract: {"material_name": {"ln_J_n_at_TK": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thermodynamic_params.json`
- `/app/outputs/step_02_nucleation_rates.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_thermodynamic_params.json
- path: `/app/outputs/step_01_thermodynamic_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Thermodynamic parameters predicted by the enthalpy saving model for three glass-forming melts.
- schema:
  - `type`: object
  - `required`:
    - `Pd43Ni10Cu27P20`: object with fields epsilon_ls0, epsilon_lgs0, delta_epsilon_0, T_0m, T_0g, Delta_Cp_Tg, T_K (all numeric)
    - `indomethacin`: object (same fields)
    - `As2Se3`: object (same fields)
  - `items`:
    - `epsilon_ls0`: float
    - `epsilon_lgs0`: float
    - `delta_epsilon_0`: float
    - `T_0m`: float (K)
    - `T_0g`: float (K)
    - `Delta_Cp_Tg`: float (J/mol/K)
    - `T_K`: float (K)

### step_02_nucleation_rates.json
- path: `/app/outputs/step_02_nucleation_rates.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Steady-state nucleation rate logarithm at the Kauzmann temperature.
- schema:
  - `type`: object
  - `required`:
    - `Pd43Ni10Cu27P20`: object with field ln_J_n_at_TK
    - `indomethacin`: object (same field)
    - `As2Se3`: object (same field)
  - `items`:
    - `ln_J_n_at_TK`: float (natural log)

Notes: The hidden checker compares submitted values to the paper-reported gold using tolerances. Units are Kelvin for temperatures, J/mol/K for specific heat jump, and dimensionless for logarithms.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_thermodynamic_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Pd43Ni10Cu27P20": "object with fields epsilon_ls0, epsilon_lgs0, delta_epsilon_0, T_0m, T_0g, Delta_Cp_Tg, T_K (all numeric)",
          "indomethacin": "object (same fields)",
          "As2Se3": "object (same fields)"
        },
        "items": {
          "epsilon_ls0": "float",
          "epsilon_lgs0": "float",
          "delta_epsilon_0": "float",
          "T_0m": "float (K)",
          "T_0g": "float (K)",
          "Delta_Cp_Tg": "float (J/mol/K)",
          "T_K": "float (K)"
        }
      },
      "description": "Thermodynamic parameters predicted by the enthalpy saving model for three glass-forming melts."
    },
    {
      "file": "step_02_nucleation_rates.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Pd43Ni10Cu27P20": "object with field ln_J_n_at_TK",
          "indomethacin": "object (same field)",
          "As2Se3": "object (same field)"
        },
        "items": {
          "ln_J_n_at_TK": "float (natural log)"
        }
      },
      "description": "Steady-state nucleation rate logarithm at the Kauzmann temperature."
    }
  ],
  "notes": "The hidden checker compares submitted values to the paper-reported gold using tolerances. Units are Kelvin for temperatures, J/mol/K for specific heat jump, and dimensionless for logarithms."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact. The verifier compares your computed values in step_01_thermodynamic_params.json and step_02_nucleation_rates.json to reference values, applying appropriate tolerances. Each stage carries a weight, and the final reward is the weighted sum. You do not need to match specific published numbers exactly; the verifier checks that your calculations are correct within the model's expected precision. Ensure your output files contain exactly the fields required by the output contract, with no extra metadata.
