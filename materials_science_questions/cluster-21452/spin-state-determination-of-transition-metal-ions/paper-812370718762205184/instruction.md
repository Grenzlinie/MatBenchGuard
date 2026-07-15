# Calculating site-projected magnetic moments for Ca3Co2O6 from spin-polarized DFT

## Problem background
Ca3Co2O6 is a one-dimensional chain compound with trigonal crystal structure (space group R-3c). The chains consist of alternating CoO6 octahedra (site Co1) and CoO6 trigonal prisms (site Co2), leading to two inequivalent cobalt environments. The magnetic properties of this material are intriguing: below about 25 K, ferromagnetic alignment appears inside the chains, but the overall magnetic order involves competing interchain interactions, resulting in a complex phase diagram with several metastable states. A central puzzle is whether the different oxygen coordinations at Co1 and Co2 force the cobalt ions into distinct spin states — low-spin at the octahedral site and high-spin at the trigonal-prismatic site — and how the resulting local magnetic moments are distributed among the cobalt and oxygen atoms. Reproducing the site-projected magnetic moments from first-principles calculations is essential to resolve these spin-state assignments and understand the origin of the extended moments that characterize the low-temperature magnetism.

## Approach
Use spin-polarized density functional theory (DFT) to compute the ferromagnetic electronic ground state of Ca3Co2O6. Build the crystal structure from the known lattice parameters (hexagonal axes a = 9.060 Å, c = 10.366 Å) and atomic positions for Ca, Co, and O. Employ an open-source DFT code with a suitable exchange-correlation functional (LDA or GGA) and pseudopotential / PAW library. Align all Co spins in the same direction (ferromagnetic configuration). Converge the total energy and the atomic forces, then extract the site-projected magnetic moments (in μB) from the self-consistent spin density. The moments on Co1, Co2, and the oxygen sites (averaged over all oxygen atoms if multiple) are the key quantities to report.

## Reproduction target
Produce a CSV file containing the local magnetic moments for the ferromagnetic configuration. The file must include the site-projected moments for Co1, Co2, and oxygen (averaged if multiple oxygen sites exist). The CSV columns are 'site' (string) and 'spin_moment' (float, in μB). Write this file as `/app/outputs/magnetic_moments.csv`.

## Assets

- Ca3Co2O6 crystal structure: 10.1016/S0038-1098(96)00701-4
- Open-source DFT code (e.g., Quantum Espresso): https://www.quantum-espresso.org
- Pseudopotentials for Co, Ca, O: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Prepare Ca3Co2O6 input structure
- Role: process
- Action: Obtain the crystal structure of Ca3Co2O6 (space group R-3c, lattice constants a=9.060 Å, c=10.366 Å, atomic positions from Aasland et al. or ICSD) and generate a DFT input file.
- Evidence: `/app/outputs/structure_input.scf`

### Step 2: Calculate ferromagnetic magnetic moments
- Role: scored (load-bearing)
- Action: Perform a spin-polarized DFT calculation on Ca3Co2O6 with all Co spins aligned ferromagnetically. Use an open-source DFT code, an appropriate exchange-correlation functional, and pseudopotentials. Converge the total energy and compute site-projected magnetic moments (in μB). Extract the moments for Co1, Co2, and oxygen (average if multiple oxygen sites) and write them to magnetic_moments.csv.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: CSV with columns: site (string), spin_moment (float, μB). Example rows: Co1,<value>; Co2,<value>; O,<average_value>.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Site-projected magnetic moments for Co1, Co2, and oxygen from a spin-polarized DFT calculation on ferromagnetic Ca3Co2O6.
- schema:
  - `type`: table
  - `required_columns`: `site`, `spin_moment`
  - `units`:
    - `spin_moment`: mu_B

Notes: The oxygen moment may be averaged over all oxygen sites. Tolerances for scoring are defined in the hidden grading spec and are not disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "spin_moment"
        ],
        "units": {
          "spin_moment": "mu_B"
        }
      },
      "description": "Site-projected magnetic moments for Co1, Co2, and oxygen from a spin-polarized DFT calculation on ferromagnetic Ca3Co2O6."
    }
  ],
  "notes": "The oxygen moment may be averaged over all oxygen sites. Tolerances for scoring are defined in the hidden grading spec and are not disclosed here."
}
```

## How you are scored
A hidden verifier will read your `magnetic_moments.csv` and compare each site-projected moment against reference expectations within tolerances that account for methodological spread among DFT implementations. It will also verify the spin-state assignments by checking whether the moments fall into the expected low-spin and high-spin regimes. Your final score is the weighted sum of these checks; merely reporting numbers is not enough — the values must agree with the reference within the allowed tolerances and satisfy the spin-state conditions.
