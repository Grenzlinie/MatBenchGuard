# Reactive molecular dynamics protocol for ethylene polymerization in nanotube confinement and bulk

## Problem background
Understanding how nanoscale confinement affects chemical reactions is important for designing nanotube-based synthetic vessels. This computational study investigates ethylene polymerization in three distinct geometries: bulk liquid, inside a (10,10) carbon nanotube, and inside a (7,7) carbon nanotube. Using all-atom reactive molecular dynamics simulations, the aim is to quantify the polymerization kinetics under confinement and compare them to the uninhibited bulk behaviour. Such comparisons reveal how spatial constraints and the presence of reaction by-products alter the progression and final extent of polymer growth.

## Approach
The polymerization of ethylene is simulated with the AIREBO reactive potential in LAMMPS. Instead of explicitly modelling the nanotube walls, a soft-wall cylindrical confining potential is employed. This potential is fitted to the cylindrically averaged interaction energy of atomic probes with explicit rigid nanotubes, reproducing the adsorption and repulsion physics without the cost of simulating the tube itself. Three systems are constructed at equivalent atomic number densities: a bulk liquid, a (10,10) tube, and a (7,7) tube. Canonical (NVT) simulations are run at several elevated temperatures (2800‑3400 K) to generate radicals thermally and drive chain growth. The reaction progress is tracked via the weight‑averaged molecular weight M_w. Second‑order kinetics are assumed to extract temperature‑dependent rate constants, and an Arrhenius analysis yields activation energies for each geometry. The entire workflow computes the confinement effect on polymerization rates and energetics.

## Reproduction target
Obtain weight‑averaged molecular weight (M_w) as a function of time for each system (bulk, (10,10) tube, (7,7) tube) at temperatures 2800, 3000, 3200, and 3400 K. From these curves, fit second‑order rate constants. Finally, determine the activation energy for polymerization in each geometry via an Arrhenius fit of the rate constants. The output files must contain the complete set of curves, rate constants, and activation energies; the verifier will check that these reflect the expected physical trends of nanoscale confinement on the polymerization reaction.

## Assets

- LAMMPS: https://www.lammps.org/

## Workflow steps

### Step 1: Compute equilibrium nanotube radii
- Role: process
- Action: Perform 0 K energy minimization of pristine (10,10) and (7,7) single-walled carbon nanotubes using the AIREBO potential in LAMMPS to obtain the equilibrium inner radii R.
- Evidence: `/app/outputs/step_1_radii.json`

### Step 2: Compute cylindrical average interaction energy profiles
- Role: process
- Action: For each tube chirality, compute the AIREBO interaction energy between a single C or H atom probe and an explicit rigid nanotube as a function of radial distance from the tube axis. Cylindrically average the energy to obtain reference V(r) profiles for fitting the confining potential.
- Evidence: `/app/outputs/step_2_energy_profiles.csv`

### Step 3: Fit confining potential parameters
- Role: process
- Action: Using the functional form V(r)=A*(σ/(R-r))^(2p+q)-B*(σ/(R-r))^(p+q)+C*(σ/(R-r))^q+D with p=4 and the radii from step_1, fit the remaining parameters (A, B, C, D, q, σ) to the reference V(r) profiles from step_2 for each tube chirality.
- Evidence: `/app/outputs/step_3_fitted_params.json`

### Step 4: Build initial systems
- Role: process
- Action: Construct initial configurations of ethylene monomers for three systems: bulk (128 monomers, cubic box 19.9 Å, 3D periodic), (10,10) tube (78 monomers, length 60 Å, 1D periodic), and (7,7) tube (100 monomers, length 557 Å, 1D periodic). Set atomic number density to ~0.75 g/cm³.
- Evidence: `/app/outputs/step_4_system_setup.txt`

### Step 5: Run reactive MD simulations
- Role: process
- Action: Run canonical-ensemble (NVT) reactive molecular dynamics of ethylene polymerization in all three systems at temperatures 2800, 3000, 3200, 3400 K, using LAMMPS with AIREBO potential, fitted confining potential (for tubes), and a generalized Langevin thermostat. Simulate at least 5 ns for bulk, 20 ns for tubes.
- Evidence: `/app/outputs/step_5_md.log`

### Step 6: Compute weight-averaged molecular weight Mw vs time
- Role: scored (load-bearing)
- Action: From the simulation trajectories, identify molecular fragments and compute weight-averaged molecular weight M_w as a function of time for each system and temperature. Write the results to step_01_mw_vs_time.csv.
- Output file: `/app/outputs/step_01_mw_vs_time.csv`
- Format: csv
- Contract: Columns: system (bulk,10_10,7_7), temperature_K (int), time_ns (float), Mw_g_per_mol (float).
- Scoring: scored by hidden verifier

