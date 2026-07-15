# Displacement Cascade Properties in 3C-SiC from Molecular Dynamics

## Problem background
Silicon carbide (SiC) is a semiconductor with potential for use in high-temperature and radiation-hard environments. Understanding the primary damage produced by energetic knock-on atoms is essential for predicting its radiation tolerance. Displacement cascades in SiC occur on picosecond timescales and create a mixture of defects, including Frenkel pairs and antisite defects. This task aims to characterise the primary damage in 3C‑SiC by simulating displacement cascades and quantifying the cascade dynamics, defect production, and clustering.

## Approach
Molecular dynamics (MD) simulations of displacement cascades in 3C‑SiC will be performed using a Tersoff-type interatomic potential. A perfect cubic SiC lattice will be thermalised at 300 K and then cascades initiated by imparting a kinetic energy to a randomly chosen Si atom (the primary knock-on atom, PKA) along a crystallographic direction. The simulations cover a range of damage energies from 0.25 to 30 keV, with system sizes increasing with energy and damping boundary conditions to mimic an infinite medium. The atomic trajectories are saved and analysed post-simulation to identify displaced atoms, vacancies, interstitials, and antisite defects. The mean-square displacement of displaced atoms is used to determine the cascade lifetime. Defect counts are combined with the Kinchin–Pease formula (using a weighted average displacement threshold energy of 22 eV) to compute defect production efficiency. The size distribution of interstitial clusters is obtained by grouping connected interstitials within the nearest-neighbour distance.

## Reproduction target
Run a suite of MD cascade simulations and produce the following outputs:

1. For a 10 keV Si PKA, compute and report the cascade lifetime in picoseconds.
2. For Si PKA at damage energies of 0.25, 0.5, 1, 5, 10, and 30 keV, report the total number of displacements and the defect production efficiency calculated as N_displacements / (0.4 * E_PKA / 22 eV). For the 10 keV cascades also report the ratio of C interstitials to Si interstitials.
3. Determine the maximum number of interstitials in any connected cluster observed across all simulations.

All outputs must be written to the specified files under `/app/outputs`.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- Tersoff potential parameters for 3C-SiC

## Workflow steps

### Step 1: Run MD cascade simulations
- Role: process
- Action: Perform molecular dynamics simulations of displacement cascades in 3C‑SiC using LAMMPS with a Tersoff potential. Create a periodic 3C‑SiC lattice at 300 K and initiate cascades by giving a randomly chosen Si atom a velocity corresponding to damage energies of 0.25, 0.5, 1, 5, 10, and 30 keV along crystallographic directions. Use system sizes appropriate to the energy (8000 atoms for low energies, up to 2 million atoms for 30 keV) with damping boundaries. Run at least 5 cascades per energy for energies ≥ 1 keV, and at least 15 for energies < 1 keV. Save atomic trajectories for subsequent analysis.
- Evidence: `/app/outputs/md_simulation_complete.log`

### Step 2: Compute cascade lifetime for 10 keV Si PKA
- Role: scored (load-bearing)
- Action: From the saved trajectory of one 10 keV Si PKA cascade, identify atoms displaced more than half the nearest‑neighbour distance from their lattice site. Compute the mean‑square displacement (MSD) of these atoms as a function of time and determine the cascade lifetime as the characteristic relaxation time (time after which MSD levels off). Write the lifetime in picoseconds to a text file.
- Output file: `/app/outputs/cascade_lifetime.txt`
- Format: txt
- Contract: A single non‑negative number on the first line, e.g., 0.15
- Scoring: scored by hidden verifier

### Step 3: Compute defect production efficiency and Frenkel pair ratio
- Role: scored (load-bearing)
- Action: For all Si PKA cascades at each damage energy (0.25, 0.5, 1, 5, 10, 30 keV), identify displaced atoms, vacancies, interstitials, and anti‑site defects after cascade relaxation. Count total displacements as the sum of Frenkel pairs and anti‑site defects. For each energy, compute defect production efficiency as N_displacements / (0.4 * E_PKA / E_d) using a weighted average displacement threshold energy E_d = 22 eV. For the 10 keV Si PKA cascades, report the ratio of C interstitials to Si interstitials. Output a JSON file summarising these per‑energy results.
- Output file: `/app/outputs/displacement_summary.json`
- Format: json
- Contract: { "0.25": {"total_displacements": <float>, "efficiency": <float>}, "0.5": {...}, "1": {...}, "5": {...}, "10": {"total_displacements": <float>, "efficiency": <float>, "ratio_C_Si_interstitials": <float>}, "30": {...} }
- Scoring: scored by hidden verifier

