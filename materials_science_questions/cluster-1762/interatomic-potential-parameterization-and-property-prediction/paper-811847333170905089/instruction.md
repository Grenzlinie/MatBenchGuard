# Thermal conductivity of ZnTe from equilibrium molecular dynamics

## Problem background
ZnTe is an II-VI semiconductor with applications in electronics and thermoelectrics. Understanding its lattice thermal conductivity κ(T) as a function of temperature is crucial for device design and material selection. This task aims to compute κ(T) using equilibrium molecular dynamics and to determine the structural parameters characterising the phonon heat-current relaxation.

## Approach
The computational approach uses classical equilibrium molecular dynamics (EMD) with the Green–Kubo fluctuation–dissipation theorem to obtain the lattice thermal conductivity. The atomic interactions in zinc-blende ZnTe are described by a Tersoff empirical potential. First, static lattice dynamics using GULP provide the equilibrium lattice constant and phonon density of states (PDOS). The PDOS is then used to derive a quantum temperature correction that maps the simulated classical temperature to the real temperature, ensuring the correct treatment of quantum effects. Subsequent MD simulations are run with LAMMPS in isothermal–isobaric (NPT) ensemble for equilibration, followed by microcanonical (NVE) production to collect heat current data. From the heat current autocorrelation function (HCACF) a normalised correlation function g(t) is computed. Thermal conductivity is obtained by fitting g(t) to a double-exponential decay model and integrating analytically, with the final value corrected for quantum temperature effects. The task also reports the double-exponential fit parameters for one representative temperature.

## Reproduction target
Compute the lattice thermal conductivity κ of zinc-blende ZnTe at the following real temperatures: 300 K, 400 K, 500 K, 600 K, 700 K, and 800 K. The conductivities must be reported in a CSV file with columns T_K (integer temperature in Kelvin) and kappa_W_mK (thermal conductivity in W/m/K). Additionally, for the 400 K simulation, provide the double-exponential fit parameters obtained from the normalised HCACF: A1, tau1_ps, A2, tau2_ps, and the temperature-corrected prefactor K0 (in W/m/K). Output these parameters as a JSON file. All steps of the pipeline must be executed, including the static lattice dynamics and quantum temperature correction, to produce the final results.

## Assets

- GULP (General Utility Lattice Program): https://gulp.curtin.edu.au
- LAMMPS (Molecular Dynamics Simulator): https://lammps.sandia.gov
- Tersoff potential parameters for ZnTe (Kanoun et al. 2003): 10.1016/S1293-2558(03)00151-2

## Workflow steps

### Step 1: Static lattice dynamics
- Role: process
- Action: Use GULP with the Tersoff potential to compute the equilibrium lattice constant, elastic constants, and the phonon density of states D(ω) of zinc-blende ZnTe. Save D(ω) as phonon_dos.csv.
- Evidence: `/app/outputs/phonon_dos.csv`

### Step 2: Quantum temperature correction
- Role: process
- Action: From the phonon density of states D(ω), compute the classical MD temperature T_MD as a function of real temperature T using the temperature-dependent internal energy relation and the temperature gradient factor dT_MD/dT. Save the mapping table as temperature_scaling.csv with columns T_K, T_MD_K, dT_MD_dT.
- Evidence: `/app/outputs/temperature_scaling.csv`

### Step 3: EMD heat-current autocorrelation at 400 K
- Role: process
- Action: Run equilibrium MD simulations for ZnTe at 400 K using LAMMPS with a 5×5×5 supercell (1000 atoms), the Tersoff potential, and the equilibrium lattice constant. Equilibrate in the NPT ensemble, then run NVE production to collect heat-current data. Compute the normalized heat-current autocorrelation function g(t). Save g(t) as g_t_400K.csv with columns t_ps and g_t.
- Evidence: `/app/outputs/g_t_400K.csv`

