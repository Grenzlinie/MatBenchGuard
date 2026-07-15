# Empirical power-law relations between bulk modulus and interatomic distance for elemental substances and compounds

## Problem background
Bulk modulus quantifies a material's resistance to uniform compression and is closely related to hardness. For elemental substances, an empirical power-law form B = C d^{-m} has been suggested to relate the bulk modulus B to the interatomic distance d, with the exponent m and pre-factor C possibly varying with bonding character. If such relations can be determined from known elemental data, they could provide a simple route to estimate the bulk moduli of compounds by combining the parameters of their constituent elements.

## Approach
First, elemental substances are assigned to one of five bonding-mode groups (sp³, spd, 3d, 4d, 5d/4f) using a supplied classification. For each group, the elements that are not excluded because of strong antibonding effects are used. A linear least-squares fit of log(B) vs. log(d) yields the exponent m and pre-factor C of the power law B = C d^{-m} for that group.

For a binary compound A_x B_y, the effective pre-factor and exponent are assumed to be the weighted geometric means of the constituent elemental parameters: C_AB = C_A^{z} · C_B^{1-z} and m_AB = m_A^{z} · m_B^{1-z}, with the composition fraction z = x/(x+y). The predicted bulk modulus is then B_pred = C_AB · d^{-m_AB}, where d is the compound's d-spacing. This scheme is applied to a set of AB-type compounds whose d-spacings are provided.

## Reproduction target
Using the provided elemental d-spacings (nm) and experimental bulk moduli (GPa), together with the given bonding-mode classification, perform least-squares fits to determine m and C for each of the five groups. Write the fitted parameters to step_01_fitted_parameters.csv. Then, using those fitted parameters, the provided compound d-spacings, and the geometric mean formula, compute predicted bulk moduli for the listed compounds (e.g., CaO, SrO, BaO, CoO, MnO, FeO, NiO, ZnO, EuO, Sc2O3) and write the results to step_02_predicted_B.csv. Both output files must adhere to the stated column schemas.

## Assets

- NumPy: numpy
- SciPy: scipy
- Pandas: pandas

## Workflow steps

### Step 1: Load elemental data and apply bonding-group classification
- Role: process
- Action: Load the provided table of elemental interatomic distances (nm) and bulk moduli (GPa). Using the supplied bonding-group classification (Table 2), assign each element to one of five groups: sp³, spd, 3d, 4d, and 5d/4f. Exclude elements with strong antibonding character (certain vanadium-group elements and chalcogens) from subsequent fitting.
- Evidence: `/app/outputs/classification_log.txt`

### Step 2: Fit power-law parameters for each bonding group
- Role: scored
- Action: For each of the five groups, perform a least-squares fit of log(bulk modulus) versus log(interatomic distance) to determine the exponent m and preterm C in B = C d^{-m}. Write the resulting (Group, m, C) rows to CSV.
- Output file: `/app/outputs/step_01_fitted_parameters.csv`
- Format: csv
- Contract: Columns: Group (string identifier of bonding mode), m (float exponent), C (float preterm).
- Scoring: scored by hidden verifier

### Step 3: Predict bulk moduli of AB compounds
- Role: scored (load-bearing)
- Action: Using the fitted group parameters from step_02, the provided interatomic distances for the specified AB compounds, and the geometric mean formula B_AB = (C_A^z * C_B^(1-z)) * d^{-(m_A^z * m_B^(1-z))} with z = x/(x+y) for compound A_xB_y, compute the predicted bulk modulus (GPa) for each compound. Assign the constituent elements to the appropriate bonding group (sp³ for diamond C, Si, Ge, Sn; spd for Zn, Cd, etc.; 3d for transition metals; 4d/5d4f as labeled). Output CSV with two columns: Compound (string identifier) and Predicted_B_GPa (float). Include at least 10 compounds from the provided list (e.g., CaO, SrO, BaO, CoO, MnO, FeO, NiO, ZnO, EuO, Sc2O3).
- Output file: `/app/outputs/step_02_predicted_B.csv`
- Format: csv
- Contract: Columns: Compound (string), Predicted_B_GPa (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_fitted_parameters.csv`
- `/app/outputs/step_02_predicted_B.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_fitted_parameters.csv
- path: `/app/outputs/step_01_fitted_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Fitted power-law exponent m and preterm C for each of the five bonding-mode groups.
- schema:
  - `type`: table
  - `required_columns`: `Group`, `m`, `C`
  - `units`:
    - `Group`: string (sp3, spd, 3d, 4d, 5d4f)
    - `m`: dimensionless exponent
    - `C`: GPa·nm^m (preterm)

### step_02_predicted_B.csv
- path: `/app/outputs/step_02_predicted_B.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Predicted bulk moduli (GPa) for the listed AB compounds, computed via geometric-mean formula using the fitted group parameters.
- schema:
  - `type`: table
  - `required_columns`: `Compound`, `Predicted_B_GPa`
  - `units`:
    - `Compound`: string
    - `Predicted_B_GPa`: float (GPa)

Notes: All scoring uses hidden paper-reported reference values. The instruction provides the required interatomic distances and classification table; no external datasets need to be fetched.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_fitted_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Group",
          "m",
          "C"
        ],
        "units": {
          "Group": "string (sp3, spd, 3d, 4d, 5d4f)",
          "m": "dimensionless exponent",
          "C": "GPa·nm^m (preterm)"
        }
      },
      "description": "Fitted power-law exponent m and preterm C for each of the five bonding-mode groups."
    },
    {
      "file": "step_02_predicted_B.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Compound",
          "Predicted_B_GPa"
        ],
        "units": {
          "Compound": "string",
          "Predicted_B_GPa": "float (GPa)"
        }
      },
      "description": "Predicted bulk moduli (GPa) for the listed AB compounds, computed via geometric-mean formula using the fitted group parameters."
    }
  ],
  "notes": "All scoring uses hidden paper-reported reference values. The instruction provides the required interatomic distances and classification table; no external datasets need to be fetched."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact (the fitted parameters CSV and the predicted moduli CSV). It compares your reported values against hidden reference values taken from the original study. Each artifact contributes a portion of the final reward (0 to 1). The comparison uses tolerances that account for reasonable numerical differences arising from independent fitting. Simply restating the paper's numbers without executing the required steps will not succeed; your pipeline must genuinely compute the outputs from the provided data and formulas.