### Step 7: Fit second-order rate constants
- Role: scored
- Action: Assuming second-order polymerization kinetics, fit the M_w(t) data from step_01 for each system and each temperature to obtain a rate constant. Write the fitted rate constants to step_02_rate_constants.csv.
- Output file: `/app/outputs/step_02_rate_constants.csv`
- Format: csv
- Contract: Columns: system (bulk,10_10,7_7), temperature_K (int), rate_constant_s_per_mol (float).
- Scoring: scored by hidden verifier

### Step 8: Determine activation energies
- Role: scored
- Action: Perform an Arrhenius fit (ln k vs 1/T) using the rate constants from step_02 for each system to extract the activation energy and its standard error. Write the results to step_03_activation_energies.csv.
- Output file: `/app/outputs/step_03_activation_energies.csv`
- Format: csv
- Contract: Columns: system (bulk,10_10,7_7), activation_energy_kcal_per_mol (float), Ea_error_kcal_per_mol (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_mw_vs_time.csv`
- `/app/outputs/step_02_rate_constants.csv`
- `/app/outputs/step_03_activation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_mw_vs_time.csv
- path: `/app/outputs/step_01_mw_vs_time.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Weight-averaged molecular weight evolution data. The checker verifies monotonic increase, plateau in confined systems, and correct ordering (bulk > (10,10) > (7,7)) at comparable times.
- schema:
  - `type`: table
  - `required_columns`: `system`, `temperature_K`, `time_ns`, `Mw_g_per_mol`
  - `units`:
    - `time_ns`: nanosecond
    - `Mw_g_per_mol`: g/mol

### step_02_rate_constants.csv
- path: `/app/outputs/step_02_rate_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fitted second-order polymerization rate constants. The checker checks ordering and that the ratio of bulk to tube rates falls within the paper's reported factor windows (18±9 for (10,10), 50±25 for (7,7)).
- schema:
  - `type`: table
  - `required_columns`: `system`, `temperature_K`, `rate_constant_s_per_mol`
  - `units`:
    - `rate_constant_s_per_mol`: s^{-1} mol^{-1}

### step_03_activation_energies.csv
- path: `/app/outputs/step_03_activation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Activation energies from Arrhenius analysis. The checker verifies that the activation energies fall within the paper-reported error bars: 52–78 kcal/mol (bulk), 44–60 ((10,10)), 49–59 ((7,7)).
- schema:
  - `type`: table
  - `required_columns`: `system`, `activation_energy_kcal_per_mol`, `Ea_error_kcal_per_mol`
  - `units`:
    - `activation_energy_kcal_per_mol`: kcal/mol
    - `Ea_error_kcal_per_mol`: kcal/mol

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_mw_vs_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "temperature_K",
          "time_ns",
          "Mw_g_per_mol"
        ],
        "units": {
          "time_ns": "nanosecond",
          "Mw_g_per_mol": "g/mol"
        }
      },
      "description": "Weight-averaged molecular weight evolution data. The checker verifies monotonic increase, plateau in confined systems, and correct ordering (bulk > (10,10) > (7,7)) at comparable times."
    },
    {
      "file": "step_02_rate_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "temperature_K",
          "rate_constant_s_per_mol"
        ],
        "units": {
          "rate_constant_s_per_mol": "s^{-1} mol^{-1}"
        }
      },
      "description": "Fitted second-order polymerization rate constants. The checker checks ordering and that the ratio of bulk to tube rates falls within the paper's reported factor windows (18±9 for (10,10), 50±25 for (7,7))."
    },
    {
      "file": "step_03_activation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "activation_energy_kcal_per_mol",
          "Ea_error_kcal_per_mol"
        ],
        "units": {
          "activation_energy_kcal_per_mol": "kcal/mol",
          "Ea_error_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Activation energies from Arrhenius analysis. The checker verifies that the activation energies fall within the paper-reported error bars: 52–78 kcal/mol (bulk), 44–60 ((10,10)), 49–59 ((7,7))."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will evaluate the three scored output files independently. For the M_w versus time data, it will verify that M_w increases monotonically with time and, for the confined systems, that the growth saturates (plateaus). It will also check that at equivalent times the ordering is bulk > (10,10) > (7,7). For the rate constants, it will verify that the rate constants follow the same geometric ordering and that the ratios of the bulk rate to the tube rates fall within expected factor windows. For the activation energies, it will check that the values lie inside acceptable ranges consistent with the polymerization energetics. The final score is a weighted combination of these assessments. Your output must be computed from the simulation and analysis you perform; reporting numbers from the paper or a guess will not satisfy the checks.
