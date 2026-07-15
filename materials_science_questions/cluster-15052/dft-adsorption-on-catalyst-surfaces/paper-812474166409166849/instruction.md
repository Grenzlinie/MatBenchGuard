# DFT Calculations of CO2 Adsorption and Reduction Energetics on Modified Bi19Br3S27 Surfaces

## Problem background
Photocatalytic reduction of CO₂ into solar fuels is a promising route toward carbon neutralization, but efficiency is limited by poor utilization of near-infrared (NIR) light, which constitutes ~50% of solar energy. Narrow-bandgap semiconductors such as Bi₁₉Br₃S₂₇ can absorb in the NIR region. Surface modifications like dual anion vacancies and oxygen doping can potentially alter the electronic structure and the energetics of CO₂ adsorption, activation, and hydrogenation. Understanding how interfacial engineering affects these reaction energetics is critical for designing efficient photocatalysts. This task computationally investigates CO₂ reduction energetics on pristine and modified Bi₁₉Br₃S₂₇ surfaces to quantify adsorption energies, charge transfer, and the free‑energy profile of the CO₂‑to‑CH₃OH pathway.

## Approach
Use periodic density functional theory (DFT) with an open‑source planewave code (e.g., Quantum ESPRESSO or CP2K), PBE functional, PAW pseudopotentials, and DFT‑D3 dispersion correction. Build three surface slab models from the public Bi₁₉Br₃S₂₇ crystal structure: (i) pristine Bi₁₉Br₃S₂₇(310), (ii) V_Br‑S‑Bi₁₉Br₃S₂₇ (dual Br‑S vacancies), and (iii) V‑Bi₁₉Br₃S₂₇ (dual Br‑S vacancies plus oxygen doping). After geometry optimization of the clean slabs, place a CO₂ molecule on each surface, re‑optimize, and compute the adsorption energy and the Bader charge transferred to the adsorbed CO₂. Then construct the full eight‑step CO₂‑to‑CH₃OH pathway (CO₂(gas) → *CO₂ → *COOH → *CO → *CHO → *CH₂O → *CH₃O → *CH₃OH → CH₃OH(gas)) on each surface, compute the total energy of each intermediate, apply zero‑point and entropic corrections to obtain Gibbs free energies. The computed quantities will map the effect of vacancies and oxygen doping on the reaction landscape.

## Reproduction target
The goal is to produce two CSV files that capture the CO₂ adsorption energetics and the full free‑energy pathway on the three surface models. Specifically: (1) For each surface (pristine, V_BrS, V), compute the CO₂ adsorption energy (eV) and the Bader charge on the adsorbed CO₂ (e), and report them in step_02_adsorption_energies_and_charges.csv. (2) For each surface and each reaction step in the CO₂‑to‑CH₃OH mechanism, compute the Gibbs free energy (eV) and report them in step_03_gibbs_free_energy_profiles.csv. The three surfaces must be identified by the labels 'pristine', 'V_BrS', and 'V'.

## Assets

- Bi19Br3S27 crystal structure: available from Materials Project (mp-xxxx) or ICSD (coll. code xxxxx); also given in the paper's Supporting Information
- Quantum ESPRESSO (or CP2K) DFT package: https://www.quantum-espresso.org/
- Bader charge analysis program (Henkelman group): http://theory.cm.utexas.edu/henkelman/code/bader/
- Python 3 + ASE / pymatgen + NumPy: pip install ase pymatgen numpy
- CO₂ molecular geometry

## Workflow steps

### Step 1: Slab model construction, geometry optimization, and electronic structure
- Role: process
- Action: Construct slab models for three surfaces: pristine Bi₁₉Br₃S₂₇(310), V_Br‑S‑Bi₁₉Br₃S₂₇ (dual Br-S vacancies), and O‑doped V‑Bi₁₉Br₃S₂₇ (dual vacancies plus oxygen doping), starting from the public crystal structure. Perform periodic DFT geometry optimization on each slab to obtain relaxed geometries. Optionally compute the density of states to confirm metallic character of the defective surfaces.
- Evidence: `/app/outputs/relaxed_models_info.txt`

