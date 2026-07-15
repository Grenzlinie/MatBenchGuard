# Coverage-Dependent Linear Regression of Adsorption Energies for CO2 Reduction Selectivity Classification on Pb, Ag, and Au

## Problem background
Electrochemical CO₂ reduction (CO₂RR) is a promising route for converting CO₂ into valuable fuels and chemicals, yet density functional theory (DFT) models have historically struggled to correctly predict the product selectivity (CO vs formate vs multiple products) across different metal catalysts. A central difficulty is that most DFT studies consider a single surface coverage of the key reaction intermediates (COOHads, HCOOads, Hads) and obtain adsorption energies that appear to misclassify several metals. This reproduction task investigates whether explicitly accounting for coverage‑dependent adsorption energies — computing total adsorption energies for multiple identical adsorbates on a surface — can resolve these misclassifications. Coverage‑dependent linear regressions of total adsorption energies yield a slope (equal to the ratio of per‑adsorbate adsorption energies) and an intercept; nonzero intercepts are hypothesized to reveal systematic lateral‑interaction errors present in single‑coverage calculations, while the slope provides a descriptor for predicting the dominant two‑electron product.

## Approach
The core idea is to compute DFT total energies for metal slabs with varying numbers (n = 1–4) of identical adsorbates (HCOO, COOH, H) in a fixed supercell, perform a global structural search to find low‑energy adsorbate arrangements, and then extract total adsorption energies. From these energies, for each metal surface, two linear regressions are carried out: (i) total E_ads(HCOO) vs total E_ads(COOH) and (ii) total E_ads(COOH) vs total E_ads(H). The slope of the first regression — the HCOO:COOH adsorption energy ratio — is used to separate CO‑selective from HCOOH‑selective surfaces through a threshold of 1.65. For surfaces where the slope is below 1.65, the COOH:H slope further distinguishes single‑product (CO) from multiproduct surfaces by its sign (negative vs positive). The workflow is to be implemented using open‑source tools (ASE for structure handling and minima‑hopping global optimization, GPAW for plane‑wave DFT with a van der Waals‑inclusive functional). Gas‑phase molecular and zero‑point energy corrections are applied as specified in the method. No proprietary data or code is required; the necessary crystal structures (FCC Ag, Au, Pb) can be generated from standard bulk parameters.

## Reproduction target
Using an open‑source DFT code (GPAW), compute total adsorption energies for HCOO, COOH and H on Ag(111), Au(111) and Pb(111) at coverages of 1, 2, 3 and 4 adsorbates per 2×3 supercell, employing a global optimization (e.g., minima hopping) to locate low‑energy configurations. Apply the required zero‑point energy corrections and the fixed molecular corrections (+0.09 eV for H₂, +0.25 eV for COOHads) as per the experimental protocol. Perform linear regressions of total E_ads(HCOO) vs total E_ads(COOH) and total E_ads(COOH) vs total E_ads(H) for each metal, saving slopes and intercepts. Then classify each metal according to the scheme: if the HCOO:COOH slope > 1.65 → predict ‘HCOOH’; if < 1.65 → predict ‘CO_single’ when the COOH:H slope is negative and ‘CO_multi’ when positive. The final output must include the raw adsorption energies, the regression fits, and the classification. The checker will assess the consistency of the slopes and intercepts (ordering, nonzero intercepts) and the correctness of the classification against a hidden reference drawn from experimental selectivity; the reproduction is considered successful only if the computed quantities pass these structural and reference checks.

## Assets

- ASE (Atomic Simulation Environment): https://gitlab.com/ase/ase
- GPAW: https://wiki.fysik.dtu.dk/gpaw/
- Crystal structure data for Ag, Au, Pb

## Workflow steps

### Step 1: DFT calculations and adsorption energy computation
- Role: process
- Action: Construct 2×3×4-layer slabs of Ag(111), Au(111), and Pb(111). For each metal, run DFT total energy calculations for clean slabs, gas-phase CO₂ and H₂ references, and slabs with 1,2,3,4 identical adsorbates of HCOO, COOH, and H. Use minima hopping (or equivalent global optimizer) to find low-energy adsorbate configurations. Compute total adsorption energies including zero-point energy corrections and the standard +0.09 eV (H₂) and +0.25 eV (COOHₐₔₛ) corrections. Save all results to coverage_energies.json.
- Evidence: `/app/outputs/coverage_energies.json`

