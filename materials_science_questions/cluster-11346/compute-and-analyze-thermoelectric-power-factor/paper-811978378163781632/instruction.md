# Compute DFT band gap of Re3GeAs6

## Problem background
Thermoelectric materials convert heat to electricity, and their efficiency is governed by a dimensionless figure of merit ZT that combines the Seebeck coefficient, electrical conductivity, and thermal conductivity. Achieving high ZT requires a carefully tuned electronic structure: a narrow band gap semiconductor with a sharp variation in the density of states near the Fermi level can yield both a large Seebeck coefficient and sufficient electrical conductivity. The recently discovered arsenides Re3(Ge,As)7 are n-type thermoelectrics that adopt a complex cubic crystal structure. Electronic structure calculations play a central role in explaining their thermoelectric performance: they predict the existence and magnitude of a band gap, which directly affects the Seebeck coefficient and the temperature dependence of the electrical properties. Reproducing the computed band gap of the stoichiometric compound Re3GeAs6 provides a critical test of the theoretical model underlying these materials.

## Approach
The electronic band gap of a crystalline solid can be obtained from first-principles calculations within density functional theory (DFT). The approach used in this work is to perform a DFT calculation for Re3GeAs6 employing the local density approximation (LDA) for the exchange-correlation functional. The calculation uses a specific ordered arrangement of Ge and As on the 16f site (E2) that is consistent with the electronic structure calculation reported in the original paper. The structure is defined below with explicit atomic coordinates for a unit cell that contains 4 formula units (Re12Ge4As24). You will set up a self-consistent field (SCF) calculation followed by a non-self-consistent band structure calculation to obtain the electronic eigenvalues on a dense k-point path. From the resulting band energies, the fundamental (minimum) band gap is identified as the smallest energy difference between the top of the valence band and the bottom of the conduction band, irrespective of whether it is direct or indirect. The workflow uses an open-source plane-wave DFT code (e.g., Quantum ESPRESSO, ABINIT, or SIESTA) together with standard LDA pseudopotentials for rhenium, germanium, and arsenic. No special spin‑polarisation or relativistic corrections are required. The calculation should be converged with respect to the plane-wave kinetic energy cutoff and k-point sampling; the exact values are your choice as long as the result is physically meaningful.

## Ordered crystal structure for Re3GeAs6

Use the following crystal structure data. The unit cell is cubic with space group Im‑3m (No. 229) and lattice parameter a = 8.73180 Å. The atomic positions are listed in crystallographic coordinates; the unit cell contains 12 Re, 12 As on the 12d site (As1), and 16 mixed E2 sites, which are assigned explicitly: 4 Ge atoms and 12 As atoms on the positions listed below. This assignment models a complete Ge/As ordering on the 16f site as employed in the paper's electronic structure calculation.

### Re atoms (12e site)
Re   0.3413  0.0000  0.0000
Re   0.0000  0.3413  0.0000
Re   0.0000  0.0000  0.3413
Re   0.6587  0.0000  0.0000
Re   0.0000  0.6587  0.0000
Re   0.0000  0.0000  0.6587
Re   0.8413  0.5000  0.5000
Re   0.5000  0.8413  0.5000
Re   0.5000  0.5000  0.8413
Re   0.1587  0.5000  0.5000
Re   0.5000  0.1587  0.5000
Re   0.5000  0.5000  0.1587

### As atoms on the 12d site (As1)
As   0.2500  0.0000  0.5000
As   0.5000  0.0000  0.2500
As   0.0000  0.2500  0.5000
As   0.5000  0.2500  0.0000
As   0.0000  0.5000  0.2500
As   0.2500  0.5000  0.0000
As   0.7500  0.5000  0.0000
As   0.0000  0.5000  0.7500
As   0.5000  0.7500  0.0000
As   0.0000  0.7500  0.5000
As   0.5000  0.0000  0.7500
As   0.7500  0.0000  0.5000

### Ge atoms on the 16f site (E2)
Ge   0.1663  0.1663  0.1663
Ge   0.6663  0.6663  0.6663
Ge   0.8337  0.1663  0.1663
Ge   0.3337  0.6663  0.6663

### As atoms on the 16f site (E2)
As   0.1663  0.8337  0.1663
As   0.6663  0.3337  0.6663
As   0.1663  0.1663  0.8337
As   0.6663  0.6663  0.3337
As   0.8337  0.8337  0.1663
As   0.3337  0.3337  0.6663
As   0.8337  0.1663  0.8337
As   0.3337  0.6663  0.3337
As   0.1663  0.8337  0.8337
As   0.6663  0.3337  0.3337
As   0.8337  0.8337  0.8337
As   0.3337  0.3337  0.3337

(Use the exact coordinates above to generate the input for your DFT code. All positions are in crystallographic units relative to the cubic cell with a = 8.73180 Å.)

## Reproduction target
Compute the fundamental band gap of Re3GeAs6 using DFT with LDA exchange-correlation and the explicitly ordered crystal structure described above. Write the band gap value in electronvolts (eV) as a single floating-point number to the file `/app/outputs/band_gap_reported.txt`.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- LDA pseudopotentials for Re, Ge, As: SSSP Efficiency 1.1 or PSlibrary 1.0.0 (or equivalent LDA pseudopotential library)

## Workflow steps

### Step 1: Compute band gap
- Role: scored (load-bearing)
- Action: Set up and run a DFT calculation for Re3GeAs6 using the crystal structure and ordered atomic positions listed in the Approach section. Use LDA exchange-correlation. Perform an SCF calculation and then a non-self-consistent band structure calculation on a suitable k‑point path. Extract the fundamental band gap (smallest direct or indirect gap) from the band structure. Write the band gap value in eV to `/app/outputs/band_gap_reported.txt` as a single floating-point number.
- Output file: `/app/outputs/band_gap_reported.txt`
- Format: txt
- Contract: Single line containing a floating-point number representing the band gap in eV.
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

Notes: The band gap value is compared to the paper's LMTO-LDA band gap with a hidden tolerance to account for implementation differences.

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
  "notes": "The band gap value is compared to the paper's LMTO-LDA band gap with a hidden tolerance to account for implementation differences."
}
```

## How you are scored
Your work is scored automatically by a hidden verifier that runs after the task completes. The verifier reads the band gap value from `/app/outputs/band_gap_reported.txt` and compares it against a hidden reference value derived from the original paper's electronic structure calculation. The comparison uses an absolute tolerance that is wide enough to absorb legitimate differences between DFT implementations (e.g., different pseudopotentials, basis sets, k-point grids) while still requiring a physically plausible gap. If your reported value falls within the acceptable range, you receive full credit for this scored artifact. Otherwise, the score is zero.