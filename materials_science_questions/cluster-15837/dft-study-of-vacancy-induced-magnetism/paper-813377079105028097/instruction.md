# DFT study of vacancy-induced magnetism in Bi2S3 and ZnS surfaces

## Problem background
The origin of room-temperature ferromagnetism in undoped semiconducting sulfides is an open question. Experiments on Bi2S3 and ZnS nanocrystalline powders suggest that intrinsic defects on the particle surfaces may be responsible. Density functional theory (DFT) studies can probe which types of defects—cation vacancies, anion vacancies, or interstitial atoms—produce magnetic moments and whether pairs of such defects couple ferromagnetically. This task reproduces the ab initio surface-defect calculations to compute magnetic moments for a range of defect configurations.

## Approach
We adopt a plane-wave pseudopotential DFT approach with a generalized-gradient approximation (e.g., PBE) functional. Supercell slab models of the Bi2S3(001) and ZnS(001) surfaces are built from bulk crystals, with a vacuum layer to isolate the slabs. Pristine, defect-free surfaces are first relaxed, then point defects are introduced: single neutral vacancies (Bi, Zn, S), single interstitial atoms (Bi, Zn), and pairs of cation vacancies at selected sites. For each defect model, spin-polarized total energies and forces are minimized, and the total magnetic moment of the cell is obtained. For the two-vacancy configurations, both ferromagnetic and antiferromagnetic initial spin arrangements are calculated, and the relative stability is determined. All calculations use the open-source Quantum ESPRESSO package and PAW pseudopotentials from standard libraries.

## Reproduction target
Run all DFT calculations and report the following in a JSON file `results.json`:

- Single vacancies: total magnetic moment (in μB) for V_Bi and V_S in Bi2S3(001), and V_Zn and V_S in ZnS(001).
- Single interstitials: total magnetic moment for Bi_i in Bi2S3(001) and Zn_i in ZnS(001).
- Two-cation-vacancy pairs: for three distinct Bi-vacancy configurations in Bi2S3 (Bi1–Bi2, Bi1–Bi3, Bi2–Bi3) and three Zn-vacancy configurations in ZnS (Zn1–Zn2, Zn1–Zn3, Zn1–Zn4), report both the total magnetic moment and a boolean indicating whether the ferromagnetic state has lower energy than the antiferromagnetic state.

The JSON must conform exactly to the schema given in the output contract. All values must be derived from properly converged DFT calculations; no other source of numbers is acceptable.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotentials for Bi, Zn, S (PBE): http://pseudopotentials.quantum-espresso.org/
- Atomic Simulation Environment (ASE): https://gitlab.com/ase/ase
- Python 3: python3
- Crystal structure data for Bi2S3 and ZnS

## Workflow steps

### Step 1: Bulk supercell relaxation
- Role: process
- Action: Relax the 1×1×3 bulk Bi2S3 supercell and the 2×2×2 bulk ZnS supercell using spin-polarized DFT to obtain optimized lattice parameters and atomic positions.
- Evidence: `/app/outputs/bulk_relaxation.log`

### Step 2: Surface slab construction and relaxation
- Role: process
- Action: From the relaxed bulk supercells, cleave the (001) surfaces to create stoichiometric slabs (50 atoms for Bi2S3, 48 atoms for ZnS), add a 10 Å vacuum layer, and fully relax all atomic positions.
- Evidence: `/app/outputs/slab_relaxation.log`

