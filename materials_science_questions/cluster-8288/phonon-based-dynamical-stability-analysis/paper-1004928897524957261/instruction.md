# Phonon stability and band gap of alkali-functionalized CuSe/AgSe monolayers

## Problem background
Two-dimensional (2D) transition metal monochalcogenides (TMMs) such as CuSe and AgSe monolayers have recently been fabricated. They adopt a planar honeycomb crystal structure (space group P3m1) with one metal and one Se atom per primitive unit cell. In their pristine form, the electronic character of these monolayers may limit their use in semiconductor devices. This task investigates the ground-state structural and electronic properties of pristine CuSe and AgSe monolayers and explores whether surface functionalization with alkali metal atoms (Li, K) can modify the electronic band gap and dynamical stability.

## Approach
Use density functional theory (DFT) at the generalized-gradient-approximation level with the Perdew–Burke–Ernzerhof (PBE) functional, implemented in the open-source Quantum ESPRESSO package with standard PBE pseudopotentials. The conceptual workflow is: (1) construct and relax the pristine CuSe and AgSe monolayers via variable-cell geometry optimization; (2) compute isolated-atom reference energies (Cu, Ag, Se) as inputs to the cohesive energy evaluation; (3) perform band-structure calculations on the relaxed pristine monolayers to determine their electronic band gap; (4) for Li on CuSe, compare the total energies of four high-symmetry adsorption sites (top-Se, top-Cu, hollow, bridge) to locate the most stable binding configuration; (5) relax the full Li- and K-functionalized CuSe systems starting from the identified most stable site; (6) compute the electronic band structure for Li-CuSe to obtain its band gap, and compute the phonon dispersion for K-CuSe via the finite-displacement method to assess its dynamical stability. All reported quantities are extracted directly from the DFT total energies and band structures.

## Reproduction target
Produce two scored JSON artifacts under `/app/outputs`:  
- **`pristine_results.json`** — For pristine CuSe and AgSe monolayers, report the relaxed equilibrium lattice constant `a` (Å), the cohesive energy per atom (eV) computed as `(E_tot − E_metal − E_Se) / 2`, and the PBE electronic band gap (eV).  
- **`functionalized_results.json`** — For Li-functionalized CuSe (Li-CuSe), report the PBE electronic band gap (eV) and a boolean flag indicating dynamical stability. For K-functionalized CuSe (K-CuSe), report a boolean flag indicating dynamical stability (based on the presence or absence of imaginary frequencies in the computed phonon dispersion).

## Assets

- Quantum ESPRESSO (pw.x, ph.x): https://www.quantum-espresso.org/
- SSSP Efficiency PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Relax pristine CuSe and AgSe monolayers and compute isolated atom energies
- Role: process
- Action: Construct the planar honeycomb crystal structures for CuSe and AgSe (space group P3m1, primitive unit cell with one metal and one Se atom). Perform a variable-cell geometry relaxation for each using DFT (PBE functional) as implemented in Quantum ESPRESSO pw.x. Additionally, compute total energies of isolated Cu, Ag, and Se atoms in large cells to serve as isolated-atom references.
- Evidence: none

### Step 2: Compute pristine structural and electronic baseline
- Role: scored (load-bearing)
- Action: From the relaxed geometries and isolated atom energies, extract the lattice constant a, compute the cohesive energy per atom as E_coh = (E_tot - E_X - E_Se)/2, and perform a band structure calculation to determine the electronic band gap (should be zero). Write the results to pristine_results.json.
- Output file: `/app/outputs/pristine_results.json`
- Format: json
- Contract: {"CuSe": {"lattice_constant_a": "float (Å)", "cohesive_energy_per_atom": "float (eV)", "band_gap": 0.0}, "AgSe": {"lattice_constant_a": "float (Å)", "cohesive_energy_per_atom": "float (eV)", "band_gap": 0.0}}
- Scoring: scored by hidden verifier

### Step 3: Determine most stable adsorption site for Li on CuSe
- Role: process
- Action: Place a Li atom at the four high-symmetry sites (Top-Se, Top-Cu, Hollow, Bridge) on the relaxed CuSe monolayer. For each configuration, perform a geometry relaxation (allowing the Li and nearby atoms to move) at the PBE level. Identify the lowest-energy site.
- Evidence: none

### Step 4: Relax Li-CuSe and K-CuSe functionalized monolayers
- Role: process
- Action: For Li and K, place the alkali atom at the most stable hollow site on the relaxed CuSe monolayer and perform a full variable-cell geometry relaxation at the PBE level for each functionalized system (Li-CuSe and K-CuSe).
- Evidence: none

