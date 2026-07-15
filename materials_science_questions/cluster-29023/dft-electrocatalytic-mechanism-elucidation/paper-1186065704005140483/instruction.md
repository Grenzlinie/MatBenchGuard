# DFT Adsorption Energy of AuCl4- on Isomeric COFs

## Problem background
Gold recovery from electronic waste is a pressing environmental and economic challenge. Recent research explores covalent organic frameworks (COFs) as materials for selective gold adsorption and photoreduction. In particular, two isomeric π-conjugated COFs based on triazine-aldehyde monomers, with either ortho-diazine (v-2D-COF-Dz) or para-pyrazine (v-2D-COF-Pz) units, have been studied for their ability to capture AuCl₄⁻ ions from solution. Understanding how the nitrogen topology influences the adsorption energy is key to designing more effective COF-based gold recovery systems. This task requires using density functional theory (DFT) to compute the adsorption energies of AuCl₄⁻ on these two COFs.

## Approach
The method involves building periodic AA-stacked structural models of v-2D-COF-Dz and v-2D-COF-Pz from their building blocks (TFPT aldehyde with 3,6-dimethylpyridazine and 2,5-dimethylpyrazine, respectively). After geometry optimization of the pristine COF unit cells, a single AuCl₄⁻ ion is placed at a specific binding site: on a carbon atom adjacent to nitrogen in v-2D-COF-Dz, and on a nitrogen atom in v-2D-COF-Pz. Plane-wave DFT calculations with the Perdew–Burke–Ernzerhof (PBE) functional are used to compute the total energies of the isolated COF slab, the isolated AuCl₄⁻ ion, and each COF+AuCl₄⁻ adsorption complex. The adsorption energy E_ads = E(COF+AuCl₄⁻) – E(COF) – E(AuCl₄⁻) is then computed for each COF. The calculations are performed using a publicly available periodic DFT code with standard pseudopotentials.

## Reproduction target
Compute and report, in electronvolts (eV), the adsorption energies of AuCl₄⁻ on the carbon site adjacent to nitrogen in v-2D-COF-Dz and on the nitrogen site in v-2D-COF-Pz. The results must be written to a JSON file containing the two adsorption energies. Additionally, determine the relative ordering of the two adsorption energies (which is more negative/stronger). This will reveal the topology-dependent adsorption affinity. No experimental data or measurements are to be reproduced; the task is purely computational.

## Assets

- Periodic DFT code (e.g., Quantum ESPRESSO, CP2K, VASP): https://www.quantum-espresso.org/
- PBE pseudopotentials (GBRV, SSSP, or similar)

## Workflow steps

### Step 1: Construct and geometry-optimise the COF unit cells
- Role: process
- Action: Construct AA-stacked periodic models of v-2D-COF-Dz (TFPT + 3,6-dimethylpyridazine) and v-2D-COF-Pz (TFPT + 2,5-dimethylpyrazine) using the connectivity described in the paper. Perform DFT geometry optimization (cell and atomic positions) to obtain relaxed structures for both COFs.
- Evidence: none

### Step 2: Compute AuCl4- adsorption energies on the two COFs
- Role: scored (load-bearing)
- Action: Place AuCl4- on the carbon site adjacent to nitrogen in the relaxed v-2D-COF-Dz structure, and on the nitrogen site in the relaxed v-2D-COF-Pz structure. Perform DFT calculations for the isolated COF slab, isolated AuCl4-, and each adsorption complex. Compute E_ads = E(COF+AuCl4-) - E(COF) - E(AuCl4-) for each case. Write the two energies in electronvolts to the output JSON.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: {"dz_adsorption_energy_eV": float, "pz_adsorption_energy_eV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The adsorption energy of AuCl4- on the carbon site adjacent to nitrogen in v-2D-COF-Dz, and on the nitrogen site in v-2D-COF-Pz. Both values in electronvolts.
- schema:
  - `type`: object
  - `required`:
    - `dz_adsorption_energy_eV`: number
    - `pz_adsorption_energy_eV`: number
  - `units`:
    - `dz_adsorption_energy_eV`: eV
    - `pz_adsorption_energy_eV`: eV

Notes: The checker compares the agent's computed adsorption energies to the paper-reported reference values within a tolerance and verifies that the Dz value is more negative (stronger adsorption) than the Pz value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "dz_adsorption_energy_eV": "number",
          "pz_adsorption_energy_eV": "number"
        },
        "units": {
          "dz_adsorption_energy_eV": "eV",
          "pz_adsorption_energy_eV": "eV"
        }
      },
      "description": "The adsorption energy of AuCl4- on the carbon site adjacent to nitrogen in v-2D-COF-Dz, and on the nitrogen site in v-2D-COF-Pz. Both values in electronvolts."
    }
  ],
  "notes": "The checker compares the agent's computed adsorption energies to the paper-reported reference values within a tolerance and verifies that the Dz value is more negative (stronger adsorption) than the Pz value."
}
```

## How you are scored
Your submission will be scored by a hidden automated verifier. The verifier reads the reported adsorption energies from `adsorption_energies.json` and compares them to reference values (derived from the original scientific study) within a tolerance that accounts for computational differences. It also checks that the relative ordering of the two energies (which one is more negative) is correct. Partial credit is awarded according to predefined rewards: accuracy of each energy value and correctness of the ordering determine the final score. You do not need to provide any additional files; only the JSON output is evaluated.
