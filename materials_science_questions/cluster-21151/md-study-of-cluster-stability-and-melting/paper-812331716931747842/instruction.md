# Molecular Dynamics Study of KCl Cluster Melting

## Problem background
First-order phase transitions in finite clusters are fundamental to understanding how bulk thermodynamic behavior emerges at the nanoscale. Alkali halide clusters, in particular, serve as model systems for studying size-dependent melting and freezing, because their interactions are well described by simple pairwise potentials. However, small clusters often exhibit hysteresis—the melting and freezing temperatures differ—and it is debated whether this hysteresis is an intrinsic finite-size effect or an artifact of the simulation protocol. Resolving this requires a computational approach that carefully controls the total energy of the system and examines the coexistence of solid-like and liquid-like ions during the transition.

## Approach
The workflow uses constant-energy (NVE) molecular dynamics simulations with the Born‑Mayer‑Huggins potential to study the melting transition of unconstrained KCl clusters. Starting from a rock‑salt (fcc) lattice, the cluster is heated rapidly by velocity rescaling, then a series of independent NVE runs is performed at increasing fixed total energies that span the transition. For each run the average temperature is recorded, yielding a temperature‑versus‑energy curve. To identify coexisting solid and liquid phases, the velocity autocorrelation function (VACF) of individual cations is computed at a chosen short time lag where solid‑like and liquid‑like ions are clearly separated. Ions are classified as liquid if their VACF exceeds a threshold determined from fully solid and fully liquid reference states; otherwise they are solid. The liquid molar fraction is then plotted against total energy. From the temperature‑energy curve one estimates the melting temperature (the plateau region) and the direct enthalpy of melting (the energy gap between the solid and liquid branches at the melting temperature). From the liquid‑fraction curve, a linear fit gives the VACF‑based enthalpy of melting.

## Reproduction target
Your goal is to compute the melting temperature and enthalpy of melting for a KCl cluster of size 5832 ions, and to assess the change in behavior from a smaller 512‑ion cluster.

Specifically, you must produce:
- Temperature‑vs‑total‑energy curves for clusters of 512 and 5832 ions along the melting path.
- For the 5832 cluster, the liquid molar fraction as a function of total energy, obtained via VACF‑based ion classification.
- From the 5832 data, derive the melting temperature (from the plateau in the T‑E curve) and the enthalpy of melting by two methods: (i) the direct energy‑difference method and (ii) the VACF‑based linear‑fit method.

The target is the set of artifacts (raw T‑E data, liquid fraction data, and final derived quantities) — not any single pre‑specified numerical value.

## Assets

- Born-Mayer-Huggins potential parameters for KCl
- Molecular dynamics code (e.g., LAMMPS): lammps

## Workflow steps

### Step 1: Prepare fcc configurations and pre-heat
- Role: process
- Action: Generate rock-salt (fcc) lattices for KCl clusters with 512 and 5832 ions. Heat the clusters quickly by velocity rescaling to a temperature just below the expected melting onset to provide initial configurations for the energy-controlled runs.
- Evidence: `/app/outputs/preheated_configurations`

### Step 2: Run NVE MD for KCl 512 and collect T-E data
- Role: scored
- Action: For the KCl 512 cluster, perform a series of constant-energy molecular dynamics simulations at increasing total energies covering the melting transition. At each fixed total energy, allow equilibration and record the average temperature over the production phase. Write the (total_energy_kJ_mol, temperature_K) pairs to /app/outputs/kcl_512_te.csv.
- Output file: `/app/outputs/kcl_512_te.csv`
- Format: csv
- Contract: CSV with columns: total_energy_kJ_mol (float, kJ/mol), temperature_K (float, K).
- Scoring: scored by hidden verifier

### Step 3: Run NVE MD for KCl 5832 and collect T-E data
- Role: scored
- Action: For the KCl 5832 cluster, perform a series of constant-energy simulations across the melting transition. Average the temperature for each fixed total energy. Write the (total_energy_kJ_mol, temperature_K) pairs to /app/outputs/kcl_5832_te.csv.
- Output file: `/app/outputs/kcl_5832_te.csv`
- Format: csv
- Contract: CSV with columns: total_energy_kJ_mol (float, kJ/mol), temperature_K (float, K).
- Scoring: scored by hidden verifier

### Step 4: Run NVE MD for KCl 5832 with velocity recording at melting state points
- Role: process
- Action: For the 5832-ion cluster, run additional constant-energy simulations for selected state points spanning the melting transition, storing the velocities of all ions at regular time steps to enable VACF computation. This can be done by appending velocity trajectory output to the previous runs or by running dedicated short runs at each energy.
- Evidence: `/app/outputs/velocity_trajectories`

### Step 5: Compute VACFs and determine phase classification threshold
- Role: process
- Action: From the velocity trajectories of a fully solid and a fully liquid state of the 5832 cluster, compute the individual velocity autocorrelation functions for all cations. Identify a time window (e.g., between steps 32 and 40, corresponding to a time interval) where the solid and liquid VACFs do not overlap. Set a classification threshold (e.g., VACF value at a specific time step) to discriminate solid from liquid ions.
- Evidence: `/app/outputs/vacf_threshold_params`

### Step 6: Classify ions using VACF and compute liquid molar fraction
- Role: scored (load-bearing)
- Action: For each saved state point of the 5832 cluster from the melting region, compute the VACF of each cation at the chosen time step. Classify an ion as liquid if its VACF value > threshold, otherwise solid. Calculate the liquid molar fraction (number of liquid ions divided by total ions). Write the (total_energy_kJ_mol, liquid_mole_fraction) pairs to /app/outputs/kcl_5832_liq_mol_frac.csv.
- Output file: `/app/outputs/kcl_5832_liq_mol_frac.csv`
- Format: csv
- Contract: CSV with columns: total_energy_kJ_mol (float, kJ/mol), liquid_mole_fraction (float, between 0 and 1).
- Scoring: scored by hidden verifier

