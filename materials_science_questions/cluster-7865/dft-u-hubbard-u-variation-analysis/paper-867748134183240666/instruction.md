# Electronic and Magnetic Properties of 3d TM-Doped Black and Blue Phosphorenes

## Problem background
Two-dimensional phosphorene allotropes (black and blue) are stable elemental semiconductors with promising electronic properties. Substitutional doping with 3d transition metals (Sc–Ni) can induce magnetism, potentially giving rise to dilute magnetic semiconductor or half-metal behaviors. Understanding how the TM impurity's electronic configuration and its hybridization with phosphorus defect states control the magnetic state is essential for designing phosphorene-based spintronic devices.

## Approach
This study employs first-principles density functional theory (DFT) calculations with the plane-wave pseudopotential method to examine substitutional 3d TM impurities in black and blue phosphorenes. The conceptual workflow consists of: (1) constructing a diamond-like 2×2 supercell of each phosphorene, (2) creating a phosphorus vacancy and relaxing the structure, (3) substituting a TM atom at the vacancy site and fully relaxing again, (4) performing spin-polarized DFT calculations using the PBE exchange‑correlation functional on all relaxed TM-doped systems, and (5) repeating the electronic structure calculations with the PBE+U method (applying literature on‑site Hubbard U corrections appropriate for each TM) to account for strong correlation effects. For each doped system the total spin moment, the local Mulliken spin moment on the TM, and the binding energy (defined as E_b = –(E_total – E_vacancy – E_isolated_TM)) are extracted. The band gap of the spin‑polarized system is analyzed to classify each configuration as a dilute magnetic semiconductor, a half-metal, or nonmagnetic.

## Reproduction target
For each 3d TM (Sc, Ti, V, Cr, Mn, Fe, Co, Ni) doped into black phosphorene and into blue phosphorene, compute the following quantities using both the PBE and PBE+U functionals:
- total spin moment (in μB)
- local Mulliken spin moment on the TM (in μB)
- binding energy (in eV)
- magnetic classification: one of "DMS" (dilute magnetic semiconductor), "half-metal", or "nonmagnetic"
Collect the results in the two JSON output files described in the workflow steps below.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE version): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build supercells
- Role: process
- Action: Construct 2x2 diamond-like supercells for black and blue phosphorenes using the lattice parameters provided in the paper. These serve as the starting structures for all subsequent calculations.
- Evidence: none

### Step 2: Relax pristine phosphorenes
- Role: process
- Action: Perform full geometry relaxation (ions and cell) for the pristine black and blue phosphorene supercells to obtain equilibrium lattice constants and atomic positions.
- Evidence: none

### Step 3: Create and relax phosphorus vacancy in black phosphorene
- Role: process
- Action: Introduce a single phosphorus vacancy in the relaxed black phosphorene supercell, then fully relax the structure. This relaxed vacancy configuration is used as the reference for TM substitution.
- Evidence: none

### Step 4: TM substitution and relaxation
- Role: process
- Action: For each 3d TM (Sc, Ti, V, Cr, Mn, Fe, Co, Ni), substitute the TM atom at the vacancy site of both black and blue phosphorenes, fully relax the structures, and compute the binding energy E_b = -(E_total - E_vacancy - E_isolated_TM). Save the relaxed coordinates of each doped system.
- Evidence: none

### Step 5: PBE electronic structure calculations
- Role: process
- Action: Run spin-polarized DFT calculations with the PBE functional for all relaxed TM-doped supercells. Extract the total spin moment, the local Mulliken spin moment on the TM, and determine the magnetic classification (dilute magnetic semiconductor, half-metal, or nonmagnetic).
- Evidence: none

### Step 6: PBE+U electronic structure calculations
- Role: process
- Action: Repeat the spin-polarized calculations using the PBE+U method with the literature U parameters (Sc 4.0, Ti 5.5, V 3.3, Cr 3.5, Mn 3.5, Fe 4.3, Co 3.3, Ni 6.5 eV). Record total spin moment, local moment, band gap, and classification.
- Evidence: none

### Step 7: Compile results for black phosphorene
- Role: scored (load-bearing)
- Action: Collect the computed properties from the PBE and PBE+U runs for all TMs in black phosphorene and write them into a single JSON file.
- Output file: `/app/outputs/results_black_phosphorene.json`
- Format: json
- Contract: Each top-level key is a TM element symbol (Sc,Ti,V,Cr,Mn,Fe,Co,Ni). Each value is an object with keys "PBE" and "PBE_U". Under each functional, the object has: "total_spin_moment" (float, in μB), "local_spin_moment" (float, Mulliken spin on TM, in μB), "binding_energy" (float, in eV), "classification" (string: "DMS", "half-metal", or "nonmagnetic").
- Scoring: scored by hidden verifier

