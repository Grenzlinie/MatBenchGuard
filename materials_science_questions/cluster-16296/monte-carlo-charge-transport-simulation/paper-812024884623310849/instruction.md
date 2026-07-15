# Collisional Broadening in Monte Carlo Charge Transport Simulation

## Problem background
Semiclassical Monte Carlo (MC) simulation is a standard tool for studying high-field charge transport in semiconductors. In the traditional approach, electron scattering rates are computed using Fermi’s golden rule, and the electron energy E and momentum p satisfy the classical dispersion relation E = p²/(2m). Previous attempts to include collisional broadening (CB) in MC simulations led to non‑physical instabilities in the high‑energy tail of the electron distribution. A recent algorithm (CB‑MC) has been proposed that treats energy and momentum as independent state variables and introduces per‑event energy deviations derived from the uncertainty principle, avoiding the accumulation of broadening corrections. The task is to implement both the traditional MC and the CB‑MC algorithm and to characterize their behaviour under a range of applied electric fields by computing the average electron energy, the energy distribution, and the energy–momentum dispersion relation.

## Approach
A model semiconductor is used with a single spherical parabolic band (effective mass m* = 0.32) and monoenergetic phonons (ħω_ph = 450 K). The electrons start at a temperature of 300 K and are accelerated by uniform electric fields F = 2, 5, 10, 15, 20, 25, 30 kV/cm. The scattering is momentum‑randomizing (isotropic). Two Monte Carlo algorithms are compared.

**Traditional MC:** Free flight follows classical equations of motion with momentum update Δp = e F Δt. The scattering probability depends on the electron kinetic energy. After a non‑self‑scattering phonon event, the new momentum magnitude is determined from energy conservation E_f = E_i ± ħω_ph and the classical dispersion E = p²/(2m); the momentum direction is resampled isotropically.

**CB‑MC algorithm:** Electron energy E and momentum p are treated as independent state variables. During free flight, momentum is updated classically (Δp = e F Δt) and the kinetic‑energy bookkeeping before a scattering event is E = E_prev + (p² − p_prev²)/(2m). Position updates follow z(t) = z₀ + (p/m)Δt + ½ (eF/m) Δt². At each non‑self‑scattering phonon event, the nominal energy change is ± ħω_ph, and a stochastic deviation δE = (r − 0.5) σ is added, where σ = ħ/Δt and r is a uniform random number in (0, 1). The post‑scatter momentum magnitude is then assigned from the broadened energy, p = √[2m (E ± ħω_ph + δE)]. No memory of previous broadening is carried forward; the next inter‑event time determines the next σ. Self‑scattering events do not change energy or momentum.

Both algorithms use the same scattering‑probability model and physical parameters. The task is to run the simulations for all listed fields, discard initial transient, collect steady‑state trajectories, and produce the three output artifacts described below.

## Reproduction target
Compute the following three quantities from the simulated trajectories and write them to CSV files under `/app/outputs`:

1. **Average electron energy as a function of applied field.** For each field value 2, 5, 10, 15, 20, 25, 30 kV/cm, output the time‑averaged electron energy (in eV) obtained with the traditional MC simulation and with the CB‑MC simulation. Write one row per field to `average_energy.csv` with columns `field_kVcm`, `avg_energy_traditional`, `avg_energy_CBMC`.

2. **Energy distribution histogram at 10 kV/cm.** From the trajectories at F = 10 kV/cm, construct a histogram of electron energies using a bin width of approximately 0.005 eV covering the full energy range. Output the bin boundaries and the counts for both algorithms. Write to `energy_histogram_10kVcm.csv` with columns `energy_low`, `energy_high`, `count_traditional`, `count_CBMC`.

3. **Energy–momentum dispersion scatter at 10 kV/cm.** From the trajectories at F = 10 kV/cm, extract a sample of at least 5000 (|p|, E) pairs for each algorithm. Write the momentum magnitude (in a consistent unit such as atomic units) and the energy (in eV) along with a label indicating the algorithm. Write to `dispersion_scatter_10kVcm.csv` with columns `momentum`, `energy`, `algorithm`.

