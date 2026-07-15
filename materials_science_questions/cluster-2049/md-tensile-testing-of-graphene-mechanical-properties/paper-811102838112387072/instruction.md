# MD Simulation of Carbon Fiber/Polymer Interphase: Transverse Tensile Testing and Mechanical Property Extraction

## Problem background
The interphase region between carbon fiber and polymer matrix significantly influences composite performance. Existing molecular models often represent the carbon fiber surface as pristine graphene and describe interactions solely through Lennard‑Jones potentials, which neglect mechanical entanglement and covalent bond breaking. This work uses a molecular interphase model where voids are intentionally created in stacked graphene layers. The voids allow polymer chains to penetrate and entangle, altering the transverse mechanical behavior. Molecular dynamics simulations are used to characterize the resulting transverse modulus and ultimate tensile strength for different interphase configurations. Your task is to compute these mechanical properties from the modeled interphases.

## Approach
The approach constructs atomistic interphase models that combine graphene layers (some pristine, some with voids created by removing carbon atoms) and a DGEBF‑DETA epoxy matrix. After initial energy minimization and NPT equilibration, a cut‑off‑based cross‑linking algorithm cures the epoxy. Three model configurations represent different interphase structures: pristine graphene (PG), graphene with voids where displacement is applied to all polymer atoms (GV_all), and graphene with voids where displacement is applied to half the polymer atoms (GV_half). Each configuration is strained in transverse tension at a constant displacement rate while constraining the graphene layers to roller boundary conditions. Spatially and temporally averaged virial stress is computed from the simulations to obtain stress–strain curves. The transverse modulus is extracted from the linear region of the curve, and the ultimate tensile strength is taken as the peak stress. The final artifact is a CSV file containing the raw stress–strain data for all three configurations.

## Reproduction target
Produce a single CSV file, stress_strain_data.csv, with columns: config (one of 'PG', 'GV_all', 'GV_half'), strain (dimensionless), and stress (in GPa). The file must contain at least 100 data points per configuration, covering strain from 0 to at least 0.10. The hidden verifier will recompute the transverse modulus (linear regression slope over 1–3% strain) and ultimate tensile strength (maximum stress) from these data and compare the results to reference benchmarks. It will also verify the relative structural ordering of the three configurations.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- MMFF force field (Merck Molecular Force Field): https://www.swissparam.ch/
- OPLS force field (Optimized Potential for Liquid Simulation): https://docs.lammps.org/force_fields.html
- Reactive force field (e.g., AIREBO): https://docs.lammps.org/bond_airebo.html
- DGEBF and DETA molecular structures

## Workflow steps

### Step 1: Build interphase models
- Role: process
- Action: Construct initial atomistic configurations for PG interphase (all 15 graphene layers pristine) and GV interphase (5 PG / 5 GV / 5 PG stacking, voids created in middle 5 layers by removing carbon atoms). The polymer matrix contains DGEBF and DETA with a 100:27 weight ratio, ~15,000 polymer atoms and ~15,840 carbon fiber atoms. Initial box dimensions ~100×65×50 Å³.
- Evidence: `/app/outputs/model_build.log`

### Step 2: Initial energy minimization and NPT equilibration
- Role: process
- Action: Relax the interphase models by conjugate gradient energy minimization, then equilibrate under NPT ensemble at 300 K and 1 atm for 10 ns (1 fs timestep) using Nose-Hoover thermostat/barostat. Use MMFF for polymer and OPLS for graphene.
- Evidence: `/app/outputs/equilibration.log`

### Step 3: Numerical curing of epoxy
- Role: process
- Action: Apply a cut-off based crosslinking algorithm: create covalent C–N bonds between carbon atoms in resin and nitrogen atoms in hardener when their distance is ≤ 4 Å. Curing is performed on the equilibrated models.
- Evidence: `/app/outputs/curing.log`

### Step 4: Post-curing NPT equilibration
- Role: process
- Action: Continue NPT ensemble equilibration (300 K, 1 atm) on the cured models until total energy converges to a stable value.
- Evidence: `/app/outputs/post_cure_equilibration.log`

### Step 5: Virtual transverse tensile tests
- Role: process
- Action: Run MD tension simulations for three configurations using a reactive force field: PG (displace all polymer atoms), GV_all (displace all polymer atoms), GV_half (displace half the polymer atoms). Apply a constant displacement rate of 0.001 Å/fs to the polymer matrix while constraining graphene layers to roller boundary conditions. Run simulations to at least 10% strain, recording virial stress and box dimensions.
- Evidence: `/app/outputs/tensile_simulation.log`

### Step 6: Compute stress-strain curves and output data
- Role: scored (load-bearing)
- Action: From the MD output of the tensile tests, compute the spatially and temporally averaged virial stress as a function of engineering strain for each configuration. Save the resulting data to a single CSV file stress_strain_data.csv with columns config, strain, stress.
- Output file: `/app/outputs/stress_strain_data.csv`
- Format: csv
- Contract: CSV with columns: config (string: 'PG', 'GV_all', 'GV_half'), strain (float), stress (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_strain_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_strain_data.csv
- path: `/app/outputs/stress_strain_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress-strain curves for three interphase configurations (PG, GV_all, GV_half). The checker recomputes transverse modulus and ultimate tensile strength from these data.
- schema:
  - `type`: table
  - `required_columns`: `config`, `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: GPa

Notes: The agent must carry out all process steps to generate the provided stress-strain data. The checker extracts properties and compares them to hidden reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_strain_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "config",
          "strain",
          "stress"
        ],
        "units": {
          "strain": "dimensionless",
          "stress": "GPa"
        }
      },
      "description": "Stress-strain curves for three interphase configurations (PG, GV_all, GV_half). The checker recomputes transverse modulus and ultimate tensile strength from these data."
    }
  ],
  "notes": "The agent must carry out all process steps to generate the provided stress-strain data. The checker extracts properties and compares them to hidden reference values."
}
```

## How you are scored
A hidden verifier reads the submitted stress_strain_data.csv. It computes, for each configuration, the transverse modulus (slope of a linear fit over strain 1–3%) and ultimate tensile strength (maximum stress). These values are compared to hidden reference numbers with tolerances that account for computational reproducibility differences (different force‑field implementations, stochastic simulation runs, etc.). The verifier also checks that the ordering of the moduli and strengths across the three configurations is physically consistent. The final score is a weighted combination of these checks; simply reporting values without legitimate simulation data will not succeed.
