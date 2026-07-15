# MD Simulation of Functionalized Carbon Nanotube Pull-Out and Interfacial Friction Characterization

## Problem background
Carbon nanotube (CNT) reinforced polymer composites rely on interfacial load transfer. Chemical functionalization can enhance interfacial adhesion compared to non-bonded composites. Molecular dynamics (MD) simulations can study the pull-out behavior of a functionalized CNT from a polymer matrix, characterizing nanoscale friction features such as the critical pull-out force and effective interfacial viscosity. This task investigates the interfacial sliding of a (10,10) CNT chemically bonded to crystalline polyethylene under incremental axial loading.

## Approach
The simulation setup uses a (10,10) carbon nanotube embedded in a crystalline polyethylene matrix, with three covalent attachments linking one polymer chain to the nanotube. Interatomic interactions are described by a reactive hydrocarbon potential (AIREBO/Brenner) for covalent bonds and a Lennard-Jones potential for non-bonded interactions. During the MD simulation at 300 K, an axial force is applied to all nanotube atoms and incremented over time, causing the nanotube to slide relative to the matrix. The nanotube center-of-mass velocity and the total applied force are monitored. From the recorded force-velocity relationship, a linear fit is performed to extract the critical pull-out force (f0) and the effective viscosity coefficient (χeff). The effective interfacial viscosity μeff is then derived using the interfacial area and the van der Waals gap. In addition, the velocity profile is examined for discrete peaks that occur after the force-induced breakage of a covalent linkage, marking transient acceleration events.

## Reproduction target
Reproduce the MD pull-out simulation for the functionalized CNT-polymer system, extract the force-velocity data series, fit the interfacial friction model to obtain the critical pull-out force f0 and effective viscosity coefficient χeff, and compute the effective interfacial viscosity μeff. Also identify the velocity peaks that appear in the nanotube's motion after the breakage of one of the covalent attachments (around step 141,000). All results must be produced from the MD simulation and post-processing; the verifier will independently recompute and check these quantities.

## Assets

- LAMMPS molecular dynamics package: https://lammps.sandia.gov
- Python with numpy, scipy: numpy, scipy
- Brenner/AIREBO potential parameters for hydrocarbons
- Lennard-Jones parameters for polyethylene

## Workflow steps

### Step 1: Construct functionalized NT-polymer system
- Role: process
- Action: Generate the initial atomic configuration and LAMMPS input for a (10,10) carbon nanotube embedded in crystalline polyethylene with three covalent attachments (links) to one polymer chain, using the AIREBO potential for covalent bonds and Lennard-Jones for non-bonded interactions.
- Evidence: `/app/outputs/system.data`

### Step 2: Run MD pull-out simulation
- Role: process
- Action: Run LAMMPS molecular dynamics at 300 K with a timestep of 0.05 fs. Apply an incremental axial force to all nanotube atoms over 210,000 steps. The force schedule is as follows: the total axial force on the nanotube (in nN) is given by F(t) = r * t for t ≤ 105,000 steps, and F(t) = r * 105,000 + 2.5r * (t - 105,000) for t > 105,000, where r = 3 nN / (105,000 + 2.5 * 105,000) ≈ 8.16 × 10^{-6} nN/step, so that the total force reaches approximately 3 nN at step 210,000. Distribute this total force equally among all nanotube atoms. Output the nanotube center-of-mass velocity and displacement.
- Evidence: `/app/outputs/pullout.log`

### Step 3: Extract force-velocity data
- Role: scored (load-bearing)
- Action: Parse the simulation log to extract the applied force on the nanotube and the nanotube center-of-mass axial velocity for every recorded timestep after sliding onset. Save as a CSV with columns: step, force_nN, velocity_A_per_ps.
- Output file: `/app/outputs/force_velocity_data.csv`
- Format: csv
- Contract: step:int, force_nN:float, velocity_A_per_ps:float
- Scoring: scored by hidden verifier

