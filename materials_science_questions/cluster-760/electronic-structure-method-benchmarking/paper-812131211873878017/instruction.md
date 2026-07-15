# Single-molecule H2 absorption energy in sodalite: DFT vs force-field benchmark

## Problem background
Accurate modelling of molecular hydrogen confined in nanoporous materials is essential for understanding hydrogen storage. In siliceous sodalite, the interactions of H2 with the framework and with other H2 molecules are weak and nonbonding, making them challenging for electronic structure methods. This work compares periodic density functional theory (DFT) using four different exchange-correlation functionals (LDA, PW91, PBE, BLYP) with classical force-field (FF) descriptions of the H2‑framework and H2‑H2 interactions. The goal is to quantify how the choice of method affects the predicted absorption energy of a single H2 molecule within a sodalite cage.

## Approach
The absorption energy E_abs of a single H2 molecule in a sodalite cage is defined as E_abs = E_LC - E_EC - E_H2, where E_LC is the total energy of the cage with one H2, E_EC is the total energy of the empty cage, and E_H2 is the energy of an isolated H2 molecule. These energies are computed for each functional (LDA, PW91, PBE, BLYP) and for a classical force-field model (FF_Buck) that combines Lennard‑Jones potentials for the H2‑framework interactions with the Buck et al. potential for H2‑H2 interactions. All calculations are performed at a fixed lattice constant of 8.77 Å using the sodalite unit cell (Si12O24 per cell, representing two cages). DFT optimisations employ ultrasoft pseudopotentials and Γ‑point sampling; the classical model uses the Sanders force field for the SiO2 framework together with the published Si‑H2, O‑H2, and H2‑H2 parameters. Only one sodalite cage is loaded, and all atomic positions are relaxed at constant cell volume.

## Reproduction target
Compute the single‑molecule absorption energy E_abs for one H2 molecule confined in a sodalite cage using each of the five methods: LDA, PW91, PBE, BLYP, and FF_Buck. For each method, perform geometry optimisations (at fixed cell volume) of the empty cage, the cage loaded with one H2 molecule, and the isolated H2 molecule. Collect the three total energies (E_LC, E_EC, E_H2) and then calculate E_abs. Report all values in a single JSON file, with one entry per method containing the method name, E_abs (eV), E_LC (eV), E_EC (eV), and E_H2 (eV).

## Assets

- Sodalite unit cell coordinates
- Force field parameters (Si-H2, O-H2 LJ; H2-H2 Buck)
- Quantum ESPRESSO (plane-wave DFT code): https://www.quantum-espresso.org/
- GULP (force-field / molecular mechanics engine): https://github.com/gulp-developers/gulp
- Vanderbilt ultrasoft pseudopotentials (SSSP efficiency library): https://www.materialscloud.org/sssp/

## Workflow steps

### Step 1: Construct sodalite supercell
- Role: process
- Action: Construct the sodalite unit cell (two cages per cell, Si12O24) with lattice constant a = 8.77 Å using standard atomic coordinates for SOD. This fixed cell will be used for all subsequent calculations.
- Evidence: none

### Step 2: DFT optimisation of empty sodalite cage
- Role: process
- Action: For each exchange-correlation functional (LDA, PW91, PBE, BLYP) perform a full atomic position optimisation of the empty sodalite cage at fixed cell volume using plane-wave DFT with ultrasoft pseudopotentials and Γ‑point sampling. Record the total energy E_EC for each functional.
- Evidence: `/app/outputs/dft_empty_energies.txt`

### Step 3: DFT optimisation of H2-loaded sodalite cage
- Role: process
- Action: For each functional, place one H2 molecule inside the cage (starting position from the van den Berg et al. arrangement) and perform a full geometry optimisation at fixed cell volume. Record the total energy of the loaded system E_LC.
- Evidence: `/app/outputs/dft_loaded_energies.txt`

### Step 4: Isolated H2 molecule calculation (DFT)
- Role: process
- Action: For each functional, compute the total energy of an isolated H2 molecule in a sufficiently large vacuum box at the same level of theory. Record E_H2.
- Evidence: `/app/outputs/dft_h2_energies.txt`

