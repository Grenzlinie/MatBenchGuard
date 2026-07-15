# Gas-phase equilibrium composition from Knudsen effusion data and thermochemical literature

## Problem background
Ytterbium(III) oxide selenide, (YbO)₂Se, is a compound belonging to the family of lanthanoid oxide selenides. Structural and spectroscopic properties of this material have been characterised, but no thermochemical data are available for (YbO)₂Se or related phases. When heated, (YbO)₂Se decomposes incongruently into solid Yb₂O₃ and a gas phase that contains ytterbium and selenium atoms and possibly diatomic or molecular species. The present task reproduces a thermochemical analysis that uses Knudsen effusion mass‑loss measurements and literature free‑energy functions to determine the dominant decomposition reaction and to extract its enthalpy, entropy, and the standard enthalpy of formation of (YbO)₂Se(s).

## Approach
The analysis combines the Knudsen effusion equation, which relates the mass‑loss rate of each gaseous species to its partial pressure, with the known dissociation equilibria for YbSe(g) ⇌ Yb(g) + Se(g) and Se₂(g) ⇌ 2 Se(g). The equilibrium constants for the dissociation reactions are obtained from the supplied free‑energy functions and dissociation enthalpies. Together with a mass‑balance constraint derived from the overall decomposition stoichiometry, these relations form a cubic equation for one of the unknown partial pressures. Solving this equation at every experimental temperature gives the individual partial pressures of Yb(g), Se(g), YbSe(g), and Se₂(g).

From those partial pressures the equilibrium constant K for the overall decomposition reaction

(YbO)₂Se(s) → ⅓ Yb₂O₃(s) + ⅔ Yb(g) + Se(g)

is calculated at each temperature. A subsequent unweighted linear least‑squares fit of log₁₀ K versus 1 / T yields the vapour‑pressure equation. Using estimated heat‑capacity and entropy increments for (YbO)₂Se(s)—obtained by additive combination of known thermodynamic data for Yb₂O₃ and relevant selenides—the reaction enthalpy and entropy are extrapolated to 298 K by both second‑law and third‑law methods. Finally, the standard enthalpy of formation of (YbO)₂Se(s) is derived from the second‑law decomposition enthalpy and the provided standard enthalpies of formation of Yb₂O₃(s), Yb(g), and Se(g).

All required numerical input data—the effusion rates, orifice areas, free‑energy functions, dissociation enthalpies, thermodynamic increments, and standard formation enthalpies—are listed directly in these instructions. The agent must implement the cubic‑equation solver, the linear regression, and the thermodynamic extrapolations in code; no external data fetch is necessary.

## Reproduction target
Using the provided Knudsen effusion mass‑loss rates (30 data points covering 1753–1997 K, orifice area, and molar masses) and the supplied free‑energy functions, dissociation enthalpies, and standard enthalpies of formation, compute:

- The individual partial pressures of Yb(g), Se(g), YbSe(g), and Se₂(g) at each experimental temperature.
- The equilibrium constant K for the decomposition reaction (YbO)₂Se(s) → ⅓ Yb₂O₃(s) + ⅔ Yb(g) + Se(g) at each temperature.
- A vapour‑pressure equation log₁₀ K = A + B / T via an unweighted linear least‑squares fit.
- The second‑law enthalpy ΔH°₂₉₈(II) and entropy ΔS°₂₉₈(II), and the third‑law enthalpy ΔH°₂₉₈(III) and entropy ΔS°₂₉₈(III) for that reaction, extrapolated to 298 K using the provided thermodynamic increment data.
- The standard enthalpy of formation ΔH°_{f,298} of (YbO)₂Se(s).

Produce two output files:
- `/app/outputs/processed_tables.csv` – a table with columns: T_K, rate_mgh, p_Yb_bar, p_Se_bar, p_YbSe_bar, p_Se2_bar, K, deltaH_III_kJmol.
- `/app/outputs/results.json` – a JSON object with the keys: logK_slope, logK_intercept, deltaH_II_kJmol, deltaS_II_JmolK, deltaH_III_kJmol, deltaS_III_JmolK, deltaH_f_formation_kJmol.

## Assets

- Mills, Thermodynamic Data for Inorganic Sulphides, Selenides and Tellurides (1974)
- Hultgren et al., Selected Values of Thermodynamic Properties of Metals and Alloys (1963)
- Pankratz and King, U.S. Bur. Mines Rep. Invest. No. 6175 (1963)
- Holley et al., Prog. Sci. Technol. Rare Earths 3 (1968)
- Standard enthalpies of formation (Yb₂O₃, Yb(g), Se(g))

## Workflow steps

