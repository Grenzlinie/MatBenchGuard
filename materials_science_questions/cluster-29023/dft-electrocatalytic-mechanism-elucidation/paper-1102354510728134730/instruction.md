# DFT Free Energy Profiles for Photocatalytic H₂O₂ Synthesis on a Cationic Covalent Organic Framework

## Problem background
Photocatalytic hydrogen peroxide (H₂O₂) production from water and molecular oxygen is a green alternative to the energy-intensive anthraquinone process. Cationic covalent organic frameworks (COFs) that combine electron-rich terpyridine/quarterpyridine knots with electron-deficient pyridinium linkers have emerged as high-performance photocatalysts. Among them, iTPPy-COF – a vinylene-linked COF built from a phenyl-extended terpyridine trialdehyde (TPPyTA) and N-ethyl-2,4,6-trimethylpyridinium bromide – is proposed to operate via concurrent two-electron oxygen reduction (ORR) and two-electron water oxidation (WOR) channels without sacrificial agents. Density functional theory (DFT) can elucidate the thermodynamic driving forces by mapping the free energy landscape of the key reaction intermediates on specific active sites. Reproducing the DFT free energy profiles and the adsorption energy of the *O–O* intermediate on the pyridinium N⁺ site is essential to validate the proposed dual-channel mechanism and to provide a computational baseline for further catalyst design.

## Approach
The approach follows two conceptual stages. First, a periodic model of iTPPy-COF is constructed in the eclipsed AA stacking mode from its monomer connectivity: TPPyTA cores are linked to pyridinium units via vinylene (–C≡C–) bonds. The unit cell dimensions are derived from the reported PXRD 100 peak at 4.06° 2θ (Cu Kα radiation) and the HRTEM stripe spacing (~0.37 nm), yielding an in-plane pore size of ~1.91 nm. Full geometry optimization is performed with a periodic DFT code using a dispersion correction (e.g., DFT-D3) and an implicit solvent model to obtain a relaxed structure. Second, the computational hydrogen electrode (CHE) model at T=298 K and pH=0 is applied to compute Gibbs free energies of the reaction intermediates. For the ORR pathway on the pyridinium N⁺ site in a Yeager-type configuration, the energies of *O₂, *OO*, and H₂O₂ are evaluated. For the WOR pathway on a pyridine C=N site adjacent to a benzene ring, the energies of H₂O, *OH, and H₂O₂ are computed. The free energy of each step is obtained from the energies of the relevant species, and the adsorption free energy ΔG of *OO* on N⁺ is extracted to quantify the key intermediate stabilization.

## Reproduction target
Construct the AA-stacked periodic model of iTPPy-COF and perform DFT geometry optimization as described. Then compute the Gibbs free energy profiles for both pathways and output a single JSON file free_energy_profiles.json with the following entries: OO_adsorption_on_Nplus_delta_G_eV (the adsorption free energy of *O–O* on the pyridinium N⁺ site in eV), ORR (an array of objects with species and delta_G_eV for the intermediates *O2, *OO*, H2O2 in the 2e⁻ ORR), WOR (an array for the intermediates H2O, *OH, H2O2 in the 2e⁻ WOR), ORR_downhill (a boolean indicating whether every ORR step has ΔG < 0), and WOR_uphill_steps (a boolean indicating whether at least one WOR step has ΔG > 0). The final output file must conform to this schema.

## Assets

- Periodic DFT code with dispersion correction and implicit solvent (e.g., Quantum ESPRESSO, GPAW, CP2K): Quantum ESPRESSO (open-source) or equivalent

## Workflow steps

### Step 1: Build and optimize iTPPy-COF structural model
- Role: process
- Action: Construct a periodic AA-stacked model of the iTPPy-COF structure from the monomer connectivity (TPPyTA trialdehyde linked to N-ethyl-2,4,6-trimethylpyridinium bromide via vinylene bonds) using the unit cell dimensions determined from the reported PXRD 100 peak (4.06° 2θ, Cu Kα) and HRTEM stripe spacing (~0.37 nm). Perform full DFT geometry optimization with dispersion correction and implicit solvent.
- Evidence: `/app/outputs/optimized_structure.cif`

