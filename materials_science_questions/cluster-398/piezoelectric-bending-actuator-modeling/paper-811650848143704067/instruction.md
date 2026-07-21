# Numerical buckling and post-buckling analysis of laminated FGM cylindrical shell with PFRC actuators

## Problem background
Hybrid laminated cylindrical shells composed of a functionally graded material (FGM) core and outer piezoelectric fiber reinforced composite (PFRC) actuator layers can serve in environments with combined thermal, electric, and axial compression loads. Predicting their stability is critical for design, but requires solving nonlinear mechanical and thermal fields together. This task addresses the computation of the critical axial buckling load and the post-buckling equilibrium paths (load versus end-shortening and load versus radial deflection) for such a shell. The shell geometry, constituent materials, and boundary temperatures are fully specified; the goal is to numerically determine the buckling loads and post-buckling response for several volume-fraction indices and thermal conditions.

## Approach
The analysis is based on Donnell shell theory with nonlinear strain-displacement relations. First, the temperature distribution through the shell thickness is obtained by solving the one-dimensional steady-state heat conduction equation with prescribed inner and outer surface temperatures and temperature-dependent thermal conductivities. Then, effective material properties are computed: the FGM layer follows a power-law distribution of ceramic and metal constituents, and the PFRC layers are modeled using micromechanics relations to obtain elastic, piezoelectric, and thermal expansion coefficients. These properties are used to assemble the overall membrane, coupling, and flexural stiffness matrices and the thermal/electric force and moment resultants. The total potential energy of the shell is expressed in terms of an assumed deflection function and an Airy stress function, and the Ritz energy method is applied to derive the governing nonlinear algebraic equations. From these equations, the linear critical buckling load (the smallest load at which a nontrivial equilibrium exists) is extracted, and the post-buckling load-shortening and load-deflection curves are traced by solving the nonlinear equilibrium relations incrementally.

## Reproduction target
Implement the numerical procedure outlined in the Workflow steps to produce the following results:

1. Critical buckling loads (P_cr) for a shell with length L = 3 m, mean radius R = 0.5 m, total thickness H = 0.005 m, FGM layer thickness h = 0.003 m, PFRC fiber volume fraction Vf = 0.6, and volume fraction indices k = 0, 2, 3, 4, under two thermal boundary conditions:
   - Case I: inner temperature Ti = 300 K, outer temperature To = 300 K.
   - Case II: Ti = 600 K, To = 300 K.

2. Post-buckling load-shortening and load-deflection curves for a shell with L = 0.5 m, H = 0.005 m, h = 0.003 m, Vf = 0.6, radius-to-thickness ratio R/H = 100, and k = 0.5, 2, 4, under the same case I and case II thermal conditions.

Save all computed results to a single JSON file.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute temperature distribution through thickness
- Role: process
- Action: Solve the 1D steady heat conduction equation through the thickness of the laminated shell with given outer and inner surface temperatures, layer thicknesses (H, h), and temperature-dependent thermal conductivities of FGM and PFRC. Obtain the piecewise temperature profiles and interface temperatures. Record the distribution in 'temperature_profile.txt'.
- Evidence: `/app/outputs/temperature_profile.txt`

### Step 2: Compute effective stiffness and resultants
- Role: process
- Action: Compute effective material properties for the FGM layer (power-law distribution, temperature-dependent coefficients) and for the PFRC layers (micromechanics formulas). Assemble the membrane, coupling, and flexural stiffness matrices (A, B, D) and the thermal and electric force/moment resultants by integrating through the thickness. Output the derived total stiffness coefficients and resultants to 'stiffness_parameters.json'.
- Evidence: `/app/outputs/stiffness_parameters.json`

