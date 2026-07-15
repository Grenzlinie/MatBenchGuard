# Structural Distortion of Vanadium Dioxide Phases Under Germanium Substitution

## Problem background
Vanadium dioxide (VO₂) undergoes a metal-insulator transition from a high-temperature rutile (R) phase to a low-temperature monoclinic (M1) phase. In the M1 phase, vanadium atoms form dimers along the crystallographic c-axis, whereas in the R phase, vanadium atoms are equally spaced. Doping with germanium (Ge) has been reported to increase the transition temperature. This task investigates how substitutional germanium affects the structural stability of the competing phases. In particular, we ask whether Ge dopants can induce M1-like dimerization in the rutile phase while leaving the already-dimerized M1 phase largely unperturbed.

## Approach
We model Ge-doped VO₂ using density-functional theory (DFT) supercell calculations. We perform structural relaxations with the Quantum ESPRESSO code using the PBE exchange-correlation functional and scalar-relativistic ultrasoft pseudopotentials. The supercells are constructed from the experimental unit cells of both the M1 and R phases, with one or two vanadium atoms replaced by germanium. After relaxation, we analyze the nearest-neighbor V–V distances along the chain direction and the angles between the V–V vector and the c-axis. Comparing these structural fingerprints between the R and M1 phases reveals the differential response to Ge doping.

## Reproduction target
Perform DFT structural relaxations for four Ge-doped VO₂ supercells:
1. M1 phase with a single Ge in a 2×2×2 supercell (M1_single).
2. Rutile phase with a single Ge in a 2×2×2 supercell (R_single).
3. M1 phase with two Ge atoms in the Ge₀₃ configuration in a 2×2×3 supercell (M1_Ge03).
4. Rutile phase with two Ge atoms in the Ge₀₃ configuration in a 2×2×3 supercell (R_Ge03).
For each relaxed structure, identify all nearest-neighbor V–V pairs along the c-direction and compute their interatomic distance (Å) and the angle between the V–V vector and the c-axis (degrees). Output these values as a JSON file `summary_structural_results.json` with keys `M1_single`, `R_single`, `M1_Ge03`, `R_Ge03`, each containing a `distances` array and an `angles` array. The verifier will evaluate the distributions of distances and angles for each system against pre-defined structural criteria.

## Assets

- Quantum ESPRESSO (v6.4.1 or later): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials for V, O, Ge (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- VO2 Ge-doped supercell input files (Materials Cloud record 2023.2): https://archive.materialscloud.org/record/2023.2

## Workflow steps

### Step 1: DFT structural relaxations of Ge-doped supercells
- Role: process
- Action: For each of the four target systems — (1) M1 VO2 with one Ge in a 2×2×2 supercell, (2) rutile VO2 with one Ge in a 2×2×2 supercell, (3) M1 VO2 with two Ge in the Ge03 configuration in a 2×2×3 supercell, (4) rutile VO2 with two Ge in the Ge03 configuration in a 2×2×3 supercell — set up a Quantum ESPRESSO calculation using the PBE functional, SSSP pseudopotentials, and relax atomic positions and lattice vectors. The relaxed geometries from these calculations are required for the subsequent structural analysis.
- Evidence: `/app/outputs/relaxed_outputs`

### Step 2: Compute V–V distances and tilt angles
- Role: scored (load-bearing)
- Action: From each relaxed supercell, identify all nearest-neighbor V–V pairs along the chain direction (c-axis). For each pair, calculate the interatomic distance and the angle between the V–V vector and the c-axis. Write a JSON file `summary_structural_results.json` containing, under the keys 'M1_single', 'R_single', 'M1_Ge03', 'R_Ge03', objects with fields 'distances' (list of floats in Å) and 'angles' (list of floats in degrees).
- Output file: `/app/outputs/summary_structural_results.json`
- Format: json
- Contract: {"M1_single": {"distances": [float, ...], "angles": [float, ...]}, "R_single": {"distances": [float, ...], "angles": [float, ...]}, "M1_Ge03": {"distances": [float, ...], "angles": [float, ...]}, "R_Ge03": {"distances": [float, ...], "angles": [float, ...]}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/summary_structural_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### summary_structural_results.json
- path: `/app/outputs/summary_structural_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Distributions of nearest-neighbor V–V distances (in Å) and tilt angles (in degrees) for the four doped systems, used to verify structural trends.
- schema:
  - `type`: object
  - `properties`:
    - `M1_single`:
      - `type`: object
      - `properties`:
        - `distances`:
          - `type`: array
          - `items`:
            - `type`: number
          - `unit`: Angstrom
        - `angles`:
          - `type`: array
          - `items`:
            - `type`: number
          - `unit`: degrees
    - `R_single`:
      - `type`: object
      - `properties`:
        - `distances`:
          - `type`: array
          - `items`:
            - `type`: number
          - `unit`: Angstrom
        - `angles`:
          - `type`: array
          - `items`:
            - `type`: number
          - `unit`: degrees
    - `M1_Ge03`:
      - `type`: object
      - `properties`:
        - `distances`:
          - `type`: array
          - `items`:
            - `type`: number
          - `unit`: Angstrom
        - `angles`:
          - `type`: array
          - `items`:
            - `type`: number
          - `unit`: degrees
    - `R_Ge03`:
      - `type`: object
      - `properties`:
        - `distances`:
          - `type`: array
          - `items`:
            - `type`: number
          - `unit`: Angstrom
        - `angles`:
          - `type`: array
          - `items`:
            - `type`: number
          - `unit`: degrees
  - `required`: `M1_single`, `R_single`, `M1_Ge03`, `R_Ge03`

Notes: The R-phase systems are expected to show significantly broader/split distance distributions and non-zero tilt angles compared to M1, but the exact tolerance ranges for the structural audit are defined in the hidden checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "summary_structural_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "properties": {
          "M1_single": {
            "type": "object",
            "properties": {
              "distances": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "unit": "Angstrom"
              },
              "angles": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "unit": "degrees"
              }
            }
          },
          "R_single": {
            "type": "object",
            "properties": {
              "distances": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "unit": "Angstrom"
              },
              "angles": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "unit": "degrees"
              }
            }
          },
          "M1_Ge03": {
            "type": "object",
            "properties": {
              "distances": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "unit": "Angstrom"
              },
              "angles": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "unit": "degrees"
              }
            }
          },
          "R_Ge03": {
            "type": "object",
            "properties": {
              "distances": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "unit": "Angstrom"
              },
              "angles": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "unit": "degrees"
              }
            }
          }
        },
        "required": [
          "M1_single",
          "R_single",
          "M1_Ge03",
          "R_Ge03"
        ]
      },
      "description": "Distributions of nearest-neighbor V–V distances (in Å) and tilt angles (in degrees) for the four doped systems, used to verify structural trends."
    }
  ],
  "notes": "The R-phase systems are expected to show significantly broader/split distance distributions and non-zero tilt angles compared to M1, but the exact tolerance ranges for the structural audit are defined in the hidden checker."
}
```

## How you are scored
A hidden verifier reads your `summary_structural_results.json`. It computes a score for each of the four systems based on how well the recorded distance and angle distributions match the expected structural trends, using quantitative thresholds. The overall reward is a weighted combination of the per-system scores. Reporting the correct distributions requires faithfully executing the DFT relaxations; the verifier does not simply compare your numbers against a single gold value.
