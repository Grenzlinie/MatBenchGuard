# NEB-based Lithium Ion Migration Barrier Computation

## Problem background
Solid-state lithium ion conductors are promising for safer, high-energy-density batteries. Understanding the microscopic mechanism of Li⁺ transport — whether it proceeds predominantly by vacancy diffusion or by interstitial migration — is essential for designing materials with high ionic conductivity. This task concerns the lithium selenidostannate Li₄[SnSe₄], a compound whose crystal structure features tetrahedral [SnSe₄]⁴⁻ anions and Li⁺ ions occupying both octahedral and tetrahedral sites. Density functional theory (DFT) calculations can predict the formation energies of Li⁺ Frenkel defects and the energy barriers for Li⁺ migration along various pathways, from which the macroscopic activation energy for each mechanism can be derived and the dominant conduction pathway can be identified.

## Approach
The computational approach consists of the following conceptual stages. (i) Build a 1×2×2 supercell of the orthorhombic (Pnma) crystal structure of Li₄[SnSe₄] using the published crystallographic data. (ii) Perform DFT geometry optimization of the pristine (defect‑free) supercell to obtain the reference total energy. (iii) Create supercells with a single Li⁺ Frenkel defect by moving a Li⁺ ion from its regular octahedral (type‑1) or tetrahedral site to an initially empty interstitial octahedral site (types 2, 3, 4) and relax each defective supercell, keeping the cell shape and volume fixed. The formation energy of each defect is obtained from the total energy difference with the pristine reference. (iv) Use the nudged elastic band (NEB) method at the DFT level to compute minimum‑energy paths and barriers for a series of Li⁺ migration processes: interstitial migration (via a type‑3 intermediate and direct type‑2→type‑2 hop), and vacancy migration (octahedral‑type‑1 hops along the *a* and *c* directions, tetrahedral‑site hops, octahedral↔tetrahedral hops, a one‑dimensional continuous pathway, and an inter‑channel crossing). (v) Combine the lowest Frenkel formation energy and the appropriate migration barrier to obtain the Arrhenius activation energy for each mechanism: E_A = E_B + ½ min(E_F). The dominant transport mechanism is the one that gives the lower activation energy.

## Reproduction target
Your goal is to produce, as the single scored artifact, a file `/app/outputs/results.json` containing the following computed quantities (all in eV):

- Frenkel formation energies for moving a Li⁺ ion from an octahedral type‑1 site to interstitial types 2, 3, and 4, and from a tetrahedral site to a type‑2 interstitial.
- NEB energy barriers for interstitial migration: lowest barrier via a type‑3 intermediate, and direct type‑2→type‑2 hop.
- NEB energy barriers for vacancy migration: octahedral type‑1 hops along the *a* and *c* axes; tetrahedral‑tetrahedral hop; octahedral‑tetrahedral minimum; continuous one‑dimensional barrier; inter‑channel barrier.
- Macroscopic activation energies for the vacancy and interstitial mechanisms computed as E_A = E_B + ½·min(E_F).
- A string `dominant_mechanism` that is either `"vacancy"` or `"interstitial"`, determined by which of the two activation energies is lower.

The exact JSON schema is specified in the output contract below.

## Assets

- Crystallographic Information File for Li4[SnSe4] (compound 1): 10.1021/cm400541n
- GPAW (Grid-based Projector-Augmented Wave method): https://wiki.fysik.dtu.dk/gpaw/
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Build supercell
- Role: process
- Action: Using the published crystal structure (CIF), construct a 1×2×2 supercell of Li4[SnSe4] (compound 1) for DFT calculations.
- Evidence: none

### Step 2: Relax pristine supercell
- Role: process
- Action: Perform DFT geometry optimization of the pristine (defect-free) supercell to obtain the reference relaxed structure and total energy.
- Evidence: none

