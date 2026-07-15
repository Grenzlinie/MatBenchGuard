# Reproduction of Binding Energies, Dipole Moments, and Water State Distributions in Zwitterionic Gel Electrolytes

## Problem background
Aqueous zinc-metal batteries are promising due to low cost and safety, but they suffer from side reactions and dendrite growth linked to the electrolyte. Zwitterionic polymer gel electrolytes have been proposed to mitigate these issues by preferentially immobilizing anions and water molecules near the electrode while allowing zinc ions to migrate freely. The strength of this preferential immobilization is hypothesized to depend on the molecular dipole moment of the zwitterionic monomers, offering a molecular-design principle for improved electrolytes. This task investigates that relationship by computing monomer–ion binding energies, monomer dipole moments, and the resulting water-state distributions in gel electrolytes.

## Approach
The computational investigation proceeds in two parts. First, density functional theory (DFT) calculations are used to optimize the geometries of three zwitterionic monomers (DMAPS, MPC, CBMA) starting from their SMILES strings. For each optimized monomer, the binding energy with sulfate (SO₄²⁻) near the quaternary ammonium group, with water near the quaternary ammonium group, with zinc (Zn²⁺) near the negatively charged group, and with water near the negatively charged group is computed. The molecular dipole moment is obtained from the electrostatic potential. Second, classical molecular dynamics (MD) simulations of a 2 M ZnSO₄ aqueous electrolyte containing each corresponding polymer (PDMAPS, PMPC, PCBMA) are performed. Simulation trajectories are analyzed to determine the percentages of water molecules that are free, coordinated to Zn²⁺, or fixed by the polymer. The goal is to link the calculated monomer dipole moments and binding preferences to the macroscopic water-state distributions in the gel electrolytes.

## Reproduction target
Produce two JSON artifacts:

1. `binding_and_dipole.json`: contains the DFT-computed binding energies (in eV) for the four specific interactions (SO₄²⁻ near N, H₂O near N, Zn²⁺ near negative group, H₂O near negative group) and the molecular dipole moments (in Debye) for DMAPS, MPC, and CBMA.

2. `water_states.json`: contains the MD-derived percentages of water in free, Zn²⁺-coordinated, and polymer-fixed states for the three gel electrolytes (PDMAPS, PMPC, PCBMA).

The task is to generate these files by executing the workflow described in the steps.

## Assets

- ORCA or equivalent DFT package: https://orcaforum.kofo.mpg.de
- LAMMPS or equivalent MD code: https://lammps.sandia.gov
- Monomers SMILES strings
- Force field parameters (OPLS-AA or GAFF): https://zarbi.chem.yale.edu/oplsaam.html

## Workflow steps

### Step 1: DFT calculations of monomer properties
- Role: process
- Action: Using a DFT code (e.g., ORCA or an open-source equivalent), optimize the geometries of the three zwitterionic monomers — DMAPS, MPC, CBMA — starting from the provided SMILES strings. Compute the binding energies of each monomer with (i) SO₄²⁻ near the quaternary ammonium group, (ii) H₂O near the quaternary ammonium group, (iii) Zn²⁺ near the negatively charged group (sulfonate/phosphoryl/carboxylate), and (iv) H₂O near the negatively charged group. Also compute the molecular dipole moment of each optimized monomer from the electrostatic potential.
- Evidence: `/app/outputs/dft_runtimes.log`

### Step 2: Write binding energies and dipole moments
- Role: scored (load-bearing)
- Action: Write a JSON file containing the computed binding energies (in eV) and molecular dipole moments (in Debye) for DMAPS, MPC, CBMA. The binding energies are for four specific interactions: SO₄²⁻ near quaternary ammonium, H₂O near quaternary ammonium, Zn²⁺ near negatively charged group, and H₂O near negatively charged group.
- Output file: `/app/outputs/binding_and_dipole.json`
- Format: json
- Contract: {"type":"object","required":["binding_energies","dipole_moments"],"properties":{"binding_energies":{"type":"object","required":["SO4_near_N","H2O_near_N","Zn_near_neg","H2O_near_neg"],"properties":{"SO4_near_N":{"type":"object","required":["DMAPS","MPC","CBMA"],"additionalProperties":false},"H2O_near_N":{"type":"object","required":["DMAPS","MPC","CBMA"],"additionalProperties":false},"Zn_near_neg":{"type":"object","required":["DMAPS","MPC","CBMA"],"additionalProperties":false},"H2O_near_neg":{"type":"object","required":["DMAPS","MPC","CBMA"],"additionalProperties":false}},"additionalProperties":false},"dipole_moments":{"type":"object","required":["DMAPS","MPC","CBMA"],"additionalProperties":false}},"units":{"binding_energies":"eV","dipole_moments":"Debye"}}
- Scoring: scored by hidden verifier

