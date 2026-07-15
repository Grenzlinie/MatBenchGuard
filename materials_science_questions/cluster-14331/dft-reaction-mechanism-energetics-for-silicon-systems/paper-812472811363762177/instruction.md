# DFT Energetics of C–Si Cleavage and Isomerism in Hypercoordinated Phenyl Silicates

## Problem background
Phenyl bis‑catecholato silicates are promising precursors for generating aryl radicals under photoredox conditions, but their reactivity is much lower than that of their alkyl analogues. Understanding how substituents on the catechol ligands influence the ease of Si–C bond cleavage after photooxidation is crucial for designing efficient aryl radical precursors. This task reproduces the computational component of a study that used density functional theory (DFT) to quantify the barriers and reaction free energies for phenyl‑radical expulsion from a series of oxidized silicates, and to characterize an unusual electronic‑structure phenomenon known as SOMO–HOMO inversion in the resulting radical intermediates.

## Approach
The reproduction is based on DFT calculations at the ωB97M‑D3BJ/def2‑SV(P) level of theory, with an explicit DMF solvent molecule where needed to model solvent coordination to silicon. Molecular structures of all silicate anions, oxidized radical intermediates, product spirosilanes, and cis/trans isomers of key phenyl silicates are built from the chemical diagrams and descriptions provided in the paper. The workflow first optimizes geometries of all minima and locates transition states for homolytic Si–C bond cleavage in seven oxidized silicates: a primary alkyl case and six species carrying different substituents on the catechol and/or the migrating carbon (cyclohexyl, cyano‑, methoxy‑, phenyl, cyano‑phenyl, methoxy‑phenyl). Barriers and reaction free energies are extracted from these stationary points. Additionally, the cis/trans energy gap is computed for two phenyl silicates, and frontier orbital analyses (HOMO and SOMO energies) are performed on two radical cage intermediates to check for SOMO–HOMO inversion.

## Reproduction target
Compute and report:

1. **Si–C cleavage energetics:** for the seven oxidized silicates (primary_alkyl, I·Cy, I·Cy·CN, I·Cy·OMe, I·Ph, I·Ph·CN, I·Ph·OMe), locate the transition state for homolytic Si–C bond cleavage, then compute the free‑energy barrier ΔG‡ and the reaction free energy ΔG (in kcal mol⁻¹) both with and without an explicit DMF molecule (where the original study reports both). Write the results to `table5_barriers.csv` (columns: silicate, barrier_with_DMF, barrier_without_DMF, reaction_free_energy_with_DMF, reaction_free_energy_without_DMF).

2. **Cis/trans isomer gap:** for phenyl silicates 1b and 1h, compute the energy difference between the cis and trans isomers (kcal mol⁻¹) and write the gap together with the absolute energies of each isomer to `cis_trans_gaps.json`.

3. **SOMO–HOMO inversion:** for radical intermediates II·Ph and II·Ph·CN, extract the HOMO and SOMO energies (eV) and write them to `somo_homo.json`. Confirm that the SOMO energy lies below the HOMO energy in each case.

All output files must follow the exact schema declared in the Output Contract section.

## Assets

- ORCA quantum chemistry package (version 5.x or later): https://www.faccts.de/orca/
- Molecular structures of silicates and radicals

## Workflow steps

### Step 1: Build initial 3D molecular models
- Role: process
- Action: Construct initial Cartesian coordinate files (.xyz) for all required silicate anions, oxidized radical intermediates, product spirosilanes, and cis/trans isomers of 1b and 1h, based on the chemical structures given in the paper. Ensure the silicon center adopts a square‑pyramidal geometry and include a DMF molecule coordinated to silicon where needed (as described for the radical‑expulsion TS).
- Evidence: `/app/outputs/initial_models.zip`

### Step 2: DFT geometry optimizations of minima
- Role: process
- Action: Optimize geometries of all reactant, product, and intermediate minima at the ωB97M‑D3BJ/def2‑SV(P) level of theory, using an implicit solvent model for DMF if available, and explicitly include one DMF molecule for the structures involved in the Si–C cleavage step (oxidized silicates and radical‑cage complexes). Also optimize the cis and trans isomers of 1b and 1h.
- Evidence: `/app/outputs/optimized_geometries.zip`

