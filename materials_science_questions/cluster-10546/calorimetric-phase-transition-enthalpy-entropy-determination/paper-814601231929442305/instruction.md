# Transition Temperature Estimation from Polymorph Melting and Solubility Data

## Problem background
Polymorphs of a pharmaceutical compound can have different thermodynamic stabilities. In enantiotropic systems, the relative stability changes at a transition temperature (T_tr) below the melting point of the lower-melting form, and determining T_tr is essential for drug development. This task deals with three polymorphs (Form 1, Form A, Form B) of a model compound. You are given the following experimental data:

**Melting data (onset temperatures and heats of fusion):**
| Polymorph | T_m (°C) | ΔH_f (kJ/mol) |
|-----------|----------|---------------|
| Form 1    | 90.66    | 21.93         |
| Form A    | 120.74   | 39.74         |
| Form B    | 122.22   | 35.80         |

**Solubility data in water (mg/mL):**
| T (°C) | Form A | Form B |
|--------|--------|--------|
| 20     | 1.55   | 2.11   |
| 25     | 1.87   | 2.49   |
| 30     | 2.41   | 3.15   |
| 35     | 2.94   | 3.70   |
| 40     | 3.63   | 4.46   |
| 45     | 4.28   | 5.18   |
| 50     | 5.18   | 6.13   |

**Empirical constants for the configurational heat capacity difference (C_pConf):**
| Polymorph | k1 (J·K⁻¹·mol⁻¹) | k2 (J·K⁻²·mol⁻¹) | k3 (J·mol⁻¹) |
|-----------|-------------------|-------------------|--------------|
| Form A    | 550.7             | 0.6752            | 111189.5     |
| Form B    | 601.8             | 0.1902            | 114428.3     |

The Heat of Fusion Rule states: if the higher-melting polymorph also has the higher heat of fusion, the pair is enantiotropic (there exists a T_tr below the lower melting point); otherwise it is monotropic. Your goal is to classify the polymorphic relationships using this rule and then estimate T_tr for the enantiotropic pair (expected to be Form A and Form B) using several computational methods.

## Approach
The reproduction follows a two-stage computational pipeline. First, apply the Heat of Fusion Rule: using the given melting data, determine for each pair of polymorphs whether the relationship is monotropic or enantiotropic; this step confirms that Form A and Form B are enantiotropic. Second, compute T_tr for Form A ↔ Form B directly using the four methods described below, employing the provided solubility, melting, and empirical C_pConf constants (no fitting is required; the constants are already given).

(1) Solubility extrapolation: construct van't Hoff plots (ln solubility vs 1/T) from the given solubility data (in mg/mL). Since the solubility of two polymorphs is equal at T_tr, find the intersection temperature of the two extrapolated curves.

(2) Heat of transition (ΔH_tr) method: compute ΔH_tr as the difference between the heats of fusion of Form A and Form B. Then, for each temperature T0 in the solubility dataset, calculate T_tr using the relationship that involves ΔH_tr, the solubility ratio, and T0. Report the average of these estimates.

(3) Melting data method: using the onset melting temperatures and heats of fusion of Form A and Form B, compute T_tr with a formula that includes a heat capacity correction term. Assume the heat capacity correction constant is k = 0.003 K⁻¹.

(4) Configurational free energy (G_c) phase diagram method: for each form, compute G_c as a function of temperature using the melting data and the fitted C_pConf constants. Two approximations are used: (a) a linear C_pConf model that yields one expression for G_c(T) (equivalent to the paper's eq 21), and (b) a hyperbolic C_pConf model that yields a different expression (equivalent to eq 22). For each approximation, find the temperature at which the G_c curves of Form A and Form B intersect; this gives two T_tr values. All five T_tr values are collected into a single CSV file.

## Reproduction target
Produce a CSV file at `/app/outputs/transition_temperatures.csv` containing two columns: `method` (string) and `T_tr_C` (float, representing degrees Celsius). The file must have exactly five rows, with method labels:
  SolubilityExtrapolation
  DeltaHtr
  MeltingData
  GcPhase_eq19
  GcPhase_eq20
The five values are the transition temperatures obtained from the four methods (the Gc phase diagram method contributes two values, one for each C_pConf approximation). All values must be computed from the provided data and the described formulas; no external lookups or manual copying of results is allowed.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib
- Pandas: pandas

## Workflow steps

### Step 1: Apply Heat of Fusion Rule
- Role: process
- Action: Using the given melting data in the Problem background, determine the thermodynamic relationships (monotropic or enantiotropic) according to the Heat of Fusion Rule. Write a JSON file classification.json containing the pairwise classifications (e.g., {"Form1_vs_FormA":"monotropic", "Form1_vs_FormB":"monotropic", "FormA_vs_FormB":"enantiotropic"}).
- Evidence: `/app/outputs/classification.json`

### Step 2: Compute Transition Temperature Using Four Methods
- Role: scored (load-bearing)
- Action: Compute the transition temperature T_tr between Form A and Form B using the four methods described in Approach, based on the provided solubility data, melting data, and the empirical C_pConf constants from the Problem background. The methods are: (1) solubility extrapolation via van't Hoff plots; (2) heat of transition (ΔH_tr) method; (3) melting data method; (4) configurational free energy (G_c) phase diagram method with linear C_pConf approximation (using the k1,k2 constants) and with hyperbolic approximation (using k3). Output all five computed T_tr values (in degrees Celsius) to a CSV file transition_temperatures.csv with columns `method` and `T_tr_C`. Use method labels: SolubilityExtrapolation, DeltaHtr, MeltingData, GcPhase_eq19, GcPhase_eq20.
- Output file: `/app/outputs/transition_temperatures.csv`
- Format: csv
- Contract: Two columns: `method` (string) and `T_tr_C` (float, degrees Celsius). Five rows exactly.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_temperatures.csv
- path: `/app/outputs/transition_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Transition temperature estimates from the four thermodynamic methods (solubility extrapolation, ΔH_tr, melting data, and G_c phase diagram with two C_pConf approximations). Five computed T_tr values.
- schema:
  - `type`: table
  - `required_columns`: `method`, `T_tr_C`
  - `units`:
    - `T_tr_C`: degrees Celsius

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "method",
          "T_tr_C"
        ],
        "units": {
          "T_tr_C": "degrees Celsius"
        }
      },
      "description": "Transition temperature estimates from the four thermodynamic methods (solubility extrapolation, ΔH_tr, melting data, and G_c phase diagram with two C_pConf approximations). Five computed T_tr values."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently evaluates each required artifact and combines the scores into a final reward. The primary scored artifact is `transition_temperatures.csv`. The verifier compares your computed T_tr values against reference results (hidden from you) using an appropriate tolerance; to earn full credit, all five values must be within the tolerance. The intermediate process artifact `classification.json` is not directly scored but is a mandatory step that supports the T_tr computation. Simply reporting numbers without executing the actual computations will not pass the verifier's checks.
