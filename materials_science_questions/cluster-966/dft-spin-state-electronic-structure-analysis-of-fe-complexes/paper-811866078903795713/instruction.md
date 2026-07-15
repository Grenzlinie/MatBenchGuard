# Fe-C(carbene) bond dissociation energy and NMR shifts via DFT/CCSD(T)

## Problem background
Iron tetracarbonyl carbene complexes such as (CO)4FeCF2 serve as model systems for Fischer-type metal‑carbene bonding. Because experimental isolation and NMR characterization of this monomeric complex have been challenging, computational methods are used to predict its ground‑state geometry, Fe–C bond strength, and 13C and 19F NMR chemical shifts, including the anisotropy of the carbenic carbon resonance. Reproducing these predictions provides insight into the electronic structure and reactivity of this class of complexes.

## Approach
The workflow follows a multi‑stage computational protocol. First, geometries of all relevant species—the equatorial and axial isomers of (CO)4FeCF2, Fe(CO)5, Fe(CO)4 (singlet and triplet), CF2 (singlet and triplet), and CO—are optimized at the BP86 density functional level using the BS‑A basis set, and harmonic vibrational frequencies are computed to obtain zero‑point energy corrections. Second, single‑point coupled‑cluster CCSD(T)/BS‑A calculations (frozen core) are performed on the optimized geometries to obtain accurate total energies. From these, the zero‑point‑corrected bond dissociation energies D0 are derived for the Fe–C bond in (CO)4FeCF2 (relative to singlet Fe(CO)4 and singlet CF2) and for the Fe–CO bond in Fe(CO)5 (relative to singlet Fe(CO)4 and CO), together with the energy difference between the equatorial and axial isomers. Third, GIAO‑based NMR shielding tensors are calculated at the B3LYP/BS‑C level for the equatorial isomer (1b) and for the reference molecules CH4 and HF. The isotropic 13C chemical shifts (relative to CH4) and 19F chemical shift (relative to CCl3F, using HF as a secondary reference) are then extracted, along with the principal components of the 13C chemical shift tensor for the carbenic carbon atom.

