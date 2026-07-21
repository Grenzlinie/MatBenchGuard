# Recomputing the Temperature Shift Rate of the Characteristic UV Frequency in Quartz

## Problem background
The refractive indices of crystalline quartz change with temperature, and their temperature coefficients exhibit a wavelength dependence that reverses sign in the ultraviolet. A theory by Ramachandran explains these changes as a superposition of two effects: the decrease in oscillator density due to thermal expansion, and the shift of the characteristic ultraviolet absorption frequency toward longer wavelengths. The theory leads to a linear relation between a transformed temperature coefficient and a function of the wavenumber, whose slope involves the logarithmic temperature derivative of the characteristic frequency, denoted χ_t = d(log ν₀)/dt. This quantity is a key parameter linking optical and thermal behaviour. Your task is to implement the dispersion relations and the analysis procedure to compute χ_t from published experimental temperature-coefficient data, first at a fixed temperature of 60 °C and then as a function of temperature up to 435 °C.

## Input data
All numerical data required for the calculations are provided below. They are extracted from the original paper that reported this analysis.

### Dispersion formula constants
The simplified dispersion formulas for the ordinary (n_ω) and extraordinary (n_e) indices at room temperature are:

```
n_ω^2 = a_o + c_o ν^2 + b_o/(ν_0^2 − ν^2) − e_o/ν^2
n_e^2 = a_e + c_e ν^2 + b_e/(ν_0^2 − ν^2) − e_e/ν^2
```

where ν = 1/λ (λ in microns) and

| symbol | value |
|--------|-------|
| a_o    | 1.7239 |
| a_e    | 1.7210 |
| c_o    | 0.002682 |
| c_e    | 0.002761 |
| b_o    | 49.630 |
| b_e    | 51.962 |
| ν_0^2  | 78.436 |
| e_o    | 0.0109 |
| e_e    | 0.0109 |

**Verification indices** – Use the following reference values to check your implementation of the dispersion formulas:

| λ (microns) | n_ω (observed) | n_e (observed) |
|-------------|----------------|----------------|
| 0.20255     | 1.6456         | 1.6584         |
| 0.312279    | 1.5743         | 1.5845         |
| 0.467815    | 1.5510         | 1.56037        |
| 0.64385     | 1.5423         | 1.5513         |

### Experimental temperature‑coefficient data at 60 °C (Micheli)
These data are used in Step 2 to determine χ_t at 60 °C. The values are the observed temperature coefficients (dn/dt) of the ordinary and extraordinary rays, quoted in the paper as ×10⁶ (i.e., in units of 10⁻⁶ per °C). The thermal expansion coefficient at 60 °C is γ_t = 35.6×10⁻⁶.

| λ (microns) | (dn_ω/dt) × 10⁶  (observed) | (dn_e/dt) × 10⁶  (observed) |
|-------------|-----------------------------|-----------------------------|
| 0.202       | +1.84                       | +1.29                       |
| 0.257       | −3.09                       | −3.89                       |
| 0.312       | −4.65                       | −5.68                       |
| 0.340       | −5.08                       | −6.17                       |
| 0.467       | −5.96                       | −7.15                       |
| 0.508       | −6.26                       | −7.29                       |
| 0.643       | −6.60                       | −7.64                       |

### Experimental data for the extraordinary ray as a function of temperature (Reed)
These data are used in Step 4 to compute χ_t at multiple temperatures. The thermal expansion coefficients γ_t are listed in units of 10⁻⁶ /°C. The dn_e/dt values are those published by Reed and correspond to the raw tabulated numbers (which, in the original paper, carry a factor of 10⁻¹⁰ cm/°C? — in practice the linear relations given below use these numbers directly as they appear in the paper’s table, without additional rescaling). **Important**: The column names in the output CSV reflect the verifier’s naming convention, not the physical unit; treat the dn_e/dt entries as the Reed numbers reproduced below.

| Temperature (°C) | γ_t × 10⁶ | dn_e/dt (4358) | dn_e/dt (5893) | dn_e/dt (6563) |
|-----------------|-----------|----------------|----------------|----------------|
| 23.0            | 34.35     | −6.52          | −7.14          | −7.18          |
| 61.2            | 35.6      | −7.07          | −7.66          | −7.73          |
| 125.2           | 37.7      | −7.71          | −8.29          | −8.43          |
| 177.0           | 39.35     | −8.73          | −9.33          | −9.44          |
| 227.5           | 41.1      | −9.52          | −10.12         | −10.30         |
| 275             | 42.65     | −11.06         | −11.78         | −11.91         |
| 328             | 44.7      | −13.48         | −14.19         | −14.27         |
| 385             | 47.3      | −17.53         | −18.40         | −18.57         |
| 435             | 49.95     | −21.49         | −22.53         | −22.75         |

