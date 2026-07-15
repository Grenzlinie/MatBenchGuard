# Interband Optical Conductivity Band Peak from DFT-LDA for Magnesium

## Problem background
The optical spectra of metals have been a subject of controversy: some argue that single-particle theory is insufficient and that electron–hole (excitonic) interactions dominate, while others contend that single-particle density-functional theory (DFT) in the local-density approximation (LDA) can accurately describe the interband optical conductivity without explicit excitonic corrections. A key test system is pure magnesium (Mg), where the interband absorption spectrum shows a well-defined peak whose energy can be predicted from a band-structure calculation. Resolving this debate requires a quantitative comparison between a DFT‑LDA interband spectrum and the experimental peak position.

## Approach
Perform a self‑consistent DFT‑LDA band‑structure calculation for hexagonal close‑packed (hcp) Mg using norm‑conserving pseudopotentials. From the Kohn‑Sham eigenvalues and dipole matrix elements, compute the interband optical conductivity σ(ω) as a function of photon energy. The calculation must use a sufficiently dense k‑point mesh and a sufficient number of empty bands to converge the conductivity. The resulting spectrum is a CSV file (energy, sigma) whose main peak energy — defined as the energy at which sigma is maximal — is the quantitative target. No electron‑hole interaction corrections or many‑body effects beyond LDA are included.

## Reproduction target
Produce a CSV file containing the interband optical conductivity spectrum of hcp Mg computed with DFT‑LDA. The hidden verifier will extract the energy of the maximum conductivity (the main peak) from that file and compare it to an experimentally measured peak energy for pure Mg. The objective is for the computed peak energy to lie close to the experimental reference.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PseudoDojo norm-conserving pseudopotential for Mg (LDA): http://www.pseudo-dojo.org/
- Crystallographic data for hcp Mg
- Optical conductivity post-processing (epsilon.x or custom script): epsilon.x is distributed with Quantum ESPRESSO

## Workflow steps

### Step 1: DFT-LDA band structure and optical conductivity calculation for hcp Mg
- Role: process
- Action: Perform a self-consistent DFT-LDA calculation for hcp Mg using Quantum ESPRESSO with the norm-conserving pseudopotential, then compute the interband optical conductivity (σ(ω)) using epsilon.x or an equivalent custom script. The calculation should include a dense k-point mesh for the optical spectra and a sufficient number of empty bands.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 2: Write optical conductivity spectrum
- Role: scored (load-bearing)
- Action: Extract the interband optical conductivity σ(ω) as a function of photon energy from the calculation outputs and write a CSV file with two columns: energy (eV) and sigma (arbitrary units).
- Output file: `/app/outputs/optical_conductivity_spectrum.csv`
- Format: csv
- Contract: CSV file with header row: energy,sigma. energy in eV, sigma positive dimensionless (arb. units). Values sorted by increasing energy.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optical_conductivity_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optical_conductivity_spectrum.csv
- path: `/app/outputs/optical_conductivity_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Interband optical conductivity spectrum of hcp Mg computed from DFT-LDA. The hidden checker extracts the energy at maximum sigma and compares it to a confidential experimental gold standard, rewarding proximity below a defined tolerance.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `sigma`
  - `units`:
    - `energy`: eV
    - `sigma`: arbitrary

Notes: The checked quantity is the main peak energy (eV) derived from this spectrum. The agent is not required to download experimental data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optical_conductivity_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "sigma"
        ],
        "units": {
          "energy": "eV",
          "sigma": "arbitrary"
        }
      },
      "description": "Interband optical conductivity spectrum of hcp Mg computed from DFT-LDA. The hidden checker extracts the energy at maximum sigma and compares it to a confidential experimental gold standard, rewarding proximity below a defined tolerance."
    }
  ],
  "notes": "The checked quantity is the main peak energy (eV) derived from this spectrum. The agent is not required to download experimental data."
}
```

## How you are scored
A hidden verifier reads your optical_conductivity_spectrum.csv, locates the photon energy where sigma is maximal, and compares that energy to a confidential experimental gold standard obtained from independent measurements on pure Mg. Full credit is awarded if the deviation is within a tolerance that accounts for implementation differences; the reward decreases linearly as the deviation grows, reaching zero at a larger deviation. The verifier also checks that all sigma values are non‑negative and that the peak does not occur at the extremes of the energy range. No other quantities are scored; only the CSV file matters.
