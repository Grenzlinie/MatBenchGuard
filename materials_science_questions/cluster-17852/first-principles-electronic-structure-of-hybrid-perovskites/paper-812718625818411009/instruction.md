# Band Alignment of Hybrid Perovskite/Titania Interfaces from DFT

## Problem background
Hybrid organic-inorganic halide perovskites, such as methylammonium lead iodide (MAPbI3), are promising light-absorbing materials for photovoltaic devices. The power conversion efficiency of solar cells employing these perovskites is strongly influenced by the band alignment at the interface between the perovskite layer and the electron transport material (e.g., titanium dioxide, TiO2). In this theoretical investigation, we study MAPbI3 interfaces with rutile TiO2, considering different terminations of the perovskite slab: PbI-terminated, MAI-terminated, and a variant where the methylammonium (MA) cation at the TiO2 surface is deprotonated. The central question is how the interface composition affects the built-in electrostatic potential, the band gap, and the driving force for electron injection from the perovskite into TiO2, thereby determining the most favorable configuration for efficient charge transfer.

## Approach
We employ density functional theory (DFT) calculations within the generalized gradient approximation (PBE functional). The workflow proceeds as follows: (i) Construct isolated perovskite slabs with MAI and PbI terminations and optimize their geometries. (ii) Form three interface models by placing each optimized slab on a rutile TiO2 (001) surface: PbI/titania, MAI/titania, and deprotonated MAI/titania. (iii) Optimize the interface structures, exploring several lateral displacements to locate the most stable configuration. (iv) For each optimized interface, perform electronic structure calculations to obtain the planar-averaged electrostatic potential along the direction normal to the interface, the total and atom-projected density of states (DOS), and the band structure with fat-band projections onto iodine and lead atoms. From these data, we derive three quantities: (a) the built-in potential ΔV = V(∞)−V(−∞), where V(±∞) are the asymptotic vacuum potentials on either side; (b) the Kohn-Sham band gap of the interface system; and (c) the energy separation between the lower edge of the Pb-projected conduction bands and the TiO2 conduction band edge, which serves as a descriptor for the electron-injection driving force. The three interfaces are compared based on these quantities.

## Reproduction target
Your task is to compute the following for the three interface models (PbI/titania, MAI/titania, deprotonated MAI/titania):

1. Built-in potentials (in eV) — save as an array of objects in `builtin_potentials.json`.
2. Kohn-Sham band gaps (in eV) — save as an array of objects in `interface_band_gaps.json`.
3. Ranking of the interfaces by driving force for electron injection, ordered from most favorable (smallest Pb–TiO2 conduction edge separation) to least favorable — save as an object with a `ranking` array in `driving_force_ranking.json`.

All artifacts must be placed under `/app/outputs` and adhere to the output contract specified in this instruction.

## Assets

- SIESTA: https://departments.icmab.es/leem/siesta/
- Quantum-ESPRESSO: https://www.quantum-espresso.org/
- Troullier–Martins norm-conserving pseudopotentials: https://departments.icmab.es/leem/siesta/Databases/Pseudopotentials/
- Ultrasoft pseudopotentials for Quantum-ESPRESSO: https://www.materialscloud.org/discover/sssp/
- Crystal structure of MAPbI3 (tetragonal I4/mcm)
- Crystal structure of rutile TiO2 (P4_2/mnm)

## Workflow steps

### Step 1: Build and optimize isolated perovskite slabs
- Role: process
- Action: Build the MAI-terminated and PbI-terminated MAPbI3 slab models from the bulk tetragonal I4/mcm structure, ensuring apolar orientation of MA cations to cancel net dipole; optimize atomic positions using SIESTA with the PBE functional and norm-conserving pseudopotentials, employing dipole correction as needed.
- Evidence: `/app/outputs/slab_geometries.log`

### Step 2: Build and optimize interface geometries
- Role: process
- Action: For each of PbI/titania, MAI/titania, and deprotonated MAI/titania interfaces: construct supercell by matching the optimized perovskite slabs with a rutile TiO2 (001) slab; perform several initial lateral displacements to find the most stable configuration; optimize atomic positions using SIESTA.
- Evidence: `/app/outputs/interface_geometries.log`

### Step 3: DFT electronic structure of interfaces
- Role: process
- Action: For each optimized interface, perform Quantum-ESPRESSO PBE calculation using ultrasoft pseudopotentials. Compute the planar-averaged electrostatic potential along z, total and atom-projected density of states, and band structure in fat-band representation with projections over iodine and lead.
- Evidence: `/app/outputs/raw_dft_outputs.tar.gz`

### Step 4: Extract built-in potentials
- Role: scored (load-bearing)
- Action: From the planar-averaged potential data for each interface, compute V(∞) and V(-∞) as the asymptotic average in the vacuum regions; calculate built-in potential ΔV = V(∞) - V(-∞). Output the values.
- Output file: `/app/outputs/builtin_potentials.json`
- Format: json
- Contract: Array of objects: [{"interface": "string (PbI/titania | MAI/titania | MAIdep/titania)", "builtin_potential_eV": float}]
- Scoring: scored by hidden verifier