### Linear relations for χ_t from Reed’s data
At each temperature, χ_t (in units of 10⁻⁵) is obtained from the Reed data using the following expressions, which are algebraically derived from the theory. Use the numerical values from the table exactly as they appear (the dn values are the raw Reed numbers, and γ is the γ_t × 10⁶ value):

```
χ_t_4358 = −(2.0535 * dn_4358 + 1.2155 * γ) / 10.0
χ_t_5893 = −(2.1760 * dn_5893 + 1.2155 * γ) / 10.0
χ_t_6563 = −(2.2067 * dn_6563 + 1.2970 * γ) / 10.0
```

All χ_t values are to be reported in units of 10⁻⁵.

## Approach
1. **Implement the dispersion formulas** for the ordinary and extraordinary refractive indices using the constants in the Input data section. Verify your implementation by computing the indices at the four reference wavelengths and comparing with the observed values provided.

2. **Derive the temperature-coefficient relation.** Starting from the dispersion formula, express the temperature derivative dn/dt in terms of the thermal expansion coefficient γ_t and the unknown shift rate χ_t. The derivation shows that after accounting for the density change, the quantity

   ```
   L = 2 n (dn/dt) + γ_t (n² − a)
   ```

   should be linear in X = 1/(ν₀² − ν²)², with the slope proportional to χ_t. The theoretical slope B is related to χ_t by χ_t = −slope / (2 b ν₀²), where b is the oscillator strength from the dispersion formula and ν₀² = 78.436.

3. **Determine χ_t at 60 °C.** Use the Micheli dn/dt data for both ordinary and extraordinary rays at 60 °C, together with γ_t = 35.6×10⁻⁶. For each ray, compute L and X for the seven wavelengths, perform a least‑squares linear regression of L against X, and extract χ_t from the slope. Report the average χ_t from the two rays.

4. **Validate the fitted model.** Using the linear relations obtained, compute the temperature coefficients dn/dt at the seven wavelengths listed and compare them with Micheli’s observed values to verify the internal consistency of the analysis. Save the comparison as a CSV.

5. **Compute χ_t as a function of temperature.** Using the Reed data for the extraordinary ray at nine temperatures and the linear relations provided in the Input data section, compute χ_t at each temperature and at each of the three wavelengths (4358, 5893, 6563 Å). Tabulate the results together with the input values.

All required input data are supplied in the ”Input data” section. The agent does not need to fetch any external datasets.

## Reproduction target
Produce four output artifacts:

- A text file containing the χ_t at 60 °C (units of 10⁻⁵).
- A CSV table with the derived χ_t versus temperature for the extraordinary ray.
- A text file with the refractive indices computed during the dispersion formula verification (process evidence, not scored).
- A CSV table comparing calculated and observed dn/dt at 60 °C (process evidence, not scored).

The two scored files will be assessed by an automated verifier; the two process-evidence files are only checked for existence and shape.

## Assets
- Python 3
- NumPy
- SciPy

## Workflow steps

### Step 1: Implement dispersion formulas
- Role: process
- Action: Implement the simplified dispersion formulas for ordinary and extraordinary indices using the constants from the Input data. Verify by computing the indices at the four wavelengths listed (0.20255, 0.312279, 0.467815, 0.64385 µm) and confirm agreement with the provided observed values. Write the computed indices (one set per line, any readable format) to a file.
- Evidence: `/app/outputs/refractive_indices.txt`

### Step 2: Determine χ_t at 60 °C from Micheli data
- Role: scored (load-bearing)
- Action: Using the implemented dispersion formulas, γ_t = 35.6×10⁻⁶, and the Micheli dn/dt data tabulated in Input data, compute L and X for each ray, perform linear regression, extract χ_t from the slopes, and compute the average.
- Output file: `/app/outputs/chi_t_60.txt`
- Format: txt – a single floating-point number representing χ_t in 10⁻⁵.
- Scoring: scored by hidden verifier.

### Step 3: Validate computed dn/dt against experiment
- Role: process
- Action: Using the fitted linear relations from Step 2, compute the dn/dt values for the seven wavelengths and compare with Micheli’s observed values. Save a table with columns: wavelength, dn_o_dt_calc, dn_o_dt_obs, dn_e_dt_calc, dn_e_dt_obs.
- Evidence: `/app/outputs/validation_table.csv`

