# Photothermal Tuning Simulation of Toroidal Microcavities

## Problem background
Ultrahigh-quality factor toroidal optical microcavities are promising for sensing and photonics, but their absolute resonance wavelengths are fixed by fabrication, necessitating tuning mechanisms. One approach is photothermal tuning: a free-space laser is focused onto the resonator's silicon support pillar, causing local heating that changes the temperature of the silica rim and shifts the resonance wavelength through the thermo-optic effect. Finite-element heat-flow simulations play a critical role in modelling the temperature profiles and predicting the resulting resonance shift and thermal dynamics. This task aims to compute the equilibrium resonance shift as a function of pump power for two different toroid geometries, and to determine the thermal equilibration cutoff frequency, by implementing the heat-flow model with an open-source finite-element solver.

## Approach
Build a finite-element model of the toroid geometry (silicon pillar and silica toroid) using the dimensions and thermal properties provided in the supplementary material. Set up steady-state and transient heat transfer physics with appropriate boundary conditions. Solve the steady-state problem for a range of absorbed pump powers to obtain the equilibrium temperature distribution. Extract the temperature at the silica rim where the optical mode resides, then convert it to a resonance wavelength shift using the known thermo-optic relation for silica. Separately, run a time-dependent simulation with a modulated heat source to obtain the temporal temperature response, and extract the thermal cutoff frequency from that response. The entire workflow uses an open-source finite-element solver (e.g., FEniCS) and follows the modelling recipe described in the supplementary material.

## Reproduction target
Produce a CSV file (`steady_state_results.csv`) containing the simulated resonance wavelength shifts for both standard and re-etched toroid geometries over a set of absorbed pump powers, computed from steady-state finite-element heat-flow simulations and the thermo-optic relation. Also produce a text file (`cutoff_frequency.txt`) containing the thermal equilibration cutoff frequency for the standard toroid geometry, determined from a time-dependent simulation. The shift-versus-power data and cutoff frequency will be compared to a hidden reference to assess the accuracy of the simulations.

## Assets

- Paper supplementary material (PDF detailing simulation geometry, material properties, and boundary conditions): 10.1063/1.4833539
- Open-source finite element solver (e.g., FEniCS): fenics

## Workflow steps

### Step 1: FEM model setup
- Role: process
- Action: Set up the finite-element model geometry for standard and re-etched toroids using the dimensions and material thermal properties (silicon, silica) from the supplementary material. Define steady-state and transient heat transfer physics, boundary conditions, and mesh.
- Evidence: none

### Step 2: Steady-state heat-flow simulations
- Role: process
- Action: Run steady-state heat-flow simulations for a set of absorbed pump powers (e.g., 0 to 15 mW) for both standard and re-etched toroid geometries. Save the resulting temperature field or temperature profiles for later extraction.
- Evidence: none

### Step 3: Compute resonance shift
- Role: scored (load-bearing)
- Action: For each pump power and toroid type, extract the silica rim temperature from the steady-state simulation results. Apply the resonance-shift formula Δλ = (λ0/n0)*(dn/dT(T))*(T-T0) with λ0=1.566 μm, n0=1.444, and dn/dT(T)=2.6e-8 T + 7.5e-7 K^{-1}. Write the pump power, temperature, and shift to the output CSV.
- Output file: `/app/outputs/steady_state_results.csv`
- Format: csv
- Contract: CSV with columns: toroid_type (string, 'standard' or 're-etched'), pump_power_mW (float), temperature_K (float), shift_pm (float). Each row is one pump power.
- Scoring: scored by hidden verifier

### Step 4: Time-dependent heat-flow simulation
- Role: process
- Action: Run a transient heat-flow simulation for the standard toroid geometry with a modulated heating source (e.g., square wave modulation) covering a frequency range. Save the temporal temperature response.
- Evidence: none

### Step 5: Extract cutoff frequency
- Role: scored (load-bearing)
- Action: Analyze the transient simulation output to determine the thermal equilibration cutoff frequency (the frequency at which the response magnitude falls to a specified fraction of its low-frequency value, or equivalent from the exponential time dependence). Write the cutoff frequency (in Hz) to the output file.
- Output file: `/app/outputs/cutoff_frequency.txt`
- Format: txt
- Contract: A single floating-point number representing the cutoff frequency in Hz.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/steady_state_results.csv`
- `/app/outputs/cutoff_frequency.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### steady_state_results.csv
- path: `/app/outputs/steady_state_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted resonance wavelength shift as a function of pump power for both standard and re-etched toroids, derived from steady-state finite-element heat-flow simulations and the thermo-optic coefficient relation.
- schema:
  - `type`: table
  - `required_columns`: `toroid_type`, `pump_power_mW`, `temperature_K`, `shift_pm`

### cutoff_frequency.txt
- path: `/app/outputs/cutoff_frequency.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Predicted thermal equilibration cutoff frequency for a standard toroid geometry from time-dependent finite-element simulations.
- schema:
  - `type`: text
  - `description`: Single floating-point number, the thermal equilibration cutoff frequency in Hz.

Notes: The checker compares the agent's shift values at key pump powers and the cutoff frequency to the paper-reported values with appropriate tolerances, and may also verify the shift-vs-power trend (linear for standard toroid, quadratic for re-etched toroid).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "steady_state_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "toroid_type",
          "pump_power_mW",
          "temperature_K",
          "shift_pm"
        ]
      },
      "description": "Predicted resonance wavelength shift as a function of pump power for both standard and re-etched toroids, derived from steady-state finite-element heat-flow simulations and the thermo-optic coefficient relation."
    },
    {
      "file": "cutoff_frequency.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number, the thermal equilibration cutoff frequency in Hz."
      },
      "description": "Predicted thermal equilibration cutoff frequency for a standard toroid geometry from time-dependent finite-element simulations."
    }
  ],
  "notes": "The checker compares the agent's shift values at key pump powers and the cutoff frequency to the paper-reported values with appropriate tolerances, and may also verify the shift-vs-power trend (linear for standard toroid, quadratic for re-etched toroid)."
}
```

## How you are scored
A hidden verifier independently checks your output artifacts. For `steady_state_results.csv`, it examines the simulated shift values at key pump powers and the overall shift-versus-power trend, comparing them to hidden reference data. For `cutoff_frequency.txt`, it compares the reported cutoff frequency to a hidden reference value. Each artifact carries a weight, and the final reward (a float between 0 and 1) depends on how closely your results match the expected outcomes within acceptable tolerances. Simply copying numbers from the paper is not enough; you must run the simulations to produce the required outputs.
