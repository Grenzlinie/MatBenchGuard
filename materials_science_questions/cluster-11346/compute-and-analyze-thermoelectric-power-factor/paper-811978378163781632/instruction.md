# Compute DFT band gap of Re3GeAs6

## Problem background
Thermoelectric materials convert heat to electricity, and their efficiency is governed by a dimensionless figure of merit ZT that combines the Seebeck coefficient, electrical conductivity, and thermal conductivity. Achieving high ZT requires a carefully tuned electronic structure: a narrow band gap semiconductor with a sharp variation in the density of states near the Fermi level can yield both a large Seebeck coefficient and sufficient electrical conductivity. The recently discovered arsenides Re3(Ge,As)7 are n-type thermoelectrics that adopt a complex cubic crystal structure. Electronic structure calculations play a central role in explaining their thermoelectric performance: they predict the existence and magnitude of a band gap, which directly affects the Seebeck coefficient and the temperature dependence of the electrical properties. Reproducing the computed band gap of the stoichiometric compound Re3GeAs6 provides a critical test of the theoretical model underlying these materials.

## Approach
The electronic band gap of a crystalline solid can be obtained from first-principles calculations within density functional theory (DFT). The approach used in this work is to perform a DFT calculation for Re3GeAs6 employing the local density approximation (LDA) for the exchange-correlation functional, using the experimentally determined crystal structure. The calculation models the infinite periodic solid by a unit cell with space group Im-3m and lattice parameter a = 8.73180 Å, containing Re atoms at the 12e site, As atoms at the 12d site, and a mixed-occupancy E2 site (16f) with 25% Ge and 75% As. You will set up a self-consistent field (SCF) calculation followed by a non-self-consistent band structure calculation to obtain the electronic eigenvalues on a dense k-point path. From the resulting band energies, the fundamental (minimum) band gap is identified as the smallest energy difference between the top of the valence band and the bottom of the conduction band, irrespective of whether it is direct or indirect. The workflow uses an open-source plane-wave DFT code (e.g., Quantum ESPRESSO, ABINIT, or SIESTA) together with standard LDA pseudopotentials for rhenium, germanium, and arsenic. No special spin‑polarisation or relativistic corrections are required. The calculation should be converged with respect to the plane-wave kinetic energy cutoff and k-point sampling; the exact values are your choice as long as the result is physically meaningful.

## Reproduction target
Compute the fundamental band gap of Re3GeAs6 using DFT with LDA exchange-correlation and the experimental crystal structure described in the workflow steps. Write the band gap value in electronvolts (eV) as a single floating-point number to the file `/app/outputs/band_gap_reported.txt`. For example, if the gap is 0.92 eV, the file would contain the line `0.92`.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- LDA pseudopotentials for Re, Ge, As: SSSP Efficiency 1.1 or PSlibrary 1.0.0 (or equivalent LDA pseudopotential library)

## Workflow steps

### Step 1: Prepare DFT input files
- Role: process
- Action: Create the necessary input files for a DFT calculation of Re3GeAs6 using the experimental crystal structure (space group Im-3m, a = 8.73180 Å, atomic positions: Re at 12e (0.3413,0,0), As1 at 12d (0.25,0,0.5), E2 at 16f (0.1663,0.1663,0.1663) with occupancy 0.25 Ge + 0.75 As). Use LDA exchange-correlation. Package all input files into a tar.gz archive named input_files.tar.gz.
- Evidence: `/app/outputs/input_files.tar.gz`

### Step 2: Compute band gap
- Role: scored (load-bearing)
- Action: Run the DFT calculation using the prepared input files and an open-source DFT code. Extract the fundamental band gap (the smallest direct or indirect gap) from the calculation results. Write the band gap value in eV to band_gap_reported.txt as a single floating-point number.
- Output file: `/app/outputs/band_gap_reported.txt`
- Format: txt
- Contract: Single line containing a floating-point number (e.g., '0.92') representing the band gap in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_reported.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_reported.txt
- path: `/app/outputs/band_gap_reported.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Band gap of Re3GeAs6 computed using DFT-LDA.
- schema:
  - `type`: text
  - `units`: eV

Notes: The band gap value is compared to the paper's LMTO-LDA band gap with a hidden tolerance to account for implementation differences. The input_files.tar.gz evidence is verified but not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_reported.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "eV"
      },
      "description": "Band gap of Re3GeAs6 computed using DFT-LDA."
    }
  ],
  "notes": "The band gap value is compared to the paper's LMTO-LDA band gap with a hidden tolerance to account for implementation differences. The input_files.tar.gz evidence is verified but not scored."
}
```

## How you are scored
Your work is scored automatically by a hidden verifier that runs after the task completes. The verifier reads the band gap value from `/app/outputs/band_gap_reported.txt` and compares it against a hidden reference value derived from the original paper's electronic structure calculation. The comparison uses an absolute tolerance that is wide enough to absorb legitimate differences between DFT implementations (e.g., different pseudopotentials, basis sets, k-point grids) while still requiring a physically plausible gap. If your reported value falls within the acceptable range, you receive full credit for this scored artifact. Otherwise, the score is zero. The presence of the input file archive `/app/outputs/input_files.tar.gz` is also checked, but it does not affect the reward.
