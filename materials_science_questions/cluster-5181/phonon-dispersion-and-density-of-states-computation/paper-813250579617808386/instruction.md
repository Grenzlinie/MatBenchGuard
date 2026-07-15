# Laser-induced thermal phonon squeezing in silicon: RMS displacement and peak analysis

## Problem background
When an intense femtosecond laser pulse irradiates a semiconductor such as silicon, the electrons are rapidly heated to several thousand kelvin while the lattice remains cold. This nonthermal state can drastically modify interatomic forces before any significant atomic motion occurs, leading to transient structural transformations. At absorbed fluences below the melting threshold, the sudden softening of bonds can induce a periodic variation in the width of the atomic displacement distribution — an effect known as thermal phonon squeezing. Understanding this oscillatory collective motion is crucial because it may reveal early-stage atomic pathways that precede nonthermal melting. This task reproduces the thermal squeezing signature by computing the time-dependent root‑mean‑square atomic displacement and associated squeezing metrics for a silicon crystal excited to a specific electronic temperature.

## Approach
The reproduction employs electronic‑temperature‑dependent density‑functional‑theory molecular dynamics to simulate the ultrafast response of a 96‑atom diamond‑structure silicon supercell. The workflow first determines the harmonic phonon modes of the system in its ground state and in the excited state corresponding to an electronic temperature of 50 mhartree via finite‑displacement calculations. Using the ground‑state eigenvectors, atomic positions and velocities are initialised by inverse‑transform sampling from a Maxwell–Boltzmann distribution at a lattice temperature of 316 K (1 mhartree). The supercell is then instantaneously promoted to the excited‑state potential and evolved microcanonically with a 2 fs timestep for at least 200 fs. All forces are obtained from a DFT code that supports Fermi–Dirac smearing at the given electronic temperature. From the trajectory, the time series of the root‑mean‑square atomic displacement is computed, and the key indicators of thermal squeezing — the time of the first maximum of the RMS displacement and the ratios of the mean‑square displacement extremes to the zero‑point variance of the excited potential — are extracted. The entire procedure uses open‑source tools and the publicly known crystal structure of silicon.

## Reproduction target
Produce two scored artifacts for the 50 mhartree case:
1. `rms_displacement_50mH.csv` — a time series of the root‑mean‑square atomic displacement (Å) averaged over all 96 atoms, sampled every 2 fs for the first 200 fs. The file must contain columns `time_fs`, `rms_displacement_AA`, and a constant column `zero_point_variance_AA2` (the excited‑state zero‑point variance) to serve as a reference. The RMS displacement must display oscillatory behaviour with at least one clear maximum followed by a decrease within the recorded time window.
2. `peak_and_variance.json` — a JSON object containing the floating‑point keys `peak_time_fs_50mH` (the time of the first RMS displacement maximum in the first 200 fs), `zero_point_variance_AA2` (the quantum zero‑point variance of the excited‑state potential in Å²), `variance_min_ratio_50mH`, and `variance_max_ratio_50mH` (the minimum and maximum mean‑square displacement divided by the zero‑point variance).

## Assets

- CP2K (open-source DFT code): https://www.cp2k.org
- Python scientific computing packages: numpy scipy matplotlib

## Workflow steps

### Step 1: Phonon frequency calculation (ground and excited state)
- Role: process
- Action: Perform DFT phonon calculations for a 96‑atom diamond silicon supercell using the finite‑displacement method. Compute the dynamical matrix and obtain orthonormal eigenvectors and eigenfrequencies for (i) the ground state (no electronic smearing) and (ii) the laser‑excited state at an electronic temperature of 50 mhartree.
- Evidence: `/app/outputs/phonon_frequencies.json`

### Step 2: Initialize atomic velocities and displacements
- Role: process
- Action: Using the ground‑state phonon eigenvectors and frequencies, sample atomic velocities and displacements from a Maxwell–Boltzmann distribution at a lattice temperature of 1 mhartree (316 K) via inverse transform sampling. Generate a set of initial atomic configurations and velocities.
- Evidence: `/app/outputs/initial_positions.xyz`

### Step 3: Ab initio molecular dynamics at 50 mhartree
- Role: process
- Action: Run a microcanonical (NVE) molecular dynamics simulation for the 96‑atom Si supercell instantaneously excited to an electronic temperature of 50 mhartree. Use a 2 fs timestep and total simulation time of at least 200 fs. Employ electronic‑temperature‑dependent DFT with Fermi–Dirac smearing at 50 mhartree. Record atomic coordinates every timestep.
- Evidence: `/app/outputs/md_trajectory.xyz`

### Step 4: Compute RMS displacement time series
- Role: scored (load-bearing)
- Action: From the recorded MD trajectory, compute the root‑mean‑square atomic displacement from equilibrium positions as a function of time (averaged over all atoms). Output a CSV file with columns time_fs, rms_displacement_AA, and zero_point_variance_AA2 (constant column from excited‑state phonons).
- Output file: `/app/outputs/rms_displacement_50mH.csv`
- Format: csv
- Contract: CSV with columns: time_fs (float, time in femtoseconds), rms_displacement_AA (float, √⟨u²⟩ in Å), zero_point_variance_AA2 (float, constant zero-point variance in Å²).
- Scoring: scored by hidden verifier

