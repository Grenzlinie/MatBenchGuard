# Formation energies and migration barriers of vacancy clusters in diamond

## Problem background
In diamond, the aggregation of diffusing monovacancies (V1) into divacancies (V2) is a fundamental step in the evolution of vacancy clusters. These clusters influence the formation of nitrogen‑vacancy (NV) centers, which are widely used for quantum sensing, bio‑imaging, and other applications. This task investigates the energetics of the intermediate vacancy isomers that appear along the pathway from two isolated V1 to a bound V2. Using density functional theory (DFT) and the nudged elastic band (NEB) method, we aim to compute the formation energies of the relevant vacancy structures and the migration barriers that govern which routes are kinetically accessible. The goal is to determine, from first principles, the relative stability of these isomers and the energy landscape of the divacancy formation process.

## Approach
The approach uses plane‑wave DFT with the PBE exchange‑correlation functional and a Vanderbilt ultrasoft pseudopotential for carbon, as implemented in the open‑source Quantum ESPRESSO (PWscf) code. All calculations employ a cubic supercell that is large enough to isolate a defect, with Brillouin‑zone sampling at the Γ‑point. 

First, geometry optimisations are performed for the pristine diamond supercell and for each vacancy defect: monovacancy (V1), divacancy (V2), and the isomers 2C, 2O, 3C, 3E, 3A, and 1I. Spin‑restricted and spin‑polarised relaxations are carried out to identify the lowest‑energy spin state of each species. Formation energies are then computed relative to the pristine crystal. 

Next, reaction paths connecting key intermediates are mapped with the climbing‑image nudged elastic band method, using spin‑restricted DFT. The transitions studied are 3E→2O, 3A→2O, 3C→2C, 2C→V2, and 2O→V2. After locating the transition‑state geometries, spin‑polarised single‑point energy calculations on those geometries provide spin‑corrected activation barriers. The reported reaction energies and barriers reflect the difference between the ground‑state energies of the reactants and products, as well as the corrected barrier height.

## Reproduction target
Produce two JSON artifacts under `/app/outputs`:

1. `formation_energies.json` – an object with keys "V1", "V2", "2C", "2O", "3C", "3E", "3A". Each value is a float in eV representing the formation energy of that defect in its lowest‑energy spin state. The formation energy for species with n vacancies is defined as E_f^n = E_vac^n – ((N–n)/N) · E_cryst^N, where N = 216 is the number of atoms in the ideal supercell, E_vac^n is the total energy of the relaxed defect supercell, and E_cryst^N is the total energy of the relaxed pristine supercell.

2. `migration_barriers.json` – an object with keys "3E→2O", "3A→2O", "3C→2C", "2C→V2", "2O→V2". Each value is an object containing the spin‑corrected reaction energy ("E_R", in eV) and the activation barrier ("barrier", in eV) for that elementary step. The reaction energy is computed as the difference in the lowest‑energy spin states of product and reactant; the barrier is computed as the difference between the spin‑polarised energy of the transition state and the energy of the lowest‑energy spin state of the reactant.

## Assets

- Quantum ESPRESSO (PWscf): https://www.quantum-espresso.org/
- C.pbe-n-rrkjus_psl.1.0.0.UPF (Vanderbilt ultrasoft pseudopotential): https://www.quantum-espresso.org/pseudo-search-results/?el_id=6&unp_id&fun_id&colum_k&origin_id
- Ideal diamond crystal structure

## Workflow steps

### Step 1: Prepare defect supercells
- Role: process
- Action: Generate initial 216-atom cubic supercell coordinates for pristine diamond and for the vacancy defects: monovacancy (V1), divacancy (V2), and the isomers 2C, 2O, 3C, 3E, 3A, and 1I by removing the appropriate carbon atoms from the ideal lattice. Ensure the supercell size is large enough to isolate the defect.
- Evidence: `/app/outputs/coordinates.log`