### Step 5: Assess electronic band gap of Li-CuSe and dynamical stability of K-CuSe
- Role: scored (load-bearing)
- Action: For the relaxed Li-CuSe system, compute the electronic band structure and determine the band gap (value, direct/indirect character). For the relaxed K-CuSe system, compute the phonon dispersion using the finite-displacement method (e.g., phonopy or ph.x) and check for the presence of imaginary frequencies indicating dynamical instability. Write the band gap for Li-CuSe and the dynamical stability flags for both systems to functionalized_results.json.
- Output file: `/app/outputs/functionalized_results.json`
- Format: json
- Contract: {"Li_CuSe": {"band_gap": "float (eV)", "dynamically_stable": true}, "K_CuSe": {"dynamically_stable": false}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_results.json`
- `/app/outputs/functionalized_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_results.json
- path: `/app/outputs/pristine_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Structural and electronic properties of pristine CuSe and AgSe monolayers.
- schema:
  - `type`: object
  - `required`: `CuSe`, `AgSe`
  - `properties`:
    - `CuSe`:
      - `type`: object
      - `required`: `lattice_constant_a`, `cohesive_energy_per_atom`, `band_gap`
      - `properties`:
        - `lattice_constant_a`:
          - `type`: number
          - `unit`: Å
        - `cohesive_energy_per_atom`:
          - `type`: number
          - `unit`: eV
        - `band_gap`:
          - `type`: number
          - `unit`: eV
          - `expected`: 0
    - `AgSe`:
      - `type`: object
      - `required`: `lattice_constant_a`, `cohesive_energy_per_atom`, `band_gap`
      - `properties`:
        - `lattice_constant_a`:
          - `type`: number
          - `unit`: Å
        - `cohesive_energy_per_atom`:
          - `type`: number
          - `unit`: eV
        - `band_gap`:
          - `type`: number
          - `unit`: eV
          - `expected`: 0

### functionalized_results.json
- path: `/app/outputs/functionalized_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Electronic band gap for Li-CuSe and dynamical stability flags for Li-CuSe and K-CuSe.
- schema:
  - `type`: object
  - `required`: `Li_CuSe`, `K_CuSe`
  - `properties`:
    - `Li_CuSe`:
      - `type`: object
      - `required`: `band_gap`, `dynamically_stable`
      - `properties`:
        - `band_gap`:
          - `type`: number
          - `unit`: eV
          - `threshold`: 0
        - `dynamically_stable`:
          - `type`: boolean
    - `K_CuSe`:
      - `type`: object
      - `required`: `dynamically_stable`
      - `properties`:
        - `dynamically_stable`:
          - `type`: boolean

Notes: Checker compares pristine lattice constants, cohesive energies, and band gap zero within appropriate tolerances; Li-CuSe band gap > 0 confirms metal-to-semiconductor transition; dynamical stability flags must match expected stability.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "CuSe",
          "AgSe"
        ],
        "properties": {
          "CuSe": {
            "type": "object",
            "required": [
              "lattice_constant_a",
              "cohesive_energy_per_atom",
              "band_gap"
            ],
            "properties": {
              "lattice_constant_a": {
                "type": "number",
                "unit": "Å"
              },
              "cohesive_energy_per_atom": {
                "type": "number",
                "unit": "eV"
              },
              "band_gap": {
                "type": "number",
                "unit": "eV",
                "expected": 0
              }
            }
          },
          "AgSe": {
            "type": "object",
            "required": [
              "lattice_constant_a",
              "cohesive_energy_per_atom",
              "band_gap"
            ],
            "properties": {
              "lattice_constant_a": {
                "type": "number",
                "unit": "Å"
              },
              "cohesive_energy_per_atom": {
                "type": "number",
                "unit": "eV"
              },
              "band_gap": {
                "type": "number",
                "unit": "eV",
                "expected": 0
              }
            }
          }
        }
      },
      "description": "Structural and electronic properties of pristine CuSe and AgSe monolayers."
    },
    {
      "file": "functionalized_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "Li_CuSe",
          "K_CuSe"
        ],
        "properties": {
          "Li_CuSe": {
            "type": "object",
            "required": [
              "band_gap",
              "dynamically_stable"
            ],
            "properties": {
              "band_gap": {
                "type": "number",
                "unit": "eV",
                "threshold": 0
              },
              "dynamically_stable": {
                "type": "boolean"
              }
            }
          },
          "K_CuSe": {
            "type": "object",
            "required": [
              "dynamically_stable"
            ],
            "properties": {
              "dynamically_stable": {
                "type": "boolean"
              }
            }
          }
        }
      },
      "description": "Electronic band gap for Li-CuSe and dynamical stability flags for Li-CuSe and K-CuSe."
    }
  ],
  "notes": "Checker compares pristine lattice constants, cohesive energies, and band gap zero within appropriate tolerances; Li-CuSe band gap > 0 confirms metal-to-semiconductor transition; dynamical stability flags must match expected stability."
}
```

## How you are scored
A hidden verifier independently reads each scored output file and compares the reported quantities against reference data using appropriate tolerances. Every scored step carries a share of the total reward. The verifier follows directional scoring rules: for quantities where a better value exists, meeting or exceeding a reference threshold earns full credit, and credit only degrades for results that fall short; for fixed deterministic quantities, closeness to the reference within tolerance is required. Reporting values without evidence of the required DFT computations is insufficient — the verifier checks structural consistency across artifacts. Rewards from all scored stages are combined into a single final score between 0 and 1.
