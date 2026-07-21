# DFT-Based Internal Reorganization Energy of Halogen-Substituted Pentacenes

## Problem background
Organic semiconductors rely on small internal reorganization energies (λ) to achieve high charge-carrier mobility. Pentacene is a benchmark material with excellent mobility, but its poor solubility in common organic solvents limits low-cost processing. Introducing halogen substituents (F, Cl, Br) at specific positions is proposed to improve solubility while preserving favourable charge-transport properties. The central quantity of interest is the internal reorganization energy for holes (λ†) and electrons (λ‡), which can be obtained from density functional theory (DFT) calculations on the neutral, cation, and anion states of pentacene and six halogen-substituted pentacenes.

## Approach
The workflow uses DFT to optimise the geometries of all molecules in their neutral, cationic, and anionic states at the B3LYP/6-31G(d) level, starting from nearly planar initial structures. Vibrational frequencies are computed at the same level to characterise the stationary points. Single-point energies are then calculated on the optimised geometries using the larger 6-311+G(d,p) basis set, which includes diffuse functions essential for accurate anion energies. For each molecule, seven energy terms are collected: neutral energy at its equilibrium geometry (E0(Q0)), neutral energy at cation geometry (E0(Q+)), cation energy at neutral geometry (E+(Q0)), cation energy at its own geometry (E+(Q+)), and the analogous terms for the anion. These raw energies are the building blocks from which hole and electron reorganization energies are later derived.

## Reproduction target
Produce a single JSON file, `/app/outputs/reorganization_energies.json`, containing the seven Hartree energy terms listed above for each of the seven molecules: pentacene, 2-fluoropentacene, 2-chloropentacene, 2-bromopentacene, 2,9-difluoropentacene, 2,9-dichloropentacene, and 2,9-dibromopentacene. The file must follow the schema described in the output contract. From this file the verifier will compute λ† = (E0(Q†) – E0(Q0)) + (E†(Q0) – E†(Q†)) and λ‡ = (E0(Q‡) – E0(Q0)) + (E‡(Q0) – E‡(Q‡)), convert to electronvolts, and compare the values against hidden reference data. No other output from you is required.

## Assets

- Psi4 quantum chemistry package: psi4
- RDKit cheminformatics toolkit: rdkit

## Workflow steps

### Step 1: Generate initial molecular structures
- Role: process
- Action: Create initial planar Cartesian coordinates (roughly planar) for all seven molecules: pentacene, 2-fluoropentacene, 2-chloropentacene, 2-bromopentacene, 2,9-difluoropentacene, 2,9-dichloropentacene, 2,9-dibromopentacene, in neutral, cationic, and anionic states. Start from nearly planar structures.
- Evidence: none

### Step 2: B3LYP/6-31G(d) geometry optimization and frequency calculation
- Role: process
- Action: For each of the seven molecules, run DFT geometry optimization and vibrational frequency calculation for the neutral, cation, and anion states at the B3LYP/6-31G(d) level using initial nearly planar geometries. The optimized geometries (Q0, Q+, Q-) serve as equilibrium structures.
- Evidence: `/app/outputs/geometry_optimizations.log`

### Step 3: B3LYP/6-311+G(d,p) single-point energy calculations
- Role: process
- Action: Using the optimized geometries from step 1, compute single-point electronic energies at the B3LYP/6-311+G(d,p) level for all required charge/geometry combinations: E0(Q0), E0(Q+), E0(Q-), E+(Q0), E+(Q+), E-(Q0), E-(Q-).
- Evidence: none

