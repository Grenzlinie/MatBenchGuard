# Compute band gap and projected DOS for KNiF3 from periodic unrestricted Hartree-Fock calculations

## Problem background
KNiF3 is a perovskite magnetic insulator that orders antiferromagnetically at low temperature. Understanding its electronic structure is essential for interpreting its magnetic and transport properties. This task investigates the ground-state electronic structure using periodic unrestricted Hartree-Fock (UHF) calculations. The goal is to compute the band gap and the orbital character of the valence and conduction band edges for both the ferromagnetic (FM) and antiferromagnetic (AFM) phases. The crystal adopts a cubic perovskite structure (space group Pm-3m) with experimental lattice parameter a = 4.01 Å; Ni occupies (0,0,0), F occupies (0.5,0,0), (0,0.5,0), (0,0,0.5) and K occupies (0.5,0.5,0.5). The basis sets are contracted Gaussian-type functions. The required exponents and contraction coefficients (s, p, sp, d shells) are provided below.



## Approach
The computational approach uses periodic unrestricted Hartree-Fock (UHF) calculations with an open-source periodic Hartree-Fock engine (e.g., CP2K) to compute the electronic structure of KNiF3. Two magnetic configurations are studied: ferromagnetic (all Ni spins aligned) and antiferromagnetic (alternating spin layers; a doubled unit cell may be needed to accommodate the spin ordering). The calculations are performed at the experimental lattice parameter using the Gaussian basis sets specified above. After achieving self-consistent convergence, the total and orbital-projected density of states (PDOS) are constructed from the wavefunctions. Projections are made onto F states, Ni t2g states, and Ni eg states. The fundamental band gap is determined from the energy region where the total DOS vanishes. The character of the highest valence band and lowest conduction band is examined by comparing the projected DOS contributions at the band edges.

## Reproduction target
Produce a single CSV file, `/app/outputs/dos_and_pdos.csv`, that contains the total and projected density of states for both the FM and AFM phases. The columns must be: energy (eV), total_dos, pdos_f, pdos_ni_t2g, pdos_ni_eg. The file must have two data blocks, each preceded by a comment line identifying the phase: `# FM phase` and `# AF phase`. The target is to: (1) obtain the fundamental band gap (in eV) for each phase, and (2) from the computed PDOS, determine the dominant orbital contributions at the valence band maximum and conduction band minimum for both FM and AFM phases, and report these in the output file.

## Assets

- CP2K open-source molecular simulation package: https://www.cp2k.org/
- Gaussian basis sets for Ni, K, F

## Workflow steps

### Step 1: Prepare input structures and basis sets
- Role: process
- Action: Define the KNiF3 cubic perovskite crystal structure (experimental lattice parameter a=4.01 Å, space group Pm-3m, Ni at (0,0,0), F at (0.5,0,0) etc.) and assemble the Gaussian basis sets for Ni, K, and F as given in the problem description. Create input files for periodic UHF calculations (FM and AFM supercells if needed) for CP2K or an equivalent open-source periodic HF code.
- Evidence: none

### Step 2: Run UHF-SCF calculations for FM and AFM phases
- Role: process
- Action: Perform self-consistent periodic unrestricted Hartree-Fock calculations for the ferromagnetic and antiferromagnetic configurations of KNiF3 using the prepared inputs. Use a k-point mesh equivalent to IS=8 (at least 29 irreducible points) and tight integral tolerances. Achieve convergence of total energy and obtain wavefunctions/electron density.
- Evidence: `/app/outputs/uhf_output.log`

### Step 3: Compute projected DOS and band gap
- Role: scored (load-bearing)
- Action: Post-process the converged wavefunctions from both FM and AFM phases to obtain total and orbital-projected density of states (PDOS) onto F, Ni t2g, and Ni eg. Determine the fundamental band gap (energy difference between the top of the valence band and the bottom of the conduction band) for each phase. Write a CSV file with columns: energy (eV), total_dos, pdos_f, pdos_ni_t2g, pdos_ni_eg. Include separate blocks for FM and AFM, each preceded by a header line identifying the phase.
- Output file: `/app/outputs/dos_and_pdos.csv`
- Format: csv
- Contract: CSV with columns: energy (eV, float), total_dos (float), pdos_f (float), pdos_ni_t2g (float), pdos_ni_eg (float). Each block (FM, AFM) starts with a comment line '# FM phase' or '# AFM phase'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_and_pdos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_and_pdos.csv
- path: `/app/outputs/dos_and_pdos.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Projected density of states and band gap. The checker recomputes the fundamental band gap (energy range where total_dos is zero) and verifies that at the valence band maximum, pdos_f + pdos_ni_t2g dominates, and at the conduction band minimum, pdos_f + pdos_ni_eg dominates, confirming the reported orbital character.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_dos`, `pdos_f`, `pdos_ni_t2g`, `pdos_ni_eg`
  - `units`:
    - `energy`: eV
  - `description`: The file contains data blocks for FM and AFM phases, each preceded by a comment line '# FM phase' or '# AFM phase'.

Notes: The band gap and orbital character are recomputed by the hidden checker from the raw PDOS data. No gold values or tolerances are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_and_pdos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_dos",
          "pdos_f",
          "pdos_ni_t2g",
          "pdos_ni_eg"
        ],
        "units": {
          "energy": "eV"
        },
        "description": "The file contains data blocks for FM and AFM phases, each preceded by a comment line '# FM phase' or '# AFM phase'."
      },
      "description": "Projected density of states and band gap. The checker recomputes the fundamental band gap (energy range where total_dos is zero) and verifies that at the valence band maximum, pdos_f + pdos_ni_t2g dominates, and at the conduction band minimum, pdos_f + pdos_ni_eg dominates, confirming the reported orbital character."
    }
  ],
  "notes": "The band gap and orbital character are recomputed by the hidden checker from the raw PDOS data. No gold values or tolerances are disclosed."
}
```

## How you are scored
A hidden verifier will independently process your `dos_and_pdos.csv`. It will recompute the fundamental band gap for each phase from the total DOS data and examine the projected DOS at the band edges. Your computed band gaps and the orbital character compliance will be compared against hidden reference criteria. The verifier assigns a weighted score based on how well your results match those criteria. Reporting numbers without genuinely performing the UHF calculations will not achieve full credit; the evaluation is designed to require the computed electronic structure artifact.
