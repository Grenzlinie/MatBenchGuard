# CALPHAD thermodynamic optimization of Al-P and Fe-Al-P systems

## Problem background
Accurate thermodynamic databases are critical for predicting phase equilibria and optimizing materials processes, particularly in steel galvannealing and semiconductor manufacturing. The Al-P and Fe-Al-P systems are central to understanding the interactions between aluminum, phosphorus, and iron in steels, affecting coating formation, corrosion resistance, and mechanical properties. Previous assessments contain inconsistencies, and a robust thermodynamic description is needed. This task aims to develop a consistent thermodynamic database for these systems by performing a CALPHAD optimization of the Gibbs energy functions for all relevant phases.

## Approach
The CALPHAD (CALculation of PHAse Diagrams) method is employed to optimize the Gibbs energy functions of all phases in the Al-P and Fe-Al-P systems. The liquid phase is modeled using the Modified Quasichemical Model, which accounts for short-range ordering, while solid solutions are described with the Compound Energy Formalism. The binary Fe-P and Fe-Al subsystems are taken from published optimizations and held fixed. The Gibbs energies of the stoichiometric AlP compound and the liquid Al-P solution are optimized to reproduce the experimental AlP melting point, Al-rich liquidus, and vaporization equilibria. The ternary Fe-Al-P system is then optimized using the Toop interpolation technique with Al as the asymmetric component. The optimization simultaneously considers all available experimental data, including heat capacities, enthalpies of formation, phase boundaries, and activity coefficients.

## Reproduction target
Compute a self-consistent set of Gibbs energy parameters for the Al-P and Fe-Al-P systems. Using these parameters, calculate and report: (1) the Al-P phase diagram, including the melting temperature of AlP (congruent point) and the Al-rich liquidus curve; (2) isothermal sections of the Fe-Al-P phase diagram at 450, 650, and 800 °C, showing the equilibrium phase boundaries; (3) the activity coefficient of phosphorus in liquid Fe-Al-P alloys at 1400 and 1600 °C for Al concentrations up to 5 wt%, referenced to the 1 wt% standard state. Your computed quantities should be consistent with the experimental data from the literature that you will compile and use in the optimization.

## Assets

- pycalphad (CALPHAD library): https://pycalphad.org/
- SGTE pure element database
- Experimental data for Al-P system
- Fe-P binary thermodynamic parameters
- Fe-Al binary thermodynamic parameters

## Workflow steps

### Step 1: Prepare experimental data for Al-P and Fe-Al-P systems
- Role: process
- Action: Compile the experimental data points required for optimization and validation: heat capacity of AlP, standard enthalpy and entropy of AlP, Al-rich liquidus compositions, melting point of AlP, vapor pressures of Al(g) and P2(g) over AlP, Fe-Al-P isothermal tie-lines, activity coefficients of P in liquid Fe-Al, and the solubility of P in BCC_A2. Digitize the numerical values from the cited publications and produce a structured file.
- Evidence: `/app/outputs/experimental_data.json`

### Step 2: Fit heat capacity function of stoichiometric AlP
- Role: process
- Action: Fit the heat capacity expression C_P(T) = a + b*T + c*T^{-2} to the selected experimental heat capacity data for AlP. Report the fitted coefficients.
- Evidence: `/app/outputs/alp_cp_fit.json`

### Step 3: Thermodynamic optimization of Al-P and Fe-Al-P parameters
- Role: scored (load-bearing)
- Action: Using an open-source CALPHAD framework, perform the thermodynamic optimization. Adopt the published parameters for the Fe-P and Fe-Al binary subsystems. Optimize the Gibbs energy parameters for stoichiometric AlP (ΔH°_298, S°_298, and Cp coefficients) and the liquid Al-P interaction parameters. Extend to the ternary Fe-Al-P system using the Toop interpolation with Al as the asymmetric component and optimize ternary parameters as needed. The optimization must simultaneously reproduce the experimental melting point of AlP, the Al-rich liquidus, vapor pressures, and the ternary phase equilibria. Output the complete set of optimized model parameters.
- Output file: `/app/outputs/optimized_parameters.json`
- Format: json
- Contract: JSON object with required top-level keys "AlP" and "liquid". "AlP" must contain "Delta_H_298" (number, J/mol), "S_298" (number, J/(mol·K)), "Cp" (object with "a", "b", "c" numbers for C_P = a + b*T + c*T^{-2}). "liquid" must contain "delta_g_AlP" as an array [a, b] representing Δg_AlP = a + b*T (a in J/mol, b in J/(mol·K)). Optional ternary liquid parameters may be included under "ternary_FeP_Al" with keys "g_FeP_Al_101" and "g_FeP_Al_011".
- Scoring: scored by hidden verifier

