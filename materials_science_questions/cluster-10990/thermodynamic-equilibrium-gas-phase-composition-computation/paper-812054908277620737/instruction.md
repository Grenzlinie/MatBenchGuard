# Equilibrium Partial Pressure Computation for Oxynitride Decomposition Reactions

## Problem background
Oxynitride glasses in the Si-Y-Al-O-N system can lose transparency and develop dark coloration when melted at high temperatures. This degradation has been linked to the formation of silicon precipitates resulting from thermal decomposition reactions between oxide and nitride components during melting. A quantitative understanding of the gas-phase products of these decomposition reactions—particularly the equilibrium partial pressures of SiO(g), O₂(g), N₂(g), and Al₂O(g)—is essential to explain the observed behavior and to guide processing strategies such as changes in batch composition or nitrogen overpressure. This task addresses the thermodynamic analysis of six candidate decomposition reactions in the Al-Si-N-O subsystem. The goal is to compute the equilibrium partial pressures of the dominant vapor species from these reactions as functions of temperature and N₂ pressure, using standard thermochemical data, and thereby to determine the relative decomposition propensities and the effectiveness of nitrogen pressure in suppressing decomposition.

## Approach
The analysis relies on the equilibrium thermodynamic relationships for the following six high-temperature reactions (condensed phases are solid unless noted: Si(l) denotes liquid silicon):

1) SiO₂(s) = Si(l) + O₂(g)
2) SiO₂(s) = SiO(g) + ½ O₂(g)
3) Si₃N₄(s) + SiO₂(s) = 2 SiO(g) + 2 Si(l) + 2 N₂(g)
4) Si₃N₄(s) + Al₂O₃(s) = 3 SiO(g) + 2 AlN(s) + N₂(g)
5) Si₃N₄(s) + 3 SiO₂(s) = 6 SiO(g) + 2 N₂(g)
6) 2 AlN(s) + SiO₂(s) = SiO(g) + Al₂O(g) + N₂(g)

For each reaction, the standard Gibbs free energy change ΔG°(T) is obtained from the JANAF Thermochemical Tables over the temperature range 300–2000 K. The equilibrium constant is computed as K(T) = exp(–ΔG°(T)/RT). Under the assumption that all condensed phases are in their standard states (unit activity), and that N₂(g), when involved, is present at the specified pressure, the equilibrium partial pressures of the other gaseous species are derived from K(T) and the reaction stoichiometry. This calculation is performed:

- For all six reactions, at temperatures from 1400 K to 2000 K (at least seven equally spaced points) at a fixed N₂ pressure of 101.3 kPa.
- For reactions (3)–(6), at a fixed temperature of 2000 K while the N₂ pressure is varied over the range 0.1–10 MPa (at least five points).

The results are the equilibrium partial pressures (in bar) and their base-10 logarithms, stored in two CSV files. These data enable a comparison of how the partial pressure of SiO(g), the main decomposition product, differs among reactions and how it responds to increasing N₂ pressure.

## Reproduction target
Produce two CSV files:

- step_01_partial_pressures_vs_T.csv: for each of the six reactions, the equilibrium partial pressure (bar) and log10(partial pressure) of every gaseous species, evaluated at a fixed N₂ pressure of 101.3 kPa for at least seven equally spaced temperatures between 1400 K and 2000 K.
- step_02_partial_pressures_vs_PN2.csv: for reactions (3)–(6) only, the same quantities evaluated at 2000 K for at least five N₂ pressures ranging from 0.1 MPa to 10 MPa.

The values must be computed from the JANAF thermochemical data using the equilibrium-constant method, with the assumption that all condensed phases are at unit activity. The objective is to correctly compute the partial pressures so that they accurately reflect the thermodynamics of the given reactions under the specified conditions.

## Assets

- JANAF Thermochemical Tables: https://janaf.nist.gov/
- Python scientific computing packages: numpy scipy pandas

## Workflow steps

### Step 1: Obtain thermochemical data
- Role: process
- Action: Retrieve standard Gibbs free energy values for all relevant species (SiO₂(s), Si(l), O₂(g), SiO(g), Si₃N₄(s), Al₂O₃(s), AlN(s), Al₂O(g)) from the JANAF Thermochemical Tables (2nd edition or equivalent) covering the temperature range 300 K – 2000 K. Store the data in a structured format (e.g., JSON) for subsequent equilibrium calculations.
- Evidence: `/app/outputs/thermo_data.json`

### Step 2: Compute partial pressures vs temperature
- Role: scored (load-bearing)
- Action: For each of the six decomposition reactions (oxide‑nitride reactions), compute the equilibrium constant K(T) from the standard Gibbs free energy change (ΔG° = –RT ln K) using the thermochemical data obtained in step 0. Derive the equilibrium partial pressures of all gaseous species, assuming unit activity for pure condensed phases and a fixed total N₂ pressure of 101.3 kPa. For reactions where N₂ is a participant, treat its partial pressure as the fixed background; for others, N₂ may be absent. Evaluate at least seven equally spaced temperatures from 1400 K to 2000 K. Output the log10 (base 10) of each partial pressure in units of bar.
- Output file: `/app/outputs/step_01_partial_pressures_vs_T.csv`
- Format: csv
- Contract: CSV file with columns: reaction_id (integer, 1–6), temperature_K (integer), formula (string, the gas species formula), partial_pressure_bar (float, units bar), log10_partial_pressure (float). One row per reaction per temperature point.
- Scoring: scored by hidden verifier

