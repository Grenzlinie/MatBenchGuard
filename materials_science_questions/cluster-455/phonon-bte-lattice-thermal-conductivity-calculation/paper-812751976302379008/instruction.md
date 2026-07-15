# Thermal Conductivity of C80H30 Nanographene via EMD Simulation

## Problem background
The thermal conductivity of warped nanographene (C80H30) is of fundamental and practical interest for nanoscale thermal management. This non‑planar carbon nanostructure, characterized by a network of non‑hexagonal rings and attached hydrogen atoms, is expected to exhibit anisotropic heat transport due to its curved morphology. Classical molecular dynamics simulations can provide quantitative predictions of its directional thermal conductivities and help understand how structural disorder influences thermal transport.

## Approach
Equilibrium molecular dynamics (EMD) simulations using the AIREBO reactive potential are employed to compute the thermal conductivity via the Green‑Kubo formalism. The molecule is placed in a periodic supercell, equilibrated in the canonical ensemble (NVT) at the target temperature, and then evolved to record atomic velocities and energies. The heat flux autocorrelation functions are computed from the production trajectory and integrated to obtain the thermal conductivity in the x, y, and z directions. A preliminary time‑step convergence study identifies an integration time step that balances energy conservation and numerical cost.

## Reproduction target
Compute the three directional thermal conductivities λx, λy, and λz of C80H30 at 300 K and store them in a JSON file (`/app/outputs/step_01_thermal_conductivity.json`) with keys lambda_x, lambda_y, lambda_z, each a floating‑point number in units of W·m⁻¹·K⁻¹.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/download.html
- AIREBO potential: https://lammps.sandia.gov/doc/pair_airebo.html
- C80H30 molecular structure: 10.1038/nchem.1695

## Workflow steps

### Step 1: Build C80H30 supercell structure
- Role: process
- Action: Obtain the atomic coordinates of the C80H30 nanographene molecule from the public literature (e.g., the synthesis paper Kawasumi et al. 2013) or construct it using standard molecular modeling tools. Place the molecule in a tetragonal supercell with lattice parameters a = b = 1.7 nm, c = 1.6 nm, producing the initial configuration for the simulation.
- Evidence: `/app/outputs/initial_structure.data`

### Step 2: Time step convergence study
- Role: process
- Action: Perform short NVT simulations at 300 K using LAMMPS and the AIREBO potential with different time steps (e.g., 0.2 fs to 1.0 fs). Monitor total, potential, and kinetic energies to select the time step (0.6 fs) that minimizes total/potential energy while keeping kinetic energy stable.
- Evidence: `/app/outputs/time_step_energy_data.json`

### Step 3: Equilibration and production MD simulation
- Role: process
- Action: Using the determined time step (0.6 fs), run a 2 ns NVT equilibration at 300 K followed by a 2 ns production run with the AIREBO potential. Save atomic velocities, positions, and total energies at every time step to a trajectory file for subsequent heat flux calculation.
- Evidence: `/app/outputs/production_trajectory.dcd`

### Step 4: Compute thermal conductivity via Green-Kubo
- Role: scored (load-bearing)
- Action: From the production trajectory, compute the heat flux autocorrelation functions for the x, y, and z directions and integrate them using the Green-Kubo relation to obtain the directional thermal conductivities λx, λy, λz in W·m⁻¹·K⁻¹. Write the three values to the JSON output file.
- Output file: `/app/outputs/step_01_thermal_conductivity.json`
- Format: json
- Contract: JSON object with keys lambda_x (float), lambda_y (float), lambda_z (float). Values are thermal conductivities in W/(m·K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thermal_conductivity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_thermal_conductivity.json
- path: `/app/outputs/step_01_thermal_conductivity.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Directional thermal conductivities of C80H30 nanographene at 300 K computed from an EMD simulation with the AIREBO potential. The checker compares each value to a hidden reference and also verifies that the ordering lambda_y > lambda_z > lambda_x holds.
- schema:
  - `type`: object
  - `required`:
    - `lambda_x`: float (W/(m·K))
    - `lambda_y`: float (W/(m·K))
    - `lambda_z`: float (W/(m·K))

Notes: The checker will use reference_match: the reported directional thermal conductivities will be compared to the paper's reported values with absolute tolerances. Additionally, the known structural ordering λy > λz > λx must be satisfied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_thermal_conductivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lambda_x": "float (W/(m·K))",
          "lambda_y": "float (W/(m·K))",
          "lambda_z": "float (W/(m·K))"
        }
      },
      "description": "Directional thermal conductivities of C80H30 nanographene at 300 K computed from an EMD simulation with the AIREBO potential. The checker compares each value to a hidden reference and also verifies that the ordering lambda_y > lambda_z > lambda_x holds."
    }
  ],
  "notes": "The checker will use reference_match: the reported directional thermal conductivities will be compared to the paper's reported values with absolute tolerances. Additionally, the known structural ordering λy > λz > λx must be satisfied."
}
```

## How you are scored
A hidden verifier reads the output JSON file, confirms it contains the required keys with numeric values, and compares the reported thermal conductivities to reference data. The final score is a weighted combination of schema compliance and numerical accuracy. Simply copying the paper’s published numbers will not satisfy the verifier; the simulation must be correctly executed to produce results that fall within the verifier’s acceptance criteria.
