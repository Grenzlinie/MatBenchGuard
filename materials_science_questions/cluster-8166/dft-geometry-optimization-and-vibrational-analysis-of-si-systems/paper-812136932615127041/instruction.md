# DFT study of Si doping in closed CNTs: formation energies, HOMO/LUMO, and effective work function

## Problem background
Field emission properties of carbon nanotubes (CNTs) are sensitive to their geometric and electronic structure. Theoretical studies suggest that doping the closed cap of a CNT with heteroatoms can modify the local density of states near the Fermi level and alter the effective work function, which in turn affects field-emission performance. In particular, substituting carbon atoms with silicon introduces new electronic states and can change the frontier orbital energies. This task reproduces first-principles density functional theory (DFT) calculations to determine the formation energies, HOMO/LUMO energies, and effective work function of pure and Si-doped closed (5,5) and (9,0) single-wall carbon nanotubes. The computed quantities allow an assessment of the energetic stability of different doping configurations and the influence of Si concentration on the effective work function.

## Approach
First-principles calculations are performed using DFT with the generalized gradient approximation (GGA) in the BLYP parametrization and a double-zeta polarized (DZP) basis set. The systems investigated are pure and Si-substituted (5,5) and (9,0) CNTs with hydrogen termination at the open ends. Several doping models are constructed: for the (5,5) CNT, single Si substitution at three different cap sites (models I–III) and a double Si substitution at para-positions (model IV); for the (9,0) CNT, single (model V) and double (model VI) Si substitution at the topmost hexagon. Geometry optimizations are carried out for all CNT models, keeping bottom hydrogens fixed. A bulk silicon calculation provides the Si chemical potential, while the pure CNT total energy per carbon atom defines the C chemical potential. Formation energies are calculated from total-energy differences. HOMO and LUMO energies are extracted from the electronic structure, and an effective work function is estimated as (LUMO − HOMO)/2, assuming the Fermi level lies at mid-gap. The final deliverable is a table of formation energies and frontier orbital energies for all pure and doped models.

## Reproduction target
Using the DFT method described, compute the formation energy, HOMO, LUMO, and effective work function for the eight CNT models: pure (5,5) and pure (9,0), plus the six Si‑doped configurations (models I–VI). Pure systems serve as the reference; their formation energy is defined as zero. Output the results in a CSV file with columns: `system` (string), `formation_energy_eV` (float), `homo_eV` (float), `lumo_eV` (float), `effective_work_function_eV` (float). The CSV must contain exactly one row per model, following the system identifiers listed in the output contract. The computed values will be evaluated for internal consistency and compared against expected reference results.

## Assets

- SIESTA: https://siesta-project.org/siesta/
- ASE (Atomic Simulation Environment): ase
- Pseudopotentials for C, Si, H: https://pseudo.siesta-project.org

## Workflow steps

### Step 1: Build initial CNT models and bulk Si cell
- Role: process
- Action: Construct atomic coordinates for (5,5) and (9,0) CNTs with hydrogen termination at the bottom, then create Si-doping models: model I (single Si at topmost pentagon), model II (Si at second layer), model III (Si at third layer), model IV (two Si at para-sites of hexagon at second layer), model V (single Si at topmost hexagon), model VI (two Si at para-sites of hexagon). Also generate a bulk Si unit cell.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: DFT geometry optimization of all CNT models
- Role: process
- Action: Perform DFT geometry optimization for all CNT models (pure and doped) using SIESTA with GGA (BLYP) and DZP basis set. Fix bottom hydrogen atoms during relaxation. Converge forces to reasonable tolerance. Save optimized geometries and total energies.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 3: Compute chemical potentials
- Role: process
- Action: Compute the total energy per atom of bulk Si, E_Si, from the optimized bulk Si cell. Determine the carbon chemical potential E_C as the total energy per carbon atom of the optimized pure CNT (total energy divided by number of C atoms). Output both values.
- Evidence: `/app/outputs/chemical_potentials.txt`

### Step 4: Calculate formation energies, HOMO/LUMO, and effective work function
- Role: scored (load-bearing)
- Action: From the optimized total energies of all models and the chemical potentials, compute formation energies for each doped model using the formula: formation energy = (total energy of doped system - total energy of pure system) - (E_Si - E_C). Extract HOMO and LUMO energies from the DFT electronic structure output. Compute effective work function as (LUMO - HOMO)/2. Write a CSV file with columns: system, formation_energy_eV, homo_eV, lumo_eV, effective_work_function_eV.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: system (string, values 'pure_5_5','model_I','model_II','model_III','model_IV','pure_9_0','model_V','model_VI'), formation_energy_eV (float), homo_eV (float), lumo_eV (float), effective_work_function_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of formation energies, HOMO, LUMO, and effective work function for all CNT systems. Each row corresponds to one model.
- schema:
  - `type`: table
  - `required_columns`: `system`, `formation_energy_eV`, `homo_eV`, `lumo_eV`, `effective_work_function_eV`
  - `units`:
    - `formation_energy_eV`: eV
    - `homo_eV`: eV
    - `lumo_eV`: eV
    - `effective_work_function_eV`: eV

Notes: The effective work function is defined as (LUMO - HOMO)/2. Formation energy of pure systems is zero. The checker will compare each quantity to hidden reference values and verify the trend that effective work function decreases with Si doping.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "formation_energy_eV",
          "homo_eV",
          "lumo_eV",
          "effective_work_function_eV"
        ],
        "units": {
          "formation_energy_eV": "eV",
          "homo_eV": "eV",
          "lumo_eV": "eV",
          "effective_work_function_eV": "eV"
        }
      },
      "description": "Table of formation energies, HOMO, LUMO, and effective work function for all CNT systems. Each row corresponds to one model."
    }
  ],
  "notes": "The effective work function is defined as (LUMO - HOMO)/2. Formation energy of pure systems is zero. The checker will compare each quantity to hidden reference values and verify the trend that effective work function decreases with Si doping."
}
```

## How you are scored
After your job completes, a hidden verifier will read the `/app/outputs/results.csv` file and independently assess your computed quantities. It compares each numeric entry (formation energy, HOMO, LUMO, effective work function) against reference values derived from the original study, using tolerances that account for the DFT toolchain differences. Additionally, the verifier checks that certain structural relations hold among the models (for example, expected trends in effective work function with doping level). The final reward is a weighted combination of these checks: numeric accuracy and trend correctness carry the largest weight, while file format and schema compliance have a small weight. There is no credit for simply restating known numbers; the checker tests that your DFT workflow produced physically meaningful and consistent results.
