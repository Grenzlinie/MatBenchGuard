# Binary Droplet Adsorption Model: Size-Dependent Surface Tension and Composition

## Problem background
Atmospheric binary droplets containing soluble surfactants such as nitric acid can exhibit size-dependent surface tension and composition due to adsorption of surfactant molecules at the droplet–vapor interface. Understanding how adsorption and surface tension change with droplet radius is crucial for predicting surface-stimulated crystal nucleation, because the condition for surface-stimulated freezing depends on the droplet's surface tension. The central open question is to compute the relationships between droplet radius and surface tension, excess surface coverage, interior mole fraction, and overall mole fraction for aqueous nitric acid droplets at a temperature of 193.15 K, using a Gibbsian thermodynamic model with Langmuir adsorption.

## Approach
The droplet is modelled within Gibbsian thermodynamics as a liquid sphere of uniform interior composition plus a dividing surface that carries an excess of the surfactant (component 2) quantified by the adsorption Γ₂. The interior composition is described by the mole ratio x, and the overall droplet composition by y. The surface tension σ(x) is obtained by integrating the Gibbs adsorption equation together with a Langmuir isotherm that relates the dimensionless adsorption to the bulk activities (activities from Clegg & Brimblecombe for the HNO₃–H₂O system). The Langmuir isotherm contains two parameters (saturation adsorption s∞ and equilibrium constant b) that must be fitted to experimental surface-tension data for aqueous nitric acid (Granzhan & Laktionova). Once σ(x) is known, the coupled equilibrium (Kelvin) and mass-partitioning equations are solved for x, y, and the droplet-size variable (related to radius via the pure-component volumes). From x and y one obtains the interior and overall mole fractions χ_int and χ_ovl. Computations are performed for fixed overall mole fractions 0.1, 0.2, 0.3, 0.4 over radii 5–100 nm to extract σ(R), excess coverage Γ₂/Γ∞, and χ_int(R); for fixed interior mole fractions 0.1, 0.2, 0.3, 0.4 to obtain χ_ovl(R); and for an organic contaminant modeled by an additional Langmuir isotherm (parameters Γo∞, K) to compute σ(R) at three partial pressures (3.3×10⁻⁸, 1×10⁻⁷, 3×10⁻⁷ Torr) for χ_ovl = 0.2. All quantities are converted to physical units (radius in nm, surface tension in dyne/cm).

## Reproduction target
Fit the Langmuir adsorption parameters using the experimental data, then solve the thermodynamic model for aqueous nitric acid droplets at T = 193.15 K. Produce a single JSON file `/app/outputs/step_01_results.json` containing five arrays with the following fields:

- `sigma_vs_R`: for each combination of overall mole fraction χ_ovl = 0.1,0.2,0.3,0.4 and radius R = 5,10,20,30,50,100 nm, report the surface tension σ (dyne/cm).
- `Gamma_vs_R`: for the same (χ_ovl, R) pairs, report the relative excess surface coverage Γ₂/Γ∞.
- `chi_int_vs_R`: for the same (χ_ovl, R) pairs, report the interior mole fraction χ_int.
- `chi_ovl_vs_R_fixed_chi_int`: for each fixed interior mole fraction χ_int = 0.1,0.2,0.3,0.4 and the same radii R, report the overall mole fraction χ_ovl.
- `organics_effect`: for each organic partial pressure Po = 3.3×10⁻⁸, 1×10⁻⁷, 3×10⁻⁷ Torr and radius R, report the surface tension σ for a droplet with overall mole fraction χ_ovl = 0.2.

All radii are in nm, surface tensions in dyne/cm, mole fractions dimensionless, and coverage ratio dimensionless. The file must be valid JSON with the exact schema shown in the output contract.

## Assets

- Clegg & Brimblecombe (1990) thermodynamic model for HNO3-H2O: https://doi.org/10.1021/j100376a020
- Clegg & Brimblecombe (1992) continuation: https://doi.org/10.1021/j100425a010
- Granzhan & Laktionova (1975) surface tension of aqueous HNO3

## Workflow steps

### Step 1: Fit Langmuir adsorption parameters to experimental surface tension data
- Role: process
- Action: Using the experimental surface tension data of Granzhan & Laktionova for aqueous HNO3, integrate the Gibbs adsorption equation with the Langmuir isotherm to express surface tension γ(x). Fit the parameters s∞ (dimensionless saturation adsorption) and b (equilibrium constant) such that γ(x) matches the experimental data at T=193.15 K. Use activity coefficients from Clegg & Brimblecombe. Save the fitted parameters for the downstream solving step.
- Evidence: `/app/outputs/fitted_params.json`

