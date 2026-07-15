# Site-Dependent Hydrogen Adsorption Free Energy from DFT Calculations

## Problem background
Electrocatalytic hydrogen evolution reaction (HER) via water splitting is a key route for sustainable hydrogen production. Metal-free catalysts are highly desirable but often suffer from limited activity. Covalent organic frameworks (COFs) are porous crystalline materials with large surface areas, tunable structures, and extended π-conjugation, making them promising electrocatalysts. A newly synthesized triazine-based 2D COF (C6-TRZ-TFP) has been shown to catalyze HER in acidic medium. Density functional theory (DFT) calculations were employed to understand the catalytic mechanism: the hydrogen adsorption free energy (ΔG_H*) and the charge occupancy on carbon atoms are used to assess the relative activity of different carbon sites in the COF. This task focuses on the DFT analysis; you will compute the site-dependent ΔG_H* and charge occupancy for the six inequivalent carbon adsorption sites in the C6-TRZ-TFP structure to determine which sites are more favorable for HER.

## Approach
You will employ plane-wave density functional theory (DFT) using the Perdew–Burke–Ernzerhof (PBE) functional to model the C6-TRZ-TFP COF slab. The procedure is as follows:

1. **Construct the structure**: Build the 3D periodic crystal structure from the published atomic coordinates and lattice parameters (trigonal P3 space group, eclipsed AA stacking) obtained from the supporting information of the original publication.
2. **Identify adsorption sites**: Mark the six inequivalent carbon atoms (sites 1–6) that serve as H* adsorption centers.
3. **Pristine slab relaxation**: Perform a full geometry optimization of the clean COF slab to obtain the reference total energy and equilibrium positions.
4. **H-adsorbed slab relaxations**: For each of the six carbon sites, place a hydrogen atom above the site and relax the slab+adsorbate system, allowing structural buckling. Record the final total energies and geometries.
5. **Vibrational analysis**: Compute vibrational frequencies for each optimized H-adsorbed structure to obtain zero-point energy (ZPE) and vibrational entropy corrections.
6. **Free energy calculation**: For each site, calculate ΔG_H* = E(COF+H) – E(COF) – ½ E(H₂) + ΔZPE – TΔS, using DFT total energies, ZPE/entropy corrections, and the computed energy of gas-phase H₂.
7. **Charge occupancy extraction**: From the electronic structure of the H-adsorbed configurations, extract the σ and π charge occupancy on each adsorption carbon site.

You will compare the computed ΔG_H* across the six sites and relate them to the charge occupancy (electron-deficient vs. electron-rich character). The final outputs are the site-resolved free energies and charge occupancy values, as detailed in the workflow steps.

## Reproduction target
Produce the following two artifacts from your DFT workflow:

1. **Hydrogen adsorption free energies**: A JSON file mapping each of the six carbon sites (site1 through site6) to its computed ΔG_H* value (in eV).
2. **Charge occupancy**: A JSON file mapping each site to an object containing the `sigma` and `pi` charge occupancy (in electrons).

The objective is to obtain these numbers by executing the DFT protocol described in the workflow steps. The verifier will compare your reported values against hidden reference data and expected trends among the sites. You must submit both files exactly as specified in the output contract.

## Assets

- Crystal structure coordinates for C6-TRZ-TFP COF (Table S1 of supporting information): Available from the supporting information of the original publication (DOI: 10.1002/cssc.202101663)
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE efficiency): https://www.materialscloud.org/discover/sssp/table/pbe/efficiency
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Construct crystal structure and identify adsorption sites
- Role: process
- Action: Build the 3D periodic crystal structure of C6-TRZ-TFP COF using the published atomic coordinates and lattice parameters (trigonal P3 space group, a=b=41.6441 Å, c=3.4915 Å, γ=120°) from the PDF/Material. Use the eclipsed AA stacking model. Identify the six inequivalent carbon atoms as adsorption sites for hydrogen.
- Evidence: `/app/outputs/model_setup.log`

### Step 2: DFT geometry optimization of pristine COF slab
- Role: process
- Action: Perform a full geometry relaxation of the pristine (no adsorbate) COF slab using DFT to obtain the reference total energy and equilibrium atomic positions.
- Evidence: `/app/outputs/pristine_relaxed.log`

### Step 3: DFT geometry optimization of H-adsorbed structures
- Role: process
- Action: For each of the six carbon sites, place a hydrogen atom above the site and perform a full geometry relaxation of the slab+adsorbate system, allowing structural buckling. Record the optimized geometries and total DFT energies.
- Evidence: `/app/outputs/H_ads_opt.log`

