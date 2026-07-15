# Cooling-rate dependence of local pair ordering in simulated aluminium glass

## Problem background
The atomic structure of metallic glasses, formed by rapid quenching from the melt, is sensitive to the cooling rate used during solidification. Understanding how different local structural motifs — such as icosahedral clusters, fcc-like units, hcp-like units, and defective arrangements — depend on the cooling history is key to linking processing conditions to glass stability and mechanical properties. In particular, the Honeycutt–Andersen pair analysis technique provides a powerful way to decompose the local order into a set of characteristic pair types, each with a distinct geometric signature. This task investigates aluminium glass simulated by constant-pressure molecular dynamics, and aims to quantify how the relative populations of five key pair types (1551, 1541, 1431, 1421, 1422) vary across a wide range of cooling rates. The central quantity to produce is the percentage of each pair type at the final low temperature of 300 K for each cooling rate, which will then be assessed for systematic cooling-rate trends.

## Approach
The approach combines large-scale molecular dynamics simulations with a common structural analysis algorithm. A system of 500 aluminium atoms is described by the Ercolessi-Adams many-body glue potential and cooled under constant pressure from the liquid state down to 300 K. Six cooling rates, spanning nearly four orders of magnitude (from 1.9×10^12 K/s to 1.9×10^15 K/s), are applied to generate a set of glassy configurations. For each cooled trajectory, the Honeycutt–Andersen pair analysis technique is applied to classify every atom pair according to its four-index descriptor. The relative fractions of the five pair types 1551, 1541, 1431, 1421, and 1422 are extracted at 300 K, providing a multivariate fingerprint of the local structure as a function of the thermal history. The comparison across cooling rates reveals how microstructural ordering evolves with quench severity.

## Reproduction target
Produce the relative percentages of the five pair types at 300 K for all six cooling rates and save them in the file `pair_fractions_300K.csv`. The target is to correctly capture the cooling-rate dependence trends of each pair type. For some pair types the fraction exhibits a monotonic trend (either increasing or decreasing) with cooling rate, while for others the fraction is nearly constant, showing no systematic variation. The verifier will evaluate your submitted fractions against these expected structural relationships. No separate prediction or holdout is required; the complete output is the CSV table described in the output contract.

## Assets

- Ercolessi-Adams glue potential for Aluminium: https://www.ctcms.nist.gov/potentials/entry/Al__Al_1.eam.alloy/
- LAMMPS molecular dynamics package: https://lammps.sandia.gov
- Honeycutt-Andersen pair analysis technique: 10.1021/j100303a014

## Workflow steps

### Step 1: Molecular dynamics quenching simulations
- Role: process
- Action: Run constant-pressure molecular dynamics simulations for 500 aluminium atoms using the Ercolessi-Adams glue potential, periodic boundary conditions, and six cooling rates: gamma1=1.9e12 K/s, gamma2=4.7e12 K/s, gamma3=9.5e12 K/s, gamma4=1.9e13 K/s, gamma5=1.9e14 K/s, gamma6=1.9e15 K/s. Generate atomic trajectories from high temperature down to 300 K.
- Evidence: `/app/outputs/md_quench.log`

### Step 2: Pair analysis and cooling-rate dependence at 300 K
- Role: scored (load-bearing)
- Action: For each of the six cooling-rate trajectories, apply the Honeycutt–Andersen pair analysis technique to extract the relative percentages (fractions) of the five pair types: 1551, 1541, 1431, 1421, 1422 at the final temperature 300 K. Save all results in one CSV.
- Output file: `/app/outputs/pair_fractions_300K.csv`
- Format: csv
- Contract: columns: cooling_rate (text), T (numeric, temperature 300.0 K), pair_index (text, one of 1551,1541,1431,1421,1422), fraction (numeric, relative percentage 0-100).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pair_fractions_300K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pair_fractions_300K.csv
- path: `/app/outputs/pair_fractions_300K.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Relative percentages of five pair types for six cooling rates at 300 K. Used to verify monotonic trends (1551 decreases with cooling rate, 1422 increases) and independence (1541,1431,1421 show no systematic trend).
- schema:
  - `type`: table
  - `required_columns`: `cooling_rate`, `T`, `pair_index`, `fraction`
  - `units`:
    - `T`: K
    - `fraction`: percentage (0-100)

Notes: The checker will verify structural relationships (ordering, trend monotonicity, and independence) rather than exact numerical match. Small non-monotonic jumps due to numerical noise are allowed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pair_fractions_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "cooling_rate",
          "T",
          "pair_index",
          "fraction"
        ],
        "units": {
          "T": "K",
          "fraction": "percentage (0-100)"
        }
      },
      "description": "Relative percentages of five pair types for six cooling rates at 300 K. Used to verify monotonic trends (1551 decreases with cooling rate, 1422 increases) and independence (1541,1431,1421 show no systematic trend)."
    }
  ],
  "notes": "The checker will verify structural relationships (ordering, trend monotonicity, and independence) rather than exact numerical match. Small non-monotonic jumps due to numerical noise are allowed."
}
```

## How you are scored
A hidden verifier will read your `pair_fractions_300K.csv` and check the structural properties of the data. For each of the five pair types, the verifier determines whether the fraction as a function of cooling rate follows the correct pattern (monotonic increase, monotonic decrease, or near‑constancy) that the original study reported. Partial credit is assigned for each condition that is satisfied; the more patterns correctly matched, the higher your score. The verifier uses small tolerances to accommodate numerical noise from your specific MD integration and analysis implementation, but the fundamental ordering and trend direction must be correct. There is no need to match exact paper values; what matters is that the cooling-rate trends are reproduced.