### Step 3: Transition state search and barrier energies for Si–C cleavage
- Role: scored (load-bearing)
- Action: For the seven oxidized silicates (primary alkyl, I•Cy, I•Cy•CN, I•Cy•OMe, I•Ph, I•Ph•CN, I•Ph•OMe), locate the transition state for homolytic Si–C bond cleavage, compute the free‑energy barrier ΔG‡ and the reaction free energy ΔG (in kcal mol⁻¹). Perform the calculations with and without an explicit DMF molecule where the paper reports both. Write results to a CSV file.
- Output file: `/app/outputs/table5_barriers.csv`
- Format: csv
- Contract: CSV with columns: silicate (string), barrier_with_DMF (float, kcal/mol), barrier_without_DMF (float or empty), reaction_free_energy_with_DMF (float, kcal/mol), reaction_free_energy_without_DMF (float or empty). Rows correspond to: primary_alkyl, I·Cy, I·Cy·CN, I·Cy·OMe, I·Ph, I·Ph·CN, I·Ph·OMe.
- Scoring: scored by hidden verifier

### Step 4: Cis/trans isomer energy gaps for 1b and 1h
- Role: scored
- Action: From the optimized geometries of the cis and trans isomers of phenyl silicates 1b and 1h, compute the relative electronic energy (or free energy) difference and report the gap in kcal mol⁻¹. Write the results to a JSON file.
- Output file: `/app/outputs/cis_trans_gaps.json`
- Format: json
- Contract: JSON object with keys '1b' and '1h'. Each value is an object with fields: 'gap' (float, kcal/mol, positive when cis is more stable), 'cis_energy' (float, kcal/mol), 'trans_energy' (float, kcal/mol).
- Scoring: scored by hidden verifier

