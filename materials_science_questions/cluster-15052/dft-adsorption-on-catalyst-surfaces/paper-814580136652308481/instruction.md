# DFT Adsorption and Reduction of CO2 on CeO2 Surfaces

## Problem background
Converting CO₂ into fuels and valuable chemicals is a promising route to mitigate greenhouse gas emissions, and ceria (CeO₂) is an important catalyst for CO₂ hydrogenation. The initial reduction step—whether CO₂ dissociates directly to CO+O, or is hydrogenated to formate (HCOO) or carboxyl (COOH)—determines the product distribution, but the relative favorability of these pathways on perfect versus oxygen-defective CeO₂(111) surfaces is not fully understood. This task reproduces a first-principles investigation that uses density functional theory to compare CO₂ adsorption, reductive dissociation, and hydrogenation on both perfect and O-defective CeO₂(111), with the goal of determining which adsorption configurations are most stable and which initial reduction channel dominates on each surface.

## Approach
Density functional theory with a Hubbard U correction (DFT+U) is used to model the strongly correlated Ce 4f electrons. A bulk CeO₂ cell is optimized to obtain the equilibrium lattice constant, from which a p(2×2) nine-layer CeO₂(111) slab is constructed. The perfect slab is relaxed, and an oxygen vacancy is introduced at a surface O site to create the O-defective surface. CO₂ is placed in several known adsorption geometries on each surface: monodentate, bidentate, and linear physisorbed on the perfect surface; and three configurations on the defective surface involving the vacancy (O-atom filling, carbonate near vacancy, and C-atom occupying vacancy). For each adsorption complex, geometry optimization yields adsorption energies, C–O bond lengths, the O–C–O angle, and Bader charges. Transition states for key reaction steps are located via the climbing-image nudged elastic band (CI-NEB) method: direct dissociation of CO₂ starting from two adsorption modes on each surface, and hydrogenation of co-adsorbed CO₂+H to COOH and to HCOO, also from two starting configurations per surface. Reaction energies and energy barriers are extracted from the initial state, transition state, and final state energies.

## Reproduction target
Compute and report the following quantities in the designated output files:

- `bulk_surface.json`: the equilibrium bulk lattice constant (Å) of CeO₂, the surface energy (J/m²) of the perfect CeO₂(111) slab, and the oxygen vacancy formation energy (eV) on that surface.

- `adsorption_perfect.csv`: for CO₂ on the perfect CeO₂(111) surface, adsorption energies (eV), C–Oₐ and C–Oᵇ bond lengths (Å), O–C–O angle (degrees), and net Bader charge (|e|) on the CO₂ moiety for the configurations P-1 (monodentate carbonate), P-2 (bidentate carbonate), and P-3 (linear physisorbed).

- `adsorption_defective.csv`: analogous quantities for CO₂ on the O-defective CeO₂(111) surface for the configurations D-1 (O-atom inserted into the vacancy), D-2 (carbonate near the vacancy), and D-3 (C-atom occupying the vacancy).

- `reaction_pathways.json`: for each of the following pathways, the initial and final state labels, the reaction energy (eV, E_FS – E_IS), and the energy barrier (eV, E_TS – E_IS):
  * Perfect surface dissociation from P-1 and from P-2
  * Defective surface dissociation from D-1 and from D-3
  * Perfect surface hydrogenation to COOH from the co-adsorption configuration CH-1
  * Perfect surface hydrogenation to HCOO from CH-2
  * Defective surface hydrogenation to COOH from CW-1
  * Defective surface hydrogenation to HCOO from CW-2

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Prepare perfect and O-defective CeO2(111) surfaces
- Role: scored
- Action: Perform DFT+U calculations to: (a) optimize the bulk CeO2 cell and obtain the equilibrium lattice constant; (b) construct a p(2×2) 9-layer CeO2(111) slab, relax it, and compute the surface energy; (c) create an O-defective surface by removing one surface O atom, relax it, and compute the O vacancy formation energy. Extract the relevant quantities into the output file.
- Output file: `/app/outputs/bulk_surface.json`
- Format: json
- Contract: Object with keys: bulk_lattice_constant (float), surface_energy (float), vacancy_formation_energy (float). Example: {"bulk_lattice_constant": <float>, "surface_energy": <float>, "vacancy_formation_energy": <float>}
- Scoring: scored by hidden verifier

