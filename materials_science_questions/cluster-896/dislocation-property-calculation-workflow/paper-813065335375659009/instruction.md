# Dislocation Core Reconstruction Energies and Electronic Structure in Semiconductors

## Problem background
Dislocations in zinc-blende semiconductors can adversely affect electronic properties and are a critical factor in device miniaturisation. Dislocation mobility is a thermally activated process, and it is believed that the energetics of the dislocation core — in particular the reconstruction of dangling bonds — controls this mobility. Understanding the core reconstruction energy and the associated electronic states is therefore essential for predicting dislocation behaviour in materials such as silicon, gallium arsenide, and aluminium phosphide. This task targets the computation of core reconstruction energies for 30° partial dislocations and the characterisation of their electronic band structure, including the presence of gap states and their splitting upon reconstruction.

## Approach
The computational approach models a dislocation dipole containing two 30° partial dislocations inside a periodic supercell. For each material (Si, GaAs, AlP) and for each relevant core type (unreconstructed α, unreconstructed β, and fully reconstructed), a 96‑atom orthorhombic supercell is built with the dislocation line and glide plane defined by the crystal structure. Total energies are obtained from density functional theory (DFT) using the local density approximation (LDA), a plane‑wave basis set, and norm‑conserving pseudopotentials. Atomic positions are relaxed until Hellmann–Feynman forces fall below a tight threshold; an optional classical‑potential pre‑relaxation may accelerate convergence. The reconstruction energy per core bond is defined as the total‑energy difference between the relaxed unreconstructed configuration and the relaxed reconstructed configuration. For aluminium phosphide, additional electronic‑structure calculations are performed along the dislocation‑line reciprocal‑space direction using dense k‑point sampling, from which the bulk band gap, the nature (half‑filled or gapped) of the one‑dimensional band in the gap for the β core, the bonding–antibonding gap for the reconstructed β core, and the energy of the resonant level for the α core are extracted.

## Reproduction target
Compute and report the reconstruction energies (in eV per core bond) for 30° partial dislocations in Si, GaAs, and AlP. For Si, only the α core is required; for GaAs and AlP, both α and β cores are required. The energies must be written to `/app/outputs/reconstruction_energies.json`. Additionally, for AlP only, compute the electronic band structure of the dislocation cores and provide the following four properties in `/app/outputs/AlP_electronic_structure_results.json`: the bulk band gap (eV), whether the unreconstructed β core exhibits a half‑filled one‑dimensional band inside the gap (true/false), the bonding–antibonding gap (eV) for the reconstructed β core, and the energy (eV) of the α‑reconstructed resonant level relative to the valence‑band maximum. All outputs must adhere to the exact JSON schemas described in the workflow steps and output contract.

## Assets

- Quantum ESPRESSO (or an equivalent open‑source plane‑wave DFT code): https://www.quantum-espresso.org/
- Norm‑conserving pseudopotentials for Si, Al, P, Ga, As: http://www.pseudo-dojo.org/

## Workflow steps

### Step 1: Build supercell and initial dislocation core configurations
- Role: process
- Action: Construct a 96‑atom orthorhombic supercell containing a dislocation dipole of 30° partial dislocations in the {111} glide plane for Si, GaAs, and AlP. Create initial atomic positions for unreconstructed α, unreconstructed β, and fully reconstructed core configurations as described in the theoretical model (using the known bulk crystal structures, dislocation line direction, Burgers vector, and glide plane).
- Evidence: none

### Step 2: Relax structures using DFT
- Role: process
- Action: For each material (Si, GaAs, AlP) and each core configuration (unreconstructed α, unreconstructed β, reconstructed), perform DFT structural relaxation using LDA, a plane‑wave basis, norm‑conserving pseudopotentials, and a small k‑point mesh. Pre‑relaxation with a classical interatomic potential is optional. Relax until Hellmann–Feynman forces on all atoms are below 0.001 Ry/a.u. Save the final total energies and relaxed atomic coordinates.
- Evidence: `/app/outputs/dft_relaxation_log.txt`

### Step 3: Compute reconstruction energies
- Role: scored (load-bearing)
- Action: Compute the reconstruction energy per core bond (in eV) for each material and core type. For each 30° partial, take the total‑energy difference between the fully relaxed unreconstructed core configuration and the relaxed reconstructed configuration. Output a JSON file with the results.
- Output file: `/app/outputs/reconstruction_energies.json`
- Format: json
- Contract: JSON object with top‑level key 'materials' (array of objects). Each object has keys: 'material' (string, one of 'Si','GaAs','AlP'), 'core_type' (string, 'alpha' or 'beta'), 'reconstruction_energy_eV' (float, positive number). For Si only the α core is reported.
- Scoring: scored by hidden verifier

