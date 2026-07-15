# Computing thermodynamic properties of alloys using Miedema-Bakker model

## Problem background
Predicting the thermodynamic properties of multicomponent alloys is central to materials design. The Miedema semi-empirical model, combined with Bakker's elastic energy expressions, provides a simple yet effective way to estimate mixing enthalpies and Gibbs free energies for solid solutions, amorphous phases, and intermetallic compounds. The MAAT (Materials Analysis Applying Thermodynamics) software implements these models with a built-in database of elemental parameters. This task targets reproducing the core computational pipeline: given the elemental parameters for the constituting elements and the model equations, compute the Gibbs free energy of mixing and related quantities for several specific alloy systems under defined temperature and field conditions.

## Approach
The approach uses the Miedema semi-empirical model, which estimates the enthalpy of mixing from elemental parameters: electronegativity φ*, electron density n_WS^(1/3), molar volume V_m, shear modulus G, bulk modulus K, and melting temperature T_m. The total enthalpy of mixing is the sum of three contributions: a chemical term (from electron density and electronegativity differences), an elastic mismatch term (from size and stiffness differences), and a structural term (from valence-electron structure). The Gibbs free energy of mixing is obtained by adding the ideal configurational entropy term (−TΔS^m, where ΔS^m = −R Σ x_i ln x_i). For ternary alloys, the binary mixing enthalpies are extrapolated to the ternary composition using Hillert's asymmetric method. For an amorphous phase, a topological enthalpy term is added and the elastic/structural contributions are omitted; for intermetallic compounds, only the chemical term is used. When an external centrifugal field is present, an additional energy term G_ef = 0.5 × PA_i × ρ^2 × ω^2 is included, with the radius ρ and angular velocity ω as given. The task is to implement this model, compute the required thermodynamic quantities at the specified compositions, temperatures, and centrifugal conditions, and write the results to a structured JSON file.

## Reproduction target
Implement the Miedema‑Bakker model and compute the following thermodynamic quantities (all in kJ/mol):

(1) Gibbs free energy of mixing ΔGm for a solid solution of Cu-7Cr-7Mo (at.%) at 298 K.

(2) ΔGm and Gibbs free energy of amorphous formation ΔGam for Ti-13Ta-12Sn (at.%) at 298 K.

(3) ΔGm and enthalpy of formation of the intermetallic compound ΔHf for Cu-7Nb-7Co (at.%) at 298 K.

(4) ΔGm for Cu-50Cr (wt.%) at 298 K and 503 K **without** centrifugal field, and ΔGm **with** centrifugal field (radius 150 mm, angular velocity 6000 rpm ≈ 628 rad/s, applied for 4 h) at 453 K and 503 K.

Report all computed values in a structured JSON file named `computed_thermodynamic_values.json` under `/app/outputs`. The JSON structure must follow the schema described in the output contract.

## Assets

- Miedema elemental parameters for 58 elements: https://doi.org/10.1016/0378-4363(80)90114-0

## Workflow steps

### Step 1: Load Miedema elemental parameters
- Role: process
- Action: Load the required Miedema and Bakker model parameters (electronegativity φ*, electron density n_WS^(1/3), molar volume V_m, shear modulus G, bulk modulus K, melting temperature T_m) for the elements Cu, Cr, Mo, Ti, Ta, Sn, Nb, Co from the publicly available Miedema database.
- Evidence: `/app/outputs/parameters.json`

### Step 2: Compute binary mixing enthalpies
- Role: process
- Action: For each binary pair (Cu-Mo, Cu-Cr, Mo-Cr, Ti-Ta, Ti-Sn, Ta-Sn, Cu-Co, Cu-Nb, Co-Nb, and Cu-Cr for centrifugal field analysis) compute the mixing enthalpy components (chemical ΔH_chem, elastic ΔH_elast, structural ΔH_struct) using the Miedema and Bakker equations, including the volume correction factor S(x) with M=1 for solid solutions. Compute enthalpy curves over the full composition range.
- Evidence: `/app/outputs/binary_enthalpies.json`

