# Analytical Navier Solution for CNTRC Beam Bending, Buckling and Vibration

## Problem background
Carbon nanotube-reinforced composite (CNTRC) beams are promising lightweight structural elements in aerospace and mechanical engineering. Predicting their mechanical response — bending deflections, stresses, buckling loads, and vibration frequencies — under different reinforcement distributions and elastic foundation conditions is essential for design and analysis. This task requires implementing a computational model to analyze the mechanical behavior of such beams.

## Approach
The CNTRC beam is modeled using a higher-order shear deformation beam theory that accounts for transverse shear distribution through the thickness. Effective material properties (elastic moduli, Poisson's ratio, density) are estimated via the rule of mixture, incorporating size-dependent CNT efficiency parameters calibrated for different carbon nanotube volume fractions. The carbon nanotubes are distributed across the thickness in four patterns: uniform (UD), and functionally graded distributions denoted O, X, and V. The governing equations of motion are derived from Hamilton's principle and simplified to a set of algebraic equations via the Navier solution for simply supported boundary conditions. The bending problem is solved for applied transverse loads (uniform and sinusoidal) while buckling and free vibration are treated as eigenvalue problems. The computed results are reported in dimensionless form to facilitate comparison.

## Reproduction target
Implement a Python program that, for a given CNT distribution pattern (UD, O, X, V), volume fraction, beam geometry, and elastic foundation stiffness, computes the dimensionless transverse displacement (w̄), axial displacement (ū), normal stress (σ̄x), and shear stress (σ̄xz) for static bending; the dimensionless critical buckling load (N̄x0); and the fundamental natural frequency (ω̄). First validate the implementation by reproducing known solutions for a homogeneous isotropic beam and a functionally graded (alumina‑aluminum) beam. Then evaluate the program on the specified loading, boundary, and material configurations detailed in the workflow steps.

## Assets

- SWCNT and PMMA material properties
- CNT efficiency parameters ηi for each Vcnt*
- Validation case material properties (alumina and aluminum)

## Workflow steps

### Step 1: Define CNT distribution and effective material properties
- Role: process
- Action: Implement the CNT volume fraction distributions for UD, O, X, V patterns and compute through-thickness effective elastic moduli (E11, E22, G12), Poisson’s ratio, density, and reduced stiffnesses Q11, Q55 using the rule of mixture with CNT efficiency parameters.
- Evidence: none

### Step 2: Compute sectional stiffness and mass integrals
- Role: process
- Action: Select a higher‑order shear deformation theory (e.g., TSDT) and numerically integrate the effective properties over the beam thickness to obtain the stiffness coefficients A11, B11, D11, C11, E11, H11, A55 and the mass moments I0..I5. Write the resulting integrals for each relevant CNT distribution and volume fraction to a JSON evidence file for traceability.
- Evidence: `/app/outputs/sectional_integrals.json`

### Step 3: Validation: isotropic and FG beam bending
- Role: scored (load-bearing)
- Action: Implement the Navier solution for a simply supported beam under uniform load. Use the provided material properties for a homogeneous isotropic beam (p=0) and a functionally graded alumina‑aluminum beam (p=1.0), L/h=20. Compute the dimensionless transverse displacement (w̄), axial displacement (ū), normal stress (σ̄x) and shear stress (σ̄xz) and write them to the output file.
- Output file: `/app/outputs/step_00_validation.json`
- Format: json
- Contract: A JSON array of two objects, each with keys: beam_type (string), p (integer), L_h (integer), w_bar (float), u_bar (float), sigma_x_bar (float), sigma_xz_bar (float). The first object is for beam_type='isotropic', p=0; the second for beam_type='FG', p=1.
- Scoring: scored by hidden verifier

### Step 4: Bending analysis of UD CNTRC beams
- Role: scored
- Action: For a UD CNTRC beam with Vcnt*=0.12 and L/h=20, compute the dimensionless bending outputs (w̄, ū, σ̄x, σ̄xz) under uniform load without foundation (βw=0, βs=0) and with foundation (βw=0.1, βs=0.02), and under sinusoidal load without foundation. Use the TSDT. Write all results to the output file.
- Output file: `/app/outputs/step_01_bending.json`
- Format: json
- Contract: A JSON array of three objects, each with keys: beam_type (string), L_h (integer), Vcnt_star (float), load_type (string: 'uniform' or 'sinusoidal'), foundation (string: 'none' or 'with'), beta_w (float), beta_s (float), w_bar (float), u_bar (float), sigma_x_bar (float), sigma_xz_bar (float).
- Scoring: scored by hidden verifier

### Step 5: Buckling analysis of CNTRC beams
- Role: scored
- Action: For UD, O, and X CNTRC beams with Vcnt*=0.12 and L/h=15, compute the dimensionless critical buckling load N̄x0 under no-foundation (βw=0, βs=0) and with-foundation (βw=0.1, βs=0.02) conditions. Use TSDT. Write results to the output file.
- Output file: `/app/outputs/step_02_buckling.json`
- Format: json
- Contract: A JSON array of six objects, each with keys: beam_type (string), L_h (integer), Vcnt_star (float), foundation (string), beta_w (float), beta_s (float), N_bar (float).
- Scoring: scored by hidden verifier

### Step 6: Vibration analysis of CNTRC beams
- Role: scored
- Action: For UD, O, X, and V CNTRC beams with Vcnt*=0.12 and L/h=15, compute the dimensionless fundamental natural frequency ω̄ under no-foundation (βw=0, βs=0) and with-foundation (βw=0.1, βs=0.02) conditions. Use TSDT. Write results to the output file.
- Output file: `/app/outputs/step_03_vibration.json`
- Format: json
- Contract: A JSON array of eight objects, each with keys: beam_type (string), L_h (integer), Vcnt_star (float), foundation (string), beta_w (float), beta_s (float), omega_bar (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_00_validation.json`
- `/app/outputs/step_01_bending.json`
- `/app/outputs/step_02_buckling.json`
- `/app/outputs/step_03_vibration.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_00_validation.json
- path: `/app/outputs/step_00_validation.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Validation bending results for isotropic (p=0) and FG (p=1) beams, L/h=20, uniform load.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `beam_type`, `p`, `L_h`, `w_bar`, `u_bar`, `sigma_x_bar`, `sigma_xz_bar`
    - `properties`:
      - `beam_type`:
        - `type`: string
      - `p`:
        - `type`: integer
      - `L_h`:
        - `type`: integer
      - `w_bar`:
        - `type`: number
      - `u_bar`:
        - `type`: number
      - `sigma_x_bar`:
        - `type`: number
      - `sigma_xz_bar`:
        - `type`: number

### step_01_bending.json
- path: `/app/outputs/step_01_bending.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Bending analysis of UD CNTRC beams with Vcnt*=0.12, L/h=20 under various loads and foundation conditions.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `beam_type`, `L_h`, `Vcnt_star`, `load_type`, `foundation`, `beta_w`, `beta_s`, `w_bar`, `u_bar`, `sigma_x_bar`, `sigma_xz_bar`
    - `properties`:
      - `beam_type`:
        - `type`: string
      - `L_h`:
        - `type`: integer
      - `Vcnt_star`:
        - `type`: number
      - `load_type`:
        - `type`: string
        - `enum`: `uniform`, `sinusoidal`
      - `foundation`:
        - `type`: string
        - `enum`: `none`, `with`
      - `beta_w`:
        - `type`: number
      - `beta_s`:
        - `type`: number
      - `w_bar`:
        - `type`: number
      - `u_bar`:
        - `type`: number
      - `sigma_x_bar`:
        - `type`: number
      - `sigma_xz_bar`:
        - `type`: number

### step_02_buckling.json
- path: `/app/outputs/step_02_buckling.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Buckling loads for UD, O, X CNTRC beams with Vcnt*=0.12, L/h=15.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `beam_type`, `L_h`, `Vcnt_star`, `foundation`, `beta_w`, `beta_s`, `N_bar`
    - `properties`:
      - `beam_type`:
        - `type`: string
      - `L_h`:
        - `type`: integer
      - `Vcnt_star`:
        - `type`: number
      - `foundation`:
        - `type`: string
        - `enum`: `none`, `with`
      - `beta_w`:
        - `type`: number
      - `beta_s`:
        - `type`: number
      - `N_bar`:
        - `type`: number

### step_03_vibration.json
- path: `/app/outputs/step_03_vibration.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fundamental natural frequencies for UD, O, X, V CNTRC beams with Vcnt*=0.12, L/h=15.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `beam_type`, `L_h`, `Vcnt_star`, `foundation`, `beta_w`, `beta_s`, `omega_bar`
    - `properties`:
      - `beam_type`:
        - `type`: string
      - `L_h`:
        - `type`: integer
      - `Vcnt_star`:
        - `type`: number
      - `foundation`:
        - `type`: string
        - `enum`: `none`, `with`
      - `beta_w`:
        - `type`: number
      - `beta_s`:
        - `type`: number
      - `omega_bar`:
        - `type`: number

Notes: The hidden checker compares each submitted numeric value to the paper‑reported reference values using an appropriate tolerance. The V‑beam does not exhibit bifurcation buckling and is therefore not included in the buckling step. The chosen shear deformation theory can be any of the higher‑order ones listed in the instruction; TSDT is recommended.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_00_validation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "beam_type",
            "p",
            "L_h",
            "w_bar",
            "u_bar",
            "sigma_x_bar",
            "sigma_xz_bar"
          ],
          "properties": {
            "beam_type": {
              "type": "string"
            },
            "p": {
              "type": "integer"
            },
            "L_h": {
              "type": "integer"
            },
            "w_bar": {
              "type": "number"
            },
            "u_bar": {
              "type": "number"
            },
            "sigma_x_bar": {
              "type": "number"
            },
            "sigma_xz_bar": {
              "type": "number"
            }
          }
        }
      },
      "description": "Validation bending results for isotropic (p=0) and FG (p=1) beams, L/h=20, uniform load."
    },
    {
      "file": "step_01_bending.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "beam_type",
            "L_h",
            "Vcnt_star",
            "load_type",
            "foundation",
            "beta_w",
            "beta_s",
            "w_bar",
            "u_bar",
            "sigma_x_bar",
            "sigma_xz_bar"
          ],
          "properties": {
            "beam_type": {
              "type": "string"
            },
            "L_h": {
              "type": "integer"
            },
            "Vcnt_star": {
              "type": "number"
            },
            "load_type": {
              "type": "string",
              "enum": [
                "uniform",
                "sinusoidal"
              ]
            },
            "foundation": {
              "type": "string",
              "enum": [
                "none",
                "with"
              ]
            },
            "beta_w": {
              "type": "number"
            },
            "beta_s": {
              "type": "number"
            },
            "w_bar": {
              "type": "number"
            },
            "u_bar": {
              "type": "number"
            },
            "sigma_x_bar": {
              "type": "number"
            },
            "sigma_xz_bar": {
              "type": "number"
            }
          }
        }
      },
      "description": "Bending analysis of UD CNTRC beams with Vcnt*=0.12, L/h=20 under various loads and foundation conditions."
    },
    {
      "file": "step_02_buckling.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "beam_type",
            "L_h",
            "Vcnt_star",
            "foundation",
            "beta_w",
            "beta_s",
            "N_bar"
          ],
          "properties": {
            "beam_type": {
              "type": "string"
            },
            "L_h": {
              "type": "integer"
            },
            "Vcnt_star": {
              "type": "number"
            },
            "foundation": {
              "type": "string",
              "enum": [
                "none",
                "with"
              ]
            },
            "beta_w": {
              "type": "number"
            },
            "beta_s": {
              "type": "number"
            },
            "N_bar": {
              "type": "number"
            }
          }
        }
      },
      "description": "Buckling loads for UD, O, X CNTRC beams with Vcnt*=0.12, L/h=15."
    },
    {
      "file": "step_03_vibration.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "beam_type",
            "L_h",
            "Vcnt_star",
            "foundation",
            "beta_w",
            "beta_s",
            "omega_bar"
          ],
          "properties": {
            "beam_type": {
              "type": "string"
            },
            "L_h": {
              "type": "integer"
            },
            "Vcnt_star": {
              "type": "number"
            },
            "foundation": {
              "type": "string",
              "enum": [
                "none",
                "with"
              ]
            },
            "beta_w": {
              "type": "number"
            },
            "beta_s": {
              "type": "number"
            },
            "omega_bar": {
              "type": "number"
            }
          }
        }
      },
      "description": "Fundamental natural frequencies for UD, O, X, V CNTRC beams with Vcnt*=0.12, L/h=15."
    }
  ],
  "notes": "The hidden checker compares each submitted numeric value to the paper‑reported reference values using an appropriate tolerance. The V‑beam does not exhibit bifurcation buckling and is therefore not included in the buckling step. The chosen shear deformation theory can be any of the higher‑order ones listed in the instruction; TSDT is recommended."
}
```

## How you are scored
A hidden verifier independently scores each scored output file (step_00_validation.json, step_01_bending.json, step_02_buckling.json, step_03_vibration.json). It compares the dimensionless values you write to hidden reference values derived from the original study. Each stage carries a weight, and the total reward is the weighted sum of stage scores. Reporting the correct numbers is not sufficient; your implementation must produce them from the described analytical procedure. The verifier does not inspect intermediate artifacts or code quality—it only examines the final output files.
