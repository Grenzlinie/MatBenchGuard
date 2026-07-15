# Reproducing dynamical stability, magnetism, and half-metallicity of α-BaNaO₄ from first principles

## Problem background
Molecular oxygen (O₂) dimers can carry local magnetic moments due to unpaired electrons in their π* orbitals. In known alkali superoxides, O₂ dimer layers stack with an in-plane offset, leading to antiferromagnetic coupling between layers. This study proposes that a head-to-head stacking of O₂ dimer layers, separated by Ba²⁺ ions and arranged in a tetragonal P4/mmm structure (α-BaNaO₄), may switch the interlayer coupling to ferromagnetic (FM) and produce a half-metal. Using first-principles calculations, the dynamical, mechanical, and thermal stability of this compound, as well as its magnetic and electronic properties, are assessed.

## Approach
This task uses density-functional theory (DFT) calculations with the PBE functional and the open-source Quantum ESPRESSO code as a substitute for VASP. The workflow proceeds as follows: 1) construct the α-BaNaO₄ unit cell; 2) perform a full geometry relaxation; 3) compute phonon dispersions via finite-displacement (PHONOPY) to verify dynamical stability; 4) compute elastic constants to verify mechanical stability against the tetragonal Born criteria; 5) perform spin‑polarized total-energy calculations for ferromagnetic (FM), three antiferromagnetic (AFM) ordering patterns, and non-magnetic (NM) to determine the magnetic ground state and extract the nearest-neighbor (J₁) and next-nearest-neighbor (J₂) exchange coupling constants; 6) compute the spin‑resolved band structure to check for half-metallicity (spin‑up channel insulating, spin‑down channel metallic); 7) run a classical Heisenberg Monte Carlo simulation using the extracted J₁, J₂, and a magnetic anisotropy A to obtain the temperature‑dependent magnetization and susceptibility, from which the Curie temperature is identified. The final outputs are consolidated into a single JSON file.

## Reproduction target
You must produce a file `/app/outputs/results.json` containing the following fields, all derived from your executed workflow: minimum_phonon_frequency (cm⁻¹, expected >0 for stability), elastic_stability (true if Born criteria hold), magnetic_ground_state (one of 'FM', 'AFM', 'NM'), energy_differences (a dictionary of FM versus each AFM and NM configuration in meV), spin_up_bandgap (eV), spin_down_metallic (true if the spin‑down channel crosses the Fermi level), and curie_temperature (K). The objective is to successfully compute these quantities for the α-BaNaO₄ material using the outlined first‑principles pipeline.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- PHONOPY: https://phonopy.github.io/phonopy/
- Python with numpy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Build α-BaNaO₄ crystal structure
- Role: process
- Action: Construct the tetragonal P4/mmm unit cell of α-BaNaO₄ with Ba, Na ions and O₂ dimers arranged in head-to-head stacking along [001] separated by Ba. Write an initial structure file for DFT.
- Evidence: `/app/outputs/initial_structure.cif`

### Step 2: DFT relaxation of α-BaNaO₄
- Role: process
- Action: Perform a full geometry relaxation (atomic positions and lattice parameters) with spin‑unpolarised DFT using the PBE functional, a plane‑wave basis, and PAW pseudopotentials. Save the final relaxed structure and total energy.
- Evidence: `/app/outputs/relax_output.txt`

### Step 3: Phonon dispersion and dynamical stability
- Role: process
- Action: Run finite‑displacement phonon calculations on the relaxed structure using the PHONOPY interface with Quantum ESPRESSO. Obtain the full phonon band structure across the Brillouin zone and determine the minimum frequency.
- Evidence: `/app/outputs/phonon_band.yaml`

### Step 4: Elastic constants and mechanical stability
- Role: process
- Action: Compute the elastic stiffness constants of the relaxed α-BaNaO₄ structure from DFT stress‑strain calculations. Check that the constants satisfy the tetragonal Born stability criteria.
- Evidence: `/app/outputs/elastic_constants.txt`

### Step 5: Spin‑polarized DFT for magnetic configurations
- Role: process
- Action: Perform spin‑polarized DFT calculations for the FM, AFM1, AFM2, AFM3, and NM collinear arrangements of the α-BaNaO₄ cell. Extract total energies and derive nearest‑neighbour (J1) and next‑nearest‑neighbour (J2) exchange coupling constants.
- Evidence: `/app/outputs/magnetic_energies.json`

### Step 6: Spin‑resolved band structure
- Role: process
- Action: Compute the spin‑resolved electronic band structure of the FM ground‑state structure along a high‑symmetry path. Determine whether the spin‑up channel is insulating (gap > 0) and the spin‑down channel is metallic (Fermi level crossed).
- Evidence: `/app/outputs/band_structure.json`

