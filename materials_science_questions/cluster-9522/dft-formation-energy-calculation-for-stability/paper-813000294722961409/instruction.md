# DFT Optimization of O-Ti₂AlNb and Heusler Modifications

## Problem background
The Ti–Al–Nb intermetallic system contains an orthorhombic O‑Ti₂AlNb phase that can appear during high‑temperature oxidation and may influence the mechanical and oxidation behaviour of Ti₃Al‑based alloys. Density‑functional theory (DFT) can be used to determine its equilibrium crystal structure, compare its stability to hypothetical modifications, and provide quantitative geometric and energetic data. This task addresses the computational characterization of the O‑Ti₂AlNb phase and two predicted Heusler‑derived structures (H1 and H2) by performing first‑principles geometry optimizations with several exchange‑correlation functionals.

## Approach
The workflow targets three crystal structures: (1) the experimentally known orthorhombic O‑Ti₂AlNb (space group Cmcm, 4 formula units per cell), and two face‑centred cubic Heusler modifications — (2) H1 with Ti at 8c (¼,¼,¼), Al at 4a (0,0,0), Nb at 4b (½,½,½), and (3) H2 obtained by swapping Al and Nb from H1. For each structure, full‑cell DFT geometry optimizations are performed with three different exchange‑correlation functionals: the local density approximation (LDA), the generalized‑gradient approximation (PBE), and the hybrid functional B3LYP. The optimizations relax all atomic positions and lattice parameters until forces and stresses are converged. The resulting optimized lattice constants, atomic coordinates, and total energies per formula unit are collected into a single JSON artifact. This design allows a comparison of the O‑phase geometry with independent experimental reference data and an assessment of the energetic ordering among the three structure candidates.

## Reproduction target
Produce the file `optimized_structures_and_energies.json` containing, for each of the nine structure‑functional combinations (O / H1 / H2 and LDA / PBE / B3LYP), the optimized lattice parameters (in Å), fractional atomic coordinates, and total energy per formula unit (with the energy unit stated). For the O‑phase entries, the computed lattice parameters are to be compared against the known experimental literature values to quantify geometry accuracy. For every functional, the O‑phase total energy must be lower than those of H1 and H2, and the energies of H1 and H2 must be nearly equal. The JSON file must contain exactly nine entries and be placed at `/app/outputs/optimized_structures_and_energies.json`.

## Assets

- Crystal structure of O-Ti₂AlNb (Cmcm, from Mozer et al. 1990)
- AlCu₂Mn Heusler prototype structure (Fm‑3m)
- Open‑source DFT code (e.g., Quantum ESPRESSO, CP2K, ABINIT): https://www.quantum-espresso.org/
- Standard pseudopotentials/basis sets for Ti, Al, Nb

## Workflow steps

### Step 1: Prepare DFT input structures
- Role: process
- Action: Using the crystal structure descriptions for O-Ti₂AlNb (Cmcm) and the Heusler prototype (Fm‑3m), create input files for DFT geometry optimization for the O‑Ti₂AlNb structure and the two Heusler‑derived modifications H1 and H2. Each structure must be prepared for calculations with the LDA, GGA‑PBE, and hybrid B3LYP functionals.
- Evidence: `/app/outputs/input_structures.json`

### Step 2: Perform DFT geometry optimizations
- Role: process
- Action: For each of the three structures (O, H1, H2) and each of the three functionals (LDA, GGA‑PBE, B3LYP), run a full‑cell DFT geometry optimization using an open‑source code. Relax atomic positions and lattice cell parameters until forces and stresses converge. Record the total energy, optimized lattice parameters, and final atomic positions for each calculation.
- Evidence: `/app/outputs/dft_logs.json`

