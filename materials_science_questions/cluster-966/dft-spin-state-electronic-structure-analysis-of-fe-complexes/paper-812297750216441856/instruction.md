# DFT Geometry Optimization and Frequency Analysis of D6d Sandwich Complexes

## Problem background
Sandwich-type complexes formed by a transition metal between two aromatic monocyclic ligands have broad applications in organometallic chemistry. A new class of such complexes has been proposed in which the ligands are planar hexacoordinate carbon rings (B6C2−) bound in an η6 fashion, yielding staggered D6d structures. The problem is to determine, by computational means, whether these complexes are true minima on the potential energy surface — characterized by specific optimized bond lengths and real vibrational frequencies — for the transition metals Fe, Co, and Ni.

## Approach
The complexes are studied computationally by density functional theory (DFT). The method uses the B3LYP exchange-correlation functional and the 6-311+G(3df) basis set. Staggered D6d sandwich complexes of the form [(B6C)2M] (M = Fe, Co, Ni) are constructed from the planar D6h B6C2− ligand, where the B–B and B–C bond distances are approximately 1.588 Å. The transition metal is placed along the sixfold axis, and each complex is assigned the appropriate total charge (Fe: −2, Co: −1, Ni: 0) and a suitable spin multiplicity. Full geometry optimizations are performed on these initial structures, followed by harmonic vibrational frequency calculations on the optimized geometries. The primary outputs are the optimized Cartesian coordinates and the set of vibrational frequencies.

## Reproduction target
The objective is to obtain the optimized geometries of the three D6d sandwich complexes and to verify that all vibrational frequencies are real (no imaginary modes), thereby confirming they are minima. For each complex, produce a coordinate file in XYZ format containing the final atomic positions, and extract the lowest (real) vibrational frequency in cm⁻¹. No external data is required; the computational procedure alone yields these results.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- B3LYP functional and 6-311+G(3df) basis set: Built into ORCA and other major quantum chemistry packages; no external download needed.

## Workflow steps

### Step 1: Initial geometry construction
- Role: process
- Action: Build initial guess molecular structures for the three D6d [(B6C)2M] complexes (M=Fe, Co, Ni) using the known planar D6h B6C2- ligand geometry (B–B and B–C bond lengths approximately 1.588 Å). Place the transition metal along the sixfold axis in a staggered conformation and assign the appropriate total charge and multiplicity for each complex (Fe: -2, Co: -1, Ni: 0).
- Evidence: `/app/outputs/initial_geometries.log`

### Step 2: Geometry optimization of [(B6C)2Fe]2-
- Role: scored
- Action: Run DFT geometry optimization (functional: B3LYP, basis set: 6-311+G(3df)) on the D6d [(B6C)2Fe]2- complex to locate a minimum. Output the optimized Cartesian coordinates in XYZ format.
- Output file: `/app/outputs/D6d_Fe.xyz`
- Format: txt
- Contract: XYZ format: first line = number of atoms, second line = comment, subsequent lines = <element> <x> <y> <z> (coordinates in Å).
- Scoring: scored by hidden verifier

### Step 3: Geometry optimization of [(B6C)2Co]-
- Role: scored
- Action: Run DFT geometry optimization (B3LYP/6-311+G(3df)) on the D6d [(B6C)2Co]- complex. Output the optimized Cartesian coordinates in XYZ format.
- Output file: `/app/outputs/D6d_Co.xyz`
- Format: txt
- Contract: Same as step 2.
- Scoring: scored by hidden verifier

### Step 4: Geometry optimization of [(B6C)2Ni]
- Role: scored
- Action: Run DFT geometry optimization (B3LYP/6-311+G(3df)) on the neutral D6d [(B6C)2Ni] complex. Output the optimized Cartesian coordinates in XYZ format.
- Output file: `/app/outputs/D6d_Ni.xyz`
- Format: txt
- Contract: Same as step 2.
- Scoring: scored by hidden verifier

### Step 5: Vibrational frequency calculation
- Role: scored (load-bearing)
- Action: Perform harmonic vibrational frequency calculations at the same DFT level (B3LYP/6-311+G(3df)) on each optimized D6d structure (Fe, Co, Ni). Verify that no imaginary frequencies are present. Extract the lowest (real) vibrational frequency in cm-1 for each complex and write a JSON file summarizing the results.
- Output file: `/app/outputs/vibrational_frequencies.json`
- Format: json
- Contract: JSON object with keys 'Fe', 'Co', 'Ni'. Each value is an object with keys 'lowest_frequency' (float, cm⁻¹) and 'all_real' (bool).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/D6d_Fe.xyz`
- `/app/outputs/D6d_Co.xyz`
- `/app/outputs/D6d_Ni.xyz`
- `/app/outputs/vibrational_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### D6d_Fe.xyz
- path: `/app/outputs/D6d_Fe.xyz`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Optimized Cartesian coordinates of the D6d [(B6C)2Fe]2- complex. The checker recomputes bond lengths (B–B, B–C, B–Fe, C–Fe) from these coordinates.
- schema:
  - `type`: text
  - `format`: XYZ