### Step 5: Force-field optimisation of empty sodalite cage
- Role: process
- Action: Implement the Sanders force field for SiO₂ together with the Si–H₂/O–H₂ Lennard-Jones parameters and the H₂–H₂ Buck potential. Perform a geometry optimisation of the empty cage at fixed cell (a = 8.77 Å) using GULP or an equivalent classical engine. Record the total energy E_EC.
- Evidence: `/app/outputs/ff_empty_energy.txt`

### Step 6: Force-field optimisation of H2-loaded sodalite cage
- Role: process
- Action: Using the same force-field setup, place one H₂ molecule inside the cage and optimise atomic positions at fixed cell. Record the total energy E_LC.
- Evidence: `/app/outputs/ff_loaded_energy.txt`

### Step 7: Isolated H2 energy (force field)
- Role: process
- Action: For the force-field calculations the H₂ molecule is represented as a single interaction site with no internal energy. Set the isolated H₂ energy E_H2 = 0 eV.
- Evidence: none

### Step 8: Compute single-molecule absorption energies
- Role: scored (load-bearing)
- Action: For each method (LDA, PW91, PBE, BLYP, FF_Buck) compute the single-molecule absorption energy E_abs = E_LC - E_EC - E_H₂ using the energies obtained in the previous steps. Compile the results into a JSON file containing one entry per method with fields method, E_abs_eV, E_LC_eV, E_EC_eV, E_H2_eV.
- Output file: `/app/outputs/step_01_single_molecule_energies.json`
- Format: json
- Contract: Array of objects, each with keys: method (string), E_abs_eV (number), E_LC_eV (number), E_EC_eV (number), E_H2_eV (number). Methods: LDA, PW91, PBE, BLYP, FF_Buck.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_single_molecule_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_single_molecule_energies.json
- path: `/app/outputs/step_01_single_molecule_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed absorption energies E_abs and the constituent total energies for LDA, PW91, PBE, BLYP, and FF_Buck.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `method`, `E_abs_eV`, `E_LC_eV`, `E_EC_eV`, `E_H2_eV`
    - `properties`:
      - `method`:
        - `type`: string
      - `E_abs_eV`:
        - `type`: number
      - `E_LC_eV`:
        - `type`: number
      - `E_EC_eV`:
        - `type`: number
      - `E_H2_eV`:
        - `type`: number

Notes: The checker compares the agent's reported E_abs values against the paper's published results with an appropriate tolerance, and also verifies internal consistency: E_abs = E_LC - E_EC - E_H₂ within numerical precision.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_single_molecule_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "method",
            "E_abs_eV",
            "E_LC_eV",
            "E_EC_eV",
            "E_H2_eV"
          ],
          "properties": {
            "method": {
              "type": "string"
            },
            "E_abs_eV": {
              "type": "number"
            },
            "E_LC_eV": {
              "type": "number"
            },
            "E_EC_eV": {
              "type": "number"
            },
            "E_H2_eV": {
              "type": "number"
            }
          }
        }
      },
      "description": "Computed absorption energies E_abs and the constituent total energies for LDA, PW91, PBE, BLYP, and FF_Buck."
    }
  ],
  "notes": "The checker compares the agent's reported E_abs values against the paper's published results with an appropriate tolerance, and also verifies internal consistency: E_abs = E_LC - E_EC - E_H₂ within numerical precision."
}
```

## How you are scored
A hidden verifier reads your submitted JSON and scores each method independently. The verifier compares your computed E_abs to a reference value derived from the original study, accepting results that fall within a realistic numerical tolerance that accounts for legitimate spread due to different software, pseudopotentials, or force‑field engines. The verifier also checks internal consistency: E_abs must equal E_LC - E_EC - E_H2 within numerical precision. For each method, results that meet or exceed the reference quality earn full credit, while larger deviations earn partial credit. The final reward is a weighted combination of the per‑method scores.
