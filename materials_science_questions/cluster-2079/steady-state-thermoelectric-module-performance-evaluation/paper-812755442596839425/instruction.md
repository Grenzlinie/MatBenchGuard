# Steady-state thermoelectric cooling analysis for 50-nm node CMOS package

## Problem background
Shrinking CMOS technology nodes lead to increasing power density and higher junction temperatures, raising the risk of thermal runaway. Thermoelectric coolers (TECs) can actively pump heat via the Peltier effect and offer a compact, solid-state cooling solution. This task investigates the steady-state thermal behaviour of a 50-nm node chip when integrated with a TEC module inside the package. The objective is to compute the resulting junction temperature, overall chip power, TEC power consumption, coefficient of performance, and the optimal TEC p-n couple counts for maximum efficiency and minimum power.

## Approach
This task implements an analytical electrothermal model for a CMOS package. The model consists of: (1) a temperature-dependent chip power model that captures dynamic and leakage power, (2) thermal resistance networks for a traditional flip-chip C4 package and a TEC-integrated package, (3) an equivalent thermal resistance for the active TEC derived from the Peltier effect, (4) a steady-state temperature solver based on the quadratic energy balance, and (5) optimization formulas for the number of p-n couples to maximize COP and minimize TEC power. The workflow computes all quantities for a 50-nm technology node with a specified CP1.4-125-0.06L TEC device at a fixed applied current of 2.5 A. The TEC-integrated package is compared against the C4 baseline.

## Reproduction target
Compute the steady-state junction temperature for both a traditional C4 package and the same chip integrated with a CP1.4-125-0.06L TEC device, the corresponding chip total powers, the TEC electrical power consumption, the coefficient of performance (COP), and the optimal numbers of p-n couples that maximize COP and minimize TEC power. All quantities are evaluated for a 50-nm technology node chip, with the TEC driven at a constant current of 2.5 A. The complete set of results must be saved as a single JSON file (`results.json`). The specific process conditions, material parameters, and device specifications are provided in the workflow steps.

## Assets
All necessary numerical parameters, formulas, and device specifications are embedded in the workflow steps; no external datasets, model weights, or proprietary files are required. The only software dependencies are Python with `numpy` and `scipy` for numerical computation.

## Workflow steps

### Step 1: Parameter extraction
- Role: process
- Action: Compute the temperature-dependent power model coefficients A, B, X from the 50-nm technology node parameters (Table I data) and deduce the TEC module Seebeck coefficient, electrical resistance, and thermal conductance from the CP1.4-125-0.06L device nominal characteristics.
- Evidence: none

### Step 2: Thermal resistance modeling
- Role: process
- Action: Compute thermal resistances for the cold plate, thermal paste, and heat sink. Derive the equivalent TEC thermal resistance R_TECs as a function of current and temperatures. Formulate junction-to-ambient thermal resistances for the C4 package and TEC-integrated package.
- Evidence: none

### Step 3: Steady-state temperature and power computation
- Role: process
- Action: For an applied TEC current of 2.5 A, solve the quadratic steady-state temperature equation for both the C4 and TEC-integrated packages. Compute the chip total power for each package using the temperature-dependent power model. Compute the TEC electrical power consumption.
- Evidence: none

### Step 4: COP and p-n couple optimization
- Role: process
- Action: Using the cold-side temperature from the TEC case at I=2.5 A, compute the COP. Determine the optimal numbers of p-n couples that maximize COP and minimize TEC power using the derived optimization formulas.
- Evidence: none

### Step 5: Final results aggregation
- Role: scored (load-bearing)
- Action: Assemble the computed quantities (steady-state temperatures, chip powers, TEC power, COP, optimal p-n couple counts) into a structured JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"T_steady_C4": number, "T_steady_TEC": number, "P_chip_C4": number, "P_chip_TEC": number, "P_TEC": number, "COP": number, "Npn_cop": integer, "Npn_P": integer}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file containing the computed steady-state junction temperature for C4 and TEC packages, chip total powers, TEC electrical power, coefficient of performance, and optimal p-n couple counts maximizing COP and minimizing TEC power, for a 50-nm technology node chip with CP1.4-125-0.06L TEC device at 2.5 A.
- schema:
  - `type`: object
  - `required`: `T_steady_C4`, `T_steady_TEC`, `P_chip_C4`, `P_chip_TEC`, `P_TEC`, `COP`, `Npn_cop`, `Npn_P`
  - `properties`:
    - `T_steady_C4`:
      - `type`: number
      - `unit`: °C
    - `T_steady_TEC`:
      - `type`: number
      - `unit`: °C
    - `P_chip_C4`:
      - `type`: number
      - `unit`: W
    - `P_chip_TEC`:
      - `type`: number
      - `unit`: W
    - `P_TEC`:
      - `type`: number
      - `unit`: W
    - `COP`:
      - `type`: number
    - `Npn_cop`:
      - `type`: integer
    - `Npn_P`:
      - `type`: integer

Notes: All quantities computed for the specified 50-nm node parameters, CP1.4-125-0.06L TEC device, and applied current 2.5 A. The ANSYS finite-element validation step is excluded per scope; no external datasets are required beyond the publicly available ITRS data and TEC datasheet values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "T_steady_C4",
          "T_steady_TEC",
          "P_chip_C4",
          "P_chip_TEC",
          "P_TEC",
          "COP",
          "Npn_cop",
          "Npn_P"
        ],
        "properties": {
          "T_steady_C4": {
            "type": "number",
            "unit": "°C"
          },
          "T_steady_TEC": {
            "type": "number",
            "unit": "°C"
          },
          "P_chip_C4": {
            "type": "number",
            "unit": "W"
          },
          "P_chip_TEC": {
            "type": "number",
            "unit": "W"
          },
          "P_TEC": {
            "type": "number",
            "unit": "W"
          },
          "COP": {
            "type": "number"
          },
          "Npn_cop": {
            "type": "integer"
          },
          "Npn_P": {
            "type": "integer"
          }
        }
      },
      "description": "JSON file containing the computed steady-state junction temperature for C4 and TEC packages, chip total powers, TEC electrical power, coefficient of performance, and optimal p-n couple counts maximizing COP and minimizing TEC power, for a 50-nm technology node chip with CP1.4-125-0.06L TEC device at 2.5 A."
    }
  ],
  "notes": "All quantities computed for the specified 50-nm node parameters, CP1.4-125-0.06L TEC device, and applied current 2.5 A. The ANSYS finite-element validation step is excluded per scope; no external datasets are required beyond the publicly available ITRS data and TEC datasheet values."
}
```

## How you are scored
A hidden verifier automatically scores your submission by reading `/app/outputs/results.json`. It compares every field (`T_steady_C4`, `T_steady_TEC`, `P_chip_C4`, `P_chip_TEC`, `P_TEC`, `COP`, `Npn_cop`, `Npn_P`) to independently determined reference values. The score is binary: you receive full credit (1.0) only if all values fall within predefined absolute tolerances; otherwise the score is 0.0. Your task is to compute every value from the provided model and parameters – reporting a predetermined number without running the full computation will not pass the tolerance check.
