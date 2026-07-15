# Molecular Dynamics Study of Structural Transition in Small Atomic Clusters

## Problem background
Small atomic clusters at temperatures above the bulk melting point may exhibit a structural transition from close-packed, compact arrangements to chainlike configurations with a minimal number of interatomic bonds. A theoretical model, the virtual chains model, hypothesizes that in the high-temperature regime the average potential energy of a cluster of g atoms (U_g) scales linearly as U_g ≈ (g-1)U_2, where U_2 is the dimer potential energy. This task requires testing that hypothesis through molecular dynamics simulations and quantitative analysis of the structural and thermodynamic properties of clusters with up to nine atoms.

## Approach
Implement molecular dynamics simulations in the (P,T)-ensemble using a short‑range interatomic potential (cutoff 1.6a, a/r0 = 6) and a Berendsen thermostat. Simulate clusters of sizes g = 3, 4, 5, 6, 7 at a series of reduced temperatures T* spanning 0.42 to 0.71, and run an additional simulation for g=6 at T* = 0.46. Record atomic trajectories. Compute the time‑averaged potential energy U_g from each trajectory and obtain U_2 from a separate dimer simulation or from an analytical integration of the potential. From these compute the normalized ratio U_g / ((g-1) U_2) for each (g,T*). Analyze bond‑count distributions to estimate the structural transition temperature T0* at which the probabilities of the minimum‑bond and maximum‑bond states are equal. At T* = 0.71 determine the probability P1 that a cluster forms exactly one simple virtual chain (a linear structure in which interior atoms have two nearest neighbours and end atoms have one). For a 6‑atom cluster at T* = 0.46 compute the radial distribution function G(r) around the central atom, expressed in reduced distance units.

## Reproduction target
Produce four scored CSV files:

1. potential_energy_ratio.csv: for g = 3,4,5,7 at ≥5 temperatures spanning T* 0.42–0.71, the normalized ratio U_g / ((g-1)U_2).
2. transition_temperatures.csv: for g = 3,4,5,7, the temperature T0* where P_{g-1} = P_{3g-6}.
3. single_chain_probability.csv: for g = 3,…,9 at T* = 0.71, the probability P1 of a single simple virtual chain.
4. rdf_g6.csv: for a 6‑atom cluster at T* = 0.46, the radial distribution function G(r) in reduced units r* = 2^{1/6} r/a for r* ∈ [0,3].

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): http://lammps.sandia.gov

## Workflow steps

### Step 1: Molecular Dynamics Simulation
- Role: process
- Action: Perform MD simulations in the (P,T)-ensemble using a short-range potential (cutoff 1.6a, a/r0=6) and a Berendsen thermostat. Simulate clusters of sizes g=3,4,5,6,7 at temperatures T* spanning 0.42 to 0.71, and for g=6 at T*=0.46. Record atomic trajectories (positions, velocities). For each cluster size, also simulate a single dimer (g=2) to compute U2 as a function of T*.
- Evidence: none

### Step 2: Compute average potential energy ratio
- Role: scored (load-bearing)
- Action: From the MD trajectories for clusters g=3,4,5,7 at each temperature T*, compute the average potential energy U_g (time average of total potential energy). Compute the dimer average potential energy U2 at the same temperatures from a separate dimer simulation or via analytical integration of the potential. For each (g,T*) compute the normalized ratio U_g / ((g-1) * U2). Write the results to `potential_energy_ratio.csv`.
- Output file: `/app/outputs/potential_energy_ratio.csv`
- Format: csv
- Contract: CSV with columns: g (integer), T_star (float), ratio (float). At least 5 temperatures per g for g=3,4,5,7.
- Scoring: scored by hidden verifier

### Step 3: Determine structural transition temperature T0*
- Role: scored
- Action: For each cluster size g=3,4,5,7, analyze the MD trajectories to estimate the bond-count distribution P_k at each temperature. Identify the temperature T0* at which the probability of the minimum-bond state (k=g-1) equals the probability of the maximum-bond state (k=3g-6). Write the results to `transition_temperatures.csv`.
- Output file: `/app/outputs/transition_temperatures.csv`
- Format: csv
- Contract: CSV with columns: g (integer), T0_star (float). For g=3,4,5,7.
- Scoring: scored by hidden verifier

