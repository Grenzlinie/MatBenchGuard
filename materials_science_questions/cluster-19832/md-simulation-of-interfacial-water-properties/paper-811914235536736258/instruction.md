# LSFD Peptide β-Hairpin Folding via Molecular Dynamics

## Problem background
Amyloid diseases involve the conversion of proteins into β‑sheet‑rich fibrillar aggregates. Understanding the conformational distributions of fibrillogenic peptides in their monomeric state is a prerequisite for designing aggregation inhibitors. This task addresses the LSFD peptide (sequence LSFDNSGAITIG‑NH₂), a model amyloid peptide derived from a human adenovirus fibre protein. Previous experiments have shown that LSFD forms amyloid‑like fibrils and β‑rich monolayers, but the monomeric conformational preferences—especially the secondary structure content and the most populated folded state—are not fully established. The goal is to determine, via atomistic molecular dynamics simulations in explicit solvent, what equilibrium secondary structures and what dominant cluster conformation the LSFD peptide adopts in bulk water and at a water/vapor interface at an elevated temperature that facilitates reversible folding.

## Approach
Perform all‑atom, explicit‑solvent molecular dynamics simulations of the amidated LSFD peptide using the GROMOS96‑43a1 force field and the SPC water model. For bulk water, start from an extended peptide conformation in an octahedral box solvated with SPC water; for the interface, start from a compact β‑hairpin‑like conformation placed in a water slab and then extend the box to create a vapour phase. All production simulations are run at 350 K, which allows multiple folding and unfolding events within accessible timescales. For each environment, three independent trajectories are generated with different initial velocity distributions (bulk: NPT ensemble at 1 bar, at least 200 ns each with one extended to 300 ns; interface: NVT ensemble with a fixed box, 300 ns each). After discarding appropriate equilibration periods, the trajectories are analysed: compute per‑residue average secondary structure content (coil, β‑sheet, turn, bend) using backbone hydrogen‑bond definitions analogous to DSSP. Then perform Daura clustering on the main‑chain atoms of the core residues (384‑391) with an RMSD cutoff of 0.14 nm and report the percentage of configurations belonging to the largest cluster for each environment. This workflow probes the equilibrium conformational distribution and identifies the most populated folded state without imposing any prior bias on the structural outcome.

## Reproduction target
1. Set up and run molecular dynamics simulations of the LSFD peptide in bulk water at 350 K (three independent NPT runs, ≥200 ns each, one extended to 300 ns) and at a water/vapour interface at 350 K (three independent NVT runs, 300 ns each) using the GROMOS96‑43a1 force field and SPC water.
2. From the trajectories, after removing initial equilibration periods (5 ns for bulk; 10 ns plus any periods where the peptide completely desorbs from the interface), compute per‑residue average coil, β‑sheet, turn, and bend content for the full 12‑residue peptide.
3. Perform Daura clustering on the main‑chain atoms of residues 384‑391 with an RMSD cutoff of 0.14 nm and determine the percentage of configurations in the largest cluster for each environment.
4. Record all results in a single JSON file (`results.json`) with the structure: `{"water": {"secondary_structure": [{"residue": int, "beta_sheet": float, "turn": float, "bend": float, "coil": float}], "largest_cluster_percentage": float}, "interface": {"secondary_structure": [{"residue": int, "beta_sheet": float, "turn": float, "bend": float, "coil": float}], "largest_cluster_percentage": float}}`.

## Assets

- GROMACS: https://www.gromacs.org
- DSSP: dssp
- GROMOS96-43a1 force field: GROMACS force field files
- SPC water model: GROMACS water models

## Workflow steps

### Step 1: Prepare solvated LSFD system
- Role: process
- Action: Build the solvated LSFD peptide system from the amidated sequence LSFDNSGAITIG-NH2 in an extended conformation, solvate with ~7066 SPC water molecules in an octahedral box, energy minimize and equilibrate solvent with peptide restraints.
- Evidence: `/app/outputs/bulk_system.pdb`

### Step 2: Production MD of LSFD in water at 350 K
- Role: process
- Action: Run three independent NPT simulations at 350 K and 1 bar for at least 200 ns each (one extended to 300 ns) using the GROMOS96-43a1 force field, SPC water, 4 fs timestep, Berendsen thermostat and barostat. Use different initial velocity distributions per run.
- Evidence: none

### Step 3: Prepare LSFD at water/vapor interface system
- Role: process
- Action: Build the interfacial system by placing LSFD in a compact β-hairpin conformation in a water slab of size 4.5×4.5×3.6 nm³, energy minimize, equilibrate solvent, then extend the box to 9 nm in z to create a vapor phase.
- Evidence: `/app/outputs/interface_system.pdb`