### Step 4: Report largest interstitial cluster size
- Role: scored (load-bearing)
- Action: From the defect identification in step 03, determine the largest interstitial cluster (connected group of interstitial atoms within nearest‑neighbour distance) observed across all cascades. Write the integer size (number of interstitials in that cluster) to a text file.
- Output file: `/app/outputs/cluster_summary.txt`
- Format: txt
- Contract: One non‑negative integer on the first line, e.g., 3
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cascade_lifetime.txt`
- `/app/outputs/displacement_summary.json`
- `/app/outputs/cluster_summary.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cascade_lifetime.txt
- path: `/app/outputs/cascade_lifetime.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Cascade lifetime determined from the mean‑square displacement relaxation time. A smaller lifetime indicates faster relaxation; the value must be less than or equal to a hidden gold threshold.
- schema:
  - `type`: text
  - `description`: A single non‑negative number (float) representing the cascade lifetime in picoseconds for a 10 keV Si PKA in 3C‑SiC.

### displacement_summary.json
- path: `/app/outputs/displacement_summary.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Per‑damage‑energy summary of total displacements, defect production efficiency, anti‑site defect fraction, and for 10 keV the C‑to‑Si interstitial ratio. The checker recomputes efficiency from total_displacements, checks monotonicity, anti‑site fraction range, and closeness to hidden references.
- schema:
  - `type`: object
  - `required`: `0.25`, `0.5`, `1`, `5`, `10`, `30`
  - `items`:
    - `0.25`:
      - `total_displacements`: float
      - `efficiency`: float
      - `anti_site_fraction`: float
    - `0.5`:
      - `total_displacements`: float
      - `efficiency`: float
      - `anti_site_fraction`: float
    - `1`:
      - `total_displacements`: float
      - `efficiency`: float
      - `anti_site_fraction`: float
    - `5`:
      - `total_displacements`: float
      - `efficiency`: float
      - `anti_site_fraction`: float
    - `10`:
      - `total_displacements`: float
      - `efficiency`: float
      - `anti_site_fraction`: float
      - `ratio_C_Si_interstitials`: float
    - `30`:
      - `total_displacements`: float
      - `efficiency`: float
      - `anti_site_fraction`: float

### cluster_summary.txt
- path: `/app/outputs/cluster_summary.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum interstitial cluster size. The value must be less than or equal to a hidden threshold (the paper's reported upper bound).
- schema:
  - `type`: text
  - `description`: A single non‑negative integer: the maximum number of interstitials in any cluster observed across all cascades. A smaller value indicates less clustering.

Notes: All energies listed must be simulated; omitting any under‑scopes the task. The anti_site_fraction is now reported for every energy; the verifier checks it lies within the paper's expected range and that efficiency values are monotonically decreasing.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cascade_lifetime.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single non‑negative number (float) representing the cascade lifetime in picoseconds for a 10 keV Si PKA in 3C‑SiC."
      },
      "description": "Cascade lifetime determined from the mean‑square displacement relaxation time. A smaller lifetime indicates faster relaxation; the value must be less than or equal to a hidden gold threshold."
    },
    {
      "file": "displacement_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "0.25",
          "0.5",
          "1",
          "5",
          "10",
          "30"
        ],
        "items": {
          "0.25": {
            "total_displacements": "float",
            "efficiency": "float",
            "anti_site_fraction": "float"
          },
          "0.5": {
            "total_displacements": "float",
            "efficiency": "float",
            "anti_site_fraction": "float"
          },
          "1": {
            "total_displacements": "float",
            "efficiency": "float",
            "anti_site_fraction": "float"
          },
          "5": {
            "total_displacements": "float",
            "efficiency": "float",
            "anti_site_fraction": "float"
          },
          "10": {
            "total_displacements": "float",
            "efficiency": "float",
            "anti_site_fraction": "float",
            "ratio_C_Si_interstitials": "float"
          },
          "30": {
            "total_displacements": "float",
            "efficiency": "float",
            "anti_site_fraction": "float"
          }
        }
      },
      "description": "Per‑damage‑energy summary of total displacements, defect production efficiency, anti‑site defect fraction, and for 10 keV the C‑to‑Si interstitial ratio. The checker recomputes efficiency from total_displacements, checks monotonicity, anti‑site fraction range, and closeness to hidden references."
    },
    {
      "file": "cluster_summary.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single non‑negative integer: the maximum number of interstitials in any cluster observed across all cascades. A smaller value indicates less clustering."
      },
      "description": "Maximum interstitial cluster size. The value must be less than or equal to a hidden threshold (the paper's reported upper bound)."
    }
  ],
  "notes": "All energies listed must be simulated; omitting any under‑scopes the task. The anti_site_fraction is now reported for every energy; the verifier checks it lies within the paper's expected range and that efficiency values are monotonically decreasing."
}
```

## How you are scored
A hidden verifier will independently assess each scored output. For `cascade_lifetime.txt` it checks whether the reported lifetime satisfies a hidden threshold; only a physically low value will earn full credit. For `displacement_summary.json` it recomputes the defect production efficiency from the reported displacement counts and verifies that the efficiencies decrease monotonically with increasing energy and that the 10 keV C‑to‑Si interstitial ratio falls within an expected range. For `cluster_summary.txt` it checks that the reported maximum cluster size does not exceed a hidden upper bound. The verifier combines these checks into a single reward. You must run the full simulation pipeline; reporting numbers that happen to be close to the paper’s own results is not sufficient if the underlying simulations were not carried out.