### Step 4: Compute Al-P phase diagram
- Role: scored
- Action: Using the optimized database, compute the Al-P liquidus curve. Determine the melting temperature of stoichiometric AlP and the liquidus composition over the full composition range. Output the phase diagram data.
- Output file: `/app/outputs/alp_phase_diagram.csv`
- Format: csv
- Contract: CSV with columns: T_K (temperature in K), x_P (mole fraction of P in liquid), phase_flag (character indicating the phase boundary type). Additionally, a row with T_melt_K and fixed composition x_P=0.5 for the congruent melting point of AlP.
- Scoring: scored by hidden verifier

### Step 5: Compute Fe-Al-P isothermal sections
- Role: scored
- Action: Using the optimized database, compute the isothermal phase diagrams of the Fe-Al-P system at 450, 650, and 800 °C. Identify the phase boundaries and report the equilibrium compositions.
- Output file: `/app/outputs/fealp_isothermal_sections.csv`
- Format: csv
- Contract: CSV with columns: T_C (temperature in °C: 450, 650, 800), region_label (phase name, e.g., BCC_A2, AlP, liquid), x_Fe, x_Al, x_P (mole fractions for each phase boundary point or tie-line end-point).
- Scoring: scored by hidden verifier

### Step 6: Compute activity coefficient of P in liquid Fe-Al
- Role: scored
- Action: Using the optimized database, calculate the activity coefficient of phosphorus in liquid Fe-Al-P alloys at 1400 and 1600 °C for Al concentrations up to 5 wt%. Output the results.
- Output file: `/app/outputs/p_activity_coefficient.csv`
- Format: csv
- Contract: CSV with columns: T_C (1400, 1600), wt_Al (weight percent Al in the alloy), gamma_P (activity coefficient of P, referenced to the 1 wt% standard state), log10_gamma_P (base-10 logarithm of gamma_P).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_parameters.json`
- `/app/outputs/alp_phase_diagram.csv`
- `/app/outputs/fealp_isothermal_sections.csv`
- `/app/outputs/p_activity_coefficient.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_parameters.json
- path: `/app/outputs/optimized_parameters.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Optimized Gibbs energy parameters for the Fe-Al-P system. Contains all data needed to recompute phase boundaries and thermodynamic properties.
- schema:
  - `type`: object
  - `required`: `AlP`, `liquid`
  - `properties`:
    - `AlP`:
      - `type`: object
      - `required`: `Delta_H_298`, `S_298`, `Cp`
      - `properties`:
        - `Delta_H_298`:
          - `type`: number
          - `description`: Standard enthalpy of formation at 298.15 K in J/mol
        - `S_298`:
          - `type`: number
          - `description`: Standard entropy at 298.15 K in J/(mol K)
        - `Cp`:
          - `type`: object
          - `required`: `a`, `b`, `c`
          - `properties`:
            - `a`:
              - `type`: number
              - `description`: Coefficient a in C_P = a + b*T + c*T^{-2}, J/(mol K)
            - `b`:
              - `type`: number
              - `description`: Coefficient b, J/(mol K^2)
            - `c`:
              - `type`: number
              - `description`: Coefficient c, J*K/mol
    - `liquid`:
      - `type`: object
      - `required`: `delta_g_AlP`
      - `properties`:
        - `delta_g_AlP`:
          - `type`: array
          - `minItems`: 2
          - `maxItems`: 2
          - `items`:
            - `type`: number
          - `description`: Temperature-dependent Al-P pair parameter, [a, b] where Δg_AlP = a + b*T, a in J/mol, b in J/(mol K)
        - `ternary_FeP_Al`:
          - `type`: object
          - `description`: Optional ternary liquid parameters (Toop, Al asymmetric)
          - `properties`:
            - `g_FeP_Al_101`:
              - `anyOf`:
                - `type`: number
                - `type`: array
                - `minItems`: 2
                - `maxItems`: 2
                - `items`:
                  - `type`: number
              - `description`: Parameter g_FeP(Al)^{101}, constant or [a,b]
            - `g_FeP_Al_011`:
              - `anyOf`:
                - `type`: number
                - `type`: array
                - `minItems`: 2
                - `maxItems`: 2
                - `items`:
                  - `type`: number
              - `description`: Parameter g_FeP(Al)^{011}, constant or [a,b]

### alp_phase_diagram.csv
- path: `/app/outputs/alp_phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Al-P phase diagram data: melting temperature of AlP and liquidus compositions.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `x_P`, `phase_flag`
  - `description`: Must include the liquidus curve and a separate row indicating the melting temperature of AlP (x_P=0.5).