### D6d_Co.xyz
- path: `/app/outputs/D6d_Co.xyz`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Optimized Cartesian coordinates of the D6d [(B6C)2Co]- complex.
- schema:
  - `type`: text
  - `format`: XYZ

### D6d_Ni.xyz
- path: `/app/outputs/D6d_Ni.xyz`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Optimized Cartesian coordinates of the D6d [(B6C)2Ni] complex.
- schema:
  - `type`: text
  - `format`: XYZ

### vibrational_frequencies.json
- path: `/app/outputs/vibrational_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Lowest vibrational frequencies and reality flags for the three sandwich complexes, verified by frequency calculations.
- schema:
  - `type`: object
  - `required`: `Fe`, `Co`, `Ni`
  - `properties`:
    - `Fe`:
      - `type`: object
      - `required`: `lowest_frequency`, `all_real`
      - `properties`:
        - `lowest_frequency`:
          - `type`: number
          - `unit`: cm-1
        - `all_real`:
          - `type`: boolean
    - `Co`:
      - `type`: object
      - `required`: `lowest_frequency`, `all_real`
      - `properties`:
        - `lowest_frequency`:
          - `type`: number
          - `unit`: cm-1
        - `all_real`:
          - `type`: boolean
    - `Ni`:
      - `type`: object
      - `required`: `lowest_frequency`, `all_real`
      - `properties`:
        - `lowest_frequency`:
          - `type`: number
          - `unit`: cm-1
        - `all_real`:
          - `type`: boolean

Notes: The target bond lengths and frequencies are compared to the paper's reported values using tolerances appropriate for a different DFT engine (ORCA vs. Gaussian).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "D6d_Fe.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "format": "XYZ"
      },
      "description": "Optimized Cartesian coordinates of the D6d [(B6C)2Fe]2- complex. The checker recomputes bond lengths (B–B, B–C, B–Fe, C–Fe) from these coordinates."
    },
    {
      "file": "D6d_Co.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "format": "XYZ"
      },
      "description": "Optimized Cartesian coordinates of the D6d [(B6C)2Co]- complex."
    },
    {
      "file": "D6d_Ni.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "format": "XYZ"
      },
      "description": "Optimized Cartesian coordinates of the D6d [(B6C)2Ni] complex."
    },
    {
      "file": "vibrational_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Fe",
          "Co",
          "Ni"
        ],
        "properties": {
          "Fe": {
            "type": "object",
            "required": [
              "lowest_frequency",
              "all_real"
            ],
            "properties": {
              "lowest_frequency": {
                "type": "number",
                "unit": "cm-1"
              },
              "all_real": {
                "type": "boolean"
              }
            }
          },
          "Co": {
            "type": "object",
            "required": [
              "lowest_frequency",
              "all_real"
            ],
            "properties": {
              "lowest_frequency": {
                "type": "number",
                "unit": "cm-1"
              },
              "all_real": {
                "type": "boolean"
              }
            }
          },
          "Ni": {
            "type": "object",
            "required": [
              "lowest_frequency",
              "all_real"
            ],
            "properties": {
              "lowest_frequency": {
                "type": "number",
                "unit": "cm-1"
              },
              "all_real": {
                "type": "boolean"
              }
            }
          }
        }
      },
      "description": "Lowest vibrational frequencies and reality flags for the three sandwich complexes, verified by frequency calculations."
    }
  ],
  "notes": "The target bond lengths and frequencies are compared to the paper's reported values using tolerances appropriate for a different DFT engine (ORCA vs. Gaussian)."
}
```

## How you are scored
An automated verifier will score your submitted artifacts independently for each workflow stage. The verifier computes average bond lengths (B–B, B–C, B–M, C–M) from each XYZ file and compares them to a hidden reference. It also checks that the reported lowest frequencies are positive (real) and consistent with the reference. The final reward is a weighted combination of these checks. Honest execution of the DFT workflow is sufficient; you do not need to know the exact target numbers in advance. The verifier uses tolerances that accommodate typical variations between DFT implementations, so a correct re‑run will pass.