### Step 4: Vibrational frequency calculations
- Role: process
- Action: Compute vibrational frequencies for each optimized H-adsorbed structure to extract zero-point energy (ZPE) and vibrational entropy corrections required for free energy evaluation.
- Evidence: `/app/outputs/vibrations.log`

### Step 5: Calculate hydrogen adsorption free energies ΔG_H*
- Role: scored (load-bearing)
- Action: Compute ΔG_H* for each site using the standard formula ΔG_H* = E(COF+H) - E(COF) - 0.5*E(H2) + ΔZPE - TΔS, where E(COF+H) and E(COF) are DFT total energies, E(H2) is the DFT energy of gas-phase H2, and ΔZPE and TΔS include vibrational corrections and standard gas-phase H2 entropy. Report the six values in a JSON file.
- Output file: `/app/outputs/step_01_adsorption_free_energies.json`
- Format: json
- Contract: {"site1": <float>, "site2": <float>, "site3": <float>, "site4": <float>, "site5": <float>, "site6": <float>}
- Scoring: scored by hidden verifier

### Step 6: Compute electronic charge occupancy on active sites
- Role: scored (load-bearing)
- Action: From the DFT electronic structure of the H-adsorbed optimized structures, extract the total charge occupancy (σ + π) and separate σ and π contributions on each adsorption carbon site. Report them in a JSON file.
- Output file: `/app/outputs/step_02_charge_occupancy.json`
- Format: json
- Contract: {"site1": {"sigma": <float>, "pi": <float>}, "site2": {"sigma": <float>, "pi": <float>}, "site3": {"sigma": <float>, "pi": <float>}, "site4": {"sigma": <float>, "pi": <float>}, "site5": {"sigma": <float>, "pi": <float>}, "site6": {"sigma": <float>, "pi": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_adsorption_free_energies.json`
- `/app/outputs/step_02_charge_occupancy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_adsorption_free_energies.json
- path: `/app/outputs/step_01_adsorption_free_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Map from site label to the computed hydrogen adsorption free energy ΔG_H* in eV.
- schema:
  - `type`: object
  - `required`:
    - `site1`: float (eV)
    - `site2`: float (eV)
    - `site3`: float (eV)
    - `site4`: float (eV)
    - `site5`: float (eV)
    - `site6`: float (eV)

### step_02_charge_occupancy.json
- path: `/app/outputs/step_02_charge_occupancy.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Per-site σ and π charge occupancy (in electrons). The electron‑deficient vs electron‑rich character is judged by comparing total charge (σ+π).
- schema:
  - `type`: object
  - `required`:
    - `site1`: object
    - `site2`: object
    - `site3`: object
    - `site4`: object
    - `site5`: object
    - `site6`: object
  - `item_schema`:
    - `sigma`: float
    - `pi`: float

Notes: The agent must compute both artifacts from first‑principles DFT runs. No gold values are disclosed; the hidden verifier compares against paper‑reported numbers and structural trends (site ordering).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_adsorption_free_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "site1": "float (eV)",
          "site2": "float (eV)",
          "site3": "float (eV)",
          "site4": "float (eV)",
          "site5": "float (eV)",
          "site6": "float (eV)"
        }
      },
      "description": "Map from site label to the computed hydrogen adsorption free energy ΔG_H* in eV."
    },
    {
      "file": "step_02_charge_occupancy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "site1": "object",
          "site2": "object",
          "site3": "object",
          "site4": "object",
          "site5": "object",
          "site6": "object"
        },
        "item_schema": {
          "sigma": "float",
          "pi": "float"
        }
      },
      "description": "Per-site σ and π charge occupancy (in electrons). The electron‑deficient vs electron‑rich character is judged by comparing total charge (σ+π)."
    }
  ],
  "notes": "The agent must compute both artifacts from first‑principles DFT runs. No gold values are disclosed; the hidden verifier compares against paper‑reported numbers and structural trends (site ordering)."
}
```

## How you are scored
The hidden verifier will score each of the two load-bearing artifacts (adsorption free energies and charge occupancy) independently. For each artifact, the verifier compares your reported values against a hidden reference (the expected computed values) and checks structural patterns (e.g., the relative ordering of ΔG_H* among the sites and the correlation between electron deficiency and free energy). Scoring is based on how closely your results match the reference, with a tolerance that accounts for legitimate variations due to different computational settings (convergence, pseudopotential choice, etc.). Each artifact’s score is a number between 0 and 1, and the final reward is a weighted sum of these scores (adsorption free energies carry higher weight). To achieve a high score, your DFT calculations must be performed correctly, and the output files must contain the exact keys and formats specified. Merely guessing or reporting arbitrary values will not pass the verifier’s checks.