### Step 4: Fit interfacial friction model
- Role: scored
- Action: Perform a linear regression of velocity (Å/ps) versus force (nN) on the data points where sliding has occurred. Extract the intercept f0 (critical pull-out force) and the slope 1/χeff, then compute the effective viscosity coefficient χeff. Compute the effective interfacial viscosity μeff in centipoise (cP) using the formula: μeff = χeff * (h_vdW / A_i) * 100, where χeff is in nN·ps/Å, h_vdW = 3.4 Å is the van der Waals separation, and A_i = 2900 Å^2 is the interfacial area. Output a JSON file with f0_nN, chi_eff_nN_ps_per_A, mu_eff_cP, and R_squared.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: {"f0_nN": number, "chi_eff_nN_ps_per_A": number, "mu_eff_cP": number, "R_squared": number}
- Scoring: scored by hidden verifier

### Step 5: Identify velocity peaks after linkage breakage
- Role: scored
- Action: From the velocity profile (force_velocity_data.csv or simulation log), locate all local maxima in the nanotube velocity after step 141,000. Save each peak as an object with step and velocity_A_per_ps in a JSON array.
- Output file: `/app/outputs/velocity_peaks.json`
- Format: json
- Contract: [{"step": int, "velocity_A_per_ps": float}, ...]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/force_velocity_data.csv`
- `/app/outputs/fitted_parameters.json`
- `/app/outputs/velocity_peaks.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### force_velocity_data.csv
- path: `/app/outputs/force_velocity_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of applied force and NT axial velocity, from which the checker recomputes f0 and χeff.
- schema:
  - `type`: table
  - `required_columns`: `step`, `force_nN`, `velocity_A_per_ps`
  - `units`:
    - `force_nN`: nN
    - `velocity_A_per_ps`: Å/ps

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-reported fitted parameters; the checker compares these to hidden reference values.
- schema:
  - `type`: object
  - `required`:
    - `f0_nN`: number
    - `chi_eff_nN_ps_per_A`: number
    - `mu_eff_cP`: number
    - `R_squared`: number
  - `units`:
    - `f0_nN`: nN
    - `chi_eff_nN_ps_per_A`: nN·ps/Å
    - `mu_eff_cP`: cP

### velocity_peaks.json
- path: `/app/outputs/velocity_peaks.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Velocity peaks detected after step 141,000, verifying the discrete acceleration events reported in the paper.
- schema:
  - `type`: array
  - `items`:
    - `step`: integer
    - `velocity_A_per_ps`: number

Notes: All output files must be placed in /app/outputs. The checker will recompute f0 and χeff from force_velocity_data.csv and compare against paper values within tolerances. The velocity peaks will be checked for correct timing and minimum magnitude.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "force_velocity_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "step",
          "force_nN",
          "velocity_A_per_ps"
        ],
        "units": {
          "force_nN": "nN",
          "velocity_A_per_ps": "Å/ps"
        }
      },
      "description": "Time series of applied force and NT axial velocity, from which the checker recomputes f0 and χeff."
    },
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "f0_nN": "number",
          "chi_eff_nN_ps_per_A": "number",
          "mu_eff_cP": "number",
          "R_squared": "number"
        },
        "units": {
          "f0_nN": "nN",
          "chi_eff_nN_ps_per_A": "nN·ps/Å",
          "mu_eff_cP": "cP"
        }
      },
      "description": "Agent-reported fitted parameters; the checker compares these to hidden reference values."
    },
    {
      "file": "velocity_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "step": "integer",
          "velocity_A_per_ps": "number"
        }
      },
      "description": "Velocity peaks detected after step 141,000, verifying the discrete acceleration events reported in the paper."
    }
  ],
  "notes": "All output files must be placed in /app/outputs. The checker will recompute f0 and χeff from force_velocity_data.csv and compare against paper values within tolerances. The velocity peaks will be checked for correct timing and minimum magnitude."
}
```

## How you are scored
A hidden verifier will read your output artifacts and independently score each workflow stage. The raw force-velocity data will be used to recompute the derived friction parameters. The fitted parameters you report will be compared against the expected force-velocity relationship. The velocity peaks will be audited for correct timing and characteristics. The final reward is a weighted combination of these stage scores. Reporting a number without the underlying simulation traces is not sufficient; the verifier reconstructs the key quantities from your raw data.