### fealp_isothermal_sections.csv
- path: `/app/outputs/fealp_isothermal_sections.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Fe-Al-P isothermal phase boundaries, each row with a phase name label for a boundary point.
- schema:
  - `type`: table
  - `required_columns`: `T_C`, `region_label`, `x_Fe`, `x_Al`, `x_P`
  - `description`: Each row is a single phase boundary point or tie‑line end‑point, with region_label containing the phase name (e.g., BCC_A2, AlP, liquid).

### p_activity_coefficient.csv
- path: `/app/outputs/p_activity_coefficient.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Activity coefficient of phosphorus in liquid Fe-Al-P alloys.
- schema:
  - `type`: table
  - `required_columns`: `T_C`, `wt_Al`, `gamma_P`, `log10_gamma_P`
  - `description`: Activity coefficient of P in liquid Fe-Al-P at 1400 and 1600 °C.

Notes: The checker will recompute the Al-P phase diagram and other properties from the submitted optimized_parameters.json and compare to experimental data within tolerances. All units are SI (J/mol, K, mole fraction) unless otherwise specified. The solver must adopt published Fe-P and Fe-Al binary parameters as fixed inputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "AlP",
          "liquid"
        ],
        "properties": {
          "AlP": {
            "type": "object",
            "required": [
              "Delta_H_298",
              "S_298",
              "Cp"
            ],
            "properties": {
              "Delta_H_298": {
                "type": "number",
                "description": "Standard enthalpy of formation at 298.15 K in J/mol"
              },
              "S_298": {
                "type": "number",
                "description": "Standard entropy at 298.15 K in J/(mol K)"
              },
              "Cp": {
                "type": "object",
                "required": [
                  "a",
                  "b",
                  "c"
                ],
                "properties": {
                  "a": {
                    "type": "number",
                    "description": "Coefficient a in C_P = a + b*T + c*T^{-2}, J/(mol K)"
                  },
                  "b": {
                    "type": "number",
                    "description": "Coefficient b, J/(mol K^2)"
                  },
                  "c": {
                    "type": "number",
                    "description": "Coefficient c, J*K/mol"
                  }
                }
              }
            }
          },
          "liquid": {
            "type": "object",
            "required": [
              "delta_g_AlP"
            ],
            "properties": {
              "delta_g_AlP": {
                "type": "array",
                "minItems": 2,
                "maxItems": 2,
                "items": {
                  "type": "number"
                },
                "description": "Temperature-dependent Al-P pair parameter, [a, b] where Δg_AlP = a + b*T, a in J/mol, b in J/(mol K)"
              },
              "ternary_FeP_Al": {
                "type": "object",
                "description": "Optional ternary liquid parameters (Toop, Al asymmetric)",
                "properties": {
                  "g_FeP_Al_101": {
                    "anyOf": [
                      {
                        "type": "number"
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": {
                          "type": "number"
                        }
                      }
                    ],
                    "description": "Parameter g_FeP(Al)^{101}, constant or [a,b]"
                  },
                  "g_FeP_Al_011": {
                    "anyOf": [
                      {
                        "type": "number"
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": {
                          "type": "number"
                        }
                      }
                    ],
                    "description": "Parameter g_FeP(Al)^{011}, constant or [a,b]"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Optimized Gibbs energy parameters for the Fe-Al-P system. Contains all data needed to recompute phase boundaries and thermodynamic properties."
    },
    {
      "file": "alp_phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "x_P",
          "phase_flag"
        ],
        "description": "Must include the liquidus curve and a separate row indicating the melting temperature of AlP (x_P=0.5)."
      },
      "description": "Al-P phase diagram data: melting temperature of AlP and liquidus compositions."
    },
    {
      "file": "fealp_isothermal_sections.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_C",
          "region_label",
          "x_Fe",
          "x_Al",
          "x_P"
        ],
        "description": "Each row is a single phase boundary point or tie‑line end‑point, with region_label containing the phase name (e.g., BCC_A2, AlP, liquid)."
      },
      "description": "Fe-Al-P isothermal phase boundaries, each row with a phase name label for a boundary point."
    },
    {
      "file": "p_activity_coefficient.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_C",
          "wt_Al",
          "gamma_P",
          "log10_gamma_P"
        ],
        "description": "Activity coefficient of P in liquid Fe-Al-P at 1400 and 1600 °C."
      },
      "description": "Activity coefficient of phosphorus in liquid Fe-Al-P alloys."
    }
  ],
  "notes": "The checker will recompute the Al-P phase diagram and other properties from the submitted optimized_parameters.json and compare to experimental data within tolerances. All units are SI (J/mol, K, mole fraction) unless otherwise specified. The solver must adopt published Fe-P and Fe-Al binary parameters as fixed inputs."
}
```

## How you are scored
A hidden verifier evaluates each scored workflow step's artifact against a hidden gold dataset derived from experimental measurements. The verifier recomputes phase boundaries and other properties from your submitted optimized parameters and compares them to experimental data, checking the melting point of AlP, the Al-rich liquidus, the isothermal phase boundaries, and the activity coefficients of phosphorus. Each scored step (3, 4, 5, 6) is scored independently, and the final reward is a weighted sum of these per-stage scores. Reporting numerical values without correct underlying computations will yield a low score, as the verifier re-derives quantities from your artifacts.