### Step 3: Defect magnetic moment and coupling calculations
- Role: scored (load-bearing)
- Action: Using the relaxed surface slabs, create defect supercells for (a) single neutral vacancies: V_Bi (5%), V_S (3.33%) in Bi2S3, V_Zn (4.17%), V_S (4.17%) in ZnS; (b) three distinct two-cation-vacancy configurations for Bi2S3 (Bi1-Bi2, Bi1-Bi3, Bi2-Bi3) and for ZnS (Zn1-Zn2, Zn1-Zn3, Zn1-Zn4); (c) single interstitial atoms: Zn_i at the stable octahedral site in ZnS, Bi_i at the stable site in Bi2S3. For each defect model, perform spin-polarized DFT relaxation and compute total magnetic moment. For the two-vacancy configurations, also compute the total energy of both ferromagnetic (FM) and antiferromagnetic (AFM) spin arrangements and determine whether the FM state is lower in energy. Assemble all results into a single JSON file results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"single_vacancies":[{"system":"Bi2S3_V_Bi","mu_B":"float"},{"system":"Bi2S3_V_S","mu_B":"float"},{"system":"ZnS_V_Zn","mu_B":"float"},{"system":"ZnS_V_S","mu_B":"float"}],"two_vacancies":[{"system":"Bi2S3_V_Bi_Bi1_Bi2","mu_B":"float","FM_lower_than_AFM":"bool"},{"system":"Bi2S3_V_Bi_Bi1_Bi3","mu_B":"float","FM_lower_than_AFM":"bool"},{"system":"Bi2S3_V_Bi_Bi2_Bi3","mu_B":"float","FM_lower_than_AFM":"bool"},{"system":"ZnS_V_Zn_Zn1_Zn2","mu_B":"float","FM_lower_than_AFM":"bool"},{"system":"ZnS_V_Zn_Zn1_Zn3","mu_B":"float","FM_lower_than_AFM":"bool"},{"system":"ZnS_V_Zn_Zn1_Zn4","mu_B":"float","FM_lower_than_AFM":"bool"}],"single_interstitials":[{"system":"ZnS_Zn_i","mu_B":"float"},{"system":"Bi2S3_Bi_i","mu_B":"float"}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing computed magnetic moments (in μB) and FM/AFM coupling indicators for all defect configurations.
- schema:
  - `type`: object
  - `properties`:
    - `single_vacancies`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `system`:
            - `type`: string
          - `mu_B`:
            - `type`: number
            - `unit`: μB
        - `required`: `system`, `mu_B`
    - `two_vacancies`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `system`:
            - `type`: string
          - `mu_B`:
            - `type`: number
            - `unit`: μB
          - `FM_lower_than_AFM`:
            - `type`: boolean
        - `required`: `system`, `mu_B`, `FM_lower_than_AFM`
    - `single_interstitials`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `system`:
            - `type`: string
          - `mu_B`:
            - `type`: number
            - `unit`: μB
        - `required`: `system`, `mu_B`
  - `required`: `single_vacancies`, `two_vacancies`, `single_interstitials`

Notes: The hidden checker compares each mu_B value against the paper's reference values within a tolerance, and verifies that FM_lower_than_AFM is true for every two-vacancy configuration.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "single_vacancies": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "system": {
                  "type": "string"
                },
                "mu_B": {
                  "type": "number",
                  "unit": "μB"
                }
              },
              "required": [
                "system",
                "mu_B"
              ]
            }
          },
          "two_vacancies": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "system": {
                  "type": "string"
                },
                "mu_B": {
                  "type": "number",
                  "unit": "μB"
                },
                "FM_lower_than_AFM": {
                  "type": "boolean"
                }
              },
              "required": [
                "system",
                "mu_B",
                "FM_lower_than_AFM"
              ]
            }
          },
          "single_interstitials": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "system": {
                  "type": "string"
                },
                "mu_B": {
                  "type": "number",
                  "unit": "μB"
                }
              },
              "required": [
                "system",
                "mu_B"
              ]
            }
          }
        },
        "required": [
          "single_vacancies",
          "two_vacancies",
          "single_interstitials"
        ]
      },
      "description": "JSON file containing computed magnetic moments (in μB) and FM/AFM coupling indicators for all defect configurations."
    }
  ],
  "notes": "The hidden checker compares each mu_B value against the paper's reference values within a tolerance, and verifies that FM_lower_than_AFM is true for every two-vacancy configuration."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads `results.json`. Each reported magnetic moment is compared against a hidden reference, and each two-vacancy `FM_lower_than_AFM` is checked for correctness. The reward is the fraction of these checks that pass (all checks weighted equally). Simply copying numbers from another source will not pass, because the verifier expects values produced by the correct computational protocol.
