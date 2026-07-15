# Computational Reproduction of Monolayer and Heterostructure Electronic and Optical Properties Using DFT

## Problem background
Two-dimensional (2D) layered materials and their van der Waals heterostructures can exhibit tunable electronic and optical properties when subjected to external perturbations such as strain and electric fields, making them promising candidates for optoelectronic devices. Understanding the stability of candidate monolayers and how their band gaps, refractive index, and optical absorption respond to these external controls is important for device design. This work studies a new monolayer, C₃As, and its heterostructure with arsenene using first-principles calculations to determine whether the monolayer is dynamically stable and to characterize the fundamental electronic and optical properties under equilibrium conditions as well as under vertical strain and external electric field.

## Approach
Use density functional theory (DFT) as implemented in the open-source Quantum Espresso code. The exchange-correlation interaction is treated at the generalized gradient approximation (GGA) level using the Perdew–Burke–Ernzerhof (PBE) functional, with the semi-empirical DFT-D3 van der Waals correction to capture weak interlayer interactions. Starting from the primitive unit cells of monolayer C₃As and arsenene, construct a 2×2 C₃As / 3×3 arsenene heterostructure supercell. Perform full geometry relaxation for the monolayers and the heterostructure. Compute the phonon dispersion of the relaxed C₃As monolayer via density-functional perturbation theory (DFPT) to assess dynamical stability (presence/absence of imaginary frequencies). Calculate the electronic band structure, projected density of states, and the complex dielectric function (yielding refractive index and optical absorption) for the relaxed monolayers and the equilibrium heterostructure. Then, for the heterostructure, repeat the electronic structure calculation under two additional external conditions: (i) increasing the interlayer vertical separation by +0.8 Å (vertical strain) while keeping in-plane lattice parameters fixed, and (ii) applying a sawtooth external electric field of +0.8 V/Å perpendicular to the layers, with dipole correction. Extract the target quantities described below from the resulting output files.

## Reproduction target
From the DFT calculations, extract and report in a single JSON file named results.json the following seven quantities:
- monolayer_bandgap_eV: the indirect band gap (eV) of the relaxed monolayer C₃As.
- monolayer_refractive_index: the static refractive index of monolayer C₃As.
- monolayer_first_absorption_peak_eV: the energy (eV) of the first optical absorption peak of monolayer C₃As.
- monolayer_max_imaginary_frequency_cm-1: the maximum imaginary phonon frequency (cm⁻¹) of the monolayer C₃As phonon dispersion; a negative or zero value indicates dynamical stability.
- heterostructure_bandgap_0strain_eV: the band gap (eV) of the C₃As/arsenene heterostructure at its relaxed equilibrium interlayer distance (no strain and no electric field).
- heterostructure_bandgap_plus0.8strain_eV: the band gap (eV) of the heterostructure when the interlayer distance is increased by +0.8 Å (vertical strain) relative to equilibrium.
- heterostructure_bandgap_plus0.8efield_eV: the band gap (eV) of the heterostructure under an external electric field of +0.8 V/Å applied perpendicular to the layers.

## Assets

- Quantum Espresso: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Structure relaxation
- Role: process
- Action: Perform DFT structure relaxation for monolayer C3As, arsenene monolayer, and C3As/arsenene heterostructure (2×2 C3As supercell on 3×3 arsenene supercell) using Quantum Espresso with PBE functional, DFT-D3 vdW correction, plane-wave kinetic energy cutoff 400 eV, Monkhorst–Pack k‑point mesh 25×25×1 for monolayers, 16×16×1 for bilayer, and 20 Å vacuum. Relax atomic positions and cell vectors until forces <1e-4 eV/Å and stress <1e-3 GPa.
- Evidence: `/app/outputs/relaxed_coordinates.xyz`

### Step 2: Phonon dispersion and stability
- Role: process
- Action: Calculate the phonon dispersion for the relaxed C3As monolayer via density-functional perturbation theory (DFPT) in Quantum Espresso. Verify that no imaginary frequencies appear (all modes real).
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 3: Equilibrium electronic band structure
- Role: process
- Action: Compute the electronic band structure and projected density of states for the relaxed monolayers (C3As, arsenene) and the relaxed heterostructure using the tetrahedron method and Blöchl corrections. Determine the band gap (value, nature indirect/direct, and k‑point location).
- Evidence: `/app/outputs/band_structure_eq.dat`

### Step 4: Optical properties (equilibrium)
- Role: process
- Action: Calculate the complex dielectric function, refractive index, and absorption spectrum for the relaxed monolayers and heterostructure. Extract the static refractive index and locate the energy of the first absorption peak.
- Evidence: `/app/outputs/optical_data_eq.dat`

