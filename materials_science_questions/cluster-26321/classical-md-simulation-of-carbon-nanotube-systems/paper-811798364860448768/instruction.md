# Classical MD Simulation of Carbon Nanotube Systems: Interfacial Shear Stress and Solvation Shell Structure

## Problem background
When liquids flow through nanoscale channels, the resistance they encounter arises from interactions with the solid wall at the molecular level. For applications such as high‑performance energy‑absorption systems that rely on forced liquid infiltration into nanopores, this resistance directly determines energy dissipation and device efficiency. A key quantity is the interfacial shear stress τ, which is the force per area exerted between the liquid and the wall. The corresponding nominal viscosity η̃ captures the effective fluid‑dynamic resistance. Molecular dynamics simulations suggest that the dominant microscopic factor controlling τ is the position and structure of the first solvation shell—the layer of liquid molecules immediately adjacent to the wall—because it governs the short‑range repulsive forces. The task is to compute τ and η̃ for water flowing inside a carbon nanotube under well‑defined conditions, using non‑equilibrium molecular dynamics (NEMD), and to produce the radial density profile of oxygen atoms that reveals the location of this first solvation shell.

## Approach
A rigid, defect‑free single‑walled carbon nanotube of specified diameter and length is filled with pure water modelled by the SPC/E force field. The simulation cell is periodic along the tube axis. After energy minimization and equilibration in the NVT ensemble at room temperature, a uniform axial body force is applied to every water atom, driving the liquid along the tube. The mean centre‑of‑mass velocity is recorded until it reaches a target value. Once the steady‑state forced flow is established, the velocity is monitored and atomic trajectories are saved for density analysis. Then the driving force is suddenly removed, and the liquid decelerates freely. From the initial deceleration of the centre of mass, Newton’s second law gives the net wall shear force, which is converted to the interfacial shear stress τ using the known tube surface area. The effective (nominal) viscosity η̃ is computed from τ, the tube radius, and the steady‑state mean velocity. Independently, the radial oxygen density profile is calculated by binning oxygen atoms in cylindrical shells and averaging over the steady‑state flow period; it shows the characteristic peak of the first solvation shell near the carbon wall.

## Reproduction target
Determine the interfacial shear stress τ (in MPa) and the nominal viscosity η̃ (in centipoise, cp) for pure SPC/E water flowing inside a neutral (18,18) single‑walled carbon nanotube (diameter 24.41 Å, periodic length 60 Å) at a mean axial transport rate of approximately 216 m/s. The necessary raw velocity time‑series and system metadata are written to steady_velocity.csv, deceleration_phase.csv, and system_metadata.json. Separately, compute the radial oxygen density profile across the tube and output it as radial_density.csv. The analysis follows the NEMD protocol described in the Workflow steps, using the force‑field parameters for SPC/E water and water‑carbon Lennard‑Jones interactions given in the paper's Table I.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov

## Workflow steps

### Step 1: System construction and force-field assignment
- Role: process
- Action: Build the simulation cell containing a rigid (18,18) single-walled carbon nanotube (diameter 24.41 Å, periodic along axis with length 60 Å) filled with SPC/E water at initial density 998 kg/m³. Assign force-field parameters from the paper (SPC/E water model and water-carbon Lennard-Jones interactions). No ions are added. Produce the initial LAMMPS data and input files.
- Evidence: `/app/outputs/system.data`

### Step 2: NVT equilibration
- Role: process
- Action: Perform a 100 ps NVT simulation at 298.5 K with a 1 fs time step. Use a Nosé-Hoover thermostat (time constant 0.1 ps) and subtract the mean axial velocity during temperature calculation. Apply periodic boundary conditions in the axial direction.
- Evidence: `/app/outputs/equil.log`

### Step 3: NEMD production run (driven flow and deceleration)
- Role: process
- Action: From the equilibrated configuration, apply a uniform axial body force to drive the water. Record the mean centre-of-mass velocity. When the mean axial velocity reaches approximately 216 m/s, continue the forced flow for a period while dumping atomic positions for the radial density analysis. Then remove the driving force and run for a short period while recording the centre-of-mass velocity at fine time resolution to capture the initial deceleration. Maintain temperature control as in the equilibration step.
- Evidence: `/app/outputs/production.log`

