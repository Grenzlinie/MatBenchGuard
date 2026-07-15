# DFT Calculation of Raman Blue Shifts in Twisted Bilayer Black Phosphorus

## Problem background
Black phosphorus (BP) is a layered two‑dimensional material with strong in‑plane anisotropy and layer‑dependent phonon properties. When two BP layers are stacked with a relative twist angle, the resulting moiré superlattice may modify the interlayer coupling and influence the Raman‑active vibrational modes, notably the A_g^1 and A_g^2 modes. Density functional theory (DFT) calculations allow the determination of phonon frequencies and Raman intensities for such twisted heterostructures, providing a theoretical window into the interlayer interactions. This task investigates the Raman‑mode wavenumbers in a 70.53° twisted bilayer black phosphorus compared with an untwisted bilayer configuration.

## Approach
The core method is a first‑principles DFT workflow. First, the crystal structures are constructed for both an untwisted bilayer BP and the 70.53° twisted bilayer BP superlattice (the simplest coincidence‑site lattice case, p=q=1) using the CSL theory. Then, using the Quantum ESPRESSO package with the PBE functional and norm‑conserving pseudopotentials for phosphorus, geometry relaxation (if needed) is followed by Γ‑point phonon calculations. The resulting phonon frequencies and Raman intensities are extracted. For the untwisted bilayer, the Ag¹ and Ag² modes are identified by their irreducible representations; for the twisted bilayer, the two Raman‑active A‑symmetry modes with the highest intensity in the relevant frequency windows are selected as the corresponding modes. Finally, the wavenumbers (in cm⁻¹) for these modes are compared: differences (twisted minus untwisted) are computed to quantify any shifts induced by the twist.

## Reproduction target
Compute and report the wavenumbers (in cm⁻¹) for the Ag1‑like and Ag2‑like Raman‑active phonon modes in untwisted bilayer black phosphorus and in the 70.53° twisted bilayer black phosphorus. Then compute the shift for each mode as (twisted wavenumber − untwisted wavenumber). Write the six numbers – four wavenumbers and two shifts – into the JSON file `dft_raman_results.json` at the path `/app/outputs/dft_raman_results.json` using the exact schema given in Workflow step 4.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Norm-conserving PBE pseudopotentials for phosphorus: https://legacy.materialscloud.org/sssp/

## Workflow steps

### Step 1: Generate crystal structures for untwisted and twisted bilayer BP
- Role: process
- Action: Construct atomic coordinates for untwisted bilayer black phosphorus and the 70.53° twisted bilayer superlattice (p=q=1) using the coincidence-site lattice method. Output coordinate files in Quantum ESPRESSO input format.
- Evidence: `/app/outputs/coordinates.log`

### Step 2: Run DFT phonon calculation for untwisted bilayer BP
- Role: process
- Action: Using Quantum ESPRESSO, perform geometry relaxation if needed, then a Γ‑point phonon calculation for untwisted bilayer black phosphorus with PBE functional and norm-conserving pseudopotentials, energy cutoff 80 Ry. Extract phonon frequencies and Raman intensities.
- Evidence: `/app/outputs/untwisted_phonon.log`

### Step 3: Run DFT phonon calculation for twisted bilayer BP
- Role: process
- Action: Similarly compute phonon frequencies and Raman intensities for the 70.53° twisted bilayer black phosphorus with the same DFT parameters.
- Evidence: `/app/outputs/twisted_phonon.log`

### Step 4: Identify modes and compute blue shifts
- Role: scored (load-bearing)
- Action: From the calculated phonon modes, identify the Raman-active modes corresponding to Ag1 and Ag2: for untwisted bilayer by symmetry, for twisted bilayer by highest intensity in the appropriate frequency region and A symmetry. Compute wavenumbers (cm⁻¹) and blue shifts (twisted minus untwisted). Write the results to dft_raman_results.json.
- Output file: `/app/outputs/dft_raman_results.json`
- Format: json
- Contract: {"untwisted_bilayer_Ag1": number, "untwisted_bilayer_Ag2": number, "twisted_bilayer_Ag1": number, "twisted_bilayer_Ag2": number, "blue_shift_Ag1": number, "blue_shift_Ag2": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_raman_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_raman_results.json
- path: `/app/outputs/dft_raman_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the main DFT phonon wavenumbers and shifts.
- schema:
  - `type`: object
  - `required_keys`: `untwisted_bilayer_Ag1`, `untwisted_bilayer_Ag2`, `twisted_bilayer_Ag1`, `twisted_bilayer_Ag2`, `blue_shift_Ag1`, `blue_shift_Ag2`
  - `units`: cm^{-1} for all numeric fields

Notes: The checker compares reported values to the paper's Table 1 values with tolerances (hidden) for each wavenumber and shift. The blue shifts carry higher weight in scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_raman_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "untwisted_bilayer_Ag1",
          "untwisted_bilayer_Ag2",
          "twisted_bilayer_Ag1",
          "twisted_bilayer_Ag2",
          "blue_shift_Ag1",
          "blue_shift_Ag2"
        ],
        "units": "cm^{-1} for all numeric fields"
      },
      "description": "Scored artifact containing the main DFT phonon wavenumbers and shifts."
    }
  ],
  "notes": "The checker compares reported values to the paper's Table 1 values with tolerances (hidden) for each wavenumber and shift. The blue shifts carry higher weight in scoring."
}
```

## How you are scored
A hidden verifier reads your `dft_raman_results.json` file and compares each of the six reported values to reference values (derived from the original study) using tolerances that absorb legitimate DFT‑implementation variability. The verifier checks that all required keys are present and that the values are numbers. Each value that falls within its tolerance earns a fractional reward; the two shift values carry a higher weight than the wavenumbers. The final score is the weighted sum of the six partial scores, normalized to the range [0, 1].
