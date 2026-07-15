# MD Simulation of CNT Surface Enrichment and Depletion Layer Formation

## Problem background
When polymer composites filled with carbon nanotubes (CNTs) are held in the melt state, their electrical conductance can increase over time. One hypothesis is that the nanotubes migrate toward the confining surfaces, creating a thin near-surface layer enriched in CNTs while leaving a temporarily depleted region just beneath it. This computational task uses molecular dynamics (MD) simulations to investigate the spatial redistribution of CNTs in a simplified polymer-like medium. The simulation models CNTs as coarse-grained chains subject to a Langevin thermostat, confined between attractive walls. The goal is to compute the local CNT volume fraction as a function of distance from the walls during early evolution, and to examine whether the distribution develops features consistent with surface enrichment and subsurface depletion.

## Approach
The system consists of a rectangular simulation cell that is periodic in the X and Y directions and confined in Z by two Lennard‑Jones walls. The walls attract the CNT beads, while the polymer melt is represented implicitly through a Langevin thermostat (random and frictional forces). Each CNT is modeled as a chain of rigid statistical segments; each segment is built from overlapping spherical particles that interact via a colloidal pair potential. The CNT–CNT interaction is kept weak, and the CNT–wall attraction is strong. Starting from an initial uniform distribution of CNTs at low volume fraction, the dynamics are propagated using the LAMMPS MD engine. Particle coordinates are saved at the initial configuration and at a representative later timestep. From these snapshots, histograms of the CNT volume fraction along the wall‑normal direction are computed. By examining the change in the histogram shape, one can assess the formation (if any) of a surface‑enriched layer and a subsurface depleted region.

## Reproduction target
Produce two CSV files under `/app/outputs`: `histogram_initial.csv` and `histogram_evolved.csv`. Each file must contain the CNT volume fraction binned along the Z axis (the direction normal to the confining walls), with columns `z_bin_center` (nm) and `volume_fraction` (dimensionless). The initial histogram corresponds to the starting configuration (time step 0). The evolved histogram corresponds to a snapshot after the system has been propagated long enough for redistribution to occur. The hidden verifier will perform a structural audit on these histograms, evaluating whether they exhibit certain distribution characteristics associated with surface enrichment and subsurface depletion.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/

## Workflow steps

### Step 1: Generate initial CNT configuration
- Role: process
- Action: Create a 1.5 μm × 1.5 μm × 3 μm simulation cell with attractive Lennard‑Jones walls in the Z direction and periodic boundaries in X and Y. Generate coarse‑grained CNTs as chains of statistical segments (~150 nm each), each segment made of overlapping spherical particles (diameter ~9 nm) using a chain‑growth algorithm. Distribute CNTs uniformly at 0.5 vol.% and output a LAMMPS data file.
- Evidence: `/app/outputs/config.log`

### Step 2: Run MD simulation
- Role: process
- Action: Run LAMMPS with the colloidal pair potential for CNT beads (weak CNT–CNT interaction), Lennard‑Jones wall potential (strong CNT–wall attraction), and a Langevin thermostat. Propagate the system for a time that reliably produces the depletion layer structure (e.g., ~1000 timesteps). Save particle coordinates at the initial state (step 0) and at a representative later timestep in dump files.
- Evidence: `/app/outputs/trajectory.log`

### Step 3: Compute initial volume‑fraction histogram
- Role: scored
- Action: From the dump file at the initial timestep, bin CNT bead positions along Z (wall‑normal direction) and compute the volume fraction of CNT material in each bin. Write histogram_initial.csv with columns z_bin_center (nm) and volume_fraction.
- Output file: `/app/outputs/histogram_initial.csv`
- Format: csv
- Contract: columns: z_bin_center (float, nm), volume_fraction (float)
- Scoring: scored by hidden verifier

### Step 4: Compute evolved volume‑fraction histogram
- Role: scored (load-bearing)
- Action: From the dump file at the evolved timestep, bin CNT bead positions along Z and compute the volume fraction per bin. Write histogram_evolved.csv with identical columns.
- Output file: `/app/outputs/histogram_evolved.csv`
- Format: csv
- Contract: columns: z_bin_center (float, nm), volume_fraction (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/histogram_initial.csv`
- `/app/outputs/histogram_evolved.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### histogram_initial.csv
- path: `/app/outputs/histogram_initial.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Initial CNT volume fraction histogram along Z; expected to be roughly uniform because CNTs are initially distributed uniformly.
- schema:
  - `type`: table
  - `required_columns`: `z_bin_center`, `volume_fraction`
  - `units`:
    - `z_bin_center`: nm
    - `volume_fraction`: dimensionless

### histogram_evolved.csv
- path: `/app/outputs/histogram_evolved.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Evolved CNT volume fraction histogram along Z; the checker verifies that a near‑surface enrichment peak exists (e.g., volume fraction in the first few bins significantly higher than the bulk average) and that a subsurface depletion region (volume fraction lower than the bulk average) appears at a depth of 20–100 nm from the wall.
- schema:
  - `type`: table
  - `required_columns`: `z_bin_center`, `volume_fraction`
  - `units`:
    - `z_bin_center`: nm
    - `volume_fraction`: dimensionless

Notes: Both histograms are analysed by a structural audit. The evolved histogram must exhibit the hallmarks of the reported phenomenon: a peak near the confining walls and a trough (depleted layer) underneath it, at the specified depth range. No absolute tolerance on volume fraction values is required; the check is relative to the bulk average of the middle bins.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "histogram_initial.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z_bin_center",
          "volume_fraction"
        ],
        "units": {
          "z_bin_center": "nm",
          "volume_fraction": "dimensionless"
        }
      },
      "description": "Initial CNT volume fraction histogram along Z; expected to be roughly uniform because CNTs are initially distributed uniformly."
    },
    {
      "file": "histogram_evolved.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z_bin_center",
          "volume_fraction"
        ],
        "units": {
          "z_bin_center": "nm",
          "volume_fraction": "dimensionless"
        }
      },
      "description": "Evolved CNT volume fraction histogram along Z; the checker verifies that a near‑surface enrichment peak exists (e.g., volume fraction in the first few bins significantly higher than the bulk average) and that a subsurface depletion region (volume fraction lower than the bulk average) appears at a depth of 20–100 nm from the wall."
    }
  ],
  "notes": "Both histograms are analysed by a structural audit. The evolved histogram must exhibit the hallmarks of the reported phenomenon: a peak near the confining walls and a trough (depleted layer) underneath it, at the specified depth range. No absolute tolerance on volume fraction values is required; the check is relative to the bulk average of the middle bins."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the two CSV files. The verifier performs structural checks on the histogram content—examining the shape of the distribution, relative heights of certain regions, and consistency with expected physical behavior. Each scored stage is assigned a weight, and the final reward is the weighted sum of the per‑stage scores. Simply reporting a single aggregated number or copying a value from the literature is not sufficient; the verifier evaluates the actual distribution data you submit.
