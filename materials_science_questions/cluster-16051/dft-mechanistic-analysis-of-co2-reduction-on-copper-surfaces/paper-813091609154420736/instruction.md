# DFT Analysis of Cation Effects on CO Reduction Intermediates on Cu(100)

## Problem background
Electrochemical reduction of carbon monoxide (CO) on copper electrodes produces methane (C1) and ethylene (C2), but the selectivity between these products is known to depend on the electrode surface structure and on the identity of the alkali cation present in the electrolyte. The origin of this cation effect remains debated. Density functional theory (DFT) calculations that explicitly include alkali cations near adsorbed intermediates on Cu(100) can provide energetic insight: they allow a direct comparison of the reaction energies of key hydrogenation steps in the C1 and C2 pathways, both in vacuum and with different cations.

## Approach
The reproduction follows a first-principles protocol. A periodic Cu(100) slab model is built (surface unit cell and number of atomic layers as given in the workflow) with the bottom layers fixed. The intermediates *CO, *CHO, *OCCO, and *OCCOH are placed at plausible adsorption sites. For the cation-containing runs, one explicit Li⁺, Na⁺, or Cs⁺ ion is introduced near the oxygen atom(s) of the adsorbate to mimic the electrochemical double layer. Total energies of all configurations (bare slab, slab+adsorbates, slab+adsorbates+cation) and of gas-phase H₂ are computed with the PBE exchange-correlation functional. From these, adsorption energies are derived using CO(g) as a reference. Reaction energies for the C1 (*CO → *CHO) and C2 (2*CO → *OCCOH) hydrogenation steps are then calculated via the computational hydrogen electrode, using the energy of gas-phase H₂. The results are evaluated both in vacuum and after averaging over the three cations. Finally, the cation-induced shifts in the adsorption energies of the *OCCO, 2*CO, and *OCCOH intermediates are extracted.

