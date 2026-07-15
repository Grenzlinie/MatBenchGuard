# Hydrated Silica Surface QM/MM Interaction with Molecular Probes

## Problem background
The interaction of hydrated silica surfaces with molecular probes is central to understanding acid-base properties and surface reactivity. When adsorbates hydrogen-bond to surface silanol groups, the O-H stretching frequency shifts relative to the clean surface, and the magnitude of the shift depends on the adsorbate and the treatment of electrostatic interactions in computational models. In a hybrid quantum mechanical / molecular mechanics (QM/MM) simulation, one must decide how the MM region's charges influence the QM region. The present work studies three coupling levels: (1) steric-only, where the MM part provides only steric repulsion; (2) electrostatic with fixed charges obtained once from isolated fragments; and (3) electrostatic with charges updated after a preliminary optimization. The central open question is which treatment gives O-H stretching frequencies closest to experiment for adsorbates that interact weakly versus strongly with the silica surface. Reproducing the frequency shifts and adsorption enthalpies for a systematic set of probe molecules allows this question to be answered quantitatively.

## Approach
We use a cluster model cut from the (111) surface of β-cristobalite. The neutral cluster (OH)Si25O66H33 is partitioned into a QM region containing the surface hydroxyl group and its first neighbours and an MM region representing the rest of the lattice, with hydrogen link atoms capping broken bonds. Force field parameters for Si–O, O–H bonds, angles, torsions, and van der Waals interactions are as defined in the embedded force field table (Sybyl-type).

Density functional theory (DFT) calculations at the PBE level with a triple-ζ basis set are used for the QM region. The workflow starts by computing Hirshfeld atomic charges on the isolated cluster and on each free probe molecule; these charges are later used in the electrostatic coupling. The clean surface O–H frequency is obtained from a QM/MM optimization with fixed charges. Then, for each of seven probe molecules (H2S, O3, CO, NH3, (CH3)2CO, C5H5N, CH3CN), three QM/MM optimizations are performed:

- Steric-only coupling (no electrostatic interaction between QM and MM) – labeled PM‑A_st.
- Electrostatic coupling with the initial charges – PM‑A_el.
- Updated-charge coupling: after a PM‑A_el optimization, a single-point QM calculation on the whole complex provides new Hirshfeld charges, which are then used in a re-optimization – PM‑A_ch.

For each treatment we compute the adsorption enthalpy ΔH = E(complex) – E(clean A) – E(free probe) and the O–H stretching frequency v; from the clean surface reference we obtain the shift Δv = v_OH_clean – v. The collection of these values for the clean surface and all probes constitutes the final reproduction target.

## Reproduction target
Reproduce the complete QM/MM protocol: build the silica cluster, partition it, obtain initial charges, optimize the clean surface and compute its O–H stretching frequency, then for each of the seven probes run three optimizations per probe (steric-only, fixed-charge, updated-charge) and compute ΔH, v, and Δv. The final output is a single JSON file `qm_mm_results.json` containing one entry for the clean surface (with its O–H frequencies under the three treatments) and one entry for each probe, listing the adsorption enthalpies (ΔH_st, ΔH_el, ΔH_ch), O–H stretching frequencies (v_st, v_el, v_ch), and frequency shifts (Δv_st, Δv_el, Δv_ch). The objective is to produce numbers that, when compared against hidden reference values, are within the tolerances expected for an independent QM/MM implementation using a modern code.

## Assets

- Open-source DFT/QM-MM code: cp2k or nwchem or orca
- Beta-cristobalite crystal structure: http://www.crystallography.net/cod/1011098.cif
- Sybyl force field parameters for silica (from Table 1 of the paper):

| Parameter       | K (kcal/mol/Å² or kcal/mol/deg²) | r0 (Å) | kδ (kcal/mol/deg²) | ϑ0 (deg) | kτ (kcal/mol) | An        | D0 (kcal/mol) | R0 (Å) |
|-----------------|----------------------------------|--------|---------------------|-----------|---------------|-----------|---------------|--------|
| Si–O            | 1827.44                          | 1.55   |                     |           |               |           |               |        |
| O–H             | 1114.65                          | 0.98   |                     |           |               |           |               |        |
| O–Si–O          |                                  |        | 0.001               | 109.7     |               |           |               |        |
| Si–O–Si         |                                  |        | 0.191               | 180       |               |           |               |        |
| Si–O–H          |                                  |        | 0.11                | 180       |               |           |               |        |
| Si–O–Si–O       |                                  |        |                     |           | 1.485         | –3        |               |        |
| Si              |                                  |        |                     |           |               |           | 0.0420        | 4.200  |
| O               |                                  |        |                     |           |               |           | 0.1160        | 3.040  |
| H               |                                  |        |                     |           |               |           | 0.0420        | 3.000  |

Notes: Eoop values are set to 0. Units: K and kδ are in kcal/mol/Å² and kcal/mol/deg², respectively; r0 and R0 are in Å; kτ and D0 are in kcal/mol; n is the periodicity and A its sign.

## Workflow steps

### Step 1: Build Silica Cluster Model A
- Role: process
- Action: Construct the silica cluster model A (OH)Si25O66H33 from the (111) surface of beta-cristobalite. Define the QM/MM partition: inner QM region B (OH)Si7O6, outer MM region. Terminate the QM region with hydrogen link atoms at 1.497 Angstrom. Assign the provided Sybyl force field parameters to the MM atoms.
- Evidence: `/app/outputs/cluster_model.xyz`

### Step 2: Compute Initial Hirshfeld Charges
- Role: process
- Action: Perform single-point PBE DFT calculations on the isolated silica cluster A (no probe) and on each of the seven free probe molecules (H2S, O3, CO, NH3, (CH3)2CO, C5H5N, CH3CN) to obtain Hirshfeld atomic charges for all atoms. Store these charges for later electrostatic coupling.
- Evidence: `/app/outputs/initial_charges.json`