### Step 4: Thermal conductivity calculation
- Role: scored (load-bearing)
- Action: For each temperature T = 300, 400, 500, 600, 700, 800 K, perform EMD simulations to obtain the normalized HCACF g(t), fit it to a double-exponential decay g(t)=A1·exp(−t/τ1)+A2·exp(−t/τ2), and compute the real thermal conductivity κ using the Green–Kubo formula with quantum temperature correction: κ = K(0)·(A1·τ1 + A2·τ2) where K(0)=G(0)·dT_MD/dT. Output κ(T) in thermal_conductivity.csv with columns T_K and kappa_W_mK.
- Output file: `/app/outputs/thermal_conductivity.csv`
- Format: csv
- Contract: columns: T_K (int, K), kappa_W_mK (float, W/m/K)
- Scoring: scored by hidden verifier

### Step 5: HCACF double-exponential fit parameters at 400 K
- Role: scored
- Action: For T=400 K, record the double-exponential fit parameters obtained from the normalized HCACF g(t) and the temperature-corrected prefactor K(0). Save them as fit_parameters_400K.json.
- Output file: `/app/outputs/fit_parameters_400K.json`
- Format: json
- Contract: JSON object with keys: A1 (float), tau1_ps (float, ps), A2 (float), tau2_ps (float, ps), K0 (float, W/m/K)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity.csv`
- `/app/outputs/fit_parameters_400K.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity.csv
- path: `/app/outputs/thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal conductivity of ZnTe at temperatures 300, 400, 500, 600, 700, 800 K. Values are compared against paper-extracted reference values with tolerance; monotonic decrease with T is also checked.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `kappa_W_mK`
  - `units`:
    - `T_K`: K
    - `kappa_W_mK`: W/m/K

### fit_parameters_400K.json
- path: `/app/outputs/fit_parameters_400K.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Double-exponential fit parameters for the normalized HCACF at 400 K. Checked for structural consistency (A1+A2 within [0.9,1.1], τ1 < τ2) and compared against a refit of the agent's raw g(t) curve.
- schema:
  - `type`: object
  - `required`:
    - `A1`: float
    - `tau1_ps`: float
    - `A2`: float
    - `tau2_ps`: float
    - `K0`: float

Notes: The agent must fetch GULP and LAMMPS, extract Tersoff parameters from the reference paper, and run the full static and MD pipeline. All scored outputs are compared against hidden gold values (thermal conductivity) or structural rules (fit parameters).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "kappa_W_mK"
        ],
        "units": {
          "T_K": "K",
          "kappa_W_mK": "W/m/K"
        }
      },
      "description": "Thermal conductivity of ZnTe at temperatures 300, 400, 500, 600, 700, 800 K. Values are compared against paper-extracted reference values with tolerance; monotonic decrease with T is also checked."
    },
    {
      "file": "fit_parameters_400K.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "A1": "float",
          "tau1_ps": "float",
          "A2": "float",
          "tau2_ps": "float",
          "K0": "float"
        }
      },
      "description": "Double-exponential fit parameters for the normalized HCACF at 400 K. Checked for structural consistency (A1+A2 within [0.9,1.1], τ1 < τ2) and compared against a refit of the agent's raw g(t) curve."
    }
  ],
  "notes": "The agent must fetch GULP and LAMMPS, extract Tersoff parameters from the reference paper, and run the full static and MD pipeline. All scored outputs are compared against hidden gold values (thermal conductivity) or structural rules (fit parameters)."
}
```

## How you are scored
A hidden verifier scores each output file independently, then combines the scores into a single final reward. The thermal conductivity values are compared to reference values derived from the original study, with appropriate tolerances to account for legitimate differences in molecular dynamics implementation. The verifier also checks that the reported κ decreases monotonically with temperature. For the fit parameters, the verifier performs structural checks (e.g., A1+A2 must be close to 1, τ1 < τ2) and may refit the agent's supplied raw g(t) curve to verify self-consistency. Merely copying numbers from a known source will not meet the requirements; the results must be produced by executing the full workflow described in the steps.
