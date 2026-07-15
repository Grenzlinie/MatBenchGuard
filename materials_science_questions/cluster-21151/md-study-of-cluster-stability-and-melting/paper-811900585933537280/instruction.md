# Energetic Stability of Magic-Size Ni Clusters from MD Simulations

## Problem background
Small metal clusters often exhibit magic-number stability, where certain cluster sizes are energetically preferred over others. For Ni clusters, icosahedral configurations with atom counts N = 55 and N = 147 are of special interest because they may be exceptionally stable. The energetic preference can be quantified by the ground-state potential energy per atom and by the second energy difference Δ_N^{(2)} = E_{N-1} – 2E_N + E_{N+1}. Understanding how these energetic quantities change with temperature provides insight into the structural stability of magic-size clusters.

## Approach
Perform molecular dynamics simulations of Ni clusters using the Voter-Chen embedded-atom method (EAM) potential. Build initial atomic configurations by populating fcc coordination shells for cluster sizes N in the ranges 50–60 and 142–152. For each size, heat the cluster above its melting temperature, then cool in steps of 20 K with an exposure time of approximately 2×10^5 MD steps (200 ps) per temperature step, recording the potential energy per atom during cooling. From the cooling-run energies, extract the ground-state energy per atom E_p(N) at the lowest temperature, and for N = 55 and N = 147 compute the second energy difference Δ_N^{(2)}(T) at each temperature step using the energies of clusters N−1, N, and N+1. The E_p(N) curve is then examined for local minima, and the temperature dependence of Δ_N^{(2)} is used to assess whether the energetic preference persists up to the melting point.

## Reproduction target
Produce two output files.
1. `Ni_ground_state_energy.csv` — ground-state potential energy per atom E_p (eV/atom) for each Ni cluster size N in the ranges 50–60 and 142–152.
2. `Ni_delta2_temperature.csv` — the temperature T (K) and the second energy difference Δ_N^{(2)} (eV) for N = 55 and N = 147 at each cooling temperature step.
The hidden verifier will check whether the E_p(N) data exhibit local minima at N = 55 and N = 147, and whether Δ_N^{(2)} remains positive and approximately constant up to the melting temperature, which would indicate the structural stability of the magic-size clusters.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- Voter-Chen EAM potential for Ni: https://www.ctcms.nist.gov/potentials/entry/1999--Voter-A-F--Ni--LAMMPS--ipr1/

## Workflow steps

### Step 1: Generate initial Ni cluster structures
- Role: process
- Action: Generate atomic coordinates for Ni clusters with N from 50 to 60 and 142 to 152 by populating fcc coordination shells. Save initial configurations to be used in MD runs.
- Evidence: none

### Step 2: Run MD heating/cooling cycles with LAMMPS
- Role: process
- Action: For each Ni cluster size, perform an MD simulation using the Voter-Chen EAM potential. Heat the cluster above the melting temperature, then cool in steps of 20 K with an exposure time of approximately 2×10^5 MD steps (200 ps) per temperature. Record potential energy per atom at every temperature step.
- Evidence: none

### Step 3: Extract ground-state energy per atom Ep(N)
- Role: scored (load-bearing)
- Action: From the cooling runs, take the potential energy per atom at the lowest temperature reached for each N. Write a CSV with two columns: N (integer) and Ep (eV/atom).
- Output file: `/app/outputs/Ni_ground_state_energy.csv`
- Format: csv
- Contract: Columns: N (integer), Ep (float, eV/atom). One row per cluster size.
- Scoring: scored by hidden verifier

### Step 4: Compute second energy difference Δ_N^{(2)} vs temperature
- Role: scored
- Action: For N=55 and N=147, compute Δ_N^{(2)} = E_{N-1} - 2E_N + E_{N+1} at each cooling temperature step using the energies of clusters N-1, N, N+1 (i.e., for N=55 use sizes 54,55,56; for N=147 use 146,147,148). Write a CSV with columns: N (integer, either 55 or 147), T (float, K), Delta2 (float, eV).
- Output file: `/app/outputs/Ni_delta2_temperature.csv`
- Format: csv
- Contract: Columns: N (integer), T (float, K), Delta2 (float, eV). One row per (N, T) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/Ni_ground_state_energy.csv`
- `/app/outputs/Ni_delta2_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### Ni_ground_state_energy.csv
- path: `/app/outputs/Ni_ground_state_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Ground-state potential energy per atom for Ni clusters with N in the ranges 50-60 and 142-152. Used to verify local energy minima at N=55 and 147.
- schema:
  - `type`: table
  - `required_columns`: `N`, `Ep`
  - `units`:
    - `Ep`: eV/atom

### Ni_delta2_temperature.csv
- path: `/app/outputs/Ni_delta2_temperature.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Second energy difference as a function of temperature for Ni55 and Ni147. Verifies that Δ_N^{(2)} remains positive and essentially constant up to the melting temperature.
- schema:
  - `type`: table
  - `required_columns`: `N`, `T`, `Delta2`
  - `units`:
    - `T`: K
    - `Delta2`: eV

Notes: Scoring is entirely structural: the checker verifies local minima in Ep(N) and positivity/constancy of Δ_N^{(2)} without comparing to external gold values. The target_policy is structural_audit for both artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "Ni_ground_state_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "Ep"
        ],
        "units": {
          "Ep": "eV/atom"
        }
      },
      "description": "Ground-state potential energy per atom for Ni clusters with N in the ranges 50-60 and 142-152. Used to verify local energy minima at N=55 and 147."
    },
    {
      "file": "Ni_delta2_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "T",
          "Delta2"
        ],
        "units": {
          "T": "K",
          "Delta2": "eV"
        }
      },
      "description": "Second energy difference as a function of temperature for Ni55 and Ni147. Verifies that Δ_N^{(2)} remains positive and essentially constant up to the melting temperature."
    }
  ],
  "notes": "Scoring is entirely structural: the checker verifies local minima in Ep(N) and positivity/constancy of Δ_N^{(2)} without comparing to external gold values. The target_policy is structural_audit for both artifacts."
}
```

## How you are scored
A hidden verifier judges your submitted CSV files. It independently checks (a) that your E_p(N) curve shows local minima at N = 55 and N = 147, and (b) that your Δ_N^{(2)}(T) data for N = 55 and N = 147 remain positive and nearly constant over a broad temperature range up to at least 800 K. The final reward is a weighted combination of these checks; simply producing numbers from the simulation is not enough — the trends and stability characteristics must satisfy the required structural conditions.