### Step 2: Linear regression of adsorption energies
- Role: scored (load-bearing)
- Action: From coverage_energies.json, for each metal perform a linear regression of total E_ads(Y) vs total E_ads(X) for the pairs (HCOO vs COOH) and (COOH vs H) using the data points for n = 1–4 (or fewer if some coverages are too packed). Extract the slope and intercept. Save the results to regression_fits.json.
- Output file: `/app/outputs/regression_fits.json`
- Format: json
- Contract: list of objects, each with: metal (string), pair (string, e.g. 'HCOO_vs_COOH', 'COOH_vs_H'), slope (float, eV/eV), intercept (float, eV)
- Scoring: scored by hidden verifier

### Step 3: Selectivity classification
- Role: scored
- Action: Using the slopes from regression_fits.json, classify each metal: if HCOO:COOH slope > 1.65 → 'HCOOH'; if < 1.65 → 'CO_single' if H:COOH slope < 0 else 'CO_multi'. Output the classification to classification_summary.json.
- Output file: `/app/outputs/classification_summary.json`
- Format: json
- Contract: list of objects, each with: metal (string), predicted_category (string, one of 'HCOOH', 'CO_single', 'CO_multi'), evidence (string describing the slope values used)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/regression_fits.json`
- `/app/outputs/classification_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### regression_fits.json
- path: `/app/outputs/regression_fits.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Slopes and intercepts from coverage-dependent linear regressions of total adsorption energies. The checker will verify relative ordering (Ag < Au < Pb for HCOO:COOH slope) and that at least two intercepts have magnitude > 0.05 eV.
- schema:
  - `type`: array
  - `items`:
    - `metal`: string
    - `pair`: string (e.g. 'HCOO_vs_COOH', 'COOH_vs_H')
    - `slope`: float (eV/eV)
    - `intercept`: float (eV)

### classification_summary.json
- path: `/app/outputs/classification_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Selectivity classification of each metal derived from the regression slopes. The checker will compare predicted categories against hidden experimental selectivity (Ag: CO_single, Au: CO_single, Pb: HCOOH).
- schema:
  - `type`: array
  - `items`:
    - `metal`: string
    - `predicted_category`: string (one of 'HCOOH', 'CO_single', 'CO_multi')
    - `evidence`: string

Notes: The DFT calculations are computationally intensive; the solving agent may need external compute resources (GPUs, multiple cores). The classification threshold (1.65) and product naming (CO_single/CO_multi) follow the paper's scheme. Regression ordering and intercept magnitude are scored via structural audit; classification accuracy is scored via reference match.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "regression_fits.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "metal": "string",
          "pair": "string (e.g. 'HCOO_vs_COOH', 'COOH_vs_H')",
          "slope": "float (eV/eV)",
          "intercept": "float (eV)"
        }
      },
      "description": "Slopes and intercepts from coverage-dependent linear regressions of total adsorption energies. The checker will verify relative ordering (Ag < Au < Pb for HCOO:COOH slope) and that at least two intercepts have magnitude > 0.05 eV."
    },
    {
      "file": "classification_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "metal": "string",
          "predicted_category": "string (one of 'HCOOH', 'CO_single', 'CO_multi')",
          "evidence": "string"
        }
      },
      "description": "Selectivity classification of each metal derived from the regression slopes. The checker will compare predicted categories against hidden experimental selectivity (Ag: CO_single, Au: CO_single, Pb: HCOOH)."
    }
  ],
  "notes": "The DFT calculations are computationally intensive; the solving agent may need external compute resources (GPUs, multiple cores). The classification threshold (1.65) and product naming (CO_single/CO_multi) follow the paper's scheme. Regression ordering and intercept magnitude are scored via structural audit; classification accuracy is scored via reference match."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently examines each output file. For regression_fits.json, the verifier performs structural checks: it verifies that the slopes for the COOH vs HCOO pair are in the expected relative order across the three metals and that at least two metals exhibit intercepts with magnitude larger than a small tolerance, demonstrating the systematic bias. For classification_summary.json, the verifier compares your predicted categories against a hidden set of known experimental selectivity labels for Ag, Au and Pb derived from the literature. The final reward is a weighted combination of these checks; reporting approximate values without having genuinely executed the DFT and regression workflows is unlikely to pass the structural and reference checks.
