# High pressure melt curve of iron using atom-in-jellium model

## Problem background
The high-pressure melt curve of iron is critical for understanding the thermal evolution and magnetic dynamo of planetary cores, especially in massive rocky exoplanets. Direct melt curve predictions via quantum molecular dynamics are computationally demanding, and empirical extrapolations can diverge at high compression. This work applies an efficient atom-in-jellium displacement model, combined with a Lindemann-like criterion, to predict the iron melt curve over a wide pressure range from first-principles electronic structure calculations. Reproducing the computed melt curve and its analytic fit provides a physically grounded reference for core freezing in super-Earths.

## Approach
The method treats a single iron atom (Z=26, atomic mass 55.845 u) inside a spherical Wigner-Seitz cell filled with a uniform jellium of electrons. At each mass density and temperature, a self-consistent Kohn-Sham calculation yields the equilibrium electron density. A small displacement of the ion from the cell center is applied, and the Hellmann-Feynman restoring force constant is computed. This gives the Einstein vibrational frequency and, via the Debye model, the Debye temperature and the mean fractional displacement u_f (ion displacement divided by the Wigner-Seitz radius). The melt curve is defined by the contour u_f = 0.12 – a value that empirical calibration shows matches available quantum molecular dynamics melting points for iron at high compression. The equation of state (pressure) is obtained from the atom-in-jellium free energy at each grid point. Finally, a Simon power-law equation T_m = T0 (P / P0)^b is fitted to the pressure-temperature melt points to provide a compact analytic representation.

## Reproduction target
Compute the atom-in-jellium model for iron on a grid of mass density (covering at least 5 to 100 g/cm³) and temperature (covering at least 1000 to 50000 K). From the resulting u_f grid, extract the u_f = 0.12 contour and output the corresponding melt curve as a CSV file (columns: density_g_cm3, temperature_K, pressure_GPa) with at least 20 points. Then fit a Simon equation T_m = T0 (P / P0)^b to these points over the pressure range 1–100 TPa and output the fitting parameters as a JSON file (keys: T0, P0, exponent).

## Assets

- Iron atomic properties

## Workflow steps

### Step 1: Atom-in-jellium simulation for iron
- Role: process
- Action: Implement the atom-in-jellium model for iron (Z=26, atomic mass 55.845 u) within a Wigner-Seitz cell. For a grid of mass densities (covering at least 5–100 g/cm³) and temperatures (covering at least 1000–50000 K), compute the equilibrium electron density, Hellmann-Feynman restoring force constant, Einstein frequency, Einstein and Debye temperatures, the mean fractional displacement u_f, and the equation of state (pressure).
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Derive high-pressure Fe melt curve
- Role: scored (load-bearing)
- Action: From the computed u_f grid, interpolate to find the contour where u_f = 0.12. Along this contour, compute the pressure using the atom-in-jellium equation of state. Output a CSV file with columns: density_g_cm3, temperature_K, pressure_GPa, covering the melt curve from about 5 to 100 g/cm³ (at least 20 points).
- Output file: `/app/outputs/melt_curve.csv`
- Format: csv
- Contract: CSV with columns: density_g_cm3 (float), temperature_K (float), pressure_GPa (float). At least 20 rows.
- Scoring: scored by hidden verifier

### Step 3: Simon equation fit for Fe melt curve
- Role: scored (load-bearing)
- Action: Fit a Simon-type equation T_m = T0 * (P / P0)^b to the pressure-temperature data from the previous step over the pressure range 1–100 TPa. Output the fit parameters as a JSON file.
- Output file: `/app/outputs/simon_fit.json`
- Format: json
- Contract: JSON object with keys 'T0' (float, temperature in K at reference pressure), 'P0' (float, reference pressure in GPa), 'exponent' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/melt_curve.csv`
- `/app/outputs/simon_fit.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### melt_curve.csv
- path: `/app/outputs/melt_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: High-pressure melt curve of iron (u_f=0.12 contour). Minimum 20 rows, each with density, temperature, and pressure.
- schema:
  - `type`: table
  - `required_columns`: `density_g_cm3`, `temperature_K`, `pressure_GPa`
  - `units`:
    - `density_g_cm3`: g/cm^3
    - `temperature_K`: K
    - `pressure_GPa`: GPa

### simon_fit.json
- path: `/app/outputs/simon_fit.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Simon equation parameters for the melt curve. T0 (K) at reference pressure P0 (GPa), exponent.
- schema:
  - `type`: object
  - `required`:
    - `T0`: number
    - `P0`: number
    - `exponent`: number

Notes: The melt curve is scored by comparing the agent's computed points to a hidden set digitized from the paper's Fig. 2; the Simon parameters are compared to the paper's reported values. Both use tolerances appropriate for implementation-dependent differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "melt_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "density_g_cm3",
          "temperature_K",
          "pressure_GPa"
        ],
        "units": {
          "density_g_cm3": "g/cm^3",
          "temperature_K": "K",
          "pressure_GPa": "GPa"
        }
      },
      "description": "High-pressure melt curve of iron (u_f=0.12 contour). Minimum 20 rows, each with density, temperature, and pressure."
    },
    {
      "file": "simon_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "T0": "number",
          "P0": "number",
          "exponent": "number"
        }
      },
      "description": "Simon equation parameters for the melt curve. T0 (K) at reference pressure P0 (GPa), exponent."
    }
  ],
  "notes": "The melt curve is scored by comparing the agent's computed points to a hidden set digitized from the paper's Fig. 2; the Simon parameters are compared to the paper's reported values. Both use tolerances appropriate for implementation-dependent differences."
}
```

## How you are scored
A hidden verifier independently evaluates the artifacts you write to /app/outputs. Each step's output is compared against a reference standard derived from the published results. The verifier checks that melt_curve.csv contains at least 20 points covering the stated density range and that the pressure and temperature values along the u_f=0.12 contour are physically consistent and match the reference within tolerances that account for numerical implementation differences. The Simon fit parameters are compared similarly. The reward is a weighted combination of the step scores; simply copying or guessing the published numbers without running the full simulation will not satisfy the checks.
