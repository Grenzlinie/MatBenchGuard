# DFT Adsorption Energies of N-based Gases on Mg-Embedded C3B Monolayer

## Problem background
Two-dimensional nanomaterials are promising candidates for gas-sensing applications because of their high surface‑to‑volume ratio and tunable electronic properties. Among these, the carbon‑based C3B monolayer has attracted attention, but pristine C3B generally interacts only weakly with gas molecules. Doping or decorating the sheet with metal atoms is a common strategy to enhance chemical sensitivity. This task focuses on the adsorption behaviour of several nitrogen‑based gas molecules (NO, N2O, NH3, and NO2) on a magnesium‑decorated C3B monolayer. The aim is to compute how strongly each molecule binds to the Mg site and to quantify the changes in adsorption characteristics compared to the bare C3B surface, thereby assessing the potential of Mg‑C3B as a gas‑sensing material.

## Approach
The study uses first‑principles density functional theory (DFT) calculations with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and the Grimme DFT‑D2 dispersion correction to account for van der Waals interactions. Computations are carried out on a 2×2×1 supercell of C3B with a vacuum layer that prevents spurious interactions between periodic images. The workflow proceeds as follows: (i) relax the pristine C3B monolayer and extract its indirect band gap; (ii) place a Mg atom at the hollow site of the relaxed C3B sheet, perform a spin‑polarised relaxation, and compute the Mg adsorption energy; (iii) for each gas molecule, adsorb it on the pristine C3B surface, relax, and record the weak physisorption energies; (iv) for each gas molecule, adsorb it on the Mg‑C3B system in several chemically plausible orientations (e.g., via the nitrogen or oxygen end of the molecule), relax, and compute both the adsorption energy and the equilibrium distance from the Mg atom to the nearest atom of the molecule. All relaxations are spin‑polarised when open‑shell species (NO, NO2) or the Mg‑C3B system are involved. Finally, the computed numerical results are collected into a single JSON file for evaluation. Any DFT code supporting the required functionals may be used.

## Reproduction target
Your task is to carry out the DFT calculations outlined above and to report the following quantities in the JSON file `/app/outputs/adsorption_results.json`:

- The indirect band gap (in eV) of the relaxed pristine C3B monolayer.
- The adsorption energy (in eV) of a single Mg atom adsorbed on the hollow site of C3B.
- For each gas (NO, N2O, NO2, NH3), the adsorption energy on the pristine C3B surface.
- For each gas on the Mg‑decorated C3B system, the adsorption energy and the equilibrium Mg–adsorbate distance for the configurations:
   * NO bound through its N atom (configuration I) and through its O atom (configuration II)
   * N2O bound through its N atom
   * NO2 bound through its O atoms (configuration I) and through its N atom (configuration II)
   * NH3 bound through its N atom

The output JSON must follow the provided contract exactly, and all values must be computed from your own DFT runs.

## Assets

- SIESTA DFT code: https://departments.icmab.es/leem/siesta/
- C3B monolayer crystal structure

## Workflow steps

### Step 1: Prepare C3B supercell
- Role: process
- Action: Construct the 2×2×1 supercell of C3B monolayer by starting from a graphene lattice and substituting two carbon atoms with boron atoms. Write the initial atomic coordinates as an XYZ file.
- Evidence: `/app/outputs/c3b_structure.xyz`

### Step 2: Pristine C3B relaxation and band gap calculation
- Role: process
- Action: Perform DFT relaxation of the pristine C3B supercell using the PBE functional with DFT-D2 dispersion, an 8×8×1 Monkhorst–Pack k‑mesh, and a vacuum layer of 20 Å. Compute the electronic band structure and extract the indirect band gap.
- Evidence: `/app/outputs/pristine_c3b_output.log`

### Step 3: Mg adsorption on C3B
- Role: process
- Action: Place a Mg atom at the hollow site of the relaxed C3B monolayer and perform a spin‑polarized DFT relaxation using the same computational parameters. Compute the adsorption energy of Mg onto C3B.
- Evidence: `/app/outputs/mg_c3b_output.log`

### Step 4: Gas adsorption on pristine C3B
- Role: process
- Action: For each of the molecules NO, N₂O, NO₂, and NH₃, place the molecule above the pristine C3B surface in a plausible initial orientation, relax the system with DFT, and compute the adsorption energy. (This provides the physisorption reference values.)
- Evidence: `/app/outputs/gas_pristine_adsorption.log`

### Step 5: Gas adsorption on Mg‑C3B
- Role: process
- Action: For each gas molecule, adsorb it on the Mg site of the optimized Mg‑C3B system in the specified configurations: NO (N‑end and O‑end), N₂O (N‑end), NO₂ (O‑end and N‑end), NH₃ (N‑end). Perform spin‑polarized DFT relaxation and compute the adsorption energy and the equilibrium Mg–adsorbate distance.
- Evidence: `/app/outputs/gas_mgc3b_adsorption.log`

### Step 6: Compile adsorption results
- Role: scored (load-bearing)
- Action: Collect the computed values from the DFT runs and write a single JSON file that contains: the Mg adsorption energy on C3B, the pristine C3B band gap, the list of gas adsorption energies and distances for each configuration on Mg‑C3B, and the list of gas adsorption energies on pristine C3B.
- Output file: `/app/outputs/adsorption_results.json`
- Format: json
- Contract: JSON object with keys: Mg_adsorption_energy (float, eV), pristine_C3B_band_gap (float, eV), gas_adsorptions (array of objects with keys: molecule (string), configuration (string), E_ad (float, eV), distance (float, Å)), pristine_gas_adsorptions (array of objects with keys: molecule (string), E_ad (float, eV)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_results.json
- path: `/app/outputs/adsorption_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compilation of all computed DFT adsorption energies and distances. The checker compares each numeric value to the corresponding paper-reported value using hidden tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Mg_adsorption_energy`: number (eV)
    - `pristine_C3B_band_gap`: number (eV)
    - `gas_adsorptions`: array of objects each containing molecule (string), configuration (string), E_ad (number eV), distance (number Angstrom)
    - `pristine_gas_adsorptions`: array of objects each containing molecule (string), E_ad (number eV)

Notes: Each adsorption and distance value is compared against a hidden reference with predefined tolerances. The exact tolerance values are not disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Mg_adsorption_energy": "number (eV)",
          "pristine_C3B_band_gap": "number (eV)",
          "gas_adsorptions": "array of objects each containing molecule (string), configuration (string), E_ad (number eV), distance (number Angstrom)",
          "pristine_gas_adsorptions": "array of objects each containing molecule (string), E_ad (number eV)"
        }
      },
      "description": "Compilation of all computed DFT adsorption energies and distances. The checker compares each numeric value to the corresponding paper-reported value using hidden tolerances."
    }
  ],
  "notes": "Each adsorption and distance value is compared against a hidden reference with predefined tolerances. The exact tolerance values are not disclosed to the agent."
}
```

## How you are scored
A hidden verifier compares every required numerical value in your `adsorption_results.json` against reference values that were independently derived from the original study. Each value is checked individually: if your reported number falls within a predefined tolerance of the reference, you earn full credit for that item; otherwise you receive no credit for that item. The final reward is the average of the per‑item credits. The exact tolerances are not disclosed – only accurate results obtained by faithfully executing the described DFT workflow will satisfy all constraints. Reporting values without running the calculations is very unlikely to succeed.