### Step 2: CO2 adsorption on perfect CeO2(111)
- Role: scored
- Action: Using the relaxed perfect surface, perform DFT+U geometry optimizations for CO2 in monodentate (P-1), bidentate (P-2), and linear physisorbed (P-3) configurations. Compute adsorption energies (E_ads = E(slab+CO2) - E(slab) - E(CO2_gas)), structural parameters (C–Oa, C–Ob bond lengths, O–C–O angle), and Bader charges on the adsorbed CO2. Collect the results into the output CSV.
- Output file: `/app/outputs/adsorption_perfect.csv`
- Format: csv
- Contract: CSV with columns: config (P-1/P-2/P-3), E_ads (eV), C_Oa (Ang), C_Ob (Ang), O_C_O_angle (deg), Bader_charge (|e|).
- Scoring: scored by hidden verifier

### Step 3: CO2 adsorption on O-defective CeO2(111)
- Role: scored
- Action: Using the relaxed O-defective surface, perform DFT+U geometry optimizations for CO2 in D-1 (O-atom inserted into vacancy), D-2 (carbonate near vacancy), and D-3 (C-atom occupying vacancy) configurations. Compute adsorption energies, structural parameters, and Bader charges as above; write the output CSV.
- Output file: `/app/outputs/adsorption_defective.csv`
- Format: csv
- Contract: CSV with columns: config (D-1/D-2/D-3), E_ads (eV), C_Oa (Ang), C_Ob (Ang), O_C_O_angle (deg), Bader_charge (|e|).
- Scoring: scored by hidden verifier

