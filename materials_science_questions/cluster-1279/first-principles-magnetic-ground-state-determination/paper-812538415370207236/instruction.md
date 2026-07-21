# First-principles adsorption energies and geometries of H2, CH4, and C2H2 on ferromagnetic Ti2N monolayer

## Problem background
Transformer oil degrades under electrical faults, releasing dissolved gases such as H2, CH4, and C2H2. Efficient removal or detection of these gases is important for insulation health. This task uses first-principles DFT to investigate the potential of a pristine Ti2N monolayer as an adsorbent for these three gases. We aim to compute the adsorption energy, Hirshfeld charge transfer, and structural changes for each gas on a ferromagnetically ordered 3×3×1 Ti2N supercell, in order to determine whether the adsorption is chemical or physical and whether gas molecules undergo bond dissociation.

## Approach
We employ periodic density functional theory (DFT) with the GGA-PBE functional and the Grimme D2 dispersion correction, using the CP2K package with DZVP basis sets and GTH pseudopotentials. First, the magnetic ground state is determined by minimizing the total energy of ferromagnetic and antiferromagnetic configurations of the Ti2N monolayer. The relaxed ferromagnetic substrate is then used for subsequent adsorption studies. Isolated gas molecules (H2, CH4, C2H2) are optimized in large simulation cells. For each gas, an adsorption complex is built by placing the molecule at the most stable site on the Ti2N surface (for H2, H atoms centered above three top‑layer Ti atoms; for C2H2, C atoms near Ti atoms; for CH4, the molecule at the centre of three Ti atoms), and a geometry optimisation is performed. From each final structure we extract the total energy, Hirshfeld charge transfer, and relevant interatomic distances. Adsorption energies are then calculated as E_ad = E(gas/Ti2N) − E(gas) − E(Ti2N).

## Reproduction target
The final artifact is a JSON file (reproduction_results.json) containing total energies for the clean substrate, isolated gas molecules, and each adsorbed system, together with the derived adsorption energies for H2, CH4, and C2H2, Hirshfeld charge transfers for each adsorbed gas, and key bond lengths (H–H after H2 adsorption; C–C and C–H for C2H2). The verifier will recompute adsorption energies from the total energies and compare the numerical results against hidden reference criteria to determine the nature of each gas–surface interaction.

## Assets

- CP2K: https://www.cp2k.org/

## Workflow steps

### Step 1: Determine ferromagnetic ground state and relax Ti2N monolayer
- Role: process
- Action: Perform periodic DFT geometry optimisation for a pristine 3×3×1 Ti2N monolayer with ferromagnetic spin ordering (GGA-PBE, Grimme D2 dispersion). Confirm that ferromagnetic is the lowest-energy magnetic state by also computing an antiferromagnetic trial. Obtain the relaxed atomic coordinates and total energy of the ferromagnetic substrate.
- Evidence: `/app/outputs/ti2n_fm.xyz`

### Step 2: Optimize isolated gas molecules
- Role: process
- Action: Perform geometry optimisation and total energy calculation for isolated H2, CH4, and C2H2 molecules in a large periodic cell using the same DFT settings (GGA-PBE, D2 dispersion). Store the optimised structures and total energies for each molecule.
- Evidence: `/app/outputs/gas_energies.txt`

### Step 3: Adsorption geometry optimisation and property extraction
- Role: process
- Action: For each gas (H2, CH4, C2H2), build an adsorption system by placing the molecule on the pristine Ti2N surface at the most stable adsorption site reported: H atoms centred above three top‑layer Ti atoms for H2; C atoms near Ti atoms for C2H2; CH4 at the centre of three Ti atoms. Run DFT geometry optimisation (GGA-PBE, D2 dispersion) and from the final configuration extract the total energy, Hirshfeld charge transfer, H–H distance after H2 adsorption, and C–C distance for C2H2. Save all raw numbers in a structured file.
- Evidence: `/app/outputs/adsorption_raw.json`