### Step 5: Extract interface band gaps
- Role: scored (load-bearing)
- Action: From the band structure data, determine the Kohn-Sham band gap for each interface (energy difference between valence band maximum and conduction band minimum). Output the values.
- Output file: `/app/outputs/interface_band_gaps.json`
- Format: json
- Contract: Array of objects: [{"interface": "string", "band_gap_eV": float}]
- Scoring: scored by hidden verifier

### Step 6: Determine driving force ranking for electron injection
- Role: scored (load-bearing)
- Action: From the projected DOS and fat-band data, identify the bottom of the Pb-projected conduction bands and the conduction band edge of TiO2 for each interface. Compute the energy separation ΔE_drive. Rank the interfaces from most favorable (smallest ΔE_drive) to least favorable. Output the ranking.
- Output file: `/app/outputs/driving_force_ranking.json`
- Format: json
- Contract: Object: {"ranking": ["string", "string", "string"]} where the first element is the most favorable interface.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/builtin_potentials.json`
- `/app/outputs/interface_band_gaps.json`
- `/app/outputs/driving_force_ranking.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### builtin_potentials.json
- path: `/app/outputs/builtin_potentials.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Built-in potentials ΔV (eV) for PbI/titania, MAI/titania, and MAIdep/titania interfaces.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `interface`, `builtin_potential_eV`
    - `properties`:
      - `interface`:
        - `type`: string
        - `enum`: `PbI/titania`, `MAI/titania`, `MAIdep/titania`
      - `builtin_potential_eV`:
        - `type`: number
        - `units`: eV

### interface_band_gaps.json
- path: `/app/outputs/interface_band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Kohn-Sham band gaps (eV) for the three interface systems.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `interface`, `band_gap_eV`
    - `properties`:
      - `interface`:
        - `type`: string
        - `enum`: `PbI/titania`, `MAI/titania`, `MAIdep/titania`
      - `band_gap_eV`:
        - `type`: number
        - `units`: eV

### driving_force_ranking.json
- path: `/app/outputs/driving_force_ranking.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ranking of interfaces by driving force for electron injection (smallest ΔE_drive first).
- schema:
  - `type`: object
  - `required`: `ranking`
  - `properties`:
    - `ranking`:
      - `type`: array
      - `items`:
        - `type`: string
        - `enum`: `PbI/titania`, `MAI/titania`, `MAIdep/titania`
      - `minItems`: 3
      - `maxItems`: 3
      - `description`: Ordered from most favorable to least favorable for electron injection

Notes: All scored artifacts are derived from the DFT electronic structure calculations. The ranking must contain exactly three entries corresponding to PbI/titania, MAI/titania, and MAIdep/titania in the correct order.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "builtin_potentials.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "interface",
            "builtin_potential_eV"
          ],
          "properties": {
            "interface": {
              "type": "string",
              "enum": [
                "PbI/titania",
                "MAI/titania",
                "MAIdep/titania"
              ]
            },
            "builtin_potential_eV": {
              "type": "number",
              "units": "eV"
            }
          }
        }
      },
      "description": "Built-in potentials ΔV (eV) for PbI/titania, MAI/titania, and MAIdep/titania interfaces."
    },
    {
      "file": "interface_band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "interface",
            "band_gap_eV"
          ],
          "properties": {
            "interface": {
              "type": "string",
              "enum": [
                "PbI/titania",
                "MAI/titania",
                "MAIdep/titania"
              ]
            },
            "band_gap_eV": {
              "type": "number",
              "units": "eV"
            }
          }
        }
      },
      "description": "Kohn-Sham band gaps (eV) for the three interface systems."
    },
    {
      "file": "driving_force_ranking.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "ranking"
        ],
        "properties": {
          "ranking": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "PbI/titania",
                "MAI/titania",
                "MAIdep/titania"
              ]
            },
            "minItems": 3,
            "maxItems": 3,
            "description": "Ordered from most favorable to least favorable for electron injection"
          }
        }
      },
      "description": "Ranking of interfaces by driving force for electron injection (smallest ΔE_drive first)."
    }
  ],
  "notes": "All scored artifacts are derived from the DFT electronic structure calculations. The ranking must contain exactly three entries corresponding to PbI/titania, MAI/titania, and MAIdep/titania in the correct order."
}
```

## How you are scored
A hidden verifier will evaluate your submitted artifacts by comparing your computed built-in potentials, band gaps, and driving-force ranking against reference values obtained from the original study. The verifier uses appropriate tolerances for numerical quantities and checks the relative ordering of the ranking. Each scored artifact contributes to the final reward according to a weighted scheme; the detailed scoring rules and tolerances are not disclosed. Simply reporting numbers without executing the computational pipeline will not yield a passing score. The verifier runs in a separate environment and does not require internet access.