All files must follow the column schemas exactly. The simulations are stochastic; ensure you collect enough statistics (at least 10⁶ scattering events per field) so that the results are converged.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Traditional Monte Carlo Simulation
- Role: process
- Action: Run a traditional semiclassical Monte Carlo simulation for a model semiconductor (single spherical parabolic band, effective mass m*=0.32, monoenergetic phonons at ℏω=450 K, initial temperature 300 K, momentum-randomizing scattering) under uniform electric fields F = 2,5,10,15,20,25,30 kV/cm. Use scattering probabilities evaluated at the electron kinetic energy and the classical dispersion relation E=p²/(2m). Record raw electron energies and momenta for each field to construct steady-state distributions, discarding the initial transient.
- Evidence: none

### Step 2: CB‑MC Simulation with Collisional Broadening
- Role: process
- Action: Run the CB‑MC simulation described in the paper: treat electron energy E and momentum p as independent state variables, update momentum during free flight by Δp = eFΔt, position by z(t) = z₀ + (p/m)Δt + ½(eF/m)Δt², and kinetic-energy bookkeeping before scattering by E = E_prev + (p² - p_prev²)/(2m). At each non‑self‑scattering phonon event, set nominal energy E = E ± ℏω_ph, sample a per‑event energy deviation δE = (r-0.5)σ with σ = ℏ/Δt and r∈(0,1), then assign post‑scatter momentum magnitude p = √[2m(E ± ℏω_ph + δE)]. Recompute σ from the current inter‑event time. Use the same model parameters, fields, and scattering probability model as step_01. Record raw energies and momenta for post‑processing.
- Evidence: none

### Step 3: Average Energy vs Field
- Role: scored (load-bearing)
- Action: From the steady‑state trajectories of both simulations (step_01 and step_02), compute the time‑averaged electron energy for each electric field value. Write the results to average_energy.csv with one row per field.
- Output file: `/app/outputs/average_energy.csv`
- Format: csv
- Contract: columns: field_kVcm (float, kV/cm), avg_energy_traditional (float, eV), avg_energy_CBMC (float, eV); rows for fields 2,5,10,15,20,25,30 kV/cm in increasing order.
- Scoring: scored by hidden verifier

### Step 4: Energy Histogram at 10 kV/cm
- Role: scored
- Action: From the trajectories at F=10 kV/cm for both methods, construct a histogram of electron energies with a bin width of approximately 0.005 eV over the full energy range. Write the histogram to energy_histogram_10kVcm.csv.
- Output file: `/app/outputs/energy_histogram_10kVcm.csv`
- Format: csv
- Contract: columns: energy_low (float, eV), energy_high (float, eV), count_traditional (int), count_CBMC (int). Bin width ≈ 0.005 eV.
- Scoring: scored by hidden verifier

### Step 5: Dispersion Scatter at 10 kV/cm
- Role: scored
- Action: From the trajectories at F=10 kV/cm for both methods, extract a sample of at least 5000 (|p|, E) pairs per algorithm. Write the data to dispersion_scatter_10kVcm.csv.
- Output file: `/app/outputs/dispersion_scatter_10kVcm.csv`
- Format: csv
- Contract: columns: momentum (float, atomic units or consistent internal units), energy (float, eV), algorithm ('traditional' or 'CB‑MC'). At least 5000 rows per algorithm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/average_energy.csv`
- `/app/outputs/energy_histogram_10kVcm.csv`
- `/app/outputs/dispersion_scatter_10kVcm.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### average_energy.csv
- path: `/app/outputs/average_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Average electron energy for traditional and CB‑MC simulations at each applied field. Used to check that CB‑MC energy > traditional and both increase monotonically with field.
- schema:
  - `type`: table
  - `required_columns`: `field_kVcm`, `avg_energy_traditional`, `avg_energy_CBMC`
  - `units`:
    - `field_kVcm`: kV/cm
    - `avg_energy_traditional`: eV
    - `avg_energy_CBMC`: eV

### energy_histogram_10kVcm.csv
- path: `/app/outputs/energy_histogram_10kVcm.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Energy distribution histogram at 10 kV/cm. Used to verify a moderate high‑energy tail increase (CB/traditional tail ratio in [1.0,2.0]) and absence of a runaway peak.
- schema:
  - `type`: table
  - `required_columns`: `energy_low`, `energy_high`, `count_traditional`, `count_CBMC`
  - `units`:
    - `energy_low`: eV
    - `energy_high`: eV
    - `count_traditional`: count
    - `count_CBMC`: count

