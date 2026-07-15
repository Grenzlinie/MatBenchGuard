# Periodic DFT Adsorption Energies on PdV/TiO₂(101) Surface

## Problem background
The combined catalytic removal of volatile organic compounds (VOCs) and nitrogen oxides (NOₓ) from industrial flue gases is an important environmental challenge. Recent experimental work has shown that modifying vanadia‑titania catalysts with palladium (PdₓVᵧ/TiO₂) greatly improves the simultaneous conversion of benzene and NOₓ, with the Pd₀.₁₂V₄/TiO₂ catalyst being particularly effective. First‑principles density functional theory (DFT) calculations were performed to understand the molecular origin of this enhanced activity by evaluating the adsorption energies of the key reactant gases (NH₃, benzene, O₂, NO, NO₂) on the PdV/TiO₂(101) surface. These adsorption energies quantify how strongly each gas binds to the active metal sites (V and Pd) and are central to explaining the observed catalytic performance. This task reproduces that DFT adsorption‑energy analysis.

## Approach
The task uses periodic plane‑wave DFT with the open‑source Quantum ESPRESSO suite and standard pseudopotentials from the SSSP library. A slab model of anatase‑TiO₂(101) is constructed from the public crystal structure (Materials Project mp‑390). One Pd atom and one V atom are placed on the surface to mimic the active PdOₓ/VOₓ species. The slab is fully relaxed, then the adsorption energy is computed for each gas molecule at the designated V or Pd site using the formula Eₐdₛ = E(gas+surface) – E(surface) – E(gas), where each term is obtained from a separate geometry optimization. The computed energies for nine different molecule–site combinations provide a quantitative fingerprint of the catalyst surface's reactivity.

## Reproduction target
Produce a JSON file containing the computed adsorption energies (in eV) for the following nine configurations: NH₃ adsorbed on V (nitrogen‑end), NH₃ adsorbed on Pd (nitrogen‑end), benzene adsorbed on Pd, O₂ adsorbed on V, O₂ adsorbed on Pd, NO adsorbed on V (nitrogen‑end), NO adsorbed on Pd (nitrogen‑end), NO₂ adsorbed on Pd (nitrogen‑end), and NO₂ adsorbed on Pd (oxygen‑end). The file must be written to `/app/outputs/adsorption_energies.json` and must be a JSON object with the keys `NH3_V`, `NH3_Pd`, `Benzene_Pd`, `O2_V`, `O2_Pd`, `NO_V_N`, `NO_Pd_N`, `NO2_Pd_N`, `NO2_Pd_O`, each mapping to a floating‑point number. No other files are scored.

## Assets

- Anatase-TiO₂ crystal structure: https://next-gen.materialsproject.org/materials/mp-390
- SSSP pseudopotentials library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Build and optimize PdV/TiO₂(101) slab model
- Role: process
- Action: Construct a periodic slab model of anatase-TiO₂(101) (2×2 supercell) with one Pd atom and one V atom placed on the surface as active sites (PdO_x/VO_x species), following the paper's description. Perform full geometry optimization of the slab to obtain relaxed atomic coordinates. This relaxed structure serves as the reference for all subsequent adsorption calculations.
- Evidence: `/app/outputs/slab_relaxed.xyz`

### Step 2: Compute DFT adsorption energies for gas molecules
- Role: scored (load-bearing)
- Action: For each gas molecule (NH₃, benzene, O₂, NO, NO₂), optimize the isolated molecule in a large cell and then optimize the molecule adsorbed at the specified site (V or Pd) on the relaxed slab from step 1. Calculate adsorption energy as E_ads = E(gas+surface) – E(surface) – E(gas), all taken from their respective optimized geometries. Report the energies (eV) for the nine defined site–adsorbate combinations and write them to the output file.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: JSON object with keys: NH3_V, NH3_Pd, Benzene_Pd, O2_V, O2_Pd, NO_V_N, NO_Pd_N, NO2_Pd_N, NO2_Pd_O. Each value is a float representing the adsorption energy in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file containing computed adsorption energies (eV) for NH₃, benzene, O₂, NO, and NO₂ on PdV/TiO₂(101) surface at specified sites.
- schema:
  - `type`: object
  - `required`: `NH3_V`, `NH3_Pd`, `Benzene_Pd`, `O2_V`, `O2_Pd`, `NO_V_N`, `NO_Pd_N`, `NO2_Pd_N`, `NO2_Pd_O`
  - `properties`:
    - `NH3_V`:
      - `type`: number
    - `NH3_Pd`:
      - `type`: number
    - `Benzene_Pd`:
      - `type`: number
    - `O2_V`:
      - `type`: number
    - `O2_Pd`:
      - `type`: number
    - `NO_V_N`:
      - `type`: number
    - `NO_Pd_N`:
      - `type`: number
    - `NO2_Pd_N`:
      - `type`: number
    - `NO2_Pd_O`:
      - `type`: number

Notes: The adsorbate sites and exact reference values are hidden; scoring compares each value to the paper-reported energy within a generous tolerance to absorb DFT implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "NH3_V",
          "NH3_Pd",
          "Benzene_Pd",
          "O2_V",
          "O2_Pd",
          "NO_V_N",
          "NO_Pd_N",
          "NO2_Pd_N",
          "NO2_Pd_O"
        ],
        "properties": {
          "NH3_V": {
            "type": "number"
          },
          "NH3_Pd": {
            "type": "number"
          },
          "Benzene_Pd": {
            "type": "number"
          },
          "O2_V": {
            "type": "number"
          },
          "O2_Pd": {
            "type": "number"
          },
          "NO_V_N": {
            "type": "number"
          },
          "NO_Pd_N": {
            "type": "number"
          },
          "NO2_Pd_N": {
            "type": "number"
          },
          "NO2_Pd_O": {
            "type": "number"
          }
        }
      },
      "description": "JSON file containing computed adsorption energies (eV) for NH₃, benzene, O₂, NO, and NO₂ on PdV/TiO₂(101) surface at specified sites."
    }
  ],
  "notes": "The adsorbate sites and exact reference values are hidden; scoring compares each value to the paper-reported energy within a generous tolerance to absorb DFT implementation differences."
}
```

## How you are scored
A hidden verifier reads your `adsorption_energies.json` and compares each of the nine reported energies against a set of reference values. Because the absolute adsorption energy from DFT is sensitive to the choice of exchange‑correlation functional, pseudopotential, and computational parameters, the comparison uses a tolerance that accommodates the expected spread among reasonable implementations. The total reward is the fraction of energies that fall within the tolerance range; all nine entries must be present and be valid numbers. There is no partial credit for missing or ill‑formed entries. The reference values and tolerance are hidden; the verifier only checks the final output.
