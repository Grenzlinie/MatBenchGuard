# DFT electronic structure of V2O5 supported on TiO2 and Al2O3: band gaps and conduction band alignment

## Problem background
In selective catalytic reduction (SCR) of nitrogen oxides, the catalytic activity of supported vanadia catalysts depends strongly on the oxide support. Anatase TiO₂ and γ-Al₂O₃ are common supports, yet the electronic-structure origin of their different promoting effects is not fully understood. Density functional theory (DFT) calculations of monolayer V₂O₅ on these surfaces can probe band gaps, charge redistribution, and the alignment of the V₂O₅ conduction band relative to the Fermi level, offering mechanistic insight into support effects.

## Approach
Construct slab models of a monolayer V₂O₅ on the anatase TiO₂(001) and γ-Al₂O₃(100) surfaces. Relax the geometry of both models using spin‑polarized DFT with the GGA‑PBE exchange‑correlation functional, keeping the bottom layers fixed and including at least 20 Å of vacuum. For each relaxed structure, compute the total density of states (DOS) and the atomic‑site projected DOS (PDOS) for V and O atoms. From the total DOS extract the band gap as the energy difference between the valence‑band maximum and the conduction‑band minimum. From the V₂O₅ PDOS determine the energy of the V₂O₅ conduction‑band minimum relative to the Fermi level. Comparing the VTi and VAl systems reveals how the support modifies the electronic structure of the active vanadia layer.

## Reproduction target
Carry out the DFT workflow above and produce three structured output files:
- `step_01_band_gaps.json`: the DFT‑computed band gaps (in eV) for the VTi and VAl systems.
- `step_02_dos_data.csv`: a fine‑grid dataset of total DOS and PDOS contributions (V, support‑O, vanadia‑O) for both systems.
- `step_03_cb_offset.json`: the energy of the V₂O₅ conduction‑band minimum relative to the Fermi level (in eV) for VTi and VAl.
These values must be obtained from your own DFT simulations using the public crystal structures of anatase TiO₂ (mp‑390) and γ‑Al₂O₃ (mp‑1245); they must not be copied from any external source.

## Assets

- GGA-PBE DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Anatase TiO2 (001) slab model: https://materialsproject.org/materials/mp-390
- γ-Al2O3 (100) slab model: https://materialsproject.org/materials/mp-1245
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Geometry optimization of VTi and VAl slab models
- Role: process
- Action: Build monolayer V2O5 slab models on anatase TiO2(001) and γ-Al2O3(100) surfaces. Perform spin-polarized GGA-PBE DFT geometry relaxation with vacuum ≥20 Å.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: Electron density difference maps
- Role: process
- Action: Compute electron density difference maps for the relaxed VTi and VAl structures to visualize charge redistribution.
- Evidence: `/app/outputs/density_maps_report.txt`

### Step 3: Compute band gaps
- Role: scored (load-bearing)
- Action: From the relaxed structures, compute total density of states (DOS). Determine the band gap as the energy difference between the valence band maximum and conduction band minimum for each model. Extract and report the band gaps.
- Output file: `/app/outputs/step_01_band_gaps.json`
- Format: json
- Contract: {"VTi_band_gap_eV": <float>, "VAl_band_gap_eV": <float>}
- Scoring: scored by hidden verifier

### Step 4: Full DOS and PDOS data
- Role: scored
- Action: Compute and output the detailed total DOS and projected DOS (V, O from support, O from V2O5) for both VTi and VAl models on a fine energy grid covering valence and conduction bands near the Fermi level.
- Output file: `/app/outputs/step_02_dos_data.csv`
- Format: csv
- Contract: system,energy_eV,total_dos,pdos_V,pdos_O_support,pdos_O_vana
- Scoring: scored by hidden verifier

### Step 5: V2O5 conduction band minimum relative to Fermi
- Role: scored
- Action: From the projected DOS of V2O5 in each model, determine the energy of the conduction band minimum (onset) relative to the Fermi level. Report for both VTi and VAl models.
- Output file: `/app/outputs/step_03_cb_offset.json`
- Format: json
- Contract: {"VTi_V2O5_CB_minus_Fermi_eV": <float>, "VAl_V2O5_CB_minus_Fermi_eV": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_gaps.json`
- `/app/outputs/step_02_dos_data.csv`
- `/app/outputs/step_03_cb_offset.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_gaps.json
- path: `/app/outputs/step_01_band_gaps.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Band gaps for VTi and VAl models.
- schema:
  - `type`: object
  - `required`:
    - `VTi_band_gap_eV`: float
    - `VAl_band_gap_eV`: float

### step_02_dos_data.csv
- path: `/app/outputs/step_02_dos_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Full DOS and PDOS data for both systems.
- schema:
  - `type`: table
  - `required_columns`: `system`, `energy_eV`, `total_dos`, `pdos_V`, `pdos_O_support`, `pdos_O_vana`

### step_03_cb_offset.json
- path: `/app/outputs/step_03_cb_offset.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Conduction band minimum energies relative to Fermi level.
- schema:
  - `type`: object
  - `required`:
    - `VTi_V2O5_CB_minus_Fermi_eV`: float
    - `VAl_V2O5_CB_minus_Fermi_eV`: float

Notes: Scoring verifies relative trends based on the submitted values; the specific expected ordering is not disclosed. Only relative trends are scored; absolute DFT band-gap values are not compared to any fixed reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "VTi_band_gap_eV": "float",
          "VAl_band_gap_eV": "float"
        }
      },
      "description": "Band gaps for VTi and VAl models."
    },
    {
      "file": "step_02_dos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "energy_eV",
          "total_dos",
          "pdos_V",
          "pdos_O_support",
          "pdos_O_vana"
        ]
      },
      "description": "Full DOS and PDOS data for both systems."
    },
    {
      "file": "step_03_cb_offset.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "VTi_V2O5_CB_minus_Fermi_eV": "float",
          "VAl_V2O5_CB_minus_Fermi_eV": "float"
        }
      },
      "description": "Conduction band minimum energies relative to Fermi level."
    }
  ],
  "notes": "Scoring verifies relative trends based on the submitted values; the specific expected ordering is not disclosed. Only relative trends are scored; absolute DFT band-gap values are not compared to any fixed reference."
}
```

## How you are scored
The hidden verifier reads your submitted files and evaluates them stage by stage. It will verify that the relative ordering of the computed band gaps and conduction‑band offsets matches the expected physical trend (the details of which are not disclosed). For the DOS file, it performs sanity and consistency checks. Only the relative trend is scored; absolute DFT band‑gap values are not compared to any fixed reference. Each scored stage contributes a weight, and the final reward is a weighted sum.