### Step 4: Production MD of LSFD at interface at 350 K
- Role: process
- Action: Run three independent NVT simulations at 350 K for 300 ns each using a fixed box size, starting from the interfacial system with different initial velocity distributions.
- Evidence: none

### Step 5: Secondary structure and cluster analysis
- Role: scored (load-bearing)
- Action: Analyze the bulk water and interface trajectories after discarding appropriate equilibration periods. Compute per-residue average coil, β-sheet, turn, and bend content using DSSP-style hydrogen bond definitions. Perform Daura clustering on main-chain atoms of residues 384-391 with RMSD cutoff 0.14 nm and report the percentage of configurations in the largest cluster for each environment. Write the results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"water": {"secondary_structure": [{"residue": int, "beta_sheet": float, "turn": float, "bend": float, "coil": float}], "largest_cluster_percentage": float}, "interface": {"secondary_structure": [{"residue": int, "beta_sheet": float, "turn": float, "bend": float, "coil": float}], "largest_cluster_percentage": float}}
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
- target_policy: exact_match
- description: Scored artifact containing per-residue secondary structure percentages and the largest Daura cluster population for both bulk water and water/vapor interface environments at 350 K.
- schema:
  - `type`: object
  - `required`: `water`, `interface`
  - `properties`:
    - `water`:
      - `type`: object
      - `required`: `secondary_structure`, `largest_cluster_percentage`
      - `properties`:
        - `secondary_structure`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `residue`, `beta_sheet`, `turn`, `bend`, `coil`
            - `properties`:
              - `residue`:
                - `type`: integer
              - `beta_sheet`:
                - `type`: number
              - `turn`:
                - `type`: number
              - `bend`:
                - `type`: number
              - `coil`:
                - `type`: number
        - `largest_cluster_percentage`:
          - `type`: number
    - `interface`:
      - `type`: object
      - `required`: `secondary_structure`, `largest_cluster_percentage`
      - `properties`:
        - `secondary_structure`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `residue`, `beta_sheet`, `turn`, `bend`, `coil`
            - `properties`:
              - `residue`:
                - `type`: integer
              - `beta_sheet`:
                - `type`: number
              - `turn`:
                - `type`: number
              - `bend`:
                - `type`: number
              - `coil`:
                - `type`: number
        - `largest_cluster_percentage`:
          - `type`: number

Notes: The agent must produce the full per-residue secondary structure and cluster percentages by running the MD simulations and analysis; the hidden checker compares these reported values to the paper's results with appropriate tolerances.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "water",
          "interface"
        ],
        "properties": {
          "water": {
            "type": "object",
            "required": [
              "secondary_structure",
              "largest_cluster_percentage"
            ],
            "properties": {
              "secondary_structure": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "residue",
                    "beta_sheet",
                    "turn",
                    "bend",
                    "coil"
                  ],
                  "properties": {
                    "residue": {
                      "type": "integer"
                    },
                    "beta_sheet": {
                      "type": "number"
                    },
                    "turn": {
                      "type": "number"
                    },
                    "bend": {
                      "type": "number"
                    },
                    "coil": {
                      "type": "number"
                    }
                  }
                }
              },
              "largest_cluster_percentage": {
                "type": "number"
              }
            }
          },
          "interface": {
            "type": "object",
            "required": [
              "secondary_structure",
              "largest_cluster_percentage"
            ],
            "properties": {
              "secondary_structure": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "residue",
                    "beta_sheet",
                    "turn",
                    "bend",
                    "coil"
                  ],
                  "properties": {
                    "residue": {
                      "type": "integer"
                    },
                    "beta_sheet": {
                      "type": "number"
                    },
                    "turn": {
                      "type": "number"
                    },
                    "bend": {
                      "type": "number"
                    },
                    "coil": {
                      "type": "number"
                    }
                  }
                }
              },
              "largest_cluster_percentage": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Scored artifact containing per-residue secondary structure percentages and the largest Daura cluster population for both bulk water and water/vapor interface environments at 350 K."
    }
  ],
  "notes": "The agent must produce the full per-residue secondary structure and cluster percentages by running the MD simulations and analysis; the hidden checker compares these reported values to the paper's results with appropriate tolerances."
}
```

## How you are scored
An automated hidden verifier will read your `results.json` and compare each entry against reference data. The reward is based on how closely your per‑residue secondary structure percentages and largest cluster percentages match the expected values, with small allowances for the stochastic nature of the simulations. The two environments (water and interface) are weighted equally, and within each environment the per‑residue secondary structure array and the cluster percentage contribute to the score. The verifier also checks that the secondary structure percentages sum to approximately 100% for each residue. Reporting numbers alone without executing the full simulation and analysis pipeline is not sufficient – the verifier rewards faithful reproduction of the computational experiment.
