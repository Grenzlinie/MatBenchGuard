# DFT Energy Comparison of SiCN Cluster Bonding Configurations

## Problem background
Amorphous silicon carbon nitride (a-SiCN) thin films can exhibit a strong bonding preference when nitrogen is introduced during deposition, resulting in a marked change in the local bonding structure. To explain this experimentally observed affinity, computational studies have examined simple SiCN cluster models using density functional theory (DFT). In this task you will reproduce the computational part: building hydrogen-terminated cluster models and computing their total energies and key bond lengths to investigate the relative stability of Si–C versus Si–N bonding configurations.

## Approach
The approach uses ab initio total-energy calculations on four small SiCN clusters, each terminated with hydrogen atoms to avoid boundary effects. The clusters represent different bonding arrangements: Si–C–N, Si–N–C, Si–C=N, and Si–N=C. For each cluster, perform a geometry optimization and total-energy calculation with a consistent DFT setup (e.g., the PBE functional, spin-paired, with an appropriate basis set or pseudopotentials). From the optimized geometries, extract the final total energy and the Si–C and Si–N bond lengths. The relative stabilities of the configurations and the bond-length trends provide insight into the bonding preferences in the material.

## Reproduction target
Compute the total energy (in eV) and the Si–C and Si–N bond lengths (in Å) for each of the four clusters after geometry optimization. Report all results in a single JSON file. From your computed energies, determine which bonding arrangement is more stable in each pair (Si–C–N vs Si–N–C, and Si–C=N vs Si–N=C), and compare the Si–N and Si–C bond lengths to see whether one is consistently shorter. The hidden verifier will evaluate whether your results satisfy the expected stability ordering and bond-length relation.

## Assets

- Open-source DFT software (e.g., ORCA, Quantum ESPRESSO, GPAW, CP2K)
- Python 3

## Workflow steps

### Step 1: Construct cluster models
- Role: process
- Action: Build initial atomic geometries for four hydrogen-terminated SiCN clusters: Si-C-N, Si-N-C, Si-C=N, Si-N=C. Dangling bonds are saturated with H atoms as described in the paper. Output initial coordinates in a suitable format for the DFT code.
- Evidence: `/app/outputs/initial_clusters.xyz`

### Step 2: Perform DFT geometry optimization and total energy calculation
- Role: process
- Action: Use the chosen open-source DFT code to carry out geometry optimization and total energy calculation for each of the four clusters. Use a consistent computational setup (e.g., PBE functional, spin-paired, appropriate basis/pseudopotential). Extract the final total energy and the Si-C and Si-N bond lengths from the optimized structures.
- Evidence: `/app/outputs/dft_details.log`

### Step 3: Report computed energies and bond lengths
- Role: scored (load-bearing)
- Action: Write a JSON file results.json with key 'clusters' containing a list of four objects, each with fields: 'name' (string: 'Si-C-N', 'Si-N-C', 'Si-C=N', 'Si-N=C'), 'total_energy_eV' (float), and 'bond_lengths' (object with float keys 'Si-C' and 'Si-N' where applicable).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with key 'clusters' (list of objects). Each object has 'name' (string), 'total_energy_eV' (float), and 'bond_lengths' (object with float values for 'Si-C' and/or 'Si-N').
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
- target_policy: structural_audit
- description: Energies and bond lengths for the four SiCN clusters; used to verify relative stability ordering and bond length trends.
- schema:
  - `type`: object
  - `required`:
    - `clusters`: list of cluster objects
  - `items`:
    - `name`: string
    - `total_energy_eV`: float (eV)
    - `bond_lengths`: object with keys 'Si-C' and 'Si-N', each a float (Å)

Notes: The absolute total energies are method-dependent, so ordering and bond-length trends are the verifiable claims.

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
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "clusters": "list of cluster objects"
        },
        "items": {
          "name": "string",
          "total_energy_eV": "float (eV)",
          "bond_lengths": "object with keys 'Si-C' and 'Si-N', each a float (Å)"
        }
      },
      "description": "Energies and bond lengths for the four SiCN clusters; used to verify relative stability ordering and bond length trends."
    }
  ],
  "notes": "The absolute total energies are method-dependent, so ordering and bond-length trends are the verifiable claims."
}
```

## How you are scored
A hidden verifier reads your `results.json` and compares the reported energies and bond lengths against established reference criteria. It checks whether the energy ordering between the paired configurations meets the expected trend and whether the bond-length comparisons are consistent. The verifier combines the results of each check into a single reward between 0 and 1. Simply reporting numbers without the correct physical ordering will not yield a high score; the values must reflect the underlying bonding preferences captured by the DFT calculations.
