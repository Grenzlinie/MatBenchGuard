# DFT Investigation of H₂ and H₂S Adsorption on Palladium and Doped Palladium Surfaces

## Problem background
Palladium-based membranes used for hydrogen separation are susceptible to sulfur poisoning by H₂S present in syngas. Doping Pd with other metals may improve sulfur resistance while maintaining high hydrogen permeability. This task investigates, via first-principles density functional theory, how substituting a single surface Pd atom with Nb or Cu alters the adsorption of H₂ and H₂S on the Pd(111) surface, aiming to understand the mechanisms that govern binding preferences and the relative affinity of the three surfaces (pure Pd, Pd–Nb, and Pd–Cu) for these molecules.

## Approach
Use plane-wave DFT calculations with open-source pseudopotentials to model four-layer 4×4 (111) slabs of pure Pd, Pd–Nb (one surface Pd replaced by Nb), and Pd–Cu (one surface Pd replaced by Cu). Add a vacuum layer to isolate the slabs. For each surface, first relax the clean slab (fixing the bottom two layers) and compute the total energies of the isolated H₂ and H₂S gas-phase molecules. Then place dissociated H₂ at the most stable fcc–fcc site and the H₂S molecule at the bridge–fcc–top site, relax the adsorption complexes, and compute the total energies of the combined systems. The adsorption energy for H₂ is defined as half the difference between the complex energy and the sum of the clean-surface and gas-phase H₂ energies; for H₂S it is the direct difference. The workflow culminates in reporting the six adsorption energies (three surfaces × two adsorbates) and analyzing the resulting trend in H₂S binding strength.

## Reproduction target
Compute the adsorption energies (in eV) for dissociated H₂ at the fcc–fcc site and for H₂S at the bridge–fcc–top site on pure Pd(111), Pd–Nb(111), and Pd–Cu(111) surfaces. Report the six resulting values. In addition, determine whether doping with Nb or Cu leads to a consistent relative ordering of H₂S binding strengths among the three surfaces (i.e., assess which dopant binds H₂S more or less strongly compared to pure Pd and compared to the other dopant). The ordering should be monotonic; more negative adsorption energy values correspond to stronger binding.

## Assets

- Quantum ESPRESSO: Open-source plane-wave DFT code; available at https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials: Pseudopotentials for Pd, Cu, Nb, H, S; available at https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure data (Pd, Nb, Cu): Lattice constants and bulk structures from standard references (e.g., Materials Project https://materialsproject.org/)

## Workflow steps

### Step 1: Build slab models and initial adsorbate configurations
- Role: process
- Action: Construct four-layer 4x4 (111) slab models for pure Pd, Pd-Nb, and Pd-Cu surfaces, add a vacuum layer, and set up initial adsorbate positions for H2 (fcc-fcc site) and H2S (bridge-fcc-top site). Write the required input files for the plane-wave DFT code.
- Evidence: none

### Step 2: Reference DFT calculations for clean surfaces and gas-phase molecules
- Role: process
- Action: Using Quantum ESPRESSO with appropriate pseudopotentials, relax the clean Pd, Pd-Nb, and Pd-Cu slabs (fixing bottom layers) and compute their total energies. Also compute the total energies of isolated H2 and H2S molecules in the gas phase. Save the relaxed structures and total energies.
- Evidence: `/app/outputs/reference_energies.log`

### Step 3: DFT geometry optimizations of H2 and H2S adsorption complexes
- Role: process
- Action: Place dissociated H2 at the fcc-fcc site and the H2S molecule at the bridge-fcc-top site on each of the three surfaces. Perform full geometry relaxations (except the bottom two slab layers) to obtain the total energies E_surf+H2 and E_surf+H2S.
- Evidence: `/app/outputs/adsorption_energies_raw.log`

### Step 4: Calculate and export the adsorption energies
- Role: scored (load-bearing)
- Action: Using the total energies from the previous steps, compute the adsorption energies: E_ads(H2) = (E_surf+H2 - E_surf - E_H2)/2, E_ads(H2S) = E_surf+H2S - E_surf - E_H2S. Report the six values (Pd, PdNb, PdCu for both H2 and H2S) in a CSV file.
- Output file: `/app/outputs/step_01_adsorption_energies.csv`
- Format: csv
- Contract: Columns: system (string), adsorbate (string), E_ads_eV (float). Exactly six rows covering the three surface types and two adsorbates.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_adsorption_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_adsorption_energies.csv
- path: `/app/outputs/step_01_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with six rows: system (Pd, PdNb, PdCu), adsorbate (H2 or H2S), and the computed adsorption energy E_ads_eV (float). Rows must be in the order: Pd_H2, PdNb_H2, PdCu_H2, Pd_H2S, PdNb_H2S, PdCu_H2S.
- schema:
  - `type`: table
  - `required_columns`: `system`, `adsorbate`, `E_ads_eV`
  - `units`:
    - `E_ads_eV`: eV

Notes: The adsorption energies will be compared to the paper's reported values within a tolerance, and the trend for H2S binding strength (Cu < Pd < Nb, i.e., more negative means stronger binding) will also be checked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "adsorbate",
          "E_ads_eV"
        ],
        "units": {
          "E_ads_eV": "eV"
        }
      },
      "description": "CSV file with six rows: system (Pd, PdNb, PdCu), adsorbate (H2 or H2S), and the computed adsorption energy E_ads_eV (float). Rows must be in the order: Pd_H2, PdNb_H2, PdCu_H2, Pd_H2S, PdNb_H2S, PdCu_H2S."
    }
  ],
  "notes": "The adsorption energies will be compared to the paper's reported values within a tolerance, and the trend for H2S binding strength (Cu < Pd < Nb, i.e., more negative means stronger binding) will also be checked."
}
```

## How you are scored
A hidden verifier inspects your submitted `step_01_adsorption_energies.csv`. It compares each reported adsorption energy against independently obtained reference values (hidden) within a tolerance that accounts for legitimate differences between DFT codes. The H₂ and H₂S energies are weighted roughly equally. For H₂S, the verifier additionally checks that the three values exhibit a physically consistent monotonic trend across the pure-Pd and doped surfaces (more negative means stronger binding); a correct ordering combined with values within tolerance earns full credit for that part. The total reward is the weighted sum; meeting or exceeding the reference quality never penalizes you.
