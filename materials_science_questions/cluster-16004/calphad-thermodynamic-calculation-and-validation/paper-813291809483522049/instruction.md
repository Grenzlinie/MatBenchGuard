# Thermodynamic and Phase Diagram Calculation for Solid Cu-Ni Alloys

## Problem background
The Cu-Ni system is a classical binary alloy that shows complete solid solubility at elevated temperatures and a miscibility gap at lower temperatures. A reliable thermodynamic description of the solid solution is essential for predicting phase equilibria and for CALPHAD-type assessments. This work addresses the determination of the Redlich-Kister parameters for the excess Gibbs energy, enthalpy, and entropy of solid Cu-Ni alloys from Knudsen cell mass spectrometric measurements, and the subsequent computation of thermodynamic activities and the solid-liquid phase diagram.

## Approach
The thermodynamic description of the solid solution is based on the Algebraic Intensity‑Ratio (A.I.R.) method. Ion‑current intensity‑ratios measured by Knudsen cell mass spectrometry are expressed as temperature‑dependent regression lines, yielding a set of intercepts d(x) and slopes k(x) for several alloy compositions. Using these data together with the Redlich‑Kister polynomial expansion for the molar excess Gibbs energy, the excess Gibbs energy parameters are fitted by a least‑squares regression. The enthalpy and entropy parameters are then obtained from the temperature dependence of the Gibbs energy parameters via the relation B_n^G(T) = B_n^H – T B_n^S. With these parameters, the molar excess enthalpy, excess entropy, excess Gibbs energy, and the thermodynamic activities are evaluated at 1350 K across the composition range.

For the phase diagram, the solid‑phase parameters are combined with independently known liquid‑phase Redlich‑Kister parameters and pure‑component thermophysical data (heats of melting and heat capacities). The two nonlinear solid‑liquid equilibrium equations are solved at multiple temperatures by a Newton‑Raphson method to obtain the coexisting liquid and solid compositions. All computations can be performed with standard scientific Python libraries.

## Reproduction target
Using the supplied intercepts d(x) and slopes k(x) for each alloy composition, determine the Redlich‑Kister parameters B_n^H and B_n^S for the solid phase (n = 0, 1, 2). Using these parameters, compute the molar excess enthalpy H^E, excess entropy S^E, excess Gibbs energy G^E, and the thermodynamic activities a_Cu and a_Ni at T = 1350 K for mole fractions x_Ni from 0.0 to 1.0 in steps of 0.1. Finally, combine the solid‑phase parameters with the provided liquid‑phase Redlich‑Kister parameters and the given pure‑component heats of melting and heat capacities to solve the solid‑liquid equilibrium conditions at fourteen specified temperatures (1700, 1675, 1650, 1625, 1600, 1575, 1550, 1525, 1500, 1475, 1450, 1425, 1400, 1375 K) via a Newton solver, yielding the liquid and solid equilibrium compositions. All required input data are provided in this instruction; no external fetching is needed.

## Assets

- Python scientific computing libraries (numpy, scipy): numpy scipy
- Liquid-phase Redlich-Kister parameters for Cu-Ni

## Workflow steps

### Step 1: Fit Redlich-Kister Parameters for Solid Cu-Ni
- Role: scored
- Action: Using the provided intercepts d(x) and slopes k(x) for each alloy composition, compute the left-hand side of the regression formula at T=1350 K and perform a least-squares fit to obtain B_0^G, B_1^G, B_2^G at 1350 K. From the temperature dependence of the data, extract B_n^H and B_n^S via linear regression using the relation B_n^G(T) = B_n^H - T B_n^S. Output the three sets of parameters.
- Output file: `/app/outputs/table2_parameters.csv`
- Format: csv
- Contract: CSV with 3 rows. Columns: n (int), B_H (float, J/mol), B_S (float, J/(mol·K)). Rows for n=0,1,2.
- Scoring: scored by hidden verifier

### Step 2: Compute Thermodynamic Properties at 1350 K
- Role: scored
- Action: Using the Redlich-Kister parameters from the previous step and the Redlich-Kister expansion, compute the molar excess enthalpy H^E, excess entropy S^E, excess Gibbs energy G^E, and the thermodynamic activities a_Cu and a_Ni at T=1350 K for x_Ni from 0.0 to 1.0 in steps of 0.1. Output the results as a table.
- Output file: `/app/outputs/table3_properties.csv`
- Format: csv
- Contract: CSV with 11 rows (x_Ni = 0.0, 0.1, ..., 1.0). Columns: x_Ni (float), H_E (float, J/mol), S_E (float, J/(mol·K)), G_E (float, J/mol), a_Cu (float), a_Ni (float).
- Scoring: scored by hidden verifier

