# Reproduction of Butterfly Bending Angles and Heat of Hydrogenation for Cyclobutene-Fused Tricycles

## Problem background
Pyramidalized alkenes are strained molecules where the carbon atoms of a double bond are forced out of the usual planar geometry. The degree of pyramidalization can be measured by the butterfly bending angle Ψ, defined as 180° minus the magnitude of a particular dihedral angle across the double bond. This task examines a series of cyclobutene‑fused tricyclic alkenes. Theoretical work has explored whether fusing a cyclobutene ring to norbornene‑, norbornadiene‑, or bicyclo[2.2.2]octene‑type scaffolds dramatically increases pyramidalization and whether one of these strained alkenes exhibits antiaromatic character reflected in an unusually exothermic first hydrogenation. Your goal is to compute the butterfly bending angles for the key compounds and the first heat of hydrogenation of one of them using quantum‑chemical methods.

## Approach
Carry out geometry optimizations using density functional theory (the hybrid B3LYP functional) and, for a subset of compounds, second‑order Møller–Plesset perturbation theory (MP2), both with the 6‑31G(d) basis set. After optimizing each structure, compute the butterfly bending angle Ψ for the C2=C5 double bond from the dihedral angle D of the atoms that define that bond: Ψ = 180 − |D|. For the hydrogenation, optimize the geometries of the reactant alkene, its monohydrogenated diene product, and a hydrogen molecule; then compute the zero‑point‑corrected total electronic energies and obtain the heat of hydrogenation as ΔH = E(products) − E(reactants). All calculations should be performed with an open‑source electronic structure package such as Psi4 (or ORCA), which supports the required methods and basis set and yields results that are directly comparable to the paper’s reference values after accounting for small package‑dependent differences.

## Reproduction target
Produce the following three scored JSON files under /app/outputs:

1. **psi_values_b3lyp.json** – For compounds labelled 5, 6, 7, 8, 9, 10, and 11, compute the butterfly bending angle Ψ (in degrees) at the B3LYP/6‑31G(d) level. The JSON object must have keys '5', '6', '7', '8', '9', '10', '11', each mapping to a numeric floating‑point value.

2. **psi_values_mp2.json** – For compounds 5, 6, 10, and 11, compute Ψ (in degrees) at the MP2/6‑31G(d) level. The JSON object must have keys '5', '6', '10', '11', each mapping to a numeric floating‑point value.

3. **hydrogenation_heat_9.json** – For compound 9 (tricyclo[4.2.2.0²⁻⁵]deca-2(5),7,9-triene), compute the heat of hydrogenation of the first hydrogenation step (conversion to the corresponding diene 23) at the B3LYP/6‑31G(d) level. The JSON object must have a single key `first_hydrogenation_heat` mapping to a numeric value in kcal/mol.

## Assets

- Psi4 (open-source quantum chemistry package): https://psicode.org/
- RDKit (optional molecular builder): https://www.rdkit.org/

## Workflow steps

### Step 1: Build initial molecular geometries
- Role: process
- Action: Construct initial 3D Cartesian coordinates for compounds 5–11, the diene product 23, and H2 molecule using a molecular builder or manual assembly based on the chemical structures described in the paper.
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: B3LYP optimization and butterfly bending angles for all compounds
- Role: scored (load-bearing)
- Action: Optimize geometries of compounds 5–11 at B3LYP/6-31G(d) level. For each compound, compute the butterfly bending angle Ψ for the C2=C5 double bond as Ψ = 180 − |D|, where D is the dihedral angle 1-2-3-4. Report the angles in a JSON file.
- Output file: `/app/outputs/psi_values_b3lyp.json`
- Format: json
- Contract: A JSON object with keys '5', '6', '7', '8', '9', '10', '11' each mapping to a numeric floating-point value in degrees.
- Scoring: scored by hidden verifier

