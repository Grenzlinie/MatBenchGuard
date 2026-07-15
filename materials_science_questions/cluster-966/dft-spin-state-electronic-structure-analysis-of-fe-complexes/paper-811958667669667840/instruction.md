# DFT and TDDFT study of porphyrin-like eumelanin tetramer formation, optical spectra, and stacking

## Problem background
Eumelanin is a widespread biological pigment whose molecular structure and the origin of its broad, featureless optical absorption remain incompletely understood. This work examines a porphyrin-like tetramer model built from indolequinone (IQ) and its tautomers (including quinone-methide, MQ), linked via C2–C7′ bonds. The goal is to use first-principles density functional theory (DFT) and time-dependent DFT (TDDFT) to compute the relative formation energies along the proposed synthesis pathway, the optical absorption spectra from monomers to stacked oligomers, and the stacking energetics, thereby assessing whether the computational results are consistent with the structural model.

## Approach
The conceptual approach is to perform all-electron-like DFT calculations with the SIESTA code using the local density approximation (LDA) for exchange-correlation, a double-ζ polarized (DZP) basis set, and Troullier–Martins norm-conserving pseudopotentials. Molecular structures for the IQ monomer, MQ monomer, IQ–IQ (II) dimer, IQ–MQ (IMa) dimer, a rotated IMb dimer, an IMIM tetramer with an inner porphyrin-like ring, and a planar stacked IMIM–IMIM octamer are built following the C2–C7′ bonding rule and an interlayer separation of ~3.0–3.3 Å. Each system is relaxed to its ground-state geometry and its total energy recorded, along with that of an isolated H₂ molecule. Relative formation energies are derived from these total energies using H₂ as the hydrogen reservoir. Linear-response TDDFT is then employed to obtain optical absorption spectra over 200–900 nm. From these spectra, the main absorption peaks are identified and the integrated dipole strength per monomer unit over 250–600 nm is computed. Finally, the stacking energy of the planar stacked octamer is evaluated as the difference between its total energy and twice the energy of the isolated tetramer.

## Reproduction target
Compute the following quantities from the DFT and TDDFT calculations:
- Formation energies (all in eV):
  - E_rel_II = E(II) + E(H₂) − 2·E(IQ)
  - E_rel_IMa_vs_II = E(IMa) − E(II)
  - E_rot = E(IMb) − E(IMa)
  - E_MQ_vs_IQ = E(MQ) − E(IQ)
- Optical absorption spectra for the IQ monomer, II dimer, IMa dimer, IMb dimer, IMIM tetramer, and the planar stacked IMIM–IMIM octamer. From these spectra, extract the main absorption peaks (wavelength in nm and relative intensity 0–1) for each species and the integrated transition dipole strength per monomer unit (Debye²) over the 250–600 nm range.
- Stacking energy of the planar stacked IMIM–IMIM octamer: E_stacking = E(octamer) − 2·E(IMIM_tetramer).

## Assets

- SIESTA DFT code: https://siesta-project.org/siesta/
- Troullier-Martins pseudopotentials for H, C, N, O: SIESTA pseudopotential database (e.g. Pseudo-Dojo)
- Atomic Simulation Environment (ASE): pip install ase
- Molecular structure definitions (IQ, MQ, dimers, tetramers, stacked octamer)

## Workflow steps

### Step 1: Build initial molecular geometries
- Role: process
- Action: Construct initial atomic coordinates for: isolated IQ monomer, isolated MQ monomer, IQ-IQ (II) dimer, IQ-MQ (IMa) dimer, rotated IMb dimer, IMIM tetramer, and the planar stacked IMIM-IMIM octamer. Follow the C2-C7' bonding rule, porphyrin-like ring, and parallel stacking with interlayer distance ~3.0-3.3 Å.
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: DFT geometry optimization and total energy calculation
- Role: process
- Action: For each species from step_01, run DFT geometry optimization with SIESTA using LDA functional, DZP basis set, and Troullier-Martins pseudopotentials, until forces are converged. Also compute the total energy of an isolated H2 molecule at the same level of theory. Save the final optimized geometries and total energies.
- Evidence: `/app/outputs/total_energies.json`

### Step 3: Calculate formation energies
- Role: scored (load-bearing)
- Action: Using the total energies from step_02, compute the following relative energies (all in eV) with H2 as hydrogen reservoir: (1) E_rel_II = E(II) + E(H2) - 2*E(IQ), (2) E_rel_IMa_vs_II = E(IMa) - E(II), (3) E_rot = E(IMb) - E(IMa), (4) E_MQ_vs_IQ = E(MQ) - E(IQ). Output a JSON file with these four values.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: Object with keys: E_rel_II (float, eV), E_rel_IMa_vs_II (float, eV), E_rot (float, eV), E_MQ_vs_IQ (float, eV).
- Scoring: scored by hidden verifier

### Step 4: Compute TDDFT optical absorption spectra
- Role: process
- Action: For the optimized structures from step_02, run linear-response TDDFT with SIESTA using the same functional/basis, to compute the optical absorption spectrum in the range 200-900 nm for: IQ monomer, II dimer, IMa dimer, IMb dimer, IMIM tetramer, and the planar stacked IMIM-IMIM octamer. Save the wavelength (nm) vs. absorption intensity data for each species.
- Evidence: `/app/outputs/spectra_raw.json`

