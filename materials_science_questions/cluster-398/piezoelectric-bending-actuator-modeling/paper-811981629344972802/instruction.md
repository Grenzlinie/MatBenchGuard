# Dislocation-induced birefringence in anisotropic piezoelectric crystals

## Problem background
Dislocations in anisotropic piezoelectric crystals generate mechanical stress and electric fields. Through the elasto-optic and electro-optic effects, these fields locally alter the refractive index, creating inhomogeneities that can degrade the optical quality of high‑precision components. In real crystals such as ADP, KDP and α‑quartz, the coupled electromechanical behavior makes it impossible to estimate these index variations with simple isotropic models. A numerical procedure based on the Eshelby method solves the coupled elastic and electric field equations for a straight dislocation in an infinite medium, providing the stress and electric field distributions, from which the refractive index change and birefringence can be computed. This task quantifies the resulting maximum birefringence and detection distances for a set of characteristic dislocation types in those materials.

## Approach
To model a straight dislocation in an anisotropic piezoelectric crystal, one must simultaneously solve the coupled equations of linear elasticity and electrostatics, which are linked through the piezoelectric constants. The Eshelby method transforms the problem into solving a characteristic eighth‑degree polynomial whose roots determine the field solutions. The implementation therefore requires the full set of material tensors: second‑order elastic stiffness, third‑order piezoelectric, second‑order dielectric constants, piezo‑optical and electro‑optical tensors, and the unperturbed optical indicatrix. With the stress tensor and electric field obtained at each field point, the local change of the optical indicatrix is computed via the linear elasto‑optic and electro‑optic tensors, yielding the refractive index change and birefringence. From the resulting angular distribution, the maximum birefringence at a fixed radial distance (1 µm) and the radial distance where the birefringence falls below a prescribed detection threshold (corresponding to a refractive index change of 10⁻⁶ for a 1 mm thick crystal) can be extracted.

## Reproduction target
For each dislocation type listed in the workflow steps (with given line direction ξ and Burgers vector b) for ADP, KDP and α‑quartz, carry out the numerical simulation described above to compute:
- the maximum birefringence (ΔΔn)_max at a radial distance of 1 µm from the dislocation core, and
- the maximum detection distance r_max, defined as the radial distance at which the birefringence drops below the detection limit corresponding to a refractive index change of 10⁻⁶ in the intensity distribution for a 1 mm thick crystal.
Write these results as a JSON array saved at /app/outputs/table2_reproduced.json. Each element must contain the fields material (string), dislocation_type_xi (string), dislocation_type_b (string), delta_n_max (number, dimensionless), and r_max (number, in micrometers). The table must include all dislocation types from the original report, including those that yield zero birefringence.

## Assets

- Elastic, piezoelectric, dielectric, piezo-optical, and electro-optical tensor constants for ADP (NH4H2PO4), KDP (KH2PO4), and α-quartz (SiO2)

## Workflow steps

### Step 1: Acquire material constants and implement numerical solver
- Role: process
- Action: Obtain the full set of material tensors (elastic stiffness, piezoelectric, dielectric, piezo-optical, electro-optical constants, and unperturbed indicatrix) for ADP, KDP and α-quartz from public literature or databases. Implement the Eshelby-type numerical method to solve the coupled electromechanical PDEs for a straight dislocation in an infinite anisotropic piezoelectric medium, producing mechanical stress and electric field distributions.
- Evidence: `/app/outputs/solver_evidence.log`

### Step 2: Compute Table 2: maximum birefringence and detection distances
- Role: scored (load-bearing)
- Action: For each dislocation type (with given line direction ξ and Burgers vector b) in ADP, KDP and α-quartz as described in Table 2, run the numerical solver to compute the refractive index change Δn. Determine the maximum birefringence (ΔΔn)_max at 1 μm radial distance from the dislocation core and the maximum detection distance r_max (where birefringence drops below the detection limit corresponding to Δn=10^{-6} in intensity distribution for 1 mm crystal thickness). Output these values in a JSON table covering all rows, including zero-result entries.
- Output file: `/app/outputs/table2_reproduced.json`
- Format: json
- Contract: Array of objects with fields: material (string), dislocation_type_xi (string), dislocation_type_b (string), delta_n_max (number, dimensionless), r_max (number, μm).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table2_reproduced.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table2_reproduced.json
- path: `/app/outputs/table2_reproduced.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reproduced Table 2: maximum birefringence at 1 μm distance and maximum detection distance for each dislocation type in ADP, KDP, and α-quartz. The hidden checker compares these values to the paper's reference values using tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `material`, `dislocation_type_xi`, `dislocation_type_b`, `delta_n_max`, `r_max`
    - `properties`:
      - `material`:
        - `type`: string
      - `dislocation_type_xi`:
        - `type`: string
      - `dislocation_type_b`:
        - `type`: string
      - `delta_n_max`:
        - `type`: number
      - `r_max`:
        - `type`: number
        - `units`: μm

Notes: The isotropic approximation results (Table 1) are excluded from this reproduction target.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table2_reproduced.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "material",
            "dislocation_type_xi",
            "dislocation_type_b",
            "delta_n_max",
            "r_max"
          ],
          "properties": {
            "material": {
              "type": "string"
            },
            "dislocation_type_xi": {
              "type": "string"
            },
            "dislocation_type_b": {
              "type": "string"
            },
            "delta_n_max": {
              "type": "number"
            },
            "r_max": {
              "type": "number",
              "units": "μm"
            }
          }
        }
      },
      "description": "Reproduced Table 2: maximum birefringence at 1 μm distance and maximum detection distance for each dislocation type in ADP, KDP, and α-quartz. The hidden checker compares these values to the paper's reference values using tolerances."
    }
  ],
  "notes": "The isotropic approximation results (Table 1) are excluded from this reproduction target."
}
```

## How you are scored
Your submission is scored by a hidden verifier that compares your computed delta_n_max and r_max values for each row of the table to a set of reference values derived from the paper’s reported results. Every row that meets the undisclosed tolerance criteria earns equal credit; the total reward is the fraction of rows that match within tolerance. Additional checks may verify that the relative ordering of values across materials and dislocation types is consistent with the physics. Only the table2_reproduced.json file carries weight; the solver evidence log from Step 1 is inspected for completeness but does not directly affect the score. The isotropic‑approximation stage and qualitative intensity figures are excluded from scoring.
