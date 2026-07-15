# DFT Reproduction of Dual-Atom Nanozyme Synergistic Effects on Peroxidase-like Activity

## Problem background
Single-atom nanozymes exhibit peroxidase (POD)-like activity, but their catalytic efficiency is limited by scaling relations. Dual-atom nanozymes (DAzymes), particularly heteronuclear metal‑nitrogen‑carbon systems such as Fe₁Co₁‑NC, are proposed to overcome this limitation by introducing a second metal site that modifies the electronic structure and reaction pathway. To understand the underlying synergistic effect at the atomic scale, density functional theory (DFT) is used to compute the adsorption and dissociation of H₂O₂ on model catalyst surfaces, the charge redistribution upon dissociation, and the d‑band centre of the active Fe atom. The aim of this reproduction is to independently compute these quantities for the single‑atom Fe₁‑NC and the dual‑atom Fe₁Co₁‑NC and to compare them so that the role of the Co dopant can be assessed from first‑principles simulation.

## Approach
We build periodic slab models of Fe‑N₄ and Fe‑Co‑N₄ coordination embedded in a graphitic carbon nitride matrix using the bond lengths and coordination numbers extracted from EXAFS analysis (Fe–N 2.03 Å, Fe–O 1.77 Å, Co–N 2.01 Å, Co–O 1.79 Å; Fe–N coordination 4, Co–N coordination 4, one O neighbour each). Spin‑polarised DFT calculations with the PBE exchange‑correlation functional and a dispersion correction (DFT‑D3) are employed. After geometry optimisation, the H₂O₂ adsorption state (H₂O₂*), the dissociated state (2OH*), and the clean surface plus gas‑phase H₂O₂ are evaluated to obtain total energies. Bader charge analysis is performed on the 2OH* configuration to quantify the net charge on the OH fragments. The projected density of states (PDOS) of the Fe d‑orbitals is used to compute the d‑band centre relative to the Fermi level. All calculations are carried out for both Fe₁‑NC and Fe₁Co₁‑NC under identical simulation settings to ensure a fair comparison.

## Reproduction target
Compute and report the following quantities for Fe₁‑NC and Fe₁Co₁‑NC:
- The H₂O₂ dissociation energy ΔE = E(2OH*) − E(H₂O₂*) in eV.
- The net Bader charge (in units of e) on the two OH fragments in the 2OH* configuration.
- The Fe d‑band centre (in eV, referenced to the Fermi level) extracted from the projected density of states.
Present the results in three CSV files as specified in the workflow steps. The reproduction is considered successful if the relative ordering between the two systems for each quantity matches the trend predicted by the dual‑atom synergistic mechanism.

## Assets

- Quantum ESPRESSO DFT code: https://www.quantum-espresso.org/
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/
- Atomic Simulation Environment: ase
- Standard pseudopotential library (SSSP): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build DFT slab models
- Role: process
- Action: Construct periodic slab models of Fe-N₄ and Fe-Co-N₄ coordination embedded in a graphitic carbon nitride matrix, using the bond lengths (Fe–N 2.03 Å, Fe–O 1.77 Å, Co–N 2.01 Å, Co–O 1.79 Å) and coordination numbers (Fe–N 4, Co–N 4, one O neighbor each) from EXAFS analysis. Create a vacuum layer and fix bottom layers as needed.
- Evidence: `/app/outputs/structure_files.txt`

### Step 2: DFT geometry optimization and electronic structure
- Role: process
- Action: Perform spin-polarized DFT relaxation on both Fe₁-NC and Fe₁Co₁-NC slabs to obtain relaxed atomic positions, total energies, and electronic density of states (DOS). Use a suitable exchange-correlation functional and dispersion correction. Save the relaxed coordinates, total energies, and projected DOS for Fe d orbitals.
- Evidence: `/app/outputs/relaxed_energies.txt`

### Step 3: H₂O₂ dissociation energy
- Role: scored (load-bearing)
- Action: From the relaxed slabs, adsorb H₂O₂ on the Fe site and optimize to obtain the adsorbed H₂O₂* state energy; then dissociate H₂O₂ into two OH groups (one migrating to the Co site in Fe₁Co₁-NC) and optimize to obtain the 2OH* state energy. Compute the dissociation energy ΔE = E(2OH*) − E(H₂O₂*) for both systems. Write the results.
- Output file: `/app/outputs/step_01_dissociation_energy.csv`
- Format: csv
- Contract: Two columns: 'system' (string: Fe1-NC, Fe1Co1-NC), 'dissociation_energy_eV' (float)
- Scoring: scored by hidden verifier

