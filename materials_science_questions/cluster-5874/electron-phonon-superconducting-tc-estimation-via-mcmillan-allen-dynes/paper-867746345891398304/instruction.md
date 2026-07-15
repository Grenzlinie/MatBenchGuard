# Electron-Phonon Superconducting Tc Estimation via McMillan-Allen-Dynes

## Problem background
Superconducting critical temperature (Tc) in transition-metal diborides is governed by the electron-phonon coupling strength. Ab initio density-functional theory can compute phonon properties and the isotropic Eliashberg function α²F(ω), from which the electron-phonon coupling constant λ, the logarithmic average frequency ω_log, and an estimate of Tc (via the linearized isotropic gap equation) can be derived. This task focuses on five transition-metal diborides: TaB₂, VB₂, NbB₂, TiB₂, and YB₂.

## Approach
Use density-functional theory (DFT) and density-functional perturbation theory (DFPT) to perform geometry optimization, phonon dispersion, and electron-phonon coupling calculations for each compound with an open-source DFT code (e.g., Quantum ESPRESSO) and public pseudopotentials. From the computed phonon linewidths, obtain the isotropic Eliashberg function α²F(ω). Extract the coupling constant λ and ω_log from α²F(ω) via the standard summations. Then solve the linearized isotropic gap equation with a Coulomb pseudopotential μ*=0.13 to estimate Tc. The results for the five compounds are to be computed and compared.

## Reproduction target
For each of the five compounds, compute the isotropic Eliashberg function α²F(ω) and output it as a JSON file. From this α²F data, calculate the electron-phonon coupling constant λ, the logarithmic average phonon frequency ω_log, and the superconducting transition temperature Tc estimated from the linearized isotropic gap equation with μ*=0.13. Write these parameters to a CSV file.

## Assets

- Lattice constants for TMB₂ compounds: The experimental lattice parameters a and c (in Å) for each compound are as follows:
  - TaB2: a = 3.08, c = 3.265
  - VB2: a = 2.998, c = 3.056
  - NbB2: a = 3.09, c = 3.3
  - TiB2: a = 3.038, c = 3.23
  - YB2: a = 3.290, c = 3.835
- Pseudopotentials (SSSP efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Quantum ESPRESSO (or alternative DFT code): https://www.quantum-espresso.org

## Workflow steps

### Step 1: Compute isotropic Eliashberg function α²F(ω)
- Role: scored
- Action: For each compound TaB2, VB2, NbB2, TiB2, and YB2, set up the crystal structure using the lattice constants provided in the task. Perform density-functional theory (DFT) geometry optimization, phonon dispersion, and electron-phonon coupling calculations using an open-source DFT code (e.g., Quantum ESPRESSO) and appropriate pseudopotentials. From the computed phonon linewidths and phonon density-of-states, obtain the isotropic Eliashberg function α²F(ω). Output the energy grid (meV) and the corresponding α²F values.
- Output file: `/app/outputs/step_01_alph2F_data.json`
- Format: json
- Contract: JSON object: { "<compound_name>": { "energy": [float array in meV], "alpha2F": [float array] } } for each compound: TaB2, VB2, NbB2, TiB2, YB2. The energy and alpha2F arrays must have equal length and cover the relevant phonon frequency range.
- Scoring: scored by hidden verifier

### Step 2: Extract coupling constant λ, ω_log, and Tc
- Role: scored
- Action: From the α²F data produced in step 1, compute for each compound the electron-phonon coupling constant λ = 2 Σ (α²F_i / ω_i * Δω), the logarithmic average phonon frequency ω_log = exp[ (2/λ) Σ (α²F_i ln(ω_i) / ω_i * Δω) ]. Solve the linearized isotropic gap equation with a Coulomb pseudopotential μ*=0.13 to estimate the superconducting transition temperature Tc. Output the results as a CSV file.
- Output file: `/app/outputs/step_02_elph_params.csv`
- Format: csv
- Contract: CSV with columns: compound, lambda, omega_log, Tc. One row per compound using the same compound names as in step 1 (TaB2, VB2, NbB2, TiB2, YB2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_alph2F_data.json`
- `/app/outputs/step_02_elph_params.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_alph2F_data.json
- path: `/app/outputs/step_01_alph2F_data.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw isotropic Eliashberg function α²F(ω) for the five diborides. The checker recomputes the coupling constant λ and logarithmic average frequency ω_log from this data and scores them against the paper's reported values with appropriate tolerances.
- schema:
  - `type`: object
  - `required_keys`: `TaB2`, `VB2`, `NbB2`, `TiB2`, `YB2`
  - `per_key`:
    - `energy`: 1D float array (meV)
    - `alpha2F`: 1D float array (dimensionless)
  - `notes`: Each array pair must be of equal length. The checker will recompute λ and ω_log from these arrays and compare against hidden paper values.

### step_02_elph_params.csv
- path: `/app/outputs/step_02_elph_params.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Reported coupling parameters and Tc. The checker compares the Tc values to the paper's Table III using absolute/relative tolerances.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `lambda`, `omega_log`, `Tc`
  - `units`:
    - `lambda`: dimensionless
    - `omega_log`: meV
    - `Tc`: K

Notes: The DFT calculations are computationally heavy; the solving agent may use external high-performance compute and must bring the final artifacts to /app/outputs. No wet-lab steps are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_alph2F_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required_keys": [
          "TaB2",
          "VB2",
          "NbB2",
          "TiB2",
          "YB2"
        ],
        "per_key": {
          "energy": "1D float array (meV)",
          "alpha2F": "1D float array (dimensionless)"
        },
        "notes": "Each array pair must be of equal length. The checker will recompute λ and ω_log from these arrays and compare against hidden paper values."
      },
      "description": "Raw isotropic Eliashberg function α²F(ω) for the five diborides. The checker recomputes the coupling constant λ and logarithmic average frequency ω_log from this data and scores them against the paper's reported values with appropriate tolerances."
    },
    {
      "file": "step_02_elph_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "lambda",
          "omega_log",
          "Tc"
        ],
        "units": {
          "lambda": "dimensionless",
          "omega_log": "meV",
          "Tc": "K"
        }
      },
      "description": "Reported coupling parameters and Tc. The checker compares the Tc values to the paper's Table III using absolute/relative tolerances."
    }
  ],
  "notes": "The DFT calculations are computationally heavy; the solving agent may use external high-performance compute and must bring the final artifacts to /app/outputs. No wet-lab steps are required."
}
```

## How you are scored
A hidden verifier independently evaluates the artifacts produced by each workflow stage. For Step 1, it recomputes λ and ω_log from the submitted α²F data and compares them against reference values. For Step 2, it reads the reported Tc and compares it to a reference. The final reward is a weighted average across all compounds and stages. Simply stating expected numbers without running the full DFT pipeline will not earn credit.
