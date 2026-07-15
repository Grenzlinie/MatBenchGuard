# DFPT computation of local vibrational modes for light impurities in silicon

## Problem background
Vibrational spectroscopy using infrared and Raman measurements is a primary experimental tool for identifying light impurities and defect complexes in crystalline silicon. Interpreting these spectra requires accurate theoretical predictions of local vibrational mode (LVM) frequencies. First‑principles density‑functional theory (DFT) can provide such frequencies, but standard frozen‑phonon approaches using finite atomic displacements necessarily include some anharmonic contributions that degrade accuracy. A more rigorous route is density‑functional perturbation theory (DFPT), which extracts the harmonic dynamical matrix directly from the ground‑state electron density without displacing any atom, promising high‑quality frequencies for harmonic modes.

## Approach
You will use the SIESTA DFT code, which expands electronic wavefunctions in numerical atomic orbitals (LCAO). The workflow follows linear‑response DFPT: for each target system, first obtain the equilibrium geometry by relaxing all atomic coordinates until the maximum force is below the required threshold. Then, using the relaxed ground‑state charge density, compute the dynamical matrix analytically from the first‑order change in the density matrix induced by infinitesimal atomic displacements. Diagonalization of the dynamical matrix gives vibrational eigenfrequencies and eigenvectors at the Γ point. The required systems span a free silane molecule and several light‑impurity defect complexes in a 64‑atom silicon supercell. Basis‑set choices (double‑zeta or double‑zeta‑polarized) and norm‑conserving pseudopotentials with LDA exchange‑correlation are used throughout, following the paper’s protocol.

## Reproduction target
Produce a JSON file named `frequencies.json` containing the harmonic stretch‑mode frequencies (in cm⁻¹) for the following systems:
- SiH₄ (free molecule): T₂, A₁, E, and the second T₂ modes.
- H_BC (bond‑center interstitial hydrogen in a 64‑atom Si supercell): stretch mode.
- H₂ (molecular hydrogen at the tetrahedral interstitial site): stretch mode.
- H₂* (H_BC + H_AB complex): stretch modes for H_BC and H_AB.
- VH₄ (fully hydrogenated vacancy): T₂ stretch mode.
- O_i (interstitial oxygen): A₂ᵤ stretch mode.
The output contract details the exact JSON schema. You must perform the full DFT‑DFPT pipeline (geometry relaxation → dynamical matrix → diagonalization) to obtain these frequencies; simply reporting literature values is not sufficient.

## Assets

- SIESTA DFT code: https://gitlab.com/siesta-project/siesta
- Norm-conserving pseudopotentials: https://departments.icmab.es/leem/siesta/Databases/Pseudopotentials/

## Workflow steps

### Step 1: Geometry optimization of all systems
- Role: process
- Action: For each system (free SiH4 molecule, H_BC, H2, H2*, VH4, and O_i in a 64-atom Si supercell) set up the periodic simulation cell, select the appropriate basis set (DZP for SiH4, DZ for the defect systems), and relax all atomic coordinates using DFT-LDA until the maximum force on any atom is below 0.01 eV/Å. For the defect systems, place the impurity at the correct site as described in the paper.
- Evidence: `/app/outputs/relax_energy.log`

### Step 2: DFPT dynamical matrix calculation
- Role: process
- Action: For each relaxed configuration, run SIESTA in DFPT linear-response mode to compute the harmonic dynamical matrix analytically from the first-order electronic response. Use the same basis set and pseudopotentials as in the relaxation step.
- Evidence: `/app/outputs/siesta.FC`

### Step 3: Diagonalization and mode identification
- Role: process
- Action: Diagonalize the dynamical matrix to obtain eigenfrequencies and eigenvectors at the Γ point. For each system, identify the local vibrational modes of the light impurities based on displacement patterns and symmetries.
- Evidence: `/app/outputs/phonon_freqs.txt`

### Step 4: Write scored frequencies
- Role: scored (load-bearing)
- Action: Write the harmonic frequencies for the specified stretch modes of all systems to a JSON file. For SiH4, include the T2, A1, E, and second T2 modes. For H_BC, include the stretch mode. For H2, include the stretch mode. For H2*, include the H_BC and H_AB stretch modes. For VH4, include the T2 mode. For O_i, include the A₂u stretch mode. Frequencies in cm⁻¹.
- Output file: `/app/outputs/frequencies.json`
- Format: json
- Contract: JSON object with keys 'si_h4', 'h_bc', 'h2', 'h2_star', 'vh4', 'o_i'. Each value is an array of objects with fields 'mode' (string) and 'freq' (number, cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### frequencies.json
- path: `/app/outputs/frequencies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed harmonic vibrational frequencies for the stretch modes of free SiH4 and selected defects in silicon. The checker compares each frequency to the paper's computed values; average absolute percent error ≤5% earns full credit.
- schema:
  - `type`: object
  - `required`:
    - `si_h4`: array of {mode: string, freq: number}
    - `h_bc`: array of {mode: string, freq: number}
    - `h2`: array of {mode: string, freq: number}
    - `h2_star`: array of {mode: string, freq: number}
    - `vh4`: array of {mode: string, freq: number}
    - `o_i`: array of {mode: string, freq: number}
  - `items`:
    - `type`: object
    - `properties`:
      - `mode`: string
      - `freq`: number (cm⁻¹)

Notes: The scored output depends on successfully running the entire DFPT workflow; a lazy agent cannot fabricate the correct frequencies without performing the calculations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "si_h4": "array of {mode: string, freq: number}",
          "h_bc": "array of {mode: string, freq: number}",
          "h2": "array of {mode: string, freq: number}",
          "h2_star": "array of {mode: string, freq: number}",
          "vh4": "array of {mode: string, freq: number}",
          "o_i": "array of {mode: string, freq: number}"
        },
        "items": {
          "type": "object",
          "properties": {
            "mode": "string",
            "freq": "number (cm⁻¹)"
          }
        }
      },
      "description": "Computed harmonic vibrational frequencies for the stretch modes of free SiH4 and selected defects in silicon. The checker compares each frequency to the paper's computed values; average absolute percent error ≤5% earns full credit."
    }
  ],
  "notes": "The scored output depends on successfully running the entire DFPT workflow; a lazy agent cannot fabricate the correct frequencies without performing the calculations."
}
```

## How you are scored
A hidden verifier will read your `frequencies.json` and compare each reported frequency to a gold reference value for the same system and mode. It calculates the absolute percent error for every required mode and then computes the average. The final reward is 1.0 if the average error is within a predefined tolerance; beyond that tolerance the reward decreases as the error grows. The full metric is monotonic—lower average error always yields higher reward. The verifier never needs to inspect your intermediate log files; only the `frequencies.json` artifact is scored.