### Step 8: Compile results for blue phosphorene
- Role: scored (load-bearing)
- Action: Analogous compilation for all TM-doped blue phosphorene systems.
- Output file: `/app/outputs/results_blue_phosphorene.json`
- Format: json
- Contract: Same structure as results_black_phosphorene.json: top-level keys Sc..Ni, each containing "PBE" and "PBE_U" objects with total_spin_moment (float, μB), local_spin_moment (float, μB), binding_energy (float, eV), classification (string: "DMS", "half-metal", "nonmagnetic").
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_black_phosphorene.json`
- `/app/outputs/results_blue_phosphorene.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_black_phosphorene.json
- path: `/app/outputs/results_black_phosphorene.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled spin moments, binding energies, and magnetic classification for black phosphorene from PBE and PBE+U calculations.
- schema:
  - `type`: object
  - `required`:
    - `Sc`: object
    - `Ti`: object
    - `V`: object
    - `Cr`: object
    - `Mn`: object
    - `Fe`: object
    - `Co`: object
    - `Ni`: object
  - `items`:
    - `PBE`: object
    - `PBE_U`: object
  - `unit`:
    - `total_spin_moment`: μB
    - `local_spin_moment`: μB
    - `binding_energy`: eV
    - `classification`: string

### results_blue_phosphorene.json
- path: `/app/outputs/results_blue_phosphorene.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled spin moments, binding energies, and magnetic classification for blue phosphorene from PBE and PBE+U calculations.
- schema:
  - `type`: object
  - `required`:
    - `Sc`: object
    - `Ti`: object
    - `V`: object
    - `Cr`: object
    - `Mn`: object
    - `Fe`: object
    - `Co`: object
    - `Ni`: object
  - `items`:
    - `PBE`: object
    - `PBE_U`: object
  - `unit`:
    - `total_spin_moment`: μB
    - `local_spin_moment`: μB
    - `binding_energy`: eV
    - `classification`: string

Notes: The checker compares the submitted values against the paper's reported results with appropriate tolerances on spin moments, exact classification matching, and binding energy trend correlation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_black_phosphorene.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Sc": "object",
          "Ti": "object",
          "V": "object",
          "Cr": "object",
          "Mn": "object",
          "Fe": "object",
          "Co": "object",
          "Ni": "object"
        },
        "items": {
          "PBE": "object",
          "PBE_U": "object"
        },
        "unit": {
          "total_spin_moment": "μB",
          "local_spin_moment": "μB",
          "binding_energy": "eV",
          "classification": "string"
        }
      },
      "description": "Compiled spin moments, binding energies, and magnetic classification for black phosphorene from PBE and PBE+U calculations."
    },
    {
      "file": "results_blue_phosphorene.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Sc": "object",
          "Ti": "object",
          "V": "object",
          "Cr": "object",
          "Mn": "object",
          "Fe": "object",
          "Co": "object",
          "Ni": "object"
        },
        "items": {
          "PBE": "object",
          "PBE_U": "object"
        },
        "unit": {
          "total_spin_moment": "μB",
          "local_spin_moment": "μB",
          "binding_energy": "eV",
          "classification": "string"
        }
      },
      "description": "Compiled spin moments, binding energies, and magnetic classification for blue phosphorene from PBE and PBE+U calculations."
    }
  ],
  "notes": "The checker compares the submitted values against the paper's reported results with appropriate tolerances on spin moments, exact classification matching, and binding energy trend correlation."
}
```

## How you are scored
A hidden verifier will read your `results_black_phosphorene.json` and `results_blue_phosphorene.json` files and compare the reported quantities to reference values. The verifier checks each component as follows:
- **Spin moments** – numeric agreement within reasonable tolerances (a better‑than‑reference value is not penalized).
- **Magnetic classification** – exact string match against the expected classification.
- **Binding energy trend** – consistency of the overall ranking across the 3d series (evaluated via a rank correlation).

The scoring is monotonic in quality: a result that meets or exceeds the hidden reference earns full credit for that component, while worse results receive proportionally lower credit. The final reward is a weighted sum with the following contributions: total spin moment 60%, magnetic classification 30%, binding energy trend 10%.