### Step 3: Compute Cu-Ni Solid-Liquid Phase Diagram
- Role: scored (load-bearing)
- Action: Using the solid-phase parameters from step 1, the provided liquid-phase Redlich-Kister parameters, and the given pure-component heats of melting and heat capacities, solve the solid-liquid equilibrium conditions at 14 temperatures (1700,1675,1650,1625,1600,1575,1550,1525,1500,1475,1450,1425,1400,1375 K) using a Newton-Raphson solver. Output the coexisting liquid and solid compositions.
- Output file: `/app/outputs/table5_phasediagram.csv`
- Format: csv
- Contract: CSV with 14 rows. Columns: T_K (float), x_Ni_liquid (float), x_Ni_solid (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table2_parameters.csv`
- `/app/outputs/table3_properties.csv`
- `/app/outputs/table5_phasediagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table2_parameters.csv
- path: `/app/outputs/table2_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Redlich-Kister parameters B_n^H and B_n^S for n=0,1,2 of solid Cu-Ni.
- schema:
  - `type`: table
  - `required_columns`: `n`, `B_H`, `B_S`
  - `rows`: 3
  - `units`:
    - `B_H`: J/mol
    - `B_S`: J/(mol·K)

### table3_properties.csv
- path: `/app/outputs/table3_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic properties of solid Cu-Ni at 1350 K.
- schema:
  - `type`: table
  - `required_columns`: `x_Ni`, `H_E`, `S_E`, `G_E`, `a_Cu`, `a_Ni`
  - `rows`: 11
  - `units`:
    - `H_E`: J/mol
    - `S_E`: J/(mol·K)
    - `G_E`: J/mol
    - `a_Cu`: dimensionless
    - `a_Ni`: dimensionless

### table5_phasediagram.csv
- path: `/app/outputs/table5_phasediagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Cu-Ni equilibrium phase diagram compositions at selected temperatures.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `x_Ni_liquid`, `x_Ni_solid`
  - `rows`: 14
  - `units`:
    - `T_K`: K
    - `x_Ni_liquid`: mole fraction
    - `x_Ni_solid`: mole fraction

Notes: All outputs are verified by comparing each numeric value to the corresponding paper-reported reference values within prescribed tolerances. The tolerances are chosen to accommodate minor numerical differences from independent implementations and solver settings.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table2_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "B_H",
          "B_S"
        ],
        "rows": 3,
        "units": {
          "B_H": "J/mol",
          "B_S": "J/(mol·K)"
        }
      },
      "description": "Redlich-Kister parameters B_n^H and B_n^S for n=0,1,2 of solid Cu-Ni."
    },
    {
      "file": "table3_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_Ni",
          "H_E",
          "S_E",
          "G_E",
          "a_Cu",
          "a_Ni"
        ],
        "rows": 11,
        "units": {
          "H_E": "J/mol",
          "S_E": "J/(mol·K)",
          "G_E": "J/mol",
          "a_Cu": "dimensionless",
          "a_Ni": "dimensionless"
        }
      },
      "description": "Thermodynamic properties of solid Cu-Ni at 1350 K."
    },
    {
      "file": "table5_phasediagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "x_Ni_liquid",
          "x_Ni_solid"
        ],
        "rows": 14,
        "units": {
          "T_K": "K",
          "x_Ni_liquid": "mole fraction",
          "x_Ni_solid": "mole fraction"
        }
      },
      "description": "Cu-Ni equilibrium phase diagram compositions at selected temperatures."
    }
  ],
  "notes": "All outputs are verified by comparing each numeric value to the corresponding paper-reported reference values within prescribed tolerances. The tolerances are chosen to accommodate minor numerical differences from independent implementations and solver settings."
}
```

## How you are scored
Your submission is evaluated by an automated verifier that independently checks each output file. For each scored artifact, the verifier compares the computed numerical values to hidden reference values using prescribed tolerances that account for minor numerical differences from independent implementations. The overall score is the average of the fraction of correct rows across the three artifacts (each weighted equally). This scoring rewards a genuine computational reproduction; simply reporting numbers from the original publication without performing the required calculation is unlikely to pass.