### Step 3: Clean Surface QM/MM Optimization
- Role: process
- Action: Set up QM/MM calculation for cluster A with the defined partition and force field parameters. Optimize the geometry of the O3SiOH surface site (hydroxyl group and nearest neighbours) and compute the O-H stretching frequency of the clean surface. Record this frequency as v_OH_clean.
- Evidence: `/app/outputs/clean_oh_freq.txt`

### Step 4: Probe Adsorption QM/MM Calculations and Aggregate Results
- Role: scored (load-bearing)
- Action: For each of the seven probe molecules (H2S, O3, CO, NH3, (CH3)2CO, C5H5N, CH3CN), conduct three QM/MM geometry optimizations: (a) steric-only coupling (PM-A_st) with no electrostatic coupling; (b) electrostatic coupling using the initial Hirshfeld charges from step 1 (PM-A_el); (c) electrostatic coupling with updated charges – take the optimized PM-A_el geometry, run a single-point QM on the whole PM-A_el cluster to obtain new Hirshfeld charges, then re-optimize (PM-A_ch). For each treatment compute the adsorption enthalpy ΔH and the O-H stretching frequency v, and also the frequency shift Δv = v_OH_clean – v. Collect all results, including the clean surface frequency, into a single JSON file named qm_mm_results.json.
- Output file: `/app/outputs/qm_mm_results.json`
- Format: json
- Contract: JSON array of objects, each with keys: probe (string), delta_H_st (float), delta_H_el (float), delta_H_ch (float), v_st (float), v_el (float), v_ch (float), delta_v_st (float), delta_v_el (float), delta_v_ch (float). The first element has probe='clean', v_st/v_el/v_ch from the clean surface (delta_H fields set to 0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/qm_mm_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### qm_mm_results.json
- path: `/app/outputs/qm_mm_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated QM/MM results for clean and seven probe systems. Frequencies in cm^-1, enthalpies in kcal/mol. Clean surface entry has probe='clean', v_st/v_el/v_ch from the clean surface, and delta_H fields set to 0.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `probe`:
        - `type`: string
      - `delta_H_st`:
        - `type`: number
      - `delta_H_el`:
        - `type`: number
      - `delta_H_ch`:
        - `type`: number
      - `v_st`:
        - `type`: number
      - `v_el`:
        - `type`: number
      - `v_ch`:
        - `type`: number
      - `delta_v_st`:
        - `type`: number
      - `delta_v_el`:
        - `type`: number
      - `delta_v_ch`:
        - `type`: number
    - `required`: `probe`, `v_st`, `v_el`, `v_ch`, `delta_v_st`, `delta_v_el`, `delta_v_ch`, `delta_H_st`, `delta_H_el`, `delta_H_ch`

Notes: The array must contain exactly eight entries: one for 'clean' and one for each of H2S, O3, CO, NH3, (CH3)2CO, C5H5N, CH3CN. The order of probe entries after the clean entry is not prescribed. The checker will compare frequency and enthalpy values to hidden reference values within tolerances, and verify the relative ordering of the different treatments.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "qm_mm_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "probe": {
              "type": "string"
            },
            "delta_H_st": {
              "type": "number"
            },
            "delta_H_el": {
              "type": "number"
            },
            "delta_H_ch": {
              "type": "number"
            },
            "v_st": {
              "type": "number"
            },
            "v_el": {
              "type": "number"
            },
            "v_ch": {
              "type": "number"
            },
            "delta_v_st": {
              "type": "number"
            },
            "delta_v_el": {
              "type": "number"
            },
            "delta_v_ch": {
              "type": "number"
            }
          },
          "required": [
            "probe",
            "v_st",
            "v_el",
            "v_ch",
            "delta_v_st",
            "delta_v_el",
            "delta_v_ch",
            "delta_H_st",
            "delta_H_el",
            "delta_H_ch"
          ]
        }
      },
      "description": "Aggregated QM/MM results for clean and seven probe systems. Frequencies in cm^-1, enthalpies in kcal/mol. Clean surface entry has probe='clean', v_st/v_el/v_ch from the clean surface, and delta_H fields set to 0."
    }
  ],
  "notes": "The array must contain exactly eight entries: one for 'clean' and one for each of H2S, O3, CO, NH3, (CH3)2CO, C5H5N, CH3CN. The order of probe entries after the clean entry is not prescribed. The checker will compare frequency and enthalpy values to hidden reference values within tolerances, and verify the relative ordering of the different treatments."
}
```

## How you are scored
Your output is evaluated by a hidden verifier that reads `qm_mm_results.json`. The verifier checks the following, each contributing a portion of the final score:

- Numerical accuracy: how well your computed O–H stretching frequencies and adsorption enthalpies agree with the paper's reference values (within tolerances that reflect the expected variation from using a different code, basis set, and convergence settings).
- Relative treatment ordering: whether the relationship between v_st, v_el, and v_ch for each probe follows the qualitative patterns that a correct implementation of the three coupling schemes should exhibit (e.g., the steric-only model may over‑ or under‑shift weakly interacting probes compared to the electrostatic models, and the updated-charge treatment should not produce frequencies that are wildly inconsistent with the other two).
- Self‑consistency: e.g., the frequency shifts Δv derived from the reported clean‑surface frequency are consistent with the reported v values.

The final reward is a float in [0, 1], with larger weight given to the scored step that aggregates the probe results. To succeed you must faithfully execute the described protocol; merely guessing or copying known literature values will fail the verifier's tolerance and structural checks.
