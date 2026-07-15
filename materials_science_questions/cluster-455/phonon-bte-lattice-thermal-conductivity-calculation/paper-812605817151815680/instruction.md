# First-principles BTE thermal conductivity of wurtzite AlN

## Problem background
Wide-bandgap semiconductor materials with high thermal conductivity are critical for thermal management in high-power electronics. Aluminum nitride (AlN) is a promising candidate due to its intrinsically high phonon thermal conductivity, making it desirable for integration into devices as thin films. However, achieving bulk-like thermal conductivity in thin films is challenging because phonon transport can be severely degraded by defects, impurities, and boundary scattering. First-principles calculations based on the phonon Boltzmann transport equation (BTE) provide a benchmark for the intrinsic thermal conductivity of pristine AlN and the phonon mean free path spectrum, which are essential to understand the room-temperature bulk performance limit and to interpret experimental measurements. This task reproduces such a calculation: you will compute the thermal conductivity accumulation as a function of phonon mean free path for bulk wurtzite AlN at 300 K, providing reference data for both in-plane and cross-plane directions.

## Approach
The reproduction follows a standard first-principles workflow to solve the linearized phonon BTE. First, density functional theory (DFT) is used to relax the atomic positions of the wurtzite AlN unit cell and to compute harmonic (second-order) interatomic force constants via density functional perturbation theory (DFPT). Next, a supercell is constructed to calculate anharmonic (third-order) force constants using a finite-difference method, which captures three-phonon scattering processes. With the force constants, ShengBTE is employed to iteratively solve the linearized BTE on a phonon momentum grid, yielding phonon lifetimes, group velocities, and the cumulative thermal conductivity resolved by mean free path. Finally, post-processing extracts the accumulation curves (in-plane and cross-plane) and the asymptotic bulk conductivity values at 300 K. The entire procedure uses the open-source packages Quantum ESPRESSO and ShengBTE, together with standard pseudopotentials for Al and N.

## Reproduction target
Your goal is to produce two artifacts.

1. A CSV file `thermal_conductivity_accumulation.csv` containing the cumulative thermal conductivity (in W m⁻¹ K⁻¹) as a function of phonon mean free path (in µm) at 300 K for both in‑plane and cross‑plane directions, with at least 50 logarithmically spaced points spanning from 0.01 µm to 100 µm; the cumulative functions must be monotonically increasing.

2. A JSON file `bulk_kappa_300K.json` reporting the asymptotic bulk thermal conductivity values (in W m⁻¹ K⁻¹) for the in‑plane and cross‑plane directions at 300 K, extracted as the largest‑MFP accumulation values.

The outputs will be evaluated by a hidden verifier comparing them to independently derived reference data.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- ShengBTE: https://www.shengbte.net
- SSSP efficiency pseudopotentials for Al and N: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT relaxation and harmonic force constants
- Role: process
- Action: Using Quantum ESPRESSO: (1) relax the internal coordinates of the wurtzite AlN primitive cell (lattice parameters a=3.111 Å, c=4.979 Å, u=0.3821). (2) Perform a self‑consistent field (SCF) calculation with a suitable k‑point mesh. (3) Run DFPT to obtain the second‑order interatomic force constants (harmonic).
- Evidence: none

### Step 2: Third‑order force constants
- Role: process
- Action: Construct a supercell of the relaxed primitive cell. Use the finite‑difference approach (thirdorder.py from the ShengBTE package coupled with Quantum ESPRESSO) to compute the third‑order anharmonic force constants.
- Evidence: none

### Step 3: Solve phonon BTE
- Role: process
- Action: Run ShengBTE on a suitable q‑point grid to iteratively solve the linearized phonon BTE. This yields the phonon scattering rates, thermal conductivity tensor, and mean‑free‑path resolved contributions.
- Evidence: none

### Step 4: Generate thermal conductivity accumulation CSV
- Role: scored (load-bearing)
- Action: From the ShengBTE output, compute the cumulative thermal conductivity as a function of phonon mean free path (MFP) for both in‑plane and cross‑plane directions at 300 K. Select at least 50 MFP points logarithmically spaced from 0.01 µm to 100 µm. Ensure the accumulation functions are monotonic increasing. Write the data as a CSV file.
- Output file: `/app/outputs/thermal_conductivity_accumulation.csv`
- Format: csv
- Contract: Columns: mfp_um (float, mean free path in µm), kappa_in_plane (float, cumulative in-plane thermal conductivity in W/m·K), kappa_cross_plane (float, cumulative cross-plane thermal conductivity in W/m·K). At least 50 rows, monotonically increasing values.
- Scoring: scored by hidden verifier

