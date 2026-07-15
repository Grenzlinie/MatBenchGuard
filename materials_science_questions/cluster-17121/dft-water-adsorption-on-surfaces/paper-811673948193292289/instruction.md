# DFT Adsorption Energies and Gaps for H₂O and NH₃ on ZnO Nanostructures

## Problem background
Zinc oxide (ZnO) nanostructures are promising gas-sensing materials because of their high surface-to-volume ratio and strong dependence of electrical conductance on adsorbate binding. This study investigates the adsorption of water (H₂O) and ammonia (NH₃) molecules on hydrogen-terminated ZnO nanoclusters — aromatic-like (AL-ZnONC, Zn₃O₃H₆), naphthalene-like (NLL-ZnONC, Zn₅O₅H₈), pyrene-like (PRL-ZnONC, Zn₈O₈H₁₀) — and on graphene-like ZnO nanosheets — coronene-like (CNL-ZnONS, Zn₁₂O₁₂H₁₂) and circumcoronene-like (CCL-ZnONS, Zn₂₇O₂₇H₁₈). The key quantities that govern sensor performance are the adsorption energies of the molecules and the changes they induce in the electronic structure, quantified by the HOMO-LUMO energy gap. This task reproduces those adsorption energies and gaps for all distinct adsorption configurations on each substrate.

## Approach
The calculations are performed at the B3LYP/LanL2DZ level of density functional theory. 
First, atomistic models of the five bare ZnO substrates are built from their known chemical formulas and symmetries, with hydrogen termination at the edges. The isolated H₂O and NH₃ molecules are constructed separately. Full geometry optimizations are carried out for every bare substrate and for each isolated adsorbate.

Next, for each ZnO model, all symmetry-distinct initial adsorption orientations of H₂O and NH₃ are generated. The H₂O molecule is placed with its oxygen atom pointing toward a surface Zn site, while its hydrogen atoms are oriented toward surface oxygen or hydride hydrogen atoms; NH₃ is placed with its nitrogen atom directed toward a surface Zn site and its hydrogen atoms staggered or eclipsed relative to the underlying Zn–O bonds, as appropriate. Every initial adsorption complex is then fully geometry optimized.

Finally, the total electronic energies of all optimized structures (bare substrates, isolated molecules, and adsorption complexes) are extracted. Adsorption energies ΔE_ads are computed as  
ΔE_ads = E_complex − (E_adsorbate + E_substrate),  
and HOMO-LUMO energy gaps ΔE_GAP are obtained from the frontier orbital eigenvalues of each bare substrate and each adsorption complex. All results are collected into a single structured CSV file.

## Reproduction target
Produce, at the B3LYP/LanL2DZ level, the adsorption energies (ΔE_ads in kcal/mol) and HOMO-LUMO energy gaps (ΔE_GAP in eV) for all bare ZnO models and for every distinct energy-minimum adsorption configuration of H₂O and NH₃ on each model.  