### Step 4: Bader charge on 2OH*
- Role: scored (load-bearing)
- Action: Using the 2OH* optimized geometry, perform Bader charge analysis to obtain the net charge (in e) on the two OH fragments. Write the net charge for each system.
- Output file: `/app/outputs/step_02_bader_charge.csv`
- Format: csv
- Contract: Two columns: 'system' (string: Fe1-NC, Fe1Co1-NC), 'charge_e' (float)
- Scoring: scored by hidden verifier

### Step 5: Fe d-band center
- Role: scored
- Action: From the projected density of states, compute the d-band center of the Fe atom (energy relative to Fermi level) for both Fe₁-NC and Fe₁Co₁-NC. Write the d-band center values.
- Output file: `/app/outputs/step_03_d_band_center.csv`
- Format: csv
- Contract: Two columns: 'system' (string: Fe1-NC, Fe1Co1-NC), 'd_band_center_eV' (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_dissociation_energy.csv`
- `/app/outputs/step_02_bader_charge.csv`
- `/app/outputs/step_03_d_band_center.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_dissociation_energy.csv
- path: `/app/outputs/step_01_dissociation_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: H₂O₂ dissociation energy for Fe₁-NC and Fe₁Co₁-NC. The checker verifies a relative ordering between the two systems; no absolute numerical thresholds are imposed.
- schema:
  - `type`: table
  - `required_columns`: `system`, `dissociation_energy_eV`
  - `units`:
    - `dissociation_energy_eV`: eV

### step_02_bader_charge.csv
- path: `/app/outputs/step_02_bader_charge.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Net Bader charge on 2OH* for Fe₁-NC and Fe₁Co₁-NC. The checker verifies a relative ordering between the two systems; no absolute numerical thresholds are imposed.
- schema:
  - `type`: table
  - `required_columns`: `system`, `charge_e`
  - `units`:
    - `charge_e`: e

### step_03_d_band_center.csv
- path: `/app/outputs/step_03_d_band_center.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Fe d-band center for Fe₁-NC and Fe₁Co₁-NC. The checker verifies a relative ordering between the two systems; no absolute numerical thresholds are imposed.
- schema:
  - `type`: table
  - `required_columns`: `system`, `d_band_center_eV`
  - `units`:
    - `d_band_center_eV`: eV

Notes: All scored quantities are checked by relative trend (ordering) between the two systems; no absolute numerical thresholds are imposed. The task focuses on the core DFT mechanistic claim of synergistic effect of Co doping on Fe in the dual-atom nanozyme.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_dissociation_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "dissociation_energy_eV"
        ],
        "units": {
          "dissociation_energy_eV": "eV"
        }
      },
      "description": "H₂O₂ dissociation energy for Fe₁-NC and Fe₁Co₁-NC. The checker verifies a relative ordering between the two systems; no absolute numerical thresholds are imposed."
    },
    {
      "file": "step_02_bader_charge.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "charge_e"
        ],
        "units": {
          "charge_e": "e"
        }
      },
      "description": "Net Bader charge on 2OH* for Fe₁-NC and Fe₁Co₁-NC. The checker verifies a relative ordering between the two systems; no absolute numerical thresholds are imposed."
    },
    {
      "file": "step_03_d_band_center.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "d_band_center_eV"
        ],
        "units": {
          "d_band_center_eV": "eV"
        }
      },
      "description": "Fe d-band center for Fe₁-NC and Fe₁Co₁-NC. The checker verifies a relative ordering between the two systems; no absolute numerical thresholds are imposed."
    }
  ],
  "notes": "All scored quantities are checked by relative trend (ordering) between the two systems; no absolute numerical thresholds are imposed. The task focuses on the core DFT mechanistic claim of synergistic effect of Co doping on Fe in the dual-atom nanozyme."
}
```

## How you are scored
A hidden verifier independently checks each of the three output CSV files. For each file, the verifier compares the value reported for Fe1‑NC with that reported for Fe1Co1‑NC. A specific relative ordering (greater than or less than) is expected; if the ordering holds exactly, that artifact earns full weight. Partial credit is awarded if some but not all artifacts satisfy their required ordering. No absolute numerical tolerance is imposed – only the relative trend matters, because the absolute values depend on the exact DFT setup. The final reward is the weighted sum of the per‑artifact scores (the main targets carry the largest weight), scaled to the interval [0, 1].