### Step 3: Generate and relax Frenkel defect supercells
- Role: process
- Action: Create supercells with a single Li+ ion moved from a regular lattice site to an interstitial octahedral site (types 2, 3, and 4 from type-1, and tetrahedral-to-type-2) and relax them with DFT, keeping cell shape and volume fixed.
- Evidence: none

### Step 4: Run NEB migration barrier calculations
- Role: process
- Action: Perform nudged elastic band (NEB) calculations for all specified Li+ migration paths: interstitial (via type-3 intermediate and direct type-2↔type-2) and vacancy (octahedral type1 along a and c, tetrahedral minimum, octahedral↔tetrahedral, continuous 1D segment, inter-channel hop). Use DFT relaxed initial and final structures.
- Evidence: none

### Step 5: Compute activation energies and write results
- Role: scored (load-bearing)
- Action: From the DFT results, compute Frenkel formation energies (E_F), migration barriers (E_B), and macroscopic activation energies E_A = E_B + 0.5 * min(E_F). Identify the dominant transport mechanism (vacancy or interstitial). Write all computed quantities and the mechanism to results.json according to the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "frenkel_formation_energies": {
    "type1_to_type2": <float in eV>,
    "type1_to_type3": <float in eV>,
    "type1_to_type4": <float in eV>,
    "tetrahedral_minimum": <float in eV>
  },
  "interstitial_migration_barriers": {
    "minimum_path_type3_intermediate": <float in eV>,
    "direct_type2_to_type2": <float in eV>
  },
  "vacancy_migration_barriers": {
    "octahedral_type1_along_a": <float in eV>,
    "octahedral_type1_along_c": <float in eV>,
    "tetrahedral_minimum": <float in eV>,
    "octahedral_to_tetrahedral_minimum": <float in eV>,
    "continuous_1d_barrier": <float in eV>,
    "inter_channel_barrier": <float in eV>
  },
  "activation_energies": {
    "vacancy_EA": <float in eV>,
    "interstitial_EA": <float in eV>
  },
  "dominant_mechanism": "<vacancy | interstitial>"
}
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
- target_policy: threshold_or_better
- description: Computed DFT-derived energies and the dominant Li+ transport mechanism for Li4[SnSe4].
- schema:
  - `type`: object
  - `required`: `frenkel_formation_energies`, `interstitial_migration_barriers`, `vacancy_migration_barriers`, `activation_energies`, `dominant_mechanism`
  - `properties`:
    - `frenkel_formation_energies`:
      - `type`: object
      - `required`: `type1_to_type2`, `type1_to_type3`, `type1_to_type4`, `tetrahedral_minimum`
      - `properties`:
        - `type1_to_type2`:
          - `type`: number
          - `unit`: eV
        - `type1_to_type3`:
          - `type`: number
          - `unit`: eV
        - `type1_to_type4`:
          - `type`: number
          - `unit`: eV
        - `tetrahedral_minimum`:
          - `type`: number
          - `unit`: eV
    - `interstitial_migration_barriers`:
      - `type`: object
      - `required`: `minimum_path_type3_intermediate`, `direct_type2_to_type2`
      - `properties`:
        - `minimum_path_type3_intermediate`:
          - `type`: number
          - `unit`: eV
        - `direct_type2_to_type2`:
          - `type`: number
          - `unit`: eV
    - `vacancy_migration_barriers`:
      - `type`: object
      - `required`: `octahedral_type1_along_a`, `octahedral_type1_along_c`, `tetrahedral_minimum`, `octahedral_to_tetrahedral_minimum`, `continuous_1d_barrier`, `inter_channel_barrier`
      - `properties`:
        - `octahedral_type1_along_a`:
          - `type`: number
          - `unit`: eV
        - `octahedral_type1_along_c`:
          - `type`: number
          - `unit`: eV
        - `tetrahedral_minimum`:
          - `type`: number
          - `unit`: eV
        - `octahedral_to_tetrahedral_minimum`:
          - `type`: number
          - `unit`: eV
        - `continuous_1d_barrier`:
          - `type`: number
          - `unit`: eV
        - `inter_channel_barrier`:
          - `type`: number
          - `unit`: eV
    - `activation_energies`:
      - `type`: object
      - `required`: `vacancy_EA`, `interstitial_EA`
      - `properties`:
        - `vacancy_EA`:
          - `type`: number
          - `unit`: eV
        - `interstitial_EA`:
          - `type`: number
          - `unit`: eV
    - `dominant_mechanism`:
      - `type`: string
      - `enum`: `vacancy`, `interstitial`

