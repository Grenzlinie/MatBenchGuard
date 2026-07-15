# Compute tip deflection of bilayer and trilayer graphene nanoribbons using improved beam theory

## Problem background
Multilayer graphene nanoribbons are quasi-one-dimensional carbon structures with exceptional mechanical properties. When bent as cantilevers, both interlayer shear and intralayer extension (in-plane stretch) influence the deflection. Newmark's composite beam theory, which simultaneously accounts for these two effects, provides a continuum model. This task concerns the accurate tip deflection of bilayer and trilayer graphene nanoribbons under a concentrated tip force, a benchmark for assessing the role of in-plane extension in multilayer nanomaterials.

## Approach
The model treats each graphene layer as an Euler–Bernoulli beam with identical transverse displacement. Interlayer shear is represented by a slip force proportional to the relative axial displacement between adjacent layers, with interface slip stiffness K = G b / h (G is the interlayer shear modulus). The centroidal normal strains of each layer are included to capture intralayer extension. Force and moment equilibrium of a differential element leads to a second-order ordinary differential equation for the curvature, which becomes a fourth-order ODE for the deflection w(x). Solving this ODE with cantilever boundary conditions (zero deflection and slope at the fixed end, zero moment and prescribed shear force at the free end) gives the exact deflection profile.

For a bilayer (each layer of thickness h, width b, length l, Young’s modulus E, interlayer shear modulus G) subjected to a tip force P, the tip deflection is

w_l = [9 P (1 − e^(2λl))] / [16 λ (1 + e^(2λl)) G b h] + (9 P l) / (16 G b h) + (P l³) / (2 E b h³),

where λ = √(8 G / (E h²)).

For a trilayer, the corresponding expression is

w_l = [32 P (1 − e^(2λl))] / [81 λ (1 + e^(2λl)) G b h] + (4 P l³) / (27 E b h³) + (32 P l) / (81 G b h),

with λ = √(9 G / (E h²)).

The normalized bending stiffness is defined as P l / (w_l b h), reported in GPa.

## Reproduction target
Use the following fixed parameters: single‑layer thickness h = 0.335 nm, width b = 1 nm, length l = 10 nm, Young’s modulus E = 1.0 TPa, interlayer shear modulus G = 4.6 GPa, and tip force P = 1 nN. Compute the tip deflection w_l (in nm) and the normalized bending stiffness P l / (w_l b h) (in GPa) for both the bilayer and trilayer cases. Write the results together with the input parameters to the JSON output file specified in the workflow.

## Assets
None. All required parameters are provided above; no external datasets, models, or tools are needed beyond a Python interpreter with standard math libraries.

## Workflow steps

### Step 1: Compute bilayer and trilayer tip deflection and normalized stiffness
- Role: scored (load-bearing)
- Action: Implement the analytical tip deflection formulas for a cantilever bilayer and trilayer graphene nanoribbon based on the Newmark beam theory described in the instruction. Use the provided geometric and material parameters: single-layer thickness h=0.335 nm, width b=1 nm, length l=10 nm, Young's modulus E=1.0 TPa, interlayer shear modulus G=4.6 GPa, tip force P=1 nN. Compute the tip deflection w_l (nm) and the normalized bending stiffness Pl/(w_l b h) (GPa) for both the bilayer and trilayer cases. Write the computed results together with the input parameters into /app/outputs/deflection_results.json.
- Output file: `/app/outputs/deflection_results.json`
- Format: json
- Contract: JSON object with keys 'bilayer' and 'trilayer'. Each maps to an object with keys: 'w_l' (float, tip deflection in nm), 'Pl_over_wl_bh' (float, normalized stiffness in GPa), and 'parameters' (object with numeric parameters and their units: E (TPa), G (GPa), h (nm), b (nm), l (nm), P (nN)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/deflection_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### deflection_results.json
- path: `/app/outputs/deflection_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed tip deflection and normalized stiffness for bilayer and trilayer configurations using Newmark beam theory.
- schema:
  - `type`: object
  - `required`: `bilayer`, `trilayer`
  - `properties`:
    - `bilayer`:
      - `type`: object
      - `required`: `w_l`, `Pl_over_wl_bh`, `parameters`
    - `trilayer`:
      - `type`: object
      - `required`: `w_l`, `Pl_over_wl_bh`, `parameters`
  - `units`:
    - `w_l`: nm
    - `Pl_over_wl_bh`: GPa

Notes: The agent must derive the formulas from the instruction text and use the exact parameters listed. The checker will recompute the expected w_l and Pl/(w_l b h) from the same formulas and compare with a tight relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "deflection_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "bilayer",
          "trilayer"
        ],
        "properties": {
          "bilayer": {
            "type": "object",
            "required": [
              "w_l",
              "Pl_over_wl_bh",
              "parameters"
            ]
          },
          "trilayer": {
            "type": "object",
            "required": [
              "w_l",
              "Pl_over_wl_bh",
              "parameters"
            ]
          }
        },
        "units": {
          "w_l": "nm",
          "Pl_over_wl_bh": "GPa"
        }
      },
      "description": "Computed tip deflection and normalized stiffness for bilayer and trilayer configurations using Newmark beam theory."
    }
  ],
  "notes": "The agent must derive the formulas from the instruction text and use the exact parameters listed. The checker will recompute the expected w_l and Pl/(w_l b h) from the same formulas and compare with a tight relative tolerance."
}
```

## How you are scored
A hidden verifier independently computes the expected tip deflection and normalized stiffness using the same analytical formulas and parameters. Your reported numeric values (w_l and P l / (w_l b h) for each configuration) are compared against the verifier’s computed values with a tight relative tolerance. Full credit is awarded if both values match within tolerance; partial credit decreases as the relative deviation grows. The final reward is a weighted combination of the scores from this scored step.
