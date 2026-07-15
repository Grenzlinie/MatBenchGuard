# DFT Evaluation of MBene Catalysts for CO2 Reduction: Adsorption, Activation, and Selectivity

## Problem background
Electrochemical reduction of CO2 into value-added fuels is a promising strategy to close the carbon cycle and mitigate greenhouse gas emissions. The search for efficient, selective catalysts is a central challenge. Two-dimensional layered materials, including MBenes (transition-metal borides), have attracted attention owing to their large surface area and tunable electronic properties. Theoretical evaluation via density functional theory (DFT) can screen candidate catalysts by predicting adsorption energies, intermediate binding strength, and reaction free-energy landscapes. This task assesses the performance of four MBene nanosheets — Mo2B2, Cr2B2, Fe2B2, Mn2B2 — and a reference Cu(111) surface for the electrochemical reduction of CO2 to CH4, focusing on CO2 activation, the potential‑limiting CHO formation step, and the competing hydrogen evolution reaction.

## Approach
Adsorption and reaction energies are computed with spin‑polarized DFT using the PBE exchange‑correlation functional, the D3 dispersion correction, and a plane‑wave basis set. Catalyst surfaces are modelled as periodic slabs with a vacuum gap. A computational hydrogen electrode (CHE) model relates the free energy of proton–electron pairs to gaseous H2. Gibbs free energy changes include zero‑point energy and entropy corrections at 298.15 K. The workflow proceeds in six stages: (i) constructing slab models from bulk crystal structures; (ii) relaxing clean surfaces; (iii) computing reference total energies of gas‑phase CO2, H2, and H2O; (iv) relaxing CO2 on each surface and extracting adsorption energies and geometric distortions; (v) relaxing the key intermediates *CO, *CHO and *H; (vi) assembling all results into a single JSON file that contains the computed quantities. The approach uses only public, open‑source resources (Quantum ESPRESSO, SSSP pseudopotentials, crystal structures from the Materials Project).

## Reproduction target
Produce a JSON file `step_01_results.json` containing, for each of the five surfaces (Mo2B2, Cr2B2, Fe2B2, Mn2B2, Cu(111)): (1) `adsorption_energy`—the CO2 adsorption energy E_ads = E(slab+CO2) – E(slab) – E(CO2_gas) in eV; (2) `C_O_bond_length`—the longer C=O bond length in the adsorbed CO2 (Å); (3) `OCO_angle`—the O–C–O bond angle (degrees); (4) `CHO_free_energy_change`—the Gibbs free energy change ΔG (eV) for the hydrogenation step *CO + H+ + e– → *CHO using the CHE model at 298.15 K; (5) `HER_free_energy_change`—the Gibbs free energy of hydrogen adsorption ΔG_H* (eV) using the same model. Use the most stable adsorption sites found. The task requires that these quantities be computed from first‑principles. You must then, based on your computed numbers, conclude whether the following trend hypotheses are supported: (a) CO2 adsorption is stronger on all MBenes than on Cu(111), with Mo2B2 showing the strongest adsorption; (b) CO2 is significantly bent on MBenes (angle ≪ 180°) while remaining essentially linear on Cu(111); (c) the CHO formation free energy increase is lower on Mo2B2 and Cr2B2 than on Fe2B2, Mn2B2, and Cu(111); (d) the HER free energy is more negative (indicating weaker H‑evolution activity) on Mo2B2 and Cr2B2 compared to the other three surfaces.

## Assets

- Quantum ESPRESSO DFT code: https://www.quantum-espresso.org/download
- PBE pseudopotentials (SSSP efficiency 1.3): https://www.materialscloud.org/discover/sssp/table
- Crystal structures for MBenes and Cu: https://materialsproject.org
- Reference molecular geometries

## Workflow steps

### Step 1: Construct catalyst surface slab models
- Role: process
- Action: Build initial atomic coordinates for MBene (Mo2B2, Cr2B2, Fe2B2, Mn2B2) and Cu(111) slab models using literature crystallographic data. For MBenes: hexagonal P6/mmm bulk, cut into four-layer slabs (metal-boron-boron-metal), bottom two layers fixed, 3x3 supercell, 20 Å vacuum. For Cu(111): fcc Cu cut as a four-layer slab, bottom two layers fixed, 3x3 supercell, 20 Å vacuum.
- Evidence: `/app/outputs/slab_geometries.log`

### Step 2: DFT geometry optimization of clean surfaces
- Role: process
- Action: Perform DFT relaxation of the clean catalyst surface slabs using the PBE functional with D3 dispersion correction. Use convergence criteria: forces < 0.02 eV/Å, energy < 1e-5 eV. Choose appropriate plane-wave cutoff (e.g., 450 eV) and k-point sampling (e.g., 3x3x1 for surfaces). Include spin polarization for magnetic atoms.
- Evidence: `/app/outputs/clean_surface_energies.json`

### Step 3: DFT calculation of gas-phase reference molecules
- Role: process
- Action: Compute total energies of isolated CO2, H2, and H2O molecules in a 20x20x20 Å³ box using the same DFT settings. Perform vibrational frequency analysis to obtain zero-point energy (ZPE) and entropy corrections at 298.15 K.
- Evidence: `/app/outputs/gas_references.json`

