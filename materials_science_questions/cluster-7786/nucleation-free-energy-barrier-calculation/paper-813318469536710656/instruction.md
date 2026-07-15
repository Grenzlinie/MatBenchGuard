# Temperature-Dependent Crystal-Melt Interfacial Energy Calculation

## Problem background
The crystal–melt interfacial energy is a key parameter in solidification kinetics and nucleation theory, influencing undercooling and glass formation. Its temperature dependence is critical for predicting solidification behavior, yet direct measurement is limited to the melting point and the homogeneous nucleation temperature. An analytical model that can compute the interfacial energy at any temperature from basic thermodynamic data would provide significant predictive power. This task implements such a model to calculate the interfacial energy and Turnbull coefficient for three face-centered cubic metals.

## Approach
The model combines a smooth-interface baseline with a configurational entropy correction for a rough equilibrium interface. For each metal, a baseline interfacial energy is first computed from the entropy of fusion and vibrational entropy at the melting point, using the Grüneisen constant and molar volumes. The temperature-dependent entropy of fusion is obtained by integrating the difference in heat capacities between the crystal and the melt along the temperature profile. The equilibrium interfacial energy is then derived by minimizing the Gibbs energy associated with adding crystal atoms to the interface, which yields a mixing term involving the fraction x* of crystal atoms in the interface layer. When the configurational correction parameter exceeds a threshold, x* deviates from 0.5 and must be solved numerically. Using the computed x*, the final interfacial energy, its non-dimensional form, and the Turnbull coefficient are calculated. The implementation must handle piecewise heat capacities for nickel and perform numerical root-finding and integration as needed.

## Reproduction target
Compute the crystal–melt interfacial energy σ^T (J/m²), the non-dimensional interfacial energy φ^T, and the Turnbull coefficient C for silver, copper, and nickel. Perform the calculations at the melting point for each metal and at the experimental homogeneous nucleation temperatures: for silver 983 K, 978 K, 974 K; for copper 1090 K, 1079 K; for nickel 1387 K, 1362 K. Write the results to a CSV file with columns: metal, temperature_K, sigma_J_per_m2, phi, C.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute Interfacial Energy and Turnbull Coefficient
- Role: scored
- Action: Implement the analytical model for crystal-melt interfacial energy as described in the methodology (smooth-interface baseline with configurational correction, solving for equilibrium fraction x*, temperature-dependent entropy of fusion). Use the provided thermodynamic parameters for silver, copper, and nickel. For each metal, compute sigma^T (J/m²), phi^T (dimensionless), and Turnbull coefficient C (dimensionless) at the melting point and at the specified homogeneous nucleation temperatures. Write the results to a CSV file.
- Output file: `/app/outputs/interfacial_energies.csv`
- Format: csv
- Contract: columns: metal (string), temperature_K (float, K), sigma_J_per_m2 (float, J/m²), phi (float, dimensionless), C (float, dimensionless). One row per (metal, temperature) pair.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interfacial_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interfacial_energies.csv
- path: `/app/outputs/interfacial_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed crystal-melt interfacial energies and Turnbull coefficients for Ag, Cu, Ni at the melting point and at specified homogeneous nucleation temperatures.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `temperature_K`, `sigma_J_per_m2`, `phi`, `C`
  - `units`:
    - `sigma_J_per_m2`: J/m^2
    - `phi`: dimensionless
    - `C`: dimensionless

Notes: The hidden checker will compare the agent's computed sigma and C values against the paper's reported numbers using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interfacial_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "temperature_K",
          "sigma_J_per_m2",
          "phi",
          "C"
        ],
        "units": {
          "sigma_J_per_m2": "J/m^2",
          "phi": "dimensionless",
          "C": "dimensionless"
        }
      },
      "description": "Computed crystal-melt interfacial energies and Turnbull coefficients for Ag, Cu, Ni at the melting point and at specified homogeneous nucleation temperatures."
    }
  ],
  "notes": "The hidden checker will compare the agent's computed sigma and C values against the paper's reported numbers using appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently evaluates the output CSV file. For each (metal, temperature) pair, it compares your computed σ^T and C against reference values derived from the paper. The final reward combines the per-row scores using appropriate tolerances; partial credit is awarded based on how many entries fall within tolerance. The verifier does not simply check for the presence of the file; it verifies the correctness of the computed numbers. Submitting only the paper's published numbers without implementing the model will not succeed because the verifier checks multiple temperatures and metals with tolerances that reflect the expected numerical spread from a correct re‑implementation.