### Step 4: Extract steady-state flow velocity and deceleration phase
- Role: scored (load-bearing)
- Action: From the NEMD production data, extract two time-series files: steady_velocity.csv (time in ps, mean axial velocity in m/s) during the steady-state forced flow period, and deceleration_phase.csv (time in ps, mean axial velocity in m/s) during the free deceleration period. Also compute the total mass of water inside the nanotube and write system_metadata.json with total_mass_kg, diameter_m, and length_m.
- Output file: `/app/outputs/steady_velocity.csv,deceleration_phase.csv,system_metadata.json`
- Format: csv
- Contract: steady_velocity.csv: columns [time (ps), mean_axial_velocity (m/s)]; deceleration_phase.csv: columns [time (ps), mean_axial_velocity (m/s)]; system_metadata.json: {"total_mass_kg": number, "diameter_m": number, "length_m": number}
- Scoring: scored by hidden verifier

### Step 5: Radial oxygen density profile
- Role: scored
- Action: Using the atomic trajectory from the steady-state forced flow period, compute the radial oxygen density profile relative to the tube centre. Average over the entire steady-state interval and output radial_density.csv with columns r_angstrom (Å) and density_kg_per_m3 (kg/m³), covering the radial range from the centre to the wall at a resolution no coarser than 0.1 Å.
- Output file: `/app/outputs/radial_density.csv`
- Format: csv
- Contract: columns: r_angstrom (float), density_kg_per_m3 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/steady_velocity.csv`
- `/app/outputs/deceleration_phase.csv`
- `/app/outputs/system_metadata.json`
- `/app/outputs/radial_density.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### deceleration_phase.csv
- path: `/app/outputs/deceleration_phase.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of the mean axial velocity during the free deceleration period. The initial slope provides the deceleration used to compute interfacial shear stress.
- schema:
  - `type`: table
  - `required_columns`: `time`, `mean_axial_velocity`
  - `units`:
    - `time`: ps
    - `mean_axial_velocity`: m/s

### radial_density.csv
- path: `/app/outputs/radial_density.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Radial oxygen density profile. The checker verifies the existence and position of the first solvation shell peak near the expected wall distance.
- schema:
  - `type`: table
  - `required_columns`: `r_angstrom`, `density_kg_per_m3`
  - `units`:
    - `r_angstrom`: Angstrom
    - `density_kg_per_m3`: kg/m^3

Notes: The primary scoring uses the raw velocity file and metadata (which are intermediate artefacts not listed here) to recompute interfacial shear stress and nominal viscosity, comparing them against the paper's reported values with tolerances consistent with re-run spread. The radial density profile is audited structurally to confirm the first solvation shell location.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "deceleration_phase.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "mean_axial_velocity"
        ],
        "units": {
          "time": "ps",
          "mean_axial_velocity": "m/s"
        }
      },
      "description": "Time series of the mean axial velocity during the free deceleration period. The initial slope provides the deceleration used to compute interfacial shear stress."
    },
    {
      "file": "radial_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_angstrom",
          "density_kg_per_m3"
        ],
        "units": {
          "r_angstrom": "Angstrom",
          "density_kg_per_m3": "kg/m^3"
        }
      },
      "description": "Radial oxygen density profile. The checker verifies the existence and position of the first solvation shell peak near the expected wall distance."
    }
  ],
  "notes": "The primary scoring uses the raw velocity file and metadata (which are intermediate artefacts not listed here) to recompute interfacial shear stress and nominal viscosity, comparing them against the paper's reported values with tolerances consistent with re-run spread. The radial density profile is audited structurally to confirm the first solvation shell location."
}
```

## How you are scored
The hidden verifier independently evaluates each scored artifact you produce. For the shear stress and nominal viscosity, the verifier reads steady_velocity.csv, deceleration_phase.csv, and system_metadata.json, recomputes τ and η̃ using the same physical definitions, and compares them against expected values with tolerances that reflect legitimate re‑run spread. For the radial density profile, the verifier audits radial_density.csv structurally, verifying that a clear first‑solvation‑shell peak exists at a physically reasonable distance from the nanotube wall. All scored artifacts contribute to the final reward; reporting a single number without the required raw trajectories and metadata is insufficient to earn full credit.
