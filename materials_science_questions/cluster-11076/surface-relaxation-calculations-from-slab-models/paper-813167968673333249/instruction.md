# NO dissociation pathway on CuO(110) surface

## Problem background
Atmospheric pollution from nitrogen oxide (NOx) emitted by vehicle exhausts is a serious environmental concern, contributing to acid rain and smog. The catalytic reduction of NOx into harmless gases relies on the dissociation of nitric oxide (NO), which is the rate-limiting step. Precious metal catalysts (e.g., Rh, Pd, Pt) are effective but expensive. This motivates the search for cheaper, abundant materials that can catalyze NO dissociation with comparable performance. Copper oxides (Cu₂O, CuO) have emerged as promising candidates. This study investigates the dissociation of NO on the Cu-terminated CuO(110) surface using density functional theory (DFT) calculations to determine the reaction pathway and activation barrier.

## Approach
Spin-polarized DFT calculations with the generalized gradient approximation (PBE functional) are used to model the system. The CuO surface is represented by a periodic slab cut from the monoclinic bulk crystal (space group C2/c1). The Cu-terminated (110) face is chosen. The slab consists of four atomic layers in a 2×2 in-plane supercell. The top two layers are allowed to relax while the bottom two are fixed. The isolated NO molecule in a vacuum box serves as a reference state. NO is adsorbed on the hollow site in an N-end configuration, and its adsorption energy and N-O bond length are computed relative to the bare surface and isolated NO. To find the dissociation pathway, the coadsorption of separated N and O atoms (with O placed at the nearest hollow site) is calculated. Then, the climbing-image nudged elastic band (CI-NEB) method with four intermediate images is used to determine the minimum energy path from the molecularly adsorbed state (initial) to the coadsorbed state (final). The transition state is identified as the highest energy image along the band. The final step compiles the following quantities: (1) contraction of the interlayer distance between the topmost and second layers after relaxation, (2) molecular NO adsorption energy and N-O bond length, (3) coadsorption energy of N+O, (4) transition-state energy relative to the isolated NO + bare surface reference, and (5) the activation barrier from the molecularly adsorbed state to the transition state. All computations are performed with Quantum ESPRESSO, an open-source plane-wave DFT code, using projector augmented-wave (PAW) pseudopotentials from the SSSP PBE efficiency library.