### Step 2: Compute adsorption free energies and free energy profiles
- Role: scored (load-bearing)
- Action: Using the optimized structure, compute the Gibbs free energies of the 2e− ORR and 2e− WOR pathways on the pyridinium N⁺ site (for ORR, intermediates *O₂, *OO*, H₂O₂; for WOR, intermediates H₂O, *OH, H₂O₂) at the standard computational hydrogen electrode (CHE) conditions (T=298 K, pH=0). Report the adsorption free energy ΔG of the *O–O* intermediate on the N⁺ site, the stepwise ΔG values for each pathway, and boolean flags indicating whether ORR is overall downhill (all steps ΔG<0) and WOR contains at least one uphill step (any step ΔG>0). Output all results to free_energy_profiles.json.
- Output file: `/app/outputs/free_energy_profiles.json`
- Format: json
- Contract: {"OO_adsorption_on_Nplus_delta_G_eV": number, "ORR": [{"species": "*O2", "delta_G_eV": number}, {"species": "*OO*", "delta_G_eV": number}, {"species": "H2O2", "delta_G_eV": number}], "WOR": [{"species": "H2O", "delta_G_eV": number}, {"species": "*OH", "delta_G_eV": number}, {"species": "H2O2", "delta_G_eV": number}], "ORR_downhill": boolean, "WOR_uphill_steps": boolean}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_profiles.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_profiles.json
- path: `/app/outputs/free_energy_profiles.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed adsorption free energy of *OO* on the pyridinium N⁺ site (eV), stepwise ΔG for ORR and WOR intermediates, and thermodynamic pathway flags.
- schema:
  - `type`: object
  - `required`: `OO_adsorption_on_Nplus_delta_G_eV`, `ORR`, `WOR`, `ORR_downhill`, `WOR_uphill_steps`
  - `properties`:
    - `OO_adsorption_on_Nplus_delta_G_eV`:
      - `type`: number
      - `unit`: eV
    - `ORR`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `species`, `delta_G_eV`
        - `properties`:
          - `species`:
            - `type`: string
          - `delta_G_eV`:
            - `type`: number
            - `unit`: eV
    - `WOR`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `species`, `delta_G_eV`
        - `properties`:
          - `species`:
            - `type`: string
          - `delta_G_eV`:
            - `type`: number
            - `unit`: eV
    - `ORR_downhill`:
      - `type`: boolean
    - `WOR_uphill_steps`:
      - `type`: boolean

Notes: The checker compares OO_adsorption_on_Nplus_delta_G_eV to the paper’s reference value within a tolerance that accounts for DFT‑toolchain variance. The boolean flags must be consistent with the agent’s own reported ΔG values: ORR_downhill is true iff all entries in ORR have delta_G_eV < 0; WOR_uphill_steps is true iff at least one entry in WOR has delta_G_eV > 0. No hidden gold is needed for the flags; they are validated against the stepwise data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_profiles.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "OO_adsorption_on_Nplus_delta_G_eV",
          "ORR",
          "WOR",
          "ORR_downhill",
          "WOR_uphill_steps"
        ],
        "properties": {
          "OO_adsorption_on_Nplus_delta_G_eV": {
            "type": "number",
            "unit": "eV"
          },
          "ORR": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "species",
                "delta_G_eV"
              ],
              "properties": {
                "species": {
                  "type": "string"
                },
                "delta_G_eV": {
                  "type": "number",
                  "unit": "eV"
                }
              }
            }
          },
          "WOR": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "species",
                "delta_G_eV"
              ],
              "properties": {
                "species": {
                  "type": "string"
                },
                "delta_G_eV": {
                  "type": "number",
                  "unit": "eV"
                }
              }
            }
          },
          "ORR_downhill": {
            "type": "boolean"
          },
          "WOR_uphill_steps": {
            "type": "boolean"
          }
        }
      },
      "description": "Computed adsorption free energy of *OO* on the pyridinium N⁺ site (eV), stepwise ΔG for ORR and WOR intermediates, and thermodynamic pathway flags."
    }
  ],
  "notes": "The checker compares OO_adsorption_on_Nplus_delta_G_eV to the paper’s reference value within a tolerance that accounts for DFT‑toolchain variance. The boolean flags must be consistent with the agent’s own reported ΔG values: ORR_downhill is true iff all entries in ORR have delta_G_eV < 0; WOR_uphill_steps is true iff at least one entry in WOR has delta_G_eV > 0. No hidden gold is needed for the flags; they are validated against the stepwise data."
}
```

## How you are scored
A hidden verifier independently evaluates your submitted free_energy_profiles.json. The verifier compares your reported OO_adsorption_on_Nplus_delta_G_eV to a reference value with a tolerance that accounts for typical variations among DFT implementations. The boolean flags ORR_downhill and WOR_uphill_steps are checked against the stepwise ΔG values you supplied: ORR_downhill must be true if and only if all ORR delta_G_eV entries are strictly negative; WOR_uphill_steps must be true if and only if at least one WOR delta_G_eV entry is strictly positive. Mismatches between the flags and the values you reported will reduce the reward. The final reward is a weighted combination of these checks; you must genuinely run the calculations to produce a self-consistent result – simply reporting expected numbers is not sufficient to achieve a high score.