### Step 4: Compile final reproduction results
- Role: scored (load-bearing)
- Action: Collect the total energies from the previous steps, compute adsorption energies as E_ad = E(gas/Ti2N) − E(gas) − E(Ti2N) for each molecule, and assemble all quantities into a JSON file reproduction_results.json with the required schema: total_energies (dict with keys ti2n, h2, ch4, c2h2, h2_ti2n, ch4_ti2n, c2h2_ti2n in eV), adsorption_energies (dict with H2, CH4, C2H2 in eV), charge_transfers (dict with H2, CH4, C2H2 in e), bond_lengths (dict with H2_HH, C2H2_CC, C2H2_CH in Å).
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: JSON object with top-level keys: 'total_energies' (object with numeric values in eV), 'adsorption_energies' (object with numeric values in eV), 'charge_transfers' (object with numeric values in e), 'bond_lengths' (object with numeric values in Å). See output_contract for full schema.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Final reproduction results containing the raw total energies and derived properties. The checker will recompute adsorption energies as E_ad = total_energies['h2_ti2n'] − total_energies['h2'] − total_energies['ti2n'] (and analogously for CH4, C2H2) and compare each recomputed value to the hidden paper-reported adsorption energy with a tolerance. Structural requirements and charge transfers are also checked.
- schema:
  - `type`: object
  - `required`: `total_energies`, `adsorption_energies`, `charge_transfers`, `bond_lengths`
  - `properties`:
    - `total_energies`:
      - `type`: object
      - `required`: `ti2n`, `h2`, `ch4`, `c2h2`, `h2_ti2n`, `ch4_ti2n`, `c2h2_ti2n`
      - `properties`:
        - `ti2n`:
          - `type`: number
          - `unit`: eV
        - `h2`:
          - `type`: number
          - `unit`: eV
        - `ch4`:
          - `type`: number
          - `unit`: eV
        - `c2h2`:
          - `type`: number
          - `unit`: eV
        - `h2_ti2n`:
          - `type`: number
          - `unit`: eV
        - `ch4_ti2n`:
          - `type`: number
          - `unit`: eV
        - `c2h2_ti2n`:
          - `type`: number
          - `unit`: eV
    - `adsorption_energies`:
      - `type`: object
      - `required`: `H2`, `CH4`, `C2H2`
      - `properties`:
        - `H2`:
          - `type`: number
          - `unit`: eV
        - `CH4`:
          - `type`: number
          - `unit`: eV
        - `C2H2`:
          - `type`: number
          - `unit`: eV
    - `charge_transfers`:
      - `type`: object
      - `required`: `H2`, `CH4`, `C2H2`
      - `properties`:
        - `H2`:
          - `type`: number
          - `unit`: e
        - `CH4`:
          - `type`: number
          - `unit`: e
        - `C2H2`:
          - `type`: number
          - `unit`: e
    - `bond_lengths`:
      - `type`: object
      - `required`: `H2_HH`, `C2H2_CC`, `C2H2_CH`
      - `properties`:
        - `H2_HH`:
          - `type`: number
          - `unit`: Å
        - `C2H2_CC`:
          - `type`: number
          - `unit`: Å
        - `C2H2_CH`:
          - `type`: number
          - `unit`: Å

Notes: The output_contract defines the machine-readable scoring interface. All values are as computed by the agent; no hidden gold values or tolerances are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "total_energies",
          "adsorption_energies",
          "charge_transfers",
          "bond_lengths"
        ],
        "properties": {
          "total_energies": {
            "type": "object",
            "required": [
              "ti2n",
              "h2",
              "ch4",
              "c2h2",
              "h2_ti2n",
              "ch4_ti2n",
              "c2h2_ti2n"
            ],
            "properties": {
              "ti2n": {
                "type": "number",
                "unit": "eV"
              },
              "h2": {
                "type": "number",
                "unit": "eV"
              },
              "ch4": {
                "type": "number",
                "unit": "eV"
              },
              "c2h2": {
                "type": "number",
                "unit": "eV"
              },
              "h2_ti2n": {
                "type": "number",
                "unit": "eV"
              },
              "ch4_ti2n": {
                "type": "number",
                "unit": "eV"
              },
              "c2h2_ti2n": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "adsorption_energies": {
            "type": "object",
            "required": [
              "H2",
              "CH4",
              "C2H2"
            ],
            "properties": {
              "H2": {
                "type": "number",
                "unit": "eV"
              },
              "CH4": {
                "type": "number",
                "unit": "eV"
              },
              "C2H2": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "charge_transfers": {
            "type": "object",
            "required": [
              "H2",
              "CH4",
              "C2H2"
            ],
            "properties": {
              "H2": {
                "type": "number",
                "unit": "e"
              },
              "CH4": {
                "type": "number",
                "unit": "e"
              },
              "C2H2": {
                "type": "number",
                "unit": "e"
              }
            }
          },
          "bond_lengths": {
            "type": "object",
            "required": [
              "H2_HH",
              "C2H2_CC",
              "C2H2_CH"
            ],
            "properties": {
              "H2_HH": {
                "type": "number",
                "unit": "Å"
              },
              "C2H2_CC": {
                "type": "number",
                "unit": "Å"
              },
              "C2H2_CH": {
                "type": "number",
                "unit": "Å"
              }
            }
          }
        }
      },
      "description": "Final reproduction results containing the raw total energies and derived properties. The checker will recompute adsorption energies as E_ad = total_energies['h2_ti2n'] − total_energies['h2'] − total_energies['ti2n'] (and analogously for CH4, C2H2) and compare each recomputed value to the hidden paper-reported adsorption energy with a tolerance. Structural requirements and charge transfers are also checked."
    }
  ],
  "notes": "The output_contract defines the machine-readable scoring interface. All values are as computed by the agent; no hidden gold values or tolerances are exposed."
}
```

## How you are scored
A hidden verifier will process your submitted reproduction_results.json. It will independently recompute the adsorption energies from the total_energies field using the formula E_ad = E(gas/Ti2N) − E(gas) − E(Ti2N), and then score each adsorption energy against hidden thresholds that reward correct physical trends. It will also examine structural metrics (bond lengths) and charge transfers, comparing them to reference criteria. Each check contributes a weighted share to the total score; the final reward is the fraction of checks passed, a number between 0 and 1. Simply reporting physically unreasonable numbers without performing the DFT calculations is unlikely to yield a high score.
