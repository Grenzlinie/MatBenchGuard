# DFT Descriptor Evaluation of Ni and Co Single-Atom Sites for Electrocatalytic CO2 Reduction

## Problem background
Electrocatalytic CO₂ reduction to CO is a promising route for renewable energy storage. Bulk Ni metal is a poor CO₂RR catalyst and strongly favors the competing hydrogen evolution reaction (HER), but dispersing Ni as single atoms in nitrogen-doped graphene dramatically alters its catalytic behavior. Density functional theory (DFT) calculations can compute the CO desorption barrier and the hydrogen adsorption free energy for different single-atom sites, providing insight into the origin of this selectivity shift. In this task you will compute these catalytic descriptors for Ni and Co single-atom models embedded in graphene vacancies (with and without a neighboring nitrogen dopant) to assess how the metal identity affects the CO₂RR vs. HER selectivity.

## Approach
The catalytic descriptors are obtained from spin‑polarized DFT total‑energy calculations using the BEEF‑vdW exchange‑correlation functional. Four atomic models are built: a 7×7 graphene supercell containing either Ni or Co in a single vacancy, optionally with one neighboring N atom substituting a carbon (Ni@SV, Ni‑N@SV, Co@SV, Co‑N@SV). For each model, compute the total energies of the bare surface and of the surface with adsorbed COOH*, CO*, and H* intermediates. The computational hydrogen electrode (CHE) method relates these energies to free‑energy changes: the CO desorption barrier is obtained from the energy difference between the CO‑adsorbed state and the bare surface plus gas‑phase CO, while the HER limiting potential is derived from the H* adsorption free energy (relative to gas‑phase H₂). The workflow will be carried out with the open‑source plane‑wave code Quantum ESPRESSO and the BEEF‑vdW functional included in its libxc library.

## Reproduction target
Using Quantum ESPRESSO with the BEEF‑vdW functional, compute the total DFT energies of the bare surface and the COOH*, CO*, and H* intermediates for the four single‑atom models (Ni@SV, Ni‑N@SV, Co@SV, Co‑N@SV). From these energies, compile the structured summary `compiled_energies.json` and derive the CO desorption free‑energy barrier and the HER limiting potential for each model, saving them in `derived_barriers.json`. The final verification will check the relative ordering: for each structural pair (SV and N‑doped SV considered separately), the Ni site should exhibit a lower CO desorption barrier and a more negative (i.e., less favorable) HER limiting potential than the corresponding Co site.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BEEF-vdW exchange-correlation functional: Quantum ESPRESSO built-in (libxc)
- Ultrasoft pseudopotentials for Ni, Co, C, N, H

## Workflow steps

### Step 1: Construct atomic models of metal-doped graphene vacancies
- Role: process
- Action: Build the 7×7 graphene supercell and create four models: Ni@SV (Ni in single vacancy), Ni-N@SV (Ni in single vacancy with one neighboring N), Co@SV, Co-N@SV. Use a relaxed lattice constant or experimental graphene lattice. Save the initial structures for documentation.
- Evidence: `/app/outputs/model_coordinates.json`

### Step 2: Compute total DFT energies for surface and adsorbate states
- Role: process
- Action: For each of the four models, run spin-polarized DFT geometry optimizations and total energy calculations with Quantum ESPRESSO using the BEEF-vdW functional and appropriate cutoffs. Compute energies for the bare surface and with adsorbed COOH*, CO*, and H*. Save all raw total energies and optimized geometries for later compilation.
- Evidence: `/app/outputs/dft_energies.json`

### Step 3: Compile adsorption energies into a structured summary
- Role: scored
- Action: Post-process the DFT output to extract the total energy of each system (bare, COOH, CO, H). Apply zero-point energy and entropy corrections if desired to obtain free energies, following the computational hydrogen electrode method. Combine the results into a JSON file listing each model and its energies.
- Output file: `/app/outputs/compiled_energies.json`
- Format: json
- Contract: JSON array of objects, each with fields: model (string), site_type (string), E_bare (float, eV), E_COOH (float, eV), E_CO (float, eV), E_H (float, eV).
- Scoring: scored by hidden verifier

