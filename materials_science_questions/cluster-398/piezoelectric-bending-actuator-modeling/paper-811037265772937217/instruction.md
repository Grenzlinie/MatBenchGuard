# Static piezoelectric bimorph beam deflection via plate-bending FE

## Problem background
Piezoelectric materials, such as PVDF, can function as sensors and actuators in intelligent structures by coupling mechanical and electrical fields. Accurate modelling of such structures requires finite elements that simultaneously describe plate bending and the direct/inverse piezoelectric effects. A four‑node, 12‑degree‑of‑freedom isoparametric plate bending element augmented with electric potential degrees of freedom has been developed for this purpose. One key validation of the new element is the simulation of a cantilever PVDF bimorph beam — two identical layers with opposite polarities — and the computation of its static deflection under applied voltages. This task reproduces that validation: you will implement the piezoelectric plate bending element, model the bimorph beam, and compute the resulting nodal deflections.

## Approach
The approach couples elastic and electric fields through the linear piezoelectric constitutive equations within a Lagrangian framework. The plate element uses standard quadrilateral bending shape functions for the transverse displacement and rotations, while the electric potential is interpolated independently inside each element. After forming the element stiffness, piezoelectric coupling, and dielectric matrices, the electric potential degrees of freedom are condensed out at the element level using static condensation. This yields a reduced, purely mechanical element stiffness matrix and an equivalent electrical force vector that depends on the applied voltage. The bimorph beam is modelled by stacking two such layers with opposite poling directions, discretised with five identical elements along the length. Applying a voltage across the thickness then produces a bending deformation; the resulting nodal deflections are extracted at specified positions along the beam.

## Reproduction target
Implement the piezoelectric plate bending element and use it to model the PVDF bimorph beam (total length 100 mm, total thickness 0.5 mm, width 1 mm, two identical layers with opposite polarities) with five elements. Apply a unit voltage and compute the static deflections. Then repeat for applied voltages of 50, 100, 150, and 200 V. For each voltage case, extract the nodal deflections at distances 20, 40, 60, 80, and 100 mm from the fixed end. Output the results as a CSV file (see step contract) — the correctness of your computed deflections will be assessed by a hidden verifier.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute static deflections of PVDF bimorph beam
- Role: scored (load-bearing)
- Action: Implement the piezoelectric plate bending element (4‑node, 12 mechanical DOF + 4 electric potential DOF) using the Lagrangian formulation, constitutive laws, and condensation described in the problem. Model a cantilever PVDF bimorph beam (two identical layers, opposite polarities, total length 100 mm, total thickness 0.5 mm, width 1 mm) with five identical elements. Use material properties: E1=0.2e10 N/m², e31=0.046 C/m², ζ11=0.1062e-9 F/m, ν=0.29, ρ=1800 kg/m³. Apply a unit voltage and solve for nodal deflections. Repeat for 50, 100, 150, 200 V. Extract deflections at distances x = 20, 40, 60, 80, 100 mm from the fixed end. Output a CSV with the required columns.
- Output file: `/app/outputs/bimorph_deflections.csv`
- Format: csv
- Contract: distance_m (float), deflection_unit_voltage_m (float), deflection_50V_m (float), deflection_100V_m (float), deflection_150V_m (float), deflection_200V_m (float). One row per distance (0.02, 0.04, 0.06, 0.08, 0.10 m).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bimorph_deflections.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bimorph_deflections.csv
- path: `/app/outputs/bimorph_deflections.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Deflections computed by the plate bending element for the cantilever bimorph beam. The checker recomputes analytic deflections and compares.
- schema:
  - `type`: table
  - `required_columns`: `distance_m`, `deflection_unit_voltage_m`, `deflection_50V_m`, `deflection_100V_m`, `deflection_150V_m`, `deflection_200V_m`
  - `units`:
    - `distance_m`: meter
    - `deflection_unit_voltage_m`: meter
    - `deflection_50V_m`: meter
    - `deflection_100V_m`: meter
    - `deflection_150V_m`: meter
    - `deflection_200V_m`: meter

Notes: The hidden checker uses the analytical formula w(x)=0.375*e31*V/E1*(x/t)^2 to compute reference deflections, then scores the relative error. Full credit if relative error ≤ 10%, decaying linearly for larger errors. This is the only scored artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bimorph_deflections.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_m",
          "deflection_unit_voltage_m",
          "deflection_50V_m",
          "deflection_100V_m",
          "deflection_150V_m",
          "deflection_200V_m"
        ],
        "units": {
          "distance_m": "meter",
          "deflection_unit_voltage_m": "meter",
          "deflection_50V_m": "meter",
          "deflection_100V_m": "meter",
          "deflection_150V_m": "meter",
          "deflection_200V_m": "meter"
        }
      },
      "description": "Deflections computed by the plate bending element for the cantilever bimorph beam. The checker recomputes analytic deflections and compares."
    }
  ],
  "notes": "The hidden checker uses the analytical formula w(x)=0.375*e31*V/E1*(x/t)^2 to compute reference deflections, then scores the relative error. Full credit if relative error ≤ 10%, decaying linearly for larger errors. This is the only scored artifact."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. The verifier independently recomputes a quantitative check from your output artifact and compares it against a stored gold reference. Full marks are earned when the computed results meet the required accuracy; partial credit may be awarded for partial accuracy. Simply reporting pre‑known numbers without performing the required finite element computation will not produce a passing result. Each workflow stage contributes a weighted portion of the total score.
