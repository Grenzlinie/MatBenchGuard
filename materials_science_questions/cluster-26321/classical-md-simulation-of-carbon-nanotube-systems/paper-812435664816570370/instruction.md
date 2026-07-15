# MD-Based Transition-State Ensemble Characterization for Water in Carbon Nanotubes

## Problem background
Understanding how water enters and exits the narrow interior of carbon nanotubes is critical for designing nanoscale fluidic devices and for interpreting the behavior of hydrophobic channels in biological systems. When water fills a sufficiently narrow nanotube, it forms a single-file, hydrogen-bonded chain whose fluctuations can lead to spontaneous filling and emptying. Characterizing the transition state that separates the empty and filled states—its location, structure, and the probability that a configuration at the top of the barrier commits to filling versus emptying—remains an open challenge. This task addresses that challenge by reproducing the molecular dynamics characterization of the filling/emptying transition state ensemble for a (6,6) carbon nanotube solvated in water.

## Approach
The approach uses classical molecular dynamics (MD) simulations of a carbon nanotube solvated in TIP3P water. Two nanotube lengths are studied: a short tube (~13.5 Å) and a long tube (~27 Å). The carbon–water interactions are tuned via Lennard-Jones parameters to control the equilibrium between empty and filled states. From equilibrium trajectories, the free energy profile along the number of contiguous water molecules inside the tube is computed using occupancy probabilities. A candidate transition state ensemble is defined by a combination of occupancy (all but one water molecule inside) and the axial position of the outermost water molecule. This ensemble is validated by committor tests: for each candidate configuration, many independent simulations are launched with randomized velocities, and the fraction that reach the filled state first is recorded. The kinetics are further probed through nonequilibrium simulations in which the carbon–water potential is switched between two parameter sets, and the lifetimes of filled and empty states are extracted. Finally, the dependence of the free energy profile on the strength of the attractive interactions is examined by running simulations at several scaling factors λ of the Lennard-Jones well depth and extracting the slope of the free energy as a function of occupancy.

## Reproduction target
Using GROMACS (or an equivalent open-source MD engine) and standard analysis tools, you will produce four scored output files:

1. **Free energy profile** (`step_01_free_energy.csv`): the free energy G_N/kT for occupancy states N = 0..5 of the short tube with modified carbon–water parameters, computed from an equilibrium MD trajectory.
2. **Commitment probability results** (`step_02_commitment.csv`): for each of 10 transition-state configurations, the fraction of 50 committor trials that reach the filled state first. The overall mean and variance of these fractions characterize the transition state ensemble.
3. **Lifetime analysis** (`step_03_lifetimes.csv`): mean lifetimes, standard deviations, and numbers of events for the filled and empty states of both short and long nanotubes, obtained from nonequilibrium switching simulations.
4. **Free energy slope vs λ** (`step_04_lambda_dependence.csv`): the slope and intercept of the free energy profile G_N/N as a function of the interaction scaling parameter λ for the long tube, derived from equilibrium simulations at three λ values.

## Assets

- GROMACS (open-source MD engine): https://www.gromacs.org
- Python scientific stack (numpy, scipy, pandas, matplotlib): pip
- MDAnalysis or MDTraj: MDAnalysis

## Workflow steps

### Step 1: Build the short (13.5 Å) carbon nanotube system
- Role: process
- Action: Construct a (6,6) armchair carbon nanotube of length ~13.5 Å, solvate in a box of ~1000 TIP3P water molecules, and assign the modified carbon–water Lennard-Jones parameters (εCO = 0.06461 kcal/mol, σCO = 3.4138 Å). Create GROMACS compatible topology and coordinate files.
- Evidence: `/app/outputs/short_tube.gro, short_tube.top`

### Step 2: Run equilibrium MD for the short tube
- Role: process
- Action: Perform NPT molecular dynamics at 300 K and 1 bar for the short tube with modified carbon–water interactions, producing a trajectory of at least 42 ns (or sufficient to observe >10 filling/emptying events). Use particle-mesh Ewald for electrostatics.
- Evidence: `/app/outputs/short_eq.xtc, ener.edr`

