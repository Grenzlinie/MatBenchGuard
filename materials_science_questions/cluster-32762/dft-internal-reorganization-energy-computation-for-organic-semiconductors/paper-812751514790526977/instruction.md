# Solvent Reorganization Energy Calculation Using Marcus/Pekar Model

## Problem background
In the field of electron transfer, the reorganization free energy is a key quantity that determines the barrier for charge transfer. For a binuclear mixed-valence complex such as [(NH3)5RuIII–NC–RuII(CN)5]–, the metal-to-metal charge transfer (MMCT) absorption band provides a direct spectroscopic handle on the total reorganization free energy when combined with electrochemical data. The total reorganization free energy is the sum of an intramolecular contribution (λ_in) and a solvent (outer‑sphere) contribution (λ_out). The classical Marcus/Pekar theory predicts the solvent reorganization free energy from the dielectric properties of the medium through the Pekar factor γ = 1/n² − 1/D_s, where n is the refractive index and D_s is the static dielectric constant. By calibrating an energetic factor A using a reference medium (water), the theoretical solvent reorganization free energy (λ_out)_calc = A·γ can be compared with the experimentally extracted value (λ_out)_exp = λ_exp − λ_in. The goal of this task is to compute these quantities for a series of water–methanol, water–glycerol, and LiNO₃ electrolyte solutions and to assess the agreement and trends between the calculated and experimental solvent reorganization energies.

## Approach
The approach implements the Marcus/Pekar formalism to obtain the solvent reorganization free energy. Starting from the provided experimental data (MMCT band maximum E_op, free energy change ΔG°′, refractive index n, static dielectric constant D_s, and the constants δ and λ_in), the following computational procedure is carried out:
1. Compute the total experimental reorganization free energy λ_exp = E_op − δ − ΔG°′ (all quantities in kJ mol⁻¹).
2. For each medium, compute the Pekar factor γ = 1/n² − 1/D_s.
3. Identify the water reference entry and determine the energetic factor A as A = (λ_exp(water) − λ_in) / γ(water).
4. For every medium, calculate the theoretical solvent reorganization free energy (λ_out)_calc = A·γ and the experimental solvent reorganization free energy (λ_out)_exp = λ_exp − λ_in.
The resulting table of values allows a direct comparison of the theoretically predicted solvent reorganization energy with the one deduced from experiment across different solution compositions.

## Reproduction target
Compute a CSV file named reorganization_table.csv with the following columns: medium (string), gamma (float, dimensionless), lambda_exp (float, kJ mol⁻¹), lambda_out_calc (float, kJ mol⁻¹), lambda_out_exp (float, kJ mol⁻¹). Each row corresponds to one medium from the input data. All values must be derived from the provided input file using strictly the formulas described above; no external hardcoded numbers are allowed. The verifier will recompute these quantities independently and check them.

## Assets

- Tabulated experimental and dielectric data
- pandas: pandas
- numpy: numpy

## Workflow steps

### Step 1: Assemble input data
- Role: process
- Action: Read the bundled input CSV containing experimental and dielectric data for each medium. Handle unit conversions where necessary (e.g., convert δ from cm⁻¹ to kJ mol⁻¹). Prepare a structured dataset with all required columns.
- Evidence: `/app/outputs/assembled_data.csv`

### Step 2: Compute reorganization table
- Role: scored (load-bearing)
- Action: For each medium, compute λ_exp = E_op - δ - ΔG°′ (in kJ mol⁻¹). Compute the Pekar factor γ = 1/n² − 1/D_s. Identify the water reference entry and determine the energetic factor A = (λ_exp(water) − λ_in) / γ(water). Then compute the theoretical solvent reorganization energy (λ_out)_calc = A × γ and the experimental solvent reorganization energy (λ_out)_exp = λ_exp − λ_in for every medium. Write the results to reorganization_table.csv with the required columns.
- Output file: `/app/outputs/reorganization_table.csv`
- Format: csv
- Contract: Columns: medium (string), gamma (float, dimensionless), lambda_exp (float, kJ mol⁻¹), lambda_out_calc (float, kJ mol⁻¹), lambda_out_exp (float, kJ mol⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reorganization_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reorganization_table.csv
- path: `/app/outputs/reorganization_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed solvent reorganization energies and Pekar factors for all media, compared to hidden reference values derived from the same publicly reconstructible procedure.
- schema:
  - `type`: table
  - `required_columns`: `medium`, `gamma`, `lambda_exp`, `lambda_out_calc`, `lambda_out_exp`
  - `units`:
    - `gamma`: dimensionless
    - `lambda_exp`: kJ mol⁻¹
    - `lambda_out_calc`: kJ mol⁻¹
    - `lambda_out_exp`: kJ mol⁻¹

Notes: The agent must compute all values from the provided input data; no hardcoded gold values are permitted. The hidden checker will recompute each quantity using the identical formulas and compare with tolerance, also verifying structural trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reorganization_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "medium",
          "gamma",
          "lambda_exp",
          "lambda_out_calc",
          "lambda_out_exp"
        ],
        "units": {
          "gamma": "dimensionless",
          "lambda_exp": "kJ mol⁻¹",
          "lambda_out_calc": "kJ mol⁻¹",
          "lambda_out_exp": "kJ mol⁻¹"
        }
      },
      "description": "Computed solvent reorganization energies and Pekar factors for all media, compared to hidden reference values derived from the same publicly reconstructible procedure."
    }
  ],
  "notes": "The agent must compute all values from the provided input data; no hardcoded gold values are permitted. The hidden checker will recompute each quantity using the identical formulas and compare with tolerance, also verifying structural trends."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads your output CSV file. The verifier recomputes λ_exp, γ, A, (λ_out)_calc, and (λ_out)_exp from the same input data using the identical formulas. It checks that your reported values are numerically consistent with the recomputed values within a tolerance that accounts for legitimate numerical differences. In addition, the verifier verifies structural trends: for example, in certain media families, specific quantities should exhibit a monotonic increase or decrease with composition; your results must reproduce these expected directional patterns. The final reward is a weighted combination of these checks. Producing a table of numbers without a correctly executed workflow will not satisfy the verifier, as the structural and recomputation tests cannot be passed by simple guesswork.
