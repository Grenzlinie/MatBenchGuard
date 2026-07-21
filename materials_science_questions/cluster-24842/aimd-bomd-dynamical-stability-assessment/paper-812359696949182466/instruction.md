# DFT Molecular Dynamics and Specific Heat of Gallium Clusters

## Problem background
Experiments have shown that small gallium clusters can remain solid at temperatures far above the bulk melting point of gallium (303 K). This surprising behavior suggests that bonding in these finite-size systems differs substantially from the mixed covalent‑metallic bonding of bulk α‑Ga. To understand the origin of this enhanced thermal stability, it is necessary to study the clusters' dynamics at the atomic level using first‑principles simulations. In this task, you will compute temperature‑dependent specific‑heat curves for the neutral clusters Ga₁₇ and Ga₁₃ by performing density‑functional molecular dynamics (DFMD) simulations and a subsequent multiple‑histogram analysis. The resulting specific‑heat curves allow the melting temperature of each cluster to be identified.

## Approach
The central idea is to simulate the clusters at a wide range of temperatures using Born–Oppenheimer molecular dynamics with density functional theory (DFT). The DFT calculations use the local density approximation (LDA) and ultrasoft pseudopotentials in which only the 4s²4p¹ electrons of gallium are treated as valence electrons; the 3d electrons are kept frozen in the core. For each cluster, the simulation produces trajectories of the ionic positions, velocities, and potential energies at each temperature. The canonical ionic specific heat is then obtained from these trajectories using the multiple‑histogram technique, which optimally combines the energy distributions from all simulation temperatures into a continuous curve of Cᵥ/C₀ as a function of temperature, where C₀ = (3N − 9/2)k_B is the classical rotational‑plus‑vibrational limit for a cluster of N atoms. The peak of this curve is taken as the melting temperature.

## Reproduction target
Compute and output the normalized specific‑heat data for Ga₁₇ and Ga₁₃. For each cluster you must produce a CSV file (temperature [K] and Cᵥ/C₀) covering the full simulated temperature range. From the completed curves you are to identify the temperature of the specific‑heat maximum (the melting temperature). The evaluation will check, among other things, that the extracted melting points are consistent with the physical requirement that the cluster melting temperature exceeds the bulk gallium melting point of 303 K.

## Assets

- Open-source DFT simulation package (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org
- Gallium LDA ultrasoft pseudopotential (sp-valence, 4s²4p¹, 3d in core): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT geometry optimization of Ga17 and Ga13
- Role: process
- Action: Perform DFT geometry optimization for the neutral Ga17 and Ga13 clusters to obtain relaxed equilibrium structures. These structures serve as initial configurations for the subsequent molecular dynamics simulations.
- Evidence: `/app/outputs/optimized_geometries.xyz`

### Step 2: AIMD simulation for Ga17
- Role: process
- Action: Run Born-Oppenheimer isokinetic DFT-MD simulations for Ga17 at 23 temperatures in the range 150–1100 K, each for approximately 75 ps, starting from the optimized geometry. Record ionic trajectories (positions, velocities, potential energies).
- Evidence: `/app/outputs/ga17_trajectories.pickle`

### Step 3: AIMD simulation for Ga13
- Role: process
- Action: Run Born-Oppenheimer isokinetic DFT-MD simulations for Ga13 at 30 temperatures in the range 40–1750 K, totaling approximately 2.7 ns of aggregate simulation time, starting from the optimized geometry. Record ionic trajectories.
- Evidence: `/app/outputs/ga13_trajectories.pickle`

### Step 4: Specific heat curve for Ga17
- Role: scored (load-bearing)
- Action: Implement the multiple-histogram (MH) technique using the Ga17 AIMD trajectories from step_02 to compute the normalized ionic canonical specific heat C_v/C_0 as a function of temperature, where C_0 = (3N - 9/2)k_B. Output the temperature vs. normalized specific heat data.
- Output file: `/app/outputs/ga17_specific_heat.csv`
- Format: csv
- Contract: columns: temperature_K (float), normalized_specific_heat (float)
- Scoring: scored by hidden verifier

### Step 5: Specific heat curve for Ga13
- Role: scored
- Action: Apply the same multiple-histogram analysis to the Ga13 trajectories from step_03 to compute the normalized canonical specific heat curve.
- Output file: `/app/outputs/ga13_specific_heat.csv`
- Format: csv
- Contract: columns: temperature_K (float), normalized_specific_heat (float)
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
- target_policy: reference_match
- description: Ionic canonical specific heat (normalized) as a function of temperature for the Ga17 cluster, computed via the multiple-histogram method from AIMD trajectories.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `normalized_specific_heat`
  - `units`:
    - `temperature_K`: K
    - `normalized_specific_heat`: dimensionless (C_v / C_0)

### ga13_specific_heat.csv
- path: `/app/outputs/ga13_specific_heat.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ionic canonical specific heat (normalized) as a function of temperature for the Ga13 cluster, computed via the multiple-histogram method from AIMD trajectories.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `normalized_specific_heat`
  - `units`:
    - `temperature_K`: K
    - `normalized_specific_heat`: dimensionless (C_v / C_0)

Notes: The peak temperature of each specific-heat curve is used to infer the melting temperature. The checker will extract the peak from each CSV and compare to hidden reference values within tolerance, as well as verify the ordering Ga13 > Ga17 > bulk melting point (303 K).

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "normalized_specific_heat"
        ],
        "units": {
          "temperature_K": "K",
          "normalized_specific_heat": "dimensionless (C_v / C_0)"
        }
      },
      "description": "Ionic canonical specific heat (normalized) as a function of temperature for the Ga17 cluster, computed via the multiple-histogram method from AIMD trajectories."
    },
    {
      "file": "ga13_specific_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "normalized_specific_heat"
        ],
        "units": {
          "temperature_K": "K",
          "normalized_specific_heat": "dimensionless (C_v / C_0)"
        }
      },
      "description": "Ionic canonical specific heat (normalized) as a function of temperature for the Ga13 cluster, computed via the multiple-histogram method from AIMD trajectories."
    }
  ],
  "notes": "The peak temperature of each specific-heat curve is used to infer the melting temperature. The checker will extract the peak from each CSV and compare to hidden reference values within tolerance, as well as verify the ordering Ga13 > Ga17 > bulk melting point (303 K)."
}
```

## How you are scored
A hidden verifier reads the two CSV files and extracts the specific‑heat peak for each cluster. The verifier compares the peak temperatures to hidden reference values and checks basic physical consistency (e.g., both melting temperatures must exceed the bulk melting point of 303 K). The final reward is a weighted sum of partial scores, with the main weight on the accuracy of the peak temperatures. Full credit is awarded when the computed peaks are close to the hidden references and the physical conditions are satisfied; partial credit may be given if only one cluster’s peak is correct.
