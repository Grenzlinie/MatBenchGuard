# Compute thermodynamic functions and Debye temperature from low-temperature heat capacity data

## Problem background
Indium selenide (InSe) is a layered III–VI semiconductor with potential applications in nonlinear optics, infrared detectors, and solid‑state power sources. Accurate low‑temperature heat‑capacity data are crucial for determining standard thermodynamic functions (entropy, enthalpy increment, reduced Gibbs free energy) and for evaluating the Debye characteristic temperature, both of which are fundamental for understanding a material’s thermal and vibrational properties.

## Approach
The reproduction proceeds in two main stages: thermodynamic integration and Debye‑temperature analysis. First, load the experimental molar heat‑capacity data of InSe, provided as a table of (temperature, Cp) pairs. Apply spline smoothing to obtain a continuous Cp(T) function that captures the trend while filtering measurement scatter. Using standard numerical integration of the smoothed Cp, compute the thermodynamic functions at each target temperature: entropy S(T) = ∫₀ᵀ (Cp(u)/u) du, enthalpy increment H(T)−H(0) = ∫₀ᵀ Cp(u) du, and reduced Gibbs free energy Φ(T) = S − (H−H₀)/T. The integration requires a reasonable extrapolation from the lowest measured temperature down to 0 K. Second, evaluate the Debye characteristic temperature through a fractal‑model analysis of the heat‑capacity data. In this approach, the temperature dependence of the fracton dimension D is computed from the smoothed Cp for several trial Debye temperatures Θ. For a layered material like InSe, the correct Debye temperature corresponds to the Θ value that produces a D(T) curve with a maximum between 2 and 3. Identify the Θ that satisfies this criterion and report it as the material’s Debye temperature.

## Reproduction target
Using the provided raw Cp data, produce a CSV table of smoothed thermodynamic functions at the exact temperature grid: 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 298.15, 300, 310, 320 K (39 points). The table must contain columns T (K), Cp_smoothed (J/(K mol)), S (J/(K mol)), H_minus_H₀ (J/mol), and Phi (J/(K mol)). Additionally, produce a separate CSV file containing the Debye characteristic temperature (in K) evaluated via the fractal model.

## Assets

- Raw molar heat capacity data of InSe (Table 1)
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Spline smoothing of experimental Cp data
- Role: process
- Action: Load the raw Cp(T) data from the provided CSV file. Apply spline fitting using standard numerical libraries (e.g., SciPy) to obtain a smooth Cp(T) function that can be evaluated at arbitrary temperatures. Store the spline coefficients or smoothed curve for later integration.
- Evidence: `/app/outputs/smoothed_cp.csv`

### Step 2: Compute thermodynamic functions from smoothed Cp
- Role: scored (load-bearing)
- Action: Using the smoothed Cp(T) function from the previous step, numerically integrate Cp/T from the lowest measured temperature (extrapolated to 0 K as needed) to each target temperature to compute entropy S(T)=∫(Cp/T)dT, enthalpy increment H(T)-H(0)=∫Cp dT, and reduced Gibbs energy Φ(T)=S − (H−H0)/T. Output a CSV file with columns T, Cp_smoothed, S, H_minus_H0, Phi at the temperature grid: 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 298.15, 300, 310, 320 K (39 rows).
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: CSV with columns: T (K), Cp_smoothed (J/(K mol)), S (J/(K mol)), H_minus_H0 (J/mol), Phi (J/(K mol)). Exactly 39 rows.
- Scoring: scored by hidden verifier

### Step 3: Evaluate Debye characteristic temperature via fractal model
- Role: scored
- Action: Implement the fractal‑model analysis using the heat‑capacity data. Compute the temperature‑dependent fracton dimension D for several trial Debye temperatures Θ, or directly compute Θ(T) from the C_V data. Identify the Θ at which the D(T) curve has a maximum between 2 and 3, which corresponds to the Debye characteristic temperature for the layered InSe structure. Output the resulting Debye temperature value in a CSV file.
- Output file: `/app/outputs/debye_temperature.csv`
- Format: csv
- Contract: CSV with one row and one column: Debye_T (K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_functions.csv`
- `/app/outputs/debye_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_functions.csv
- path: `/app/outputs/thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Smoothed thermodynamic functions (heat capacity, entropy, enthalpy increment, reduced Gibbs energy) at the specified 39 temperatures. The values will be compared to the paper's reference table with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Cp_smoothed`, `S`, `H_minus_H0`, `Phi`
  - `units`:
    - `T`: K
    - `Cp_smoothed`: J/(K mol)
    - `S`: J/(K mol)
    - `H_minus_H0`: J/mol
    - `Phi`: J/(K mol)

### debye_temperature.csv
- path: `/app/outputs/debye_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Debye characteristic temperature of InSe evaluated from the heat capacity data via the fractal model.
- schema:
  - `type`: table
  - `required_columns`: `Debye_T`
  - `units`:
    - `Debye_T`: K

Notes: The spline smoothing step is mandatory but not directly scored; its output (smoothed_cp.csv) serves as evidence. Both scored artifacts are compared to the paper's reported values. The thermodynamic_functions.csv is the primary scored output and is load-bearing.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Cp_smoothed",
          "S",
          "H_minus_H0",
          "Phi"
        ],
        "units": {
          "T": "K",
          "Cp_smoothed": "J/(K mol)",
          "S": "J/(K mol)",
          "H_minus_H0": "J/mol",
          "Phi": "J/(K mol)"
        }
      },
      "description": "Smoothed thermodynamic functions (heat capacity, entropy, enthalpy increment, reduced Gibbs energy) at the specified 39 temperatures. The values will be compared to the paper's reference table with appropriate tolerances."
    },
    {
      "file": "debye_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Debye_T"
        ],
        "units": {
          "Debye_T": "K"
        }
      },
      "description": "Debye characteristic temperature of InSe evaluated from the heat capacity data via the fractal model."
    }
  ],
  "notes": "The spline smoothing step is mandatory but not directly scored; its output (smoothed_cp.csv) serves as evidence. Both scored artifacts are compared to the paper's reported values. The thermodynamic_functions.csv is the primary scored output and is load-bearing."
}
```

## How you are scored
A hidden verifier checks each scored artifact independently. For thermodynamic_functions.csv, the verifier compares every entry (Cp_smoothed, S, H_minus_H₀, Phi) against a hidden reference set, using tolerances appropriate for this type of numerical integration and smoothing. For debye_temperature.csv, the submitted Debye temperature is compared to a hidden reference value, again with an appropriate tolerance. The final reward is a weighted combination of the scores from these two artifacts. Note that merely reporting a known number is insufficient; the verifier evaluates whether the submitted values are consistent with a correct implementation of the required smoothing, integration, and fractal‑model analysis.