### Step 3: Compile optimized structures and energies
- Role: scored (load-bearing)
- Action: Compile the optimized lattice parameters, atomic positions, and total energies per formula unit for O‑Ti₂AlNb, H1, and H2 for each functional (LDA, GGA‑PBE, B3LYP) into a JSON file.
- Output file: `/app/outputs/optimized_structures_and_energies.json`
- Format: json
- Contract: Array of objects. Each object keys: 'structure_id' (string: 'O','H1','H2'), 'functional' (string: 'LDA','PBE','B3LYP'), 'lattice_parameters_angstrom' (object with keys a,b,c; for cubic H1/H2, b and c equal a), 'atomic_positions' (array of objects with keys 'element' (string) and 'fractional_coordinates' (array of three floats)), 'total_energy_per_fu' (float, total energy per formula unit), 'energy_unit' (string: 'eV' or 'Hartree').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_structures_and_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_structures_and_energies.json
- path: `/app/outputs/optimized_structures_and_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Optimized structures and total energies for Ti2AlNb phases. The verifier evaluates both lattice parameter accuracy and energetic stability relations.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `structure_id`, `functional`, `lattice_parameters_angstrom`, `atomic_positions`, `total_energy_per_fu`, `energy_unit`
    - `properties`:
      - `structure_id`:
        - `type`: string
        - `enum`: `O`, `H1`, `H2`
      - `functional`:
        - `type`: string
        - `enum`: `LDA`, `PBE`, `B3LYP`
      - `lattice_parameters_angstrom`:
        - `type`: object
        - `properties`:
          - `a`:
            - `type`: number
          - `b`:
            - `type`: number
          - `c`:
            - `type`: number
        - `required`: `a`, `b`, `c`
      - `atomic_positions`:
        - `type`: array
        - `items`:
          - `type`: object
          - `properties`:
            - `element`:
              - `type`: string
            - `fractional_coordinates`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
          - `required`: `element`, `fractional_coordinates`
      - `total_energy_per_fu`:
        - `type`: number
      - `energy_unit`:
        - `type`: string
  - `description`: For O-phase entries, the checker recomputes percentage deviation of lattice parameters from the experimental literature reference values and scores based on closeness. Additionally, the checker verifies energy ordering: for each functional, O-phase energy must be lower than H1 and H2, and |E(H1)-E(H2)| < 0.01 Hartree. The array must contain exactly nine entries.

Notes: Merged the two previously duplicate output_contract entries into a single entry that covers both the metric_recompute (lattice deviations) and structural_audit (energy ordering/degeneracy) checks performed by the verifier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_structures_and_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "structure_id",
            "functional",
            "lattice_parameters_angstrom",
            "atomic_positions",
            "total_energy_per_fu",
            "energy_unit"
          ],
          "properties": {
            "structure_id": {
              "type": "string",
              "enum": [
                "O",
                "H1",
                "H2"
              ]
            },
            "functional": {
              "type": "string",
              "enum": [
                "LDA",
                "PBE",
                "B3LYP"
              ]
            },
            "lattice_parameters_angstrom": {
              "type": "object",
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
              },
              "required": [
                "a",
                "b",
                "c"
              ]
            },
            "atomic_positions": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "element": {
                    "type": "string"
                  },
                  "fractional_coordinates": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  }
                },
                "required": [
                  "element",
                  "fractional_coordinates"
                ]
              }
            },
            "total_energy_per_fu": {
              "type": "number"
            },
            "energy_unit": {
              "type": "string"
            }
          }
        },
        "description": "For O-phase entries, the checker recomputes percentage deviation of lattice parameters from the experimental literature reference values and scores based on closeness. Additionally, the checker verifies energy ordering: for each functional, O-phase energy must be lower than H1 and H2, and |E(H1)-E(H2)| < 0.01 Hartree. The array must contain exactly nine entries."
      },
      "description": "Optimized structures and total energies for Ti2AlNb phases. The verifier evaluates both lattice parameter accuracy and energetic stability relations."
    }
  ],
  "notes": "Merged the two previously duplicate output_contract entries into a single entry that covers both the metric_recompute (lattice deviations) and structural_audit (energy ordering/degeneracy) checks performed by the verifier."
}
```

## How you are scored
A hidden verifier reads your `optimized_structures_and_energies.json` and independently scores it against reference criteria. The evaluation is decomposed into four weighted components: (1) agreement of the O‑phase lattice parameters with the experimental reference (closer is better); (2) correct energetic ordering — for each functional the O‑phase must be the lowest‑energy structure; (3) near‑degeneracy of the H1 and H2 energies; and (4) completeness of the required data fields and entries. The verifier recomputes lattice‑parameter deviations and checks ordering and degeneracy conditions based solely on the values you provide. The weighted scores are combined into a single reward between 0 and 1. No credit is given for simply reporting numbers that look plausible; the verifier derives the evaluation from the raw submitted data.
