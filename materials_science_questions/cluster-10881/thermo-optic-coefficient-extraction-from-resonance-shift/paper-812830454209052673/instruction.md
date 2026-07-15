# Recomputing the Temperature Shift Rate of the Characteristic UV Frequency in Quartz

## Problem background
The refractive indices of crystalline quartz change with temperature, and their temperature coefficients exhibit a wavelength dependence that reverses sign in the ultraviolet. A theory by Ramachandran explains these changes as a superposition of two effects: the decrease in oscillator density due to thermal expansion, and the shift of the characteristic ultraviolet absorption frequency toward longer wavelengths. The theory leads to a linear relation between a transformed temperature coefficient and a function of the wavenumber, whose slope involves the logarithmic temperature derivative of the characteristic frequency, denoted χ_t = d(log ν₀)/dt. This quantity is a key parameter linking optical and thermal behaviour. Your task is to implement the dispersion relations and the analysis procedure to compute χ_t from published experimental temperature-coefficient data, first at a fixed temperature of 60 °C and then as a function of temperature up to 435 °C.

## Approach
1. **Implement the dispersion formulas** for the ordinary and extraordinary refractive indices of quartz. Each index is expressed as a function of wavenumber ν = 1/λ (λ in microns) using a simplified form that includes: a constant background, a term from remote ultraviolet contributions, a resonant term from the characteristic ultraviolet frequency at ν₀², and a small infrared correction. The constants entering these formulas (a, c, b, ν₀², e) are given in the workflow details. Verify your implementation by computing the indices at the four wavelengths provided and compare with the reference values supplied.

2. **Derive the temperature-coefficient relation.** Starting from the dispersion formula, express the temperature derivative dn/dt in terms of the thermal expansion coefficient γ_t and the unknown shift rate χ_t. The derivation shows that after accounting for the density change, the quantity L = 2 n (dn/dt) + γ_t (n² − a) should be linear in 1/(ν₀² − ν²)², with the slope proportional to χ_t.

3. **Determine χ_t at 60 °C.** Use Michelis experimental dn/dt data for both ordinary and extraordinary rays at 60 °C, together with the thermal expansion coefficient γ_t = 35.6×10⁻⁶. For each wavelength, compute L and perform a least‑squares linear regression of L against 1/(ν₀² − ν²)². From the fitted slope, extract χ_t for each ray and report the average value.

4. **Validate the fitted model.** Using the linear relations obtained, calculate the temperature coefficients dn/dt at the seven wavelengths listed and compare them with the observed values to check the internal consistency of the analysis.

5. **Compute χ_t as a function of temperature.** Use Reeds experimental dn/dt data for the extraordinary ray at nine temperatures (23–435 °C) and the corresponding thermal expansion coefficients γ_t provided. At each temperature, apply the formula that expresses χ_t in terms of dn/dt and γ_t (this formula is algebraically equivalent to the regression relation but is rearranged to give χ_t directly from a single measurement). Perform the calculation for three wavelengths (4358, 5893, 6563 Å) at each temperature and tabulate the results.

All required input data — dispersion constants, Micheli and Reed dn/dt values, and γ_t coefficients — are supplied in the workflow instructions. The agent does not need to fetch any external datasets.

## Reproduction target
Using the supplied dispersion parameters, thermal expansion coefficients, and the experimental temperature-coefficient data (Micheli at 60 °C and Reed at multiple temperatures), produce two final artifacts:

- A plain text file containing a single floating‑point number: the computed χ_t at 60 °C, expressed in units of 10⁻⁵.
- A CSV table with the columns temperature_C, gamma_t_1e6, dn_e_dt_4358_1e6, dn_e_dt_5893_1e6, dn_e_dt_6563_1e6, chi_t_4358, chi_t_5893, chi_t_6563, giving the derived χ_t (in 10⁻⁵) at nine temperatures for three wavelengths.

The values must follow from the implemented dispersion formulas and the prescribed linear analysis; the files will be assessed by an automated verifier that compares your outputs to independently computed reference values.

## Assets

- Python 3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement dispersion formulas
- Role: process
- Action: Implement the simplified dispersion formulas for ordinary (n_ω) and extraordinary (n_e) refractive indices of quartz as functions of wavenumber ν=1/λ (λ in microns). Verify the implementation by computing indices at the four wavelengths listed in the paper (0.20255, 0.312279, 0.467815, 0.64385 µm) and confirm agreement with the known values provided in the instruction.
- Evidence: `/app/outputs/refractive_indices.txt`

