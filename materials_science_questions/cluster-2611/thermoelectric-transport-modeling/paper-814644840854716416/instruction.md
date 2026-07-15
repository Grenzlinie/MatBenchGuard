# Thermoelectric Transport in Ferroelectric BaTiO3

## Problem background
Ferroelectric perovskite BaTiO₃ exhibits a polar distortion that breaks inversion symmetry, splitting and distorting the Ti‑t₂g conduction bands. This non‑parabolic band structure could produce strongly anisotropic electronic transport properties, but the magnitude and doping dependence of the Seebeck coefficients in the ferroelectric phase remain to be computed. Understanding these effects is relevant for designing oxide thermoelectrics with improved power factor.

## Approach
First-principles density functional theory (DFT) within the GGA‑PBE approximation is used to obtain the electronic band structure of tetragonal ferroelectric BaTiO₃. From the Kohn‑Sham wavefunctions, maximally localized Wannier functions are constructed for the three Ti‑t₂g bands to enable smooth interpolation of band velocities. The Boltzmann transport equation is then solved under the constant relaxation‑time approximation to compute the Seebeck tensor components S_xx and S_zz as functions of chemical potential (electron doping) at room temperature.

## Reproduction target
Compute the diagonal Seebeck coefficient components S_xx and S_zz for electron‑doped ferroelectric BaTiO₃ at T = 300 K and a doping level of 0.03 electrons per unit cell. Additionally, compute S_xx and S_zz as a function of doping over the range x = 0.01 to 0.10 e/u.c. (in steps of 0.01) at the same temperature. Write the two values at x = 0.03 to `ferroelectric_S_03.txt` and the full doping series to `Seebeck_vs_doping.csv` as specified in the workflow steps.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code supporting GGA-PBE): https://www.quantum-espresso.org
- Wannier90: https://github.com/wannier-developers/wannier90
- BoltzWann or Boltztrap: https://github.com/giovannipizzi/BoltzWann

## Workflow steps

### Step 1: DFT structure optimization and band structure
- Role: process
- Action: Perform GGA-PBE DFT calculation for tetragonal ferroelectric BaTiO3 using experimental lattice constants a=3.991 Å, c=4.035 Å. Optimize internal atomic coordinates until forces < 1e‑3 eV/Å. Compute the ferroelectric band structure (Ti‑t2g bands) and save the Kohn‑Sham wavefunctions for Wannierization.
- Evidence: `/app/outputs/dft_output.log`

### Step 2: Wannier interpolation of t2g bands
- Role: process
- Action: Using the DFT wavefunctions from step_dft, construct maximally localized Wannier functions for the three Ti‑t2g bands with Wannier90. Obtain a smooth interpolated band structure and band velocities for transport calculations.
- Evidence: `/app/outputs/wannier_band.dat`

### Step 3: Seebeck coefficient at doping 0.03 e/u.c.
- Role: scored (load-bearing)
- Action: Run Boltzmann transport (constant‑τ) using the Wannier‑interpolated bands from step_wannier. Calculate the xx and zz diagonal components of the Seebeck tensor at T=300 K for a chemical potential corresponding to 0.03 electrons per unit cell. Write the two values to ferroelectric_S_03.txt.
- Output file: `/app/outputs/ferroelectric_S_03.txt`
- Format: txt
- Contract: Line 1: S_xx value; Line 2: S_zz value (both can be negative).
- Scoring: scored by hidden verifier

### Step 4: Seebeck coefficient as a function of doping
- Role: scored
- Action: From the same transport calculation, extract S_xx and S_zz as functions of doping x over the range 0.01 to 0.10 e/u.c. (in steps of 0.01) at T=300 K. Write a CSV file with columns: x, S_xx, S_zz.
- Output file: `/app/outputs/Seebeck_vs_doping.csv`
- Format: csv
- Contract: Columns: x (float, electrons per unit cell), S_xx (float, μV/K), S_zz (float, μV/K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ferroelectric_S_03.txt`
- `/app/outputs/Seebeck_vs_doping.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ferroelectric_S_03.txt
- path: `/app/outputs/ferroelectric_S_03.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Seebeck coefficients S_xx and S_zz at T=300 K, doping x=0.03 e/u.c.
- schema:
  - `type`: text
  - `lines`:
    - `line`: 1
    - `value`: S_xx (μV/K)
    - `unit`: μV/K
    - `line`: 2
    - `value`: S_zz (μV/K)
    - `unit`: μV/K

### Seebeck_vs_doping.csv
- path: `/app/outputs/Seebeck_vs_doping.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Seebeck coefficients S_xx and S_zz as a function of doping x from 0.01 to 0.10 e/u.c. at T=300 K.
- schema:
  - `type`: table
  - `required_columns`: `x`, `S_xx`, `S_zz`
  - `units`:
    - `x`: e/u.c.
    - `S_xx`: μV/K
    - `S_zz`: μV/K

Notes: Scoring checks: absolute values at x=0.03 compared to hidden reference with tolerance; doping series trend verified for the characteristic bump in S_zz. Relaxation time τ cancels in Seebeck, so no ambiguous scaling.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ferroelectric_S_03.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "lines": [
          {
            "line": 1,
            "value": "S_xx (μV/K)",
            "unit": "μV/K"
          },
          {
            "line": 2,
            "value": "S_zz (μV/K)",
            "unit": "μV/K"
          }
        ]
      },
      "description": "Seebeck coefficients S_xx and S_zz at T=300 K, doping x=0.03 e/u.c."
    },
    {
      "file": "Seebeck_vs_doping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "S_xx",
          "S_zz"
        ],
        "units": {
          "x": "e/u.c.",
          "S_xx": "μV/K",
          "S_zz": "μV/K"
        }
      },
      "description": "Seebeck coefficients S_xx and S_zz as a function of doping x from 0.01 to 0.10 e/u.c. at T=300 K."
    }
  ],
  "notes": "Scoring checks: absolute values at x=0.03 compared to hidden reference with tolerance; doping series trend verified for the characteristic bump in S_zz. Relaxation time τ cancels in Seebeck, so no ambiguous scaling."
}
```

## How you are scored
A hidden verifier independently reads the output artifacts and checks them against reference criteria. For `ferroelectric_S_03.txt` it compares the two Seebeck coefficients to a hidden reference with a tolerance that accounts for legitimate computational differences. For `Seebeck_vs_doping.csv` it verifies that the doping series exhibits a characteristic trend consistent with the ferroelectric band structure. The final reward is a weighted combination of these checks (the single‑point values carry most of the weight). Simply reporting the paper’s numbers without executing the pipeline will not satisfy the scoring criteria.
