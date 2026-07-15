# DFT Reproduction of Elastic and Stability Properties of TiN/WN₀.₅ Superlattices

## Problem background
Transition metal nitride thin films are widely used as hard protective coatings, but they often suffer from low intrinsic fracture toughness. Superlattice architectures, alternating nanoscale layers of two materials, have shown promise to simultaneously enhance hardness and toughness. Density functional theory (DFT) can be used to predict the stability and mechanical properties of such superlattices, guiding experimental synthesis. In this task, we focus on TiN/WN superlattices, where nitrogen vacancies in the WN layers are expected to stabilise the cubic phase and yield favourable semi‑empirical ductility indicators. The goal is to compute the energetic stability, dynamical stability, and elastic properties of a TiN/WN₀.₅ superlattice with a bilayer period of approximately 3.3 nm, and to compare the vacancy‑containing structure to a defect‑free reference.

## Approach
The reproduction relies on plane‑wave DFT calculations using an open‑source code (Quantum ESPRESSO) together with standard PBE pseudopotentials. The workflow comprises: constructing rocksalt‑based atomic models for a defect‑free TiN/WN superlattice and a TiN/WN₀.₅ superlattice (50 % ordered N vacancies in the WN layer), both with (100)‑oriented interfaces and a bilayer period close to 3.3 nm; preparing reference cells for hcp‑Ti, bcc‑W, and an N₂ molecule. Full structural relaxation of all systems is performed to obtain total energies, which are then used to compute formation energies per atom and the formation energy difference between the two superlattices. The relaxed TiN/WN₀.₅ supercell is further subjected to a phonon stability analysis via finite‑displacement force constants and Phonopy, checking for imaginary‑frequency modes. Finally, the elastic tensor is computed by applying small strain tensors and extracting stress responses; from it, the polycrystalline bulk modulus B, shear modulus G, Young’s modulus E, Poisson’s ratio, B/G ratio, and an effective Cauchy pressure are derived. All quantities are combined into a single JSON file.

## Reproduction target
Produce a JSON file named `dft_results.json` that contains the following fields computed for the TiN/WN₀.₅ superlattice: `B` (GPa), `G` (GPa), `E` (GPa), `B_over_G` (dimensionless), `Cauchy_pressure` (GPa), `poisson_ratio` (dimensionless), `formation_energy_difference` (eV/atom, relative to the defect‑free superlattice), and `phonon_stable` (`true` if the phonon density of states shows no imaginary frequencies, `false` otherwise). The numerical values must be the outcome of the DFT workflow described above.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Structure generation and input preparation
- Role: process
- Action: Construct rocksalt-based atomic models: (i) a defect-free TiN/WN superlattice with two layers each stacked along [100] and (ii) a TiN/WN₀.₅ superlattice with 50% ordered N vacancies in the WN layer, both with a bilayer period of approximately 3.3 nm. Also prepare primitive cells for hcp-Ti, bcc-W, and an isolated N₂ molecule to obtain reference chemical potentials. Generate Quantum ESPRESSO input files with appropriate convergence settings.
- Evidence: none

### Step 2: DFT total-energy calculations and structural relaxation
- Role: process
- Action: Run pw.x to fully relax each supercell (cell shape, volume, atomic positions) and the reference phases to obtain total energies. Use PBE-GGA pseudopotentials and convergence to <1 meV/atom. Save the relaxed structures for later steps.
- Evidence: none

### Step 3: Formation energy analysis
- Role: process
- Action: From the total energies and the reference chemical potentials (energy per atom of hcp-Ti, bcc-W, and per N₂ molecule) compute the formation energy per atom for both superlattices using the standard formation energy expression. Calculate the difference between the vacancy-containing and defect-free superlattice formation energies.
- Evidence: none

### Step 4: Phonon stability analysis
- Role: process
- Action: Using the relaxed TiN/WN₀.₅ supercell, compute force constants via finite-displacement DFT (ph.x) and generate the phonon density of states with Phonopy. Verify whether the DOS shows contributions at imaginary (negative) frequencies.
- Evidence: none

### Step 5: Elastic constants and moduli calculation
- Role: process
- Action: Apply strain tensors to the relaxed TiN/WN₀.₅ supercell, compute the stress response via DFT to construct the elastic constant matrix. Derive the polycrystalline bulk modulus B, shear modulus G, Young’s modulus E, Poisson’s ratio ν, B/G ratio, and the effective Cauchy pressure.
- Evidence: none

### Step 6: Reporting of computed properties
- Role: scored (load-bearing)
- Action: Compile all final quantities into a JSON file named dft_results.json. Include: B (GPa), G (GPa), E (GPa), B_over_G, Cauchy_pressure (GPa), poisson_ratio, formation_energy_difference (eV/atom), and phonon_stable (bool).
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: Object with keys: B (float, GPa), G (float, GPa), E (float, GPa), B_over_G (float), Cauchy_pressure (float, GPa), poisson_ratio (float), formation_energy_difference (float, eV/atom), phonon_stable (bool).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed elastic moduli, B/G ratio, Cauchy pressure, formation energy difference, and phonon stability verdict for the TiN/WN₀.₅ superlattice with bilayer period ~3.3 nm.
- schema:
  - `type`: object
  - `properties`:
    - `B`:
      - `type`: number
      - `units`: GPa
    - `G`:
      - `type`: number
      - `units`: GPa
    - `E`:
      - `type`: number
      - `units`: GPa
    - `B_over_G`:
      - `type`: number
    - `Cauchy_pressure`:
      - `type`: number
      - `units`: GPa
    - `poisson_ratio`:
      - `type`: number
    - `formation_energy_difference`:
      - `type`: number
      - `units`: eV/atom
    - `phonon_stable`:
      - `type`: boolean
  - `required`: `B`, `G`, `E`, `B_over_G`, `Cauchy_pressure`, `poisson_ratio`, `formation_energy_difference`, `phonon_stable`

Notes: The agent must perform the DFT workflow using Quantum ESPRESSO (or another open-source plane-wave DFT code) and Phonopy. The hidden checker compares the submitted values to the paper's reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "B": {
            "type": "number",
            "units": "GPa"
          },
          "G": {
            "type": "number",
            "units": "GPa"
          },
          "E": {
            "type": "number",
            "units": "GPa"
          },
          "B_over_G": {
            "type": "number"
          },
          "Cauchy_pressure": {
            "type": "number",
            "units": "GPa"
          },
          "poisson_ratio": {
            "type": "number"
          },
          "formation_energy_difference": {
            "type": "number",
            "units": "eV/atom"
          },
          "phonon_stable": {
            "type": "boolean"
          }
        },
        "required": [
          "B",
          "G",
          "E",
          "B_over_G",
          "Cauchy_pressure",
          "poisson_ratio",
          "formation_energy_difference",
          "phonon_stable"
        ]
      },
      "description": "Computed elastic moduli, B/G ratio, Cauchy pressure, formation energy difference, and phonon stability verdict for the TiN/WN₀.₅ superlattice with bilayer period ~3.3 nm."
    }
  ],
  "notes": "The agent must perform the DFT workflow using Quantum ESPRESSO (or another open-source plane-wave DFT code) and Phonopy. The hidden checker compares the submitted values to the paper's reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier will read your `dft_results.json` and compare each field against reference values derived from the original computational study. The comparison uses tolerances that account for differences between DFT codes and pseudopotentials, so an honest re‑execution of the described protocol will meet them. The final score is a weighted combination of per‑field scores; therefore reporting correct numbers obtained from the actual DFT workflow is essential, while guessed or hard‑coded values will fail.