## Reproduction target
Compute the reaction energies for the first hydrogenation steps on Cu(100):
- C1: *CO + H⁺ + e⁻ → *CHO
- C2: 2*CO + H⁺ + e⁻ → *OCCOH
both in vacuum and averaged over the three alkali cations (Li⁺, Na⁺, Cs⁺). Additionally, compute the cation-induced adsorption energy shift for each of the intermediates *OCCO, 2*CO, and *OCCOH, defined as the difference between the adsorption energy with the cation present (averaged over the three cations) and the adsorption energy in vacuum. Report all seven values (in eV) in the file `/app/outputs/computed_energies.json` exactly as specified in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotential library (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build atomic models
- Role: process
- Action: Construct all required input geometries: Cu(100) slab (3×3 surface unit cell, 4 atomic layers, bottom two layers fixed), with adsorbed species *CO, *CHO, *OCCO, *OCCOH on their stable sites. For cation-containing calculations, place one explicit Li⁺, Na⁺, or Cs⁺ near the oxygen atom(s) of the adsorbate at the electrochemical double layer. Prepare input files for all combinations.
- Evidence: `/app/outputs/structures.txt`

### Step 2: DFT total energy calculations
- Role: process
- Action: Perform total energy calculations using Quantum ESPRESSO with the PBE exchange‑correlation functional and SSSP efficiency pseudopotentials. Run for: clean Cu(100) slab; slab+CO (monomer), slab+CHO, slab+2CO, slab+OCCO, slab+OCCOH; the same adsorbate systems with an explicit Li⁺, Na⁺, and Cs⁺; and gas‑phase H₂. Save total energies.
- Evidence: `/app/outputs/dft_energies.csv`

### Step 3: Compute adsorption energies
- Role: process
- Action: Calculate adsorption energies: E_ads = E(slab+adsorbate) – E(clean slab) – n * E(CO_gas) for all intermediates (with and without cations). Save per‑configuration adsorption energies.
- Evidence: `/app/outputs/adsorption_energies.csv`

### Step 4: Compute reaction energies and cation shifts
- Role: scored (load-bearing)
- Action: From the adsorption energies and the gas‑phase H₂ reference, compute reaction energies ΔE using the computational hydrogen electrode: ΔE(C1) = E_ads(*CHO) – E_ads(*CO) + E(H₂)/2, and ΔE(C2) = E_ads(*OCCOH) – E_ads(2*CO) + E(H₂)/2. Calculate values for vacuum and for each cation, then average the cation results to obtain C1_with_cations and C2_with_cations. Also compute the cation‑induced adsorption energy shifts ΔΔE_ads = E_ads(with cation) – E_ads(vacuum) for *OCCO, 2*CO, and *OCCOH, averaging over the three cations. Write all seven values in eV to the output file.
- Output file: `/app/outputs/computed_energies.json`
- Format: json
- Contract: {"type": "object", "properties": {"C1_vacuum_eV": {"type": "number"}, "C2_vacuum_eV": {"type": "number"}, "C1_with_cations_eV": {"type": "number"}, "C2_with_cations_eV": {"type": "number"}, "OCCO_adsorption_shift_eV": {"type": "number"}, "2CO_adsorption_shift_eV": {"type": "number"}, "OCCOH_adsorption_shift_eV": {"type": "number"}}, "required": ["C1_vacuum_eV", "C2_vacuum_eV", "C1_with_cations_eV", "C2_with_cations_eV", "OCCO_adsorption_shift_eV", "2CO_adsorption_shift_eV", "OCCOH_adsorption_shift_eV"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_energies.json
- path: `/app/outputs/computed_energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Headline DFT reaction energies and cation-induced adsorption energy shifts on Cu(100) for CO reduction intermediates.
- schema:
  - `type`: object
  - `properties`:
    - `C1_vacuum_eV`:
      - `type`: number
    - `C2_vacuum_eV`:
      - `type`: number
    - `C1_with_cations_eV`:
      - `type`: number
    - `C2_with_cations_eV`:
      - `type`: number
    - `OCCO_adsorption_shift_eV`:
      - `type`: number
    - `2CO_adsorption_shift_eV`:
      - `type`: number
    - `OCCOH_adsorption_shift_eV`:
      - `type`: number
  - `required`: `C1_vacuum_eV`, `C2_vacuum_eV`, `C1_with_cations_eV`, `C2_with_cations_eV`, `OCCO_adsorption_shift_eV`, `2CO_adsorption_shift_eV`, `OCCOH_adsorption_shift_eV`

Notes: Scoring compares each value to a hidden gold threshold (meeting or beating the reference) and verifies the relative energetic ordering: C2_with_cations < C1_with_cations < C1_vacuum ≈ C2_vacuum, and |OCCO_shift| > |OCCOH_shift| > |2CO_shift|.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "properties": {
          "C1_vacuum_eV": {
            "type": "number"
          },
          "C2_vacuum_eV": {
            "type": "number"
          },
          "C1_with_cations_eV": {
            "type": "number"
          },
          "C2_with_cations_eV": {
            "type": "number"
          },
          "OCCO_adsorption_shift_eV": {
            "type": "number"
          },
          "2CO_adsorption_shift_eV": {
            "type": "number"
          },
          "OCCOH_adsorption_shift_eV": {
            "type": "number"
          }
        },
        "required": [
          "C1_vacuum_eV",
          "C2_vacuum_eV",
          "C1_with_cations_eV",
          "C2_with_cations_eV",
          "OCCO_adsorption_shift_eV",
          "2CO_adsorption_shift_eV",
          "OCCOH_adsorption_shift_eV"
        ]
      },
      "description": "Headline DFT reaction energies and cation-induced adsorption energy shifts on Cu(100) for CO reduction intermediates."
    }
  ],
  "notes": "Scoring compares each value to a hidden gold threshold (meeting or beating the reference) and verifies the relative energetic ordering: C2_with_cations < C1_with_cations < C1_vacuum ≈ C2_vacuum, and |OCCO_shift| > |OCCOH_shift| > |2CO_shift|."
}
```

## How you are scored
Your `computed_energies.json` will be evaluated by a hidden verifier. It compares each of the seven values against a reference that accounts for the spread expected when different DFT implementations and pseudopotentials are used; you earn full credit when your numbers agree with the reference within the allowed tolerance. In addition, the verifier checks whether the internal relationships between the seven numbers are physically consistent. The final reward is a weighted combination of the individual value accuracies and the structural consistency checks.