### Step 4: Compute CO desorption barriers and HER limiting potentials
- Role: scored (load-bearing)
- Action: Using the energies from compiled_energies.json, calculate the CO desorption free-energy barrier as the difference between the CO adsorbed state and the bare surface plus CO in gas phase (ΔG_des = E_CO - E_bare - E_CO_gas). For HER, compute the limiting potential U_L = -ΔG_H / e, where ΔG_H = E_H - E_bare - 0.5*E_H2. Apply appropriate gas-phase reference energies for CO and H2. Save the computed barriers and potentials in a JSON file.
- Output file: `/app/outputs/derived_barriers.json`
- Format: json
- Contract: JSON array of objects, each with fields: model (string), site_type (string), CO_desorption_barrier (float, eV), HER_limiting_potential (float, V vs RHE).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/compiled_energies.json`
- `/app/outputs/derived_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### compiled_energies.json
- path: `/app/outputs/compiled_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Compiled total or free energies of bare surface and adsorbed intermediates for each active site model. The checker verifies model presence and energy self-consistency.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `model`, `E_bare`, `E_COOH`, `E_CO`, `E_H`
    - `properties`:
      - `model`:
        - `type`: string
      - `site_type`:
        - `type`: string
      - `E_bare`:
        - `type`: number
        - `unit`: eV
      - `E_COOH`:
        - `type`: number
        - `unit`: eV
      - `E_CO`:
        - `type`: number
        - `unit`: eV
      - `E_H`:
        - `type`: number
        - `unit`: eV

### derived_barriers.json
- path: `/app/outputs/derived_barriers.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Derived CO desorption free-energy barriers and HER limiting potentials. The checker verifies the relative ordering (Ni sites have lower CO barriers and more negative HER potentials than Co sites) and a sign check.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `model`, `CO_desorption_barrier`, `HER_limiting_potential`
    - `properties`:
      - `model`:
        - `type`: string
      - `site_type`:
        - `type`: string
      - `CO_desorption_barrier`:
        - `type`: number
        - `unit`: eV
      - `HER_limiting_potential`:
        - `type`: number
        - `unit`: V vs RHE

Notes: Only the four single-atom models (Ni@SV, Ni-N@SV, Co@SV, Co-N@SV) are required. Double-vacancy variants are optional. The absolute DFT energies and derived barriers are not scored to exact values; the reproduction target is the correct qualitative trend between Ni and Co sites.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "compiled_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "model",
            "E_bare",
            "E_COOH",
            "E_CO",
            "E_H"
          ],
          "properties": {
            "model": {
              "type": "string"
            },
            "site_type": {
              "type": "string"
            },
            "E_bare": {
              "type": "number",
              "unit": "eV"
            },
            "E_COOH": {
              "type": "number",
              "unit": "eV"
            },
            "E_CO": {
              "type": "number",
              "unit": "eV"
            },
            "E_H": {
              "type": "number",
              "unit": "eV"
            }
          }
        }
      },
      "description": "Compiled total or free energies of bare surface and adsorbed intermediates for each active site model. The checker verifies model presence and energy self-consistency."
    },
    {
      "file": "derived_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "model",
            "CO_desorption_barrier",
            "HER_limiting_potential"
          ],
          "properties": {
            "model": {
              "type": "string"
            },
            "site_type": {
              "type": "string"
            },
            "CO_desorption_barrier": {
              "type": "number",
              "unit": "eV"
            },
            "HER_limiting_potential": {
              "type": "number",
              "unit": "V vs RHE"
            }
          }
        }
      },
      "description": "Derived CO desorption free-energy barriers and HER limiting potentials. The checker verifies the relative ordering (Ni sites have lower CO barriers and more negative HER potentials than Co sites) and a sign check."
    }
  ],
  "notes": "Only the four single-atom models (Ni@SV, Ni-N@SV, Co@SV, Co-N@SV) are required. Double-vacancy variants are optional. The absolute DFT energies and derived barriers are not scored to exact values; the reproduction target is the correct qualitative trend between Ni and Co sites."
}
```

## How you are scored
A hidden verifier will read your `compiled_energies.json` and `derived_barriers.json`. It will first confirm that all four required models are present and that the reported energies are self‑consistent. The main score is based on the relative trend: for each structural pair, the Ni site's CO desorption barrier must be lower than the Co site's, and the Ni site's HER limiting potential must be more negative than the Co site's. The exact absolute values of the barriers and potentials are not scored; only the correct sign and ordering of the differences matter. Completeness of the required files and adherence to the output format also contribute a small portion of the reward.
