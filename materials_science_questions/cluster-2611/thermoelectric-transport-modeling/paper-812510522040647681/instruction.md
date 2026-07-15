# Compute Cation Distribution from Seebeck Coefficients using Heikes Model

## Problem background
Nickel manganite (NiMn₂O₄) is the leading material for negative temperature coefficient (NTC) thermistors. Its electrical properties are governed by a hopping mechanism between Mn³⁺ and Mn⁴⁺ ions on octahedral B‑sites of the spinel structure. The cation distribution—which describes how Ni²⁺, Mn²⁺, Mn³⁺, and Mn⁴⁺ occupy tetrahedral A‑sites and octahedral B‑sites—depends on temperature and on the sample's thermal history. Because the Seebeck coefficient S(T) is sensitive to the ratio of charge carriers on the B‑sites, high‑temperature thermopower measurements can be used to back‑calculate that ratio and, in turn, to infer the cation distribution. This task requires computing the temperature‑dependent [Mn_B⁴⁺]/[Mn_B³⁺] ratio and an effective cation exchange parameter p' for a slow‑cooled NiMn₂O₄ sample from a set of provided Seebeck coefficients, using the modified Heikes formula under two different electronic degeneracy scenarios.

## Approach
The core idea is to invert the modified Heikes formula that relates the Seebeck coefficient S to the carrier concentration c = [Mn_B⁴⁺] / ([Mn_B³⁺] + [Mn_B⁴⁺]). Because the charge carriers are small polarons, spin and orbital degeneracies of the participating Mn ions must be considered. The formula is S = −(k_B/e) · ln[(g_e/g_h) · (1−c)/c], where k_B is the Boltzmann constant and e the elementary charge. The degeneracy ratio g_e/g_h takes two values in the analysis: 5/4 (assuming Jahn–Teller lifting of orbital degeneracy for Mn³⁺) and 10/4 (assuming orbital degeneracy is preserved). For each temperature, the approach is: (1) solve the Heikes equation for c, (2) compute the ratio [Mn_B⁴⁺]/[Mn_B³⁺] = c/(1−c), (3) derive the effective parameter p' = 2c/(1+2c), and (4) obtain the site occupancies from the spinel formula assuming the inversion parameter ν equals p' (i.e., ν = p = p'): Ni_A = 1−p', Mn_A = p', Ni_B = p', Mn_B³⁺ = 2−2p', Mn_B⁴⁺ = p'. The procedure must be repeated independently for both degeneracy ratios, yielding two tables that document the evolution of the cation distribution with temperature.

## Reproduction target
The Seebeck coefficient values (μV/K) for sample SC900 are:
- At 110 °C: -173.4
- At 210 °C: -143.8
- At 395 °C: -97.2 (for degeneracy 5/4) or -97.3 (for degeneracy 10/4)
- At 595 °C: -17.8
- At 795 °C: 14.7
- At 860 °C: 19.5

Given these values, perform the following: (a) using degeneracy ratio g_e/g_h = 5/4, compute and record the [Mn_B⁴⁺]/[Mn_B³⁺] ratio, the effective cation exchange parameter p', and the full site occupancy columns (Ni_A, Mn_A, Ni_B, Mn_B³⁺, Mn_B⁴⁺) in a CSV file; (b) repeat the same computation using degeneracy ratio g_e/g_h = 10/4 and write the results to a second CSV file. The goal is to produce two self‑consistent tables that capture the temperature‑dependent cation distribution as derived from the thermopower data.

## Assets

- Python scientific libraries: numpy, pandas

## Workflow steps

### Step 1: Compute cation distribution for degeneracy 5/4
- Role: scored
- Action: Use the provided Seebeck coefficient values (μV/K) at the six temperatures 110, 210, 395, 595, 795, 860 °C. For each temperature, compute the carrier concentration c = [MnB4+]/([MnB3+]+[MnB4+]) from the modified Heikes formula S = -(kB/e)*ln((5/4)*(1-c)/c) using Boltzmann constant kB = 1.380649e-23 J/K and elementary charge e = 1.602176634e-19 C. Then compute the ratio [MnB4+]/[MnB3+] = c/(1-c), effective p' = 2c/(1+2c), and the site occupancies under the assumption ν=p=p' according to the spinel cation distribution formula: Ni_A = 1-p', Mn_A = p', Ni_B = p', Mn_B3+ = 2-2p', Mn_B4+ = p'. Write the results as table_degeneracy_5_4.csv.
- Output file: `/app/outputs/table_degeneracy_5_4.csv`
- Format: csv
- Contract: Columns: Temperature_C (integer), Seebeck_uVK (float), MnB4_MnB3_ratio (float), p_prime (float), Ni_A (float), Mn_A (float), Ni_B (float), Mn_B3 (float), Mn_B4 (float). All numeric values use decimal point.
- Scoring: scored by hidden verifier

### Step 2: Compute cation distribution for degeneracy 10/4
- Role: scored
- Action: Repeat the same computation using the degeneracy ratio ge/gh = 10/4. For each temperature, use the modified Heikes formula S = -(kB/e)*ln((10/4)*(1-c)/c) with the same kB and e. Compute c, ratio, p', and site occupancies as before. Write the results as table_degeneracy_10_4.csv.
- Output file: `/app/outputs/table_degeneracy_10_4.csv`
- Format: csv
- Contract: Columns: Temperature_C (integer), Seebeck_uVK (float), MnB4_MnB3_ratio (float), p_prime (float), Ni_A (float), Mn_A (float), Ni_B (float), Mn_B3 (float), Mn_B4 (float). All numeric values use decimal point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_degeneracy_5_4.csv`
- `/app/outputs/table_degeneracy_10_4.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_degeneracy_5_4.csv
- path: `/app/outputs/table_degeneracy_5_4.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of cation distribution for the SC900 sample computed under degeneracy ratio 5/4. The Seebeck_uVK column must match the provided input values exactly; the remaining columns must be self-consistent and follow the modified Heikes formula and spinel distribution formula.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_C`, `Seebeck_uVK`, `MnB4_MnB3_ratio`, `p_prime`, `Ni_A`, `Mn_A`, `Ni_B`, `Mn_B3`, `Mn_B4`
  - `units`:
    - `Temperature_C`: °C
    - `Seebeck_uVK`: μV/K
    - `MnB4_MnB3_ratio`: dimensionless
    - `p_prime`: dimensionless
    - `Ni_A`: dimensionless (occupancy)
    - `Mn_A`: dimensionless (occupancy)
    - `Ni_B`: dimensionless (occupancy)
    - `Mn_B3`: dimensionless (occupancy)
    - `Mn_B4`: dimensionless (occupancy)

### table_degeneracy_10_4.csv
- path: `/app/outputs/table_degeneracy_10_4.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of cation distribution for the SC900 sample computed under degeneracy ratio 10/4. The Seebeck_uVK column must match the provided input values exactly; the remaining columns must be self-consistent and follow the modified Heikes formula and spinel distribution formula.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_C`, `Seebeck_uVK`, `MnB4_MnB3_ratio`, `p_prime`, `Ni_A`, `Mn_A`, `Ni_B`, `Mn_B3`, `Mn_B4`
  - `units`:
    - `Temperature_C`: °C
    - `Seebeck_uVK`: μV/K
    - `MnB4_MnB3_ratio`: dimensionless
    - `p_prime`: dimensionless
    - `Ni_A`: dimensionless (occupancy)
    - `Mn_A`: dimensionless (occupancy)
    - `Ni_B`: dimensionless (occupancy)
    - `Mn_B3`: dimensionless (occupancy)
    - `Mn_B4`: dimensionless (occupancy)

Notes: The solving agent is provided the six Seebeck coefficient values and the physical constants (kB, e) in the instruction. The tables must be computed algorithmically from those inputs; no external lookup of published values is allowed. The checker will verify both the internal consistency between ratio, p', and occupancies, and compare the computed ratio and p' columns to hidden reference values within appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_degeneracy_5_4.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_C",
          "Seebeck_uVK",
          "MnB4_MnB3_ratio",
          "p_prime",
          "Ni_A",
          "Mn_A",
          "Ni_B",
          "Mn_B3",
          "Mn_B4"
        ],
        "units": {
          "Temperature_C": "°C",
          "Seebeck_uVK": "μV/K",
          "MnB4_MnB3_ratio": "dimensionless",
          "p_prime": "dimensionless",
          "Ni_A": "dimensionless (occupancy)",
          "Mn_A": "dimensionless (occupancy)",
          "Ni_B": "dimensionless (occupancy)",
          "Mn_B3": "dimensionless (occupancy)",
          "Mn_B4": "dimensionless (occupancy)"
        }
      },
      "description": "Table of cation distribution for the SC900 sample computed under degeneracy ratio 5/4. The Seebeck_uVK column must match the provided input values exactly; the remaining columns must be self-consistent and follow the modified Heikes formula and spinel distribution formula."
    },
    {
      "file": "table_degeneracy_10_4.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_C",
          "Seebeck_uVK",
          "MnB4_MnB3_ratio",
          "p_prime",
          "Ni_A",
          "Mn_A",
          "Ni_B",
          "Mn_B3",
          "Mn_B4"
        ],
        "units": {
          "Temperature_C": "°C",
          "Seebeck_uVK": "μV/K",
          "MnB4_MnB3_ratio": "dimensionless",
          "p_prime": "dimensionless",
          "Ni_A": "dimensionless (occupancy)",
          "Mn_A": "dimensionless (occupancy)",
          "Ni_B": "dimensionless (occupancy)",
          "Mn_B3": "dimensionless (occupancy)",
          "Mn_B4": "dimensionless (occupancy)"
        }
      },
      "description": "Table of cation distribution for the SC900 sample computed under degeneracy ratio 10/4. The Seebeck_uVK column must match the provided input values exactly; the remaining columns must be self-consistent and follow the modified Heikes formula and spinel distribution formula."
    }
  ],
  "notes": "The solving agent is provided the six Seebeck coefficient values and the physical constants (kB, e) in the instruction. The tables must be computed algorithmically from those inputs; no external lookup of published values is allowed. The checker will verify both the internal consistency between ratio, p', and occupancies, and compare the computed ratio and p' columns to hidden reference values within appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads both CSV files and evaluates them against hidden reference values, without revealing those references to you. For each file, it checks: (i) that the Seebeck_uVK column exactly matches the provided input numbers; (ii) that the MnB4_MnB3_ratio and p_prime columns agree with the reference values within appropriate tolerances; and (iii) that the site occupancies are internally consistent with the Heikes formula and the spinel formula (i.e., p' = 2c/(1+2c) and the sum of A‑site occupancies equals 1, the sum of B‑site occupancies equals 1). Partial credit is given per temperature row for correct ratio and p'. The final reward is a weighted combination of these checks; simply stating numbers does not earn credit—your tables must follow from the provided Seebeck values and the prescribed formulas.