## Reproduction target
Produce three scored output files. (1) `/app/outputs/bde_results.json`: containing D0 for (CO)4FeCF2 (kcal/mol), D0 for Fe(CO)5 (kcal/mol), and the equatorial−axial isomer energy difference (kcal/mol). (2) `/app/outputs/nmr_shifts.json`: containing the isotropic 13C chemical shifts (ppm) for the axial CO, equatorial CO, average CO, and carbene carbon of the equatorial isomer, and the 19F chemical shift (ppm). (3) `/app/outputs/anisotropy_components.json`: containing the three principal components δ_YY, δ_XX, δ_ZZ (ppm) of the 13C chemical shift tensor for the carbenic carbon. All quantities must be computed at the specified theoretical levels (CCSD(T)/BS‑A//BP86/BS‑A for BDEs and isomer energy; B3LYP/BS‑C for NMR shifts and anisotropy).

## Assets

- ORCA quantum chemistry package (or equivalent): https://orcaforum.kofo.mpg.de/

## Basis sets

The workflow employs two basis sets defined in the original study:

- BS-A (used for geometry optimizations, frequency calculations, and CCSD(T) single-point energies):
  - Fe: Hay and Wadt small‑core effective core potential (ECP) with valence basis set (441/2111/41).
  - Other atoms (C, O, F): 6‑31G(d).
- BS-C (used for GIAO NMR shielding calculations):
  - Fe: Stuttgart ECP with larger valence basis set (311111/2111/411).
  - C, O, F: Bochum basis set (contractions: H (5s1p)/[3s1p] {311/1}, C (9s5p1d)/[5s4p1d] {51111/2111/1}, O (9s5p1d)/[5s4p1d] {51111/2111/1}, F (9s5p1d)/[5s4p1d] {51111/2111/1}).

These basis sets are publicly available and can be constructed from the basis set exchange or from the literature.

## Workflow steps

### Step 1: Geometry optimization at BP86/BS-A
- Role: process
- Action: Perform geometry optimization and harmonic vibrational frequency calculation at the BP86/BS-A level for all species: (CO)4FeCF2 equatorial (1b) and axial (1a) isomers, Fe(CO)5 (2), Fe(CO)4 singlet (3a) and triplet (3b), CF2 singlet and triplet, and CO. Keep optimized geometries and zero-point vibrational energies.
- Evidence: `/app/outputs/geom_optimizations.log`

### Step 2: CCSD(T)/BS-A single-point energies
- Role: process
- Action: Using the optimized geometries, perform single-point CCSD(T)/BS-A energy calculations (frozen core approximation) for all species. Record total electronic energies.
- Evidence: `/app/outputs/ccsdt_calculations.log`

### Step 3: Bond dissociation energy and isomer energy difference
- Role: scored (load-bearing)
- Action: From the CCSD(T) total energies and BP86 zero-point energies, compute the electronic and ZPE-corrected bond dissociation energy D0 for (CO)4FeCF2 (1b) relative to singlet Fe(CO)4 and singlet CF2, and for Fe(CO)5 (2) relative to singlet Fe(CO)4 and CO. Also compute the energy difference between the equatorial (1b) and axial (1a) isomers. Output a JSON file with the three values.
- Output file: `/app/outputs/bde_results.json`
- Format: json
- Contract: {"D0_1b_kcal_per_mol": number, "D0_2_kcal_per_mol": number, "energy_difference_1b_minus_1a_kcal_per_mol": number}
- Scoring: scored by hidden verifier

### Step 4: GIAO NMR shielding calculation at B3LYP/BS-C
- Role: process
- Action: Perform GIAO NMR shielding tensor calculations at the B3LYP/BS-C level for (CO)4FeCF2 (1b), Fe(CO)5 (2), CH4 (primary reference for 13C), and HF (secondary reference for 19F) using the BP86/BS-A optimized geometry of 1b and 2.
- Evidence: `/app/outputs/nmr_shielding_output.log`

### Step 5: 13C and 19F chemical shifts
- Role: scored
- Action: From the GIAO shielding tensors, compute the 13C chemical shifts (relative to CH4) for the axial CO, equatorial CO, average CO, and carbene carbon of 1b. Compute the 19F chemical shift for 1b (relative to CCl3F via HF with a correction of -214 ppm). Output a JSON file with the five chemical shift values.
- Output file: `/app/outputs/nmr_shifts.json`
- Format: json
- Contract: {"13C_carbene_shift_ppm": number, "13C_axial_CO_shift_ppm": number, "13C_equatorial_CO_shift_ppm": number, "13C_average_CO_shift_ppm": number, "19F_shift_ppm": number}
- Scoring: scored by hidden verifier

### Step 6: 13C chemical shift anisotropy components for carbene carbon
- Role: scored
- Action: From the GIAO shielding tensor of the carbene carbon in 1b, extract the principal components (δ_YY, δ_XX, δ_ZZ) of the 13C chemical shift tensor relative to CH4. Output a JSON file with the three values.
- Output file: `/app/outputs/anisotropy_components.json`
- Format: json
- Contract: {"delta_YY_ppm": number, "delta_XX_ppm": number, "delta_ZZ_ppm": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bde_results.json`
- `/app/outputs/nmr_shifts.json`
- `/app/outputs/anisotropy_components.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bde_results.json
- path: `/app/outputs/bde_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bond dissociation energies (D0) and isomer energy difference computed from CCSD(T)/BS-A energies and BP86/BS-A zero-point corrections.
- schema:
  - `type`: object
  - `required`:
    - `D0_1b_kcal_per_mol`: number
    - `D0_2_kcal_per_mol`: number
    - `energy_difference_1b_minus_1a_kcal_per_mol`: number
  - `units`:
    - `D0_1b_kcal_per_mol`: kcal/mol
    - `D0_2_kcal_per_mol`: kcal/mol
    - `energy_difference_1b_minus_1a_kcal_per_mol`: kcal/mol

### nmr_shifts.json
- path: `/app/outputs/nmr_shifts.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: 13C and 19F NMR chemical shifts for (CO)4FeCF2 (1b) calculated at B3LYP/BS-C level.
- schema:
  - `type`: object
  - `required`:
    - `13C_carbene_shift_ppm`: number
    - `13C_axial_CO_shift_ppm`: number
    - `13C_equatorial_CO_shift_ppm`: number
    - `13C_average_CO_shift_ppm`: number
    - `19F_shift_ppm`: number
  - `units`:
    - `13C_carbene_shift_ppm`: ppm
    - `13C_axial_CO_shift_ppm`: ppm
    - `13C_equatorial_CO_shift_ppm`: ppm
    - `13C_average_CO_shift_ppm`: ppm
    - `19F_shift_ppm`: ppm

### anisotropy_components.json
- path: `/app/outputs/anisotropy_components.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Principal components of the 13C chemical shift tensor for the carbene carbon in 1b.
- schema:
  - `type`: object
  - `required`:
    - `delta_YY_ppm`: number
    - `delta_XX_ppm`: number
    - `delta_ZZ_ppm`: number
  - `units`:
    - `delta_YY_ppm`: ppm
    - `delta_XX_ppm`: ppm
    - `delta_ZZ_ppm`: ppm

Notes: All scored values are compared against the paper's reported numbers with appropriate tolerances. The agent should use an open‑source quantum chemistry package (e.g., ORCA) and construct the basis sets (BS‑A, BS‑C) according to the paper's description, which are publicly available.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bde_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "D0_1b_kcal_per_mol": "number",
          "D0_2_kcal_per_mol": "number",
          "energy_difference_1b_minus_1a_kcal_per_mol": "number"
        },
        "units": {
          "D0_1b_kcal_per_mol": "kcal/mol",
          "D0_2_kcal_per_mol": "kcal/mol",
          "energy_difference_1b_minus_1a_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Bond dissociation energies (D0) and isomer energy difference computed from CCSD(T)/BS-A energies and BP86/BS-A zero-point corrections."
    },
    {
      "file": "nmr_shifts.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "13C_carbene_shift_ppm": "number",
          "13C_axial_CO_shift_ppm": "number",
          "13C_equatorial_CO_shift_ppm": "number",
          "13C_average_CO_shift_ppm": "number",
          "19F_shift_ppm": "number"
        },
        "units": {
          "13C_carbene_shift_ppm": "ppm",
          "13C_axial_CO_shift_ppm": "ppm",
          "13C_equatorial_CO_shift_ppm": "ppm",
          "13C_average_CO_shift_ppm": "ppm",
          "19F_shift_ppm": "ppm"
        }
      },
      "description": "13C and 19F NMR chemical shifts for (CO)4FeCF2 (1b) calculated at B3LYP/BS-C level."
    },
    {
      "file": "anisotropy_components.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_YY_ppm": "number",
          "delta_XX_ppm": "number",
          "delta_ZZ_ppm": "number"
        },
        "units": {
          "delta_YY_ppm": "ppm",
          "delta_XX_ppm": "ppm",
          "delta_ZZ_ppm": "ppm"
        }
      },
      "description": "Principal components of the 13C chemical shift tensor for the carbene carbon in 1b."
    }
  ],
  "notes": "All scored values are compared against the paper's reported numbers with appropriate tolerances. The agent should use an open‑source quantum chemistry package (e.g., ORCA) and construct the basis sets (BS‑A, BS‑C) according to the paper's description, which are publicly available."
}
```

## How you are scored
A hidden verifier reads your three JSON artifacts and compares each reported numeric value to pre‑established reference results derived from the original study. The comparison uses quantity‑specific tolerances that account for legitimate differences due to choice of quantum chemistry package and numerical settings. Each artifact contributes a fixed weight to the final reward, which is a single float between 0 and 1. You must execute the full computational pipeline, because the verifier expects the artifacts to be the output of those calculations; simply guessing or reporting unrelated numbers will yield a low score.
