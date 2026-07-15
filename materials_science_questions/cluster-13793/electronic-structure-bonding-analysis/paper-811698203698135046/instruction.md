# First-Principles Study of Cu Doping Effects on Electronic Structure of Ca3Co2O6

## Problem background
Thermoelectric materials can convert waste heat to electricity, offering a clean energy solution. Oxide thermoelectrics like Ca3Co2O6 have attracted attention for high-temperature stability, but their conversion efficiency is often limited by low electrical conductivity. Ca3Co2O6 features a quasi-one-dimensional crystal structure with Co-O chains along the c axis, which are believed to dominate the electronic transport. Doping with Cu at the Co sites is a strategy to modify the electronic structure and improve thermoelectric performance. Understanding how Cu doping alters the band structure, charge distribution, and chemical bonding is essential for guiding further material optimization. This task involves first-principles calculations to quantify these effects for undoped and Cu-doped Ca3Co2O6 supercells.

## Approach
Density functional theory (DFT) calculations using a plane-wave basis set with a generalized gradient approximation (GGA) functional such as PBE are performed. Two supercell models are built from the known crystal structure: a pristine Ca18Co12O36 supercell and a doped Ca18Cu3Co9O36 supercell where three Co1 atoms are replaced by Cu. Spin-polarized self-consistent field (SCF) calculations yield the electronic structure, including band energies and charge density. Band structures are computed to extract the band gap between the highest occupied and lowest unoccupied states. Population analysis (e.g., Mulliken or similar scheme) provides atomic net charges and covalent bond orders (bond overlap populations). The undoped system serves as the baseline, and changes in the electronic properties upon Cu doping are assessed by comparing the two compositions.

## Reproduction target
Perform DFT calculations on the two supercells to obtain the following quantities:
- Band gap (eV) for the undoped supercell and the Cu-doped supercell.
- Average atomic net charges (in elementary charge units) for each atom type in both supercells, covering the relevant Co, Cu, Ca, and O sites as defined in the output schema.
- Average covalent bond orders for the atom pairs Co1-O, Co2-O, Ca-O, Co1-Co2 in the undoped supercell, and Cu-O, Co2-O, Ca-O, Cu-Co2 in the doped supercell.
All values must be written to /app/outputs/results.json in the schema defined in the workflow steps.

## Assets

- Crystal structure of Ca3Co2O6: 10.1006/jssc.1996.0285
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build supercell models
- Role: process
- Action: Construct atomic coordinate files for Ca18Co12O36 and Ca18Cu3Co9O36 supercells based on the known Ca3Co2O6 crystal structure (space group R-3c, a=9.0793 Å, c=10.3810 Å). For the doped cell, replace three Co1 atoms by Cu as described in the paper (center and diagonal positions).
- Evidence: `/app/outputs/supercell_models.zip`

### Step 2: Perform DFT calculations
- Role: process
- Action: Run spin-polarized DFT calculations for both supercells using an open-source plane-wave code (e.g., Quantum ESPRESSO) with a suitable functional (e.g., PBE) and pseudopotentials. Compute SCF, band structure, and perform population analysis (e.g., Mulliken or similar) to obtain atomic net charges and bond overlap populations.
- Evidence: `/app/outputs/scf_output.log`

