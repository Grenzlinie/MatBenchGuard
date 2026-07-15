# Energy Minimization of sPBD12 Perfect Crystal with Universal Force Field

## Problem background
Syndiotactic 1,2-poly(1,3-butadiene) (sPBD12) is a thermoplastic elastomer with a known crystal structure. The crystal lattice is orthorhombic, space group Pcam, with experimental unit cell dimensions a = 10.98 Å, b = 6.60 Å, c = 5.14 Å. The asymmetric unit contains four carbon atoms whose published fractional coordinates are: C1 (0.000, 0.916, 0.000), C2 (0.014, 0.050, 0.250), C3 (0.136, 0.143, 0.250), C4 (0.143, 0.342, 0.250). Molecular mechanics force field calculations can relax this initial geometry to an energy-minimum, yielding an optimized unit cell and atomic positions. This perfect‑crystal optimization serves as a baseline for subsequent studies of configurational defects and comparison with X‑ray diffraction.

## Approach
Perform a full molecular mechanics geometry optimization using the Universal force field (UFF), which is equivalent to the Universal 1.02 force field. Starting from the experimental unit cell and fractional coordinates given above, maintain the Pcam space group and allow both the unit cell axes (a, b, c) and the atomic positions to relax to their lowest‑energy configuration. The minimization can be carried out with any open‑source tool that implements the Universal force field, such as Open Babel or LAMMPS.

## Reproduction target
Produce the optimized unit cell axes (a, b, c in ångströms) and the fractional coordinates (x, y, z) of the four carbon atoms C1–C4 in the asymmetric unit after energy minimization. Write these results into a JSON file named `step_01_perfect_crystal_results.json` in the output directory `/app/outputs`, following the exact format and schema described in the output contract.

## Assets

- sPBD12 initial crystal structure from Natta & Corradini (1956)
- Open Babel: https://pypi.org/project/openbabel/
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/

## Workflow steps

### Step 1: Build initial perfect crystal model
- Role: process
- Action: Construct the initial perfect crystal of sPBD12 in space group Pcam using the known experimental unit cell (a=10.98 Å, b=6.60 Å, c=5.14 Å) and the fractional coordinates of carbon atoms from Natta & Corradini (1956). Set up the input file for energy minimization.
- Evidence: `/app/outputs/initial_structure.log`

### Step 2: Energy minimization of perfect crystal with Universal 1.02
- Role: scored (load-bearing)
- Action: Minimize the energy of the crystal using the Universal 1.02 force field (via Open Babel or LAMMPS), allowing both the unit cell dimensions and atomic positions to relax. Write the final optimized cell axes and fractional coordinates to step_01_perfect_crystal_results.json.
- Output file: `/app/outputs/step_01_perfect_crystal_results.json`
- Format: json
- Contract: {"cell_axes": {"a": float, "b": float, "c": float},"fractional_coordinates": [{"atom": "C1", "x": float, "y": float, "z": float},{"atom": "C2", "x": float, "y": float, "z": float},{"atom": "C3", "x": float, "y": float, "z": float},{"atom": "C4", "x": float, "y": float, "z": float}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_perfect_crystal_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_perfect_crystal_results.json
- path: `/app/outputs/step_01_perfect_crystal_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized unit cell axes and fractional coordinates after energy minimization with the Universal 1.02 force field.
- schema:
  - `type`: object
  - `required`: `cell_axes`, `fractional_coordinates`
  - `properties`:
    - `cell_axes`:
      - `type`: object
      - `required`: `a`, `b`, `c`
      - `properties`:
        - `a`:
          - `type`: number
        - `b`:
          - `type`: number
        - `c`:
          - `type`: number
    - `fractional_coordinates`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `atom`, `x`, `y`, `z`
        - `properties`:
          - `atom`:
            - `type`: string
            - `enum`: `C1`, `C2`, `C3`, `C4`
          - `x`:
            - `type`: number
          - `y`:
            - `type`: number
          - `z`:
            - `type`: number
      - `minItems`: 4
      - `maxItems`: 4

Notes: Only the perfect crystal energy minimization with Universal 1.02 is scored. The hidden checker compares the submitted cell axes and fractional coordinates against reference values from the original paper’s tables within specified tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_perfect_crystal_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "cell_axes",
          "fractional_coordinates"
        ],
        "properties": {
          "cell_axes": {
            "type": "object",
            "required": [
              "a",
              "b",
              "c"
            ],
            "properties": {
              "a": {
                "type": "number"
              },
              "b": {
                "type": "number"
              },
              "c": {
                "type": "number"
              }
            }
          },
          "fractional_coordinates": {
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
                  "type": "string",
                  "enum": [
                    "C1",
                    "C2",
                    "C3",
                    "C4"
                  ]
                },
                "x": {
                  "type": "number"
                },
                "y": {
                  "type": "number"
                },
                "z": {
                  "type": "number"
                }
              }
            },
            "minItems": 4,
            "maxItems": 4
          }
        }
      },
      "description": "Optimized unit cell axes and fractional coordinates after energy minimization with the Universal 1.02 force field."
    }
  ],
  "notes": "Only the perfect crystal energy minimization with Universal 1.02 is scored. The hidden checker compares the submitted cell axes and fractional coordinates against reference values from the original paper’s tables within specified tolerances."
}
```

## How you are scored
A hidden verifier scores each workflow step independently. For the load‑bearing energy minimization step, the verifier compares your optimized cell axes and fractional coordinates against reference values within predetermined tolerances. The overall reward is a weighted combination of the scores from all steps, with the energy minimization carrying the largest weight. You must actually execute the simulation; simply reporting literature values or skipping the minimization will not earn full credit.