### Step 4: Reaction pathways: dissociation and hydrogenation
- Role: scored (load-bearing)
- Action: Perform climbing-image nudged elastic band (CI-NEB) transition state searches for the following pathways: (a) CO2 dissociation on perfect surface starting from P-1 and P-2; (b) CO2 dissociation on defective surface starting from D-1 and D-3; (c) CO2 hydrogenation to COOH on perfect surface via CH-1 configuration; (d) CO2 hydrogenation to HCOO on perfect surface via CH-2 configuration; (e) CO2 hydrogenation to COOH on defective surface via CW-1; (f) CO2 hydrogenation to HCOO on defective surface via CW-2. For each, compute the reaction energy (E_FS - E_IS) and the energy barrier (E_TS - E_IS). Record all results in the output JSON file. Include a pathway_label as specified in the schema.
- Output file: `/app/outputs/reaction_pathways.json`
- Format: json
- Contract: JSON list of objects with keys: pathway_label (string), initial_state (string), final_state (string), reaction_energy (float, eV), barrier (float, eV). Example entry: {"pathway_label":"perfect_dissoc_P1", "initial_state":"P-1", "final_state":"CO+O", "reaction_energy":<float>, "barrier":<float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_surface.json`
- `/app/outputs/adsorption_perfect.csv`
- `/app/outputs/adsorption_defective.csv`
- `/app/outputs/reaction_pathways.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_surface.json
- path: `/app/outputs/bulk_surface.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bulk lattice constant (Ang), surface energy (J/m^2), and O vacancy formation energy (eV) of the CeO2(111) system.
- schema:
  - `type`: object
  - `required`:
    - `bulk_lattice_constant`: float
    - `surface_energy`: float
    - `vacancy_formation_energy`: float

### adsorption_perfect.csv
- path: `/app/outputs/adsorption_perfect.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CO2 adsorption properties on the perfect CeO2(111) surface for configurations P-1, P-2, P-3.
- schema:
  - `type`: table
  - `required_columns`: `config`, `E_ads`, `C_Oa`, `C_Ob`, `O_C_O_angle`, `Bader_charge`
  - `units`:
    - `E_ads`: eV
    - `C_Oa`: Ang
    - `C_Ob`: Ang
    - `O_C_O_angle`: deg
    - `Bader_charge`: |e|

### adsorption_defective.csv
- path: `/app/outputs/adsorption_defective.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CO2 adsorption properties on the O-defective CeO2(111) surface for configurations D-1, D-2, D-3.
- schema:
  - `type`: table
  - `required_columns`: `config`, `E_ads`, `C_Oa`, `C_Ob`, `O_C_O_angle`, `Bader_charge`
  - `units`:
    - `E_ads`: eV
    - `C_Oa`: Ang
    - `C_Ob`: Ang
    - `O_C_O_angle`: deg
    - `Bader_charge`: |e|

### reaction_pathways.json
- path: `/app/outputs/reaction_pathways.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reaction energies and barriers for CO2 dissociation and hydrogenation pathways on perfect and defective surfaces.
- schema:
  - `type`: array
  - `items`:
    - `pathway_label`: string
    - `initial_state`: string
    - `final_state`: string
    - `reaction_energy`: float
    - `barrier`: float
  - `units`:
    - `reaction_energy`: eV
    - `barrier`: eV

Notes: All outputs are scored by comparing the agent's computed values to the paper's reported values with hidden tolerances. The reaction_pathways.json step is load-bearing to ensure the agent executes the full transition state search pipeline.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_surface.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk_lattice_constant": "float",
          "surface_energy": "float",
          "vacancy_formation_energy": "float"
        }
      },
      "description": "Bulk lattice constant (Ang), surface energy (J/m^2), and O vacancy formation energy (eV) of the CeO2(111) system."
    },
    {
      "file": "adsorption_perfect.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "config",
          "E_ads",
          "C_Oa",
          "C_Ob",
          "O_C_O_angle",
          "Bader_charge"
        ],
        "units": {
          "E_ads": "eV",
          "C_Oa": "Ang",
          "C_Ob": "Ang",
          "O_C_O_angle": "deg",
          "Bader_charge": "|e|"
        }
      },
      "description": "CO2 adsorption properties on the perfect CeO2(111) surface for configurations P-1, P-2, P-3."
    },
    {
      "file": "adsorption_defective.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "config",
          "E_ads",
          "C_Oa",
          "C_Ob",
          "O_C_O_angle",
          "Bader_charge"
        ],
        "units": {
          "E_ads": "eV",
          "C_Oa": "Ang",
          "C_Ob": "Ang",
          "O_C_O_angle": "deg",
          "Bader_charge": "|e|"
        }
      },
      "description": "CO2 adsorption properties on the O-defective CeO2(111) surface for configurations D-1, D-2, D-3."
    },
    {
      "file": "reaction_pathways.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "pathway_label": "string",
          "initial_state": "string",
          "final_state": "string",
          "reaction_energy": "float",
          "barrier": "float"
        },
        "units": {
          "reaction_energy": "eV",
          "barrier": "eV"
        }
      },
      "description": "Reaction energies and barriers for CO2 dissociation and hydrogenation pathways on perfect and defective surfaces."
    }
  ],
  "notes": "All outputs are scored by comparing the agent's computed values to the paper's reported values with hidden tolerances. The reaction_pathways.json step is load-bearing to ensure the agent executes the full transition state search pipeline."
}
```

## How you are scored
Each workflow step produces a scored artifact (bulk_surface.json, adsorption_perfect.csv, adsorption_defective.csv, reaction_pathways.json). A hidden verifier reads these files, extracts the numerical values according to the defined schemas, and compares them against reference targets. The comparison uses appropriate hidden tolerances for each type of quantity. The verifier computes a score for each artifact based on the fraction of values that fall within tolerance, weights the artifacts (with the reaction pathway step carrying the largest weight because it captures the core transition-state results), and returns a single overall reward between 0 and 1. The reference values and tolerances are not provided to you; to achieve a high score you must perform the DFT calculations as described, not fabricate or guess the numbers.
