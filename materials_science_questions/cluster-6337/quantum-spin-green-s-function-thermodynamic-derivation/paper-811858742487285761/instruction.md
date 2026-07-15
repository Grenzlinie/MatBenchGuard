# Monte Carlo Simulation of Spin-1 Blume-Capel Model on Square Lattice

## Problem background
This task studies the ferromagnetic spin-1 Blume–Capel model on a square lattice (coordination number 4). The Hamiltonian includes nearest-neighbor exchange interactions, a single-ion crystal field, and a longitudinal magnetic field. The model exhibits a variety of multicritical phenomena, such as a phase diagram with a second-order phase transition line that changes to first order at a tricritical point. The goal is to compute the thermodynamic properties numerically and to map out the phase diagram and locate the tricritical point, all in natural units (J=1, kB=1). Understanding these properties sheds light on critical phenomena in magnetic systems.

## Approach
The central computational method is Monte Carlo simulation with single-spin-flip Metropolis updates. A spin-1 Blume–Capel Hamiltonian on a 64×64 square lattice with periodic boundary conditions is simulated at zero magnetic field (h/J=0). For each temperature and crystal field value, the simulation is performed with sufficient equilibration and production Monte Carlo steps to obtain converged statistical averages. The following observables are computed as functions of temperature: magnetization per spin, magnetic susceptibility from magnetization fluctuations, internal energy from the Hamiltonian average, specific heat via numerical derivative of the internal energy, and the fourth-order Binder cumulant. The transition temperature is located from the peak of the susceptibility or from the crossing of Binder cumulant curves for different lattice sizes. Repeating the procedure for a range of crystal field values D/J yields the phase diagram (critical temperature versus crystal field). From this diagram, the tricritical point where the transition changes from continuous to first-order is extracted.

## Reproduction target
Reproduce the Monte Carlo results for the spin-1 Blume–Capel model on a square lattice at zero magnetic field by: (i) computing the temperature-dependent magnetization, susceptibility, specific heat, and Binder cumulant for D/J=0, h/J=0 and locating the transition temperature; (ii) mapping the phase diagram of critical temperature versus crystal field D/J over the range where ferromagnetic order exists; (iii) determining the tricritical point coordinates from this phase diagram. The results must be written to the specified output files in the formats described in the workflow steps.

## Assets

- Python: https://www.python.org/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Run MC simulation and compute observables for D/J=0
- Role: scored (load-bearing)
- Action: Implement a standard single-spin-flip Metropolis Monte Carlo simulation for the spin-1 Blume–Capel model on a 64×64 square lattice with periodic boundary conditions. For crystal field D/J=0 and magnetic field h/J=0, run the simulation with sufficient equilibration and production steps to obtain converged statistical averages. Compute magnetization per spin from the spin configuration, magnetic susceptibility from magnetization fluctuations, internal energy from the Hamiltonian average, specific heat via numerical derivative of the internal energy, and the fourth-order Binder cumulant as functions of temperature. Write the resulting observables to the output file.
- Output file: `/app/outputs/mc_observables.csv`
- Format: csv
- Contract: Columns: T (temperature), D_J (crystal field / J), h_J (magnetic field / J), magnetization, susceptibility, specific_heat, binder_cumulant.
- Scoring: scored by hidden verifier

### Step 2: Compute phase diagram Tc vs D/J
- Role: scored
- Action: For a range of crystal field values D/J (e.g., from -2 to 0), run the MC simulation for each value and determine the transition temperature Tc from the temperature of the susceptibility peak or the Binder cumulant crossing. Record each (D_J, Tc_J) pair. Save the phase diagram to the output file.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Columns: D_J (crystal field / J), Tc_J (critical temperature / J).
- Scoring: scored by hidden verifier

### Step 3: Extract tricritical point
- Role: scored
- Action: From the obtained phase diagram, identify the tricritical point where the transition changes from continuous to first-order. Write the coordinates D_t/J and T_t/J to a JSON file.
- Output file: `/app/outputs/tricritical_point.json`
- Format: json
- Contract: {"D_t_J": float, "T_t_J": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mc_observables.csv`
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/tricritical_point.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mc_observables.csv
- path: `/app/outputs/mc_observables.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Temperature-dependent observables (magnetization, susceptibility, specific heat, Binder cumulant) for the Blume-Capel model at D/J=0, h/J=0. The checker will verify that the curves are physically plausible and that the transition temperature extracted from them meets the paper's value within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T`, `D_J`, `h_J`, `magnetization`, `susceptibility`, `specific_heat`, `binder_cumulant`
  - `description`: All quantities are in natural units (J=1, kB=1).

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Critical temperature Tc/J as a function of crystal field D/J for h/J=0. The checker will compare selected Tc values against reference data within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `D_J`, `Tc_J`

### tricritical_point.json
- path: `/app/outputs/tricritical_point.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The tricritical point coordinates extracted from the phase diagram. The checker will compare these values to the paper's reported values within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `D_t_J`: number
    - `T_t_J`: number

Notes: All outputs are produced by Monte Carlo simulation only; the introduced effective-field approximation (IEFT) is not part of the reproduction task. The checker uses hidden gold values from the paper's MC results and applies threshold_or_better scoring: meeting or exceeding the reference earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mc_observables.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "D_J",
          "h_J",
          "magnetization",
          "susceptibility",
          "specific_heat",
          "binder_cumulant"
        ],
        "description": "All quantities are in natural units (J=1, kB=1)."
      },
      "description": "Temperature-dependent observables (magnetization, susceptibility, specific heat, Binder cumulant) for the Blume-Capel model at D/J=0, h/J=0. The checker will verify that the curves are physically plausible and that the transition temperature extracted from them meets the paper's value within a tolerance."
    },
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "D_J",
          "Tc_J"
        ]
      },
      "description": "Critical temperature Tc/J as a function of crystal field D/J for h/J=0. The checker will compare selected Tc values against reference data within a tolerance."
    },
    {
      "file": "tricritical_point.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "D_t_J": "number",
          "T_t_J": "number"
        }
      },
      "description": "The tricritical point coordinates extracted from the phase diagram. The checker will compare these values to the paper's reported values within a tolerance."
    }
  ],
  "notes": "All outputs are produced by Monte Carlo simulation only; the introduced effective-field approximation (IEFT) is not part of the reproduction task. The checker uses hidden gold values from the paper's MC results and applies threshold_or_better scoring: meeting or exceeding the reference earns full credit."
}
```

## How you are scored
A hidden verifier independently scores each scored output file. The checker reads the provided CSV and JSON artifacts and compares the extracted quantities (magnetization curve features, transition temperature, phase diagram points, tricritical coordinates) against reference values with appropriate tolerances. Scoring is directional: meeting or exceeding the reference (e.g., a more accurate location of the transition) earns full credit; results that deviate beyond tolerance lose credit gradually. Simply reporting numbers without running the full Monte Carlo pipeline will not satisfy the verification. Each scored artifact is weighted, and the final reward is a weighted combination in [0,1].