### Step 3: Extract electronic and bonding properties
- Role: scored (load-bearing)
- Action: From the DFT outputs, extract the band gaps (eV) for the undoped and Cu-doped systems. Compute average net charges (e) for each atom type as listed in Table I. Compute average covalent bond orders for the bonds listed in Table II. Write all values to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"band_gap_undoped": "number (eV)", "band_gap_doped": "number (eV)", "net_charges_undoped": {"Co1": "number", "Co2": "number", "Ca": "number", "O": "number"}, "net_charges_doped": {"Cu": "number", "Co2": "number", "Ca": "number", "O": "number"}, "bond_orders_undoped": {"Co1-O": "number", "Co2-O": "number", "Ca-O": "number", "Co1-Co2": "number"}, "bond_orders_doped": {"Cu-O": "number", "Co2-O": "number", "Ca-O": "number", "Cu-Co2": "number"}}
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
- description: DFT-computed band gaps, atomic net charges, and covalent bond orders for undoped and Cu-doped Ca3Co2O6 supercells.
- schema:
  - `type`: object
  - `required`: `band_gap_undoped`, `band_gap_doped`, `net_charges_undoped`, `net_charges_doped`, `bond_orders_undoped`, `bond_orders_doped`
  - `properties`:
    - `band_gap_undoped`:
      - `type`: number
      - `unit`: eV
    - `band_gap_doped`:
      - `type`: number
      - `unit`: eV
    - `net_charges_undoped`:
      - `type`: object
      - `properties`:
        - `Co1`:
          - `type`: number
        - `Co2`:
          - `type`: number
        - `Ca`:
          - `type`: number
        - `O`:
          - `type`: number
    - `net_charges_doped`:
      - `type`: object
      - `properties`:
        - `Cu`:
          - `type`: number
        - `Co2`:
          - `type`: number
        - `Ca`:
          - `type`: number
        - `O`:
          - `type`: number
    - `bond_orders_undoped`:
      - `type`: object
      - `properties`:
        - `Co1-O`:
          - `type`: number
        - `Co2-O`:
          - `type`: number
        - `Ca-O`:
          - `type`: number
        - `Co1-Co2`:
          - `type`: number
    - `bond_orders_doped`:
      - `type`: object
      - `properties`:
        - `Cu-O`:
          - `type`: number
        - `Co2-O`:
          - `type`: number
        - `Ca-O`:
          - `type`: number
        - `Cu-Co2`:
          - `type`: number

Notes: All values are compared against hidden paper-reported reference values within tolerances appropriate for DFT re-runs. No implementation-specific parameters are mandated.

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
        "required": [
          "band_gap_undoped",
          "band_gap_doped",
          "net_charges_undoped",
          "net_charges_doped",
          "bond_orders_undoped",
          "bond_orders_doped"
        ],
        "properties": {
          "band_gap_undoped": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_doped": {
            "type": "number",
            "unit": "eV"
          },
          "net_charges_undoped": {
            "type": "object",
            "properties": {
              "Co1": {
                "type": "number"
              },
              "Co2": {
                "type": "number"
              },
              "Ca": {
                "type": "number"
              },
              "O": {
                "type": "number"
              }
            }
          },
          "net_charges_doped": {
            "type": "object",
            "properties": {
              "Cu": {
                "type": "number"
              },
              "Co2": {
                "type": "number"
              },
              "Ca": {
                "type": "number"
              },
              "O": {
                "type": "number"
              }
            }
          },
          "bond_orders_undoped": {
            "type": "object",
            "properties": {
              "Co1-O": {
                "type": "number"
              },
              "Co2-O": {
                "type": "number"
              },
              "Ca-O": {
                "type": "number"
              },
              "Co1-Co2": {
                "type": "number"
              }
            }
          },
          "bond_orders_doped": {
            "type": "object",
            "properties": {
              "Cu-O": {
                "type": "number"
              },
              "Co2-O": {
                "type": "number"
              },
              "Ca-O": {
                "type": "number"
              },
              "Cu-Co2": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "DFT-computed band gaps, atomic net charges, and covalent bond orders for undoped and Cu-doped Ca3Co2O6 supercells."
    }
  ],
  "notes": "All values are compared against hidden paper-reported reference values within tolerances appropriate for DFT re-runs. No implementation-specific parameters are mandated."
}
```

## How you are scored
A hidden verifier reads your results.json and compares each numeric field to a set of predetermined reference values derived from the original paper's reported results. The comparison uses tolerances designed to accept a correct DFT re-implementation with a suitable functional and pseudopotentials, while excluding trivial guesses. Each field is checked independently; all fields must be within tolerance for full credit. Partial credit is assigned proportionally based on the number of fields that satisfy the tolerance. The reward is a float between 0 and 1. Simply printing the paper's numbers without performing the actual calculations is not sufficient—the verifier expects the output to match the reference exactly within the allowed margin, which a lazy guess cannot achieve. The scored workflow stage (extracting electronic and bonding properties) carries the entire reward; the process steps (building models, running DFT) are necessary prerequisites but not directly scored.
