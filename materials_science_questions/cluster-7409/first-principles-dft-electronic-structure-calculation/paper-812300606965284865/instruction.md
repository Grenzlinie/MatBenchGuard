# DFT and device simulation of metal-doped TiO₂ electron transport layer for perovskite solar cells

## Problem background
Perovskite solar cells (PSCs) rely on an electron transport layer (ETL) to extract photogenerated electrons from the perovskite absorber and deliver them to the front contact. Titanium dioxide (TiO₂) in its rutile polymorph is a widely used ETL material due to its stability, transparency, and suitable band alignment. Doping TiO₂ with metals such as tin (Sn) or zinc (Zn) modifies the electronic structure, optical absorption, and carrier mobility of the oxide, which in turn alters the power conversion efficiency (PCE) of the full solar cell device. Reproducing these effects from first principles requires (i) obtaining the band gap, optical spectrum, and carrier mobilities of pristine and doped TiO₂ from density-functional theory (DFT) calculations, and (ii) feeding these computed properties into a semiconductor device simulator to obtain the current–voltage characteristics and the PCE. The present task is to compute the DFT+U band gaps and the resulting PCE values for pristine rutile TiO₂ and for TiO₂ doped with Sn at three concentrations (3.125, 4.17, 6.25 mol%) and with Zn at one concentration (4.17 mol%), using publicly available open-source tools.

## Approach
The computational workflow proceeds in three stages.

**DFT calculations.**  A plane-wave DFT simulation using the PBE+U exchange–correlation functional is performed on a rutile TiO₂ unit cell and on supercells in which one Ti atom is replaced by Sn or Zn. Geometry optimizations are followed by electronic structure calculations that yield the Kohn–Sham band gap and the partial density of states. Optical absorption spectra are obtained from the dielectric function via the independent-particle approximation and a Kramers–Kronig transform. Carrier mobilities are computed with the constant relaxation time approximation (CRTA) using the DFT band structure as input.

**Device modelling.**  The DFT-extracted band gap, absorption coefficient, and electron/hole mobilities are used to parameterize the ETL in a one-dimensional device simulator (SCAPS‑1D). The full device stack comprises glass/FTO (front contact), the ETL (80 nm), a thin interface layer, methylammonium lead iodide perovskite (310 nm), a second interface layer, Spiro‑OMeTAD hole-transport layer (160 nm), and a gold back contact. All non-ETL material parameters are taken from the literature. The simulation is performed under standard AM 1.5G illumination at 300 K, and the photovoltaic parameters (short‑circuit current, open‑circuit voltage, fill factor, and PCE) are extracted from the computed J–V curve.

**Comparison.**  The workflow is repeated for each doping condition, allowing a direct comparison of the device performance between pristine, Sn‑doped, and Zn‑doped TiO₂ ETLs.

## Reproduction target
Produce a single JSON file, `results.json`, that contains the computed DFT+U band gaps (in eV) and the SCAPS‑1D power conversion efficiencies (in %) for the five ETL compositions: pristine rutile TiO₂, Sn‑doped TiO₂ at 3.125, 4.17, and 6.25 mol%, and Zn‑doped TiO₂ at 4.17 mol%. The required keys are `pristine_band_gap`, `sn_3.125_band_gap`, `sn_4.17_band_gap`, `sn_6.25_band_gap`, `zn_4.17_band_gap`, `pristine_pce`, `sn_3.125_pce`, `sn_4.17_pce`, `sn_6.25_pce`, `zn_4.17_pce`. The goal is to faithfully reproduce the computational procedure described in the workflow; a correctly executed simulation will yield values that fall within the expected physical range and obey specific relative trends among the doping conditions.

## Assets

- Quantum ESPRESSO (plane-wave DFT code): https://www.quantum-espresso.org
- BoltzTraP2 (transport code): https://www.boltztrapp.com
- SCAPS‑1D (solar cell simulator): https://scaps.elis.ugent.be
- Python 3 with numpy, scipy, matplotlib: numpy,scipy,matplotlib
- PAW pseudopotentials for Ti, O, Sn, Zn: https://pseudopotentials.quantum-espresso.org
- Rutile TiO₂ crystal structure (lattice parameters a=4.5937 Å, c=2.9587 Å)

