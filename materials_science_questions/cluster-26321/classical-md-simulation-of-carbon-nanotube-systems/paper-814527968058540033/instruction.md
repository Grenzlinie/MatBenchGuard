# MD Simulation of Torsional Failure in Graphene Nanoribbon Encapsulated Carbon Nanotubes

## Problem background
Carbon nanotubes filled with graphene nanoribbons (GNR@SWCNT) are promising nanocomposites for nano-devices. Understanding their torsional failure characteristics under varying chirality and temperature is critical for mechanical design. This task quantifies how shear stress and twist angle at failure depend on these factors, providing design guidelines for torsion-loading applications.

## Approach
The method uses classical molecular dynamics (MD) simulations with the Tersoff potential for intralayer carbon interactions and the Lennard-Jones potential for interlayer interactions between the GNR and SWCNT. Atomistic models of GNR@SWCNT are built for armchair SWCNTs of different chiralities and a pure SWCNT model for comparison. Each system is equilibrated at the target temperature using a velocity-scaling thermostat. Torsion is then applied by rotating one end at a constant angular velocity while holding the other end fixed. The shear stress and potential energy are recorded as functions of twist angle. From these curves, the maximum shear stress before failure, the critical twist angle at which the potential energy drops abruptly, and the interaction force at a fixed twist angle are extracted. The effect of chirality is examined by comparing different chiralities at 300 K, and the effect of temperature is examined by running the (11,11) system at 300 K, 500 K, and 700 K. A pure SWCNT of chirality (11,11) at 300 K is also simulated to compare its failure behavior to that of the GNR@SWCNT.

## Reproduction target
Compute the torsional properties of GNR@SWCNT models by performing molecular dynamics simulations as specified in the workflow steps. Produce a results.json file containing for each simulation: the maximum shear stress (GPa), the critical twist angle (degrees) at which potential energy drops sharply, and the interaction force (eV/Å) between GNR and SWCNT at a twist angle of 500°. Simulations to include are: (11,11) at 300 K, 500 K, 700 K; (13,13) at 300 K; (15,15) at 300 K; and a pure (11,11) SWCNT at 300 K. For the pure SWCNT, set the interaction force at 500° to 0.0. The verifier will compare your reported quantities to expected values and will check that the results satisfy physical trends consistent with the simulation setup.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/

## Workflow steps

### Step 1: System construction and equilibration
- Role: process
- Action: Build atomistic models of GNR@SWCNT for chiralities (11,11), (13,13), (15,15) with tube length 15 nm and appropriate graphene widths, fix end layers (5 layers) and set thermostat layers (4 layers). Construct a pure (11,11) SWCNT model. Equilibrate each system at the required temperatures (300 K, 500 K, 700 K) using MD with Tersoff intra-layer potential and Lennard-Jones interlayer interaction, employing a velocity scaling thermostat.
- Evidence: `/app/outputs/equilibration_output.log`

### Step 2: Torsion production MD simulations
- Role: process
- Action: For each equilibrated system, run torsion MD: apply a constant angular velocity of π/180 rad/ps at one end while fixing the other end. Record atom trajectories, potential energy, and compute shear stress as a function of twist angle. Run every required simulation (all chirality/temperature combinations and the pure SWCNT at 300 K) until failure or past the expected failure point.
- Evidence: `/app/outputs/torsion_run.log`

### Step 3: Torsion analysis and property extraction
- Role: scored (load-bearing)
- Action: From the raw simulation data, extract for each simulation: the maximum shear stress, the critical twist angle (where potential energy drops sharply), and the interaction force at a twist angle of 500°. Compile all results into a single JSON file following the output schema. For the pure SWCNT simulation, set the interaction force to 0.0.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with key 'simulations' containing an array of objects. Each object has fields: chirality (string, e.g., '(11,11)'), temperature (int), max_shear_stress_GPa (float), critical_twist_angle_deg (float), interaction_force_at_500deg_eV_Ang (float). Array must include entries for: (11,11) at 300K, 500K, 700K; (13,13) at 300K; (15,15) at 300K; and pure (11,11) SWCNT at 300K. For pure SWCNT, interaction_force_at_500deg_eV_Ang is 0.0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Consolidated table of extracted torsional properties for each simulation. The checker will compare reported values to hidden reference values and verify structural trends (e.g., monotonicity with temperature).
- schema:
  - `type`: object
  - `required`:
    - `simulations`: array
  - `items`:
    - `chirality`: string
    - `temperature`: int
    - `max_shear_stress_GPa`: float
    - `critical_twist_angle_deg`: float
    - `interaction_force_at_500deg_eV_Ang`: float
  - `required_columns`:
  - `units`:
    - `max_shear_stress_GPa`: GPa
    - `critical_twist_angle_deg`: degrees
    - `interaction_force_at_500deg_eV_Ang`: eV/Å per atom

Notes: The agent must run all simulations and compute the required scalar quantities; the file must contain all specified simulations. Tolerances and gold values are hidden; the agent should use standard force-field parameters (Tersoff for C–C, Lennard-Jones with ε=0.00284 eV, σ=3.4 Å for GNR–SWCNT).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "simulations": "array"
        },
        "items": {
          "chirality": "string",
          "temperature": "int",
          "max_shear_stress_GPa": "float",
          "critical_twist_angle_deg": "float",
          "interaction_force_at_500deg_eV_Ang": "float"
        },
        "required_columns": [],
        "units": {
          "max_shear_stress_GPa": "GPa",
          "critical_twist_angle_deg": "degrees",
          "interaction_force_at_500deg_eV_Ang": "eV/Å per atom"
        }
      },
      "description": "Consolidated table of extracted torsional properties for each simulation. The checker will compare reported values to hidden reference values and verify structural trends (e.g., monotonicity with temperature)."
    }
  ],
  "notes": "The agent must run all simulations and compute the required scalar quantities; the file must contain all specified simulations. Tolerances and gold values are hidden; the agent should use standard force-field parameters (Tersoff for C–C, Lennard-Jones with ε=0.00284 eV, σ=3.4 Å for GNR–SWCNT)."
}
```

## How you are scored
A hidden verifier separately scores the artifacts from each workflow stage. For the final scored artifact (results.json), the verifier compares your reported numerical quantities (maximum shear stress, critical twist angle, interaction force) against expected reference values and verifies required structural relationships (e.g., monotonic trends with temperature and chirality). The scores for each stage are weighted and combined into a final reward in [0,1]. To earn full credit, you must genuinely run the full simulation pipeline; simply guessing or copying numbers is insufficient.
