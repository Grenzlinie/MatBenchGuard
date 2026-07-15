# Photocatalytic Water Splitting Band Edge Assessment

## Problem background
Two-dimensional van der Waals heterostructures formed by combining blue phosphorus (blueP) with Janus transition-metal dichalcogenide monolayers SMoSe and SWSe (M = Mo, W) are promising candidates for visible-light photocatalytic water splitting. The band alignment type (type‑I or type‑II) and the absolute energies of the valence band maximum (VBM) and conduction band minimum (CBM) relative to the vacuum level determine whether a heterostructure can thermodynamically drive both the hydrogen evolution half‑reaction, the oxygen evolution half‑reaction, or only one of them. This task computes those properties from first‑principles to assess the photocatalytic suitability of four heterobilayer combinations: P-SeMoS, P-SMoSe, P-SeWS, and P-SWSe.

## Approach
First‑principles density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and the Grimme D2 van der Waals correction is used to relax the isolated monolayers (blueP, SMoSe, SWSe) and the corresponding heterobilayers. The hybrid HSE06 functional is additionally employed to obtain more accurate band gaps and absolute band‑edge positions. The computational workflow proceeds as follows:

1. Relax the geometry of each free‑standing monolayer and compute its PBE and HSE06 band gap to verify the method.
2. Build initial heterobilayer geometries using the two possible chalcogen‑ordering models (SMSe and SeMS) and test different stacking configurations; select the most stable stacking by binding energy and interlayer distance, then perform full relaxation with PBE+D2.
3. For each relaxed heterostructure compute projected band structures with both PBE and HSE06. From the projections extract the orbital character and the spatial localization (which monolayer) of the VBM and CBM to identify the band alignment type (type‑I if both edges reside in the same layer, type‑II otherwise).
4. Compare the absolute VBM/CBM energies (with respect to vacuum) to the standard water reduction potential (−4.44 eV at pH 0) and oxidation potential (−5.67 eV at pH 0) to decide whether overall water splitting is thermodynamically feasible (‘overall’), only the oxidation half‑reaction is feasible (‘oxidation_only’), or neither condition is met (‘no’).

All calculations are performed with an open‑source DFT code (e.g., Quantum ESPRESSO or CP2K) and publicly available PBE pseudopotentials appropriate for S, Se, P, Mo, and W.

## Reproduction target
Produce a single JSON file that collects the final computed properties for the four heterobilayers (P-SeMoS, P-SMoSe, P-SeWS, P-SWSe). For each heterostructure the record must contain:

- band_gap_PBE (eV) and band_gap_HSE06 (eV): the electronic band gap obtained with the PBE and HSE06 functionals.
- VBM_energy_vacuum (eV) and CBM_energy_vacuum (eV): the absolute energies of the valence band maximum and conduction band minimum relative to the vacuum level.
- VBM_localization and CBM_localization: the monolayer (blueP, SMoSe, or SWSe) where the respective band edge is predominantly located.
- alignment_type: either ‘I’ (both edges in the same layer) or ‘II’ (edges in different layers).
- water_splitting_type: a label stating whether the heterostructure can perform overall water splitting (‘overall’), only the oxidation half‑reaction (‘oxidation_only’), or cannot meet either redox condition (‘no’), based on the computed band‑edge positions relative to the standard potentials (−4.44 eV reduction, −5.67 eV oxidation).

All values must be derived from the DFT workflow; the exact output file path is `/app/outputs/results.json`.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO v7.2 or CP2K v2024.1): https://www.quantum-espresso.org/
- PBE pseudopotential library (e.g., SSSP efficiency for PWscf or GTH for CP2K): https://www.materialscloud.org/discover/sssp/table/efficiency
- Initial crystal structures of blueP, SMoSe, and SWSe monolayers

## Workflow steps