## Workflow steps

### Step 1: Geometry optimization of pristine rutile TiO₂ unit cell
- Role: process
- Action: Perform DFT+U geometry relaxation of the pristine rutile TiO₂ unit cell (tetragonal, space group P4₂/mnm) using PBE+U with Hubbard Ueff = 8.0 eV on Ti 3d and 6.5 eV on O 2p. Use PAW pseudopotentials, spin‑polarized calculation, and relax until forces are converged.
- Evidence: `/app/outputs/relaxed_pristine.out`

### Step 2: Electronic structure of pristine TiO₂: band gap and DOS
- Role: process
- Action: From the relaxed pristine structure, perform single‑point SCF and non‑SCF calculations to obtain the band structure and partial density of states (PDOS); compute the DFT+U band gap.
- Evidence: `/app/outputs/pristine_band_gap.txt`

### Step 3: Validate U parameter for Sn via SnO₂ band gap
- Role: process
- Action: Compute the band gap of bulk SnO₂ using DFT+U with Ueff = 6.0 eV on Sn 4d, as a validation of the U parameter choice.
- Evidence: `/app/outputs/sno2_band_gap.txt`

### Step 4: Construct Sn‑ and Zn‑doped supercells
- Role: process
- Action: Create 4×2×2, 3×2×2, and 2×2×2 supercells of rutile TiO₂ and substitute one Ti atom with Sn to achieve 3.125, 4.17, and 6.25 mol% Sn doping, respectively. Create a 3×2×2 supercell with one Ti replaced by Zn for 4.17 mol% Zn doping.
- Evidence: `/app/outputs/supercell_structures`

### Step 5: Geometry optimization of doped supercells
- Role: process
- Action: Relax all Sn‑doped and Zn‑doped supercells using the same DFT+U settings as step 1, with additional Ueff = 6.0 eV on Sn 4d and 10.8 eV on Zn 3d.
- Evidence: `/app/outputs/relaxed_doped.out`

### Step 6: Electronic structure of doped TiO₂: band gaps
- Role: process
- Action: Compute band gaps and DOS for all doped systems; extract band gap values.
- Evidence: `/app/outputs/doped_band_gaps.txt`

### Step 7: Optical property calculation
- Role: process
- Action: Compute the dielectric function and absorption spectra for the pristine and all doped systems via the independent‑particle approximation and Kramers‑Kronig transform; output absorption coefficient vs photon energy data.
- Evidence: `/app/outputs/absorption_spectra.dat`

### Step 8: Carrier mobility calculation (BoltzTraP2)
- Role: process
- Action: Convert DFT band structures to BoltzTraP2 input and compute electron and hole mobilities using the constant relaxation time approximation (τ = 1e-10 s).
- Evidence: `/app/outputs/mobility_table.csv`

### Step 9: SCAPS‑1D device simulations for all ETLs
- Role: process
- Action: For each ETL (pristine, Sn‑doped at three concentrations, Zn‑doped at 4.17 mol%), prepare and run SCAPS‑1D simulations using the device structure FTO/TiO₂ (80 nm)/interface layer (10 nm)/CH₃NH₃PbI₃ (310 nm)/interface layer (10 nm)/Spiro‑OMeTAD (160 nm)/Au. Use DFT‑extracted band gap, mobilities, and absorption spectra for the ETL, and literature parameters for the other layers. Extract photovoltaic parameters (Jsc, Voc, FF, PCE).
- Evidence: `/app/outputs/scaps_outputs.txt`