Assemble the results in a single CSV file (`adsorption_energies.csv`) with columns: `model` (one of AL-ZnONC, NLL-ZnONC, PRL-ZnONC, CNL-ZnONS, CCL-ZnONS), `adsorbate` (bare, H₂O, or NH₃), `configuration_id` (e.g., #1, #2; empty for bare), `delta_E_ads_kcalmol` (the adsorption energy; NaN for bare rows), and `delta_E_GAP_eV` (the HOMO-LUMO gap).  

The number of H₂O and NH₃ configurations must match the following:  
- AL-ZnONC: 1 H₂O, 1 NH₃  
- NLL-ZnONC: 3 each  
- PRL-ZnONC: 6 each  
- CNL-ZnONS: 6 H₂O, 3 NH₃  
- CCL-ZnONS: 11 H₂O, 6 NH₃  

All adsorption energies must be ≤ 0, and all energy gaps must be ≥ 0.

## Assets

- ORCA quantum chemistry package (>=5.0): https://orcaforum.kofo.mpg.de

## Workflow steps

### Step 1: Build initial molecular models
- Role: process
- Action: Construct initial atomic coordinates for the five hydrogen-terminated ZnO models (AL-ZnONC Zn₃O₃H₆, NLL-ZnONC Zn₅O₅H₈, PRL-ZnONC Zn₈O₈H₁₀, CNL-ZnONS Zn₁₂O₁₂H₁₂, CCL-ZnONS Zn₂₇O₂₇H₁₈) and isolated H₂O and NH₃ molecules. Use standard bonding topologies for the graphene-like ZnO sheets with hydrogen termination at edges.
- Evidence: none

### Step 2: DFT geometry optimization of bare substrates and isolated adsorbates
- Role: process
- Action: Perform B3LYP/LanL2DZ full geometry optimizations for each bare ZnO model (AL-ZnONC, NLL-ZnONC, PRL-ZnONC, CNL-ZnONS, CCL-ZnONS) and for isolated H₂O and NH₃. Converge structures to local minima.
- Evidence: none

### Step 3: Generate and optimize all adsorption configurations
- Role: process
- Action: For each ZnO model, generate all symmetry-distinct initial adsorption orientations of H₂O and NH₃ by placing the molecule with oxygen/nitrogen toward Zn surface atoms and hydrogen atoms toward surface O or hydride H atoms. Perform B3LYP/LanL2DZ geometry optimizations for every resulting complex to obtain final minimum-energy adsorption complexes.
- Evidence: none

### Step 4: Compute adsorption energies and energy gaps, output CSV
- Role: scored (load-bearing)
- Action: Extract the total electronic energies from all optimized structures (bare substrates, isolated adsorbates, adsorption complexes). Calculate adsorption energies ΔE_ads = E_complex − (E_adsorbate + E_substrate) for H₂O and NH₃ configurations. Compute HOMO-LUMO energy gaps (ΔE_GAP) for every bare substrate and every adsorption complex. Assemble all results into a single CSV file.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: Columns: model (string, one of AL-ZnONC, NLL-ZnONC, PRL-ZnONC, CNL-ZnONS, CCL-ZnONS), adsorbate (string: 'bare', 'H2O', 'NH3'), configuration_id (string, e.g. '#1','#2'; empty for bare), delta_E_ads_kcalmol (float, NaN for bare), delta_E_GAP_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies and HOMO-LUMO gaps for bare ZnO models, H₂O adsorption minima, and NH₃ adsorption minima computed at B3LYP/LanL2DZ level. Bare rows have adsorbate='bare', configuration_id empty, delta_E_ads_kcalmol=NaN.
- schema:
  - `type`: table
  - `required_columns`: `model`, `adsorbate`, `configuration_id`, `delta_E_ads_kcalmol`, `delta_E_GAP_eV`
  - `units`:
    - `delta_E_ads_kcalmol`: kcal/mol
    - `delta_E_GAP_eV`: eV

Notes: The number of rows per model/adsorbate must match the paper's described distinct configurations: AL-ZnONC: 1 H₂O, 1 NH₃; NLL-ZnONC: 3 each; PRL-ZnONC: 6 each; CNL-ZnONS: 6 H₂O, 3 NH₃; CCL-ZnONS: 11 H₂O, 6 NH₃. All delta_E_ads_kcalmol must be ≤0 and delta_E_GAP_eV ≥0.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "adsorbate",
          "configuration_id",
          "delta_E_ads_kcalmol",
          "delta_E_GAP_eV"
        ],
        "units": {
          "delta_E_ads_kcalmol": "kcal/mol",
          "delta_E_GAP_eV": "eV"
        }
      },
      "description": "Adsorption energies and HOMO-LUMO gaps for bare ZnO models, H₂O adsorption minima, and NH₃ adsorption minima computed at B3LYP/LanL2DZ level. Bare rows have adsorbate='bare', configuration_id empty, delta_E_ads_kcalmol=NaN."
    }
  ],
  "notes": "The number of rows per model/adsorbate must match the paper's described distinct configurations: AL-ZnONC: 1 H₂O, 1 NH₃; NLL-ZnONC: 3 each; PRL-ZnONC: 6 each; CNL-ZnONS: 6 H₂O, 3 NH₃; CCL-ZnONS: 11 H₂O, 6 NH₃. All delta_E_ads_kcalmol must be ≤0 and delta_E_GAP_eV ≥0."
}
```

## How you are scored
A hidden verifier reads your `adsorption_energies.csv`. It compares each adsorption energy (ΔE_ads) and HOMO-LUMO gap (ΔE_GAP) against reference values derived from the literature using pre-defined tolerances. It also checks that the number of rows per model–adsorbate combination exactly matches the configuration counts listed above, that the strongest (most negative) adsorption energy per model is correctly identified, and that the relative energetic ordering of adsorption sites is consistent with the reference. Additionally, all values must satisfy physical bounds (ΔE_ads ≤ 0 and ΔE_GAP ≥ 0). Each workflow stage contributes a weighted fraction to the final reward; simply reporting numbers without executing the DFT geometry optimizations will not produce the correct values.