### Step 3: Compute buckling and post-buckling results
- Role: scored (load-bearing)
- Action: Using the temperature distribution and stiffness coefficients, implement the Ritz energy method with the assumed deflection and stress function. Derive the nonlinear algebraic equations and compute: (1) linear critical buckling loads (P_cr) for the parameter sets L=3 m, R=0.5 m, H=0.005 m, h=0.003 m, Vf=0.6, k=0,2,3,4 under temperature case I (Ti=300K, To=300K) and case II (Ti=600K, To=300K); (2) post-buckling equilibrium paths (load-shortening and load-deflection curves) for the parameter sets L=0.5 m, H=0.005 m, h=0.003 m, Vf=0.6, R/H=100, k=0.5,2,4, under case I and case II. Save all results to 'results.json'.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"critical_buckling_loads": [{"Ti": float, "k": float, "Vf": float, "Pcr": float}], "post_buckling": [{"case": "I" or "II", "k": float, "load": [float], "shortening": [float], "deflection": [float]}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Critical buckling loads and post-buckling load-shortening and load-deflection curves computed by the Ritz energy method.
- schema:
  - `type`: object
  - `required`: `critical_buckling_loads`, `post_buckling`
  - `properties`:
    - `critical_buckling_loads`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `Ti`, `k`, `Vf`, `Pcr`
        - `properties`:
          - `Ti`:
            - `type`: number
            - `unit`: K
          - `k`:
            - `type`: number
            - `unit`: dimensionless
          - `Vf`:
            - `type`: number
            - `unit`: dimensionless
          - `Pcr`:
            - `type`: number
            - `unit`: N
    - `post_buckling`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `case`, `k`, `load`, `shortening`, `deflection`
        - `properties`:
          - `case`:
            - `type`: string
          - `k`:
            - `type`: number
            - `unit`: dimensionless
          - `load`:
            - `type`: array
            - `items`:
              - `type`: number
              - `unit`: N
          - `shortening`:
            - `type`: array
            - `items`:
              - `type`: number
              - `unit`: dimensionless
          - `deflection`:
            - `type`: array
            - `items`:
              - `type`: number
              - `unit`: m

Notes: The scored artifact contains the main numerical results of the reproduction: buckling loads for Table-3 conditions and post-buckling paths for Example-4 conditions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "critical_buckling_loads",
          "post_buckling"
        ],
        "properties": {
          "critical_buckling_loads": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "Ti",
                "k",
                "Vf",
                "Pcr"
              ],
              "properties": {
                "Ti": {
                  "type": "number",
                  "unit": "K"
                },
                "k": {
                  "type": "number",
                  "unit": "dimensionless"
                },
                "Vf": {
                  "type": "number",
                  "unit": "dimensionless"
                },
                "Pcr": {
                  "type": "number",
                  "unit": "N"
                }
              }
            }
          },
          "post_buckling": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "case",
                "k",
                "load",
                "shortening",
                "deflection"
              ],
              "properties": {
                "case": {
                  "type": "string"
                },
                "k": {
                  "type": "number",
                  "unit": "dimensionless"
                },
                "load": {
                  "type": "array",
                  "items": {
                    "type": "number",
                    "unit": "N"
                  }
                },
                "shortening": {
                  "type": "array",
                  "items": {
                    "type": "number",
                    "unit": "dimensionless"
                  }
                },
                "deflection": {
                  "type": "array",
                  "items": {
                    "type": "number",
                    "unit": "m"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Critical buckling loads and post-buckling load-shortening and load-deflection curves computed by the Ritz energy method."
    }
  ],
  "notes": "The scored artifact contains the main numerical results of the reproduction: buckling loads for Table-3 conditions and post-buckling paths for Example-4 conditions."
}
```

## How you are scored
A hidden verifier will independently inspect the outputs of each workflow stage. For the temperature profile and stiffness parameters, the verifier checks that the intermediate computations are internally consistent and physically plausible. The primary scoring is on the final results.json file: the critical buckling loads are compared to reference values, and the post-buckling curves are evaluated by interpolating the submitted load-shortening and load-deflection data at predefined displacement points and comparing the interpolated loads to reference loads. The verifier uses tolerances appropriate for numerical re-implementations of the theoretical model. Each scored stage contributes a weight toward the final reward; simply reporting a number without correctly executing the required computational procedure will not yield a passing score.
