# Compute Site-Projected Density of States for AlB2-like Ternary Silicides

## Problem background
The discovery of superconductivity in AlB2-like compounds has motivated the search for related materials. Ternary silicides M(A0.5Si0.5)2 (M = Ca, Sr, Ba; A = Al, Ga) adopt the same hexagonal AlB2-type crystal structure and exhibit superconducting transitions up to 7.7 K. The electronic structure — in particular, the density of states at the Fermi level, N(EF) — is expected to play a key role in superconductivity, but the relationship between N(EF) and Tc in these isostructural, isoelectronic compounds is not straightforward. Understanding the site- and orbital-resolved contributions to N(EF) and how they vary with the alkaline-earth element is essential to clarify the factors that control Tc in this family.

## Approach
The core method is a first-principles density functional theory (DFT) calculation of the electronic band structure and site-projected density of states. The six compounds M(A0.5Si0.5)2 (M=Ca,Sr,Ba; A=Al,Ga) are modelled in the AlB2-type crystal structure using the lattice parameters provided in the assets. Because the honeycomb layers contain an equimolar mixture of Al/Si or Ga/Si, the virtual crystal approximation (VCA) is used to treat the mixed site as an average pseudopotential species. The workflow proceeds as follows: (i) generate self-consistent field (SCF) and non-self-consistent (NSCF/PDOS) input files for all six compounds; (ii) run DFT calculations to obtain the ground-state charge density and the site- and orbital-projected density of states; (iii) extract the projected DOS contributions at the Fermi level for each sublattice (M, A, Si) and each orbital character (s, p, d, f) and compile them into a structured numerical table.

## Reproduction target
Perform DFT calculations for the six compounds M(A0.5Si0.5)2 (M=Ca, Sr, Ba; A=Al, Ga) and produce the file `dos_contributions.csv`. The file must contain one row per compound, with the following columns: `compound` (the exact compound name), `M_s`, `M_p`, `M_d`, `M_f`, `A_s`, `A_p`, `A_d`, `Si_s`, `Si_p`, `Si_d`, and `total`. All numeric values are in units of states/eV per formula unit. The objective is to obtain both the absolute magnitude of the various projected DOS contributions (especially for the reference compound Ca(Al0.5Si0.5)2) and the overall trend of the total N(EF) as the alkaline-earth metal changes from Ca to Sr to Ba, for both the Al and Ga series.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp
- Lattice parameters from Table I

## Workflow steps

### Step 1: Prepare DFT inputs
- Role: process
- Action: Generate DFT input files for the six compounds M(A0.5Si0.5)2 (M=Ca,Sr,Ba; A=Al,Ga) using the AlB2-type crystal structure and the provided lattice parameters. Use the virtual crystal approximation (VCA) to model the mixed Al/Si or Ga/Si site.
- Evidence: `/app/outputs/inputs.tar.gz`

### Step 2: Run DFT calculations
- Role: process
- Action: Perform self-consistent field (SCF) calculations to obtain ground-state charge density, then non-self-consistent calculations to compute site- and orbital-projected density of states (PDOS) for each compound.
- Evidence: `/app/outputs/pdos_outputs.tar.gz`

### Step 3: Extract Fermi-level DOS contributions
- Role: scored (load-bearing)
- Action: From the PDOS outputs, determine the projected density of states at the Fermi level for each sublattice and orbital component. Write a CSV file with columns: compound, M_s, M_p, M_d, M_f, A_s, A_p, A_d, Si_s, Si_p, Si_d, total.
- Output file: `/app/outputs/dos_contributions.csv`
- Format: csv
- Contract: CSV with header: compound, M_s, M_p, M_d, M_f, A_s, A_p, A_d, Si_s, Si_p, Si_d, total. Each row corresponds to one of the six compounds. Values are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_contributions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_contributions.csv
- path: `/app/outputs/dos_contributions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: One row per compound containing the site- and orbital-projected density of states at the Fermi level. All values are in states/eV per formula unit.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `M_s`, `M_p`, `M_d`, `M_f`, `A_s`, `A_p`, `A_d`, `Si_s`, `Si_p`, `Si_d`, `total`
  - `units`:
    - `M_s`: states/eV
    - `M_p`: states/eV
    - `M_d`: states/eV
    - `M_f`: states/eV
    - `A_s`: states/eV
    - `A_p`: states/eV
    - `A_d`: states/eV
    - `Si_s`: states/eV
    - `Si_p`: states/eV
    - `Si_d`: states/eV
    - `total`: states/eV

Notes: The material system is the six ternary silicides M(A0.5Si0.5)2 (M=Ca,Sr,Ba; A=Al,Ga). The compound column must contain the exact string identifiers as given in the paper (Ca(Al0.5Si0.5)2, Sr(Al0.5Si0.5)2, Ba(Al0.5Si0.5)2, Ca(Ga0.5Si0.5)2, Sr(Ga0.5Si0.5)2, Ba(Ga0.5Si0.5)2).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_contributions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "M_s",
          "M_p",
          "M_d",
          "M_f",
          "A_s",
          "A_p",
          "A_d",
          "Si_s",
          "Si_p",
          "Si_d",
          "total"
        ],
        "units": {
          "M_s": "states/eV",
          "M_p": "states/eV",
          "M_d": "states/eV",
          "M_f": "states/eV",
          "A_s": "states/eV",
          "A_p": "states/eV",
          "A_d": "states/eV",
          "Si_s": "states/eV",
          "Si_p": "states/eV",
          "Si_d": "states/eV",
          "total": "states/eV"
        }
      },
      "description": "One row per compound containing the site- and orbital-projected density of states at the Fermi level. All values are in states/eV per formula unit."
    }
  ],
  "notes": "The material system is the six ternary silicides M(A0.5Si0.5)2 (M=Ca,Sr,Ba; A=Al,Ga). The compound column must contain the exact string identifiers as given in the paper (Ca(Al0.5Si0.5)2, Sr(Al0.5Si0.5)2, Ba(Al0.5Si0.5)2, Ca(Ga0.5Si0.5)2, Sr(Ga0.5Si0.5)2, Ba(Ga0.5Si0.5)2)."
}
```

## How you are scored
A hidden verifier reads your `dos_contributions.csv`. It checks the reported Fermi-level DOS values against the DFT results that would be expected for this system, evaluating (a) the correctness of the total N(EF) and the key orbital contributions for Ca(Al0.5Si0.5)2, and (b) the qualitative trend of total N(EF) across the series Ca → Sr → Ba for both the Al and Ga series. The verifier uses tolerances that account for typical differences between DFT codes and pseudopotential choices. The final reward is a weighted combination of these checks on a 0–1 scale; reporting a syntactically correct CSV alone is not sufficient — the numbers must agree with the correct physical answer produced by a faithful DFT calculation.
