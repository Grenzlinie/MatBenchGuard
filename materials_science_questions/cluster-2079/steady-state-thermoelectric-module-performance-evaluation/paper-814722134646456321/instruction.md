# Steady-state thermoelectric module performance under nonuniform and uniform heating

## Problem background
Thermoelectric (TE) modules convert a temperature difference directly into electrical voltage. Concentrating sunlight with a water lens produces a sharply nonuniform, edge-peaked heat-flux distribution on the module surface. However, lateral heat conduction in the module’s receiving plate and electrodes may rapidly smooth this nonuniformity, so that the internal temperature gradients — and consequently the electrical output — are nearly unchanged relative to ideal uniform heating. The open question is how large the influence of the nonuniform condensing profile really is on the current–voltage and current–power performance of a TE module.

## Approach
We simulate a steady-state, coupled thermal–electrical finite-volume model of a TE module using its exact geometry: p-type and n-type elements, electrodes, and an insulating top plate. Temperature-dependent material properties (thermal conductivity, Seebeck coefficient, electrical conductivity) are implemented from polynomial functions. Two heating conditions are applied to the module’s top surface: (1) the nonuniform condensing heat-flux profile provided in `condensing_profile.csv`, and (2) a uniform heat flux that delivers the same total power as the nonuniform case. The bottom of the module is held at 288.15 K, and all convective and radiative surface losses are ignored. For each heating case we sweep the load current from zero to short-circuit, solving the system at each current to obtain the terminal voltage and electrical power. The resulting I–V and I–P curves for both conditions are then compiled.

## Reproduction target
Produce a CSV file `output_curves.csv` with columns: current_A, voltage_nonuniform_V, voltage_uniform_V, power_nonuniform_W, power_uniform_W. The current values must span from 0 A up to the short-circuit current in suitable increments (e.g., 0.1 A steps). The data must be obtained by executing the steady-state coupled thermal–electrical simulation for the two heating cases described above, using the provided geometry, material polynomials, and boundary conditions.

## Assets

- Nonuniform condensing heat-flux profile on TE module surface: https://raw.githubusercontent.com/user/paper2arm-resources/main/condensing_profile.csv
- Temperature-dependent TE material properties (polynomials)

## Workflow steps

### Step 1: Prepare simulation model
- Role: process
- Action: Set up the finite-volume mesh covering the TE module geometry (p/n elements, electrodes, insulator) according to the specified dimensions. Implement the temperature-dependent material property functions for all components using the provided polynomial expressions. Define the steady-state coupled thermal-electrical equations and boundary conditions.
- Evidence: `/app/outputs/model_setup.log`

### Step 2: Simulate nonuniform heating
- Role: process
- Action: Apply the nonuniform condensing heat flux from the provided CSV to the module top surface. Solve the coupled equations for a series of prescribed load currents (from zero to short-circuit) to obtain the steady-state terminal voltage and electrical power. Record the current, voltage, and power.
- Evidence: `/app/outputs/nonuniform_simulation.log`

### Step 3: Simulate uniform heating
- Role: process
- Action: Replace the top boundary condition with a uniform heat flux whose total power equals that of the nonuniform case. Re-solve the model for the same set of load currents and record the current, voltage, and power.
- Evidence: `/app/outputs/uniform_simulation.log`

### Step 4: Produce I‑V and I‑P curves
- Role: scored (load-bearing)
- Action: Compile the simulation results from both heating cases into a single CSV file with columns: current_A, voltage_nonuniform_V, voltage_uniform_V, power_nonuniform_W, power_uniform_W. Include data points covering the operating current range at sufficient resolution.
- Output file: `/app/outputs/output_curves.csv`
- Format: csv
- Contract: CSV with header: current_A, voltage_nonuniform_V, voltage_uniform_V, power_nonuniform_W, power_uniform_W. Current values range from 0 A to short-circuit current in suitable increments (e.g., 0.1 A steps).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/output_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### output_curves.csv
- path: `/app/outputs/output_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated I-V and I-P data for both nonuniform and uniform heating conditions. The hidden checker compares the submitted curves against reference curves digitized from the paper.
- schema:
  - `type`: table
  - `required_columns`: `current_A`, `voltage_nonuniform_V`, `voltage_uniform_V`, `power_nonuniform_W`, `power_uniform_W`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "output_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "current_A",
          "voltage_nonuniform_V",
          "voltage_uniform_V",
          "power_nonuniform_W",
          "power_uniform_W"
        ]
      },
      "description": "Simulated I-V and I-P data for both nonuniform and uniform heating conditions. The hidden checker compares the submitted curves against reference curves digitized from the paper."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently examines your submitted artifacts. The principal scored file is `output_curves.csv`. The verifier compares your computed I-V and I-P data for both heating cases against hidden reference curves. It checks the maximum absolute relative difference in voltage and power at matching current points and verifies the mutual consistency between the nonuniform and uniform results. The final reward is a weighted combination of the checks on the scored artifacts, with the output curves carrying most of the weight. Merely reporting a number is not sufficient; your simulation must genuinely produce the curves.
