# Finite Element Simulation of Electrostatic Nanolithography Field

## Problem background
Graphene fluoride (GF) is an insulating two-dimensional derivative of graphene that can be locally reduced to conductive graphene by intense electrostatic fields applied with an atomic force microscope (AFM) tip. Understanding the magnitude of the electric field at the GF surface is essential for determining the threshold conditions under which fluorine is removed from the carbon lattice. This task addresses the electrostatic aspect of that process by computing the electric field distribution in an idealized AFM tip–sample system.

## Approach
The tip–sample system is modeled as a 2D axisymmetric structure. A grounded gold‑coated AFM tip (cone half‑angle 20°, hemispherical apex radius 30 nm) is placed a fixed distance above a 1 nm thick GF layer (dielectric constant 2.1) that sits on a 100 nm SiO₂ film (dielectric constant 3.9) and a silicon substrate biased at 10 V. The gap between tip and GF is vacuum (dielectric constant 1). The Laplace equation for the electrostatic potential is solved in this domain using an open‑source finite element method (FEM) package, and the magnitude of the electric field is extracted at the GF surface directly beneath the tip apex.

## Reproduction target
Compute the peak electrostatic field magnitude (in V nm⁻¹) at the surface of the graphene fluoride sheet for a tip–sample gap of 0.6 nm and a substrate bias of 10 V. Output the result as a JSON file containing the peak field value and the conditions under which it was obtained.

## Assets

- Open-source finite element method (FEM) package (e.g., FEniCS, Elmer, SfePy): fenics

## Workflow steps

### Step 1: Finite element electric field computation
- Role: scored (load-bearing)
- Action: Set up a 2D axisymmetric electrostatic model of the tip–GF–SiO₂–Si stack with the exact geometry, material dielectric constants, and bias given in the reproduction target. Solve the Laplace equation for the electric potential and compute the electric field magnitude on the GF surface. Extract the peak value at the point directly under the tip apex.
- Output file: `/app/outputs/electric_field_results.json`
- Format: json
- Contract: {"E_peak": <float>, "units": "V/nm", "conditions": {"gap_nm": 0.6, "bias_V": 10}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electric_field_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electric_field_results.json
- path: `/app/outputs/electric_field_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Peak electric field magnitude at the graphene fluoride surface under the AFM tip apex for a 0.6 nm gap and 10 V substrate bias. Compared to the paper-reported value within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `E_peak`: number
    - `units`: string
  - `items`: object
  - `required_columns`:
  - `units`:
    - `E_peak`: V/nm

Notes: Only the computational electrostatic simulation is reproduced; wet-lab fabrication and transport data are not code-verifiable.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electric_field_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "E_peak": "number",
          "units": "string"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "E_peak": "V/nm"
        }
      },
      "description": "Peak electric field magnitude at the graphene fluoride surface under the AFM tip apex for a 0.6 nm gap and 10 V substrate bias. Compared to the paper-reported value within a tolerance."
    }
  ],
  "notes": "Only the computational electrostatic simulation is reproduced; wet-lab fabrication and transport data are not code-verifiable."
}
```

## How you are scored
A hidden verifier loads your output JSON, extracts the reported peak field value, and compares it to a reference value derived from the paper's finite element simulation under the same conditions. Full credit is awarded if your value is within a published tolerance of the reference; partial credit decays smoothly as the discrepancy grows beyond that tolerance. The tolerance accommodates differences introduced by meshing, solver implementation, and the use of open‑source tools. The verifier does not penalize values that exceed the reference accuracy.