### Step 4: Probability of single simple virtual chain
- Role: scored
- Action: From the MD trajectories at T*=0.71 for cluster sizes g=3..9, determine the probability P1 that the cluster consists of exactly one simple virtual chain. Atoms are considered bonded if their distance < a+r0; a cluster forms a single simple virtual chain if its atoms can be numbered such that each interior atom is bonded only to its immediate neighbours and the end atoms have only one bond. Write the results to `single_chain_probability.csv`.
- Output file: `/app/outputs/single_chain_probability.csv`
- Format: csv
- Contract: CSV with columns: g (integer), P1 (float). For g=3..9 at T*=0.71.
- Scoring: scored by hidden verifier

### Step 5: Radial distribution function for g=6
- Role: scored
- Action: From the MD trajectory for a 6-atom cluster at T*=0.46, identify the central atom (closest to center of mass). Compute the average number of neighbors S(r) as a function of distance r from the central atom. Derive the radial distribution function G(r) in reduced units r* = 2^{1/6} * r/a. Output as `rdf_g6.csv` for r* up to 3.
- Output file: `/app/outputs/rdf_g6.csv`
- Format: csv
- Contract: CSV with columns: r_star (float), G (float). r_star = 2^{1/6} r/a, range 0 to 3.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/potential_energy_ratio.csv`
- `/app/outputs/transition_temperatures.csv`
- `/app/outputs/single_chain_probability.csv`
- `/app/outputs/rdf_g6.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### potential_energy_ratio.csv
- path: `/app/outputs/potential_energy_ratio.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Normalized average potential energy ratio. Checked against reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `g`, `T_star`, `ratio`

### transition_temperatures.csv
- path: `/app/outputs/transition_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Characteristic structural transition temperature for each cluster size. Checked within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `g`, `T0_star`

### single_chain_probability.csv
- path: `/app/outputs/single_chain_probability.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Probability of a single simple virtual chain at T*=0.71. Checked against reference within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `g`, `P1`

### rdf_g6.csv
- path: `/app/outputs/rdf_g6.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Radial distribution function G(r) for the central atom of a 6-atom cluster at T*=0.46. First peak location and height, and plateau value are checked.
- schema:
  - `type`: table
  - `required_columns`: `r_star`, `G`

Notes: All scored artifacts are numerically verifiable against paper-reported curves with appropriate tolerances. No gold values are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "potential_energy_ratio.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "g",
          "T_star",
          "ratio"
        ]
      },
      "description": "Normalized average potential energy ratio. Checked against reference values within tolerance."
    },
    {
      "file": "transition_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "g",
          "T0_star"
        ]
      },
      "description": "Characteristic structural transition temperature for each cluster size. Checked within tolerance."
    },
    {
      "file": "single_chain_probability.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "g",
          "P1"
        ]
      },
      "description": "Probability of a single simple virtual chain at T*=0.71. Checked against reference within tolerance."
    },
    {
      "file": "rdf_g6.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_star",
          "G"
        ]
      },
      "description": "Radial distribution function G(r) for the central atom of a 6-atom cluster at T*=0.46. First peak location and height, and plateau value are checked."
    }
  ],
  "notes": "All scored artifacts are numerically verifiable against paper-reported curves with appropriate tolerances. No gold values are disclosed here."
}
```

## How you are scored
A hidden verifier independently scores each of the four submitted CSV artifacts. The verifier compares your numerical output against reference data (derived from published simulation results) using predefined tolerances. For potential_energy_ratio.csv, each (g,T*) value is checked against a reference curve. For transition_temperatures.csv, the T0* values are compared within a tolerance. For single_chain_probability.csv, the P1 values are checked against a reference trend. For rdf_g6.csv, the location and height of the first peak and the plateau value for r* > 2 are examined. Each artifact contributes a weighted fraction to the total reward; the potential‑energy‑ratio carries the largest weight. All tolerance thresholds are hidden and chosen to absorb typical run‑to‑run spread from different MD implementations. Simply reporting a single number will not pass; the verifier parses your output files directly.
