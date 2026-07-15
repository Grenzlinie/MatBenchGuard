# Monte Carlo simulation of hydrogen implantation in amorphous silicon and hydrogenated amorphous silicon

## Problem background
Hydrogen implantation into amorphous silicon (a-Si) and hydrogenated amorphous silicon (a-Si:H) at low energies (below 1 keV) is central to plasma CVD processes and nanoscale depth profiling of impurities. Predicting the depth distribution of implanted atoms — specifically the mean projected range (MPR) and the standard deviation (Sigma) of the range distribution — is needed for process design. Monte Carlo simulations can compute these quantities from first principles using scattering cross sections and energy loss models.

## Approach
The simulation follows the trajectory of an incident hydrogen atom moving in straight segments through an amorphous target. After each segment the atom undergoes an elastic nuclear scattering event; the scattering angle is sampled from the universal scattering cross section (Kalbitzer–Oetzmann) and the azimuthal angle is chosen uniformly. Continuous inelastic electronic energy loss is applied along each segment using the corrected Lindhard–Scharff formula, with Bragg mixing for targets containing both Si and H. Mean free paths are determined by the atom number density and the hydrogen concentration, and collision partners are selected by weighted random choice. The simulation terminates when the atom’s energy falls below a threshold or the atom leaves the target surface. Simulations are run for pure a-Si and for a-Si:H with specified hydrogen concentrations over a range of incident energies. From the final projected depths of many trajectories, the mean projected range and standard deviation are computed for each condition, and the ratio Sigma/MPR is examined for pure a-Si.

## Reproduction target
Compute the mean projected range (MPR) and standard deviation (Sigma) of the depth distribution for hydrogen atoms implanted into: (i) pure amorphous silicon (a-Si) at incident energies 15, 30, 50, 100, 200, 500, 1000 eV; (ii) a-Si:H with hydrogen concentration 30 at.% (c=0.3) at the same seven energies; (iii) a-Si:H at a fixed incident energy of 1000 eV with hydrogen concentrations c=0.1 and 0.2. For each condition, record the final depth of at least 10,000 trajectories as a JSON Lines file. Then aggregate the results into a CSV table of MPR and Sigma per (energy, concentration) condition, and produce a separate CSV table of the Sigma/MPR ratio as a function of energy for a-Si. The reproducibility check will rely on recomputing statistics from the raw trajectory files, so both the raw files and the aggregated tables must be submitted.

## Assets

- Kalbitzer–Oetzmann universal scattering cross section: https://doi.org/10.1080/00337578008209276
- Lindhard–Scharff electronic stopping theory: https://doi.org/10.1103/PhysRev.124.128
- NumPy: numpy
- SciPy (optional): scipy

## Workflow steps

### Step 1: Implement Monte Carlo simulation code
- Role: process
- Action: Implement a Monte Carlo simulation of hydrogen atom implantation in amorphous targets. The code must model: (i) straight-line motion between discrete elastic nuclear collisions with continuous inelastic electronic energy loss; (ii) nuclear elastic scattering using the universal Kalbitzer–Oetzmann cross section, with total nuclear cross section N^{-2/3} and maximum scattering angle π; (iii) scattering angle θ sampled via the normalized integral equation using a uniform random number, and azimuthal angle φ=2πR; (iv) mean free paths: total λ_T = N^{-1/3}, and species-resolved mean free paths λ_Si = λ_T/(1-c) and λ_H = λ_T/c; (v) collision partner selected by a random number, and individual free path S = -λ_T ln(R); (vi) continuous inelastic energy loss along each segment using the corrected Lindhard–Scharff form Se = C K_LS √E, with Bragg mixing for mixed-composition targets; (vii) termination when H atom energy falls below 0.5 eV or the atom exits the target surface. Use atom number density N = 5×10^20 cm⁻³, correction factors C=1.38 for Si and C=1.0 for H.
- Evidence: `/app/outputs/implementation_report.txt`

### Step 2: Run simulation for pure amorphous silicon (a-Si)
- Role: scored (load-bearing)
- Action: Using the Monte Carlo code, simulate hydrogen implantation into pure amorphous silicon (c=0) at incident energies: 15, 30, 50, 100, 200, 500, 1000 eV. For each energy, run at least 10,000 trajectories and record the final projected depth of each implanted atom. Write a JSON Lines file where each line is a JSON object with keys 'energy' (float, eV) and 'depth' (float, angstrom).
- Output file: `/app/outputs/trajectories_aSi.jsonl`
- Format: other
- Contract: A text file with one JSON object per line. Required keys per object: energy (float, eV), depth (float, angstrom).
- Scoring: scored by hidden verifier

### Step 3: Run simulation for hydrogenated amorphous silicon (a-Si:H, 30% H)
- Role: scored (load-bearing)
- Action: Simulate hydrogen implantation into a-Si:H with H atomic concentration c=0.3 at the same seven energies as step 2: 15, 30, 50, 100, 200, 500, 1000 eV. For each energy, run at least 10,000 trajectories and output a JSON Lines file with keys 'energy' and 'depth'.
- Output file: `/app/outputs/trajectories_aSiH30.jsonl`
- Format: other
- Contract: Same schema as step 2: JSON Lines, keys 'energy' (eV) and 'depth' (angstrom).
- Scoring: scored by hidden verifier

### Step 4: Run concentration sweep at 1000 eV
- Role: scored (load-bearing)
- Action: Simulate at a fixed incident energy of 1000 eV for hydrogen concentrations c = 0.1 and 0.2. For each concentration, run at least 10,000 trajectories and record final depths. Output a JSON Lines file with keys 'energy', 'concentration', 'depth'.
- Output file: `/app/outputs/trajectories_concsweep.jsonl`
- Format: other
- Contract: JSON Lines: {"energy": 1000.0, "concentration": <float>, "depth": <float>}. energy in eV, concentration in at% (e.g., 0.1, 0.2), depth in angstrom.
- Scoring: scored by hidden verifier