### Step 5: SOMO‑HOMO inversion characterisation
- Role: scored
- Action: Perform population analysis (spin density, molecular orbitals) on the optimized geometries of radical intermediates II•Ph and II•Ph•CN. Extract the energies (in eV) of the highest occupied molecular orbital (HOMO) and the singly occupied molecular orbital (SOMO). Verify that the SOMO energy is lower than the HOMO energy in both species. Write the energies to a JSON file.
- Output file: `/app/outputs/somo_homo.json`
- Format: json
- Contract: JSON object with keys 'II_Ph' and 'II_Ph_CN'. Each value is an object with fields: 'HOMO_energy' (float, eV), 'SOMO_energy' (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table5_barriers.csv`
- `/app/outputs/cis_trans_gaps.json`
- `/app/outputs/somo_homo.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table5_barriers.csv
- path: `/app/outputs/table5_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed free-energy barriers and reaction free energies for Si–C bond homolysis in seven oxidized silicates, with and without explicit DMF.
- schema:
  - `type`: table
  - `required_columns`: `silicate`, `barrier_with_DMF`, `barrier_without_DMF`, `reaction_free_energy_with_DMF`, `reaction_free_energy_without_DMF`
  - `units`:
    - `barrier_with_DMF`: kcal/mol
    - `barrier_without_DMF`: kcal/mol
    - `reaction_free_energy_with_DMF`: kcal/mol
    - `reaction_free_energy_without_DMF`: kcal/mol

### cis_trans_gaps.json
- path: `/app/outputs/cis_trans_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relative energies (gap) between cis and trans isomers of phenyl silicates 1b and 1h, along with absolute energies of each isomer.
- schema:
  - `type`: object
  - `required`: `1b`, `1h`
  - `properties`:
    - `1b`:
      - `type`: object
      - `required`: `gap`, `cis_energy`, `trans_energy`
      - `properties`:
        - `gap`:
          - `type`: number
          - `unit`: kcal/mol
        - `cis_energy`:
          - `type`: number
          - `unit`: kcal/mol
        - `trans_energy`:
          - `type`: number
          - `unit`: kcal/mol
    - `1h`:
      - `type`: object
      - `required`: `gap`, `cis_energy`, `trans_energy`
      - `properties`:
        - `gap`:
          - `type`: number
          - `unit`: kcal/mol
        - `cis_energy`:
          - `type`: number
          - `unit`: kcal/mol
        - `trans_energy`:
          - `type`: number
          - `unit`: kcal/mol

### somo_homo.json
- path: `/app/outputs/somo_homo.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: HOMO and SOMO energies for radical intermediates II·Ph and II·Ph·CN, used to confirm the SOMO–HOMO inversion (SOMO energy lower than HOMO).
- schema:
  - `type`: object
  - `required`: `II_Ph`, `II_Ph_CN`
  - `properties`:
    - `II_Ph`:
      - `type`: object
      - `required`: `HOMO_energy`, `SOMO_energy`
      - `properties`:
        - `HOMO_energy`:
          - `type`: number
          - `unit`: eV
        - `SOMO_energy`:
          - `type`: number
          - `unit`: eV
    - `II_Ph_CN`:
      - `type`: object
      - `required`: `HOMO_energy`, `SOMO_energy`
      - `properties`:
        - `HOMO_energy`:
          - `type`: number
          - `unit`: eV
        - `SOMO_energy`:
          - `type`: number
          - `unit`: eV

Notes: All energies are reported in the units specified. For barriers and isomer gaps the checker compares to paper-reported reference values within hidden tolerances. For frontier orbitals the checker verifies that SOMO_energy < HOMO_energy and that energies match the paper's values within a hidden eV tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table5_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "silicate",
          "barrier_with_DMF",
          "barrier_without_DMF",
          "reaction_free_energy_with_DMF",
          "reaction_free_energy_without_DMF"
        ],
        "units": {
          "barrier_with_DMF": "kcal/mol",
          "barrier_without_DMF": "kcal/mol",
          "reaction_free_energy_with_DMF": "kcal/mol",
          "reaction_free_energy_without_DMF": "kcal/mol"
        }
      },
      "description": "Computed free-energy barriers and reaction free energies for Si–C bond homolysis in seven oxidized silicates, with and without explicit DMF."
    },
    {
      "file": "cis_trans_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "1b",
          "1h"
        ],
        "properties": {
          "1b": {
            "type": "object",
            "required": [
              "gap",
              "cis_energy",
              "trans_energy"
            ],
            "properties": {
              "gap": {
                "type": "number",
                "unit": "kcal/mol"
              },
              "cis_energy": {
                "type": "number",
                "unit": "kcal/mol"
              },
              "trans_energy": {
                "type": "number",
                "unit": "kcal/mol"
              }
            }
          },
          "1h": {
            "type": "object",
            "required": [
              "gap",
              "cis_energy",
              "trans_energy"
            ],
            "properties": {
              "gap": {
                "type": "number",
                "unit": "kcal/mol"
              },
              "cis_energy": {
                "type": "number",
                "unit": "kcal/mol"
              },
              "trans_energy": {
                "type": "number",
                "unit": "kcal/mol"
              }
            }
          }
        }
      },
      "description": "Relative energies (gap) between cis and trans isomers of phenyl silicates 1b and 1h, along with absolute energies of each isomer."
    },
    {
      "file": "somo_homo.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "II_Ph",
          "II_Ph_CN"
        ],
        "properties": {
          "II_Ph": {
            "type": "object",
            "required": [
              "HOMO_energy",
              "SOMO_energy"
            ],
            "properties": {
              "HOMO_energy": {
                "type": "number",
                "unit": "eV"
              },
              "SOMO_energy": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "II_Ph_CN": {
            "type": "object",
            "required": [
              "HOMO_energy",
              "SOMO_energy"
            ],
            "properties": {
              "HOMO_energy": {
                "type": "number",
                "unit": "eV"
              },
              "SOMO_energy": {
                "type": "number",
                "unit": "eV"
              }
            }
          }
        }
      },
      "description": "HOMO and SOMO energies for radical intermediates II·Ph and II·Ph·CN, used to confirm the SOMO–HOMO inversion (SOMO energy lower than HOMO)."
    }
  ],
  "notes": "All energies are reported in the units specified. For barriers and isomer gaps the checker compares to paper-reported reference values within hidden tolerances. For frontier orbitals the checker verifies that SOMO_energy < HOMO_energy and that energies match the paper's values within a hidden eV tolerance."
}
```

## How you are scored
A hidden verifier will independently score each of the three workflow stages by comparing your submitted artifacts against reference values and structural criteria. For `table5_barriers.csv`, it will evaluate whether your computed barriers and free energies are close to the expected values within a hidden tolerance and whether the relative ordering of barriers across the different silicates (e.g., relative to the unsubstituted phenyl case) is correct. For `cis_trans_gaps.json`, it will compare your reported gaps and isomer energies against reference numbers. For `somo_homo.json`, it will check that the SOMO energy is lower than the HOMO energy for both radicals and that the orbital energies fall within an acceptable range. Each stage contributes a weighted fraction to the final reward; reporting numbers that match the paper is not sufficient — the verifier checks that the values were produced by the required workflow.
