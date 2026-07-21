# Monte Carlo Hysteresis Coercivity of AFM-FM Bilayers

## Problem background
Permanent magnet design seeks rare-earth-free materials with both high saturation magnetization and coercivity. One promising strategy is to couple a ferromagnet (FM) to an antiferromagnet (AFM) via interface exchange, with the goal of enhancing coercivity. Monte Carlo simulations are used to study an anisotropic Heisenberg AFM-FM bilayer system and determine how coercivity depends on AFM Néel temperature, anisotropy, interface coupling strength, AFM volume fraction, and temperature, guiding material selection for composite magnets.

## Approach
The simulation is based on a Heisenberg model with nearest-neighbor exchange within each subsystem, uniaxial anisotropy along the in-plane x-axis, Zeeman coupling, and an interface exchange term at the AFM-FM boundary. The lattice is body-centered cubic with periodic boundary conditions in-plane and free surfaces along the z-direction. Hysteresis loops are simulated by sweeping the external field from positive saturation to a negative extreme and back, using single-spin-flip Metropolis updates with cone trial moves. Coercivity Hc is extracted from the demagnetizing branch as the field at which the magnetization crosses zero. To account for the stochastic nature of the switching, 20 independent field scans with different random seeds are performed per condition, yielding a mean Hc and its standard deviation. The bilayer system is compared against a homogeneous FM system of the same total dimensions, keeping all FM parameters identical, to isolate the AFM contribution.

## Reproduction target
Produce a CSV file `/app/outputs/coercivity_results.csv` containing the coercivity Hc and its standard deviation for each condition in the following parameter sweeps. All simulations use a 20×20 in-plane lattice, FM parameters J_FM = 0.035 eV, K_FM = 8×10⁻⁵ eV, μ_FM = 2.5 μ_B, and μ_AF = 1.0 μ_B.

- Sweep 1 (AFM anisotropy & interface coupling): vary K_AF from 0.2 to 1.0 meV in steps of 0.2 meV, for J_INT = 1, 5, 10, 20 meV, with J_AF = -30 meV, T = 300 K.
- Sweep 2 (AFM exchange / Néel temperature): vary J_AF ∈ { -30, -20, -15, -10 } meV, with J_INT = 10 meV, K_AF = 0.5 meV, T = 300 K.
- Sweep 3 (AFM thickness): vary the number of AFM layers from 1 to 24 (FM fixed at 20 layers) with J_AF = -30 meV, K_AF = 0.1 meV, J_INT = 10 meV, T = 300 K. For each AFM thickness, also compute a homogeneous FM system of size 20×20×(20 + AFM_layers) with the same FM parameters.
- Sweep 4 (temperature): vary T from 275 to 475 K in steps of 50 K, with J_AF = -30 meV, K_AF = 0.2 meV, J_INT = 10 meV. For each temperature, also compute a homogeneous FM system of size 20×20×30.

The CSV must follow the schema given in Step 2, with one row per unique parameter combination.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Monte Carlo Hysteresis Simulation
- Role: process
- Action: Implement and run Monte Carlo simulations for all parameter sets listed in the reproduction scope (varying K_AF, J_INT, J_AF, AFM layers, temperature) with 20 random-seed field scans per condition, using single-spin-flip cone trial moves and Metropolis acceptance on a 20x20x(10+20) bcc lattice. Save raw magnetization vs field data for every scan.
- Evidence: `/app/outputs/raw_magnetization_data.npz`

### Step 2: Coercivity Extraction and Reporting
- Role: scored (load-bearing)
- Action: For each simulated condition, compute coercivity Hc as the field where the magnetization crosses zero on the demagnetizing branch, averaging over 20 random-seed scans and estimating uncertainty as the standard deviation. Also compute reference Hc for the corresponding homogeneous FM system of equal size for conditions requiring it. Output all results in a single CSV.
- Output file: `/app/outputs/coercivity_results.csv`
- Format: csv
- Contract: CSV with columns: condition_id (integer), K_AF (meV), J_INT (meV), J_AF (meV), AFM_layers (integer), T (K), H_c (kOe), H_c_err (kOe), reference_H_c (kOe), reference_H_c_err (kOe).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/coercivity_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### coercivity_results.csv
- path: `/app/outputs/coercivity_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Coercivity and its uncertainty for AFM-FM bilayer systems and reference homogeneous FM systems, covering multiple parameter sweeps.
- schema:
  - `type`: table
  - `required_columns`: `condition_id`, `K_AF`, `J_INT`, `J_AF`, `AFM_layers`, `T`, `H_c`, `H_c_err`, `reference_H_c`, `reference_H_c_err`
  - `units`:
    - `K_AF`: meV
    - `J_INT`: meV
    - `J_AF`: meV
    - `T`: K
    - `H_c`: kOe
    - `H_c_err`: kOe
    - `reference_H_c`: kOe
    - `reference_H_c_err`: kOe

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "coercivity_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_id",
          "K_AF",
          "J_INT",
          "J_AF",
          "AFM_layers",
          "T",
          "H_c",
          "H_c_err",
          "reference_H_c",
          "reference_H_c_err"
        ],
        "units": {
          "K_AF": "meV",
          "J_INT": "meV",
          "J_AF": "meV",
          "T": "K",
          "H_c": "kOe",
          "H_c_err": "kOe",
          "reference_H_c": "kOe",
          "reference_H_c_err": "kOe"
        }
      },
      "description": "Coercivity and its uncertainty for AFM-FM bilayer systems and reference homogeneous FM systems, covering multiple parameter sweeps."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden checker reads your `/app/outputs/coercivity_results.csv` and compares each reported Hc (and its uncertainty) against hidden reference values derived from the original study. The checker also verifies that the data obey expected physical trends (e.g., monotonic dependencies on the varied parameters). The final score is the fraction of conditions that satisfy both the value tolerance and the trend constraints, each condition weighted equally. Simply reporting the numbers from the paper is not sufficient; the checker rewards results that are physically consistent with the simulation protocol you run.
