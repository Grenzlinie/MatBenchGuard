# Zr–N Phase Stability and Elastic Moduli via DFT and Quasiharmonic Phonon Calculations

## Problem background
Zirconium nitrides are a family of refractory materials prized for their high hardness, strength, and chemical stability, making them ideal for cutting tools, wear‑resistant coatings, and high‑temperature applications. In real materials, non‑stoichiometry due to structural vacancies leads to a wide range of compositions, and both phase stability and mechanical properties vary strongly with vacancy concentration. Predicting which compounds are stable and how their mechanical properties depend on composition is challenging and requires accurate first‑principles calculations. This task investigates the finite‑temperature thermodynamic stability and elastic response of several key Zr–N phases using density‑functional theory and quasiharmonic phonon calculations.

## Approach
The computational strategy has two branches. First, the static total energy (0 K enthalpy) of each compound and of the appropriate reference phases is obtained via plane‑wave density‑functional theory (DFT) calculations. Second, phonon calculations within the quasiharmonic approximation are performed to obtain vibrational free energies at 0 K and 1000 K. By combining static and vibrational contributions, formation free energies per atom are computed using the standard thermodynamic relation. In parallel, the elastic tensor of each compound is obtained from DFT stress‑strain calculations, and then bulk and shear moduli are derived via Voigt–Reuss–Hill averaging. The entire workflow is implemented with open‑source tools: Quantum ESPRESSO for DFT, PHONOPY for phonon calculations, and a suitable post‑processing tool (or custom finite‑difference routine) for elastic constants.

## Reproduction target
You are given the crystal structures (space group, lattice parameters, atomic positions) for four target Zr–N compounds: Zr₂N, ZrN, Zr₃N₂, and Zr₄N₅, as well as for the reference states (hcp Zr and α‑N₂/N₂ gas). Using these structures, perform the full computational pipeline described above and produce two CSV files with the required schemas:
- formation_free_energies.csv: columns compound (string), temperature_K (numeric), formation_free_energy_eV_per_atom (numeric); rows for each of the four compounds at 0 K and 1000 K.
- elastic_moduli.csv: columns compound (string), bulk_modulus_GPa (numeric), shear_modulus_GPa (numeric); rows for each of the four compounds.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp/table
- Elastic constants post-processing tool: https://github.com/max-veit/elastic
- Reference crystal structures for target compounds and reference phases

## Workflow steps

### Step 1: DFT static total energy calculations
- Role: process
- Action: Using Quantum ESPRESSO with SSSP pseudopotentials, perform DFT total energy calculations for each target compound (Zr₂N, ZrN, Zr₃N₂, Zr₄N₅) and the reference states (hcp Zr, α‑N₂ or N₂ gas). Relax atomic positions and cell parameters as needed to obtain ground-state energies.
- Evidence: `/app/outputs/dft_energies.csv`

### Step 2: Quasiharmonic phonon calculations
- Role: process
- Action: For each compound, perform phonon calculations using PHONOPY: create supercells, run finite-displacement DFT to obtain forces, compute phonon dispersions and vibrational free energies within the quasiharmonic approximation at 0 K and 1000 K.
- Evidence: `/app/outputs/phonon_free_energies.csv`

### Step 3: Formation free energies
- Role: scored (load-bearing)
- Action: Combine the static energies and vibrational free energies to compute formation free energies per atom using ΔG = [G(Zr_xN_y) - xG(Zr) - yG(N)]/(x+y). Use hcp Zr as the reference for Zr; for N, use α‑N₂ at 0 K and N₂ gas at 1000 K. Write the results to formation_free_energies.csv.
- Output file: `/app/outputs/formation_free_energies.csv`
- Format: csv
- Contract: Columns: compound (string), temperature_K (numeric), formation_free_energy_eV_per_atom (numeric)
- Scoring: scored by hidden verifier

### Step 4: Elastic moduli
- Role: scored
- Action: Perform DFT elastic constant calculations for each compound (e.g., stress-strain method). Use Voigt–Reuss–Hill averaging to compute the bulk modulus B and shear modulus G. Write the results to elastic_moduli.csv.
- Output file: `/app/outputs/elastic_moduli.csv`
- Format: csv
- Contract: Columns: compound (string), bulk_modulus_GPa (numeric), shear_modulus_GPa (numeric)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_free_energies.csv`
- `/app/outputs/elastic_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_free_energies.csv
- path: `/app/outputs/formation_free_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed formation free energies for Zr₂N, ZrN, Zr₃N₂, and Zr₄N₅ at 0 K and 1000 K. The checker compares each value to hidden paper-reported values with a tolerance of 0.01 eV/atom.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `temperature_K`, `formation_free_energy_eV_per_atom`
  - `units`:
    - `temperature_K`: kelvin
    - `formation_free_energy_eV_per_atom`: eV per atom

### elastic_moduli.csv
- path: `/app/outputs/elastic_moduli.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Bulk and shear moduli for Zr₂N, ZrN, Zr₃N₂, and Zr₄N₅. The checker compares each modulus to hidden paper-reported values with a tolerance of 5 GPa; additionally, a structural trend check verifies that moduli decrease with increasing vacancy concentration.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `bulk_modulus_GPa`, `shear_modulus_GPa`
  - `units`:
    - `bulk_modulus_GPa`: GPa
    - `shear_modulus_GPa`: GPa

Notes: Only the four key compounds are scored. The checker also checks the monotonic trend (moduli decrease with vacancy concentration) as a secondary structural requirement.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_free_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "temperature_K",
          "formation_free_energy_eV_per_atom"
        ],
        "units": {
          "temperature_K": "kelvin",
          "formation_free_energy_eV_per_atom": "eV per atom"
        }
      },
      "description": "Computed formation free energies for Zr₂N, ZrN, Zr₃N₂, and Zr₄N₅ at 0 K and 1000 K. The checker compares each value to hidden paper-reported values with a tolerance of 0.01 eV/atom."
    },
    {
      "file": "elastic_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "bulk_modulus_GPa",
          "shear_modulus_GPa"
        ],
        "units": {
          "bulk_modulus_GPa": "GPa",
          "shear_modulus_GPa": "GPa"
        }
      },
      "description": "Bulk and shear moduli for Zr₂N, ZrN, Zr₃N₂, and Zr₄N₅. The checker compares each modulus to hidden paper-reported values with a tolerance of 5 GPa; additionally, a structural trend check verifies that moduli decrease with increasing vacancy concentration."
    }
  ],
  "notes": "Only the four key compounds are scored. The checker also checks the monotonic trend (moduli decrease with vacancy concentration) as a secondary structural requirement."
}
```

## How you are scored
Your submission is scored by a hidden verifier. The verifier reads the two CSV files and compares each numeric value to reference values (based on the paper’s reported results) using a directional threshold policy: if your computed value is equal to or more favorable (e.g., a more stable formation free energy or a higher modulus) than the hidden reference, you earn full credit; as the value deviates in the wrong direction, the score decreases. Additionally, the verifier carries out a structural trend check: for the rocksalt‑derived compounds (ZrN, Zr₃N₂, Zr₄N₅), it verifies that both bulk and shear moduli decrease with increasing vacancy concentration. The final score is a weighted combination of all checks, with the formation free energies and moduli each contributing substantially.
