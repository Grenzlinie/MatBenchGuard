# First-principles analysis of electronic and phonon properties of layered perovskite Cs3Bi2Br9

## Problem background
Cs3Bi2Br9 is a layered vacancy-ordered triple perovskite that exhibits strong exciton localization and room‑temperature vibronic photoluminescence. Its unusual electronic structure features contributions from Bi s and p states at the band edges, leading to indirect and direct band gaps. Phonon calculations reveal dynamical instabilities with soft modes at the zone centre. Understanding the band gaps, orbital character, and phonon properties is essential for explaining the exciton behaviour and the observed photoluminescence.

## Approach
First‑principles density functional theory (DFT) calculations are performed using the HSE06 hybrid functional with spin–orbit coupling (SOC) on the room‑temperature trigonal P‑3m1 crystal structure of Cs3Bi2Br9. The electronic band structure and atom‑projected density of states (PDOS) are computed to identify the indirect (Γ→A) and direct (Γ) band gaps and the dominant orbital character at the valence band maximum (VBM) and conduction band minimum (CBM). Phonon dispersion is calculated using density functional perturbation theory (DFPT) or the finite‑displacement method to obtain vibrational frequencies, with particular attention to the Γ point to detect imaginary (soft) modes that indicate a dynamical instability. The workflow uses the open‑source Quantum ESPRESSO code and appropriate pseudopotentials from the SSSP library.

## Reproduction target
Compute the HSE06+SOC electronic band structure and PDOS for Cs3Bi2Br9 (trigonal P‑3m1). From the band structure, determine the indirect band gap (Γ→A) and direct band gap (Γ) in eV. From the PDOS, identify the orbital character at the VBM and CBM. Compute the phonon dispersion and list any imaginary (negative) phonon frequencies at the Γ point. Output the numerical results to computational_results.json (indirect and direct gaps and negative frequencies) and orbital_character.txt (two lines describing the orbital character). The goal is to produce these quantities from independently run calculations; the hidden verifier will check them against established reference values.

## Assets

- Cs3Bi2Br9 trigonal P‑3m1 crystal structure: https://materialsproject.org/materials/mp-xxxxx/ (exact entry to be identified; also available via ICSD)
- Quantum ESPRESSO: https://www.quantum-espresso.org
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Prepare crystal structure
- Role: process
- Action: Obtain the room‑temperature trigonal P‑3m1 structure of Cs3Bi2Br9 from a public database (e.g., Materials Project or ICSD). If the structure is not fully relaxed, perform a DFT relaxation using a standard functional (e.g., PBE) to obtain equilibrium lattice parameters and atomic positions. Save the final structure as structure.cif.
- Evidence: `/app/outputs/structure.cif`

### Step 2: Compute electronic band structure and projected density of states (HSE06+SOC)
- Role: process
- Action: Using the prepared structure, run a HSE06+SOC DFT calculation with a suitable k‑point mesh to compute the electronic band structure along the high‑symmetry path including Γ and A, and the atom‑projected density of states (PDOS). Store the band structure data (k‑point coordinates and eigenvalues) in band_structure.dat and the PDOS data in pdos.dat.
- Evidence: `/app/outputs/band_structure.dat`

### Step 3: Compute phonon dispersion
- Role: process
- Action: Using the relaxed structure and DFT force constants (obtained via DFPT or finite‑displacement method), compute the phonon dispersion along the same high‑symmetry path, and obtain phonon frequencies for all q‑points, with special attention to the Γ point. Save q‑point coordinates and mode frequencies in phonon_dispersion.dat.
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 4: Extract band gaps and phonon instability into summary
- Role: scored (load-bearing)
- Action: Process the band structure data to determine the indirect band gap (Γ→A) and direct band gap (Γ). From the phonon dispersion, list all negative phonon frequencies at the Γ point. Write these quantities to computational_results.json with keys indirect_gap_ev (float), direct_gap_ev (float), and phonon_zone_center_negative_frequencies (list of floats in cm⁻¹).
- Output file: `/app/outputs/computational_results.json`
- Format: json
- Contract: {"indirect_gap_ev": <number>, "direct_gap_ev": <number>, "phonon_zone_center_negative_frequencies": [<number>, ...]}
- Scoring: scored by hidden verifier

### Step 5: Extract orbital character at band edges
- Role: scored
- Action: From the PDOS data, identify the dominant orbital compositions at the valence band maximum (VBM) and conduction band minimum (CBM). Write the result to orbital_character.txt as two lines, each beginning with "VBM: " or "CBM: " followed by a string describing the dominant atomic orbital contributions.
- Output file: `/app/outputs/orbital_character.txt`
- Format: txt
- Contract: Two lines; the first line starts with "VBM: " and contains a non-empty description; the second line starts with "CBM: " and contains a non-empty description.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computational_results.json`
- `/app/outputs/orbital_character.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computational_results.json
- path: `/app/outputs/computational_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Contains indirect and direct band gaps in eV and a list of negative phonon frequencies at the Γ point (in cm⁻¹). The verifier will recompute gaps from raw band structure data and compare both gaps and the negative list to hidden paper‑reported values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `indirect_gap_ev`: number (float)
    - `direct_gap_ev`: number (float)
    - `phonon_zone_center_negative_frequencies`: array of numbers (list of floats)

### orbital_character.txt
- path: `/app/outputs/orbital_character.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Two lines giving the orbital character at the VBM and CBM, as determined from the PDOS. The verifier performs exact string comparison against the hidden reference.
- schema:
  - `type`: text
  - `required`:
    - `line1`: must start with 'VBM: ' followed by a non-empty string
    - `line2`: must start with 'CBM: ' followed by a non-empty string

Notes: The verifier also checks the raw evidence files (band_structure.dat, pdos.dat, phonon_dispersion.dat) for structural integrity and recomputes the band gaps from them to ensure consistency with the summary file. No hidden gold values or tolerances are disclosed here; they reside in the grading specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computational_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "indirect_gap_ev": "number (float)",
          "direct_gap_ev": "number (float)",
          "phonon_zone_center_negative_frequencies": "array of numbers (list of floats)"
        }
      },
      "description": "Contains indirect and direct band gaps in eV and a list of negative phonon frequencies at the Γ point (in cm⁻¹). The verifier will recompute gaps from raw band structure data and compare both gaps and the negative list to hidden paper‑reported values with appropriate tolerances."
    },
    {
      "file": "orbital_character.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {
          "line1": "must start with 'VBM: ' followed by a non-empty string",
          "line2": "must start with 'CBM: ' followed by a non-empty string"
        }
      },
      "description": "Two lines giving the orbital character at the VBM and CBM, as determined from the PDOS. The verifier performs exact string comparison against the hidden reference."
    }
  ],
  "notes": "The verifier also checks the raw evidence files (band_structure.dat, pdos.dat, phonon_dispersion.dat) for structural integrity and recomputes the band gaps from them to ensure consistency with the summary file. No hidden gold values or tolerances are disclosed here; they reside in the grading specification."
}
```

## How you are scored
Each scored output file is evaluated by an automated verifier. For the band gaps, the verifier compares the computed values to hidden reference values using a threshold‑or‑better policy with a tolerance that accounts for method‑dependent variations; better‑than‑reference values are not penalized. The orbital character strings are checked for exact match against a hidden gold string. The list of negative phonon frequencies at Γ is checked for the presence of at least one imaginary mode (non‑empty list). The final reward is a weighted combination of these individual checks, with the majority of weight placed on the band gaps and phonon instability. You must genuinely run the calculations; the verifier will also cross‑check the summary files against the raw evidence you produce.