### Step 5: Generate bulk thermal conductivity JSON
- Role: scored
- Action: Extract the asymptotic bulk thermal conductivity values at 300 K for the in‑plane and cross‑plane directions (largest MFP points). Write them as a JSON object.
- Output file: `/app/outputs/bulk_kappa_300K.json`
- Format: json
- Contract: Keys: kappa_in_plane_300K (float, W/m·K), kappa_cross_plane_300K (float, W/m·K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity_accumulation.csv`
- `/app/outputs/bulk_kappa_300K.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity_accumulation.csv
- path: `/app/outputs/thermal_conductivity_accumulation.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Thermal conductivity accumulation as a function of phonon mean free path at 300 K; at least 50 points, monotonic increasing. Evaluated with threshold-or-better: meeting or exceeding the hidden reference earns full credit; lower values reduce score proportionally to deficit.
- schema:
  - `type`: table
  - `required_columns`: `mfp_um`, `kappa_in_plane`, `kappa_cross_plane`
  - `units`:
    - `mfp_um`: µm
    - `kappa_in_plane`: W/(m·K)
    - `kappa_cross_plane`: W/(m·K)

### bulk_kappa_300K.json
- path: `/app/outputs/bulk_kappa_300K.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Bulk thermal conductivity of pristine wurtzite AlN at 300 K, extracted from the asymptotic accumulation. Evaluated with threshold-or-better: meeting or exceeding the hidden reference earns full credit.
- schema:
  - `type`: object
  - `required`:
    - `kappa_in_plane_300K`: number
    - `kappa_cross_plane_300K`: number
  - `units`:
    - `kappa_in_plane_300K`: W/(m·K)
    - `kappa_cross_plane_300K`: W/(m·K)

Notes: The accumulation CSV is the primary scored artifact. The bulk JSON is a compact summary. Both use threshold-or-better scoring: exceeding the paper's reference is not penalized; the reward degrades only for values below the threshold. The checker is being updated concurrently to implement directional threshold comparison for the CSV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity_accumulation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "mfp_um",
          "kappa_in_plane",
          "kappa_cross_plane"
        ],
        "units": {
          "mfp_um": "µm",
          "kappa_in_plane": "W/(m·K)",
          "kappa_cross_plane": "W/(m·K)"
        }
      },
      "description": "Thermal conductivity accumulation as a function of phonon mean free path at 300 K; at least 50 points, monotonic increasing. Evaluated with threshold-or-better: meeting or exceeding the hidden reference earns full credit; lower values reduce score proportionally to deficit."
    },
    {
      "file": "bulk_kappa_300K.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "kappa_in_plane_300K": "number",
          "kappa_cross_plane_300K": "number"
        },
        "units": {
          "kappa_in_plane_300K": "W/(m·K)",
          "kappa_cross_plane_300K": "W/(m·K)"
        }
      },
      "description": "Bulk thermal conductivity of pristine wurtzite AlN at 300 K, extracted from the asymptotic accumulation. Evaluated with threshold-or-better: meeting or exceeding the hidden reference earns full credit."
    }
  ],
  "notes": "The accumulation CSV is the primary scored artifact. The bulk JSON is a compact summary. Both use threshold-or-better scoring: exceeding the paper's reference is not penalized; the reward degrades only for values below the threshold. The checker is being updated concurrently to implement directional threshold comparison for the CSV."
}
```

## How you are scored
A hidden verifier will inspect your outputs. For the accumulation CSV, it will check that the file has the required columns, at least 50 rows, and that both `kappa_in_plane` and `kappa_cross_plane` increase monotonically. It will then compare your cumulative conductivity values at a set of prescribed mean free paths to a hidden reference. For the bulk JSON, it will compare your reported in‑plane and cross‑plane conductivities to a hidden reference. The scoring function is designed so that if your conductivities meet or exceed the reference (i.e., are higher, indicating better performance), you are not penalized; only significantly lower values reduce the score. The final reward is a weighted combination of both artifacts, with the accumulation CSV being the primary contributor.
