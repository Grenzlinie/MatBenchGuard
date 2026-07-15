# 3D Phase-field simulation of martensitic transformation variant selection and junction plane analysis

## Problem background
Zirconia undergoes a tetragonal-to-monoclinic (T→M) martensitic transformation that produces a set of monoclinic variants with specific crystallographic relationships. Understanding which variants appear on a free surface and how they pack—the arrangement of variants and their interfaces—is critical to predicting transformation toughening and degradation in zirconia ceramics. However, variant selection and microstructural patterning emerge from a complex interplay of thermodynamics, kinetics, and elasticity that cannot be predicted by simple rules. This task uses a three-dimensional phase-field simulation to compute which monoclinic variants form when a tetragonal single crystal transforms with a free (001) surface, and to determine the crystallographic junction planes between adjacent variants. The outcome is a microstructural pattern that reflects strain accommodation and can be checked against crystallographic expectations.

## Approach
The model is a 3D Ginzburg–Landau phase-field description of the T→M transformation. The microstructure is represented by 12 non-conserved order parameters, one for each crystallographically distinct monoclinic variant. The total free energy combines a Landau polynomial chemical free energy (capturing the bulk thermodynamic driving force) and an elastic strain energy that accounts for the stress-free transformation strain of each variant and for elastic inhomogeneity between the tetragonal parent and the different monoclinic products. The order parameter evolution follows the Allen–Cahn equation, coupled to the mechanical equilibrium condition. The simulation domain is a 1 µm × 1 µm × 1 µm tetragonal single crystal with a free top surface (001)_t and fixed boundaries elsewhere. A small embryo containing all 12 variants is placed near the free surface, and the system is allowed to evolve until the microstructure stabilizes. From the final order parameter fields, the set of monoclinic variants present on the free surface is identified, and the Miller indices (in the tetragonal reference frame) of the planes separating adjacent variants (junction planes) are computed.

## Reproduction target
After executing the full phase-field simulation and analyzing the final order parameter fields, produce a structured JSON file that reports (1) the list of monoclinic variant labels (string names) that appear on the free (001)_t surface, and (2) for each pair of adjacent variants, the Miller indices (three integers) of their junction plane expressed in the tetragonal coordinate system. The simulation must be run with the material parameters and initial conditions specified in the workflow steps; the JSON output must conform to the schema described in the output contract.

## Assets

- FEniCS (or alternative open-source finite element/phase-field solver): https://fenicsproject.org/

## Workflow steps

### Step 1: Prepare material and model parameters
- Role: process
- Action: Calculate the chemical driving force ΔG at T=1170 K from the Gibbs free energy functions for tetragonal and monoclinic zirconia. Compute the stress-free strain tensors for all 12 monoclinic variants using the provided lattice parameters and deformation gradient formulas. Compute the rotated monoclinic elastic stiffness tensors for each variant. Determine the Landau polynomial parameters, gradient energy coefficient β, and kinetic coefficient L.
- Evidence: none

### Step 2: Run 3D phase-field simulation
- Role: process
- Action: Implement the 3D phase-field model (Allen–Cahn kinetics for 12 order parameters coupled to mechanical equilibrium) in an open-source finite element solver. Set up a 1×1×1 µm single-crystal domain with a free (001)_t top surface and fixed boundaries on the other faces. Initialize with a multivariant embryo containing all 12 variants. Solve the time-dependent PDE until the microstructure stabilizes.
- Evidence: none

### Step 3: Identify variants on free surface and junction planes
- Role: scored (load-bearing)
- Action: From the final order parameter fields, determine which monoclinic variants are present on the free (001)_t surface (order parameter η≈1). For each pair of adjacent variants, compute the Miller indices of the junction plane in the tetragonal coordinate frame. Output the results as a JSON file.
- Output file: `/app/outputs/step_01_variant_report.json`
- Format: json
- Contract: type=object; required=['variants_on_free_surface', 'junction_planes']; properties={'variants_on_free_surface': {'type': 'array', 'items': {'type': 'string'}}, 'junction_planes': {'type': 'array', 'items': {'type': 'object', 'required': ['variant_pair', 'plane_indices'], 'properties': {'variant_pair': {'type': 'array', 'minItems': 2, 'maxItems': 2, 'items': {'type': 'string'}}, 'plane_indices': {'type': 'array', 'minItems': 3, 'maxItems': 3, 'items': {'type': 'integer'}}}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_variant_report.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_variant_report.json
- path: `/app/outputs/step_01_variant_report.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Scored artifact containing the list of monoclinic variants present on the free (001)_t surface and the Miller indices (in the tetragonal frame) of junction planes between adjacent variants.
- schema:
  - `type`: object
  - `required`: `variants_on_free_surface`, `junction_planes`
  - `properties`:
    - `variants_on_free_surface`:
      - `type`: array
      - `items`:
        - `type`: string
    - `junction_planes`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `variant_pair`, `plane_indices`
        - `properties`:
          - `variant_pair`:
            - `type`: array
            - `minItems`: 2
            - `maxItems`: 2
            - `items`:
              - `type`: string
          - `plane_indices`:
            - `type`: array
            - `minItems`: 3
            - `maxItems`: 3
            - `items`:
              - `type`: integer

Notes: The checker will verify that the reported variants correspond to correspondence C and that the junction plane Miller indices belong to the {100}_t or {110}_t families. Flexible naming conventions are accepted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_variant_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "variants_on_free_surface",
          "junction_planes"
        ],
        "properties": {
          "variants_on_free_surface": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "junction_planes": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "variant_pair",
                "plane_indices"
              ],
              "properties": {
                "variant_pair": {
                  "type": "array",
                  "minItems": 2,
                  "maxItems": 2,
                  "items": {
                    "type": "string"
                  }
                },
                "plane_indices": {
                  "type": "array",
                  "minItems": 3,
                  "maxItems": 3,
                  "items": {
                    "type": "integer"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Scored artifact containing the list of monoclinic variants present on the free (001)_t surface and the Miller indices (in the tetragonal frame) of junction planes between adjacent variants."
    }
  ],
  "notes": "The checker will verify that the reported variants correspond to correspondence C and that the junction plane Miller indices belong to the {100}_t or {110}_t families. Flexible naming conventions are accepted."
}
```

## How you are scored
A hidden verifier reads the submitted `/app/outputs/step_01_variant_report.json`. It checks the set of variants reported on the free surface: the correct expected outcome is that only variants belonging to crystallographic correspondence C appear. The verifier also checks that every reported junction plane’s Miller indices belong to the families `{100}_t` or `{110}_t` (one index equals ±1 and the others 0, or two indices equal ±1 and the third 0). Flexible naming conventions and sign/order variations within these rules are accepted. Full credit requires both conditions to be met. If the variant set is correct but some junction planes deviate from the allowed families, partial credit is awarded. The verifier does not compare absolute surface profiles or quantitative geometry; it only audits the crystallographic structure of the reported variants and planes.
