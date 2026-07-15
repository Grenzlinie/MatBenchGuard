# Polynomial description of the Fe-C-Si phase diagram up to 4.5 wt% Si including Cu, Mn, Cr and P

## Problem background
Silicon cast irons with more than 3 wt% Si require accurate models of the stable Fe-C-Si phase diagram to predict solidification behavior. The austenite and graphite liquidus curves become nonlinear at higher silicon contents, and the effects of common alloying elements (Cu, Mn, Cr, P) must be included. This task aims to produce polynomial descriptions of the liquidus temperatures, eutectic carbon content, and partition coefficients for the Fe-C-Si system up to 4.5 wt% Si with the listed additions, using CALPHAD calculations and polynomial fitting.

## Approach
Use an open-source CALPHAD tool (PyCalphad) with a suitable Fe-C-Si-X thermodynamic database to compute stable equilibrium phase diagrams. For the ternary Fe-C-Si system and for additions of Cu, Mn, Cr, P, calculate the austenite and graphite liquidus temperatures over ranges of carbon and silicon contents. Fit linear relations T_L = T0 + m_C · w_C at each silicon level, then express T0 and m_C as second-order polynomials of silicon. Extend the fits to include additive and interaction terms for the alloying elements. Equate the fitted austenite and graphite liquidus expressions to derive the eutectic carbon content as a rational function of composition; also produce a simplified quadratic approximation and a corresponding carbon equivalent (CE) formula. Compute partition coefficients from the austenite composition at the liquidus, and fit them as polynomials of silicon content and undercooling ΔT. All coefficients are obtained from the CALPHAD-generated data without relying on pre‑supplied values.

## Reproduction target
Produce the following five JSON files containing polynomial coefficients, all derived from the CALPHAD calculations described above:

- **table_ternary_coefficients.json**: coefficients for T0_gamma, mC_gamma, T0_gra, mC_gra as second‑order polynomials of w_Si.
- **table_alloy_coefficients.json**: extended coefficients for T0_gamma, mC_gamma, T0_gra including Cu, Mn, Cr, P terms.
- **eutectic_relation.json**: coefficients for the rational expression of the eutectic carbon content w_C^eut as a function of Si and alloy additions.
- **ce_approximation.json**: coefficients for a simplified quadratic eutectic composition and the corresponding carbon equivalent (CE).
- **partition_coefficient.json**: polynomial coefficients for the partition coefficients k_C, k_Si, k_Cu, k_Mn, k_Cr, k_P as functions of w_Si and ΔT.

All files must be placed in `/app/outputs`. The specific structure of each file is detailed in the workflow steps and output contract.

## Assets

- PyCalphad: pycalphad
- Thermodynamic database for Fe-C-Si system: 10.1007/BF02667324

## Workflow steps

### Step 1: Generate CALPHAD liquidus and partition coefficient data
- Role: process
- Action: Using PyCalphad and the Fe-C-Si database, compute stable equilibrium phase diagrams for Fe-C-Si with Si = 0, 2, 3, 4.5 wt% and for each alloying addition (Cu up to 1 wt%, Mn up to 0.5 wt%, Cr up to 0.25 wt%, P up to 0.25 wt%). For each composition record the austenite and graphite liquidus temperatures, eutectic points, and partition coefficients of all elements. Cover the carbon range stated in the paper (e.g., 2.5–4.5 wt% C, varying with Si).
- Evidence: `/app/outputs/reference_data.csv`