### dispersion_scatter_10kVcm.csv
- path: `/app/outputs/dispersion_scatter_10kVcm.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Scatter data of electron energy vs |p| at 10 kV/cm. Used to check that CB‑MC shows energy broadening (variance > 1e-6 in several momentum bins) while traditional does not.
- schema:
  - `type`: table
  - `required_columns`: `momentum`, `energy`, `algorithm`
  - `units`:
    - `momentum`: a.u.
    - `energy`: eV
    - `algorithm`: string

Notes: Structural scoring tier T3: ordering, tail ratio, and variance checks only; no exact numeric gold values are required. The agent must run both MC simulations to obtain realistic statistics; fabricated data that happens to pass the structural audits cannot be ruled out, but the workflow design forces genuine execution through the load‑bearing average‑energy step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "average_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "field_kVcm",
          "avg_energy_traditional",
          "avg_energy_CBMC"
        ],
        "units": {
          "field_kVcm": "kV/cm",
          "avg_energy_traditional": "eV",
          "avg_energy_CBMC": "eV"
        }
      },
      "description": "Average electron energy for traditional and CB‑MC simulations at each applied field. Used to check that CB‑MC energy > traditional and both increase monotonically with field."
    },
    {
      "file": "energy_histogram_10kVcm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_low",
          "energy_high",
          "count_traditional",
          "count_CBMC"
        ],
        "units": {
          "energy_low": "eV",
          "energy_high": "eV",
          "count_traditional": "count",
          "count_CBMC": "count"
        }
      },
      "description": "Energy distribution histogram at 10 kV/cm. Used to verify a moderate high‑energy tail increase (CB/traditional tail ratio in [1.0,2.0]) and absence of a runaway peak."
    },
    {
      "file": "dispersion_scatter_10kVcm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "momentum",
          "energy",
          "algorithm"
        ],
        "units": {
          "momentum": "a.u.",
          "energy": "eV",
          "algorithm": "string"
        }
      },
      "description": "Scatter data of electron energy vs |p| at 10 kV/cm. Used to check that CB‑MC shows energy broadening (variance > 1e-6 in several momentum bins) while traditional does not."
    }
  ],
  "notes": "Structural scoring tier T3: ordering, tail ratio, and variance checks only; no exact numeric gold values are required. The agent must run both MC simulations to obtain realistic statistics; fabricated data that happens to pass the structural audits cannot be ruled out, but the workflow design forces genuine execution through the load‑bearing average‑energy step."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects the three output CSV files. The verifier does **not** require exact numeric matches; instead it checks structural properties that indicate whether the CB‑MC algorithm was correctly implemented and behaves as expected relative to the traditional MC:

* The average‑energy check verifies ordering and monotonicity patterns across the field values.
* The energy‑histogram check examines the shape of the distribution and the relative high‑energy tail of the two algorithms.
* The dispersion‑scatter check probes the presence or absence of energy broadening for different momentum values.

Each of the three artifacts contributes equally to the final reward (total reward is the average of the three sub‑scores, each in [0,1]). The verifier also validates that the output files have the required format and column schemas. Running an honest simulation that follows the described algorithms is essential; fabricating numbers that superficially pass the structural checks is not sufficient.
