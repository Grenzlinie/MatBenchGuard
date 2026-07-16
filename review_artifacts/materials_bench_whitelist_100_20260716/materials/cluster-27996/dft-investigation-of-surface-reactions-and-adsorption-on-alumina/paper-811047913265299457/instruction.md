# Reproduce HF/STO-3G Orbital Spacings for Methoxide Adsorbate on Lithium Clusters

## Problem background
Methanol adsorbed on lithium surfaces forms a surface complex whose nature has been probed by He(I) ultraviolet photoelectron spectroscopy (UPS). The experimental identification relies heavily on molecular orbital calculations that provide the expected orbital energy spacings for candidate surface species. This reproduction task focuses on the computational evidence: computing the occupied molecular orbital spacings (relative to the highest occupied orbital) for specific methoxide-on‑lithium cluster models. By producing these computed orbital spacings, the computational support for the species assignment can be re‑examined.

## Approach
Two cluster models are constructed to represent a bcc Li(100) surface, using bulk lithium positions (lattice constant 3.509 Å): a nine‑atom cluster with five atoms in the first layer and four in the second (Li9(5,4)), and a nine‑atom cluster with four atoms in the first layer and five in the second (Li9(4,5)). A methoxide (CH3O) adsorbate is placed in an on‑top site on the first model, and in a symmetric double‑bridge site bridging two adjacent surface Li atoms on the second model. The internal geometry of the CH3O fragment is taken from a separately optimized CH3OLi at the HF/STO‑3G level (C–O = 1.403 Å, C–H = 1.097 Å, ∠OCH = 111.4°).

Geometry optimizations are performed at the Hartree–Fock/STO‑3G level of theory. All lithium atoms are held fixed at their bulk bcc positions, and the internal geometry of the methoxide group is frozen. The only relaxed coordinate is the distance from the oxygen atom to the surface plane, optimized to give the minimum total energy for each model. From the converged wavefunctions, the energies of the four highest occupied molecular orbitals are extracted and reported relative to the highest occupied orbital (HOMO), which is set to 0 eV.

## Reproduction target
Produce a JSON file, `/app/outputs/final_orbital_spacings.json`, containing the computed relative orbital energies (in eV) and total energies (in atomic units) for the two cluster models:

- `CH3O/Li9(5,4) on‑top`
- `CH3O/Li9(4,5) symmetric double‑bridge`

All calculations must be performed at the HF/STO‑3G level of theory. The relative orbital energies are expressed with respect to the HOMO (0.0 eV), listing the energies of the four highest occupied orbitals (HOMO and the next three).

## Assets

- Psi4 (or PySCF) quantum chemistry package: psi4

## Workflow steps

### Step 1: Build cluster models
- Role: process
- Action: Construct initial geometries for CH3O/Li9(5,4) on-top and CH3O/Li9(4,5) symmetric double-bridge models. Lithium atoms are placed at bcc lattice positions with lattice constant a=3.509 Å. Use CH3O geometry from a separately optimized CH3OLi at the same level (C-O=1.403 Å, C-H=1.097 Å, ∠OCH=111.4°).
- Evidence: `/app/outputs/cluster_models.xyz`

### Step 2: Geometry optimization
- Role: process
- Action: Perform constrained geometry optimization at the HF/STO-3G level. Keep all Li atoms fixed at bcc lattice positions and the internal geometry of the CH3O fragment fixed. Relax the Li-O distance (Re) for each model to find the minimum total energy.
- Evidence: `/app/outputs/optimization_results.json`

### Step 3: Report orbital spacings
- Role: scored (load-bearing)
- Action: Extract total energies (in atomic units) and energies of the four highest occupied molecular orbitals from the converged SCF wavefunctions of the optimized models. Compute orbital energies relative to the highest occupied molecular orbital (HOMO), set to 0.0 eV. Write the results to final_orbital_spacings.json.
- Output file: `/app/outputs/final_orbital_spacings.json`
- Format: json
- Contract: A JSON object with key 'models' containing a list of two entries. Each entry has 'model_name' (string), 'total_energy' (float, au), and 'relative_orbital_energies' (list of floats, eV, with the first element 0.0 for HOMO).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/final_orbital_spacings.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### final_orbital_spacings.json
- path: `/app/outputs/final_orbital_spacings.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Orbital spacings (four highest occupied orbitals) relative to HOMO for two CH3O/Li cluster models, as computed by HF/STO-3G.
- schema:
  - `type`: object
  - `required`: `models`
  - `properties`:
    - `models`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `model_name`, `total_energy`, `relative_orbital_energies`
        - `properties`:
          - `model_name`:
            - `type`: string
          - `total_energy`:
            - `type`: number
            - `description`: Hartree
          - `relative_orbital_energies`:
            - `type`: array
            - `items`:
              - `type`: number
            - `minItems`: 4
            - `maxItems`: 4
            - `description`: eV, four elements: HOMO (0.0), HOMO-1, HOMO-2, HOMO-3

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "final_orbital_spacings.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "models"
        ],
        "properties": {
          "models": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "model_name",
                "total_energy",
                "relative_orbital_energies"
              ],
              "properties": {
                "model_name": {
                  "type": "string"
                },
                "total_energy": {
                  "type": "number",
                  "description": "Hartree"
                },
                "relative_orbital_energies": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  },
                  "minItems": 4,
                  "maxItems": 4,
                  "description": "eV, four elements: HOMO (0.0), HOMO-1, HOMO-2, HOMO-3"
                }
              }
            }
          }
        }
      },
      "description": "Orbital spacings (four highest occupied orbitals) relative to HOMO for two CH3O/Li cluster models, as computed by HF/STO-3G."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier evaluates your submission by comparing the relative orbital energies and total energies in `final_orbital_spacings.json` to reference values derived from the original work. The comparison is designed to accept small numerical differences that naturally arise from using a different quantum chemistry code, so an honest computational reproduction is expected to pass. The verifier also checks that the required intermediate artifacts (`cluster_models.xyz`, `optimization_results.json`) are present and consistent with the workflow, but these checks carry only a minor weight. The final reward is a combined score over all stages; simply reporting the original paper's numbers without executing the computation will not satisfy the verifier.