### Step 1: Compute partial pressures, equilibrium constant K, and third-law enthalpies
- Role: scored (load-bearing)
- Action: Using the provided Knudsen effusion mass‑loss rates (temperature, orifice area, mass‑loss temporal rate, molar masses) and the supplied free‑energy functions and dissociation enthalpies, set up and solve the cubic equation to obtain the individual partial pressures of Yb(g), Se(g), YbSe(g), and Se₂(g). From these, compute the equilibrium constant K for reaction (2) at every temperature, and derive the per‑temperature third‑law enthalpy ΔH°₂₉₈(III). Write the full table (columns: T_K, rate_mgh, p_Yb_bar, p_Se_bar, p_YbSe_bar, p_Se2_bar, K, deltaH_III_kJmol) to processed_tables.csv.
- Output file: `/app/outputs/processed_tables.csv`
- Format: csv
- Contract: Columns: T_K (float), rate_mgh (float), p_Yb_bar (float), p_Se_bar (float), p_YbSe_bar (float), p_Se2_bar (float), K (float), deltaH_III_kJmol (float).
- Scoring: scored by hidden verifier

### Step 2: Compute vapour‑pressure equation, second‑/third‑law parameters, and enthalpy of formation
- Role: scored
- Action: From the K values across all temperatures, perform an unweighted linear least‑squares fit of log₁₀(K) vs 1/T to obtain the vapour‑pressure equation coefficients. Derive the second‑law enthalpy ΔH°₂₉₈(II) and entropy ΔS°₂₉₈(II) by extrapolation using the estimated thermodynamic increments for (YbO)₂Se(s) (additivity of Yb₂O₃ and La₂Se₃ heat capacities and entropies). Compute the mean third‑law enthalpy and the corresponding entropy. Finally, calculate the standard enthalpy of formation of (YbO)₂Se(s) from ΔH°₂₉₈(II) and the provided standard enthalpies of formation of Yb₂O₃(s), Yb(g), and Se(g). Write all parameters to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with fields: logK_slope (float), logK_intercept (float), deltaH_II_kJmol (float), deltaS_II_JmolK (float), deltaH_III_kJmol (float), deltaS_III_JmolK (float), deltaH_f_formation_kJmol (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/processed_tables.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### processed_tables.csv
- path: `/app/outputs/processed_tables.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table with partial pressures, equilibrium constants, and third-law enthalpies for each temperature. The hidden reference values are recomputed from the same input data.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `rate_mgh`, `p_Yb_bar`, `p_Se_bar`, `p_YbSe_bar`, `p_Se2_bar`, `K`, `deltaH_III_kJmol`

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Headline thermodynamic parameters obtained from the linear regression and extrapolation. The hidden reference values are recomputed from the same input data.
- schema:
  - `type`: object
  - `required`:
    - `logK_slope`: float
    - `logK_intercept`: float
    - `deltaH_II_kJmol`: float
    - `deltaS_II_JmolK`: float
    - `deltaH_III_kJmol`: float
    - `deltaS_III_JmolK`: float
    - `deltaH_f_formation_kJmol`: float

Notes: The agent must implement the cubic-equation solver and the linear-extrapolation procedure. All necessary thermochemical data are provided in the task instructions. The checker independently recomputes the quantities and compares the agent's output against the hidden reference values within predefined tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "processed_tables.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "rate_mgh",
          "p_Yb_bar",
          "p_Se_bar",
          "p_YbSe_bar",
          "p_Se2_bar",
          "K",
          "deltaH_III_kJmol"
        ]
      },
      "description": "Table with partial pressures, equilibrium constants, and third-law enthalpies for each temperature. The hidden reference values are recomputed from the same input data."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "logK_slope": "float",
          "logK_intercept": "float",
          "deltaH_II_kJmol": "float",
          "deltaS_II_JmolK": "float",
          "deltaH_III_kJmol": "float",
          "deltaS_III_JmolK": "float",
          "deltaH_f_formation_kJmol": "float"
        }
      },
      "description": "Headline thermodynamic parameters obtained from the linear regression and extrapolation. The hidden reference values are recomputed from the same input data."
    }
  ],
  "notes": "The agent must implement the cubic-equation solver and the linear-extrapolation procedure. All necessary thermochemical data are provided in the task instructions. The checker independently recomputes the quantities and compares the agent's output against the hidden reference values within predefined tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently recomputes every scored quantity from the same input data and algorithm that you are given. The verifier reads your processed_tables.csv and results.json and compares them against its own recomputed reference values. Your reward is a weighted combination of the accuracy of the partial‑pressure table (40 %), the second‑law and third‑law thermodynamic parameters (30 %), the standard enthalpy of formation (20 %), and a structural check (10 %) that confirms the molecular species YbSe and Se₂ together contribute only a tiny fraction of the total pressure across all temperatures.

The verifier uses tolerance windows that account for the small numerical differences expected when different implementations of the cubic‑equation solver and linear regression are used. Simply reproducing a number that matches a literature report is not sufficient; the verifier recomputes everything from your raw outputs. You must therefore write code that correctly implements the thermochemical procedure described in the workflow steps.
