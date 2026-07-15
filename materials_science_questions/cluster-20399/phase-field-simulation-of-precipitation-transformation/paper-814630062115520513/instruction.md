# Phase-Field Simulation of Directional Ternary Eutectic Solidification

## Problem background
Directional solidification of ternary eutectic alloys, such as Ag–Al–Cu, produces complex microstructural patterns whose connectivity strongly influences material properties. Predicting and controlling these patterns is challenging because of the interplay between diffusion and interfacial energies. Quantitative measures like the nearest‑neighbor connectivity of the intermetallic phases are therefore of central interest. This task centres on reproducing large‑scale three‑dimensional phase‑field simulations that generate such patterns and then computing the nearest‑neighbour distributions for the Ag₂Al and Al₂Cu phases, which are the primary structural features to be compared with experimental observations.

## Approach
The core method is a grand‑potential phase‑field model that evolves three solid order parameters and a liquid, coupled to diffusion of chemical potentials with an anti‑trapping current. The driving force derives from parabolic free‑energy fits around the eutectic composition. The simulation is performed under a frozen temperature gradient (directional solidification), using a moving window technique that follows the solidification front to keep the computational domain manageable. Two parameter sets are defined; the “EXP” set uses a liquid composition and solid phase fractions derived from experiments and is intended to reproduce microstructures comparable to experimental micrographs. The simulation is run on a large 3‑D grid with periodic lateral boundaries until steady‑state growth is reached. From a steady‑state cross‑section near the front, the nearest‑neighbour connectivity of the Ag₂Al and Al₂Cu regions is quantified: for each region, the number of adjacent regions of the other intermetallic phase is counted (ignoring the surrounding Al matrix), and histograms of relative frequency versus neighbour count are produced.

## Reproduction target
Using the EXP parameter set (liquid composition: 0.237 Ag, 0.622 Al, 0.141 Cu; solid phase fractions: 0.334 Al, 0.309 Al₂Cu, 0.355 Ag₂Al; numerical and free‑energy parameters as assembled in Step 1), set up and run the grand‑potential phase‑field simulation with the waLBerla framework (or an equivalent open‑source implementation) on a domain of 800×800×4256 cells. Apply periodic lateral boundaries, Neumann condition at the solidified end, Dirichlet at the melt reservoir, and a moving window driven by a temperature gradient of 2.2 K/mm with velocity 79.35 µm/s. Run until steady‑state growth (constant phase fractions). Then extract a cross‑section near the solidification front, identify the Ag₂Al and Al₂Cu regions, and for each region count the number of neighbouring regions of the other intermetallic phase (ignore the surrounding Al matrix). Produce two CSV files: nearest_neighbors_Ag2Al.csv and nearest_neighbors_Al2Cu.csv, each with columns neighbor_count (integer) and relative_frequency (float). The distributions must contain a peak at two neighbours, reflecting the chain‑like connectivity that characterises the experimental structure.

## Assets

- waLBerla framework: https://github.com/walberla/walberla

## Workflow steps

### Step 1: Prepare EXP parameter set
- Role: process
- Action: Assemble the EXP parameter set: liquid composition (0.237 Ag, 0.622 Al, 0.141 Cu), solid phase fractions (0.334 Al, 0.309 Al₂Cu, 0.355 Ag₂Al), and the parabolic free-energy coefficients from the paper (Tables 1 and 2). Write the complete parameter set as an evidence file exp_parameters.json.
- Evidence: `/app/outputs/exp_parameters.json`

### Step 2: Run 3D phase-field directional solidification simulation
- Role: process
- Action: Set up and run the grand-potential phase-field simulation with the EXP parameter set using the waLBerla framework (or an equivalent open-source implementation). Use a domain of 800×800×4256 cells with periodic lateral boundaries, Neumann condition at the solidified end, Dirichlet at the melt reservoir, a moving window, and a frozen temperature gradient of 2.2 K/mm with velocity 79.35 µm/s. Run until steady-state growth is reached (constant phase fractions). Write a simulation log as evidence.
- Evidence: `/app/outputs/simulation.log`

### Step 3: Compute nearest-neighbor statistics for Ag₂Al
- Role: scored (load-bearing)
- Action: From the steady-state 3D phase fields, extract a cross-section near the solidification front. Identify the Ag₂Al regions and count for each Ag₂Al region the number of neighboring Ag₂Al and Al₂Cu regions (ignore the Al matrix). Compute the relative frequency histogram of neighbor counts and write to the output file.
- Output file: `/app/outputs/nearest_neighbors_Ag2Al.csv`
- Format: csv
- Contract: neighbor_count:integer, relative_frequency:float
- Scoring: scored by hidden verifier

### Step 4: Compute nearest-neighbor statistics for Al₂Cu
- Role: scored (load-bearing)
- Action: Similarly, compute the neighbor-count distribution for Al₂Cu regions from the same cross-section. Write the histogram to the output file.
- Output file: `/app/outputs/nearest_neighbors_Al2Cu.csv`
- Format: csv
- Contract: neighbor_count:integer, relative_frequency:float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nearest_neighbors_Ag2Al.csv`
- `/app/outputs/nearest_neighbors_Al2Cu.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nearest_neighbors_Ag2Al.csv
- path: `/app/outputs/nearest_neighbors_Ag2Al.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Histogram of nearest-neighbor counts for Ag₂Al regions: neighbor_count (integer) and relative_frequency (float).
- schema:
  - `type`: table
  - `required_columns`: `neighbor_count`, `relative_frequency`
  - `units`:
    - `neighbor_count`: integer count
    - `relative_frequency`: proportion between 0 and 1

### nearest_neighbors_Al2Cu.csv
- path: `/app/outputs/nearest_neighbors_Al2Cu.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Histogram of nearest-neighbor counts for Al₂Cu regions: neighbor_count (integer) and relative_frequency (float).
- schema:
  - `type`: table
  - `required_columns`: `neighbor_count`, `relative_frequency`
  - `units`:
    - `neighbor_count`: integer count
    - `relative_frequency`: proportion between 0 and 1

Notes: Scoring compares bin-wise relative frequencies to the paper's experimental reference histogram (derived from Fig. 6) using a per-bin absolute tolerance. No gold values are disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nearest_neighbors_Ag2Al.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "neighbor_count",
          "relative_frequency"
        ],
        "units": {
          "neighbor_count": "integer count",
          "relative_frequency": "proportion between 0 and 1"
        }
      },
      "description": "Histogram of nearest-neighbor counts for Ag₂Al regions: neighbor_count (integer) and relative_frequency (float)."
    },
    {
      "file": "nearest_neighbors_Al2Cu.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "neighbor_count",
          "relative_frequency"
        ],
        "units": {
          "neighbor_count": "integer count",
          "relative_frequency": "proportion between 0 and 1"
        }
      },
      "description": "Histogram of nearest-neighbor counts for Al₂Cu regions: neighbor_count (integer) and relative_frequency (float)."
    }
  ],
  "notes": "Scoring compares bin-wise relative frequencies to the paper's experimental reference histogram (derived from Fig. 6) using a per-bin absolute tolerance. No gold values are disclosed to the agent."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the two output CSV files. The verifier compares the relative frequency for each neighbour count in your files against a hidden reference distribution (derived from published experimental measurements). Credit is awarded based on how many bins agree within an acceptable tolerance; partial credit scales with the number of matching bins. The verifier does not reveal the reference values or tolerance. Simply reporting a single summary statistic is insufficient—the complete histogram must be submitted and checked. Each of the two histogram files contributes a substantial share to the total score; full credit requires both to be in good agreement with the reference.