### Step 4: Reorganization energy component assembly
- Role: scored (load-bearing)
- Action: Collect the seven single-point energies for each molecule and write them into /app/outputs/reorganization_energies.json according to the format specified in the output contract. The file must contain for each molecule the Hartree energies: E0_Q0, E0_Qplus, Eplus_Q0, Eplus_Qplus, E0_Qminus, Eminus_Q0, Eminus_Qminus.
- Output file: `/app/outputs/reorganization_energies.json`
- Format: json
- Contract: {
  "type": "object",
  "properties": {
    "molecules": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["molecule", "E0_Q0", "E0_Qplus", "Eplus_Q0", "Eplus_Qplus", "E0_Qminus", "Eminus_Q0", "Eminus_Qminus"],
        "properties": {
          "molecule": {"type": "string"},
          "E0_Q0": {"type": "number"},
          "E0_Qplus": {"type": "number"},
          "Eplus_Q0": {"type": "number"},
          "Eplus_Qplus": {"type": "number"},
          "E0_Qminus": {"type": "number"},
          "Eminus_Q0": {"type": "number"},
          "Eminus_Qminus": {"type": "number"}
        }
      }
    }
  },
  "required": ["molecules"]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reorganization_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reorganization_energies.json
- path: `/app/outputs/reorganization_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Reorganization energy components for pentacene and six halopentacenes. The checker recomputes hole (λ+) and electron (λ-) reorganization energies from these raw energies and scores against hidden paper values.
- schema:
  - `type`: object
  - `properties`:
    - `molecules`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `molecule`, `E0_Q0`, `E0_Qplus`, `Eplus_Q0`, `Eplus_Qplus`, `E0_Qminus`, `Eminus_Q0`, `Eminus_Qminus`
        - `properties`:
          - `molecule`:
            - `type`: string
          - `E0_Q0`:
            - `type`: number
          - `E0_Qplus`:
            - `type`: number
          - `Eplus_Q0`:
            - `type`: number
          - `Eplus_Qplus`:
            - `type`: number
          - `E0_Qminus`:
            - `type`: number
          - `Eminus_Q0`:
            - `type`: number
          - `Eminus_Qminus`:
            - `type`: number
  - `required`: `molecules`

Notes: The checker will verify that all computed λ+ and λ- are below 0.2 eV and check their agreement with paper-reported values within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reorganization_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "molecules": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "molecule",
                "E0_Q0",
                "E0_Qplus",
                "Eplus_Q0",
                "Eplus_Qplus",
                "E0_Qminus",
                "Eminus_Q0",
                "Eminus_Qminus"
              ],
              "properties": {
                "molecule": {
                  "type": "string"
                },
                "E0_Q0": {
                  "type": "number"
                },
                "E0_Qplus": {
                  "type": "number"
                },
                "Eplus_Q0": {
                  "type": "number"
                },
                "Eplus_Qplus": {
                  "type": "number"
                },
                "E0_Qminus": {
                  "type": "number"
                },
                "Eminus_Q0": {
                  "type": "number"
                },
                "Eminus_Qminus": {
                  "type": "number"
                }
              }
            }
          }
        },
        "required": [
          "molecules"
        ]
      },
      "description": "Reorganization energy components for pentacene and six halopentacenes. The checker recomputes hole (λ+) and electron (λ-) reorganization energies from these raw energies and scores against hidden paper values."
    }
  ],
  "notes": "The checker will verify that all computed λ+ and λ- are below 0.2 eV and check their agreement with paper-reported values within a tolerance."
}
```

## How you are scored
A hidden verifier reads your `reorganization_energies.json`, recomputes λ† and λ‡ for every molecule using the standard formulas, and evaluates them in two ways. First, each computed λ† and λ‡ is compared to a hidden reference value that is considered the correct result for this protocol; your energy terms must be accurate enough that the derived reorganization energies lie within an allowed tolerance. Second, the verifier checks whether the calculated reorganization energies satisfy a quantitative condition that is central to the material proposal. Your final reward is the fraction of molecule–charge‑carrier combinations (up to 14 values) that pass both the agreement-with-reference check and the condition check, averaged across all molecules. The condition itself is not revealed in this instruction, but it is a threshold on the reorganization energy that reflects the physical requirement for efficient charge transport.
