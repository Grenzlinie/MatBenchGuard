# Fractured RVE Homogenization with Non-Zero Fracture Poisson's Ratio

## Problem background
Naturally fractured reservoirs are modeled by homogenizing the elastic properties of a representative volume element (RVE) consisting of a rock matrix and multiple sets of parallel fractures. Classical semi‑analytical models replace each fracture by elastic springs with uncoupled normal and shear stiffnesses; they neglect the coupling between normal and shear deformations. This work generalizes the model by treating fractures as thin elastic layers that can have a non‑zero Poisson’s ratio, which captures the effect of normal stress producing lateral strain (and vice versa). As a result, the effective Young’s modulus of the fractured rock mass can differ from the uncoupled case. The task reproduces the homogenization for a periodic RVE containing three equally spaced parallel fracture planes normal to the x‑axis with spacing 1/3, and no fractures in the y and z directions. It evaluates the effect of the fracture Poisson’s ratio on the effective elastic moduli.

## Approach
A 3D finite‑element model of a unit cube is built. Three parallel planar fractures normal to the x‑axis, equally spaced with a spacing of 1/3, are modeled as thin elastic layers with a given normal stiffness (kn), shear stiffness (ks), and thickness (t). The fracture layer is assigned a Young’s modulus E_f = kn * t and a Poisson’s ratio ν_f (initially 0). The rock matrix is linear‑elastic and isotropic (E=100 GPa, ν=0.3). Periodic boundary conditions are applied, and six independent small‑strain deformation modes (three uniaxial, three shear) are solved. For each mode, the volume‑averaged stresses are computed to build the effective stiffness tensor; from it the effective Young’s moduli E_xx, E_yy, E_zz and shear moduli G_xy, G_xz, G_yz are extracted. The entire procedure is repeated with the fracture Poisson’s ratio set to 0.3, so that the influence of the coupling can be quantified. FEniCS (an open‑source FE library) is used to generate the mesh and solve the linear elasticity problems.

## Reproduction target
Produce a JSON file (`effective_moduli.json`) containing the effective elastic moduli for the fractured RVE under two conditions: (i) fracture Poisson’s ratio ν_f = 0 (base case), and (ii) fracture Poisson’s ratio ν_f = 0.3. For each case report the six independent engineering constants — E_11, E_22, E_33, G_12, G_13, G_23 — and also compute and report the percentage change in the Young’s modulus in the direction normal to the first fracture set (i.e., 100 × (E_11(ν_f=0.3) − E_11(ν_f=0)) / E_11(ν_f=0)). The required output schema is given in the workflow steps section.

## Assets

- FEniCS finite element library: https://fenicsproject.org/
- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Generate FE mesh of the fractured periodic RVE
- Role: process
- Action: Construct a 3D unit cube geometry with three parallel planar fractures normal to the x‑axis, equally spaced with spacing 1/3, modeled as thin layers. Define matrix material (E=100 GPa, ν=0.3) and fracture layer parameters (normal stiffness kn=20 GPa/m, shear stiffness ks=kn/2, thickness t=0.001). Assign the fracture material as a linear elastic solid with Young's modulus E_f = kn * t and Poisson's ratio ν_f (initially 0). Generate a conforming hexahedral mesh using FEniCS that resolves the fracture thickness with at least one element through-the-thickness. Save mesh information to evidence file.
- Evidence: `/app/outputs/mesh_info.txt`