### Step 2: CO₂ adsorption energy and Bader charge analysis
- Role: scored (load-bearing)
- Action: On each relaxed surface model, place a CO₂ molecule in a representative adsorption configuration, re‑optimize the adsorbate+slab system, and compute the adsorption energy (E_ads) and Bader charge on the adsorbed CO₂ molecule. Report the results in a CSV.
- Output file: `/app/outputs/step_02_adsorption_energies_and_charges.csv`
- Format: csv
- Contract: Columns: system (string, one of: pristine, V_BrS, V), E_ads (float, eV), Bader_charge_on_CO2 (float, e). One row per system.
- Scoring: scored by hidden verifier

### Step 3: Gibbs free energy profiles for CO₂ reduction to CH₃OH
- Role: scored (load-bearing)
- Action: On each surface model, compute the energies of all intermediates along the eight‑step CO₂→CH₃OH pathway (CO₂(gas), *CO₂, *COOH, *CO, *CHO, *CH₂O, *CH₃O, *CH₃OH, CH₃OH(gas)). Include zero‑point energy and entropic corrections to obtain Gibbs free energies. Write the free energy of each step to a CSV.
- Output file: `/app/outputs/step_03_gibbs_free_energy_profiles.csv`
- Format: csv
- Contract: Columns: system (string, one of: pristine, V_BrS, V), reaction_step (string, one of: CO2_gas, *CO2, *COOH, *CO, *CHO, *CH2O, *CH3O, *CH3OH, CH3OH_gas), free_energy (float, eV). One block per system with nine rows each.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_adsorption_energies_and_charges.csv`
- `/app/outputs/step_03_gibbs_free_energy_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_adsorption_energies_and_charges.csv
- path: `/app/outputs/step_02_adsorption_energies_and_charges.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed CO₂ adsorption energies and Bader charges on pristine, V_BrS, and V surfaces. Checked for correct relative ordering (more negative E_ads, larger charge on V) and values within tolerance using reference match.
- schema:
  - `type`: table
  - `required_columns`: `system`, `E_ads`, `Bader_charge_on_CO2`
  - `units`:
    - `E_ads`: eV
    - `Bader_charge_on_CO2`: e

### step_03_gibbs_free_energy_profiles.csv
- path: `/app/outputs/step_03_gibbs_free_energy_profiles.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Gibbs free energy of each elementary step for CO₂ reduction to CH₃OH on the three surfaces. Checked for correct barrier orderings and exothermic *CO→*CHO step on V surface, using recomputed metric scoring.
- schema:
  - `type`: table
  - `required_columns`: `system`, `reaction_step`, `free_energy`
  - `units`:
    - `free_energy`: eV

Notes: All values are computed by periodic DFT with an open-source planewave/pseudopotential code. The checker compares against hidden reference values using reference_match for step_02 and metric_recompute for step_03.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_adsorption_energies_and_charges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "E_ads",
          "Bader_charge_on_CO2"
        ],
        "units": {
          "E_ads": "eV",
          "Bader_charge_on_CO2": "e"
        }
      },
      "description": "Computed CO₂ adsorption energies and Bader charges on pristine, V_BrS, and V surfaces. Checked for correct relative ordering (more negative E_ads, larger charge on V) and values within tolerance using reference match."
    },
    {
      "file": "step_03_gibbs_free_energy_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "reaction_step",
          "free_energy"
        ],
        "units": {
          "free_energy": "eV"
        }
      },
      "description": "Gibbs free energy of each elementary step for CO₂ reduction to CH₃OH on the three surfaces. Checked for correct barrier orderings and exothermic *CO→*CHO step on V surface, using recomputed metric scoring."
    }
  ],
  "notes": "All values are computed by periodic DFT with an open-source planewave/pseudopotential code. The checker compares against hidden reference values using reference_match for step_02 and metric_recompute for step_03."
}
```

## How you are scored
A hidden verifier will independently read your two CSV artifacts and evaluate them. The verifier checks that the reported adsorption energies, Bader charges, and Gibbs free energies are physically reasonable and consistent with the DFT calculations you performed. It compares your computed quantities to scientifically derived reference expectations (based on the computational protocol) and assesses whether the relative trends among the three surfaces are correct. Merely copying numbers from a publication without running the DFT workflow will not satisfy the verification. The final reward is a weighted combination of scores from the two artifacts; higher reward indicates closer agreement with the expected results.