### Step 7: Compute melting temperature and enthalpies
- Role: scored
- Action: Using kcl_5832_te.csv, identify the approximate energy range where the temperature curve is flat (plateau) and compute the average melting temperature. Compute the direct enthalpy of melting as the vertical energy gap between the extrapolated solid and liquid branches at the melting temperature. From kcl_5832_liq_mol_frac.csv, fit a line to the linear portion of the liquid fraction curve and compute the energy difference between the y=0 and y=1 intercepts to obtain the VACF-based enthalpy. Write a JSON file /app/outputs/results.json containing the melting temperature (K) and both enthalpies (kJ/mol).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: melting_temperature_K (number, K), enthalpy_direct_kJ_mol (number, kJ/mol), enthalpy_vacf_kJ_mol (number, kJ/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kcl_512_te.csv`
- `/app/outputs/kcl_5832_te.csv`
- `/app/outputs/kcl_5832_liq_mol_frac.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kcl_512_te.csv
- path: `/app/outputs/kcl_512_te.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature vs. total energy data for the KCl 512 cluster during melting. Checker compares points to hidden gold from the paper's Appendix.
- schema:
  - `type`: table
  - `columns`: `total_energy_kJ_mol`, `temperature_K`
  - `units`:
    - `total_energy_kJ_mol`: kJ/mol
    - `temperature_K`: K

### kcl_5832_te.csv
- path: `/app/outputs/kcl_5832_te.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature vs. total energy data for the KCl 5832 cluster during melting. Checker compares points to hidden gold from the paper's Appendix.
- schema:
  - `type`: table
  - `columns`: `total_energy_kJ_mol`, `temperature_K`
  - `units`:
    - `total_energy_kJ_mol`: kJ/mol
    - `temperature_K`: K

### kcl_5832_liq_mol_frac.csv
- path: `/app/outputs/kcl_5832_liq_mol_frac.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Liquid molar fraction vs. total energy for the 5832 cluster in the melting region. Checker compares values to hidden reference points extracted from the paper's figures/tables.
- schema:
  - `type`: table
  - `columns`: `total_energy_kJ_mol`, `liquid_mole_fraction`
  - `units`:
    - `total_energy_kJ_mol`: kJ/mol
    - `liquid_mole_fraction`: dimensionless

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Derived melting temperature and enthalpies. The checker recomputes the melting temperature from the plateau of kcl_5832_te.csv, the direct enthalpy from the energy gap, and the VACF enthalpy from a linear fit of kcl_5832_liq_mol_frac.csv, then compares to hidden gold values.
- schema:
  - `type`: object
  - `required`: `melting_temperature_K`, `enthalpy_direct_kJ_mol`, `enthalpy_vacf_kJ_mol`
  - `units`:
    - `melting_temperature_K`: K
    - `enthalpy_direct_kJ_mol`: kJ/mol
    - `enthalpy_vacf_kJ_mol`: kJ/mol

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kcl_512_te.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": [
          "total_energy_kJ_mol",
          "temperature_K"
        ],
        "units": {
          "total_energy_kJ_mol": "kJ/mol",
          "temperature_K": "K"
        }
      },
      "description": "Temperature vs. total energy data for the KCl 512 cluster during melting. Checker compares points to hidden gold from the paper's Appendix."
    },
    {
      "file": "kcl_5832_te.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": [
          "total_energy_kJ_mol",
          "temperature_K"
        ],
        "units": {
          "total_energy_kJ_mol": "kJ/mol",
          "temperature_K": "K"
        }
      },
      "description": "Temperature vs. total energy data for the KCl 5832 cluster during melting. Checker compares points to hidden gold from the paper's Appendix."
    },
    {
      "file": "kcl_5832_liq_mol_frac.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": [
          "total_energy_kJ_mol",
          "liquid_mole_fraction"
        ],
        "units": {
          "total_energy_kJ_mol": "kJ/mol",
          "liquid_mole_fraction": "dimensionless"
        }
      },
      "description": "Liquid molar fraction vs. total energy for the 5832 cluster in the melting region. Checker compares values to hidden reference points extracted from the paper's figures/tables."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "melting_temperature_K",
          "enthalpy_direct_kJ_mol",
          "enthalpy_vacf_kJ_mol"
        ],
        "units": {
          "melting_temperature_K": "K",
          "enthalpy_direct_kJ_mol": "kJ/mol",
          "enthalpy_vacf_kJ_mol": "kJ/mol"
        }
      },
      "description": "Derived melting temperature and enthalpies. The checker recomputes the melting temperature from the plateau of kcl_5832_te.csv, the direct enthalpy from the energy gap, and the VACF enthalpy from a linear fit of kcl_5832_liq_mol_frac.csv, then compares to hidden gold values."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently score each output file you write. It will check the consistency and correctness of your temperature‑energy data against reference ranges, validate the liquid molar fraction curve, and recompute the melting temperature and both enthalpies from your submitted raw data. The reward assigned to your submission is a weighted combination of the performance on these artifacts; simply reporting a number is insufficient — the verifier will recompute the derived quantities from your raw outputs and compare with hidden reference values. To achieve a high score, your simulation protocol must faithfully reconstruct the melting process and the phase‑classification analysis.
