# Critical Decay Exponents from Random Transverse-Field Ising Spin Chain Simulations

## Problem background
The random transverse-field Ising chain is a canonical model for studying the effects of quenched disorder on quantum phase transitions. Unlike clean systems, disorder can drastically alter critical properties, leading to exotic, non‑power‑law correlations. This task focuses on the quantum critical point of the one‑dimensional model, where the average couplings and fields are equal. At this point, the spin‑spin and energy‑energy autocorrelation functions display unusual dynamical scaling that reflects the dominance of rare regions. The goal is to compute these autocorrelation functions and extract the characteristic decay behaviour, thereby gaining insight into the universal critical dynamics of disordered quantum systems.

## Approach
The random transverse‑field Ising chain is mapped to a system of free fermions via a Jordan‑Wigner transformation. For each disorder realization (with random couplings and fields taken from a binary or uniform distribution at the critical point), the resulting single‑particle Hamiltonian (a \(2L \times 2L\) matrix) is diagonalized. The imaginary‑time spin (σˣ) and energy (σᶻ) autocorrelation functions are then computed at the central (bulk) and surface sites using the fermion representation and Wick’s theorem. Disorder averages are accumulated over a large number of independent realizations to obtain the mean correlation functions. The agent implements this procedure for system sizes up to \(L=64\) and outputs the averaged autocorrelations as functions of imaginary time τ.

## Reproduction target
Produce four CSV files in the output directory containing the disorder‑averaged imaginary‑time autocorrelation functions:
- `bulk_spin_autocorr.csv`: τ and bulk spin autocorrelation G_bulk
- `surface_spin_autocorr.csv`: τ and surface spin autocorrelation G_surf
- `bulk_energy_autocorr.csv`: τ and bulk energy autocorrelation G_bulk_e
- `surface_energy_autocorr.csv`: τ and surface energy autocorrelation G_surf_e

Each file must have two columns (tau, correlation) with τ increasing monotonically. The data should be generated from an ensemble of at least 5000 disorder realizations with system size \(L \ge 64\). The agent does not need to perform any analysis of the decay exponents; that is done by the verifier.

## Assets