### Step 3: Compute target thermodynamic properties for all validation systems
- Role: scored (load-bearing)
- Action: Compute the following thermodynamic quantities using Hillert extrapolation for ternary systems and configurational entropy. Report all values in kJ/mol:
(1) Gibbs free energy of mixing ΔGm for Cu-7Cr-7Mo (at.%) at 298 K.
(2) ΔGm and Gibbs free energy of amorphous formation ΔGam for Ti-13Ta-12Sn (at.%) at 298 K.
(3) ΔGm and enthalpy of formation of intermetallic ΔHf for Cu-7Nb-7Co (at.%) at 298 K.
(4) ΔGm for Cu-50Cr (wt.%) at 298 K and 503 K without centrifugal field, and ΔGm with centrifugal field (radius 150 mm, angular velocity 6000 rpm corresponding to ~628 rad/s, duration 4 h) at 453 K and 503 K, using Eq. (25) for centrifugal contribution.
- Output file: `/app/outputs/computed_thermodynamic_values.json`
- Format: json
- Contract: {
  "Cu_7Cr_7Mo": { "dGm": "number" },
  "Ti_13Ta_12Sn": { "dGm": "number", "dGam": "number" },
  "Cu_7Nb_7Co": { "dGm": "number", "dHf": "number" },
  "Cu_50Cr": {
    "dGm_298K": "number",
    "dGm_503K": "number",
    "dGm_cf_453K": "number",
    "dGm_cf_503K": "number"
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_thermodynamic_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_thermodynamic_values.json
- path: `/app/outputs/computed_thermodynamic_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed thermodynamic values (Gibbs free energy, amorphous formation energy, intermetallic formation enthalpy, centrifugal-field modified free energy) for the four validation alloy systems, all in kJ/mol.
- schema:
  - `type`: object
  - `required`: `Cu_7Cr_7Mo`, `Ti_13Ta_12Sn`, `Cu_7Nb_7Co`, `Cu_50Cr`
  - `properties`:
    - `Cu_7Cr_7Mo`:
      - `type`: object
      - `required`: `dGm`
      - `properties`:
        - `dGm`:
          - `type`: number
          - `unit`: kJ/mol
    - `Ti_13Ta_12Sn`:
      - `type`: object
      - `required`: `dGm`, `dGam`
      - `properties`:
        - `dGm`:
          - `type`: number
          - `unit`: kJ/mol
        - `dGam`:
          - `type`: number
          - `unit`: kJ/mol
    - `Cu_7Nb_7Co`:
      - `type`: object
      - `required`: `dGm`, `dHf`
      - `properties`:
        - `dGm`:
          - `type`: number
          - `unit`: kJ/mol
        - `dHf`:
          - `type`: number
          - `unit`: kJ/mol
    - `Cu_50Cr`:
      - `type`: object
      - `required`: `dGm_298K`, `dGm_503K`, `dGm_cf_453K`, `dGm_cf_503K`
      - `properties`:
        - `dGm_298K`:
          - `type`: number
          - `unit`: kJ/mol
        - `dGm_503K`:
          - `type`: number
          - `unit`: kJ/mol
        - `dGm_cf_453K`:
          - `type`: number
          - `unit`: kJ/mol
        - `dGm_cf_503K`:
          - `type`: number
          - `unit`: kJ/mol

Notes: All values are in kJ/mol. Ternary systems use Hillert extrapolation. Centrifugal field parameters: radius=150 mm, angular velocity=6000 rpm (~628 rad/s), duration 4 h.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_thermodynamic_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Cu_7Cr_7Mo",
          "Ti_13Ta_12Sn",
          "Cu_7Nb_7Co",
          "Cu_50Cr"
        ],
        "properties": {
          "Cu_7Cr_7Mo": {
            "type": "object",
            "required": [
              "dGm"
            ],
            "properties": {
              "dGm": {
                "type": "number",
                "unit": "kJ/mol"
              }
            }
          },
          "Ti_13Ta_12Sn": {
            "type": "object",
            "required": [
              "dGm",
              "dGam"
            ],
            "properties": {
              "dGm": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "dGam": {
                "type": "number",
                "unit": "kJ/mol"
              }
            }
          },
          "Cu_7Nb_7Co": {
            "type": "object",
            "required": [
              "dGm",
              "dHf"
            ],
            "properties": {
              "dGm": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "dHf": {
                "type": "number",
                "unit": "kJ/mol"
              }
            }
          },
          "Cu_50Cr": {
            "type": "object",
            "required": [
              "dGm_298K",
              "dGm_503K",
              "dGm_cf_453K",
              "dGm_cf_503K"
            ],
            "properties": {
              "dGm_298K": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "dGm_503K": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "dGm_cf_453K": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "dGm_cf_503K": {
                "type": "number",
                "unit": "kJ/mol"
              }
            }
          }
        }
      },
      "description": "Computed thermodynamic values (Gibbs free energy, amorphous formation energy, intermetallic formation enthalpy, centrifugal-field modified free energy) for the four validation alloy systems, all in kJ/mol."
    }
  ],
  "notes": "All values are in kJ/mol. Ternary systems use Hillert extrapolation. Centrifugal field parameters: radius=150 mm, angular velocity=6000 rpm (~628 rad/s), duration 4 h."
}
```

## How you are scored
Each workflow stage produces an artifact. A hidden verifier independently recomputes the same thermodynamic quantities from the public model equations and elemental parameters. It compares your computed values (from `computed_thermodynamic_values.json`) against its own recomputed results and the paper-reported references using appropriate tolerances. Every scored stage contributes a weight to the final reward. Simply reporting the published numbers is not sufficient; you must demonstrate that your implementation yields values consistent with the verifier's independent recomputation.
