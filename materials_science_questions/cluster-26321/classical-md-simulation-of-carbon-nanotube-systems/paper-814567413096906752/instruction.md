# Classical MD Simulation of Nanoparticle Motion under a Staircase Electric Field

## Problem background
Manipulating neutral and nonpolar nanoparticles in water is difficult because they carry no net charge or strong polarity that an external electric field can directly exploit. This work explores whether a nonuniform external electric field can influence the motion of such a nanoparticle by altering the water environment around it. The hypothesis is that the electric field creates a spatially varying water energy, and that a nanoparticle may move in response to this energy landscape in order to minimise the change in water energy caused by its presence. The task is to reconstruct this scenario and produce quantitative evidence on how the water energy per molecule varies with position under a staircase electric field and how the nanoparticle actually moves.

## Approach
The system is a water box confined between two parallel graphene plates. The water is modelled with the SPC/E force field. A nonuniform staircase electric field is applied along the z‑direction: the region is divided into four equal vertical sections, each with a different uniform field intensity, stepping from highest intensity at the bottom to lowest at the top. A neutral, nonpolar C180 fullerene (modelled with Lennard‑Jones and harmonic potentials) is placed initially in the highest‑field region. Two molecular dynamics (MD) simulations are performed using GROMACS: a pure‑water simulation (no nanoparticle) to characterise the water energy profile under the field, and a nanoparticle‑in‑water simulation to observe the nanoparticle trajectory. From the pure‑water run, the average potential energy per water molecule (water‑water plus electric energy) is binned by z. Using that profile, the volume‑integrated water energy that would be occupied by the nanoparticle (U_NP‑volume) is computed as a function of z by integrating the energy density over a sphere of the nanoparticle’s radius. From the nanoparticle run, the centre‑of‑mass z‑coordinate of the nanoparticle is extracted as a time series. Together these three data products allow an assessment of the relationship between the electric field, the water energy, and the nanoparticle’s motion without requiring any direct electric force on the nanoparticle itself.

## Reproduction target
The goal is to execute the full MD workflow and produce the three scored output files: step_02_water_energy.csv (water energy per molecule as a function of z), step_03_U_NP_volume.csv (U_NP‑volume as a function of z), and step_01_zcoord.dat (nanoparticle centre‑of‑mass z‑coordinate versus time). The evaluation will check whether the data obtained from these simulations exhibit physical relationships that are consistent with the hypothesised mechanism. Specifically, the verifier will examine the spatial dependence of the water energy, the magnitude of U_NP‑volume at different field intensities, and the net displacement of the nanoparticle from its starting position. No pre‑existing dataset is required; all results are derived from the simulations you run on the system constructed and parameterised exactly as described.

## Assets

- GROMACS: https://www.gromacs.org/

## Workflow steps

### Step 1: System construction
- Role: process
- Action: Build the simulation cell: two graphene plates at z=0 and z=24 nm (area 5×5 nm²), fill with ~19386 SPC/E water molecules, place a C180 nanoparticle (radius 0.59 nm) with its center at (2.5,2.5,3.0) nm. Assign force-field parameters: LJ for carbon-carbon and carbon-oxygen, harmonic bonds and angles. Define the staircase electric field: four uniform steps with E=0.3 V/nm (intensities 1.2, 0.9, 0.6, 0.3 V/nm from bottom to top).
- Evidence: none

### Step 2: Pure-water MD simulation
- Role: process
- Action: Run a pure-water simulation (no nanoparticle) under the staircase electric field: NVT at 300 K (v-rescale thermostat, 2 fs timestep, LJ cutoff 1.2 nm, PME real-space cutoff 1.0 nm). Equilibrate 10 ns, then production 50 ns (total 60 ns).
- Evidence: none

### Step 3: Water energy per molecule analysis
- Role: scored (load-bearing)
- Action: From the last 50 ns of the pure-water trajectory, compute the water energy per molecule (water-water interaction energy plus electric energy −E·μ) as a function of z. Bin the z-coordinate in 0.1 nm slices and average over all water molecules and time steps to obtain the mean potential energy per molecule per bin.
- Output file: `/app/outputs/step_02_water_energy.csv`
- Format: csv
- Contract: z (nm), water_energy_per_molecule (kJ/mol)
- Scoring: scored by hidden verifier

### Step 4: U_NP-volume computation
- Role: scored
- Action: Using the water energy profile from step_02_water_energy.csv, compute U_NP-volume(z) = sum of water energy per molecule values inside a sphere of radius 0.59 nm centered at (2.5,2.5,z), for z from 0 to 24 nm in steps of 0.1 nm (or finer). Approximate by integrating the water energy density over the spherical volume.
- Output file: `/app/outputs/step_03_U_NP_volume.csv`
- Format: csv
- Contract: z (nm), U_NP_volume (kJ/mol)
- Scoring: scored by hidden verifier