### Step 7: Monte Carlo simulation for Curie temperature
- Role: process
- Action: Implement a classical Heisenberg Monte Carlo simulation using the extracted J1, J2, and a magnetic anisotropy A. Compute the temperature‑dependent magnetization and magnetic susceptibility to locate the Curie temperature.
- Evidence: `/app/outputs/mc_curie_data.json`

### Step 8: Compile final results
- Role: scored (load-bearing)
- Action: Read the outputs of all previous steps and assemble a single JSON file containing: minimum gemess of phonon frequency (cm⁻¹), elastic stability boolean, magnetic ground state string, energy differences (dict), spin‑up band gap (eV), spin‑down metallic boolean, and Curie temperature (K). Write the file to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"minimum_phonon_frequency": <float, cm⁻¹, >0 for stable>, "elastic_stability": <bool, true if Born criteria hold>, "magnetic_ground_state": <string, "FM"|"AFM"|"NM">, "energy_differences": {"FM_vs_AFM1": <float, meV>, "FM_vs_AFM2": <float, meV>, "FM_vs_AFM3": <float, meV>, "FM_vs_NM": <float, meV>}, "spin_up_bandgap": <float, eV>, "spin_down_metallic": <bool, true if Fermi level is crossed in spin‑down channel>, "curie_temperature": <float, K>}
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
- target_policy: reference_match
- description: Aggregate result artifact containing all key reproduced quantities from the workflow.
- schema:
  - `type`: object
  - `required`: `minimum_phonon_frequency`, `elastic_stability`, `magnetic_ground_state`, `energy_differences`, `spin_up_bandgap`, `spin_down_metallic`, `curie_temperature`
  - `properties`:
    - `minimum_phonon_frequency`:
      - `type`: number
      - `unit`: cm-1
      - `description`: minimum phonon frequency, >0 for stability
    - `elastic_stability`:
      - `type`: boolean
    - `magnetic_ground_state`:
      - `type`: string
      - `enum`: `FM`, `AFM`, `NM`
    - `energy_differences`:
      - `type`: object
      - `properties`:
        - `FM_vs_AFM1`:
          - `type`: number
          - `unit`: meV
        - `FM_vs_AFM2`:
          - `type`: number
          - `unit`: meV
        - `FM_vs_AFM3`:
          - `type`: number
          - `unit`: meV
        - `FM_vs_NM`:
          - `type`: number
          - `unit`: meV
    - `spin_up_bandgap`:
      - `type`: number
      - `unit`: eV
    - `spin_down_metallic`:
      - `type`: boolean
    - `curie_temperature`:
      - `type`: number
      - `unit`: K

Notes: The checker compares each field in results.json to the paper's reported values with appropriate tolerances. The target policy is reference_match as the artifact is compared against a hidden gold standard.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "minimum_phonon_frequency",
          "elastic_stability",
          "magnetic_ground_state",
          "energy_differences",
          "spin_up_bandgap",
          "spin_down_metallic",
          "curie_temperature"
        ],
        "properties": {
          "minimum_phonon_frequency": {
            "type": "number",
            "unit": "cm-1",
            "description": "minimum phonon frequency, >0 for stability"
          },
          "elastic_stability": {
            "type": "boolean"
          },
          "magnetic_ground_state": {
            "type": "string",
            "enum": [
              "FM",
              "AFM",
              "NM"
            ]
          },
          "energy_differences": {
            "type": "object",
            "properties": {
              "FM_vs_AFM1": {
                "type": "number",
                "unit": "meV"
              },
              "FM_vs_AFM2": {
                "type": "number",
                "unit": "meV"
              },
              "FM_vs_AFM3": {
                "type": "number",
                "unit": "meV"
              },
              "FM_vs_NM": {
                "type": "number",
                "unit": "meV"
              }
            }
          },
          "spin_up_bandgap": {
            "type": "number",
            "unit": "eV"
          },
          "spin_down_metallic": {
            "type": "boolean"
          },
          "curie_temperature": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "Aggregate result artifact containing all key reproduced quantities from the workflow."
    }
  ],
  "notes": "The checker compares each field in results.json to the paper's reported values with appropriate tolerances. The target policy is reference_match as the artifact is compared against a hidden gold standard."
}
```

## How you are scored
A hidden verifier loads your results.json and compares each field against hidden reference values derived from the paper’s reported results. Each field is scored independently with tolerances that account for differences between DFT implementations (Quantum ESPRESSO vs. VASP) and convergence settings. The final reward is a weighted sum of these per-field scores. The verifier does not reward trivial guessing or hardcoded numbers; only a genuine execution of the computational workflow will produce values that fall within the expected tolerances.
