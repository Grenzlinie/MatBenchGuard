# Peierls Distortion Energetics in Layered TaM2Te2 (M=Fe, Co, Ni)

## Problem background
The layered tellurides TaM2Te2 (M = Fe, Co, Ni) exhibit a Peierls-type structural distortion: TaNi2Te2 adopts an undistorted layer structure while TaCo2Te2 shows a pairing distortion that doubles the unit cell along the stacking direction. Understanding whether the distorted or undistorted motif is energetically preferred for each transition metal is central to explaining the electronic driving force behind this structural instability. Extended Hückel tight‑binding calculations on single 2D layers can be used to compute the total electronic energy of both structural variants for each metal and thereby quantify the energetic preference.

## Approach
The reproduction uses the extended Hückel tight‑binding method on single-layer (2D) models of TaM2Te2. You will construct structural models for the undistorted (high-symmetry, based on the TaNi2Te2 template) and distorted (Peierls-paired, based on the TaCo2Te2 template) geometries for M = Fe, Co, Ni by substituting the transition metal atom into the published crystal structures. Standard extended Hückel parameters for Ta, Fe, Co, Ni, and Te taken from the literature (Calhorda & Hoffmann for Ta, Ni, Fe, Co; Canadell, Mathey & Whangbo for Te) are used. For each metal and geometry, compute the total electronic energy of the layer, then calculate the energy difference between the distorted and undistorted states. The workflow consists of two stages: building the six structural models, and performing the six tight‑binding energy calculations.

## Reproduction target
Compute the energy differences ΔE(M) = E(distorted layer) − E(undistorted layer) in eV for M = Fe, Co, Ni, and write them to /app/outputs/energy_differences.json as a JSON object with keys "Fe", "Co", "Ni" and floating-point values. This file is the sole scored artifact; its contents must reflect the output of the complete tight‑binding workflow.

## Assets

- CIF files for TaNi2Te2 and TaCo2Te2: CSD-55889 (TaNi2Te2); TaCo2Te2 structure from Tremel, J. Chem. Soc. Chem. Commun. 1991, 1405
- Extended Hückel parameters for Ta, Ni, Fe, Co: 10.1021/ic00293a018
- Extended Hückel parameters for Te: 10.1021/ja00210a005
- Extended Hückel tight-binding code: https://github.com/matteoac/YAEHMOP

## Workflow steps

### Step 1: Build structural models for all six TaM2Te2 systems
- Role: process
- Action: Generate single-layer structural models for TaFe2Te2, TaCo2Te2, and TaNi2Te2 in both the undistorted (high-symmetry, analogous to TaNi2Te2) and distorted (Peierls-paired, analogous to TaCo2Te2) geometries. Use the published crystal structures of TaNi2Te2 and TaCo2Te2 as templates; substitute the metal atom appropriately to create models for all three metals. Ensure unit cell and atomic coordinates reflect the correct layer periodicity.
- Evidence: `/app/outputs/structures.json`

### Step 2: Compute total energy differences ΔE = E(distorted)-E(undistorted)
- Role: scored (load-bearing)
- Action: Perform extended Hückel tight-binding calculations on the six single-layer models from step 01. Use the standard parameter sets for Ta, Fe, Co, Ni (Calhorda & Hoffmann) and Te (Canadell et al.). For each metal M = Fe, Co, Ni, compute the total electronic energy for both the distorted and undistorted geometries, then calculate the energy difference ΔE(M) = E(distorted) - E(undistorted) in eV. Write the three differences to the output file.
- Output file: `/app/outputs/energy_differences.json`
- Format: json
- Contract: {"Fe": float (eV), "Co": float (eV), "Ni": float (eV)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_differences.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_differences.json
- path: `/app/outputs/energy_differences.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total energy differences between distorted and undistorted TaM2Te2 layers for M=Fe, Co, Ni. The checker will compare these values to hidden reference values (paper-reported) with tolerances and verify the sign pattern and relative ordering (Fe < Co < Ni).
- schema:
  - `type`: object
  - `required`:
    - `Fe`: float (eV)
    - `Co`: float (eV)
    - `Ni`: float (eV)

Notes: The DOS, COOP, and band-structure analyses are not included in the scored contract; the task focuses on the main quantitative energetic trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_differences.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Fe": "float (eV)",
          "Co": "float (eV)",
          "Ni": "float (eV)"
        }
      },
      "description": "Total energy differences between distorted and undistorted TaM2Te2 layers for M=Fe, Co, Ni. The checker will compare these values to hidden reference values (paper-reported) with tolerances and verify the sign pattern and relative ordering (Fe < Co < Ni)."
    }
  ],
  "notes": "The DOS, COOP, and band-structure analyses are not included in the scored contract; the task focuses on the main quantitative energetic trend."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads /app/outputs/energy_differences.json. The verifier checks that the file has the correct structure and contains numeric values for all three metals. The primary score is based on how closely your computed energy differences match the expected values derived from the original extended Hückel calculations, using a tolerance that accounts for implementation differences. The exact tolerance and reference values are hidden. To obtain a high reward, you must correctly execute the tight‑binding procedure; simply guessing plausible numbers is very unlikely to hit the required tolerance. No self-reported metric other than the energy differences file is scored, so a thorough re‑implementation of the computational steps is required.