### Step 3: Free energy profile along occupancy N (short tube)
- Role: scored (load-bearing)
- Action: From the short tube equilibrium trajectory, partition tube occupancy into contiguous-chain states for N=0–5. Compute probabilities p_N and derive G_N/k_BT = –ln p_N. Write the free energy profile as a CSV.
- Output file: `/app/outputs/step_01_free_energy.csv`
- Format: csv
- Contract: columns: N (int), free_energy_kT (float), uncertainty_kT (float)
- Scoring: scored by hidden verifier

### Step 4: Run committor test simulations
- Role: process
- Action: Randomly select 10 configurations from the equilibrium trajectory that satisfy the transition-state criterion (N=4 contiguous water molecules, outermost water z ≥ 6 Å from tube center). For each, generate 50 independent initial conditions by sampling Maxwell–Boltzmann velocities at 300 K and propagate until the tube fills or empties completely. Record outcomes.
- Evidence: `/app/outputs/commit_trials.log`

### Step 5: Commitment probability results
- Role: scored (load-bearing)
- Action: Aggregate the committor-test outcomes: for each configuration compute fraction p_fill of the 50 trials that reached the filled state first. Write the per-configuration fractions as a CSV.
- Output file: `/app/outputs/step_02_commitment.csv`
- Format: csv
- Contract: columns: config_id (int), p_fill (float)
- Scoring: scored by hidden verifier

### Step 6: Build the long (27 Å) carbon nanotube system
- Role: process
- Action: Construct a (6,6) armchair carbon nanotube of length ~27 Å, solvate in ~4145 TIP3P water molecules. Prepare topology files with both unmodified and modified carbon–water Lennard-Jones parameters.
- Evidence: `/app/outputs/long_tube.gro, long_tube.top`

### Step 7: Run equilibrium MD for the long tube at different λ
- Role: process
- Action: Perform equilibrium NPT simulations for the long tube with carbon–water interactions scaled by λ = 0.75 (11 ns), λ = 0.785 (13 ns), and λ = 1.0 (4 ns). Save occupancy trajectories.
- Evidence: `/app/outputs/long_lambda0.75.xtc, long_lambda0.785.xtc, long_lambda1.0.xtc`

### Step 8: Free energy slope vs λ (long tube)
- Role: scored (load-bearing)
- Action: From the occupancy trajectories, compute probabilities P_N for N = 1–8 at each λ. Fit G_N/k_BT = –ln P_N to a line and extract the slope and intercept. Write the fitted slope and intercept for each λ as a CSV.
- Output file: `/app/outputs/step_04_lambda_dependence.csv`
- Format: csv
- Contract: columns: lambda (float), slope (float), intercept (float)
- Scoring: scored by hidden verifier

### Step 9: Nonequilibrium MD for lifetime measurements
- Role: process
- Action: Perform nonequilibrium NPT simulations for both the short and long tubes: switch the carbon–water potential between unmodified (filled-favoring) and modified (empty-favoring) parameters as described in the paper. Record the times until the last filled/empty configuration before a transition (lifetimes).
- Evidence: `/app/outputs/lifetimes_short.log, lifetimes_long.log`

### Step 10: Lifetime analysis
- Role: scored (load-bearing)
- Action: From the nonequilibrium trajectories, compute the mean lifetimes, standard deviation, and number of transitions for the filled state (modified parameters) and empty state (unmodified parameters) for both tube lengths. Output the summary as a CSV.
- Output file: `/app/outputs/step_03_lifetimes.csv`
- Format: csv
- Contract: columns: tube_type (str, 'short' or 'long'), state (str, 'filled' or 'empty'), mean_lifetime_ps (float), std_ps (float), n_events (int)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_free_energy.csv`
- `/app/outputs/step_02_commitment.csv`
- `/app/outputs/step_03_lifetimes.csv`
- `/app/outputs/step_04_lambda_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_free_energy.csv
- path: `/app/outputs/step_01_free_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Free energy G_N/kT (and uncertainty) for states with N contiguous water molecules inside the short tube (N=0..5).
- schema:
  - `type`: table
  - `required_columns`: `N`, `free_energy_kT`, `uncertainty_kT`
  - `column_types`:
    - `N`: int
    - `free_energy_kT`: float
    - `uncertainty_kT`: float

### step_02_commitment.csv
- path: `/app/outputs/step_02_commitment.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Commitment probability (fraction of 50 trials that reach the filled state first) for each of the 10 tested transition-state configurations.
- schema:
  - `type`: table
  - `required_columns`: `config_id`, `p_fill`
  - `column_types`:
    - `config_id`: int
    - `p_fill`: float

