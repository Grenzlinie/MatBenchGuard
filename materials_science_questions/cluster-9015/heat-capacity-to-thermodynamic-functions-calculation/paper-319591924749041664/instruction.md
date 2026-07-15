# Thermodynamic Functions from Heat Capacity Data

## Problem background
The YVO4–BiVO4 system forms solid solutions that are of interest for their tunable structural, electronic, and thermal properties. Accurate high-temperature isobaric heat capacity (Cp) data provide the basis for deriving fundamental thermodynamic state functions. Among these, the enthalpy increment ΔH = H(T) − H(350 K) and the entropy change ΔS = S(T) − S(350 K) quantify the heat absorbed and the increase in disorder as a material is heated from a reference temperature. In this task you are given smoothed experimental Cp values (in J mol⁻¹ K⁻¹) for two single-phase solid solution compositions, and you must compute ΔH and ΔS over the temperature range 350–1000 K.

## Approach
The enthalpy increment at temperature T is obtained by numerically integrating Cp(T) from 350 K to T:

ΔH(T) = ∫_{350 K}^{T} Cp(T) dT

The entropy change is obtained by integrating Cp(T)/T over the same interval:

ΔS(T) = ∫_{350 K}^{T} (Cp(T)/T) dT

Because the data are given on a uniform 50 K grid, a standard trapezoidal rule can be applied directly. The smoothed molar heat capacity values for the two compositions are provided in the file `/app/data/cp_data.csv`. This file contains three columns: `Composition`, `T (K)`, `Cp (J/(mol·K))`. The compositions are labelled `Y0.4Bi0.6VO4` and `Y0.6Bi0.4VO4`. The temperature points are the same 14 values from 350 K to 1000 K in steps of 50 K for each composition.

Use this file as the sole source of heat capacity data. Convert ΔH to kJ mol⁻¹ (1 kJ = 1000 J) and retain ΔS in J mol⁻¹ K⁻¹. All quantities are molar per formula unit (Z = 4).

## Reproduction target
For each of the two solid solutions (Y0.4Bi0.6VO4 and Y0.6Bi0.4VO4), compute the enthalpy increment ΔH = H(T) − H(350 K) (in kJ mol⁻¹), the entropy change ΔS = S(T) − S(350 K) (in J mol⁻¹ K⁻¹), and the reduced Gibbs free energy function Φ°(T) = ΔS − ΔH/T = −[G°(T)−G°(350 K)]/T (in J mol⁻¹ K⁻¹), at every temperature in the provided grid: 350, 400, 450, ..., 1000 K. Output two CSV files (one per composition) with columns:

- T (K)
- Cp (J/(mol·K))
- delta_H (kJ/mol)
- delta_S (J/(mol·K))
- Phi (J/(mol·K))

Each row corresponds to one temperature point; the 350 K row should contain the Cp value and zero for both delta_H and delta_S. The results must be self-consistent with the integration of the supplied Cp data.

## Assets

- Smoothed heat capacity data and Mayer-Kelly coefficients for Y0.4Bi0.6VO4 and Y0.6Bi0.4VO4
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute thermodynamic functions for Y0.4Bi0.6VO4
- Role: scored (load-bearing)
- Action: Using the provided smoothed isobaric heat capacity data Cp(T) for Y0.4Bi0.6VO4 over the temperature range 350–1000 K, numerically integrate to obtain the enthalpy increment H°(T)-H°(350 K) and entropy change S°(T)-S°(350 K). Compute the reduced Gibbs free energy function Φ°(T) = ΔS − ΔH/T (with ΔH converted to J mol⁻¹) expressed in J mol⁻¹ K⁻¹. Write the results to a CSV file with columns: T (K), Cp (J/(mol·K)), delta_H (kJ/mol), delta_S (J/(mol·K)), Phi (J/(mol·K)). One row per temperature point (350, 400, 450, …, 1000 K). The 350 K row must have delta_H=0, delta_S=0, and Phi=0.
- Output file: `/app/outputs/enthalpy_entropy_Y04Bi06VO4.csv`
- Format: csv
- Contract: CSV with header: T (K), Cp (J/(mol·K)), delta_H (kJ/mol), delta_S (J/(mol·K)), Phi (J/(mol·K)). Each row corresponds to a temperature point from 350 to 1000 K in steps of 50 K.
- Scoring: scored by hidden verifier

