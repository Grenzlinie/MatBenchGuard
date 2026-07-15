# Second‑Order Nonadiabatic Coupling Calculation for H3 Molecule

## Problem background
Simulating nonadiabatic dynamics requires knowledge of nonadiabatic couplings (NACs), both first-order and second-order. While first-order NACs are widely studied, second-order NACs are less investigated yet may be important near intersection points. This task evaluates a method for computing second-order NACs for the H3 molecule, a prototypical Jahn–Teller system where the ground and first excited states are degenerate at a conical intersection.

## Approach
The method employs time-dependent density functional theory (TDDFT) within the Tamm–Dancoff approximation, combined with modified linear response theory. For a doublet system like H3, this reduces to the Slater transition state approach: a DFT calculation is performed in a mid-excited state with half-filled HOMO and LUMO. The second-order NAC is obtained as a b-matrix element, computed via finite‑difference second derivatives of the Kohn–Sham orbitals with respect to nuclear displacements. The calculation uses the local spin-density approximation (LSDA) with the Teter–Pade functional and Troullier–Martins pseudopotentials in a plane‑wave basis, as implemented in the ABINIT code.

## Reproduction target
Compute the x, y, and z components (in bohr⁻²) of the second-order NAC for each of the three hydrogen atoms in H3 at a geometry near the Jahn–Teller intersection: an equilateral triangle with bond length r(H–H) = 1.9729 bohr, and a contour radius q = 0.02 bohr, contour angle θ = 0. Use the Slater transition state method as described. Store the result in the JSON file `/app/outputs/second_order_NAC_H3.json` following the specified schema.

## Assets

- ABINIT: https://www.abinit.org/downloads
- H pseudopotential (Troullier‑Martins): https://www.abinit.org/downloads/psp‑links/lda_tm

## Workflow steps

### Step 1: Prepare H3 geometry
- Role: process
- Action: Create input files for the H3 molecule in an equilateral triangle geometry with bond length r_H‑H = 1.9729 bohr, placed according to the Jahn‑Teller configuration: one atom at the contour radius q=0.02 bohr, contour angle θ=0. Write the atomic coordinates to a file suitable for ABINIT input.
- Evidence: `/app/outputs/h3_geometry.xyz`

### Step 2: Compute second‑order NAC for H3
- Role: scored (load-bearing)
- Action: Using ABINIT with LSDA/Teter Pade functional and the Troullier‑Martins pseudopotential for hydrogen, perform a DFT/TDDFT calculation in the Slater transition state (mid‑excited state with half‑filled HOMO and LUMO) within modified linear response theory. Compute the second‑order nonadiabatic coupling (NAC) via numerical second derivatives of Kohn‑Sham orbitals using finite differences (displacement ~0.002–0.004 bohr) for each atom. Extract the x, y, z components (in bohr⁻²) for atoms 1, 2, and 3.
- Output file: `/app/outputs/second_order_NAC_H3.json`
- Format: json
- Contract: {"atoms": [{"atom": <integer>, "x": <float>, "y": <float>, "z": <float>}, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/second_order_NAC_H3.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### second_order_NAC_H3.json
- path: `/app/outputs/second_order_NAC_H3.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed second‑order NAC x, y, z components for each of the three H atoms at the specified geometry. The checker compares each component against a hidden gold value with a tolerance; credit is given per component within tolerance.
- schema:
  - `type`: object
  - `required`: `atoms`
  - `properties`:
    - `atoms`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `atom`, `x`, `y`, `z`
        - `properties`:
          - `atom`:
            - `type`: integer
          - `x`:
            - `type`: number
            - `description`: x component in bohr⁻²
          - `y`:
            - `type`: number
            - `description`: y component in bohr⁻²
          - `z`:
            - `type`: number
            - `description`: z component in bohr⁻²

Notes: The calculation is based on the Slater transition state method within TDDFT modified linear response theory, using LSDA functional and Troullier‑Martins pseudopotentials. The exact tolerance values are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "second_order_NAC_H3.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "atoms"
        ],
        "properties": {
          "atoms": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "atom",
                "x",
                "y",
                "z"
              ],
              "properties": {
                "atom": {
                  "type": "integer"
                },
                "x": {
                  "type": "number",
                  "description": "x component in bohr⁻²"
                },
                "y": {
                  "type": "number",
                  "description": "y component in bohr⁻²"
                },
                "z": {
                  "type": "number",
                  "description": "z component in bohr⁻²"
                }
              }
            }
          }
        }
      },
      "description": "Computed second‑order NAC x, y, z components for each of the three H atoms at the specified geometry. The checker compares each component against a hidden gold value with a tolerance; credit is given per component within tolerance."
    }
  ],
  "notes": "The calculation is based on the Slater transition state method within TDDFT modified linear response theory, using LSDA functional and Troullier‑Martins pseudopotentials. The exact tolerance values are hidden."
}
```

## How you are scored
A hidden verifier reads your output JSON and compares each of the nine components (x, y, z for atoms 1, 2, 3) against a reference standard. Each component that lies within a hidden tolerance earns credit. Your final reward is the fraction of components (out of 9) that fall within tolerance. Simply reporting a number is not sufficient; you must genuinely execute the computational workflow to produce the artifact.
