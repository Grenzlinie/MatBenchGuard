# Ga Cluster Melting Points from DFMD Specific Heat

## Problem background
Small atomic clusters can exhibit melting properties that differ dramatically from the bulk. Certain small gallium clusters have been observed experimentally to remain solid at temperatures well above the bulk melting point of gallium (303 K). Understanding this behavior requires a direct computation of the ionic specific heat from density-functional molecular dynamics (DFMD) simulations and a subsequent analysis of the melting signatures in the resulting curves.

## Approach
We use density-functional Born–Oppenheimer molecular dynamics within the local density approximation (LDA). The electronic structure is described with pseudopotentials that treat the gallium 4s and 4p electrons as valence electrons, while keeping the 3d electrons in the core. The workflow consists of:
- DFT geometry optimization of neutral Ga17 and Ga13 clusters to obtain low-energy starting structures.
- Isokinetic DFMD simulations for each cluster over a wide range of temperatures that spans from well below the expected melting point to well above it, generating energy and trajectory data.
- From the collected total energies, the ionic canonical specific heat (normalized by the classical zero-temperature limit) is computed as a function of temperature using the multiple-histogram technique.
The temperature that gives the maximum specific heat is taken as the melting point of the cluster.

## Reproduction target
Compute the normalized ionic canonical specific-heat curves for the neutral Ga17 and Ga13 clusters using DFMD and multiple-histogram analysis, and output each as a CSV file with columns for temperature (K) and normalized specific heat (dimensionless). From these curves, determine the melting temperature (the temperature at which the specific heat reaches its maximum) for each cluster. Then verify the relative ordering of the melting temperatures: the melting point of Ga13 must be higher than that of Ga17, and both must be above the bulk gallium melting point of 303 K.

## Assets

- CP2K: https://www.cp2k.org

## Workflow steps

### Step 1: DFT geometry optimization of Ga clusters
- Role: process
- Action: Perform DFT geometry optimization (LDA functional, sp‑valence pseudopotentials with 3d electrons in core) for neutral Ga17 and Ga13 to find low‑energy equilibrium structures; use the lowest‑energy geometry of each cluster as starting configuration for MD.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 2: MD simulations for Ga17
- Role: process
- Action: Run isokinetic Born–Oppenheimer DFMD for Ga17 at 23 target temperatures between 150 K and 1100 K, each trajectory of 75 ps (total simulated time 1.65 ns), using the same DFT settings as the optimization. Collect total energy and ionic positions for each temperature.
- Evidence: `/app/outputs/md_log_ga17.txt`

### Step 3: MD simulations for Ga13
- Role: process
- Action: Run isokinetic Born–Oppenheimer DFMD for Ga13 at 30 target temperatures between 40 K and 1750 K, total simulation time ≈2.7 ns, using the same DFT settings as the optimization. Collect trajectory data.
- Evidence: `/app/outputs/md_log_ga13.txt`

### Step 4: Specific heat curve for Ga17
- Role: scored (load-bearing)
- Action: From the Ga17 trajectory/data compute the ionic canonical specific heat (normalized by the classical zero‑temperature limit) as a function of temperature using the multiple‑histogram technique. Output a CSV with two columns: temperature (K) and normalized specific heat (dimensionless). The checker extracts the peak temperature (melting point) and compares it to the paper‑reported value within tolerance.
- Output file: `/app/outputs/ga17_specific_heat.csv`
- Format: csv
- Contract: CSV with columns: temperature (float, K), normalized_specific_heat (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 5: Specific heat curve for Ga13
- Role: scored (load-bearing)
- Action: From the Ga13 trajectory/data compute the ionic canonical specific heat (normalized) as a function of temperature using the multiple‑histogram technique. Output a CSV with two columns: temperature (K) and normalized specific heat (dimensionless). The checker extracts the peak temperature and compares it to the paper‑reported value within tolerance.
- Output file: `/app/outputs/ga13_specific_heat.csv`
- Format: csv
- Contract: CSV with columns: temperature (float, K), normalized_specific_heat (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ga17_specific_heat.csv`
- `/app/outputs/ga13_specific_heat.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ga17_specific_heat.csv
- path: `/app/outputs/ga17_specific_heat.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Specific heat curve for Ga17; temperature in K and normalized specific heat (C/C0) from multiple‑histogram analysis.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `normalized_specific_heat`
  - `units`:
    - `temperature`: K
    - `normalized_specific_heat`: dimensionless

### ga13_specific_heat.csv
- path: `/app/outputs/ga13_specific_heat.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Specific heat curve for Ga13; temperature in K and normalized specific heat (C/C0) from multiple‑histogram analysis.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `normalized_specific_heat`
  - `units`:
    - `temperature`: K
    - `normalized_specific_heat`: dimensionless

Notes: The hidden checker extracts the temperature of maximum specific heat (melting point) from each submitted CSV and compares it to the paper‑reported gold with a relative tolerance. The ordering Ga13_peak > Ga17_peak > 303 K is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ga17_specific_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "normalized_specific_heat"
        ],
        "units": {
          "temperature": "K",
          "normalized_specific_heat": "dimensionless"
        }
      },
      "description": "Specific heat curve for Ga17; temperature in K and normalized specific heat (C/C0) from multiple‑histogram analysis."
    },
    {
      "file": "ga13_specific_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "normalized_specific_heat"
        ],
        "units": {
          "temperature": "K",
          "normalized_specific_heat": "dimensionless"
        }
      },
      "description": "Specific heat curve for Ga13; temperature in K and normalized specific heat (C/C0) from multiple‑histogram analysis."
    }
  ],
  "notes": "The hidden checker extracts the temperature of maximum specific heat (melting point) from each submitted CSV and compares it to the paper‑reported gold with a relative tolerance. The ordering Ga13_peak > Ga17_peak > 303 K is also verified."
}
```

## How you are scored
Your submission will be scored by a hidden automatic verifier. For each cluster, the verifier reads the submitted CSV file, applies a smoothing procedure, and identifies the temperature of peak specific heat (the melting temperature). It checks that the extracted melting temperature lies within a scientifically acceptable tolerance range and that the relative ordering Ga13 > Ga17 > 303 K is satisfied. Each cluster contributes equally to the final reward (0.5 for Ga17, 0.5 for Ga13). Full credit is awarded when the melting temperatures meet the expected criteria; the reward decreases as the deviation increases. Simply reporting numbers from the literature is not sufficient; the verifier evaluates the computed specific-heat curves directly.