### Step 5: Compute summary statistics (MPR and Sigma)
- Role: scored
- Action: From the trajectory data produced in steps 2–4, compute for each unique (energy, concentration) condition the mean projected range (MPR) and standard deviation (Sigma) of the depth distribution. Output a CSV file with columns: energy (eV), concentration (at%), mpr (angstrom), sigma (angstrom).
- Output file: `/app/outputs/simulation_summary.csv`
- Format: csv
- Contract: CSV table with header: energy,concentration,mpr,sigma. energy: float (eV); concentration: float (at%); mpr: float (angstrom); sigma: float (angstrom).
- Scoring: scored by hidden verifier

### Step 6: Compute Sigma/MPR ratio for a-Si
- Role: scored
- Action: For the a-Si simulation results (concentration=0), compute the ratio Sigma/MPR at each incident energy. Output a CSV file with columns: energy (eV), ratio (dimensionless).
- Output file: `/app/outputs/ratio_aSi.csv`
- Format: csv
- Contract: CSV table with header: energy,ratio. energy: float (eV); ratio: float (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/trajectories_aSi.jsonl`
- `/app/outputs/trajectories_aSiH30.jsonl`
- `/app/outputs/trajectories_concsweep.jsonl`
- `/app/outputs/simulation_summary.csv`
- `/app/outputs/ratio_aSi.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### trajectories_aSi.jsonl
- path: `/app/outputs/trajectories_aSi.jsonl`
- format: other
- purpose: scored
- target_policy: metric_recompute
- description: Per-trajectory final depths for a-Si simulation. Used by checker to recompute MPR and Sigma.
- schema:
  - `type`: text
  - `description`: Each line is a JSON object with keys: energy (float, eV), depth (float, angstrom).

### trajectories_aSiH30.jsonl
- path: `/app/outputs/trajectories_aSiH30.jsonl`
- format: other
- purpose: scored
- target_policy: metric_recompute
- description: Per-trajectory final depths for a-Si:H (30% H) simulation.
- schema:
  - `type`: text
  - `description`: Each line is a JSON object with keys: energy (float, eV), depth (float, angstrom).

### trajectories_concsweep.jsonl
- path: `/app/outputs/trajectories_concsweep.jsonl`
- format: other
- purpose: scored
- target_policy: metric_recompute
- description: Per-trajectory final depths for concentration sweep at 1000 eV.
- schema:
  - `type`: text
  - `description`: Each line is a JSON object with keys: energy (float, eV), concentration (float, at%), depth (float, angstrom).

### simulation_summary.csv
- path: `/app/outputs/simulation_summary.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Aggregated mean projected range and standard deviation for all conditions.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `concentration`, `mpr`, `sigma`
  - `units`:
    - `energy`: eV
    - `concentration`: at%
    - `mpr`: angstrom
    - `sigma`: angstrom

### ratio_aSi.csv
- path: `/app/outputs/ratio_aSi.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Ratio Sigma/MPR for a-Si as function of energy, used to check approximate constancy.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `ratio`
  - `units`:
    - `energy`: eV
    - `ratio`: dimensionless

Notes: All scored outputs must be present under /app/outputs. The raw trajectory files allow the checker to recompute MPR and Sigma directly, ensuring fidelity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "trajectories_aSi.jsonl",
      "format": "other",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Each line is a JSON object with keys: energy (float, eV), depth (float, angstrom)."
      },
      "description": "Per-trajectory final depths for a-Si simulation. Used by checker to recompute MPR and Sigma."
    },
    {
      "file": "trajectories_aSiH30.jsonl",
      "format": "other",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Each line is a JSON object with keys: energy (float, eV), depth (float, angstrom)."
      },
      "description": "Per-trajectory final depths for a-Si:H (30% H) simulation."
    },
    {
      "file": "trajectories_concsweep.jsonl",
      "format": "other",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Each line is a JSON object with keys: energy (float, eV), concentration (float, at%), depth (float, angstrom)."
      },
      "description": "Per-trajectory final depths for concentration sweep at 1000 eV."
    },
    {
      "file": "simulation_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "concentration",
          "mpr",
          "sigma"
        ],
        "units": {
          "energy": "eV",
          "concentration": "at%",
          "mpr": "angstrom",
          "sigma": "angstrom"
        }
      },
      "description": "Aggregated mean projected range and standard deviation for all conditions."
    },
    {
      "file": "ratio_aSi.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "ratio"
        ],
        "units": {
          "energy": "eV",
          "ratio": "dimensionless"
        }
      },
      "description": "Ratio Sigma/MPR for a-Si as function of energy, used to check approximate constancy."
    }
  ],
  "notes": "All scored outputs must be present under /app/outputs. The raw trajectory files allow the checker to recompute MPR and Sigma directly, ensuring fidelity."
}
```

## How you are scored
Each scored artifact is evaluated independently by a hidden verifier. For the raw trajectory files the verifier regroups depths by condition and recomputes the mean projected range and standard deviation; those recomputed values are compared against reference values from the original work, with tolerances that account for statistical noise. The summary table and ratio table are cross-checked against both the recomputed statistics and the reference values. A weighted score is produced across all artifacts. Simply printing the expected numbers without producing the correct raw trajectories will not pass. The verifier also checks that the Sigma/MPR ratio for a-Si is approximately constant across the energy range.
