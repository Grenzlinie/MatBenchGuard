## Problem background

Phloroglucinol (1,3,5-trihydroxybenzene) is a biomass-derived oxygenated aromatic that can be catalytically upgraded on noble metals for renewable chemicals. Understanding its adsorption behaviour on catalytic surfaces is essential for designing hydrogenation and deoxygenation processes. This task uses density functional theory (DFT) to address three interconnected questions:
- Which adsorption sites are preferred on Pt(111) and Pd(111) surfaces?
- How does the molecule’s structure and the metal surface distort upon strong binding?
- How does liquid water (the solvent) modify the binding energy and geometry?

## Approach

Use DFT calculations with the PW91 generalized gradient approximation (GGA) functional, implemented in the open‑source Quantum ESPRESSO suite. Model the Pt(111) and Pd(111) surfaces as four‑layer slabs with vacuum. Generate a systematic set of initial adsorption configurations by varying the adsorption site (bridge, fcc hollow, hcp hollow, atop), the orientation of the aromatic ring, the placement of the OH groups, and the two configurational isomers of phloroglucinol. Relax all configurations and compute gas‑phase adsorption energies from total‑energy differences. From the most stable bridge‑site configuration on each metal, extract a comprehensive set of geometric parameters (bond lengths, adsorption heights, metal displacements, angles). To investigate solvent effects, perform ab‑initio molecular dynamics with explicit water molecules at liquid density for the most stable configurations, thermalize at 300 K, quench to 0 K, and compute the 0 K aqueous‑phase adsorption energy and the corresponding structural parameters. Compare the aqueous‑phase results with the gas‑phase results to assess the solvent‑induced weakening of binding.

## Reproduction target

You must compute and report:
1. The gas‑phase adsorption energies (E_ad_vac, in eV) for all stable configurations on Pt(111) and Pd(111).
2. The geometric parameters of the most stable bridge‑site adsorbed state (distances in Å, angles in degrees) for each metal, extracted from the relaxed gas‑phase structures.
3. The 0 K aqueous‑phase adsorption energy and the same geometric parameters for the same most stable bridge‑site configurations, obtained after quenching the water‑containing system from 300 K.
The hidden verifier will compare your computed values to reference values with appropriate tolerances that absorb legitimate implementation‑choice spread. The targets are the quantities themselves, not a specific table number; you must perform the full workflow from scratch.

## Assets

The following public resources are required. You are expected to fetch them yourself; exact versions are left to your best judgement for the PW91 functional.

