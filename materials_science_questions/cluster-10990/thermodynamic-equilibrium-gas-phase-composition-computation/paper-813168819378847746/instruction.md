# Two-Zone Vapor-Equilibration: Compute Te(g) Partial Pressure and Activity

## Problem background
Tellurium is added to steel to promote machinability; understanding its solubility and thermodynamic activity in γ‑iron is essential for process control. A two‑zone vapor‑equilibration furnace is used to equilibrate tellurium vapour with pure iron foils. Liquid tellurium held at a lower temperature generates a mixture of Te(g) and Te₂(g) vapour at a known total pressure. This vapour rises to a hotter zone containing an iron foil, where the equilibrium partial pressures of the vapour species are determined by the foil temperature and the fixed total pressure. Knowledge of the two temperatures allows the calculation of the partial pressure of monatomic tellurium, p_Te(g), and the tellurium activity a_Te(l) relative to liquid tellurium, using public thermochemical data. This task focuses on the computational core: given a set of temperature pairs (T_Te, T_Fe), compute the equilibrium partial pressure of Te(g) and the activity a_Te(l) at the foil temperature.

## Approach
The calculation uses publicly available standard Gibbs free energy functions for Te(g) and Te₂(g) from the NIST‑JANAF Thermochemical Tables. From these functions, compute the equilibrium constants K₁(T) for the reaction Te(l) = Te(g) and K₃(T) for Te₂(g) = 2Te(g) at the required temperatures. At the lower tellurium‑pool temperature T_Te, the vapour is in equilibrium with liquid tellurium, so the partial pressures p_Te and p_Te₂ must satisfy the two equilibrium conditions and sum to the total pressure P = p_Te + p_Te₂. Solve this system to obtain p_Te, p_Te₂, and P at T_Te. At the upper foil temperature T_Fe, the total pressure P remains unchanged, but the equilibrium constant K₃(T_Fe) changes; solve the system p_Te + p_Te₂ = P and p_Te₂ = p_Te² / K₃(T_Fe) to find p_Te(g) and p_Te₂(g) at T_Fe. Finally, the tellurium activity with respect to the liquid reference state is a_Te(l) = p_Te(g) / K₁(T_Fe).

## Reproduction target
Compute p_Te(g) and a_Te(l) for each of the following 19 temperature pairs (T_Fe, T_Te in Kelvin):

(1273, 798), (1273, 798), (1273, 798), (1273, 798), (1273, 798),
(1373, 798),
(1423, 798),
(1498, 798),
(1498, 873), (1498, 873),
(1498, 923), (1498, 923), (1498, 923), (1498, 923),
(1498, 973),
(1548, 973),
(1548, 1023),
(1548, 1073), (1548, 1073).

Produce a single CSV file named `te_activity_results.csv` with the header:
`T_Fe_K,T_Te_K,p_Te_g_atm,a_Te_l_dimensionless`
Each of the 19 rows must contain the input temperatures and the computed p_Te(g) (in atm) and a_Te(l) (dimensionless) for that pair, ordered as listed.

## Assets

- NIST-JANAF Thermochemical Tables (Te gas species): https://janaf.nist.gov/
- Python scientific computing stack: numpy scipy pandas

## Workflow steps

### Step 1: Compute Te(g) partial pressure and activity
- Role: scored (load-bearing)
- Action: Using the 19 temperature pairs (T_Te, T_Fe) provided in the instruction, compute the equilibrium partial pressure of monatomic tellurium Te(g) and the tellurium activity a_Te(l) at the foil temperature from public NIST-JANAF thermochemical data. Obtain standard Gibbs free energy functions for Te(g) and Te2(g). Compute equilibrium constants K1 for Te(l)=Te(g) and K3 for Te2(g)=2Te(g) at each temperature. At T_Te, solve for partial pressures p_Te and p_Te2 that are in equilibrium with liquid Te and consistent with the total pressure P = p_Te + p_Te2. Then at T_Fe, using the same total pressure P and K3(T_Fe), determine p_Te(g) and p_Te2(g). Finally compute a_Te(l) = p_Te(g) / K1(T_Fe).
- Output file: `/app/outputs/te_activity_results.csv`
- Format: csv
- Contract: Header row: T_Fe_K,T_Te_K,p_Te_g_atm,a_Te_l_dimensionless. 19 data rows, comma-separated, floating-point numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/te_activity_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### te_activity_results.csv
- path: `/app/outputs/te_activity_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium partial pressure of Te(g) and tellurium activity a_Te(l) for each of the 19 temperature pairs, computed from NIST-JANAF data.
- schema:
  - `type`: table
  - `required_columns`: `T_Fe_K`, `T_Te_K`, `p_Te_g_atm`, `a_Te_l_dimensionless`
  - `items`: object
  - `units`:
    - `T_Fe_K`: K
    - `T_Te_K`: K
    - `p_Te_g_atm`: atm
    - `a_Te_l_dimensionless`: dimensionless

Notes: The checker compares p_Te_g_atm and a_Te_l_dimensionless to hidden gold values derived from the paper's Table II using a relative tolerance of 10%.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "te_activity_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_Fe_K",
          "T_Te_K",
          "p_Te_g_atm",
          "a_Te_l_dimensionless"
        ],
        "items": {},
        "units": {
          "T_Fe_K": "K",
          "T_Te_K": "K",
          "p_Te_g_atm": "atm",
          "a_Te_l_dimensionless": "dimensionless"
        }
      },
      "description": "Equilibrium partial pressure of Te(g) and tellurium activity a_Te(l) for each of the 19 temperature pairs, computed from NIST-JANAF data."
    }
  ],
  "notes": "The checker compares p_Te_g_atm and a_Te_l_dimensionless to hidden gold values derived from the paper's Table II using a relative tolerance of 10%."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads `te_activity_results.csv`. The verifier compares each row's computed p_Te_g_atm and a_Te_l_dimensionless to corresponding reference values (derived from the same thermodynamic calculation using NIST‑JANAF data). For each row, both quantities must fall within a predefined relative tolerance to be considered correct. The final reward is the fraction of rows (out of 19) where both p_Te(g) and a_Te(l) are correct. If the file has the wrong number of rows, or the temperature pairs do not match the expected set, the reward is zero. Simply reporting the paper's published numbers is not sufficient; you must demonstrate the correct computation.
