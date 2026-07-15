# Grüneisen Parameter from Harmonic Cell Model for Bead-Spring Glass

## Problem background
The Grüneisen parameter \(\gamma\) quantifies how vibrational frequencies in a material change with volume. For polymers, internal degrees of freedom that do not contribute to pressure can absorb energy, altering the parameter relative to simple atomic systems. This task focusses on a theoretical model for a bead‑spring polymer glass, where each chain has N=10 beads. In the glassy state large‑scale rearrangements are frozen, and a harmonic cell model yields an analytical prediction for \(\gamma\) as a function of the volume ratio \(V_0/V\). The goal is to compute this theoretical prediction over a range of volume ratios.

## Approach
The harmonic cell model treats each bead as harmonically bound to a cell centre. For a bead‑spring chain with N=10, the total Grüneisen parameter can be expressed as a product of a chain‑length factor and a component \(\gamma_1\) that depends only on the volume ratio \(V_0/V\). The functional form of \(\gamma_1\) involves rational functions of that ratio. The task is to implement this closed‑form relationship, evaluate \(\gamma_1\) and \(\gamma\) at volume ratios from 1.0 down to 0.95 in steps of 0.01, and write the results. No external data or simulation is required; the formulas are evaluated directly.

## Scope
This task covers only the glassy-regime harmonic cell model (Eqs. 16–17 of the source). The co-equal liquid-state theory (above \(T_g\)) is omitted because it requires an iterative PRISM solver (e.g., pyPRISM) as part of a multi-step thermodynamic perturbation pipeline. A self-contained checker that recomputes the full liquid-theory result would itself need to solve the PRISM equations, which is a heavy computational dependency that cannot be reliably fulfilled within the verifier sandbox without external network access. Hence, only the glassy model, which is fully checkable by recomputing closed‑form expressions, is included.

## Reproduction target
Produce a CSV file at `/app/outputs/gamma_vs_volume.csv` with columns `volume_ratio` (descending from 1.0 to 0.95 in steps of 0.01), `gamma1`, and `gamma`. At least six rows must be present. The values must be computed using the harmonic cell‑model formulas for a bead‑spring chain with N=10.

## Assets
No external datasets, models, or tools are required. The calculation can be implemented in Python using only the standard `math` library.

## Workflow steps

### Step 1: Compute Grüneisen parameter from harmonic cell model
- Role: scored (load-bearing)
- Action: Implement the harmonic cell-model formulas for bead-spring chains with N=10: gamma1 = (22*(V0/V)^2 - 5) / (11*(V0/V)^2 - 5) + 1/3, gamma = (2*N+1)/(3*N) * gamma1. Compute gamma1 and gamma for volume ratio V0/V from 1.0 down to 0.95 in steps of 0.01. Save results to gamma_vs_volume.csv.
- Output file: `/app/outputs/gamma_vs_volume.csv`
- Format: csv
- Contract: columns: volume_ratio (float, descending from 1.0), gamma1 (float), gamma (float). At least 6 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gamma_vs_volume.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gamma_vs_volume.csv
- path: `/app/outputs/gamma_vs_volume.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Theoretical Grüneisen parameter for bead-spring glass (N=10) from harmonic cell model as a function of V0/V.
- schema:
  - `type`: table
  - `required_columns`: `volume_ratio`, `gamma1`, `gamma`
  - `units`:
    - `volume_ratio`: dimensionless
    - `gamma1`: dimensionless
    - `gamma`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gamma_vs_volume.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "volume_ratio",
          "gamma1",
          "gamma"
        ],
        "units": {
          "volume_ratio": "dimensionless",
          "gamma1": "dimensionless",
          "gamma": "dimensionless"
        }
      },
      "description": "Theoretical Grüneisen parameter for bead-spring glass (N=10) from harmonic cell model as a function of V0/V."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently inspects your output file. It checks the file structure (correct columns, descending `volume_ratio`, sufficient rows) and recomputes `gamma1` and `gamma` from the reported `volume_ratio` using the exact theoretical formulas. It also verifies internal consistency relationships expected from the physics of the cell model. Your final reward is a single number between 0 and 1 that combines the results of these checks; fabricating plausible‑looking numbers without following the correct derivation will score poorly.