### Step 1: Monolayer geometry relaxation
- Role: process
- Action: Relax the atomic positions and lattice parameters of isolated blueP, SMoSe, and SWSe monolayers using DFT-PBE with Grimme D2 van der Waals correction. Compute PBE and HSE06 band gaps to verify the method.
- Evidence: `/app/outputs/monolayer_results.json`

### Step 2: Heterobilayer construction and relaxation
- Role: process
- Action: Using the relaxed monolayers, build initial geometries for the four heterobilayers (P-SeMoS, P-SMoSe, P-SeWS, P-SWSe) by stacking the monolayers in the two chalcogen-ordering models (SMSe and SeMS) and testing the stacking configurations described in the task. Identify the most stable stacking by binding energy and interlayer distance, then fully relax the optimum structure with DFT-PBE+D2.
- Evidence: `/app/outputs/heterobilayer_geometries.json`

### Step 3: Electronic structure and band alignment analysis
- Role: process
- Action: For each relaxed heterostructure, compute band structures with PBE and HSE06 functionals. Extract the absolute VBM and CBM energies (relative to vacuum). From projected band structures, determine the orbital character at the band edges and the spatial localization (which monolayer) to classify each heterostructure as type-I or type-II.
- Evidence: `/app/outputs/electronic_properties.json`

### Step 4: Photocatalytic feasibility evaluation and final report
- Role: scored (load-bearing)
- Action: Using the absolute VBM/CBM energies obtained in step 03, compare each heterostructure's band edges to the standard water reduction (-4.44 eV) and oxidation (-5.67 eV) potentials at pH=0 vs. vacuum. Determine the water-splitting suitability: 'overall' if both edges straddle the redox potentials, 'oxidation_only' if only the oxidation potential is satisfied, or 'no' otherwise. Collect all final quantities — band gaps (PBE and HSE06), VBM/CBM energies, VBM and CBM localization (blueP or Janus layer), alignment type (I or II), and water_splitting_type — into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with top-level keys 'P-SeMoS', 'P-SMoSe', 'P-SeWS', 'P-SWSe'. Each value is an object with keys: band_gap_PBE (float, eV), band_gap_HSE06 (float, eV), VBM_energy_vacuum (float, eV), CBM_energy_vacuum (float, eV), VBM_localization (string: 'blueP' or 'SMoSe' or 'SWSe'), CBM_localization (string: 'blueP' or 'SMoSe' or 'SWSe'), alignment_type (string: 'I' or 'II'), water_splitting_type (string: 'overall' | 'oxidation_only' | 'no').
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
- description: Scored artifact: band gaps (PBE/HSE06), absolute VBM/CBM energies (vacuum‑referenced, negative values), VBM and CBM localization, band alignment type, and water splitting suitability for each of the four heterobilayers.
- schema:
  - `type`: object
  - `required`:
    - `P-SeMoS`:
      - `band_gap_PBE`: float (eV)
      - `band_gap_HSE06`: float (eV)
      - `VBM_energy_vacuum`: float (eV)
      - `CBM_energy_vacuum`: float (eV)
      - `VBM_localization`: string
      - `CBM_localization`: string
      - `alignment_type`: string
      - `water_splitting_type`: string
    - `P-SMoSe`:
      - `band_gap_PBE`: float (eV)
      - `band_gap_HSE06`: float (eV)
      - `VBM_energy_vacuum`: float (eV)
      - `CBM_energy_vacuum`: float (eV)
      - `VBM_localization`: string
      - `CBM_localization`: string
      - `alignment_type`: string
      - `water_splitting_type`: string
    - `P-SeWS`:
      - `band_gap_PBE`: float (eV)
      - `band_gap_HSE06`: float (eV)
      - `VBM_energy_vacuum`: float (eV)
      - `CBM_energy_vacuum`: float (eV)
      - `VBM_localization`: string
      - `CBM_localization`: string
      - `alignment_type`: string
      - `water_splitting_type`: string
    - `P-SWSe`:
      - `band_gap_PBE`: float (eV)
      - `band_gap_HSE06`: float (eV)
      - `VBM_energy_vacuum`: float (eV)
      - `CBM_energy_vacuum`: float (eV)
      - `VBM_localization`: string
      - `CBM_localization`: string
      - `alignment_type`: string
      - `water_splitting_type`: string
  - `items`: object
  - `units`:
    - `band_gap_PBE`: eV
    - `band_gap_HSE06`: eV
    - `VBM_energy_vacuum`: eV
    - `CBM_energy_vacuum`: eV

