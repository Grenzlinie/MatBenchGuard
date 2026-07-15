# Specific Heat and Crystallinity Determination via Calorimetric Data

## Problem background
Polychlorotrifluoroethylene (PCTFE) is a semicrystalline fluoropolymer whose mechanical and thermal properties depend on the fraction of crystalline material. The degree of crystallinity can be determined from enthalpy data by comparing the sample's enthalpy to that of the pure liquid and pure crystalline phases. Published specific heat measurements on air‑quenched and slow‑cooled samples provide the raw calorimetric data, and a reference heat of fusion for fully crystalline PCTFE is available from the literature. This task reproduces the computational analysis that converts the specific heat data into the experimental heat of fusion of each sample and the degree of crystallinity as a function of temperature.

## Approach
The method begins with the specific heat vs temperature data for both samples, which are provided in this instruction. Numerical integration yields raw enthalpy curves relative to an arbitrary zero at 0 °C. Within the melting region, a baseline is established by extrapolating the low‑temperature specific heat, and the area under the melting peak gives the experimental heat of fusion for each sample. Using the known heat of fusion of the pure crystal, the degree of crystallinity at 0 °C is estimated. By requiring that the liquid‑region enthalpies coincide, a constant offset between the two samples' enthalpy scales is found, and simultaneous equations are solved to obtain the enthalpies of the pure liquid and pure crystal at 0 °C relative to a common standard state. The pure‑phase specific heats at 0 °C are similarly obtained from the additivity of specific heats. Assuming a linear temperature dependence for the specific heat of both pure phases, the temperature coefficients are determined from the total enthalpy change between 0 °C and 212 °C, yielding integrated enthalpy functions. Finally, for each sample the corrected sample enthalpy is used in the enthalpy‑based crystallinity formula to compute the degree of crystallinity at every tabulated temperature.

## Reproduction target
Given the specific heat vs temperature data for the air‑quenched and slow‑cooled samples (provided in this instruction) and the reference heat of fusion of pure crystalline PCTFE (10.3 cal/g), compute and report:

1. The experimental heat of fusion Δh_f for each sample, output as `heats_of_fusion.csv`.
2. The degree of crystallinity at selected temperatures between 0 °C and 212 °C for both samples, output as `crystallinity_vs_temperature.csv`.

The expected format and contract for these files are detailed in the workflow steps and output contract sections.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Load specific heat data
- Role: process
- Action: Extract the specific heat vs temperature values for air-quenched and slow-cooled polychlorotrifluoroethylene from the data table provided in the instruction and store them in arrays for further processing.
- Evidence: none

### Step 2: Compute raw enthalpy curves
- Role: process
- Action: Numerically integrate the specific heat data from 0°C to obtain raw enthalpy differences (H_x - H_0') and (H_x - H_0'') for each sample (trapezoidal rule or similar). Write the raw enthalpy values to an intermediate CSV file.
- Evidence: `/app/outputs/raw_enthalpy.csv`

### Step 3: Determine experimental heats of fusion
- Role: scored (load-bearing)
- Action: For each sample, locate the melting peak in the specific heat curve, define a baseline by extrapolating the low-temperature cp, integrate the excess heat capacity to obtain the heat of fusion Δh_f. Write results to heats_of_fusion.csv.
- Output file: `/app/outputs/heats_of_fusion.csv`
- Format: csv
- Contract: required_columns: sample (string, one of the two sample identifiers), delta_h_cal_per_g (float, heat of fusion in cal/g)
- Scoring: scored by hidden verifier

### Step 4: Align liquid-region enthalpies and find offset
- Role: process
- Action: Compare the enthalpy curves above the melting point to find the constant offset between the two samples' enthalpy scales, so that their liquid-region enthalpies coincide.
- Evidence: none

### Step 5: Compute baseline crystallinity at 0°C
- Role: process
- Action: Using the measured heats of fusion from step_03 and the given pure-crystal heat of fusion (10.3 cal/g), calculate the degree of crystallinity X0 for each sample at 0°C.
- Evidence: none

### Step 6: Solve for pure-phase enthalpies at 0°C
- Role: process
- Action: Use the crystallinity values from step_05 and the enthalpy offset to set up and solve simultaneous equations that yield the enthalpy of the pure liquid and the pure crystal at 0°C relative to a common standard state.
- Evidence: none

### Step 7: Determine pure-phase specific heats at 0°C
- Role: process
- Action: Using the specific heat values of the samples at 0°C and their crystallinities, solve the additive specific heat equations to obtain cp of the pure liquid and cp of the pure crystal at 0°C.
- Evidence: none

### Step 8: Construct linear cp models and enthalpy functions
- Role: process
- Action: Assume cp(T) = cp0 + B*T for both pure liquid and crystal. Use the total enthalpy changes from 0 to 212°C and the cp0 values to determine B and B', then integrate to obtain the enthalpy functions H_c(T) and H_l(T).
- Evidence: none

### Step 9: Compute degree of crystallinity vs temperature
- Role: scored (load-bearing)
- Action: For each sample, compute the corrected sample enthalpy (H_x - H_0) using the standard state defined in step_06, then apply the enthalpy-based crystallinity formula X = [(H_l - H_x) / (H_l - H_c)] to calculate the degree of crystallinity at the tabulated temperatures (0–212°C). Write results to crystallinity_vs_temperature.csv.
- Output file: `/app/outputs/crystallinity_vs_temperature.csv`
- Format: csv
- Contract: required_columns: temperature_C (float, °C), air_quenched_crystallinity (float, value between 0 and 1), slow_cooled_crystallinity (float, between 0 and 1)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heats_of_fusion.csv`
- `/app/outputs/crystallinity_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heats_of_fusion.csv
- path: `/app/outputs/heats_of_fusion.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Experimental heat of fusion for the air‑quenched and slow‑cooled polymer samples.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `delta_h_cal_per_g`
  - `units`:
    - `delta_h_cal_per_g`: cal/g

### crystallinity_vs_temperature.csv
- path: `/app/outputs/crystallinity_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Degree of crystallinity (fraction) at selected temperatures between 0°C and 212°C for the two samples.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `air_quenched_crystallinity`, `slow_cooled_crystallinity`
  - `units`:
    - `temperature_C`: °C

Notes: All values are computed from the provided specific heat data and the literature pure‑crystal heat of fusion; tolerances accommodate small numerical integration differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heats_of_fusion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "delta_h_cal_per_g"
        ],
        "units": {
          "delta_h_cal_per_g": "cal/g"
        }
      },
      "description": "Experimental heat of fusion for the air‑quenched and slow‑cooled polymer samples."
    },
    {
      "file": "crystallinity_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "air_quenched_crystallinity",
          "slow_cooled_crystallinity"
        ],
        "units": {
          "temperature_C": "°C"
        }
      },
      "description": "Degree of crystallinity (fraction) at selected temperatures between 0°C and 212°C for the two samples."
    }
  ],
  "notes": "All values are computed from the provided specific heat data and the literature pure‑crystal heat of fusion; tolerances accommodate small numerical integration differences."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s artifact by comparing your computed values to expected results derived from the original study. The verifier reads `heats_of_fusion.csv` and `crystallinity_vs_temperature.csv`, checks that they conform to the specified schema, and compares the reported numbers against hidden reference values using appropriate tolerances. The contributions from these two scored artifacts are combined into a single final reward. Reporting numbers that do not result from a correct implementation of the described computational procedure will not match the hidden expectations.