### Step 4: DFT calculation of CO2 adsorption on surfaces
- Role: process
- Action: For each catalyst surface, determine the most stable adsorption site for CO2 (bridge site). Perform DFT relaxation of the adsorbate+slab system. Compute adsorption energy: E_ads = E(slab+CO2) - E(slab) - E(CO2_gas). Extract C-O bond lengths and O-C-O bond angle.
- Evidence: `/app/outputs/co2_adsorption_raw.json`

### Step 5: DFT calculation of key intermediates (*CO, *CHO, *H)
- Role: process
- Action: Compute DFT energies for adsorbed *CO (most stable site: hollow for Mo2B2/Cr2B2, top for others), *CHO (bridge site), and hydrogen atom *H (bridge for MBenes, hollow for Cu) on each clean surface. Perform geometry optimization for each species.
- Evidence: `/app/outputs/intermediate_energies.json`

### Step 6: Assemble reproduction targets
- Role: scored (load-bearing)
- Action: From the previously computed raw data, calculate for each surface (Mo2B2, Cr2B2, Fe2B2, Mn2B2, Cu(111)): (1) adsorption_energy = E_ads (eV); (2) C_O_bond_length = adsorbed CO2 C=O bond length (Å); (3) OCO_angle = O-C-O bond angle (deg); (4) CHO_free_energy_change = ΔG for *CO + H+ + e- -> *CHO using the computational hydrogen electrode model (eV); (5) HER_free_energy_change = ΔG for H* adsorption using the same model (eV). Write the results as an array of objects to step_01_results.json.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: Array of objects, each with keys: surface (string), adsorption_energy (eV, float), C_O_bond_length (Å, float), OCO_angle (deg, float), CHO_free_energy_change (eV, float), HER_free_energy_change (eV, float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Contains the reproduction targets for each catalyst surface. The hidden checker evaluates four qualitative trends: (1) adsorption energy ordering (Mo2B2 most negative, then Cr2B2, then Mn2B2/Fe2B2, Cu(111) least negative); (2) O-C-O angles on MBenes significantly < 180°, on Cu(111) ≈ 180°; (3) CHO free energy increase lower on Mo2B2 and Cr2B2 than on Fe2B2, Mn2B2, Cu(111); (4) HER free energy more negative (weaker activity) on Mo2B2 and Cr2B2 compared to Fe2B2, Mn2B2, Cu(111).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required_keys`: `surface`, `adsorption_energy`, `C_O_bond_length`, `OCO_angle`, `CHO_free_energy_change`, `HER_free_energy_change`
    - `units`:
      - `adsorption_energy`: eV
      - `C_O_bond_length`: Å
      - `OCO_angle`: degrees
      - `CHO_free_energy_change`: eV
      - `HER_free_energy_change`: eV
  - `description`: Array of results for the five surfaces (Mo2B2, Cr2B2, Fe2B2, Mn2B2, Cu(111)). Each entry has the six required keys.

Notes: Scoring is based on qualitative trend correctness, not exact numeric agreement, because the agent uses a different DFT code (Quantum ESPRESSO) than the original VASP.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required_keys": [
            "surface",
            "adsorption_energy",
            "C_O_bond_length",
            "OCO_angle",
            "CHO_free_energy_change",
            "HER_free_energy_change"
          ],
          "units": {
            "adsorption_energy": "eV",
            "C_O_bond_length": "Å",
            "OCO_angle": "degrees",
            "CHO_free_energy_change": "eV",
            "HER_free_energy_change": "eV"
          }
        },
        "description": "Array of results for the five surfaces (Mo2B2, Cr2B2, Fe2B2, Mn2B2, Cu(111)). Each entry has the six required keys."
      },
      "description": "Contains the reproduction targets for each catalyst surface. The hidden checker evaluates four qualitative trends: (1) adsorption energy ordering (Mo2B2 most negative, then Cr2B2, then Mn2B2/Fe2B2, Cu(111) least negative); (2) O-C-O angles on MBenes significantly < 180°, on Cu(111) ≈ 180°; (3) CHO free energy increase lower on Mo2B2 and Cr2B2 than on Fe2B2, Mn2B2, Cu(111); (4) HER free energy more negative (weaker activity) on Mo2B2 and Cr2B2 compared to Fe2B2, Mn2B2, Cu(111)."
    }
  ],
  "notes": "Scoring is based on qualitative trend correctness, not exact numeric agreement, because the agent uses a different DFT code (Quantum ESPRESSO) than the original VASP."
}
```

## How you are scored
Your `step_01_results.json` will be read by a hidden verifier. The verifier checks four qualitative trends (a–d above) against reference expectations derived from the literature. Each trend carries equal weight; the overall score is the fraction of trends your computed data correctly capture. Exact numerical agreement is not required because different DFT implementations can shift absolute values; the scoring focuses on the sign and ordering of the five quantities across the five surfaces. The verifier does not access the internet and does not run DFT calculations itself.