### Step 2: Determine χ_t at 60°C from Micheli data
- Role: scored (load-bearing)
- Action: Using the implemented dispersion formulas, the thermal expansion coefficient γ_t=35.6×10⁻⁶ at 60°C, and Micheli's experimental dn/dt values provided in the instruction, compute the left-hand side of the temperature coefficient equations for ordinary and extraordinary rays, perform linear regression against 1/(ν0²-ν²)² to extract the slope, and compute χ_t from the slope. Output the average χ_t value.
- Output file: `/app/outputs/chi_t_60.txt`
- Format: txt
- Contract: Plain text file containing a single floating-point number on one line, representing χ_t in units of 10⁻⁵.
- Scoring: scored by hidden verifier

### Step 3: Validate computed dn/dt against experiment
- Role: process
- Action: Using the fitted linear relations from the previous step, compute the temperature coefficients dn/dt for the wavelengths listed in the instruction (0.202, 0.257, 0.312, 0.340, 0.467, 0.508, 0.643 µm) and compare with Micheli's observed values to verify the model.
- Evidence: `/app/outputs/validation_table.csv`

### Step 4: Compute χ_t vs temperature from Reed data
- Role: scored
- Action: Using Reed's experimental dn/dt data for the extraordinary ray at the temperatures 23.0, 61.2, 125.2, 177.0, 227.5, 275, 328, 385, 435 °C and the corresponding thermal expansion coefficients γ_t provided in the instruction, apply the formula relating χ_t to dn/dt and γ_t to compute χ_t at each temperature and at each of the three wavelengths (4358, 5893, 6563 Å). Output a CSV table.
- Output file: `/app/outputs/chi_t_temperature.csv`
- Format: csv
- Contract: CSV with header: temperature_C,gamma_t_1e6,dn_e_dt_4358_1e6,dn_e_dt_5893_1e6,dn_e_dt_6563_1e6,chi_t_4358,chi_t_5893,chi_t_6563. All chi_t values in 10⁻⁵ units. One row per temperature as listed above.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/chi_t_60.txt`
- `/app/outputs/chi_t_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### chi_t_60.txt
- path: `/app/outputs/chi_t_60.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Shift rate of the characteristic UV frequency at 60°C, reported as a single floating-point number in units of 10⁻⁵.
- schema:
  - `type`: text
  - `units`: 10⁻⁵

### chi_t_temperature.csv
- path: `/app/outputs/chi_t_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of χ_t values computed from Reed's data for the extraordinary ray, showing its variation with temperature. All χ_t values are in units of 10⁻⁵.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `gamma_t_1e6`, `dn_e_dt_4358_1e6`, `dn_e_dt_5893_1e6`, `dn_e_dt_6563_1e6`, `chi_t_4358`, `chi_t_5893`, `chi_t_6563`
  - `units`:
    - `chi_t_4358`: 10⁻⁵
    - `chi_t_5893`: 10⁻⁵
    - `chi_t_6563`: 10⁻⁵

Notes: All χ_t values are to be reported in units of 10⁻⁵. The chi_t_60.txt file must contain only the numeric value (e.g., a single float). The chi_t_temperature.csv must contain exactly nine data rows (one per temperature) with the specified columns.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "chi_t_60.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": "10⁻⁵"
      },
      "description": "Shift rate of the characteristic UV frequency at 60°C, reported as a single floating-point number in units of 10⁻⁵."
    },
    {
      "file": "chi_t_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "gamma_t_1e6",
          "dn_e_dt_4358_1e6",
          "dn_e_dt_5893_1e6",
          "dn_e_dt_6563_1e6",
          "chi_t_4358",
          "chi_t_5893",
          "chi_t_6563"
        ],
        "units": {
          "chi_t_4358": "10⁻⁵",
          "chi_t_5893": "10⁻⁵",
          "chi_t_6563": "10⁻⁵"
        }
      },
      "description": "Table of χ_t values computed from Reed's data for the extraordinary ray, showing its variation with temperature. All χ_t values are in units of 10⁻⁵."
    }
  ],
  "notes": "All χ_t values are to be reported in units of 10⁻⁵. The chi_t_60.txt file must contain only the numeric value (e.g., a single float). The chi_t_temperature.csv must contain exactly nine data rows (one per temperature) with the specified columns."
}
```

## How you are scored
A hidden verifier will score each workflow stage independently by comparing your submitted artifacts to a hidden reference. For `chi_t_60.txt`, the verifier reads the single floating-point number and compares it to the expected value within an appropriate tolerance. For `chi_t_temperature.csv`, the verifier parses the table and checks each χ_t column entry by entry. The final total reward is a weighted combination of these per-stage scores. Simply copying numbers from the paper is neither expected nor sufficient; the verifier evaluates the results derived from your implemented analysis.