### Step 2: Compute thermodynamic functions for Y0.6Bi0.4VO4
- Role: scored
- Action: Using the provided smoothed isobaric heat capacity data Cp(T) for Y0.6Bi0.4VO4 over the temperature range 350–1000 K, numerically integrate to obtain the enthalpy increment H°(T)-H°(350 K) and entropy change S°(T)-S°(350 K). Compute the reduced Gibbs free energy function Φ°(T) = ΔS − ΔH/T (with ΔH converted to J mol⁻¹) expressed in J mol⁻¹ K⁻¹. Write the results to a CSV file with columns: T (K), Cp (J/(mol·K)), delta_H (kJ/mol), delta_S (J/(mol·K)), Phi (J/(mol·K)). One row per temperature point (350, 400, 450, …, 1000 K). The 350 K row must have delta_H=0, delta_S=0, and Phi=0.
- Output file: `/app/outputs/enthalpy_entropy_Y06Bi04VO4.csv`
- Format: csv
- Contract: CSV with header: T (K), Cp (J/(mol·K)), delta_H (kJ/mol), delta_S (J/(mol·K)), Phi (J/(mol·K)). Each row corresponds to a temperature point from 350 to 1000 K in steps of 50 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/enthalpy_entropy_Y04Bi06VO4.csv`
- `/app/outputs/enthalpy_entropy_Y06Bi04VO4.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### enthalpy_entropy_Y04Bi06VO4.csv
- path: `/app/outputs/enthalpy_entropy_Y04Bi06VO4.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Thermodynamic functions for Y0.4Bi0.6VO4: temperature, heat capacity, enthalpy increment, entropy change, and reduced Gibbs free energy function.
- schema:
  - `type`: table
  - `required_columns`: `T (K)`, `Cp (J/(mol·K))`, `delta_H (kJ/mol)`, `delta_S (J/(mol·K))`, `Phi (J/(mol·K))`

### enthalpy_entropy_Y06Bi04VO4.csv
- path: `/app/outputs/enthalpy_entropy_Y06Bi04VO4.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Thermodynamic functions for Y0.6Bi0.4VO4: temperature, heat capacity, enthalpy increment, entropy change, and reduced Gibbs free energy function.
- schema:
  - `type`: table
  - `required_columns`: `T (K)`, `Cp (J/(mol·K))`, `delta_H (kJ/mol)`, `delta_S (J/(mol·K))`, `Phi (J/(mol·K))`

Notes: The checker recomputes delta_H and delta_S by numerical integration of the Cp column from the submitted CSV, then computes Phi = delta_S - (delta_H [in J/mol])/T. It compares the agent's reported delta_H, delta_S, and Phi against these recomputed references. The agent must provide the Cp column exactly as given in the task data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "enthalpy_entropy_Y04Bi06VO4.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T (K)",
          "Cp (J/(mol·K))",
          "delta_H (kJ/mol)",
          "delta_S (J/(mol·K))",
          "Phi (J/(mol·K))"
        ]
      },
      "description": "Thermodynamic functions for Y0.4Bi0.6VO4: temperature, heat capacity, enthalpy increment, entropy change, and reduced Gibbs free energy function."
    },
    {
      "file": "enthalpy_entropy_Y06Bi04VO4.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T (K)",
          "Cp (J/(mol·K))",
          "delta_H (kJ/mol)",
          "delta_S (J/(mol·K))",
          "Phi (J/(mol·K))"
        ]
      },
      "description": "Thermodynamic functions for Y0.6Bi0.4VO4: temperature, heat capacity, enthalpy increment, entropy change, and reduced Gibbs free energy function."
    }
  ],
  "notes": "The checker recomputes delta_H and delta_S by numerical integration of the Cp column from the submitted CSV, then computes Phi = delta_S - (delta_H [in J/mol])/T. It compares the agent's reported delta_H, delta_S, and Phi against these recomputed references. The agent must provide the Cp column exactly as given in the task data."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently recomputes ΔH and ΔS from the Cp column you provide in each CSV file, using the same numerical integration rule. The verifier compares the recomputed values to your reported delta_H and delta_S, and also checks that your Cp column matches the data given in the task. The final reward is a weighted combination of the scores for the two compositions. Writing a correct output that is consistent with the integration of the supplied heat capacity data is required; simply copy-pasting the reference paper’s numbers is not sufficient.