### Step 4: Compute χ_t vs temperature from Reed data
- Role: scored
- Action: Using the Reed data and the linear relations given in the Input data section, compute χ_t at each of the nine temperatures and three wavelengths. Output a CSV table containing all input values and the computed χ_t.
- Output file: `/app/outputs/chi_t_temperature.csv`
- Format: csv with header: temperature_C, gamma_t_1e6, dn_e_dt_4358_1e6, dn_e_dt_5893_1e6, dn_e_dt_6563_1e6, chi_t_4358, chi_t_5893, chi_t_6563. All chi_t values in units of 10⁻⁵.
- Scoring: scored by hidden verifier.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/chi_t_60.txt` (scored)
- `/app/outputs/chi_t_temperature.csv` (scored)
- `/app/outputs/refractive_indices.txt` (process evidence)
- `/app/outputs/validation_table.csv` (process evidence)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### chi_t_60.txt
- path: `/app/outputs/chi_t_60.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Shift rate of the characteristic UV frequency at 60 °C, reported as a single floating-point number in units of 10⁻⁵.
- schema:
  - type: text
  - units: 10⁻⁵

### chi_t_temperature.csv
- path: `/app/outputs/chi_t_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of χ_t values computed from Reed's data for the extraordinary ray, showing its variation with temperature. All χ_t values are in units of 10⁻⁵.
- schema:
  - type: table
  - required_columns: `temperature_C`, `gamma_t_1e6`, `dn_e_dt_4358_1e6`, `dn_e_dt_5893_1e6`, `dn_e_dt_6563_1e6`, `chi_t_4358`, `chi_t_5893`, `chi_t_6563`
  - units:
    - chi_t_4358: 10⁻⁵
    - chi_t_5893: 10⁻⁵
    - chi_t_6563: 10⁻⁵

### refractive_indices.txt
- path: `/app/outputs/refractive_indices.txt`
- format: txt
- purpose: process
- target_policy: none
- description: Refractive indices computed from the dispersion formulas at the four verification wavelengths.
- schema:
  - type: text
  - units: none

### validation_table.csv
- path: `/app/outputs/validation_table.csv`
- format: csv
- purpose: process
- target_policy: none
- description: Comparison of calculated and observed dn/dt at 60 °C.
- schema:
  - type: table
  - required_columns: `wavelength`, `dn_o_dt_calc`, `dn_o_dt_obs`, `dn_e_dt_calc`, `dn_e_dt_obs`
  - units:
    - dn_o_dt_calc: 10⁻⁶ / °C
    - dn_o_dt_obs: 10⁻⁶ / °C
    - dn_e_dt_calc: 10⁻⁶ / °C
    - dn_e_dt_obs: 10⁻⁶ / °C

Notes: All χ_t values are to be reported in units of 10⁻⁵. The chi_t_60.txt file must contain only the numeric value. The chi_t_temperature.csv must contain exactly nine data rows with the specified columns. The validation_table.csv must have seven rows corresponding to the wavelengths in the Input data table. The refractive_indices.txt may contain the four computed index pairs in any readable form.

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
    },
    {
      "file": "refractive_indices.txt",
      "format": "txt",
      "purpose": "process",
      "target_policy": "none",
      "schema": {
        "type": "text",
        "units": "none"
      },
      "description": "Refractive indices computed from the dispersion formulas at the four verification wavelengths."
    },
    {
      "file": "validation_table.csv",
      "format": "csv",
      "purpose": "process",
      "target_policy": "none",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength",
          "dn_o_dt_calc",
          "dn_o_dt_obs",
          "dn_e_dt_calc",
          "dn_e_dt_obs"
        ],
        "units": {
          "dn_o_dt_calc": "10⁻⁶ / °C",
          "dn_o_dt_obs": "10⁻⁶ / °C",
          "dn_e_dt_calc": "10⁻⁶ / °C",
          "dn_e_dt_obs": "10⁻⁶ / °C"
        }
      },
      "description": "Comparison of calculated and observed dn/dt at 60°C."
    }
  ],
  "notes": "All χ_t values are to be reported in units of 10⁻⁵. The chi_t_60.txt file must contain only the numeric value. The chi_t_temperature.csv must contain exactly nine data rows (one per temperature) with the specified columns. The validation_table.csv must have seven rows corresponding to the wavelengths in the Input data table. The refractive_indices.txt may contain the four computed index pairs in any readable form."
}
```

## How you are scored
A hidden verifier will score each workflow stage independently by comparing your submitted artifacts to a hidden reference. For `chi_t_60.txt`, the verifier reads the single floating-point number and compares it to the expected value within an appropriate tolerance. For `chi_t_temperature.csv`, the verifier parses the table and checks each χ_t column entry by entry. The final total reward is a weighted combination of these per-stage scores. Simply copying numbers from the paper is neither expected nor sufficient; the verifier evaluates the results derived from your implemented analysis.