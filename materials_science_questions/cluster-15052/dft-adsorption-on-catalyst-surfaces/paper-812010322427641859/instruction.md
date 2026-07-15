# DFT Study of Spin States and H2 Addition in Dinuclear Group IV Metallocene N2 Complexes

## Problem background
The catalytic hydrogenation of dinitrogen is a major goal in chemistry. Dinuclear group IV metallocene complexes with side-on-coordinated N₂, of the type [(η⁵-C₅Me_nH_{5-n})₂M]₂(μ₂,η²,η²-N₂), can add H₂ across the N≡N bond, but their reactivity depends critically on the electronic ground state. Understanding how the singlet–triplet energy gap varies with the metal (M = Ti, Zr, Hf) and the ligand substitution (n = 0 or 4) is essential for predicting which complexes are viable for N₂ hydrogenation. This computational task aims to map the relative energies of all stationary points—reactants, transition states, and products—on the lowest singlet and triplet potential energy surfaces for H₂ addition, and thereby identify the ground electronic state and the corresponding activation barriers for each complex.

## Approach
The energy landscape is explored using density functional theory (DFT). The primary method is the B3LYP hybrid functional combined with the CEP-31G basis set and Stevens–Basch–Krauss relativistic effective core potentials for the transition metals and main-group atoms, with a d-polarization function (α=0.80) added to all nitrogen atoms (denoted CEP-31G(d_N)). For each metal (Ti, Zr, Hf) and each ligand set (cyclopentadienyl, n = 0, or tetramethylcyclopentadienyl, n = 4), both the closed-shell singlet and the triplet electronic states of the dinuclear N₂-bridged reactant are considered, leading to distinct reaction channels. Geometry optimizations are performed without symmetry constraints, and harmonic vibrational frequency analyses provide zero-point energy corrections for the B3LYP results. Additionally, for the unsubstituted (n = 0) reactants only, the singlet–triplet gaps are recalculated with the pure GGA functional PBE using the same ECP/basis combination, allowing an assessment of functional dependence. All energies are referenced to the closed-shell singlet reactant of the same metal/ligand combination, and reported as relative energies in kcal/mol, both with and without zero-point corrections where available.

## Reproduction target
Compute the following quantities and assemble them into the required JSON output file:

• For every combination of metal (Ti, Zr, Hf) and ligand set (n = 0, 4), at the B3LYP/CEP-31G(d_N) level: the absolute electronic energy (Hartree) and, where available, the zero-point corrected relative energy (kcal/mol) of the singlet reactant, triplet reactant, singlet transition state, triplet transition state, singlet product, and triplet product for the H₂ addition reaction.
• For the n = 0 complexes only, at the PBE/CEP-31G(d_N) level: the absolute electronic energy (Hartree) and uncorrected relative energy (kcal/mol) of the singlet and triplet reactants.

All relative energies must be referenced to the closed-shell singlet reactant of the corresponding metal/ligand combination. The results must be organized into the `energies.json` file as specified in the output contract. The computed energies should reflect the specified computational protocol and be internally consistent, showing the relative ordering of spin states and the magnitude of activation barriers.

## Assets

- ORCA (or NWChem) – open-source quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Stevens/Basch/Krauss ECP and CEP-31G basis set with d-polarization on N (α=0.80): https://www.basissetexchange.org

## Workflow steps

### Step 1: Generate initial molecular geometries
- Role: process
- Action: Construct plausible 3D structures for all stationary points: reactants, transition states, and products for each combination (n=0,4; M=Ti, Zr, Hf; singlet and triplet spin states). Use chemical knowledge and the paper's description to produce initial XYZ files.
- Evidence: none

### Step 2: B3LYP/CEP-31G(d_N) optimizations and frequency calculations
- Role: process
- Action: For every species (all metals, n=0 and 4, singlet and triplet states: reactants, TS, products), perform B3LYP/CEP-31G(d_N) geometry optimization without symmetry constraints, followed by harmonic frequency analysis to confirm the nature of the stationary point and to extract zero-point energy corrections. Use SBK relativistic ECPs for transition metals and C,N, and a d-polarization function on N (α=0.80). Record absolute energies and ZPE corrections.
- Evidence: `/app/outputs/b3lyp_absolute_energies.json`

### Step 3: PBE/CEP-31G(d_N) calculations for n=0 reactants
- Role: process
- Action: For the n=0 reactants (M=Ti, Zr, Hf) in both singlet and triplet states, perform PBE/CEP-31G(d_N) geometry optimization (no symmetry) and obtain electronic energies. Use the same SBK ECPs and d-polarization on N. Record absolute energies.
- Evidence: `/app/outputs/pbe_absolute_energies.json`

