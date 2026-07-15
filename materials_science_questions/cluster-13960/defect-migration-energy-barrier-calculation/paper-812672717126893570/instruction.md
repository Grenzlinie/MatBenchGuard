# DFT Simulation of Electron-Proton Co-Doping for Tunable Metal-Oxide Hydrogenation

## Problem background
Hydrogen doping is a powerful technique to tune the electronic, optical, and magnetic properties of metal-oxide semiconductors. However, traditional hydrogenation methods require harsh conditions such as high pressure, high temperature, and expensive catalysts. This work investigates an alternative route that uses a low-work-function metal coupled with an acid to drive protons into the oxide lattice under ambient conditions. The key computational question is whether interfacial electron transfer from the metal to the oxide can lower the barrier for hydrogen migration, enabling tunable doping. To establish this mechanism, three quantities must be computed: (1) the amount of charge transferred from different metals (Al, Zn, Cu, Ag) to anatase TiO₂; (2) how the hydrogen migration barrier on the TiO₂ surface changes under neutral, electron‑rich, and hole‑rich conditions; and (3) the evolution of the electronic density of states near the Fermi level in tungsten oxide (WO₃) as its hydrogen content increases.

## Approach
The reproduction task follows a computational protocol based on density functional theory (DFT). Using the open‑source Quantum ESPRESSO code with SSSP pseudopotentials, you will perform three sets of calculations. First, construct slab models of anatase TiO₂(101) and interface them with monolayers of Al, Zn, Cu, and Ag; compute Bader charges to extract the net electron transfer from each metal to the oxide. Second, prepare a TiO₂(101) slab with a hydrogen atom at a surface binding site and apply the climbing‑image nudged elastic band (CI‑NEB) method to obtain the minimum‑energy migration path from the surface to the subsurface; repeat the calculation under three total‑charge conditions: neutral (0), with one extra electron, and with one extra hole. Third, build a 2 × 2 × 1 supercell of WO₃ (W₈O₂₄) and introduce one to four interstitial hydrogen atoms; compute the projected density of states (PDOS) for each hydrogen concentration and integrate the occupied states from the Fermi level down to −1 eV. All crystal structures are available from the Materials Project, and the SSSP library provides the required pseudopotentials. The Bader analysis code is used for charge partitioning.

## Reproduction target
Produce three output files: (1) charge_transfer.json containing the electron transfer per metal atom (Al, Zn, Cu, Ag) in units of elementary charge e; (2) barriers.json with the hydrogen migration barrier and reaction energy (both in eV) for the neutral, electron‑doped, and hole‑doped charge states on anatase TiO₂(101) at site 1; (3) pdos_integrated.csv with two columns x (number of H atoms) and integrated_area (in arbitrary units), reporting the integrated occupied PDOS for HₓW₈O₂₄ (x = 1–4). All data must be obtained by running the described DFT calculations with Quantum ESPRESSO and the associated analysis tools. The precise numerical values will be evaluated by a hidden verifier.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Bader charge analysis code: https://theory.cm.utexas.edu/henkelman/code/bader/
- SSSP pseudopotential library: https://www.quantum-espresso.org/pseudopotentials
- Materials Project crystal structures: https://materialsproject.org/

## Workflow steps

### Step 1: Build anatase TiO₂(101) interface models
- Role: process
- Action: Construct the anatase TiO₂(101) surface slab model and interface models with Al, Zn, Cu, Ag monolayers using publicly available crystal structures from the Materials Project. Prepare input files for DFT SCF calculations.
- Evidence: none

### Step 2: Build TiO₂ surface slab with H at site 1
- Role: process
- Action: Construct the anatase TiO₂(101) surface slab model with a hydrogen atom adsorbed at surface binding site 1. Set up initial and final images for the NEB path from surface to subsurface. Prepare input files for neutral (total charge 0), electron‑doped (−1e), and hole‑doped (+1h) charge‑state calculations.
- Evidence: none

### Step 3: Build H‑doped WO₃ supercell models
- Role: process
- Action: Construct a 2×2×1 supercell of WO₃ (W₈O₂₄) from the public crystal structure. Generate structures with 1, 2, 3, and 4 interstitial hydrogen atoms (HₓW₈O₂₄, x = 1–4) and prepare input files for DFT projected density of states (PDOS) calculations.
- Evidence: none

### Step 4: Bader charge transfer for metal/TiO₂ interfaces
- Role: scored (load-bearing)
- Action: Perform DFT self‑consistent field calculations on the four metal/TiO₂ interface models using Quantum ESPRESSO. Compute Bader charges and extract the total electron transfer (in e) from each metal monolayer to the TiO₂ slab. Report the results as a JSON object with keys Al, Zn, Cu, Ag.
- Output file: `/app/outputs/charge_transfer.json`
- Format: json
- Contract: {"Al": <float e>, "Zn": <float e>, "Cu": <float e>, "Ag": <float e>}
- Scoring: scored by hidden verifier

### Step 5: H migration barrier on anatase TiO₂(101) site 1
- Role: scored
- Action: Using the climbing‑image nudged elastic band (CI‑NEB) method in Quantum ESPRESSO, compute the minimum‑energy path for H atom migration from surface to subsurface on anatase TiO₂(101) at site 1. Perform calculations under neutral (total charge 0), electron‑doped (−1 e), and hole‑doped (+1 h) conditions. Extract the energy barrier (ΔEb) and reaction energy (ΔE) in eV for each condition.
- Output file: `/app/outputs/barriers.json`
- Format: json
- Contract: {"neutral": {"barrier_eV": <float>, "reaction_energy_eV": <float>}, "electron": {"barrier_eV": <float>, "reaction_energy_eV": <float>}, "hole": {"barrier_eV": <float>, "reaction_energy_eV": <float>}}
- Scoring: scored by hidden verifier