### Step 3: MD simulations of water states in gel electrolytes
- Role: process
- Action: Run classical molecular dynamics simulations of 2 M ZnSO₄ aqueous electrolyte containing each zwitterionic polymer (PDMAPS, PMPC, PCBMA) using an explicit atomistic model and standard force fields. For each system, analyze the simulation trajectories to determine the percentages of water molecules that are in free, Zn²⁺-coordinated, and polymer-fixed states.
- Evidence: `/app/outputs/md_water_runtimes.log`

### Step 4: Write water state percentages
- Role: scored (load-bearing)
- Action: Write a JSON file containing the computed percentages of free, Zn²⁺-coordinated, and polymer-fixed H₂O for PDMAPS, PMPC, and PCBMA gel electrolytes.
- Output file: `/app/outputs/water_states.json`
- Format: json
- Contract: {"type":"object","required":["free_H2O","Zn_coordinated_H2O","polymer_fixed_H2O"],"properties":{"free_H2O":{"type":"object","required":["PDMAPS","PMPC","PCBMA"],"additionalProperties":false},"Zn_coordinated_H2O":{"type":"object","required":["PDMAPS","PMPC","PCBMA"],"additionalProperties":false},"polymer_fixed_H2O":{"type":"object","required":["PDMAPS","PMPC","PCBMA"],"additionalProperties":false}},"units":{"free_H2O":"percent","Zn_coordinated_H2O":"percent","polymer_fixed_H2O":"percent"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_and_dipole.json`
- `/app/outputs/water_states.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_and_dipole.json
- path: `/app/outputs/binding_and_dipole.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Binding energies (eV) for four specific monomer interactions and molecular dipole moments (Debye) for DMAPS, MPC, CBMA. The checker will verify the relative ordering of binding energies and that dipole moments satisfy DMAPS > MPC > CBMA.
- schema:
  - `type`: object
  - `required`: `binding_energies`, `dipole_moments`
  - `properties`:
    - `binding_energies`:
      - `type`: object
      - `required`: `SO4_near_N`, `H2O_near_N`, `Zn_near_neg`, `H2O_near_neg`
      - `properties`:
        - `SO4_near_N`:
          - `type`: object
          - `required`: `DMAPS`, `MPC`, `CBMA`
          - `additionalProperties`: False
        - `H2O_near_N`:
          - `type`: object
          - `required`: `DMAPS`, `MPC`, `CBMA`
          - `additionalProperties`: False
        - `Zn_near_neg`:
          - `type`: object
          - `required`: `DMAPS`, `MPC`, `CBMA`
          - `additionalProperties`: False
        - `H2O_near_neg`:
          - `type`: object
          - `required`: `DMAPS`, `MPC`, `CBMA`
          - `additionalProperties`: False
      - `additionalProperties`: False
    - `dipole_moments`:
      - `type`: object
      - `required`: `DMAPS`, `MPC`, `CBMA`
      - `additionalProperties`: False
  - `units`:
    - `binding_energies`: eV
    - `dipole_moments`: Debye

### water_states.json
- path: `/app/outputs/water_states.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Percentage of water molecules in free, Zn²⁺-coordinated, and polymer-fixed states for three gel electrolytes (PDMAPS, PMPC, PCBMA). The checker will verify that free water is lowest for PDMAPS and polymer-fixed water is highest for PDMAPS.
- schema:
  - `type`: object
  - `required`: `free_H2O`, `Zn_coordinated_H2O`, `polymer_fixed_H2O`
  - `properties`:
    - `free_H2O`:
      - `type`: object
      - `required`: `PDMAPS`, `PMPC`, `PCBMA`
      - `additionalProperties`: False
    - `Zn_coordinated_H2O`:
      - `type`: object
      - `required`: `PDMAPS`, `PMPC`, `PCBMA`
      - `additionalProperties`: False
    - `polymer_fixed_H2O`:
      - `type`: object
      - `required`: `PDMAPS`, `PMPC`, `PCBMA`
      - `additionalProperties`: False
  - `units`:
    - `free_H2O`: percent
    - `Zn_coordinated_H2O`: percent
    - `polymer_fixed_H2O`: percent

Notes: The task reproduces only the computational component of the paper; wet-lab experiments are excluded. The solving agent must use the provided SMILES strings as starting points for DFT and build polymer models for MD. Trends are scored, not exact numerical reproduction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_and_dipole.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "binding_energies",
          "dipole_moments"
        ],
        "properties": {
          "binding_energies": {
            "type": "object",
            "required": [
              "SO4_near_N",
              "H2O_near_N",
              "Zn_near_neg",
              "H2O_near_neg"
            ],
            "properties": {
              "SO4_near_N": {
                "type": "object",
                "required": [
                  "DMAPS",
                  "MPC",
                  "CBMA"
                ],
                "additionalProperties": false
              },
              "H2O_near_N": {
                "type": "object",
                "required": [
                  "DMAPS",
                  "MPC",
                  "CBMA"
                ],
                "additionalProperties": false
              },
              "Zn_near_neg": {
                "type": "object",
                "required": [
                  "DMAPS",
                  "MPC",
                  "CBMA"
                ],
                "additionalProperties": false
              },
              "H2O_near_neg": {
                "type": "object",
                "required": [
                  "DMAPS",
                  "MPC",
                  "CBMA"
                ],
                "additionalProperties": false
              }
            },
            "additionalProperties": false
          },
          "dipole_moments": {
            "type": "object",
            "required": [
              "DMAPS",
              "MPC",
              "CBMA"
            ],
            "additionalProperties": false
          }
        },
        "units": {
          "binding_energies": "eV",
          "dipole_moments": "Debye"
        }
      },
      "description": "Binding energies (eV) for four specific monomer interactions and molecular dipole moments (Debye) for DMAPS, MPC, CBMA. The checker will verify the relative ordering of binding energies and that dipole moments satisfy DMAPS > MPC > CBMA."
    },
    {
      "file": "water_states.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "free_H2O",
          "Zn_coordinated_H2O",
          "polymer_fixed_H2O"
        ],
        "properties": {
          "free_H2O": {
            "type": "object",
            "required": [
              "PDMAPS",
              "PMPC",
              "PCBMA"
            ],
            "additionalProperties": false
          },
          "Zn_coordinated_H2O": {
            "type": "object",
            "required": [
              "PDMAPS",
              "PMPC",
              "PCBMA"
            ],
            "additionalProperties": false
          },
          "polymer_fixed_H2O": {
            "type": "object",
            "required": [
              "PDMAPS",
              "PMPC",
              "PCBMA"
            ],
            "additionalProperties": false
          }
        },
        "units": {
          "free_H2O": "percent",
          "Zn_coordinated_H2O": "percent",
          "polymer_fixed_H2O": "percent"
        }
      },
      "description": "Percentage of water molecules in free, Zn²⁺-coordinated, and polymer-fixed states for three gel electrolytes (PDMAPS, PMPC, PCBMA). The checker will verify that free water is lowest for PDMAPS and polymer-fixed water is highest for PDMAPS."
    }
  ],
  "notes": "The task reproduces only the computational component of the paper; wet-lab experiments are excluded. The solving agent must use the provided SMILES strings as starting points for DFT and build polymer models for MD. Trends are scored, not exact numerical reproduction."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that inspects the content of `binding_and_dipole.json` and `water_states.json`. The verifier checks whether the relative trends and orderings among the computed values are consistent with the physical relationships reported in the source study. It does not require exact numerical reproduction; instead it focuses on the correct ordering of binding strengths, the relative magnitudes of dipole moments, and the expected distribution of water states across the three polymers. Each artifact is scored independently, and the final reward is a weighted combination. Simply writing numbers that match a known target without performing the computations will not satisfy the verifier, as the scoring is designed to reward honest execution of the workflow.