### step_03_lifetimes.csv
- path: `/app/outputs/step_03_lifetimes.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mean lifetimes (in ps), standard deviation, and number of transitions for filled and empty states of short and long tubes.
- schema:
  - `type`: table
  - `required_columns`: `tube_type`, `state`, `mean_lifetime_ps`, `std_ps`, `n_events`
  - `column_types`:
    - `tube_type`: str
    - `state`: str
    - `mean_lifetime_ps`: float
    - `std_ps`: float
    - `n_events`: int

### step_04_lambda_dependence.csv
- path: `/app/outputs/step_04_lambda_dependence.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Slope and intercept of the free energy profile G_N/N for the long tube as a function of the interaction scaling parameter λ.
- schema:
  - `type`: table
  - `required_columns`: `lambda`, `slope`, `intercept`
  - `column_types`:
    - `lambda`: float
    - `slope`: float
    - `intercept`: float

Notes: All outputs are derived from MD simulations that must be run by the agent. The checker reads these CSVs, recomputes aggregates where needed, and compares them against hidden reference values (paper-reported numbers) with appropriate tolerances. No gold values are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_free_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "free_energy_kT",
          "uncertainty_kT"
        ],
        "column_types": {
          "N": "int",
          "free_energy_kT": "float",
          "uncertainty_kT": "float"
        }
      },
      "description": "Free energy G_N/kT (and uncertainty) for states with N contiguous water molecules inside the short tube (N=0..5)."
    },
    {
      "file": "step_02_commitment.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "config_id",
          "p_fill"
        ],
        "column_types": {
          "config_id": "int",
          "p_fill": "float"
        }
      },
      "description": "Commitment probability (fraction of 50 trials that reach the filled state first) for each of the 10 tested transition-state configurations."
    },
    {
      "file": "step_03_lifetimes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "tube_type",
          "state",
          "mean_lifetime_ps",
          "std_ps",
          "n_events"
        ],
        "column_types": {
          "tube_type": "str",
          "state": "str",
          "mean_lifetime_ps": "float",
          "std_ps": "float",
          "n_events": "int"
        }
      },
      "description": "Mean lifetimes (in ps), standard deviation, and number of transitions for filled and empty states of short and long tubes."
    },
    {
      "file": "step_04_lambda_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda",
          "slope",
          "intercept"
        ],
        "column_types": {
          "lambda": "float",
          "slope": "float",
          "intercept": "float"
        }
      },
      "description": "Slope and intercept of the free energy profile G_N/N for the long tube as a function of the interaction scaling parameter λ."
    }
  ],
  "notes": "All outputs are derived from MD simulations that must be run by the agent. The checker reads these CSVs, recomputes aggregates where needed, and compares them against hidden reference values (paper-reported numbers) with appropriate tolerances. No gold values are disclosed here."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently examines each of the four scored CSV files. The verifier reads your artifacts, recomputes aggregate statistics where appropriate (e.g., mean and variance of the commitment probabilities), and compares them against predefined reference values using appropriate tolerances. Each stage contributes a weight toward the final reward (total = 1.0). A high score requires that the numerical results in your CSVs are consistent with the physics encoded in the simulation protocol and analysis procedure described above. Simply reporting plausible numbers is not sufficient; the verifier checks that your outputs arise from a correct execution of the workflow.