Notes: The primary scored output is results.json. The dominant_mechanism must be determined from the computed activation energies (vacancy diffusion expected to have lower activation energy). All energies in eV.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "frenkel_formation_energies",
          "interstitial_migration_barriers",
          "vacancy_migration_barriers",
          "activation_energies",
          "dominant_mechanism"
        ],
        "properties": {
          "frenkel_formation_energies": {
            "type": "object",
            "required": [
              "type1_to_type2",
              "type1_to_type3",
              "type1_to_type4",
              "tetrahedral_minimum"
            ],
            "properties": {
              "type1_to_type2": {
                "type": "number",
                "unit": "eV"
              },
              "type1_to_type3": {
                "type": "number",
                "unit": "eV"
              },
              "type1_to_type4": {
                "type": "number",
                "unit": "eV"
              },
              "tetrahedral_minimum": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "interstitial_migration_barriers": {
            "type": "object",
            "required": [
              "minimum_path_type3_intermediate",
              "direct_type2_to_type2"
            ],
            "properties": {
              "minimum_path_type3_intermediate": {
                "type": "number",
                "unit": "eV"
              },
              "direct_type2_to_type2": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "vacancy_migration_barriers": {
            "type": "object",
            "required": [
              "octahedral_type1_along_a",
              "octahedral_type1_along_c",
              "tetrahedral_minimum",
              "octahedral_to_tetrahedral_minimum",
              "continuous_1d_barrier",
              "inter_channel_barrier"
            ],
            "properties": {
              "octahedral_type1_along_a": {
                "type": "number",
                "unit": "eV"
              },
              "octahedral_type1_along_c": {
                "type": "number",
                "unit": "eV"
              },
              "tetrahedral_minimum": {
                "type": "number",
                "unit": "eV"
              },
              "octahedral_to_tetrahedral_minimum": {
                "type": "number",
                "unit": "eV"
              },
              "continuous_1d_barrier": {
                "type": "number",
                "unit": "eV"
              },
              "inter_channel_barrier": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "activation_energies": {
            "type": "object",
            "required": [
              "vacancy_EA",
              "interstitial_EA"
            ],
            "properties": {
              "vacancy_EA": {
                "type": "number",
                "unit": "eV"
              },
              "interstitial_EA": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "dominant_mechanism": {
            "type": "string",
            "enum": [
              "vacancy",
              "interstitial"
            ]
          }
        }
      },
      "description": "Computed DFT-derived energies and the dominant Li+ transport mechanism for Li4[SnSe4]."
    }
  ],
  "notes": "The primary scored output is results.json. The dominant_mechanism must be determined from the computed activation energies (vacancy diffusion expected to have lower activation energy). All energies in eV."
}
```

## How you are scored
A hidden verifier (checker) automatically loads your `/app/outputs/results.json` and compares every reported energy against a hidden reference standard. Points are awarded based on how closely each computed value matches the reference, with separate tolerances for formation energies, migration barriers, and activation energies. The verifier also checks that the declared dominant mechanism is the one whose activation energy is indeed lower. The final score is a weighted combination of the individual energy comparisons and the correct identification of the dominant mechanism. You must compute these quantities by performing the DFT workflow described in the steps; simply hard‑coding numbers is not sufficient, because the hidden reference may differ slightly from any previously reported values.