### Step 5: Vertical strain simulations
- Role: process
- Action: For the relaxed heterostructure, increase the interlayer distance by +0.8 Å while keeping in-plane lattice constants fixed. Run an SCF calculation and band structure calculation at this strained geometry.
- Evidence: `/app/outputs/band_structure_strain_0.8.dat`

### Step 6: External electric field simulations
- Role: process
- Action: For the relaxed heterostructure, apply a sawtooth-like external electric field of +0.8 V/Å perpendicular to the layers using Quantum Espresso's 'tefield' or 'efield' functionality with appropriate dipole correction. Run an SCF calculation and band structure calculation.
- Evidence: `/app/outputs/band_structure_efield_0.8.dat`

### Step 7: Compile final quantities
- Role: scored (load-bearing)
- Action: From the output files of all previous steps, extract the following quantities and write them to a JSON file named 'results.json': monolayer C3As indirect band gap (eV), its static refractive index, its first optical absorption peak energy (eV), the maximum imaginary phonon frequency (cm⁻¹, must be ≤0 to indicate stability), the heterostructure band gap (eV) at equilibrium, the heterostructure band gap at +0.8 Å vertical strain, and the heterostructure band gap at +0.8 V/Å external electric field.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: { "monolayer_bandgap_eV": float, "monolayer_refractive_index": float, "monolayer_first_absorption_peak_eV": float, "monolayer_max_imaginary_frequency_cm-1": float, "heterostructure_bandgap_0strain_eV": float, "heterostructure_bandgap_plus0.8strain_eV": float, "heterostructure_bandgap_plus0.8efield_eV": float }
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
- description: JSON file containing the seven computed properties from the DFT workflow, to be compared against hidden paper-reported reference values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `monolayer_bandgap_eV`, `monolayer_refractive_index`, `monolayer_first_absorption_peak_eV`, `monolayer_max_imaginary_frequency_cm-1`, `heterostructure_bandgap_0strain_eV`, `heterostructure_bandgap_plus0.8strain_eV`, `heterostructure_bandgap_plus0.8efield_eV`
  - `properties`:
    - `monolayer_bandgap_eV`:
      - `type`: number
      - `unit`: eV
    - `monolayer_refractive_index`:
      - `type`: number
      - `unit`: dimensionless
    - `monolayer_first_absorption_peak_eV`:
      - `type`: number
      - `unit`: eV
    - `monolayer_max_imaginary_frequency_cm-1`:
      - `type`: number
      - `unit`: cm⁻¹
    - `heterostructure_bandgap_0strain_eV`:
      - `type`: number
      - `unit`: eV
    - `heterostructure_bandgap_plus0.8strain_eV`:
      - `type`: number
      - `unit`: eV
    - `heterostructure_bandgap_plus0.8efield_eV`:
      - `type`: number
      - `unit`: eV

Notes: Scored via result-level comparison (T0) to hidden paper gold with tolerances.

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
        "required": [
          "monolayer_bandgap_eV",
          "monolayer_refractive_index",
          "monolayer_first_absorption_peak_eV",
          "monolayer_max_imaginary_frequency_cm-1",
          "heterostructure_bandgap_0strain_eV",
          "heterostructure_bandgap_plus0.8strain_eV",
          "heterostructure_bandgap_plus0.8efield_eV"
        ],
        "properties": {
          "monolayer_bandgap_eV": {
            "type": "number",
            "unit": "eV"
          },
          "monolayer_refractive_index": {
            "type": "number",
            "unit": "dimensionless"
          },
          "monolayer_first_absorption_peak_eV": {
            "type": "number",
            "unit": "eV"
          },
          "monolayer_max_imaginary_frequency_cm-1": {
            "type": "number",
            "unit": "cm⁻¹"
          },
          "heterostructure_bandgap_0strain_eV": {
            "type": "number",
            "unit": "eV"
          },
          "heterostructure_bandgap_plus0.8strain_eV": {
            "type": "number",
            "unit": "eV"
          },
          "heterostructure_bandgap_plus0.8efield_eV": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "JSON file containing the seven computed properties from the DFT workflow, to be compared against hidden paper-reported reference values with appropriate tolerances."
    }
  ],
  "notes": "Scored via result-level comparison (T0) to hidden paper gold with tolerances."
}
```

## How you are scored
A hidden verifier checks each scored output. For results.json, each reported quantity is compared against a hidden reference value using appropriate tolerances. All seven quantities must pass their respective checks to receive full credit for this stage. The overall score is a weighted sum of the stage scores. Producing intermediate evidence files (relaxed coordinates, phonon dispersion, band structure, optical data, strained and field-dependent band structures) is required; their existence and basic structure are verified but they do not directly contribute to the numeric score. Only the seven quantities in results.json determine the final reward.
