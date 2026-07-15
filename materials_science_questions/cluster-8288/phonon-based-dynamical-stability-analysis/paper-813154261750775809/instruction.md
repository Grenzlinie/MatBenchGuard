# High-pressure phase stability and dynamical stability of KN3 from first principles

## Problem background
Potassium azide (KN3) is an ionic azide compound that under ambient conditions crystallizes in a body-centered tetragonal lattice with I4/mcm symmetry containing linear N3⁻ anions. At high pressures, the crystal structure may undergo phase transitions, potentially leading to rearrangements of the nitrogen sublattice. The formation of non‑molecular nitrogen networks or rings under pressure is of fundamental interest as a route to high‑energy‑density materials. However, the detailed high‑pressure phase sequence of KN3, including the existence and stability of structures featuring planar N6 rings, is not fully understood. This task aims to compute the relative phase stability of KN3 across a broad pressure range using first‑principles methods and to assess the dynamical stability of a hexagonal phase featuring planar N6 rings.

## Approach
The method combines evolutionary crystal structure prediction with density functional theory (DFT). First, a variable‑cell evolutionary search is performed at selected pressures (20, 60, and 100 GPa) with unit cells of different sizes to generate low‑enthalpy candidate structures. The promising candidates are then refined with high‑accuracy DFT relaxations using the PBE exchange‑correlation functional, with tight convergence criteria for energy, forces, and stress. For the key candidate phases—tetragonal I4/mcm, monoclinic C2/m, and hexagonal P6/mmm—enthalpies are computed over a dense pressure grid from 0 to 100 GPa. All enthalpies are referenced to the C2/m phase. The pressure‑dependent enthalpy differences are collected to determine which phase is the most stable at each pressure. For the P6/mmm phase, which contains planar N6 rings, a phonon calculation using density functional perturbation theory (DFPT) is performed at the highest pressure (100 GPa) to obtain the phonon frequencies at high‑symmetry k‑points. The absence of imaginary frequencies indicates that the phase is dynamically stable. The DFT engine is Quantum ESPRESSO, using GBRV ultrasoft pseudopotentials for potassium and nitrogen.

## Reproduction target
Produce two scored artifacts:
1. `enthalpy_curves.json`: Compute enthalpy differences (eV per formula unit) relative to the C2/m phase for the three phases I4/mcm, C2/m, and P6/mmm as a function of pressure from 0 to 100 GPa. From this data, the stable phase sequence and the pressure ranges where each phase is most stable can be deduced.
2. `phonon_frequencies.json`: Compute the phonon frequencies at the high‑symmetry k‑points Gamma, M, K, and A for the P6/mmm structure at 100 GPa. The frequencies must be real (non‑negative), confirming that this hexagonal phase is dynamically stable at that pressure.

## Assets

- USPEX evolutionary crystal structure prediction code: http://uspex-team.org/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GBRV pseudopotentials: http://www.physics.rutgers.edu/gbrv/

## Workflow steps

### Step 1: Variable-cell evolutionary structure search
- Role: process
- Action: Run USPEX coupled with Quantum ESPRESSO to perform variable‑cell evolutionary structure prediction of KN3 at 20, 60, and 100 GPa, each with unit cells containing 1, 2, and 4 formula units. Use the PBE functional and GBRV pseudopotentials. The output is a set of low‑enthalpy candidate structures (including I4/mcm, C2/m, and P6/mmm).
- Evidence: none

### Step 2: High‑accuracy enthalpy calculations
- Role: process
- Action: For the identified candidate structures (especially I4/mcm, C2/m, P6/mmm), perform full DFT relaxations at a grid of pressures between 0 and 100 GPa using Quantum ESPRESSO with increased convergence (energy convergence 1.0e-6 eV, force threshold 0.001 eV/Å, stress <0.01 GPa). Compute the enthalpy per formula unit at each pressure, referencing all values to the enthalpy of the C2/m structure.
- Evidence: none

### Step 3: Output enthalpy curves
- Role: scored (load-bearing)
- Action: Assemble the enthalpy differences (eV/f.u.) relative to C2/m for the three key phases (I4/mcm, C2/m, P6/mmm) at a set of pressures spanning 0–100 GPa and write them to enthalpy_curves.json.
- Output file: `/app/outputs/enthalpy_curves.json`
- Format: json
- Contract: JSON object with keys 'I4/mcm', 'C2/m', 'P6/mmm', each an array of objects {pressure: float (GPa), enthalpy_delta: float (eV/f.u.)}.
- Scoring: scored by hidden verifier