### Step 3: Compute partial pressures vs N2 pressure
- Role: scored (load-bearing)
- Action: For reactions (3) through (6), recompute equilibrium partial pressures at a fixed temperature of 2000 K using the same thermochemical data and unit‑activity assumption, varying the N₂ pressure over the range 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0 MPa (or close approximations). Output the log10 (base 10) of each partial pressure in units of bar as a function of N₂ pressure.
- Output file: `/app/outputs/step_02_partial_pressures_vs_PN2.csv`
- Format: csv
- Contract: CSV file with columns: reaction_id (integer, 3–6), N2_pressure_MPa (float), formula (string, the gas species formula), partial_pressure_bar (float, units bar), log10_partial_pressure (float). One row per reaction per N₂ pressure point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_partial_pressures_vs_T.csv`
- `/app/outputs/step_02_partial_pressures_vs_PN2.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_partial_pressures_vs_T.csv
- path: `/app/outputs/step_01_partial_pressures_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Partial pressures of vapor species from the six decomposition reactions at P_N₂=101.3 kPa over 1400–2000 K. The hidden checker will recompute reference values from the same JANAF data and verify the agent’s log10 values with tolerance, as well as check structural trends (e.g., relative ordering of SiO(g) from different reactions).
- schema:
  - `type`: table
  - `required_columns`: `reaction_id`, `temperature_K`, `formula`, `partial_pressure_bar`, `log10_partial_pressure`
  - `units`:
    - `partial_pressure_bar`: bar
    - `temperature_K`: K

### step_02_partial_pressures_vs_PN2.csv
- path: `/app/outputs/step_02_partial_pressures_vs_PN2.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Partial pressures of vapor species for reactions (3)–(6) at 2000 K as a function of N₂ pressure (0.1–10 MPa). The checker will recompute reference values and verify that increasing N₂ pressure produces the expected trends (e.g., a >1 order-of-magnitude drop for reactions (5) and (6), modest change for (3) and (4)).
- schema:
  - `type`: table
  - `required_columns`: `reaction_id`, `N2_pressure_MPa`, `formula`, `partial_pressure_bar`, `log10_partial_pressure`
  - `units`:
    - `partial_pressure_bar`: bar
    - `N2_pressure_MPa`: MPa

Notes: Both CSV outputs will be scored by recomputing the equilibrium partial pressures from the same JANAF reference data and comparing the agent’s log10 values with an appropriate tolerance; structural trends (relative ordering among reactions, effect of N₂ pressure) are also part of the verification. The use of JANAF data ensures the reference is well-defined and public.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_partial_pressures_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction_id",
          "temperature_K",
          "formula",
          "partial_pressure_bar",
          "log10_partial_pressure"
        ],
        "units": {
          "partial_pressure_bar": "bar",
          "temperature_K": "K"
        }
      },
      "description": "Partial pressures of vapor species from the six decomposition reactions at P_N₂=101.3 kPa over 1400–2000 K. The hidden checker will recompute reference values from the same JANAF data and verify the agent’s log10 values with tolerance, as well as check structural trends (e.g., relative ordering of SiO(g) from different reactions)."
    },
    {
      "file": "step_02_partial_pressures_vs_PN2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction_id",
          "N2_pressure_MPa",
          "formula",
          "partial_pressure_bar",
          "log10_partial_pressure"
        ],
        "units": {
          "partial_pressure_bar": "bar",
          "N2_pressure_MPa": "MPa"
        }
      },
      "description": "Partial pressures of vapor species for reactions (3)–(6) at 2000 K as a function of N₂ pressure (0.1–10 MPa). The checker will recompute reference values and verify that increasing N₂ pressure produces the expected trends (e.g., a >1 order-of-magnitude drop for reactions (5) and (6), modest change for (3) and (4))."
    }
  ],
  "notes": "Both CSV outputs will be scored by recomputing the equilibrium partial pressures from the same JANAF reference data and comparing the agent’s log10 values with an appropriate tolerance; structural trends (relative ordering among reactions, effect of N₂ pressure) are also part of the verification. The use of JANAF data ensures the reference is well-defined and public."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently recomputes the equilibrium partial pressures from the same JANAF reference data and compares your reported values with the reference calculations. For each CSV file, the verifier will compare your log10(partial pressure) values at selected temperature and pressure points with a tolerance that accounts for minor variations arising from data edition differences or implementation details. Additionally, the verifier will perform structural checks on your dataset: for instance, it will examine the relative ordering of SiO(g) partial pressures from different reactions under the same conditions and verify that the computed pressure changes with varying N₂ pressure are consistent with the thermodynamic relations. The final reward is a weighted combination of these point-value comparisons (approximately 60%) and structural checks (approximately 40%). Simply reporting the paper’s published numbers without executing the equilibrium calculation will not be sufficient; the verifier will detect whether your output reflects a genuine thermodynamic analysis.
