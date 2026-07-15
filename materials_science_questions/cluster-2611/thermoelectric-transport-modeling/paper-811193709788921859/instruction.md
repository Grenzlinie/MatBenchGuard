# DFT Transport Calculation of Half-Heusler Seebeck Coefficients

## Problem background
Half-Heusler compounds are promising thermoelectric materials. The Gd–Ni–Sb and Lu–Ni–Sb ternary systems contain half-Heusler phases, GdNiSb and LuNiSb. Understanding their electronic transport properties, specifically the Seebeck coefficient, helps evaluate their thermoelectric potential.

## Approach
Use density-functional theory (DFT) with a plane-wave pseudopotential method to compute the electronic band structure of GdNiSb and LuNiSb in the half-Heusler structure (MgAgAs prototype, space group F‑43m). For GdNiSb, include spin polarization to account for Gd 4f electrons; for LuNiSb a non-spin‑polarized calculation is sufficient. Then apply the Boltzmann transport equation within the constant relaxation time approximation (using an open‑source code such as BoltzTraP2) to obtain the Seebeck coefficient as a function of temperature from the band energies. The final step is to extract the value at 380 K for each compound.

## Reproduction target
Produce the Seebeck coefficient at 380 K for the half‑Heusler phases GdNiSb and LuNiSb by performing DFT‑based transport calculations within the constant relaxation time approximation. Write the results to a CSV file at `/app/outputs/seebeck_coefficients.csv` with columns `compound` and `Seebeck_380K_uV_K`.

## Assets

- Half-Heusler crystal structures (GdNiSb, LuNiSb): https://materialsproject.org/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTraP2: https://github.com/sponce24/BoltzTraP2
- PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT electronic structure calculation
- Role: process
- Action: Perform spin-polarized DFT calculation for GdNiSb and non-spin-polarized DFT for LuNiSb in the half-Heusler structure (MgAgAs prototype, space group F-43m) using a plane-wave pseudopotential method. Obtain well-converged band energies (e.g., via a non-self-consistent calculation on a dense k-point mesh).
- Evidence: `/app/outputs/dft_convergence.log`

### Step 2: Compute Seebeck coefficients
- Role: scored (load-bearing)
- Action: Using the band energies from the DFT step, run Boltzmann transport calculations within the constant relaxation time approximation (BoltzTraP2) to obtain the Seebeck coefficient as a function of temperature. Extract the value at 380 K for each compound and write a CSV file.
- Output file: `/app/outputs/seebeck_coefficients.csv`
- Format: csv
- Contract: Two columns: 'compound' (string, one of 'GdNiSb', 'LuNiSb') and 'Seebeck_380K_uV_K' (float). One row per compound.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/seebeck_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### seebeck_coefficients.csv
- path: `/app/outputs/seebeck_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed Seebeck coefficient at 380 K for the half-Heusler phases GdNiSb and LuNiSb.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `Seebeck_380K_uV_K`
  - `units`:
    - `Seebeck_380K_uV_K`: µV/K

Notes: The checker compares the agent's computed values to the hidden reference gold (paper-reported values) using a tolerance that allows for method-dependent spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "seebeck_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "Seebeck_380K_uV_K"
        ],
        "units": {
          "Seebeck_380K_uV_K": "µV/K"
        }
      },
      "description": "Computed Seebeck coefficient at 380 K for the half-Heusler phases GdNiSb and LuNiSb."
    }
  ],
  "notes": "The checker compares the agent's computed values to the hidden reference gold (paper-reported values) using a tolerance that allows for method-dependent spread."
}
```

## How you are scored
A hidden verifier will independently check each scored workflow stage's output against a predetermined reference. The final reward is a weighted combination of per-stage scores. Reporting a number is not enough; your workflow must produce the required intermediate evidence (dft_convergence.log) and the final CSV following the output contract. The verifier reads your submitted artifacts from `/app/outputs`, recomputes metrics where applicable, and compares against hidden reference values with appropriate tolerances.
