# DFT-calculated CO2 adsorption energies and Bader charges on graphitic carbon nitride with and without nitrogen vacancies

## Problem background
Graphitic carbon nitride (g-C3N4) is a metal-free photocatalyst with a moderate bandgap, making it promising for photocatalytic CO2 reduction. However, its efficiency is limited by strong exciton binding energies, which hinder the separation of photo-generated charge carriers. Introducing nitrogen vacancies into the g-C3N4 lattice can alter the local electronic structure, creating regions of energy disorder that may promote exciton dissociation into free charges and enhance CO2 adsorption. Understanding this effect requires a quantitative description of the CO2 binding strength and the charge redistribution around the vacancy site. This task provides a computational route to compute these quantities using density functional theory (DFT).

## Approach
The core idea is to compare a pristine g-C3N4 surface with a surface that contains a specific nitrogen vacancy (Nv-rich-CN) through first-principles DFT calculations. You will build atomic models of both surfaces, relax their structures, and compute the binding energy of a CO2 molecule to each surface. In addition, you will perform a Bader charge analysis on the relaxed charge densities to extract the effective charges of the two carbon atoms adjacent to the vacancy (or the corresponding atoms in the pristine model). The workflow uses open-source DFT tools and post-processing codes; the required inputs are the publicly known crystal structure of heptazine-based g-C3N4 and standard DFT parameters that you will select.

## Reproduction target
Produce two primary artifacts from your DFT calculations:

1. **step_01_adsorption_energies.csv** – A CSV file with columns `model` and `adsorption_energy_eV`. It must contain two rows: `CN` (pristine g-C3N4) and `Nv-rich-CN` (g-C3N4 with an N2C vacancy). The adsorption energy is defined as `E_ads = E_total(slab+CO2) - E_slab - E_CO2` and should be reported in eV.

2. **step_02_bader_charges.json** – A JSON object with keys `"CN"` and `"Nv-rich-CN"`, each mapping to an array of two floats (in units of e) representing the Bader effective charges of the two carbon atoms directly adjacent to the N vacancy position (or the equivalent atoms in the pristine model).

Your objective is to obtain these quantities through the described DFT procedure; no other outputs are scored.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K, VASP): https://www.quantum-espresso.org
- Bader charge analysis tool (Henkelman group): http://theory.cm.utexas.edu/henkelman/code/bader/
- Heptazine-based g-C3N4 crystal structure

## Workflow steps

### Step 1: Construct CN and Nv-rich-CN supercell models
- Role: process
- Action: Build the pristine g-C3N4 2×2×1 supercell. Create the Nv-rich-CN model by removing a single N2C atom (N19 position) from the supercell. Prepare input files for DFT relaxation of the bare surfaces and CO2 molecule.
- Evidence: `/app/outputs/coordinates.txt`

### Step 2: DFT geometry relaxation and energy calculation
- Role: process
- Action: Using an open-source DFT code with GGA-PBE functional, PAW pseudopotentials, DFT-D3 dispersion correction, and appropriate convergence criteria, relax the atomic positions of (i) pristine CN surface, (ii) Nv-rich-CN surface, (iii) isolated CO2 molecule. Then compute total energies for each relaxed structure and for the CO2-adsorbed complexes on both surfaces.
- Evidence: `/app/outputs/dft_output.log`

### Step 3: Compute CO2 adsorption energies
- Role: scored (load-bearing)
- Action: From the total energies obtained in step_02, calculate the adsorption energy for each model using E_ads = E_total(slab+CO2) - E_slab - E_CO2. Write the results to step_01_adsorption_energies.csv.
- Output file: `/app/outputs/step_01_adsorption_energies.csv`
- Format: csv
- Contract: CSV with columns: 'model' (string) and 'adsorption_energy_eV' (float). Two rows: one for 'CN', one for 'Nv-rich-CN'.
- Scoring: scored by hidden verifier

### Step 4: Bader charge analysis on N-vacancy carbon atoms
- Role: scored
- Action: Perform Bader charge analysis on the charge density of the relaxed Nv-rich-CN surface and the pristine CN surface. Extract the effective charges of the two carbon atoms directly adjacent to the N vacancy (or the corresponding positions in the pristine model). Write the results to step_02_bader_charges.json.
- Output file: `/app/outputs/step_02_bader_charges.json`
- Format: json
- Contract: JSON object with keys 'CN' and 'Nv-rich-CN', values are arrays of two numbers (Bader charges in e).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_adsorption_energies.csv`
- `/app/outputs/step_02_bader_charges.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_adsorption_energies.csv
- path: `/app/outputs/step_01_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CO2 adsorption energy on pristine CN and Nv-rich-CN surfaces. The checker compares both values to hidden reference numbers with tolerance, and verifies the trend that Nv-rich-CN is more negative.
- schema:
  - `type`: table
  - `required_columns`: `model`, `adsorption_energy_eV`
  - `units`:
    - `adsorption_energy_eV`: eV

### step_02_bader_charges.json
- path: `/app/outputs/step_02_bader_charges.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bader effective charges of the two carbon atoms adjacent to the N vacancy in both models.
- schema:
  - `type`: object
  - `required`:
    - `CN`: array of two floats
    - `Nv-rich-CN`: array of two floats
  - `units`:
    - `CN`: e
    - `Nv-rich-CN`: e

Notes: The agent must use an open-source DFT code; the exact functional and pseudopotential choice is left to the solver. The checker compares the resulting energies and charges to the paper's reported values with appropriate tolerances. A trend check (Nv-rich-CN adsorption energy more negative than CN) is also applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "adsorption_energy_eV"
        ],
        "units": {
          "adsorption_energy_eV": "eV"
        }
      },
      "description": "CO2 adsorption energy on pristine CN and Nv-rich-CN surfaces. The checker compares both values to hidden reference numbers with tolerance, and verifies the trend that Nv-rich-CN is more negative."
    },
    {
      "file": "step_02_bader_charges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "CN": "array of two floats",
          "Nv-rich-CN": "array of two floats"
        },
        "units": {
          "CN": "e",
          "Nv-rich-CN": "e"
        }
      },
      "description": "Bader effective charges of the two carbon atoms adjacent to the N vacancy in both models."
    }
  ],
  "notes": "The agent must use an open-source DFT code; the exact functional and pseudopotential choice is left to the solver. The checker compares the resulting energies and charges to the paper's reported values with appropriate tolerances. A trend check (Nv-rich-CN adsorption energy more negative than CN) is also applied."
}
```

## How you are scored
A hidden verifier will independently check your two output artifacts against reference values derived from published results. The verifier applies appropriate tolerances to account for the inherent spread between different DFT implementations, and it also checks that the relative ordering of the adsorption energies is physically correct. Each artifact contributes to your final reward, which is a weighted sum of the stage scores normalized to the range [0,1]. You must genuinely execute the DFT and post-processing pipelines; simply guessing or copying a known number will not guarantee success because the tolerances are designed to validate a proper re-run of the computational procedure.