### Step 4: Compile relative energies
- Role: scored (load-bearing)
- Action: Using the computed absolute energies (Hartree) and ZPE corrections from the B3LYP and PBE calculations, compute relative energies in kcal/mol. Reference all energies to the corresponding closed-shell singlet reactant of the same metal/ligand combination. For B3LYP entries, provide both uncorrected and ZPE-corrected relative energies. For PBE entries (n=0 only), provide the uncorrected relative energies (no ZPE required). Output the aggregated data as energies.json.
- Output file: `/app/outputs/energies.json`
- Format: json
- Contract: JSON object with top-level keys 'reactants', 'TS', 'products'. Each is an array of objects: { 'n': <0 or 4>, 'metal': 'Ti'|'Zr'|'Hf', 'spin_state': 'singlet'|'triplet', 'method': 'B3LYP'|'PBE', 'species': 'reactant'|'TS'|'product', 'absolute_energy_Hartree': number, 'relative_energy_kcal_mol': number, 'relative_energy_ZPE_corrected': number (or null if not available) }.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.json
- path: `/app/outputs/energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relative energies (kcal/mol) of all stationary points for the H2 addition reaction, computed with B3LYP and PBE functionals. The hidden checker compares these values to reference data from the paper.
- schema:
  - `type`: object
  - `required`: `reactants`, `TS`, `products`
  - `properties`:
    - `reactants`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `n`, `metal`, `spin_state`, `method`, `species`, `absolute_energy_Hartree`, `relative_energy_kcal_mol`
        - `properties`:
          - `n`:
            - `type`: integer
          - `metal`:
            - `type`: string
          - `spin_state`:
            - `type`: string
          - `method`:
            - `type`: string
          - `species`:
            - `type`: string
          - `absolute_energy_Hartree`:
            - `type`: number
          - `relative_energy_kcal_mol`:
            - `type`: number
          - `relative_energy_ZPE_corrected`:
            - `type`: number
            - `optional`: True
    - `TS`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `n`, `metal`, `spin_state`, `method`, `species`, `absolute_energy_Hartree`, `relative_energy_kcal_mol`
        - `properties`:
          - `n`:
            - `type`: integer
          - `metal`:
            - `type`: string
          - `spin_state`:
            - `type`: string
          - `method`:
            - `type`: string
          - `species`:
            - `type`: string
          - `absolute_energy_Hartree`:
            - `type`: number
          - `relative_energy_kcal_mol`:
            - `type`: number
          - `relative_energy_ZPE_corrected`:
            - `type`: number
            - `optional`: True
    - `products`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `n`, `metal`, `spin_state`, `method`, `species`, `absolute_energy_Hartree`, `relative_energy_kcal_mol`
        - `properties`:
          - `n`:
            - `type`: integer
          - `metal`:
            - `type`: string
          - `spin_state`:
            - `type`: string
          - `method`:
            - `type`: string
          - `species`:
            - `type`: string
          - `absolute_energy_Hartree`:
            - `type`: number
          - `relative_energy_kcal_mol`:
            - `type`: number
          - `relative_energy_ZPE_corrected`:
            - `type`: number
            - `optional`: True

Notes: Checker compares the reported relative energies and the implied singlet-triplet gaps and barrier trends to hidden reference values from Table 1 of the paper, using tolerances that accommodate method/implementation differences. The output contract requires fields for both uncorrected and ZPE-corrected energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "reactants",
          "TS",
          "products"
        ],
        "properties": {
          "reactants": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "n",
                "metal",
                "spin_state",
                "method",
                "species",
                "absolute_energy_Hartree",
                "relative_energy_kcal_mol"
              ],
              "properties": {
                "n": {
                  "type": "integer"
                },
                "metal": {
                  "type": "string"
                },
                "spin_state": {
                  "type": "string"
                },
                "method": {
                  "type": "string"
                },
                "species": {
                  "type": "string"
                },
                "absolute_energy_Hartree": {
                  "type": "number"
                },
                "relative_energy_kcal_mol": {
                  "type": "number"
                },
                "relative_energy_ZPE_corrected": {
                  "type": "number",
                  "optional": true
                }
              }
            }
          },
          "TS": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "n",
                "metal",
                "spin_state",
                "method",
                "species",
                "absolute_energy_Hartree",
                "relative_energy_kcal_mol"
              ],
              "properties": {
                "n": {
                  "type": "integer"
                },
                "metal": {
                  "type": "string"
                },
                "spin_state": {
                  "type": "string"
                },
                "method": {
                  "type": "string"
                },
                "species": {
                  "type": "string"
                },
                "absolute_energy_Hartree": {
                  "type": "number"
                },
                "relative_energy_kcal_mol": {
                  "type": "number"
                },
                "relative_energy_ZPE_corrected": {
                  "type": "number",
                  "optional": true
                }
              }
            }
          },
          "products": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "n",
                "metal",
                "spin_state",
                "method",
                "species",
                "absolute_energy_Hartree",
                "relative_energy_kcal_mol"
              ],
              "properties": {
                "n": {
                  "type": "integer"
                },
                "metal": {
                  "type": "string"
                },
                "spin_state": {
                  "type": "string"
                },
                "method": {
                  "type": "string"
                },
                "species": {
                  "type": "string"
                },
                "absolute_energy_Hartree": {
                  "type": "number"
                },
                "relative_energy_kcal_mol": {
                  "type": "number"
                },
                "relative_energy_ZPE_corrected": {
                  "type": "number",
                  "optional": true
                }
              }
            }
          }
        }
      },
      "description": "Relative energies (kcal/mol) of all stationary points for the H2 addition reaction, computed with B3LYP and PBE functionals. The hidden checker compares these values to reference data from the paper."
    }
  ],
  "notes": "Checker compares the reported relative energies and the implied singlet-triplet gaps and barrier trends to hidden reference values from Table 1 of the paper, using tolerances that accommodate method/implementation differences. The output contract requires fields for both uncorrected and ZPE-corrected energies."
}
```

## How you are scored
Your submission is assessed by an automated hidden verifier. The verifier reads `energies.json` and checks that it contains the required entries for all species. It then compares your reported relative energies and the derived quantities—such as the singlet–triplet energy gaps and the singlet-state activation barriers for each metal—against reference results obtained from the same protocol. The checker evaluates whether the data satisfy several chemical criteria, including the correct assignment of the ground electronic state for each complex, the relative ordering of reaction barriers across metals and spin states, and the consistency of the energies across the series. No single numerical match is decisive; instead, the reward is based on adherence to the expected qualitative trends and on the quantitative proximity of your computed values to the reference results within an appropriate tolerance that respects the variability of DFT implementations. The final score is a weighted combination of these checks, and simply reporting numbers that happen to be close without having performed the calculations will not satisfy all verification conditions.