- Python scientific computing environment (NumPy, SciPy, Matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: Simulate and disorder-average autocorrelation functions
- Role: process
- Action: Generate at least 5000 disorder realizations of the random transverse-field Ising chain at the critical point (e.g., binary or uniform distribution of couplings and fields with h0=1). For system sizes up to L=64, map to free fermions via Jordan-Wigner, diagonalize the resulting 2L×2L matrix, and compute the imaginary-time spin autocorrelation (σ^x) and energy autocorrelation (σ^z) at the central site (bulk) and surface site (l=1). Accumulate and average the correlations over all realizations.
- Evidence: none

### Step 2: Output bulk spin autocorrelation
- Role: scored (load-bearing)
- Action: Write the disorder-averaged bulk spin autocorrelation function to a CSV file with columns tau and G_bulk.
- Output file: `/app/outputs/bulk_spin_autocorr.csv`
- Format: csv
- Contract: Columns: tau (float, imaginary time), G_bulk (float, disorder-averaged bulk spin autocorrelation).
- Scoring: scored by hidden verifier

### Step 3: Output surface spin autocorrelation
- Role: scored
- Action: Write the disorder-averaged surface spin autocorrelation function to a CSV file with columns tau and G_surf.
- Output file: `/app/outputs/surface_spin_autocorr.csv`
- Format: csv
- Contract: Columns: tau (float), G_surf (float, disorder-averaged surface spin autocorrelation).
- Scoring: scored by hidden verifier

### Step 4: Output bulk energy autocorrelation
- Role: scored
- Action: Write the disorder-averaged bulk energy autocorrelation function to a CSV file with columns tau and G_bulk_e.
- Output file: `/app/outputs/bulk_energy_autocorr.csv`
- Format: csv
- Contract: Columns: tau (float), G_bulk_e (float, disorder-averaged bulk energy autocorrelation).
- Scoring: scored by hidden verifier

### Step 5: Output surface energy autocorrelation
- Role: scored
- Action: Write the disorder-averaged surface energy autocorrelation function to a CSV file with columns tau and G_surf_e.
- Output file: `/app/outputs/surface_energy_autocorr.csv`
- Format: csv
- Contract: Columns: tau (float), G_surf_e (float, disorder-averaged surface energy autocorrelation).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_spin_autocorr.csv`
- `/app/outputs/surface_spin_autocorr.csv`
- `/app/outputs/bulk_energy_autocorr.csv`
- `/app/outputs/surface_energy_autocorr.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_spin_autocorr.csv
- path: `/app/outputs/bulk_spin_autocorr.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Disorder-averaged bulk spin autocorrelation function in imaginary time.
- schema:
  - `type`: table
  - `required_columns`: `tau`, `G_bulk`
  - `columns`:
    - `tau`: float, monotonically increasing imaginary time
    - `G_bulk`: float, disorder-averaged bulk spin autocorrelation [<σ_{L/2}^x(τ)σ_{L/2}^x>]_av

### surface_spin_autocorr.csv
- path: `/app/outputs/surface_spin_autocorr.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Disorder-averaged surface spin autocorrelation function in imaginary time.
- schema:
  - `type`: table
  - `required_columns`: `tau`, `G_surf`
  - `columns`:
    - `tau`: float, monotonically increasing imaginary time
    - `G_surf`: float, disorder-averaged surface spin autocorrelation [<σ_{1}^x(τ)σ_{1}^x>]_av

### bulk_energy_autocorr.csv
- path: `/app/outputs/bulk_energy_autocorr.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Disorder-averaged bulk energy autocorrelation function in imaginary time.
- schema:
  - `type`: table
  - `required_columns`: `tau`, `G_bulk_e`
  - `columns`:
    - `tau`: float, monotonically increasing imaginary time
    - `G_bulk_e`: float, disorder-averaged bulk energy autocorrelation [<σ_{L/2}^z(τ)σ_{L/2}^z>]_av

### surface_energy_autocorr.csv
- path: `/app/outputs/surface_energy_autocorr.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Disorder-averaged surface energy autocorrelation function in imaginary time.
- schema:
  - `type`: table
  - `required_columns`: `tau`, `G_surf_e`
  - `columns`:
    - `tau`: float, monotonically increasing imaginary time
    - `G_surf_e`: float, disorder-averaged surface energy autocorrelation [<σ_{1}^z(τ)σ_{1}^z>]_av

Notes: All CSV files are produced by the solving agent's simulation and disorder averaging. The hidden checker will perform separate regression analyses on each file to verify the predicted scaling forms (logarithmic for spin, power-law for energy) without relying on any self-reported metrics.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_spin_autocorr.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "tau",
          "G_bulk"
        ],
        "columns": {
          "tau": "float, monotonically increasing imaginary time",
          "G_bulk": "float, disorder-averaged bulk spin autocorrelation [<σ_{L/2}^x(τ)σ_{L/2}^x>]_av"
        }
      },
      "description": "Disorder-averaged bulk spin autocorrelation function in imaginary time."
    },
    {
      "file": "surface_spin_autocorr.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "tau",
          "G_surf"
        ],
        "columns": {
          "tau": "float, monotonically increasing imaginary time",
          "G_surf": "float, disorder-averaged surface spin autocorrelation [<σ_{1}^x(τ)σ_{1}^x>]_av"
        }
      },
      "description": "Disorder-averaged surface spin autocorrelation function in imaginary time."
    },
    {
      "file": "bulk_energy_autocorr.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "tau",
          "G_bulk_e"
        ],
        "columns": {
          "tau": "float, monotonically increasing imaginary time",
          "G_bulk_e": "float, disorder-averaged bulk energy autocorrelation [<σ_{L/2}^z(τ)σ_{L/2}^z>]_av"
        }
      },
      "description": "Disorder-averaged bulk energy autocorrelation function in imaginary time."
    },
    {
      "file": "surface_energy_autocorr.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "tau",
          "G_surf_e"
        ],
        "columns": {
          "tau": "float, monotonically increasing imaginary time",
          "G_surf_e": "float, disorder-averaged surface energy autocorrelation [<σ_{1}^z(τ)σ_{1}^z>]_av"
        }
      },
      "description": "Disorder-averaged surface energy autocorrelation function in imaginary time."
    }
  ],
  "notes": "All CSV files are produced by the solving agent's simulation and disorder averaging. The hidden checker will perform separate regression analyses on each file to verify the predicted scaling forms (logarithmic for spin, power-law for energy) without relying on any self-reported metrics."
}
```

## How you are scored
A hidden verifier will independently inspect each of the four CSV outputs. For each artifact, the verifier will check that the data is physically reasonable and consistent with the expected universal scaling behaviour. It will compare the correlation curves to hidden reference models using regression analysis, assigning a per‑artifact score between 0 and 1 based on hidden tolerances. The final reward is the average of the four scores, so all four outputs contribute equally. Merely reporting the correct numbers without the correct underlying data will not achieve a high score.