Notes: The scored artifact is compared against vacuum‑aligned reference values from the paper (Fig. 6). Tolerances: 0.15 eV for band gaps, 0.30 eV for VBM/CBM energies (wider because the reference is read from a figure). Categorical fields (alignment_type, water_splitting_type, localization) are compared exactly. Reward is proportional to the fraction of correctly reproduced entries across the four heterostructures.

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
        "required": {
          "P-SeMoS": {
            "band_gap_PBE": "float (eV)",
            "band_gap_HSE06": "float (eV)",
            "VBM_energy_vacuum": "float (eV)",
            "CBM_energy_vacuum": "float (eV)",
            "VBM_localization": "string",
            "CBM_localization": "string",
            "alignment_type": "string",
            "water_splitting_type": "string"
          },
          "P-SMoSe": {
            "band_gap_PBE": "float (eV)",
            "band_gap_HSE06": "float (eV)",
            "VBM_energy_vacuum": "float (eV)",
            "CBM_energy_vacuum": "float (eV)",
            "VBM_localization": "string",
            "CBM_localization": "string",
            "alignment_type": "string",
            "water_splitting_type": "string"
          },
          "P-SeWS": {
            "band_gap_PBE": "float (eV)",
            "band_gap_HSE06": "float (eV)",
            "VBM_energy_vacuum": "float (eV)",
            "CBM_energy_vacuum": "float (eV)",
            "VBM_localization": "string",
            "CBM_localization": "string",
            "alignment_type": "string",
            "water_splitting_type": "string"
          },
          "P-SWSe": {
            "band_gap_PBE": "float (eV)",
            "band_gap_HSE06": "float (eV)",
            "VBM_energy_vacuum": "float (eV)",
            "CBM_energy_vacuum": "float (eV)",
            "VBM_localization": "string",
            "CBM_localization": "string",
            "alignment_type": "string",
            "water_splitting_type": "string"
          }
        },
        "items": {},
        "units": {
          "band_gap_PBE": "eV",
          "band_gap_HSE06": "eV",
          "VBM_energy_vacuum": "eV",
          "CBM_energy_vacuum": "eV"
        }
      },
      "description": "Scored artifact: band gaps (PBE/HSE06), absolute VBM/CBM energies (vacuum‑referenced, negative values), VBM and CBM localization, band alignment type, and water splitting suitability for each of the four heterobilayers."
    }
  ],
  "notes": "The scored artifact is compared against vacuum‑aligned reference values from the paper (Fig. 6). Tolerances: 0.15 eV for band gaps, 0.30 eV for VBM/CBM energies (wider because the reference is read from a figure). Categorical fields (alignment_type, water_splitting_type, localization) are compared exactly. Reward is proportional to the fraction of correctly reproduced entries across the four heterostructures."
}
```

## How you are scored
After you submit `/app/outputs/results.json`, a hidden verifier reads the file and compares each entry to reference values for the same quantity and heterostructure. Numerical fields (band gaps, VBM/CBM energies) are checked against reference tolerances; categorical fields (localization, alignment type, water splitting type) are compared for exact match. The reward is proportional to the fraction of the four heterostructures for which all associated entries are correctly reproduced. The intermediate evidence files (`monolayer_results.json`, `heterobilayer_geometries.json`, `electronic_properties.json`) are not scored but must be produced as part of the workflow; only the final `results.json` determines your reward.