- **Quantum ESPRESSO** (open‑source DFT code) – https://www.quantum-espresso.org/
- **PW91 pseudopotentials** for Pt, Pd, C, O, H (e.g., SSSP library or PseudoDojo) – https://www.quantum-espresso.org/pseudopotentials/
- **Pt bulk structure** (fcc, lattice constant 3.92 Å) – e.g., Materials Project mp‑126 (https://materialsproject.org/materials/mp-126/)
- **Pd bulk structure** (fcc, lattice constant 3.89 Å) – e.g., Materials Project mp‑2 (https://materialsproject.org/materials/mp-2/)
- **Phloroglucinol molecule** (isolated geometry) – e.g., PubChem CID 3593 (https://pubchem.ncbi.nlm.nih.gov/compound/3593)
- Water molecule (standard geometry, use your own source or build from the O–H bond length and angle)

## Workflow steps

### Step 1: Data preparation and structure generation
- Role: process
- Action: Build Pt(111) and Pd(111) four‑layer slabs with vacuum (choose a sufficiently large surface cell). Construct the phloroglucinol molecule. Generate the complete set of initial adsorption configurations by combining all adsorption sites (bridge, fcc hollow, hcp hollow, atop), both orientations of the aromatic ring (A = C–C bond perpendicular to the direction of the bridge, B = parallel), both OH placements (1 = on hollow, 2 = on atop), and the two configurational isomers (I and II). This yields 20 starting geometries per metal surface. Use a systematic naming convention for each configuration: Isomer‑Site‑Orientation‑OHplacement, where Isomer is I or II, Site is Bri, Fcc, Hcp, or Atop, Orientation is A or B, and OHplacement is 1 or 2 (e.g., II‑Bri‑A1).
- Evidence: `/app/outputs/config_list.txt` (a plain text list of configuration names)

### Step 2: Gas‑phase DFT relaxations and adsorption energies
- Role: scored
- Action: Perform DFT geometry relaxations for all 20 configurations on each metal surface using the PW91 functional. For each relaxed structure that is stably adsorbed (negative adsorption energy), compute E_ad,vac = E(slab+molecule) – E(molecule) – E(slab). Report the stable configurations and their adsorption energies.
- Output file: `/app/outputs/step_01_adsorption_energies_gas.json`
- Format: json
- Contract: A JSON array of objects, each with:
  - `metal` (string, "Pt" or "Pd")
  - `configuration_name` (string, using the naming convention from Step 1, e.g., "II-Bri-A1")
  - `E_ad_vac` (number, in eV)
  The array must include every configuration that yielded a negative adsorption energy from your DFT relaxations.
- Scoring: scored by hidden verifier

### Step 3: Gas‑phase structural parameters extraction
- Role: scored
- Action: From the relaxed structures of the most stable adsorbed configuration on each metal (the one with the most negative E_ad_vac from Step 2), extract the geometric parameters that characterise the distortion of the molecule and the metal surface. Specifically, measure: d_zmin, d_zavg (adsorption heights), r_C1, r_C2 (selected C–C bond lengths), r_M1, r_M2 (relevant metal–metal distances), r_CM1, r_CM2, r_CM3 (metal–carbon distances), and the angles θ1, θ2, α (C–C–H), β (C–C–O). All parameters are defined analogously to those illustrated in Figure 3b of the original study.
- Output file: `/app/outputs/step_02_structural_params_gas.json`
- Format: json
- Contract: A JSON object with top‑level keys "Pt" and "Pd". Each value is an object containing the following numeric fields (all distances in Å, all angles in degrees): d_zmin, d_zavg, r_C1, r_C2, r_M1, r_M2, r_CM1, r_CM2, r_CM3, theta1, theta2, alpha, beta.
- Scoring: scored by hidden verifier

### Step 4: Aqueous‑phase ab‑initio molecular dynamics
- Role: process
- Action: For the most stable bridge‑site configurations on Pt(111) and Pd(111), construct a simulation cell with explicit water molecules at a density of 0.86 g/cm³. Place phloroglucinol adsorbed symmetrically on both sides of the slab. Run NVT molecular dynamics at 300 K to thermalise the system, then quench over ~700 fs to 0 K. The DFT settings (functional, cutoff) may be reduced for efficiency, but maintain consistency with the gas‑phase study. Keep a log of the simulation (including final energies and convergence).
- Evidence: `/app/outputs/md_simulation.log`

### Step 5: Aqueous‑phase 0 K results
- Role: scored (load‑bearing)
- Action: For the most stable adsorbed configuration on each metal (identified in Step 2 and used in Step 4), from the quenched aqueous configurations compute the 0 K aqueous‑phase adsorption energy E_ad,aquo,0K as the difference between the total energy of the adsorbed system and that of the detached reference state (molecule + water + slab). Also extract the same 13 geometric parameters listed in Step 3 from the quenched structure. Report these for each metal.
- Output file: `/app/outputs/step_03_aqueous_0K_results.json`
- Format: json
- Contract: A JSON object with top‑level keys "Pt" and "Pd". Each value is an object containing the field `E_ad_aquo_0K` (eV) and the same 13 structural parameters (d_zmin, d_zavg, … beta) as in Step 3. All distances in Å, all angles in degrees.
- Scoring: scored by hidden verifier

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_adsorption_energies_gas.json
- path: `/app/outputs/step_01_adsorption_energies_gas.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Gas-phase adsorption energies for all stable configurations on Pt(111) and Pd(111).
- schema:
  - `type`: array
  - `items`:
    - `metal`: string
    - `configuration_name`: string
    - `E_ad_vac`: number (eV)
  - `description`: Array of objects; must contain every configuration that yielded a negative adsorption energy from the DFT relaxations.

### step_02_structural_params_gas.json
- path: `/app/outputs/step_02_structural_params_gas.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Gas-phase structural parameters for the most stable bridge-site configurations on Pt and Pd.
- schema:
  - `type`: object
  - `required`: `Pt`, `Pd`
  - `properties`:
    - `Pt`:
      - `type`: object
      - `required`: `d_zmin`, `d_zavg`, `r_C1`, `r_C2`, `r_M1`, `r_M2`, `r_CM1`, `r_CM2`, `r_CM3`, `theta1`, `theta2`, `alpha`, `beta`
      - `units`:
        - `d_zmin`: Å
        - `d_zavg`: Å
        - `r_C1`: Å
        - `r_C2`: Å
        - `r_M1`: Å
        - `r_M2`: Å
        - `r_CM1`: Å
        - `r_CM2`: Å
        - `r_CM3`: Å
        - `theta1`: deg
        - `theta2`: deg
        - `alpha`: deg
        - `beta`: deg
    - `Pd`:
      - `type`: object
      - `required`: `d_zmin`, `d_zavg`, `r_C1`, `r_C2`, `r_M1`, `r_M2`, `r_CM1`, `r_CM2`, `r_CM3`, `theta1`, `theta2`, `alpha`, `beta`
      - `units`:
        - `d_zmin`: Å
        - `d_zavg`: Å
        - `r_C1`: Å
        - `r_C2`: Å
        - `r_M1`: Å
        - `r_M2`: Å
        - `r_CM1`: Å
        - `r_CM2`: Å
        - `r_CM3`: Å
        - `theta1`: deg
        - `theta2`: deg
        - `alpha`: deg
        - `beta`: deg

### step_03_aqueous_0K_results.json
- path: `/app/outputs/step_03_aqueous_0K_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: 0 K aqueous-phase adsorption energies and structural parameters for the most stable bridge configurations.
- schema:
  - `type`: object
  - `required`: `Pt`, `Pd`
  - `properties`:
    - `Pt`:
      - `type`: object
      - `required`: `E_ad_aquo_0K`, `d_zmin`, `d_zavg`, `r_C1`, `r_C2`, `r_M1`, `r_M2`, `r_CM1`, `r_CM2`, `r_CM3`, `theta1`, `theta2`, `alpha`, `beta`
      - `units`:
        - `E_ad_aquo_0K`: eV
        - `d_zmin`: Å
        - `d_zavg`: Å
        - `r_C1`: Å
        - `r_C2`: Å
        - `r_M1`: Å
        - `r_M2`: Å
        - `r_CM1`: Å
        - `r_CM2`: Å
        - `r_CM3`: Å
        - `theta1`: deg
        - `theta2`: deg
        - `alpha`: deg
        - `beta`: deg
    - `Pd`:
      - `type`: object
      - `required`: `E_ad_aquo_0K`, `d_zmin`, `d_zavg`, `r_C1`, `r_C2`, `r_M1`, `r_M2`, `r_CM1`, `r_CM2`, `r_CM3`, `theta1`, `theta2`, `alpha`, `beta`
      - `units`:
        - `E_ad_aquo_0K`: eV
        - `d_zmin`: Å
        - `d_zavg`: Å
        - `r_C1`: Å
        - `r_C2`: Å
        - `r_M1`: Å
        - `r_M2`: Å
        - `r_CM1`: Å
        - `r_CM2`: Å
        - `r_CM3`: Å
        - `theta1`: deg
        - `theta2`: deg
        - `alpha`: deg
        - `beta`: deg

Notes: All distances are in Å, angles in degrees, and energies in eV. The hidden verifier compares each numeric value to gold reference values with tolerances suitable for independent DFT re-implementation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_adsorption_energies_gas.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "metal": "string",
          "configuration_name": "string",
          "E_ad_vac": "number (eV)"
        },
        "description": "Array of objects; must contain every configuration that yielded a negative adsorption energy from the DFT relaxations."
      },
      "description": "Gas-phase adsorption energies for all stable configurations on Pt(111) and Pd(111)."
    },
    {
      "file": "step_02_structural_params_gas.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Pt",
          "Pd"
        ],
        "properties": {
          "Pt": {
            "type": "object",
            "required": [
              "d_zmin",
              "d_zavg",
              "r_C1",
              "r_C2",
              "r_M1",
              "r_M2",
              "r_CM1",
              "r_CM2",
              "r_CM3",
              "theta1",
              "theta2",
              "alpha",
              "beta"
            ],
            "units": {
              "d_zmin": "Å",
              "d_zavg": "Å",
              "r_C1": "Å",
              "r_C2": "Å",
              "r_M1": "Å",
              "r_M2": "Å",
              "r_CM1": "Å",
              "r_CM2": "Å",
              "r_CM3": "Å",
              "theta1": "deg",
              "theta2": "deg",
              "alpha": "deg",
              "beta": "deg"
            }
          },
          "Pd": {
            "type": "object",
            "required": [
              "d_zmin",
              "d_zavg",
              "r_C1",
              "r_C2",
              "r_M1",
              "r_M2",
              "r_CM1",
              "r_CM2",
              "r_CM3",
              "theta1",
              "theta2",
              "alpha",
              "beta"
            ],
            "units": {
              "d_zmin": "Å",
              "d_zavg": "Å",
              "r_C1": "Å",
              "r_C2": "Å",
              "r_M1": "Å",
              "r_M2": "Å",
              "r_CM1": "Å",
              "r_CM2": "Å",
              "r_CM3": "Å",
              "theta1": "deg",
              "theta2": "deg",
              "alpha": "deg",
              "beta": "deg"
            }
          }
        }
      },
      "description": "Gas-phase structural parameters for the most stable bridge-site configurations on Pt and Pd."
    },
    {
      "file": "step_03_aqueous_0K_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Pt",
          "Pd"
        ],
        "properties": {
          "Pt": {
            "type": "object",
            "required": [
              "E_ad_aquo_0K",
              "d_zmin",
              "d_zavg",
              "r_C1",
              "r_C2",
              "r_M1",
              "r_M2",
              "r_CM1",
              "r_CM2",
              "r_CM3",
              "theta1",
              "theta2",
              "alpha",
              "beta"
            ],
            "units": {
              "E_ad_aquo_0K": "eV",
              "d_zmin": "Å",
              "d_zavg": "Å",
              "r_C1": "Å",
              "r_C2": "Å",
              "r_M1": "Å",
              "r_M2": "Å",
              "r_CM1": "Å",
              "r_CM2": "Å",
              "r_CM3": "Å",
              "theta1": "deg",
              "theta2": "deg",
              "alpha": "deg",
              "beta": "deg"
            }
          },
          "Pd": {
            "type": "object",
            "required": [
              "E_ad_aquo_0K",
              "d_zmin",
              "d_zavg",
              "r_C1",
              "r_C2",
              "r_M1",
              "r_M2",
              "r_CM1",
              "r_CM2",
              "r_CM3",
              "theta1",
              "theta2",
              "alpha",
              "beta"
            ],
            "units": {
              "E_ad_aquo_0K": "eV",
              "d_zmin": "Å",
              "d_zavg": "Å",
              "r_C1": "Å",
              "r_C2": "Å",
              "r_M1": "Å",
              "r_M2": "Å",
              "r_CM1": "Å",
              "r_CM2": "Å",
              "r_CM3": "Å",
              "theta1": "deg",
              "theta2": "deg",
              "alpha": "deg",
              "beta": "deg"
            }
          }
        }
      },
      "description": "0 K aqueous-phase adsorption energies and structural parameters for the most stable bridge configurations."
    }
  ],
  "notes": "All distances are in Å, angles in degrees, and energies in eV. The hidden verifier compares each numeric value to gold reference values with tolerances suitable for independent DFT re-implementation."
}
```

## How you are scored

A hidden verifier reads the artifacts you write to `/app/outputs` and compares each numeric value to a set of reference values (derived from the experimental process). Tolerances account for reasonable differences arising from implementation choices (e.g., pseudopotential, convergence settings).

Each scored artifact is evaluated independently, and the final reward is a weighted combination of the scores. Fabricating numbers or skipping the required process steps (e.g., skipping DFT relaxations by guessing) will result in a low or zero score. The load‑bearing step (aqueous 0 K results) cannot be passed without having genuinely performed the MD simulation, so you must execute the full pipeline.