### Step 6: PDOS integrated area for H‑doped WO₃
- Role: scored (load-bearing)
- Action: For each H‑doped WO₃ model (x = 1, 2, 3, 4), perform a DFT calculation with Quantum ESPRESSO to obtain the projected density of states (PDOS). For each case, integrate the occupied PDOS from the Fermi level down to −1 eV. Output the integrated area (a.u.) as a CSV table with columns x and integrated_area.
- Output file: `/app/outputs/pdos_integrated.csv`
- Format: csv
- Contract: x,integrated_area
1,<float>
2,<float>
3,<float>
4,<float>
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/charge_transfer.json`
- `/app/outputs/barriers.json`
- `/app/outputs/pdos_integrated.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### charge_transfer.json
- path: `/app/outputs/charge_transfer.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bader charge transfer (e) for four metal/TiO₂ interfaces.
- schema:
  - `type`: object
  - `properties`:
    - `Al`:
      - `type`: number
      - `description`: electron transfer per Al atom (e)
    - `Zn`:
      - `type`: number
      - `description`: electron transfer per Zn atom (e)
    - `Cu`:
      - `type`: number
      - `description`: electron transfer per Cu atom (e)
    - `Ag`:
      - `type`: number
      - `description`: electron transfer per Ag atom (e)
  - `required`: `Al`, `Zn`, `Cu`, `Ag`

### barriers.json
- path: `/app/outputs/barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: H migration barrier and reaction energy for anatase TiO₂(101) site 1.
- schema:
  - `type`: object
  - `properties`:
    - `neutral`:
      - `type`: object
      - `properties`:
        - `barrier_eV`:
          - `type`: number
          - `description`: energy barrier (eV)
        - `reaction_energy_eV`:
          - `type`: number
          - `description`: reaction energy (eV)
      - `required`: `barrier_eV`, `reaction_energy_eV`
    - `electron`:
      - `type`: object
      - `properties`:
        - `barrier_eV`:
          - `type`: number
        - `reaction_energy_eV`:
          - `type`: number
      - `required`: `barrier_eV`, `reaction_energy_eV`
    - `hole`:
      - `type`: object
      - `properties`:
        - `barrier_eV`:
          - `type`: number
        - `reaction_energy_eV`:
          - `type`: number
      - `required`: `barrier_eV`, `reaction_energy_eV`
  - `required`: `neutral`, `electron`, `hole`

### pdos_integrated.csv
- path: `/app/outputs/pdos_integrated.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Integrated PDOS area for HₓW₈O₂₄ (x=1–4).
- schema:
  - `type`: table
  - `columns`: `x`, `integrated_area`
  - `description`: x is integer H count, integrated_area is float in a.u.

Notes: The three scored artifacts reproduce the core computational evidence for the electron‑proton co‑doping mechanism: charge transfer from metals, H migration barrier modification, and tunable carrier concentration. Tolerances (not disclosed) account for DFT code and pseudopotential variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "charge_transfer.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "Al": {
            "type": "number",
            "description": "electron transfer per Al atom (e)"
          },
          "Zn": {
            "type": "number",
            "description": "electron transfer per Zn atom (e)"
          },
          "Cu": {
            "type": "number",
            "description": "electron transfer per Cu atom (e)"
          },
          "Ag": {
            "type": "number",
            "description": "electron transfer per Ag atom (e)"
          }
        },
        "required": [
          "Al",
          "Zn",
          "Cu",
          "Ag"
        ]
      },
      "description": "Bader charge transfer (e) for four metal/TiO₂ interfaces."
    },
    {
      "file": "barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "neutral": {
            "type": "object",
            "properties": {
              "barrier_eV": {
                "type": "number",
                "description": "energy barrier (eV)"
              },
              "reaction_energy_eV": {
                "type": "number",
                "description": "reaction energy (eV)"
              }
            },
            "required": [
              "barrier_eV",
              "reaction_energy_eV"
            ]
          },
          "electron": {
            "type": "object",
            "properties": {
              "barrier_eV": {
                "type": "number"
              },
              "reaction_energy_eV": {
                "type": "number"
              }
            },
            "required": [
              "barrier_eV",
              "reaction_energy_eV"
            ]
          },
          "hole": {
            "type": "object",
            "properties": {
              "barrier_eV": {
                "type": "number"
              },
              "reaction_energy_eV": {
                "type": "number"
              }
            },
            "required": [
              "barrier_eV",
              "reaction_energy_eV"
            ]
          }
        },
        "required": [
          "neutral",
          "electron",
          "hole"
        ]
      },
      "description": "H migration barrier and reaction energy for anatase TiO₂(101) site 1."
    },
    {
      "file": "pdos_integrated.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "columns": [
          "x",
          "integrated_area"
        ],
        "description": "x is integer H count, integrated_area is float in a.u."
      },
      "description": "Integrated PDOS area for HₓW₈O₂₄ (x=1–4)."
    }
  ],
  "notes": "The three scored artifacts reproduce the core computational evidence for the electron‑proton co‑doping mechanism: charge transfer from metals, H migration barrier modification, and tunable carrier concentration. Tolerances (not disclosed) account for DFT code and pseudopotential variations."
}
```

## How you are scored
A hidden checker evaluates each of the three output artifacts against reference values that represent a correct DFT reproduction of the target quantities. The checker compares your reported electron transfers, barrier energies, reaction energies, and integrated PDOS areas to expected ranges derived from the original study. The per‑artifact scores are combined into a single overall reward. Reporting numbers from the literature without executing the computational workflow will not pass; the verification assumes that the values result from correctly building the models, running the DFT calculations, and extracting the requested quantities as described in the workflow steps.