### Step 10: Collect all target quantities into a JSON file
- Role: scored (load-bearing)
- Action: Aggregate the band gaps (in eV) and power conversion efficiencies (PCE, in %) from the previous calculations into a single JSON file named results.json. The file must contain the keys: pristine_band_gap, sn_3.125_band_gap, sn_4.17_band_gap, sn_6.25_band_gap, zn_4.17_band_gap, pristine_pce, sn_3.125_pce, sn_4.17_pce, sn_6.25_pce, zn_4.17_pce.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "pristine_band_gap": "number",
  "sn_3.125_band_gap": "number",
  "sn_4.17_band_gap": "number",
  "sn_6.25_band_gap": "number",
  "zn_4.17_band_gap": "number",
  "pristine_pce": "number",
  "sn_3.125_pce": "number",
  "sn_4.17_pce": "number",
  "sn_6.25_pce": "number",
  "zn_4.17_pce": "number"
}
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
- description: JSON file containing the computed band gaps (eV) and power conversion efficiencies (%). The hidden checker compares each value to a paper‑reported reference with appropriate tolerances and also verifies the required relative ordering: pristine PCE < 3.125% Sn PCE > 4.17% Sn PCE > 6.25% Sn PCE, and Sn 4.17% PCE > Zn 4.17% PCE.
- schema:
  - `type`: object
  - `required`: `pristine_band_gap`, `sn_3.125_band_gap`, `sn_4.17_band_gap`, `sn_6.25_band_gap`, `zn_4.17_band_gap`, `pristine_pce`, `sn_3.125_pce`, `sn_4.17_pce`, `sn_6.25_pce`, `zn_4.17_pce`
  - `properties`:
    - `pristine_band_gap`:
      - `type`: number
    - `sn_3.125_band_gap`:
      - `type`: number
    - `sn_4.17_band_gap`:
      - `type`: number
    - `sn_6.25_band_gap`:
      - `type`: number
    - `zn_4.17_band_gap`:
      - `type`: number
    - `pristine_pce`:
      - `type`: number
    - `sn_3.125_pce`:
      - `type`: number
    - `sn_4.17_pce`:
      - `type`: number
    - `sn_6.25_pce`:
      - `type`: number
    - `zn_4.17_pce`:
      - `type`: number

Notes: Band gaps are compared to hidden reference values with a tolerance of ±0.1 eV; PCE values are compared with a tolerance of ±1% absolute. The relative ordering constraints are also enforced. The intermediate DFT and SCAPS artifacts are not scored.

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
          "pristine_band_gap",
          "sn_3.125_band_gap",
          "sn_4.17_band_gap",
          "sn_6.25_band_gap",
          "zn_4.17_band_gap",
          "pristine_pce",
          "sn_3.125_pce",
          "sn_4.17_pce",
          "sn_6.25_pce",
          "zn_4.17_pce"
        ],
        "properties": {
          "pristine_band_gap": {
            "type": "number"
          },
          "sn_3.125_band_gap": {
            "type": "number"
          },
          "sn_4.17_band_gap": {
            "type": "number"
          },
          "sn_6.25_band_gap": {
            "type": "number"
          },
          "zn_4.17_band_gap": {
            "type": "number"
          },
          "pristine_pce": {
            "type": "number"
          },
          "sn_3.125_pce": {
            "type": "number"
          },
          "sn_4.17_pce": {
            "type": "number"
          },
          "sn_6.25_pce": {
            "type": "number"
          },
          "zn_4.17_pce": {
            "type": "number"
          }
        }
      },
      "description": "JSON file containing the computed band gaps (eV) and power conversion efficiencies (%). The hidden checker compares each value to a paper‑reported reference with appropriate tolerances and also verifies the required relative ordering: pristine PCE < 3.125% Sn PCE > 4.17% Sn PCE > 6.25% Sn PCE, and Sn 4.17% PCE > Zn 4.17% PCE."
    }
  ],
  "notes": "Band gaps are compared to hidden reference values with a tolerance of ±0.1 eV; PCE values are compared with a tolerance of ±1% absolute. The relative ordering constraints are also enforced. The intermediate DFT and SCAPS artifacts are not scored."
}
```

## How you are scored
A hidden verifier will read your `results.json` and compare the band gaps and PCE values to independently determined reference values. Each quantity is scored by how closely it matches the reference, using tolerances that account for the legitimate spread introduced by different implementations of the same physical model. In addition, the verifier checks that the PCE values obey the physically expected ordering across doping concentrations and between the Sn‑ and Zn‑doped cases. Meeting the tolerances and satisfying all required trends earns full credit; reported numbers that deviate substantially or violate the expected order receive proportionally lower scores. The final reward is a weighted combination of the scores for each reported quantity, with the PCE values carrying the majority of the weight.
