# Equilibrium Sublimation Criterion for 37 Substances

## Problem background
The temperature at which a solid begins to sublime or decompose is a key kinetic parameter, yet its quantitative relationship with the activation energy (or enthalpy change) is not widely established. One hypothesis proposes that for equilibrium sublimation/evaporation reactions at a low fixed vapor pressure, the ratio of the sublimation temperature to the molar enthalpy of sublimation should be approximately constant across diverse substances. Computing this ratio from reliable thermochemical data and examining its variation provides a test of the equilibrium nature of solid decompositions and a potential predictive tool.

## Approach
From basic thermodynamics, for a sublimation reaction A(solid) → A(gas) at equilibrium partial pressure P_A, the temperature T_sub (K) is given by:
  T_sub = ΔH_T° / (ΔS_T° − R ln P_A)
where ΔH_T° (kJ mol⁻¹) is the standard enthalpy change, ΔS_T° (J mol⁻¹ K⁻¹) the standard entropy change, and R = 8.314 J mol⁻¹ K⁻¹. Setting P_A = 10⁻⁷ bar (a typical detection threshold), one can compute T_sub and the ratio T_sub/ΔH_T° (in K mol kJ⁻¹) for a set of well‑characterized substances. The spread of this ratio across species indicates how constant the relationship is.
In this task you will retrieve ΔH_T° and ΔS_T° for 37 sublimation/evaporation reactions from public thermochemical databases (NIST Chemistry WebBook or equivalent), compute T_sub and the ratio for each reaction, and then derive the sample mean and standard deviation of the ratio across the set.

## Reaction List

The following 37 sublimation/evaporation reactions, with their gas-phase stoichiometries, are to be processed:

| Reactant |
|----------|
| Ag |
| B |
| Be |
| Cd |
| Co |
| Cr |
| Cu |
| Fe |
| Mo |
| Ni |
| Pd |
| Pt |
| Rh |
| Ru |
| Si |
| Ti |
| W |
| Zn |
| 2I -> I2 |
| 2Te -> Te2 |
| KCl |
| KI |
| LiF |
| NaCl |
| BaF2 |
| BeF2 |
| CaF2 |
| HgBr2 |
| HgCl2 |
| HgI2 |
| H2O |
| MgF2 |
| SnCl2 |
| SrF2 |
| ThO2 |
| ZrO2 |
| 4P(white) -> P4 |

## Reproduction target
You must:
- For each of the 37 reactions specified in the workflow steps (a list of substance names and gas-phase stoichiometries), obtain the standard molar enthalpy change ΔH_T° (kJ mol⁻¹) and standard molar entropy change ΔS_T° (J mol⁻¹ K⁻¹) from a public thermochemical database.
- Compute the sublimation temperature T_sub (K) using the formula given above with P_A = 10⁻⁷ bar.
- Compute the ratio T_sub/ΔH_T° (K mol kJ⁻¹) for each substance.
- Write all per‑substance results to `/app/outputs/ratios.csv` (columns: reaction, deltaH_kJmol, deltaS_JmolK, T_sub_K, ratio).
- Compute the sample mean and sample standard deviation of the ratio from the CSV and write them as JSON (`/app/outputs/summary.json`) with keys "mean_ratio" and "std_ratio".

## Assets

- NIST Chemistry WebBook: https://webbook.nist.gov/chemistry/
- NASA polynomial database (Burcat): https://burcat.technion.ac.il/

## Workflow steps

### Step 1: Retrieve thermochemical data for 37 substances
- Role: process
- Action: For each of the 37 sublimation/evaporation reactions listed in the instruction, retrieve the standard molar enthalpy change ΔH_T° (kJ mol⁻¹) and standard molar entropy change ΔS_T° (J mol⁻¹ K⁻¹) from a public thermochemical database (e.g., NIST Chemistry WebBook). Store the collected values in a structured file named thermodata.json.
- Evidence: `/app/outputs/thermodata.json`

### Step 2: Compute per-substance T_sub and T_sub/ΔH_T° ratio
- Role: scored (load-bearing)
- Action: For each substance, compute the sublimation temperature T_sub (K) using the relation T_sub = ΔH_T° / (ΔS_T° - R ln(10^{-7})), with R = 8.314 J mol⁻¹ K⁻¹ and equilibrium partial pressure P_A = 10^{-7} bar. Then compute the ratio T_sub/ΔH_T° (in K mol kJ⁻¹, where ΔH_T° is expressed in kJ mol⁻¹). Write the results to a CSV file (ratios.csv).
- Output file: `/app/outputs/ratios.csv`
- Format: csv
- Contract: reaction (string), deltaH_kJmol (float), deltaS_JmolK (float), T_sub_K (float), ratio (float)
- Scoring: scored by hidden verifier

### Step 3: Compute summary statistics (mean and S.D.)
- Role: scored
- Action: From the per-substance ratios in ratios.csv, compute the sample mean and sample standard deviation of the ratio. Write the results to a JSON file (summary.json) with keys 'mean_ratio' and 'std_ratio'.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: {"mean_ratio": float, "std_ratio": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ratios.csv`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ratios.csv
- path: `/app/outputs/ratios.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-substance computed sublimation temperature and T_sub/ΔH_T° ratio.
- schema:
  - `type`: table
  - `required_columns`: `reaction`, `deltaH_kJmol`, `deltaS_JmolK`, `T_sub_K`, `ratio`

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Mean and standard deviation of the ratio computed from ratios.csv; checked for internal consistency.
- schema:
  - `type`: object
  - `required`:
    - `mean_ratio`: float
    - `std_ratio`: float

Notes: The main scoring recomputes the mean and standard deviation of the ratio from ratios.csv and compares to paper-reported gold values. The summary.json file is checked for consistency with the CSV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction",
          "deltaH_kJmol",
          "deltaS_JmolK",
          "T_sub_K",
          "ratio"
        ]
      },
      "description": "Per-substance computed sublimation temperature and T_sub/ΔH_T° ratio."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "mean_ratio": "float",
          "std_ratio": "float"
        }
      },
      "description": "Mean and standard deviation of the ratio computed from ratios.csv; checked for internal consistency."
    }
  ],
  "notes": "The main scoring recomputes the mean and standard deviation of the ratio from ratios.csv and compares to paper-reported gold values. The summary.json file is checked for consistency with the CSV."
}
```

## How you are scored
A hidden verifier independently reads your output files. It will:
- Recompute the mean and standard deviation of the ratio column from your `ratios.csv`.
- Check that your `summary.json` is internally consistent with the CSV values.
- Compare the statistics (and optionally the per‑substance ratios) against reference values derived from the paper, using tolerances that account for the use of standard‑temperature data versus temperature‑corrected data.
Each scored step contributes to your total reward, with the primary weight on the summary statistics. Reporting numbers alone without correct artifacts will receive low or zero credit.