### Step 2: DFT geometry optimization and formation energies
- Role: scored
- Action: Perform spin-restricted and spin-polarized DFT geometry relaxations using Quantum ESPRESSO with PBE, Vanderbilt ultrasoft pseudopotential, 216-atom cubic supercell, Γ-point, kinetic energy cutoff 48 Ry, charge density cutoff 348 Ry. For each defect species determine the lowest-energy spin state, compute the formation energy via E_f^n = E_vac^n - ((N-n)/N) * E_cryst^N (where N=216), and write the results to formation_energies.json.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: JSON object with keys: "V1", "V2", "2C", "2O", "3C", "3E", "3A"; each value is a float representing the formation energy in eV.
- Scoring: scored by hidden verifier

### Step 3: NEB reaction pathway calculations
- Role: process
- Action: Using the optimized structures from step_formation as endpoints, run climbing-image NEB with spin-restricted PBE for the transitions 3E→2O, 3A→2O, 3C→2C, 2C→V2, and 2O→V2. Use at least 5 intermediate images, force convergence 0.05 eV/Å orthogonal to the path. Archive the transition-state geometries and raw energy profiles.
- Evidence: `/app/outputs/neb_output.log`

### Step 4: Spin-corrected migration barriers and reaction energies
- Role: scored (load-bearing)
- Action: For each NEB transition, take the transition-state geometry, perform a single spin-polarized single-point DFT energy calculation. Compute the spin-corrected activation barrier as the difference between the spin-polarized TS energy and the energy of the lowest-energy spin state of the reactant, and the reaction energy as the difference between the lowest-energy spin states of products and reactants. Output the values to migration_barriers.json.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: JSON object with keys: "3E→2O", "3A→2O", "3C→2C", "2C→V2", "2O→V2". Each value is an object with keys "E_R" (float, eV) and "barrier" (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies of monovacancy, divacancy and intermediate vacancy isomers computed from DFT geometry optimization.
- schema:
  - `type`: object
  - `required`:
    - `V1`: float (eV)
    - `V2`: float (eV)
    - `2C`: float (eV)
    - `2O`: float (eV)
    - `3C`: float (eV)
    - `3E`: float (eV)
    - `3A`: float (eV)
  - `items`: object

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spin-corrected reaction energies and activation barriers for the elementary divacancy formation steps obtained from NEB and spin-polarized single-point calculations.
- schema:
  - `type`: object
  - `required`:
    - `3E→2O`: object
    - `3A→2O`: object
    - `3C→2C`: object
    - `2C→V2`: object
    - `2O→V2`: object
  - `items`:
    - `E_R`: float (eV)
    - `barrier`: float (eV)

Notes: The monovacancy diffusion barrier along [111] is not required; the task focuses on the divacancy aggregation pathway. The 1I isomer is verified to be not a local minimum; its formation energy is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "V1": "float (eV)",
          "V2": "float (eV)",
          "2C": "float (eV)",
          "2O": "float (eV)",
          "3C": "float (eV)",
          "3E": "float (eV)",
          "3A": "float (eV)"
        },
        "items": {}
      },
      "description": "Formation energies of monovacancy, divacancy and intermediate vacancy isomers computed from DFT geometry optimization."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "3E→2O": "object",
          "3A→2O": "object",
          "3C→2C": "object",
          "2C→V2": "object",
          "2O→V2": "object"
        },
        "items": {
          "E_R": "float (eV)",
          "barrier": "float (eV)"
        }
      },
      "description": "Spin-corrected reaction energies and activation barriers for the elementary divacancy formation steps obtained from NEB and spin-polarized single-point calculations."
    }
  ],
  "notes": "The monovacancy diffusion barrier along [111] is not required; the task focuses on the divacancy aggregation pathway. The 1I isomer is verified to be not a local minimum; its formation energy is not scored."
}
```

## How you are scored
A hidden verifier will independently read your `formation_energies.json` and `migration_barriers.json` and compare the numerical values to the reference results originally reported for the same workflow. Each artifact carries a weight; the final score (a number between 0 and 1) measures how well your computed numbers agree with the reference, using appropriate tolerances that account for typical differences between DFT implementations. The closer your results are to the reference, the higher your score. There is no partial credit for simply running the workflow – the numeric agreement with the hidden reference determines your reward.
