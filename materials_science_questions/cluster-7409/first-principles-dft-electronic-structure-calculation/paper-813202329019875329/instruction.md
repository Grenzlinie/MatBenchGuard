# DFT band gap calculation of H2Ti6O13

## Problem background
Hydrogen titanium oxide H2Ti6O13 adopts a monoclinic C2/m crystal structure with one‑dimensional tunnels. First‑principles electronic structure calculations on this compound can reveal the character of the orbitals near the Fermi level and predict the size of the electronic band gap. The band gap is a key quantity that influences the material's optical absorption and transport properties. This task asks you to compute the band gap from density functional theory.

## Approach
The computational approach uses density functional theory (DFT) with the generalized gradient approximation (GGA) in the Perdew–Burke–Ernzerhof (PBE) formulation. You will construct the crystal structure of H2Ti6O13 from its published lattice parameters (a=14.6604 Å, b=3.74109 Å, c=9.2487 Å, β=96.956°) and atomic coordinates (H, Ti, O positions) and perform a self‑consistent field (SCF) calculation using a plane‑wave / pseudopotential code such as Quantum ESPRESSO. From the converged charge density you then compute the total density of states (DOS) and determine the band gap as the energy difference between the valence band maximum and the conduction band minimum. The final answer is that band gap, reported in eV.

## Reproduction target
Compute the electronic band gap of H2Ti6O13 from first‑principles DFT using the provided crystal structure and the GGA‑PBE functional. Write the band gap as a single floating‑point number (in eV) to a plain text file named `band_gap.txt` in the `/app/outputs/` directory.

## Crystal structure data

The crystal structure of H₂Ti₆O₁₃ is monoclinic, space group C2/m (No. 12), with lattice parameters a=14.6604 Å, b=3.74109 Å, c=9.2487 Å, β=96.956°. The atomic fractional coordinates are as follows (all sites fully occupied):

H1  4i  0.9992  0  0.3110
Ti1 4i  0.1167  0  0.0980
Ti2 4i  0.1676  0  0.4478
Ti3 4i  0.2274  0  0.7720
O1  2a  0       0  0
O2  4i  0.2372  0  0.2482
O3  4i  0.0628  0  0.3034
O4  4i  0.2965  0  0.5677
O5  4i  0.1241  0  0.6182
O6  4i  0.3590  0  0.8756
O7  4i  0.1693  0  0.9243

(Coordinates taken from Table 2 of the paper; uncertainties omitted.)

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Run SCF calculation
- Role: process
- Action: Perform a self-consistent field (SCF) electronic structure calculation for H2Ti6O13 using a DFT code (e.g., Quantum ESPRESSO) with the generalized gradient approximation (GGA) in the Perdew–Burke–Ernzerhof (PBE) formulation. Use the crystal structure: monoclinic C2/m, lattice constants a=14.6604 Å, b=3.74109 Å, c=9.2487 Å, β=96.956°, and atomic coordinates from Table 2 of the paper (H, Ti, O positions). Converge the total energy and electron density with respect to k-point sampling and plane-wave basis cutoff.
- Evidence: `/app/outputs/scf.out`

### Step 2: Compute DOS and band gap
- Role: scored
- Action: Using the converged charge density, compute the total density of states (DOS) and determine the band gap (energy difference between the valence band maximum and conduction band minimum). Extract the band gap value in eV and write it as a single floating-point number to band_gap.txt.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: Single floating-point number (e.g., '3.12').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The computed electronic band gap of H2Ti6O13 from the DFT calculation.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the band gap in eV.

Notes: The DFT calculation uses the published crystal structure; no wet-lab or diffraction data are required. The result is a single number representing the computed band gap.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the band gap in eV."
      },
      "description": "The computed electronic band gap of H2Ti6O13 from the DFT calculation."
    }
  ],
  "notes": "The DFT calculation uses the published crystal structure; no wet-lab or diffraction data are required. The result is a single number representing the computed band gap."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/band_gap.txt` and compares the reported band gap to a reference value (the value obtained in the original study using a similar computational setup). Your score is based on the absolute difference between your computed gap and the reference. If the difference is within a modest tolerance you earn full credit; if the difference is larger but still within a wider bound you receive partial credit; outside that range the reward is zero. The intermediate SCF evidence file `scf.out` is required to show you ran the calculation but is not directly scored.
