# High-pressure LOX droplet vaporization: transcritical minimum and lifetime scaling

## Problem background
This task investigates the vaporization of a single liquid-oxygen (LOX) droplet immersed in a quiescent high-temperature, high-pressure hydrogen gas. At high chamber pressures the droplet surface may reach the mixture critical conditions, causing the liquid–vapour interface to disappear and the vaporization regime to switch from subcritical to supercritical. The problem is to compute how the droplet lifetime (the time required for 97% mass loss) varies with ambient pressure and temperature, and to determine the pressure–temperature boundary that separates subcritical from supercritical vaporization.

## Approach
The transient vaporization is modelled by solving spherical conservation equations for mass, species (O₂/H₂), and energy with a moving droplet surface. Thermodynamic non-idealities are captured using the Redlich–Kwong–Soave cubic equation of state for the binary mixture; liquid–vapour equilibrium at the interface is enforced by equating species fugacities. Transport properties (thermal conductivity, binary diffusivity) are estimated from standard correlations (Wilke–Chang for the liquid, Wilke–Lee for the gas, together with appropriate mixing rules) applied to pure-component data available in the NIST Chemistry WebBook. For a given ambient pressure and temperature, the solver will run until the droplet loses 97% of its initial mass. The resulting trajectory data (radius, surface temperature, surface mass fraction vs. time) are post-processed to extract the droplet lifetime and to detect when the surface temperature reaches the mixture critical temperature exactly at the end of the lifetime.

## Reproduction target
Implement and execute the numerical solver for a grid of ambient pressures (covering approximately 1–40 MPa) and five ambient temperatures: 500 K, 1000 K, 1500 K, 2000 K, and 2500 K. The initial LOX droplet has a radius of 500 µm and an initial temperature of 100 K. From the simulation results, produce two CSV files:

- `/app/outputs/lifetime_curves.csv` : columns `temperature_K` (float), `pressure_MPa` (float), `lifetime_s` (float). One row for each simulated (P,T) point.
- `/app/outputs/critical_boundary.csv` : columns `temperature_K` (float), `pressure_MPa` (float). One row per temperature, giving the highest pressure for which the droplet surface reaches the mixture critical temperature exactly at the end of the 97% mass-loss lifetime.

The hidden verifier will score these outputs against a reference. It will check structural properties of the lifetime curves and the shape of the transcritical boundary; it does NOT require exact numerical agreement with a specific published table.

## Assets

- SciPy: pip install scipy
- NumPy: pip install numpy
- NIST Chemistry WebBook: https://webbook.nist.gov/

## Workflow steps

### Step 1: Run droplet vaporization simulations
- Role: process
- Action: Implement and run a numerical solver for single spherical LOX droplet vaporization in a quiescent H2 environment using the Redlich-Kwong-Soave equation of state and standard transport correlations. For each combination of ambient pressure (1–40 MPa) and temperature (500, 1000, 1500, 2000, 2500 K), simulate an LOX droplet (initial radius 500 µm, T₀=100 K) until 97% mass loss. Save trajectory data (radius‑vs‑time, surface‑temperature‑vs‑time, surface‑mass‑fraction‑vs‑time) for every case in /app/outputs/trajectories/ and write a completion marker /app/outputs/simulations_completed.txt.
- Evidence: `/app/outputs/simulations_completed.txt`

### Step 2: Compute droplet lifetime curves
- Role: scored (load-bearing)
- Action: Process the trajectory files in /app/outputs/trajectories/. For each (P, T) case, locate the time at which the remaining liquid mass falls to 3% of the initial mass (97% mass loss). Write the compiled results to /app/outputs/lifetime_curves.csv.
- Output file: `/app/outputs/lifetime_curves.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (float), pressure_MPa (float), lifetime_s (float). One row per simulated (P,T) point.
- Scoring: scored by hidden verifier

### Step 3: Identify transcritical boundary
- Role: scored
- Action: For each ambient temperature, use the trajectory files and the mixture critical line to find the highest pressure for which the droplet surface temperature reaches the mixture critical temperature exactly at the end of the 97% mass‑loss lifetime. Write the (T∞, P) pairs to /app/outputs/critical_boundary.csv.
- Output file: `/app/outputs/critical_boundary.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (float), pressure_MPa (float). One row per temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lifetime_curves.csv`
- `/app/outputs/critical_boundary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lifetime_curves.csv
- path: `/app/outputs/lifetime_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Droplet lifetime curves for various ambient temperatures; verifier checks existence of a transcritical minimum, high‑pressure plateau (RSD < 0.15), and T^{-3/4} scaling (exponent in [-0.9, -0.6]).
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `pressure_MPa`, `lifetime_s`
  - `units`:
    - `temperature_K`: K
    - `pressure_MPa`: MPa
    - `lifetime_s`: s

### critical_boundary.csv
- path: `/app/outputs/critical_boundary.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Transcritical boundary points where droplet surface reaches critical state at end of lifetime; verifier checks monotonic decrease and pressure range within 3‑20 MPa.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `pressure_MPa`
  - `units`:
    - `temperature_K`: K
    - `pressure_MPa`: MPa

Notes: All scored outputs are derived from the same underlying simulation runs. The verifier performs structural audits on the CSV files rather than comparing against digitized reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lifetime_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "pressure_MPa",
          "lifetime_s"
        ],
        "units": {
          "temperature_K": "K",
          "pressure_MPa": "MPa",
          "lifetime_s": "s"
        }
      },
      "description": "Droplet lifetime curves for various ambient temperatures; verifier checks existence of a transcritical minimum, high‑pressure plateau (RSD < 0.15), and T^{-3/4} scaling (exponent in [-0.9, -0.6])."
    },
    {
      "file": "critical_boundary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "pressure_MPa"
        ],
        "units": {
          "temperature_K": "K",
          "pressure_MPa": "MPa"
        }
      },
      "description": "Transcritical boundary points where droplet surface reaches critical state at end of lifetime; verifier checks monotonic decrease and pressure range within 3‑20 MPa."
    }
  ],
  "notes": "All scored outputs are derived from the same underlying simulation runs. The verifier performs structural audits on the CSV files rather than comparing against digitized reference values."
}
```

## How you are scored
A hidden scoring program independently evaluates each workflow step’s artifact. For scored steps, it recomputes the required metric or audits the structural properties (e.g., trends, monotonicity) against a hidden reference. The final reward is a weighted combination of the step scores. Simply reporting a plausible number without genuinely executing the simulations and analysis will not pass the verifier’s checks.