### Step 5: Nanoparticle system equilibration
- Role: process
- Action: Take the nanoparticle-water system from step 1, apply position restraints on the nanoparticle, and run NVT at 300 K (same simulation parameters as step 2) for 4 ns to equilibrate the water structure around the fixed nanoparticle.
- Evidence: none

### Step 6: Nanoparticle production simulation
- Role: process
- Action: Remove the nanoparticle restraints and continue the NVT simulation for up to 200 ns (or until the nanoparticle clearly crosses the first transition line at z=6 nm). Save the trajectory at 0.5 ps intervals.
- Evidence: none

### Step 7: Nanoparticle z-position extraction
- Role: scored (load-bearing)
- Action: From the production trajectory, extract the z-coordinate of the nanoparticle center of mass at every saved time step (0.5 ps). Write a two-column whitespace-separated text file with time (ps) and z (nm), no header.
- Output file: `/app/outputs/step_01_zcoord.dat`
- Format: txt
- Contract: time (ps) <whitespace> z (nm)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_water_energy.csv`
- `/app/outputs/step_03_U_NP_volume.csv`
- `/app/outputs/step_01_zcoord.dat`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_water_energy.csv
- path: `/app/outputs/step_02_water_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Water energy per molecule averaged in 0.1 nm z-bins. Scored by checking monotonic decrease with electric field intensity.
- schema:
  - `type`: table
  - `required_columns`: `z`, `water_energy_per_molecule`
  - `units`:
    - `z`: nm
    - `water_energy_per_molecule`: kJ/mol

### step_03_U_NP_volume.csv
- path: `/app/outputs/step_03_U_NP_volume.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Volume-integrated water energy U_NP-volume as a function of z. Scored by verifying that its magnitude is larger at a high-field (z≈3 nm) than at a low-field (z≈21 nm) position.
- schema:
  - `type`: table
  - `required_columns`: `z`, `U_NP_volume`
  - `units`:
    - `z`: nm
    - `U_NP_volume`: kJ/mol

### step_01_zcoord.dat
- path: `/app/outputs/step_01_zcoord.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Nanoparticle centre‑of‑mass z‑coordinate vs time. Scored by verifying net displacement: final average z > 6 nm (crossed first field transition).
- schema:
  - `type`: text
  - `description`: Two column whitespace-separated values: time (ps) and z_coordinate (nm). No header.

Notes: All three artifacts are required. The checker performs structural trend checks (monotonicity, threshold crossing, relative magnitude) with tolerances to absorb run-to-run noise. No absolute matching against paper-reported numeric values is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_water_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "water_energy_per_molecule"
        ],
        "units": {
          "z": "nm",
          "water_energy_per_molecule": "kJ/mol"
        }
      },
      "description": "Water energy per molecule averaged in 0.1 nm z-bins. Scored by checking monotonic decrease with electric field intensity."
    },
    {
      "file": "step_03_U_NP_volume.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "U_NP_volume"
        ],
        "units": {
          "z": "nm",
          "U_NP_volume": "kJ/mol"
        }
      },
      "description": "Volume-integrated water energy U_NP-volume as a function of z. Scored by verifying that its magnitude is larger at a high-field (z≈3 nm) than at a low-field (z≈21 nm) position."
    },
    {
      "file": "step_01_zcoord.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Two column whitespace-separated values: time (ps) and z_coordinate (nm). No header."
      },
      "description": "Nanoparticle centre‑of‑mass z‑coordinate vs time. Scored by verifying net displacement: final average z > 6 nm (crossed first field transition)."
    }
  ],
  "notes": "All three artifacts are required. The checker performs structural trend checks (monotonicity, threshold crossing, relative magnitude) with tolerances to absorb run-to-run noise. No absolute matching against paper-reported numeric values is required."
}
```

## How you are scored
A hidden verifier independently examines each of the three output files. It computes derived properties from your data and compares them to structural criteria that capture the expected physical behaviour (for example, trends, thresholds, and relative magnitudes). Each artifact is scored separately according to how well it satisfies those criteria, and the scores are combined into a final reward between 0 and 1. You do not need to match specific numerical values from the literature; instead, the verifier checks whether your simulated results faithfully reflect the underlying physics. The checks are fully automatic and do not require any internet access; only the files you place under `/app/outputs` are read. Make sure each file follows exactly the specified format and unit conventions, as formatting errors can prevent the verifier from reading your data.
