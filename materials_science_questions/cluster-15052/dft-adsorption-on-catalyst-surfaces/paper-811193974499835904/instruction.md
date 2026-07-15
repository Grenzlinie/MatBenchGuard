# Reactive Domain Peaks on fcc Surfaces

## Problem background
Formic acid oxidation on Pt electrodes is poisoned by adsorbed species. Ad-atoms deposited on Pt can suppress poisoning and enhance activity. A geometric model has been proposed to explain the enhancement: the catalytic activity is controlled by the number of isolated groups of vacant Pt sites (reactive domains) whose size equals the number of Pt sites occupied by a single ad-atom (S_M). The model predicts that the number of such reactive domains peaks at a specific ad-atom coverage, and that the measured oxidation current follows this peak. This task reproduces the model predictions for three ad-atom species (Bi, As, Hg) to determine the coverage at which the number of reactive domains is maximal and the corresponding domain density.

## Approach
The Pt electrode surface is modelled as periodic fcc(100), (111), and (110) crystal planes with known site densities from the Pt lattice constant (3.92 Å). Ad-atoms are assumed to occupy S_M Pt sites each, arranged in a regular monolayer. When ad-atoms are desorbed in an orderly fashion, the vacancies form isolated domains of exactly S_M vacant sites at certain coverages. The task is to implement a simulation that counts the number of such reactive domains on each plane as a function of ad-atom coverage, then compute the arithmetic mean of the counts over the three planes. For each ad-atom species (Bi: S_M = 3, As: S_M = 2.5, Hg: S_M = 2), identify the coverage that maximizes this mean and the corresponding domain density (in units of 10^14 cm^-2).

## Reproduction target
Produce a CSV file `peak_data.csv` with columns: species (str), S_M (float), coverage_peak (dimensionless), domain_density (10^14 cm^-2). For Bi, As, and Hg, report the coverage at which the arithmetic mean of reactive domain counts over the three fcc planes is maximal, and the value of that mean as domain density. The simulation should sweep coverage from 0 to 1 with sufficient resolution to identify the peak. The output will be scored by a hidden verifier.

## Assets

- Platinum lattice constant
- Ad-atom S_M values

## Workflow steps

### Step 1: Compute reactive domain counts
- Role: process
- Action: Write a simulation to compute the number of isolated reactive domains of size S_M on the three low-index fcc surfaces (100, 111, 110) as a function of adatom coverage, using the lattice constant of Pt (3.92 Å). The simulation should assume orderly desorption from a monolayer to create isolated domains of size exactly S_M. For each species (Bi: S_M=3, As: S_M=2.5, Hg: S_M=2), compute the count per unit area for each plane and the arithmetic mean. Save the per-coverage results to domain_data.csv.
- Evidence: `/app/outputs/domain_data.csv`

### Step 2: Determine coverage peaks and domain density
- Role: scored (load-bearing)
- Action: For each species, identify the coverage where the mean_count is maximal, and compute the corresponding domain density (the maximum value) in units of 10^14 cm^-2. Report the results in peak_data.csv.
- Output file: `/app/outputs/peak_data.csv`
- Format: csv
- Contract: species (str), S_M (float), coverage_peak (float, dimensionless), domain_density (float, units: 10^14 cm^-2)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/peak_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### peak_data.csv
- path: `/app/outputs/peak_data.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: For each ad-atom species (Bi, As, Hg), the coverage at which the arithmetic mean of reactive domain counts over fcc(100),(111),(110) is maximal, and the corresponding domain density.
- schema:
  - `type`: table
  - `required_columns`: `species`, `S_M`, `coverage_peak`, `domain_density`
  - `units`:
    - `coverage_peak`: dimensionless
    - `domain_density`: 10^14 cm^-2

Notes: The solver must compute the geometric model; experimental current measurements are not part of this task. The hidden checker compares the reported values against gold values from the paper with tolerances (coverage_peak ±0.05, domain_density ±20% relative).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "peak_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "S_M",
          "coverage_peak",
          "domain_density"
        ],
        "units": {
          "coverage_peak": "dimensionless",
          "domain_density": "10^14 cm^-2"
        }
      },
      "description": "For each ad-atom species (Bi, As, Hg), the coverage at which the arithmetic mean of reactive domain counts over fcc(100),(111),(110) is maximal, and the corresponding domain density."
    }
  ],
  "notes": "The solver must compute the geometric model; experimental current measurements are not part of this task. The hidden checker compares the reported values against gold values from the paper with tolerances (coverage_peak ±0.05, domain_density ±20% relative)."
}
```

## How you are scored
A hidden verifier independently checks your submitted `peak_data.csv`. For each ad-atom species, it compares your reported coverage_peak and domain_density to hidden reference values. The verifier awards partial credit per species based on agreement within set tolerances, and the final reward is a weighted combination of these scores. To succeed, you must implement the geometric simulation correctly; reporting arbitrary numbers will not match the hidden references. The verifier does not disclose the reference values or tolerances.
