# Mechanical moduli and ductility classification of SrLiH3 and SrPdH3 from first-principles elastic constants

## Problem background
Perovskite hydrides SrLiH3 and SrPdH3 are candidate hydrogen storage materials. Their mechanical stability, stiffness, and ductility/brittleness classification are critical for practical applications, but data on SrPdH3 have been missing. This work derives those mechanical properties from first-principles elastic constants, enabling a systematic comparison of the two compounds.

## Approach
The approach uses density functional theory with the all-electron full-potential linear augmented plane wave (FP-LAPW) method and the PBE generalized gradient approximation. For each compound, the equilibrium lattice constant is first obtained by fitting total energy versus volume data to an equation of state. Then, volume-conserving tetragonal and orthorhombic strains are applied to compute the three independent elastic constants C11, C12, C44. From these constants, the polycrystalline mechanical properties (shear modulus, Young’s modulus, Poisson’s ratio, anisotropy, Kleinman parameter, B/G ratio, and Cauchy pressure) are derived using Voigt–Reuss–Hill averaging. Ductility is classified via the Pugh criterion, Frantsevich rule, and the sign of the Cauchy pressure.

## Reproduction target
Compute the equilibrium lattice constants for cubic SrLiH3 and SrPdH3 (space group Pm3̄m) via DFT total-energy optimization. Then, using the optimized structures, apply strain calculations to obtain the three independent elastic constants C11, C12, C44 for both compounds at the PBE-GGA level. Write the results to `/app/outputs/elastic_constants.json`. The derived mechanical properties and ductility classification will be assessed by the verifier from these constants.

## Assets

- Elk FP-LAPW code: https://elk.sourceforge.net/

## Workflow steps

### Step 1: Structural optimization and equation of state fitting
- Role: process
- Action: Perform DFT total energy calculations as a function of volume for SrLiH₃ and SrPdH₃ (cubic Pm3̄m, atomic positions: Sr at (0,0,0), Li/Pd at (0.5,0.5,0.5), H at (0.5,0.5,0)). Fit the resulting E(V) data to the Murnaghan equation of state to obtain equilibrium lattice constants and bulk modulus.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 2: Equilibrium elastic constants calculation
- Role: scored (load-bearing)
- Action: Using the optimized equilibrium structures, apply volume‑conserving tetragonal and orthorhombic strains and compute the three independent elastic constants C₁₁, C₁₂, C₄₄ for both SrLiH₃ and SrPdH₃ with an all‑electron FP‑LAPW code using PBE‑GGA. Write the results to elastic_constants.json.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"SrPdH3": {"C11": <float GPa>, "C12": <float GPa>, "C44": <float GPa>}, "SrLiH3": {"C11": <float GPa>, "C12": <float GPa>, "C44": <float GPa>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed elastic constants C11, C12, C44 for the cubic perovskite hydrides SrLiH3 and SrPdH3. The verifier will recompute all derived mechanical properties (shear modulus, Young's modulus, Poisson's ratio, anisotropy, Kleinman parameter, B/G ratio, Cauchy pressure) from these constants and compare against the paper's reported PBE‑GGA values.
- schema:
  - `type`: object
  - `required`: `SrPdH3`, `SrLiH3`
  - `properties`:
    - `SrPdH3`:
      - `type`: object
      - `required`: `C11`, `C12`, `C44`
      - `units`:
        - `C11`: GPa
        - `C12`: GPa
        - `C44`: GPa
    - `SrLiH3`:
      - `type`: object
      - `required`: `C11`, `C12`, `C44`
      - `units`:
        - `C11`: GPa
        - `C12`: GPa
        - `C44`: GPa

Notes: The electronic band gap, DOS at Fermi level, Debye temperature, pressure-dependent elastic constants, and quasi-harmonic thermal properties are headline quantities in the paper but are not scored here. They require either an additional DFT band-structure/DOS run at the same level (electronic), the Gibbs program for quasi-harmonic Debye modeling (thermal vs T/P), or many extra DFT runs (pressure-dependent elastic constants). They can be addressed in a follow‑up package.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "SrPdH3",
          "SrLiH3"
        ],
        "properties": {
          "SrPdH3": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C44"
            ],
            "units": {
              "C11": "GPa",
              "C12": "GPa",
              "C44": "GPa"
            }
          },
          "SrLiH3": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C44"
            ],
            "units": {
              "C11": "GPa",
              "C12": "GPa",
              "C44": "GPa"
            }
          }
        }
      },
      "description": "Computed elastic constants C11, C12, C44 for the cubic perovskite hydrides SrLiH3 and SrPdH3. The verifier will recompute all derived mechanical properties (shear modulus, Young's modulus, Poisson's ratio, anisotropy, Kleinman parameter, B/G ratio, Cauchy pressure) from these constants and compare against the paper's reported PBE‑GGA values."
    }
  ],
  "notes": "The electronic band gap, DOS at Fermi level, Debye temperature, pressure-dependent elastic constants, and quasi-harmonic thermal properties are headline quantities in the paper but are not scored here. They require either an additional DFT band-structure/DOS run at the same level (electronic), the Gibbs program for quasi-harmonic Debye modeling (thermal vs T/P), or many extra DFT runs (pressure-dependent elastic constants). They can be addressed in a follow‑up package."
}
```

## How you are scored
A hidden verifier reads your `elastic_constants.json` and independently recomputes the polycrystalline mechanical properties (shear modulus, Young’s modulus, Poisson’s ratio, anisotropy, Kleinman parameter, B/G ratio, Cauchy pressure) using standard Voigt–Reuss–Hill formulas. It compares each computed quantity, as well as the ductility classification derived from these quantities, against reference values with tolerance margins. The final score is proportional to the number of properties that fall within tolerance plus the correctness of the ductility assessments. The structural optimization step is a required process step but is not directly scored; only the elastic constants file contributes to the reward.