### Step 4: Compute AlP dislocation core electronic structure
- Role: scored (load-bearing)
- Action: Using the relaxed AlP structures from step2, compute the electronic eigenvalues along the dislocation‑line reciprocal vector with a dense set of k‑points. From the resulting band structure, extract: (1) the bulk band gap of AlP; (2) whether the unreconstructed β core exhibits a half‑filled 1D band inside the gap; (3) the bonding‑antibonding gap for the reconstructed β core; (4) the energy of the α reconstructed resonant level relative to the valence band maximum. Output these four quantities as a JSON file.
- Output file: `/app/outputs/AlP_electronic_structure_results.json`
- Format: json
- Contract: JSON object with keys: 'bulk_gap_eV' (float, positive), 'unreconstructed_beta_half_filled_band_present' (boolean), 'reconstructed_beta_bonding_antibonding_gap_eV' (float, positive), 'alpha_reconstructed_resonant_level_position_below_VBM_eV' (float, positive).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reconstruction_energies.json`
- `/app/outputs/AlP_electronic_structure_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reconstruction_energies.json
- path: `/app/outputs/reconstruction_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reconstruction energies per core bond for 30° partial dislocations in Si, GaAs, and AlP. The checker compares each entry to hidden reference values with tolerance ±0.1 eV and checks the required ordering (α energy < β energy for III‑V compounds).
- schema:
  - `type`: object
  - `required`:
    - `materials`: array
  - `items`:
    - `material`: string
    - `core_type`: string (alpha|beta)
    - `reconstruction_energy_eV`: float

### AlP_electronic_structure_results.json
- path: `/app/outputs/AlP_electronic_structure_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electronic structure features of AlP dislocation cores. The checker compares each value to hidden reference: bulk gap ~1.04 eV (±0.10 eV), half‑filled band present = true, β bonding‑antibonding gap ~0.15 eV (±0.05 eV), α resonant level ~4.0 eV below VBM (±0.5 eV).
- schema:
  - `type`: object
  - `required`:
    - `bulk_gap_eV`: float
    - `unreconstructed_beta_half_filled_band_present`: boolean
    - `reconstructed_beta_bonding_antibonding_gap_eV`: float
    - `alpha_reconstructed_resonant_level_position_below_VBM_eV`: float

Notes: The correlation with experimental activation energies is intentionally excluded from scoring. Only reconstruction energies and the described electronic structure features are scored. All tolerances are chosen to absorb legitimate methodological spread (code, functional, basis set).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reconstruction_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "materials": "array"
        },
        "items": {
          "material": "string",
          "core_type": "string (alpha|beta)",
          "reconstruction_energy_eV": "float"
        }
      },
      "description": "Reconstruction energies per core bond for 30° partial dislocations in Si, GaAs, and AlP. The checker compares each entry to hidden reference values with tolerance ±0.1 eV and checks the required ordering (α energy < β energy for III‑V compounds)."
    },
    {
      "file": "AlP_electronic_structure_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk_gap_eV": "float",
          "unreconstructed_beta_half_filled_band_present": "boolean",
          "reconstructed_beta_bonding_antibonding_gap_eV": "float",
          "alpha_reconstructed_resonant_level_position_below_VBM_eV": "float"
        }
      },
      "description": "Electronic structure features of AlP dislocation cores. The checker compares each value to hidden reference: bulk gap ~1.04 eV (±0.10 eV), half‑filled band present = true, β bonding‑antibonding gap ~0.15 eV (±0.05 eV), α resonant level ~4.0 eV below VBM (±0.5 eV)."
    }
  ],
  "notes": "The correlation with experimental activation energies is intentionally excluded from scoring. Only reconstruction energies and the described electronic structure features are scored. All tolerances are chosen to absorb legitimate methodological spread (code, functional, basis set)."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently checks each scored output file. For `reconstruction_energies.json`, the verifier compares every reported reconstruction energy to reference values with a predefined tolerance and verifies that the expected relative ordering (α energy lower than β energy for the III‑V compounds) holds. For `AlP_electronic_structure_results.json`, the verifier compares each of the four reported quantities to reference values, again with appropriate tolerances. The checks on both files are combined using a weighted scheme to produce a final reward between 0 and 1. Simply reporting numbers that match the paper is not sufficient — you must produce them through the prescribed computational workflow, and the verifier will validate the structure and content of the artifacts you submit.