## Reproduction target
Compute the following six quantities from DFT simulations of NO dissociation on the Cu-terminated CuO(110) surface, using the public assets listed above:
- surface_contraction (Å): interlayer contraction between the topmost and second Cu layers after relaxation of the top two layers.
- adsorption_energy_molecular (eV): adsorption energy of the molecularly adsorbed NO on the hollow site with N-end configuration, defined as E_ads = E_slab+NO – (E_isolated_NO + E_bare_slab).
- N_O_bond_length (Å): equilibrium bond length of the molecularly adsorbed NO.
- adsorption_energy_coadsorbed (eV): adsorption energy of the coadsorbed N+O atoms, defined analogously.
- transition_state_energy (eV): total energy of the transition state relative to the reference (isolated NO + bare surface); the transition state is identified from the CI-NEB path.
- activation_barrier (eV): energy difference between the transition state and the molecularly adsorbed state (E_TS – E_ads_molecular).
Write these values into /app/outputs/results.json as a JSON object with the exact keys and units shown.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials (efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- CuO crystal structure (Forsyth & Hull, 1991): 10.1088/0953-8984/3/28/001

## Workflow steps

### Step 1: Construct and relax Cu-terminated CuO(110) slab
- Role: process
- Action: From the experimental monoclinic CuO crystal structure, cut a 2×2, 4-layer Cu-terminated (110) slab. Perform spin-polarised DFT relaxation of the top two layers while keeping the bottom two layers fixed.
- Evidence: `/app/outputs/slab_relax.out`

### Step 2: Compute isolated NO reference energy
- Role: process
- Action: Perform spin-polarised DFT calculation for an isolated NO molecule in a vacuum box to obtain its total energy and equilibrium bond length.
- Evidence: `/app/outputs/no_ref.out`

### Step 3: Molecular NO adsorption on Cu-terminated hollow site
- Role: process
- Action: Adsorb an NO molecule on the hollow site of the relaxed Cu-terminated slab in the N-end configuration. Relax the adsorbate and top surface layers.
- Evidence: `/app/outputs/no_ads.out`

### Step 4: Coadsorption of N and O atoms
- Role: process
- Action: Place N and O atoms on the Cu-terminated slab (O at the nearest hollow site) and relax the geometry.
- Evidence: `/app/outputs/coads.out`

### Step 5: CI-NEB reaction pathway for NO dissociation
- Role: process
- Action: Using the molecularly adsorbed state (step03) as the initial image and the coadsorbed state (step04) as the final image, run a climbing-image nudged elastic band (CI-NEB) calculation with 4 intermediate images. Identify the transition state from the minimum-energy path.
- Evidence: `/app/outputs/neb.out`

### Step 6: Compile final results
- Role: scored (load-bearing)
- Action: From the preceding calculations, extract: (a) interlayer contraction between topmost and second layer after slab relaxation, (b) molecular NO adsorption energy (E_ads = E_sys - E_iso, with E_iso = total energy of isolated NO + total energy of bare slab) and N-O bond length, (c) coadsorption energy of N+O, (d) transition-state adsorption energy from the NEB path, (e) activation barrier (energy difference between transition state and molecularly adsorbed state). Write all values into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: surface_contraction (float, Angstrom), adsorption_energy_molecular (float, eV), N_O_bond_length (float, Angstrom), adsorption_energy_coadsorbed (float, eV), transition_state_energy (float, eV), activation_barrier (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reproduced quantities for NO dissociation on CuO(110). All values are compared to the paper-reported DFT results with pre-defined tolerances.
- schema:
  - `type`: object
  - `required`:
    - `surface_contraction`: number
    - `adsorption_energy_molecular`: number
    - `N_O_bond_length`: number
    - `adsorption_energy_coadsorbed`: number
    - `transition_state_energy`: number
    - `activation_barrier`: number
  - `units`:
    - `surface_contraction`: Angstrom
    - `adsorption_energy_molecular`: eV
    - `N_O_bond_length`: Angstrom
    - `adsorption_energy_coadsorbed`: eV
    - `transition_state_energy`: eV
    - `activation_barrier`: eV

Notes: The solver must produce these quantities from their own DFT calculations using Quantum ESPRESSO with SSSP PBE pseudopotentials. The CI-NEB step may require significant CPU time; the solving agent is expected to run it on external compute and bring the final artifacts back.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "surface_contraction": "number",
          "adsorption_energy_molecular": "number",
          "N_O_bond_length": "number",
          "adsorption_energy_coadsorbed": "number",
          "transition_state_energy": "number",
          "activation_barrier": "number"
        },
        "units": {
          "surface_contraction": "Angstrom",
          "adsorption_energy_molecular": "eV",
          "N_O_bond_length": "Angstrom",
          "adsorption_energy_coadsorbed": "eV",
          "transition_state_energy": "eV",
          "activation_barrier": "eV"
        }
      },
      "description": "Reproduced quantities for NO dissociation on CuO(110). All values are compared to the paper-reported DFT results with pre-defined tolerances."
    }
  ],
  "notes": "The solver must produce these quantities from their own DFT calculations using Quantum ESPRESSO with SSSP PBE pseudopotentials. The CI-NEB step may require significant CPU time; the solving agent is expected to run it on external compute and bring the final artifacts back."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/results.json and independently checks each of the six quantities. Each value is compared to the paper’s reported result (the gold) within a predefined tolerance. The verifier also checks a structural property of the transition state (e.g., a sign constraint). Your overall score is a weighted average of per-quantity scores; you earn maximum credit when all values lie within tolerance and the structural check passes, while larger deviations yield progressively lower credit. The tolerances are chosen to account for legitimate differences between DFT codes (Quantum ESPRESSO vs. the paper’s original VASP) while distinguishing a correct re-implementation from a arbitrary guess. Reporting numbers alone is not sufficient; the verifier expects the values to originate from the DFT workflow described in the workflow steps.