### Step 2: Homogenization and effective moduli computation
- Role: scored (load-bearing)
- Action: For the base case (ν_f = 0): apply periodic boundary conditions, solve the linear elastic FE problem for six independent deformation modes (three uniaxial, three shear) under small strains. Compute volume-averaged stresses and derive the effective stiffness tensor, then extract the effective Young's moduli E_xx, E_yy, E_zz and shear moduli G_xy, G_xz, G_yz. Next, set ν_f = 0.3 (keeping other parameters) and repeat the entire homogenization. Record all extracted moduli and the percentage change in E_xx (relative to the base case) in a JSON file.
- Output file: `/app/outputs/effective_moduli.json`
- Format: json
- Contract: {
  "base_case": {
    "fracture_nu": 0.0,
    "E11": float,
    "E22": float,
    "E33": float,
    "G12": float,
    "G13": float,
    "G23": float
  },
  "nonzero_nu_case": {
    "fracture_nu": 0.3,
    "E11": float,
    "E22": float,
    "E33": float,
    "G12": float,
    "G13": float,
    "G23": float
  },
  "percent_change_E11": float
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_moduli.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_moduli.json
- path: `/app/outputs/effective_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Effective elastic moduli for the fractured RVE with fracture Poisson's ratio 0 and 0.3, plus the relative increase in E11.
- schema:
  - `type`: object
  - `required`: `base_case`, `nonzero_nu_case`, `percent_change_E11`
  - `properties`:
    - `base_case`:
      - `type`: object
      - `required`: `fracture_nu`, `E11`, `E22`, `E33`, `G12`, `G13`, `G23`
      - `properties`:
        - `fracture_nu`:
          - `type`: number
        - `E11`:
          - `type`: number
          - `units`: Pa
        - `E22`:
          - `type`: number
          - `units`: Pa
        - `E33`:
          - `type`: number
          - `units`: Pa
        - `G12`:
          - `type`: number
          - `units`: Pa
        - `G13`:
          - `type`: number
          - `units`: Pa
        - `G23`:
          - `type`: number
          - `units`: Pa
    - `nonzero_nu_case`:
      - `type`: object
      - `required`: `fracture_nu`, `E11`, `E22`, `E33`, `G12`, `G13`, `G23`
      - `properties`:
        - `fracture_nu`:
          - `type`: number
        - `E11`:
          - `type`: number
          - `units`: Pa
        - `E22`:
          - `type`: number
          - `units`: Pa
        - `E33`:
          - `type`: number
          - `units`: Pa
        - `G12`:
          - `type`: number
          - `units`: Pa
        - `G13`:
          - `type`: number
          - `units`: Pa
        - `G23`:
          - `type`: number
          - `units`: Pa
    - `percent_change_E11`:
      - `type`: number

Notes: The checker compares the reported base-case moduli to analytical solutions within tolerance and verifies that E11 for ν_f=0.3 is at least 20% higher than the base case. Only the scored artifact effective_moduli.json is evaluated.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "base_case",
          "nonzero_nu_case",
          "percent_change_E11"
        ],
        "properties": {
          "base_case": {
            "type": "object",
            "required": [
              "fracture_nu",
              "E11",
              "E22",
              "E33",
              "G12",
              "G13",
              "G23"
            ],
            "properties": {
              "fracture_nu": {
                "type": "number"
              },
              "E11": {
                "type": "number",
                "units": "Pa"
              },
              "E22": {
                "type": "number",
                "units": "Pa"
              },
              "E33": {
                "type": "number",
                "units": "Pa"
              },
              "G12": {
                "type": "number",
                "units": "Pa"
              },
              "G13": {
                "type": "number",
                "units": "Pa"
              },
              "G23": {
                "type": "number",
                "units": "Pa"
              }
            }
          },
          "nonzero_nu_case": {
            "type": "object",
            "required": [
              "fracture_nu",
              "E11",
              "E22",
              "E33",
              "G12",
              "G13",
              "G23"
            ],
            "properties": {
              "fracture_nu": {
                "type": "number"
              },
              "E11": {
                "type": "number",
                "units": "Pa"
              },
              "E22": {
                "type": "number",
                "units": "Pa"
              },
              "E33": {
                "type": "number",
                "units": "Pa"
              },
              "G12": {
                "type": "number",
                "units": "Pa"
              },
              "G13": {
                "type": "number",
                "units": "Pa"
              },
              "G23": {
                "type": "number",
                "units": "Pa"
              }
            }
          },
          "percent_change_E11": {
            "type": "number"
          }
        }
      },
      "description": "Effective elastic moduli for the fractured RVE with fracture Poisson's ratio 0 and 0.3, plus the relative increase in E11."
    }
  ],
  "notes": "The checker compares the reported base-case moduli to analytical solutions within tolerance and verifies that E11 for ν_f=0.3 is at least 20% higher than the base case. Only the scored artifact effective_moduli.json is evaluated."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/effective_moduli.json`. For the base case (ν_f=0), the verifier compares the reported Young’s and shear moduli to analytical reference values derived from the given material and fracture parameters, checking that they lie within a specified tolerance. For the non‑zero ν_f case, the verifier evaluates the relative increase in E_11 to confirm that the coupling effect is significant. The verifier also checks that, in the base case, E_22 and E_33 are close to the matrix Young’s modulus, consistent with theoretical predictions. The final reward is a weighted combination of these checks. Simply reporting numbers without correctly running the finite‑element homogenization pipeline will not produce the necessary results.