### Step 5: Peak time and zero‑point variance ratio
- Role: scored (load-bearing)
- Action: From the RMS displacement time series and the excited‑state phonon frequencies, determine the time of the first maximum of the RMS displacement within the first 200 fs (peak time). Compute the quantum zero‑point variance ⟨u²⟩₀ = (1/Nm) Σ ℏ/(2ωᵢ) using the excited‑state phonon frequencies. For the mean‑square displacement ⟨u²⟩ time series, identify its minimum and maximum values within the first 200 fs and calculate their ratios to the zero‑point variance. Save a JSON object containing peak_time_fs_50mH, zero_point_variance_AA2, variance_min_ratio_50mH, variance_max_ratio_50mH.
- Output file: `/app/outputs/peak_and_variance.json`
- Format: json
- Contract: JSON object with keys: peak_time_fs_50mH (float), zero_point_variance_AA2 (float), variance_min_ratio_50mH (float), variance_max_ratio_50mH (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rms_displacement_50mH.csv`
- `/app/outputs/peak_and_variance.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rms_displacement_50mH.csv
- path: `/app/outputs/rms_displacement_50mH.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time series of root‑mean‑square atomic displacement; structural check verifies existence of oscillatory behaviour (a clear maximum followed by a decrease).
- schema:
  - `type`: table
  - `required_columns`: `time_fs`, `rms_displacement_AA`, `zero_point_variance_AA2`
  - `units`:
    - `time_fs`: femtosecond
    - `rms_displacement_AA`: angstrom
    - `zero_point_variance_AA2`: angstrom^2

### peak_and_variance.json
- path: `/app/outputs/peak_and_variance.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reported squeezing metrics: peak time of RMS displacement and variance ratios relative to quantum zero‑point variance. Checker compares against paper‑reported values within generous tolerances.
- schema:
  - `type`: object
  - `required`: `peak_time_fs_50mH`, `variance_min_ratio_50mH`, `variance_max_ratio_50mH`
  - `items`:
    - `peak_time_fs_50mH`: float
    - `variance_min_ratio_50mH`: float
    - `variance_max_ratio_50mH`: float
    - `zero_point_variance_AA2`: float
  - `units`:
    - `peak_time_fs_50mH`: femtosecond
    - `variance_min_ratio_50mH`: dimensionless
    - `variance_max_ratio_50mH`: dimensionless
    - `zero_point_variance_AA2`: angstrom^2

Notes: The task focuses on the 50 mhartree electronic temperature case. Additional electronic temperatures may be computed optionally. The RMS displacement CSV must exhibit oscillatory behaviour; the peak and variance ratios must fall within experimentally motivated tolerances to account for code and stochastic differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rms_displacement_50mH.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_fs",
          "rms_displacement_AA",
          "zero_point_variance_AA2"
        ],
        "units": {
          "time_fs": "femtosecond",
          "rms_displacement_AA": "angstrom",
          "zero_point_variance_AA2": "angstrom^2"
        }
      },
      "description": "Time series of root‑mean‑square atomic displacement; structural check verifies existence of oscillatory behaviour (a clear maximum followed by a decrease)."
    },
    {
      "file": "peak_and_variance.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "peak_time_fs_50mH",
          "variance_min_ratio_50mH",
          "variance_max_ratio_50mH"
        ],
        "items": {
          "peak_time_fs_50mH": "float",
          "variance_min_ratio_50mH": "float",
          "variance_max_ratio_50mH": "float",
          "zero_point_variance_AA2": "float"
        },
        "units": {
          "peak_time_fs_50mH": "femtosecond",
          "variance_min_ratio_50mH": "dimensionless",
          "variance_max_ratio_50mH": "dimensionless",
          "zero_point_variance_AA2": "angstrom^2"
        }
      },
      "description": "Reported squeezing metrics: peak time of RMS displacement and variance ratios relative to quantum zero‑point variance. Checker compares against paper‑reported values within generous tolerances."
    }
  ],
  "notes": "The task focuses on the 50 mhartree electronic temperature case. Additional electronic temperatures may be computed optionally. The RMS displacement CSV must exhibit oscillatory behaviour; the peak and variance ratios must fall within experimentally motivated tolerances to account for code and stochastic differences."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that has access to reference data derived from the original experiment. The verifier independently reads `peak_and_variance.json` and checks whether the reported peak time and variance ratios fall inside tolerance bands determined by expected numerical dispersion. It also inspects `rms_displacement_50mH.csv` for the required oscillatory shape (structural check). These checks are weighted and combined into a single reward score; the peak and variance metrics carry the majority of the weight. You do not need to hit a single exact number — the accepted bands are wide enough to accommodate different DFT implementations and stochastic noise — but a result that lacks the oscillatory signature or lies far outside the physically plausible range will receive a low or zero reward.