### Step 5: Extract absorption peak positions
- Role: scored
- Action: From the raw spectra generated in step_04, identify the main absorption peaks (wavelengths with significant intensity) for each species: IQ monomer, II dimer, IMa dimer, IMb dimer, IMIM tetramer, and the planar stacked octamer. Output a JSON file listing, for each species, an array of peak objects with wavelength (nm) and relative intensity (0-1).
- Output file: `/app/outputs/absorption_peaks.json`
- Format: json
- Contract: Object with species IDs as keys, each mapping to a list of {wavelength_nm: float, intensity: float}.
- Scoring: scored by hidden verifier

### Step 6: Compute integrated dipole strengths per monomer
- Role: scored
- Action: Using the raw spectra from step_04, integrate the absorption intensity over the wavelength range 250-600 nm and divide by the number of monomer units in each species to obtain the transition dipole strength per monomer (Debye^2). Report the value for IQ monomer, II dimer, IMa dimer, IMb dimer, IMIM tetramer, and the planar stacked octamer.
- Output file: `/app/outputs/dipole_strength.json`
- Format: json
- Contract: Object with species IDs as keys and integrated dipole strength per monomer unit (Debye^2) as float.
- Scoring: scored by hidden verifier

### Step 7: Calculate planar stacking energy
- Role: scored (load-bearing)
- Action: From the total energies obtained in step_02, compute the stacking energy of the planar stacked IMIM-IMIM octamer: E_stacking = E(octamer) - 2*E(IMIM_tetramer). Report this value in eV.
- Output file: `/app/outputs/stacking_energy.json`
- Format: json
- Contract: Object with key 'planar_stacking_energy_eV' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/absorption_peaks.json`
- `/app/outputs/dipole_strength.json`
- `/app/outputs/stacking_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: DFT formation energies along the synthesis pathway, scored by comparison to paper values within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `E_rel_II`: number (eV)
    - `E_rel_IMa_vs_II`: number (eV)
    - `E_rot`: number (eV)
    - `E_MQ_vs_IQ`: number (eV)

### absorption_peaks.json
- path: `/app/outputs/absorption_peaks.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Main absorption peak positions from TDDFT, checked for ordering and presence of characteristic peaks.
- schema:
  - `type`: object
  - `required`: object
  - `items`:
    - `wavelength_nm`: float
    - `intensity`: float (0-1)
  - `description`: Species names as top-level keys, each mapping to an array of peak objects.

### dipole_strength.json
- path: `/app/outputs/dipole_strength.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Dipole strength per monomer, scored by the trend (increase from monomer to tetramer, decrease upon stacking) relative to paper data.
- schema:
  - `type`: object
  - `required`: object
  - `description`: Species names as keys mapping to integrated dipole strength per monomer unit (Debye^2).

### stacking_energy.json
- path: `/app/outputs/stacking_energy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Stacking energy of the planar stacked IMIM-IMIM octamer, compared to paper value within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `planar_stacking_energy_eV`: number (eV)

Notes: The task reproduces formation energies, absorption peaks, dipole strengths, and stacking energy as reported in the paper. Exact values are hidden; scoring uses tolerances and trend checks appropriate for a re-run with different implementation.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E_rel_II": "number (eV)",
          "E_rel_IMa_vs_II": "number (eV)",
          "E_rot": "number (eV)",
          "E_MQ_vs_IQ": "number (eV)"
        }
      },
      "description": "DFT formation energies along the synthesis pathway, scored by comparison to paper values within tolerance."
    },
    {
      "file": "absorption_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {},
        "items": {
          "wavelength_nm": "float",
          "intensity": "float (0-1)"
        },
        "description": "Species names as top-level keys, each mapping to an array of peak objects."
      },
      "description": "Main absorption peak positions from TDDFT, checked for ordering and presence of characteristic peaks."
    },
    {
      "file": "dipole_strength.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {},
        "description": "Species names as keys mapping to integrated dipole strength per monomer unit (Debye^2)."
      },
      "description": "Dipole strength per monomer, scored by the trend (increase from monomer to tetramer, decrease upon stacking) relative to paper data."
    },
    {
      "file": "stacking_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "planar_stacking_energy_eV": "number (eV)"
        }
      },
      "description": "Stacking energy of the planar stacked IMIM-IMIM octamer, compared to paper value within tolerance."
    }
  ],
  "notes": "The task reproduces formation energies, absorption peaks, dipole strengths, and stacking energy as reported in the paper. Exact values are hidden; scoring uses tolerances and trend checks appropriate for a re-run with different implementation."
}
```

## How you are scored
A hidden verifier independently compares each of your submitted artifacts (formation energies, absorption peaks, dipole strengths, and stacking energy) to reference values derived from the original study. Comparisons use numerical tolerances that account for differences in implementation and numerical settings, and also check relative trends (e.g., ordering of peak positions, presence of hyperchroism upon polymerization and hypochroism upon stacking) where applicable. The final reward is a weighted average of the scores for the individual stages, with the formation energies and stacking energy carrying the largest weight.