### Step 4: Phonon dispersion for P6/mmm
- Role: scored
- Action: Perform a density functional perturbation theory (DFPT) phonon calculation using Quantum ESPRESSO on the optimized P6/mmm structure at 100 GPa. Extract the phonon frequencies at high‑symmetry k‑points and save them to phonon_frequencies.json.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: JSON object with keys as high‑symmetry k‑point labels (e.g. 'Gamma', 'M', 'K', 'A'), each an array of frequencies (cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/enthalpy_curves.json`
- `/app/outputs/phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### enthalpy_curves.json
- path: `/app/outputs/enthalpy_curves.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Enthalpy differences relative to C2/m for the three candidate phases across the pressure range. The checker will determine the stable phase sequence and transition pressures from these curves.
- schema:
  - `type`: object
  - `required`: `I4/mcm`, `C2/m`, `P6/mmm`
  - `properties`:
    - `I4/mcm`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `pressure`, `enthalpy_delta`
        - `properties`:
          - `pressure`:
            - `type`: number
            - `unit`: GPa
          - `enthalpy_delta`:
            - `type`: number
            - `unit`: eV/f.u.
    - `C2/m`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `pressure`, `enthalpy_delta`
        - `properties`:
          - `pressure`:
            - `type`: number
            - `unit`: GPa
          - `enthalpy_delta`:
            - `type`: number
            - `unit`: eV/f.u.
    - `P6/mmm`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `pressure`, `enthalpy_delta`
        - `properties`:
          - `pressure`:
            - `type`: number
            - `unit`: GPa
          - `enthalpy_delta`:
            - `type`: number
            - `unit`: eV/f.u.

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Phonon frequencies at high-symmetry k-points for P6/mmm at 100 GPa. The checker will verify the absence of imaginary frequencies.
- schema:
  - `type`: object
  - `required`: `Gamma`, `M`, `K`, `A`
  - `properties`:
    - `Gamma`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: cm⁻¹
    - `M`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: cm⁻¹
    - `K`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: cm⁻¹
    - `A`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: cm⁻¹
  - `additionalProperties`:
    - `type`: array
    - `items`:
      - `type`: number
      - `unit`: cm⁻¹

Notes: The enthalpy curves are scored by identifying the stable phase sequence and transition pressures; the phonon frequencies are scored by verifying dynamical stability (absence of imaginary modes).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "enthalpy_curves.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "I4/mcm",
          "C2/m",
          "P6/mmm"
        ],
        "properties": {
          "I4/mcm": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "pressure",
                "enthalpy_delta"
              ],
              "properties": {
                "pressure": {
                  "type": "number",
                  "unit": "GPa"
                },
                "enthalpy_delta": {
                  "type": "number",
                  "unit": "eV/f.u."
                }
              }
            }
          },
          "C2/m": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "pressure",
                "enthalpy_delta"
              ],
              "properties": {
                "pressure": {
                  "type": "number",
                  "unit": "GPa"
                },
                "enthalpy_delta": {
                  "type": "number",
                  "unit": "eV/f.u."
                }
              }
            }
          },
          "P6/mmm": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "pressure",
                "enthalpy_delta"
              ],
              "properties": {
                "pressure": {
                  "type": "number",
                  "unit": "GPa"
                },
                "enthalpy_delta": {
                  "type": "number",
                  "unit": "eV/f.u."
                }
              }
            }
          }
        }
      },
      "description": "Enthalpy differences relative to C2/m for the three candidate phases across the pressure range. The checker will determine the stable phase sequence and transition pressures from these curves."
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "Gamma",
          "M",
          "K",
          "A"
        ],
        "properties": {
          "Gamma": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "cm⁻¹"
            }
          },
          "M": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "cm⁻¹"
            }
          },
          "K": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "cm⁻¹"
            }
          },
          "A": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "cm⁻¹"
            }
          }
        },
        "additionalProperties": {
          "type": "array",
          "items": {
            "type": "number",
            "unit": "cm⁻¹"
          }
        }
      },
      "description": "Phonon frequencies at high-symmetry k-points for P6/mmm at 100 GPa. The checker will verify the absence of imaginary frequencies."
    }
  ],
  "notes": "The enthalpy curves are scored by identifying the stable phase sequence and transition pressures; the phonon frequencies are scored by verifying dynamical stability (absence of imaginary modes)."
}
```

## How you are scored
The hidden verifier independently evaluates each output artifact and combines the scores by weight to compute the final reward.
- For `enthalpy_curves.json`: The verifier reads the enthalpy differences and determines which phase has the lowest enthalpy at each pressure. The stable phase ordering and the approximate transition pressures are compared against expected values. The agreement of the derived phase sequence with the known pattern determines the score for this stage.
- For `phonon_frequencies.json`: The verifier checks that every listed frequency at the specified k‑points is non‑negative (a small tolerance for numerical noise is allowed). A fully non‑negative set earns full credit; the presence of significant imaginary (negative) frequencies reduces the score.
The final reward is a weighted sum, with the enthalpy curves contributing the larger share and the phonon check a moderate share.