### Step 2: Fit polynomial coefficients for ternary Fe-C-Si liquidus
- Role: scored (load-bearing)
- Action: From the generated liquidus data for the ternary system, fit linear relations T_L = T0 + m_C * w_C for each Si content. Then fit second-order polynomials to the obtained T0^γ, m_C^γ, T0^gra, m_C^gra as functions of w_Si (the polynomial coefficients correspond to the paper's Eqns. 3–6). Output the polynomial coefficients as a JSON object.
- Output file: `/app/outputs/table_ternary_coefficients.json`
- Format: json
- Contract: JSON object with keys 'T0_gamma', 'mC_gamma', 'T0_gra', 'mC_gra'; each value is a list of three numeric coefficients [a0, a1, a2] for the polynomial in w_Si.
- Scoring: scored by hidden verifier

### Step 3: Fit extended polynomial coefficients with Cu, Mn, Cr, P additions
- Role: scored (load-bearing)
- Action: Using the liquidus data including Cu, Mn, Cr, P additions, fit the corrected expressions for T0^γ (including additive shifts and Cu-Si interaction), m_C^γ (including Cu-Si dependent correction), and T0^gra (additive shifts for Cu, Mn, Cr, P). Output the polynomial coefficients for the alloy system.
- Output file: `/app/outputs/table_alloy_coefficients.json`
- Format: json
- Contract: JSON object with keys 'T0_gamma_alloy', 'mC_gamma_alloy', 'T0_gra_alloy'. T0_gamma_alloy must contain the keys: 'const', 'Si', 'Si2', 'Cu', 'Cu_Si', 'Cu_Si2', 'Mn', 'Mn_Si', 'Cr', 'P' (all numbers). mC_gamma_alloy must contain: 'const', 'Si', 'Si2', 'Cu', 'Cu_Si', 'Cu_Si2'. T0_gra_alloy must contain: 'const', 'Si', 'Si2', 'Cu', 'Mn', 'Cr', 'P'.
- Scoring: scored by hidden verifier

### Step 4: Derive eutectic carbon content rational expression
- Role: scored
- Action: Equate the fitted austenite and graphite liquidus expressions (from the alloy system) to obtain the rational expression for the eutectic carbon content w_C^eut as a function of w_Si and alloy additions. Output the coefficients of this rational expression.
- Output file: `/app/outputs/eutectic_relation.json`
- Format: json
- Contract: JSON object with keys 'numerator_coefficients' (array of 10 numbers in order: constant, w_Si, w_Si^2, w_Cu, w_Si·w_Cu, w_Si^2·w_Cu, w_Mn, w_Si·w_Mn, w_Cr, w_P) and 'denominator_coefficients' (array of 6 numbers in order: constant, w_Si, w_Si^2, w_Cu, w_Si·w_Cu, w_Si^2·w_Cu).
- Scoring: scored by hidden verifier

### Step 5: Derive approximate quadratic eutectic and carbon equivalent expressions
- Role: scored
- Action: By fitting the eutectic valley calculated from the full model, derive the simplified quadratic approximation for w_C^eut and the corresponding carbon equivalent CE. Output the coefficients.
- Output file: `/app/outputs/ce_approximation.json`
- Format: json
- Contract: JSON object with keys 'wC_eut_approx' (array of 6 numbers: [constant, w_Si coefficient, w_Si^2 coefficient, w_Cu coefficient, w_Cr coefficient, w_P coefficient]) and 'CE_approx' (array of 5 numbers: [w_Si coefficient, w_Si^2 coefficient, w_Cu coefficient, w_Cr coefficient, w_P coefficient]).
- Scoring: scored by hidden verifier

### Step 6: Fit partition coefficient polynomials for C, Si, Cu, Mn, Cr, P
- Role: scored
- Action: From the partition coefficient data generated in the first step, fit the polynomials for k_C, k_Si as functions of w_Si and ΔT, and for k_Cu, k_Mn, k_Cr, k_P as functions of w_Si, ΔT, and (for Cr) ignoring Si dependence. Output the polynomial coefficients.
- Output file: `/app/outputs/partition_coefficient.json`
- Format: json
- Contract: JSON object with keys 'k_C','k_Si','k_Cu','k_Mn','k_Cr','k_P'. k_C must contain: 'const','Si','dT','Si_dT','dT2'. k_Si must contain: 'const','Si','dT','Si_dT'. k_Cu must contain: 'const','Si','dT','Si_dT'. k_Mn must contain: 'const','Si','dT','Si2_dT'. k_Cr must contain: 'const','dT'. k_P must contain: 'const','dT'. All values are numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_ternary_coefficients.json`
- `/app/outputs/table_alloy_coefficients.json`
- `/app/outputs/eutectic_relation.json`
- `/app/outputs/ce_approximation.json`
- `/app/outputs/partition_coefficient.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_ternary_coefficients.json
- path: `/app/outputs/table_ternary_coefficients.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Fitted polynomial coefficients for the ternary Fe-C-Si system.
- schema:
  - `type`: object
  - `required`:
    - `T0_gamma`: array of 3 numbers
    - `mC_gamma`: array of 3 numbers
    - `T0_gra`: array of 3 numbers
    - `mC_gra`: array of 3 numbers
  - `items`: object
  - `required_columns`:
  - `units`:
    - `T0_gamma.values`: °C
    - `mC_gamma.values`: °C/wt%
    - `T0_gra.values`: °C
    - `mC_gra.values`: °C/wt%

### table_alloy_coefficients.json
- path: `/app/outputs/table_alloy_coefficients.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Fitted polynomial coefficients for the quinary system with Cu, Mn, Cr, P. Sub‑keys are explicitly listed.
- schema:
  - `type`: object
  - `properties`:
    - `T0_gamma_alloy`:
      - `type`: object
      - `properties`:
        - `const`:
          - `type`: number
        - `Si`:
          - `type`: number
        - `Si2`:
          - `type`: number
        - `Cu`:
          - `type`: number
        - `Cu_Si`:
          - `type`: number
        - `Cu_Si2`:
          - `type`: number
        - `Mn`:
          - `type`: number
        - `Mn_Si`:
          - `type`: number
        - `Cr`:
          - `type`: number
        - `P`:
          - `type`: number
      - `required`: `const`, `Si`, `Si2`, `Cu`, `Cu_Si`, `Cu_Si2`, `Mn`, `Mn_Si`, `Cr`, `P`
    - `mC_gamma_alloy`:
      - `type`: object
      - `properties`:
        - `const`:
          - `type`: number
        - `Si`:
          - `type`: number
        - `Si2`:
          - `type`: number
        - `Cu`:
          - `type`: number
        - `Cu_Si`:
          - `type`: number
        - `Cu_Si2`:
          - `type`: number
      - `required`: `const`, `Si`, `Si2`, `Cu`, `Cu_Si`, `Cu_Si2`
    - `T0_gra_alloy`:
      - `type`: object
      - `properties`:
        - `const`:
          - `type`: number
        - `Si`:
          - `type`: number
        - `Si2`:
          - `type`: number
        - `Cu`:
          - `type`: number
        - `Mn`:
          - `type`: number
        - `Cr`:
          - `type`: number
        - `P`:
          - `type`: number
      - `required`: `const`, `Si`, `Si2`, `Cu`, `Mn`, `Cr`, `P`
  - `required`: `T0_gamma_alloy`, `mC_gamma_alloy`, `T0_gra_alloy`

### eutectic_relation.json
- path: `/app/outputs/eutectic_relation.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Coefficients of the rational expression for eutectic carbon content. Numerator and denominator arrays with strict order.
- schema:
  - `type`: object
  - `properties`:
    - `numerator_coefficients`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 10
      - `maxItems`: 10
      - `description`: Order: [constant, w_Si, w_Si^2, w_Cu, w_Si·w_Cu, w_Si^2·w_Cu, w_Mn, w_Si·w_Mn, w_Cr, w_P]
    - `denominator_coefficients`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 6
      - `maxItems`: 6
      - `description`: Order: [constant, w_Si, w_Si^2, w_Cu, w_Si·w_Cu, w_Si^2·w_Cu]
  - `required`: `numerator_coefficients`, `denominator_coefficients`

### ce_approximation.json
- path: `/app/outputs/ce_approximation.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Coefficients for the approximate quadratic eutectic composition and carbon equivalent formulas.
- schema:
  - `type`: object
  - `properties`:
    - `wC_eut_approx`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 6
      - `maxItems`: 6
      - `description`: Order: [constant, w_Si, w_Si^2, w_Cu, w_Cr, w_P]
    - `CE_approx`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 5
      - `maxItems`: 5
      - `description`: Order: [w_Si, w_Si^2, w_Cu, w_Cr, w_P]
  - `required`: `wC_eut_approx`, `CE_approx`

### partition_coefficient.json
- path: `/app/outputs/partition_coefficient.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Polynomial coefficients for partition coefficients of C, Si, Cu, Mn, Cr and P. Sub‑keys per element are explicitly listed.
- schema:
  - `type`: object
  - `properties`:
    - `k_C`:
      - `type`: object
      - `properties`:
        - `const`:
          - `type`: number
        - `Si`:
          - `type`: number
        - `dT`:
          - `type`: number
        - `Si_dT`:
          - `type`: number
        - `dT2`:
          - `type`: number
      - `required`: `const`, `Si`, `dT`, `Si_dT`, `dT2`
    - `k_Si`:
      - `type`: object
      - `properties`:
        - `const`:
          - `type`: number
        - `Si`:
          - `type`: number
        - `dT`:
          - `type`: number
        - `Si_dT`:
          - `type`: number
      - `required`: `const`, `Si`, `dT`, `Si_dT`
    - `k_Cu`:
      - `type`: object
      - `properties`:
        - `const`:
          - `type`: number
        - `Si`:
          - `type`: number
        - `dT`:
          - `type`: number
        - `Si_dT`:
          - `type`: number
      - `required`: `const`, `Si`, `dT`, `Si_dT`
    - `k_Mn`:
      - `type`: object
      - `properties`:
        - `const`:
          - `type`: number
        - `Si`:
          - `type`: number
        - `dT`:
          - `type`: number
        - `Si2_dT`:
          - `type`: number
      - `required`: `const`, `Si`, `dT`, `Si2_dT`
    - `k_Cr`:
      - `type`: object
      - `properties`:
        - `const`:
          - `type`: number
        - `dT`:
          - `type`: number
      - `required`: `const`, `dT`
    - `k_P`:
      - `type`: object
      - `properties`:
        - `const`:
          - `type`: number
        - `dT`:
          - `type`: number
      - `required`: `const`, `dT`
  - `required`: `k_C`, `k_Si`, `k_Cu`, `k_Mn`, `k_Cr`, `k_P`

Notes: All scored artifacts contain only polynomial coefficients; the checker will use them to compute derived physical quantities (liquidus temperatures, eutectic carbon content, partition coefficients) at hidden validation compositions and compare against hidden references with an appropriate tolerance. The process step generate_reference_data produces a non-scored evidence file (reference_data.csv) that a correct solve should generate.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_ternary_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "T0_gamma": "array of 3 numbers",
          "mC_gamma": "array of 3 numbers",
          "T0_gra": "array of 3 numbers",
          "mC_gra": "array of 3 numbers"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "T0_gamma.values": "°C",
          "mC_gamma.values": "°C/wt%",
          "T0_gra.values": "°C",
          "mC_gra.values": "°C/wt%"
        }
      },
      "description": "Fitted polynomial coefficients for the ternary Fe-C-Si system."
    },
    {
      "file": "table_alloy_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "T0_gamma_alloy": {
            "type": "object",
            "properties": {
              "const": {
                "type": "number"
              },
              "Si": {
                "type": "number"
              },
              "Si2": {
                "type": "number"
              },
              "Cu": {
                "type": "number"
              },
              "Cu_Si": {
                "type": "number"
              },
              "Cu_Si2": {
                "type": "number"
              },
              "Mn": {
                "type": "number"
              },
              "Mn_Si": {
                "type": "number"
              },
              "Cr": {
                "type": "number"
              },
              "P": {
                "type": "number"
              }
            },
            "required": [
              "const",
              "Si",
              "Si2",
              "Cu",
              "Cu_Si",
              "Cu_Si2",
              "Mn",
              "Mn_Si",
              "Cr",
              "P"
            ]
          },
          "mC_gamma_alloy": {
            "type": "object",
            "properties": {
              "const": {
                "type": "number"
              },
              "Si": {
                "type": "number"
              },
              "Si2": {
                "type": "number"
              },
              "Cu": {
                "type": "number"
              },
              "Cu_Si": {
                "type": "number"
              },
              "Cu_Si2": {
                "type": "number"
              }
            },
            "required": [
              "const",
              "Si",
              "Si2",
              "Cu",
              "Cu_Si",
              "Cu_Si2"
            ]
          },
          "T0_gra_alloy": {
            "type": "object",
            "properties": {
              "const": {
                "type": "number"
              },
              "Si": {
                "type": "number"
              },
              "Si2": {
                "type": "number"
              },
              "Cu": {
                "type": "number"
              },
              "Mn": {
                "type": "number"
              },
              "Cr": {
                "type": "number"
              },
              "P": {
                "type": "number"
              }
            },
            "required": [
              "const",
              "Si",
              "Si2",
              "Cu",
              "Mn",
              "Cr",
              "P"
            ]
          }
        },
        "required": [
          "T0_gamma_alloy",
          "mC_gamma_alloy",
          "T0_gra_alloy"
        ]
      },
      "description": "Fitted polynomial coefficients for the quinary system with Cu, Mn, Cr, P. Sub‑keys are explicitly listed."
    },
    {
      "file": "eutectic_relation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "numerator_coefficients": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 10,
            "maxItems": 10,
            "description": "Order: [constant, w_Si, w_Si^2, w_Cu, w_Si·w_Cu, w_Si^2·w_Cu, w_Mn, w_Si·w_Mn, w_Cr, w_P]"
          },
          "denominator_coefficients": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 6,
            "maxItems": 6,
            "description": "Order: [constant, w_Si, w_Si^2, w_Cu, w_Si·w_Cu, w_Si^2·w_Cu]"
          }
        },
        "required": [
          "numerator_coefficients",
          "denominator_coefficients"
        ]
      },
      "description": "Coefficients of the rational expression for eutectic carbon content. Numerator and denominator arrays with strict order."
    },
    {
      "file": "ce_approximation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "wC_eut_approx": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 6,
            "maxItems": 6,
            "description": "Order: [constant, w_Si, w_Si^2, w_Cu, w_Cr, w_P]"
          },
          "CE_approx": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 5,
            "maxItems": 5,
            "description": "Order: [w_Si, w_Si^2, w_Cu, w_Cr, w_P]"
          }
        },
        "required": [
          "wC_eut_approx",
          "CE_approx"
        ]
      },
      "description": "Coefficients for the approximate quadratic eutectic composition and carbon equivalent formulas."
    },
    {
      "file": "partition_coefficient.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "k_C": {
            "type": "object",
            "properties": {
              "const": {
                "type": "number"
              },
              "Si": {
                "type": "number"
              },
              "dT": {
                "type": "number"
              },
              "Si_dT": {
                "type": "number"
              },
              "dT2": {
                "type": "number"
              }
            },
            "required": [
              "const",
              "Si",
              "dT",
              "Si_dT",
              "dT2"
            ]
          },
          "k_Si": {
            "type": "object",
            "properties": {
              "const": {
                "type": "number"
              },
              "Si": {
                "type": "number"
              },
              "dT": {
                "type": "number"
              },
              "Si_dT": {
                "type": "number"
              }
            },
            "required": [
              "const",
              "Si",
              "dT",
              "Si_dT"
            ]
          },
          "k_Cu": {
            "type": "object",
            "properties": {
              "const": {
                "type": "number"
              },
              "Si": {
                "type": "number"
              },
              "dT": {
                "type": "number"
              },
              "Si_dT": {
                "type": "number"
              }
            },
            "required": [
              "const",
              "Si",
              "dT",
              "Si_dT"
            ]
          },
          "k_Mn": {
            "type": "object",
            "properties": {
              "const": {
                "type": "number"
              },
              "Si": {
                "type": "number"
              },
              "dT": {
                "type": "number"
              },
              "Si2_dT": {
                "type": "number"
              }
            },
            "required": [
              "const",
              "Si",
              "dT",
              "Si2_dT"
            ]
          },
          "k_Cr": {
            "type": "object",
            "properties": {
              "const": {
                "type": "number"
              },
              "dT": {
                "type": "number"
              }
            },
            "required": [
              "const",
              "dT"
            ]
          },
          "k_P": {
            "type": "object",
            "properties": {
              "const": {
                "type": "number"
              },
              "dT": {
                "type": "number"
              }
            },
            "required": [
              "const",
              "dT"
            ]
          }
        },
        "required": [
          "k_C",
          "k_Si",
          "k_Cu",
          "k_Mn",
          "k_Cr",
          "k_P"
        ]
      },
      "description": "Polynomial coefficients for partition coefficients of C, Si, Cu, Mn, Cr and P. Sub‑keys per element are explicitly listed."
    }
  ],
  "notes": "All scored artifacts contain only polynomial coefficients; the checker will use them to compute derived physical quantities (liquidus temperatures, eutectic carbon content, partition coefficients) at hidden validation compositions and compare against hidden references with an appropriate tolerance. The process step generate_reference_data produces a non-scored evidence file (reference_data.csv) that a correct solve should generate."
}
```

## How you are scored
Each scored artifact is evaluated independently by a hidden verifier. The verifier uses the polynomials you report to compute physical quantities (e.g., liquidus temperature, eutectic carbon content, partition coefficient) at hidden validation compositions. These computed values are compared against hidden reference values with an appropriate tolerance that accounts for differences between the CALPHAD toolchain and database. A higher score is earned by obtaining values close to the references. The scores from all artifacts are combined by weight to produce the final reward. The verifier does not re‑run CALPHAD; it only checks the correctness of your submitted polynomials. Simply reporting numbers without correctly performing the fitting procedure will not pass.