### Step 2: Solve binary droplet model and compute size-dependent properties
- Role: scored (load-bearing)
- Action: Using the fitted surface tension function γ(x) from the previous step, solve the coupled equilibrium and mass-partitioning equations for aqueous nitric acid droplets at T=193.15 K. Obtain interior mole ratio x, overall mole ratio y, and droplet size variable v2. Convert to physical quantities: radius R (nm), surface tension σ (dyne/cm), excess surface coverage Γ2/Γ∞, interior mole fraction χ_int = x/(1+x), overall mole fraction χ_ovl = y/(1+y). Compute arrays for: (a) fixed overall mole fractions χ_ovl = 0.1, 0.2, 0.3, 0.4 and a range of radii (5–100 nm): σ(R), Γ2(R)/Γ∞, χ_int(R); (b) fixed interior mole fractions χ_int = 0.1, 0.2, 0.3, 0.4 and the same radii: χ_ovl(R). For organic contamination, adopt Langmuir isotherm parameters Γo∞ and K as per the paper, and compute σ(R) for organic gas pressures Po = 3.3×10⁻⁸, 1×10⁻⁷, 3×10⁻⁷ Torr at χ_ovl = 0.2. Write all results to the specified JSON file.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: {
  "sigma_vs_R": [ { "chi_ovl": number, "R_nm": number, "sigma_dyne_cm": number } ],
  "Gamma_vs_R": [ { "chi_ovl": number, "R_nm": number, "Gamma_rel": number } ],
  "chi_int_vs_R": [ { "chi_ovl": number, "R_nm": number, "chi_int": number } ],
  "chi_ovl_vs_R_fixed_chi_int": [ { "chi_int": number, "R_nm": number, "chi_ovl": number } ],
  "organics_effect": [ { "Po_Torr": number, "R_nm": number, "sigma_dyne_cm": number } ]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Size-dependent surface tension, excess coverage, internal mole fraction, overall mole fraction (for fixed internal composition), and organic contamination effect for aqueous HNO3 droplets at 193.15 K.
- schema:
  - `type`: object
  - `properties`:
    - `sigma_vs_R`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `chi_ovl`:
            - `type`: number
          - `R_nm`:
            - `type`: number
          - `sigma_dyne_cm`:
            - `type`: number
        - `required`: `chi_ovl`, `R_nm`, `sigma_dyne_cm`
    - `Gamma_vs_R`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `chi_ovl`:
            - `type`: number
          - `R_nm`:
            - `type`: number
          - `Gamma_rel`:
            - `type`: number
        - `required`: `chi_ovl`, `R_nm`, `Gamma_rel`
    - `chi_int_vs_R`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `chi_ovl`:
            - `type`: number
          - `R_nm`:
            - `type`: number
          - `chi_int`:
            - `type`: number
        - `required`: `chi_ovl`, `R_nm`, `chi_int`
    - `chi_ovl_vs_R_fixed_chi_int`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `chi_int`:
            - `type`: number
          - `R_nm`:
            - `type`: number
          - `chi_ovl`:
            - `type`: number
        - `required`: `chi_int`, `R_nm`, `chi_ovl`
    - `organics_effect`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `Po_Torr`:
            - `type`: number
          - `R_nm`:
            - `type`: number
          - `sigma_dyne_cm`:
            - `type`: number
        - `required`: `Po_Torr`, `R_nm`, `sigma_dyne_cm`
  - `required`: `sigma_vs_R`, `Gamma_vs_R`, `chi_int_vs_R`, `chi_ovl_vs_R_fixed_chi_int`, `organics_effect`

Notes: The scored artifact contains arrays covering the paper's main headline quantities. The checker will compare the computed values to hidden reference data digitized from the paper's figures, using tolerances for surface tension (±2 dyne/cm), excess coverage (±0.05 relative), and mole fractions (±0.02), along with monotonicity trend checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "sigma_vs_R": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "chi_ovl": {
                  "type": "number"
                },
                "R_nm": {
                  "type": "number"
                },
                "sigma_dyne_cm": {
                  "type": "number"
                }
              },
              "required": [
                "chi_ovl",
                "R_nm",
                "sigma_dyne_cm"
              ]
            }
          },
          "Gamma_vs_R": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "chi_ovl": {
                  "type": "number"
                },
                "R_nm": {
                  "type": "number"
                },
                "Gamma_rel": {
                  "type": "number"
                }
              },
              "required": [
                "chi_ovl",
                "R_nm",
                "Gamma_rel"
              ]
            }
          },
          "chi_int_vs_R": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "chi_ovl": {
                  "type": "number"
                },
                "R_nm": {
                  "type": "number"
                },
                "chi_int": {
                  "type": "number"
                }
              },
              "required": [
                "chi_ovl",
                "R_nm",
                "chi_int"
              ]
            }
          },
          "chi_ovl_vs_R_fixed_chi_int": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "chi_int": {
                  "type": "number"
                },
                "R_nm": {
                  "type": "number"
                },
                "chi_ovl": {
                  "type": "number"
                }
              },
              "required": [
                "chi_int",
                "R_nm",
                "chi_ovl"
              ]
            }
          },
          "organics_effect": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "Po_Torr": {
                  "type": "number"
                },
                "R_nm": {
                  "type": "number"
                },
                "sigma_dyne_cm": {
                  "type": "number"
                }
              },
              "required": [
                "Po_Torr",
                "R_nm",
                "sigma_dyne_cm"
              ]
            }
          }
        },
        "required": [
          "sigma_vs_R",
          "Gamma_vs_R",
          "chi_int_vs_R",
          "chi_ovl_vs_R_fixed_chi_int",
          "organics_effect"
        ]
      },
      "description": "Size-dependent surface tension, excess coverage, internal mole fraction, overall mole fraction (for fixed internal composition), and organic contamination effect for aqueous HNO3 droplets at 193.15 K."
    }
  ],
  "notes": "The scored artifact contains arrays covering the paper's main headline quantities. The checker will compare the computed values to hidden reference data digitized from the paper's figures, using tolerances for surface tension (±2 dyne/cm), excess coverage (±0.05 relative), and mole fractions (±0.02), along with monotonicity trend checks."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each artifact you produce. For the scored step (`step_01_results.json`), the checker compares your computed numbers to a hidden reference solution derived from the same thermodynamic model under identical conditions. It evaluates absolute deviation within predetermined tolerances for surface tension, excess coverage, and mole fractions, and also verifies that the data obey the required monotonicity trends (e.g., as radius decreases, surface tension increases, excess coverage decreases, interior mole fraction decreases for fixed overall composition, etc.). The organics‑effect curves are checked for the correct ordering with varying organic pressure. The final reward is a weighted combination of these quantitative and structural checks; simply reporting values that happen to agree with some known result is not sufficient—you must genuinely compute them via the specified physical model.
