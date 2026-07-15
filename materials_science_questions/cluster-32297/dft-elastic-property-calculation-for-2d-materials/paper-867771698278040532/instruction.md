# DFT-Based Elastic and Auxetic Property Calculation for a 2D Monolayer

## Problem background
Two-dimensional (2D) materials can display unusual mechanical properties, such as a negative Poisson’s ratio (auxetic behavior), where a material expands transversely when stretched, and highly anisotropic elastic responses. Understanding and computing these properties is crucial for designing nanoscale electromechanical devices. Certain monolayer phosphorus allotropes with puckered structures are predicted to be promising auxetic materials. This task focuses on evaluating the in-plane elastic stiffness constants and the resulting Young’s moduli and Poisson’s ratios of the δ-phosphorene monolayer.

## Approach
The mechanical properties are obtained from first-principles calculations. Using an open‑source plane‑wave density functional theory (DFT) code, perform a geometry relaxation of the monolayer δ‑P with the PBE exchange‑correlation functional and the DFT‑D2 van der Waals correction. Then, perform a series of total‑energy calculations on the relaxed cell under small in‑plane strain deformations (normal and shear). Fit the total energy as a quadratic function of the strain tensor components to extract the four in‑plane elastic stiffness constants C11, C22, C12, C66. From these constants, derive the direction‑dependent in‑plane Young’s moduli (Ex, Ey) and Poisson’s ratios (vxy, vyx) using the plane‑stress orthotropic relations.

## Reproduction target
Produce two JSON files under `/app/outputs`: (1) `elastic_constants.json` containing the four elastic stiffness constants C11, C22, C12, C66 (in GPa) for the monolayer δ‑P; (2) `mechanical_properties.json` containing the derived Young’s moduli Ex, Ey (GPa) and Poisson’s ratios vxy, vyx. The values must be computed from the strain‑energy fitting and the plane‑stress formulas, not copied from any reference. The final output should faithfully reflect the mechanical properties of δ‑phosphorene as obtained from a consistent DFT workflow.

## Assets

- Quantum ESPRESSO (open‑source DFT code): https://www.quantum-espresso.org/
- PBE pseudopotentials for phosphorus (e.g., SSSP library): https://www.materialscloud.org/discover/sssp/
- Initial crystal structure of the monolayer (CIF file): https://doi.org/10.1103/PhysRevLett.113.046804

## Workflow steps

### Step 1: DFT Geometry Relaxation
- Role: process
- Action: Perform DFT geometry optimization on the monolayer using the provided initial crystal structure and an open‑source DFT code (e.g., Quantum ESPRESSO) with the PBE exchange‑correlation functional and DFT‑D2 van der Waals correction. Write the relaxed structure as a .cif file.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 2: Compute Elastic Stiffness Constants
- Role: scored (load-bearing)
- Action: Perform DFT total‑energy calculations for a grid of in‑plane strained configurations of the relaxed monolayer cell. Fit the total energy vs. strain to a quadratic form to extract the in‑plane elastic stiffness constants C11, C22, C12, C66 (in GPa). Save the results to elastic_constants.json.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"C11": number, "C22": number, "C12": number, "C66": number, "units": "GPa"}
- Scoring: scored by hidden verifier

### Step 3: Calculate Young’s Modulus and Poisson’s Ratio
- Role: scored (load-bearing)
- Action: From the elastic stiffness constants, apply the plane‑stress orthotropic formulas to compute the in‑plane Young’s moduli Ex, Ey and Poisson’s ratios vxy, vyx. Write the results to mechanical_properties.json.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: {"Ex": number, "Ey": number, "vxy": number, "vyx": number, "units_Ex": "GPa", "units_Ey": "GPa"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/mechanical_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: In‑plane elastic stiffness constants in GPa.
- schema:
  - `type`: object
  - `required`: `C11`, `C22`, `C12`, `C66`, `units`
  - `units`:
    - `C11`: GPa
    - `C22`: GPa
    - `C12`: GPa
    - `C66`: GPa

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Young’s moduli Ex, Ey (GPa) and Poisson’s ratios vxy, vyx.
- schema:
  - `type`: object
  - `required`: `Ex`, `Ey`, `vxy`, `vyx`, `units_Ex`, `units_Ey`
  - `units`:
    - `Ex`: GPa
    - `Ey`: GPa
    - `vxy`: dimensionless
    - `vyx`: dimensionless

Notes: The checker verifies mechanical stability (C11*C22 – C12^2 > 0 and all diagonal constants > 0) from elastic_constants.json. It recomputes Ex, Ey, vxy, vyx from the constants and cross‑checks consistency with the values in mechanical_properties.json. The final reward compares the mechanical_properties.json entries against the paper’s reference values within a hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "C11",
          "C22",
          "C12",
          "C66",
          "units"
        ],
        "units": {
          "C11": "GPa",
          "C22": "GPa",
          "C12": "GPa",
          "C66": "GPa"
        }
      },
      "description": "In‑plane elastic stiffness constants in GPa."
    },
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Ex",
          "Ey",
          "vxy",
          "vyx",
          "units_Ex",
          "units_Ey"
        ],
        "units": {
          "Ex": "GPa",
          "Ey": "GPa",
          "vxy": "dimensionless",
          "vyx": "dimensionless"
        }
      },
      "description": "Young’s moduli Ex, Ey (GPa) and Poisson’s ratios vxy, vyx."
    }
  ],
  "notes": "The checker verifies mechanical stability (C11*C22 – C12^2 > 0 and all diagonal constants > 0) from elastic_constants.json. It recomputes Ex, Ey, vxy, vyx from the constants and cross‑checks consistency with the values in mechanical_properties.json. The final reward compares the mechanical_properties.json entries against the paper’s reference values within a hidden tolerance."
}
```

## How you are scored
A hidden verifier inspects the submitted JSON files. It first checks that `elastic_constants.json` is properly formed and that the constants satisfy mechanical stability conditions (C11>0, C22>0, C66>0, C11·C22 – C12^2 > 0). Then it recomputes Ex, Ey, vxy, vyx from the Cij values of `elastic_constants.json` and verifies that these recomputed values agree with those in `mechanical_properties.json` to within a tight tolerance. Finally, it compares the computed Young’s moduli and Poisson’s ratios against hidden reference values (derived from the original study) using appropriate tolerances. The overall score is a weighted sum of these checks; reporting the paper’s numbers without deriving them from your own DFT strain‑energy fit will not pass the verifier’s consistency tests.