### Step 3: MP2 optimization and butterfly bending angles for selected compounds
- Role: scored
- Action: Optimize geometries of compounds 5, 6, 10, and 11 at MP2/6-31G(d) level. Compute Ψ as before and report in JSON.
- Output file: `/app/outputs/psi_values_mp2.json`
- Format: json
- Contract: A JSON object with keys '5', '6', '10', '11' each mapping to a numeric floating-point value in degrees.
- Scoring: scored by hidden verifier

### Step 4: Heat of hydrogenation of compound 9
- Role: scored
- Action: Optimize geometries of compound 9, its monohydrogenated product (diene 23), and H2 molecule at B3LYP/6-31G(d). Obtain zero-point corrected total electronic energies. Compute heat of hydrogenation ΔH = E(23) − [E(9) + E(H2)], converted to kcal/mol. Report in JSON.
- Output file: `/app/outputs/hydrogenation_heat_9.json`
- Format: json
- Contract: A JSON object with key 'first_hydrogenation_heat' mapping to a numeric floating-point value in kcal/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/psi_values_b3lyp.json`
- `/app/outputs/psi_values_mp2.json`
- `/app/outputs/hydrogenation_heat_9.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### psi_values_b3lyp.json
- path: `/app/outputs/psi_values_b3lyp.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Butterfly bending angles Ψ (C2=C5) in degrees computed at B3LYP/6-31G(d).
- schema:
  - `type`: object
  - `required`:
    - `5`: number
    - `6`: number
    - `7`: number
    - `8`: number
    - `9`: number
    - `10`: number
    - `11`: number
  - `units`:
    - ``: degrees

### psi_values_mp2.json
- path: `/app/outputs/psi_values_mp2.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Butterfly bending angles Ψ (C2=C5) in degrees computed at MP2/6-31G(d).
- schema:
  - `type`: object
  - `required`:
    - `5`: number
    - `6`: number
    - `10`: number
    - `11`: number
  - `units`:
    - ``: degrees

### hydrogenation_heat_9.json
- path: `/app/outputs/hydrogenation_heat_9.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: First heat of hydrogenation of tricyclo[4.2.2.0²⁻⁵]deca-2(5),7,9-triene (compound 9) at B3LYP/6-31G(d).
- schema:
  - `type`: object
  - `required`:
    - `first_hydrogenation_heat`: number
  - `units`:
    - `first_hydrogenation_heat`: kcal/mol

Notes: The hidden checker compares agent-reported values with paper-reported references using appropriate tolerances. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "psi_values_b3lyp.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "5": "number",
          "6": "number",
          "7": "number",
          "8": "number",
          "9": "number",
          "10": "number",
          "11": "number"
        },
        "units": {
          "": "degrees"
        }
      },
      "description": "Butterfly bending angles Ψ (C2=C5) in degrees computed at B3LYP/6-31G(d)."
    },
    {
      "file": "psi_values_mp2.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "5": "number",
          "6": "number",
          "10": "number",
          "11": "number"
        },
        "units": {
          "": "degrees"
        }
      },
      "description": "Butterfly bending angles Ψ (C2=C5) in degrees computed at MP2/6-31G(d)."
    },
    {
      "file": "hydrogenation_heat_9.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "first_hydrogenation_heat": "number"
        },
        "units": {
          "first_hydrogenation_heat": "kcal/mol"
        }
      },
      "description": "First heat of hydrogenation of tricyclo[4.2.2.0²⁻⁵]deca-2(5),7,9-triene (compound 9) at B3LYP/6-31G(d)."
    }
  ],
  "notes": "The hidden checker compares agent-reported values with paper-reported references using appropriate tolerances. No gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier independently examines each of the scored JSON files. It compares your submitted numeric values (butterfly bending angles and hydrogenation heat) against reference values using tolerances appropriate for the theoretical method and basis set, chosen to absorb differences that arise when a different open‑source quantum chemistry package is used. For directional metrics (like an angle or a heat) a more accurate or larger value does not incur a penalty; credit is awarded when your result meets or beats the reference within the allowed tolerance. The final reward is a weighted combination of the scores from all three stages. Simply writing a number from memory or guess will not succeed; the artefacts must be the genuine outputs of running the prescribed workflow.
