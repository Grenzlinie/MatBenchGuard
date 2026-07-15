# Reproduce CAS-SCF Energetics of Silaethylene Dimerization

## Problem background
The Woodward-Hoffmann rules predict that [2πₛ+2πₛ] cycloadditions are forbidden and proceed stepwise. For the head-to-tail dimerization of silaethylene, earlier single-reference quantum chemical calculations (SCF, CISD, CCSD) identified a C₂ₕ rhomboid transition state, suggesting a concerted reaction path. However, single-reference methods may fail in regions of weakly avoided crossings that are characteristic of forbidden reactions. The present investigation uses multireference CAS-SCF calculations to re-examine the potential energy surface, locate all critical points (minima, transition states, saddle points, and conical intersections), and determine whether a concerted pathway genuinely exists or the reaction follows a stepwise diradical mechanism.

## Approach
Perform CAS-SCF(4,4) calculations using two basis sets: 3‑21G* and DZ+d. An active space of four electrons in four orbitals provides the minimal description needed to represent the avoided crossing region of this forbidden reaction. Locate and optimize the stationary points for the anti and gauche diradical pathways, and explore the C₂ₕ rhomboid region of the potential surface. Use state-averaged orbitals to locate conical intersections between the ground and excited states. Compute vibrational frequencies for key stationary points to confirm their character (minimum or transition state). The relative energies of all critical points are computed with respect to two isolated silaethylene molecules. The reaction mechanism is assessed by comparing the energetic ordering and the structural features (bond lengths, angles) obtained from the optimizations.

## Reproduction target
Produce a single JSON file containing the computed total energies (atomic units) and relative energies (kcal/mol) for all critical points listed in the paper’s Table I at both the 3‑21G* and DZ+d levels of theory, as well as the Cartesian coordinates of the optimized geometries for the anti TS, anti M, gauche M, cis SP, C₂ₕ SP, CI_Si‑Si, and CI_C‑C. Additionally, demonstrate whether the C₂ₕ rhomboid geometry is a stationary point on the CAS-SCF surface: starting from a rhomboid guess, unconstrained optimization must be attempted, and the outcome (convergence to a different structure or failure to locate a stationary point) must be reflected in the submitted geometries. The target is to obtain a consistent set of energies and structures that correctly characterizes the reaction pathway.

## Assets

- Psi4 (or equivalent open‑source CAS‑SCF capable package): https://psicode.org/

## Workflow steps

### Step 1: CAS‑SCF calculations and geometry explorations
- Role: process
- Action: Perform CAS‑SCF(4,4) calculations with the 3‑21G* and DZ+d basis sets. Locate and optimize all critical points: anti M, anti TS, gauche M, cis SP, C₂h SP, anti_Si‑Si TS, anti_C‑C TS, and isolated reactants. Locate the conical intersections CI_Si‑Si and CI_C‑C using state‑averaged orbitals. Compute vibrational frequencies for key stationary points to confirm their character. Starting from a C₂h rhomboid guess, verify that unconstrained optimization does not converge to a stationary point in that region but collapses to another structure.
- Evidence: `/app/outputs/calculation_logs.txt`

### Step 2: Compile energies and geometries
- Role: scored (load-bearing)
- Action: Collect the total energies (atomic units) and final Cartesian coordinates for all states at both basis set levels. Compute relative energies (kcal/mol) using separated reactants as reference. Write the results to dimerization_results.json.
- Output file: `/app/outputs/dimerization_results.json`
- Format: json
- Contract: Object with keys 'energies' and 'geometries'. 'energies' is an array of objects each with keys 'state' (string), 'level' ('3‑21G*' or 'DZ+d'), 'energy_au' (float), 'relative_kcal' (float). 'geometries' is an object mapping state names to arrays of atoms each with keys 'element', 'x', 'y', 'z' (Cartesian coordinates in Å).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dimerization_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dimerization_results.json
- path: `/app/outputs/dimerization_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled absolute and relative energies plus final geometries for all critical points of the silaethylene dimerization at CAS‑SCF(4,4)/3‑21G* and CAS‑SCF(4,4)/DZ+d levels.
- schema:
  - `type`: object
  - `required`:
    - `top-level`: `energies`, `geometries`
  - `items`:
    - `energies`:
      - `type`: array
      - `item`:
        - `type`: object
        - `required`: `state`, `level`, `energy_au`, `relative_kcal`
    - `geometries`:
      - `type`: object
      - `properties`:
        - `*`:
          - `type`: array
          - `item`:
            - `type`: object
            - `required`: `element`, `x`, `y`, `z`

Notes: The agent must run the quantum chemistry calculations itself; the output file must contain the energies and geometries derived from those runs. The checker compares the reported relative energies to hidden paper references within ±2 kcal/mol tolerance and validates selected bond lengths and angles within ±0.05 Å and ±2°.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dimerization_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "top-level": [
            "energies",
            "geometries"
          ]
        },
        "items": {
          "energies": {
            "type": "array",
            "item": {
              "type": "object",
              "required": [
                "state",
                "level",
                "energy_au",
                "relative_kcal"
              ]
            }
          },
          "geometries": {
            "type": "object",
            "properties": {
              "*": {
                "type": "array",
                "item": {
                  "type": "object",
                  "required": [
                    "element",
                    "x",
                    "y",
                    "z"
                  ]
                }
              }
            }
          }
        }
      },
      "description": "Compiled absolute and relative energies plus final geometries for all critical points of the silaethylene dimerization at CAS‑SCF(4,4)/3‑21G* and CAS‑SCF(4,4)/DZ+d levels."
    }
  ],
  "notes": "The agent must run the quantum chemistry calculations itself; the output file must contain the energies and geometries derived from those runs. The checker compares the reported relative energies to hidden paper references within ±2 kcal/mol tolerance and validates selected bond lengths and angles within ±0.05 Å and ±2°."
}
```

## How you are scored
A hidden verifier reads the submitted dimerization_results.json. It checks that all required states and basis-set levels are present with correct JSON structure. It compares the reported relative energies to a hidden reference set and verifies the energetic ordering (e.g., that the anti TS is lower than the C₂ₕ TS). It also checks that no stationary C₂ₕ rhomboid geometry is present, confirming the optimization did not converge to that structure. Selected bond lengths and angles in the submitted geometries are validated against reference values. The final reward is a weighted combination of these energy and structural checks. Reporting the paper’s numbers without performing the computations is not sufficient.
