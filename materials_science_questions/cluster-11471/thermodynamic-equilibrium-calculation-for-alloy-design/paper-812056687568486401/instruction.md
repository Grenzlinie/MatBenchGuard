# Curvature-dependent equilibrium composition in Pb-Sn alloy using CALPHAD

## Problem background
In two‑phase alloys, the curvature of the precipitate‑matrix interface induces an excess Gibbs energy that shifts phase equilibria — the Gibbs‑Thomson effect. Accurate prediction of this shift is crucial for solidification, precipitation, and coarsening models. Traditional analytical formulas often rely on simplifying assumptions (dilute solution, constant precipitate composition) that fail for concentrated alloys. A computational thermodynamics (CALPHAD) approach can directly compute curvature‑dependent equilibrium from the full Gibbs free energy surfaces without such assumptions. This task reproduces the core binary demonstration for the Pb–Sn system.

## Approach
Use the CALPHAD method: obtain the Gibbs free energy of mixing for the FCC (Pb‑rich matrix) and BCT (Sn‑rich precipitate) phases from a Pb–Sn thermodynamic database. For a range of precipitate radii *r* (nm), compute the curvature‑induced excess free energy ΔG<sub>excess</sub> = 2σ V<sub>m</sub> / r, using interfacial energy σ = 235 mJ/m² and precipitate molar volume V<sub>m</sub> = 16.26 × 10⁻⁶ m³/mol. Add this excess to the BCT mixing energy. For each radius, solve the binary chemical‑potential equalities (μ<sub>Sn</sub><sup>fcc</sup> = μ<sub>Sn</sub><sup>bct</sup>, μ<sub>Pb</sub><sup>fcc</sup> = μ<sub>Pb</sub><sup>bct</sup>) using the modified BCT energy to find the equilibrium mole fraction of Sn in the FCC matrix (X<sub>Sn</sub><sup>fcc</sup>). The required thermodynamic data are available in the open‑source pycalphad package's built‑in 'PB‑SN' database.

## Reproduction target
For the Pb–Sn binary alloy at 150 °C, compute the equilibrium Sn mole fraction in the FCC matrix (X<sub>Sn</sub><sup>fcc</sup>) at a series of precipitate radii. Create a CSV file `/app/outputs/pb_sn_gibbs_thomson.csv` with columns: `radius_nm` (float, nm) and `X_Sn_fcc` (float, dimensionless mole fraction). The CSV should cover a range of radii representative of curved particles (e.g., from 1 nm to 100 nm).

## Assets

- pycalphad (Python CALPHAD package): https://pypi.org/project/pycalphad/
- SGTE Pb–Sn thermodynamic database: pycalphad

## Workflow steps

### Step 1: Compute curvature‑dependent equilibrium for Pb–Sn binary alloy
- Role: scored (load-bearing)
- Action: For the Pb–Sn binary system at 150 °C, compute the equilibrium mole fraction of Sn in the FCC matrix (X_Sn^fcc) as a function of precipitate radius (nm). Use the CALPHAD method: obtain Gibbs free energy of mixing for FCC and BCT phases from a Pb–Sn CALPHAD database; for a range of radii (e.g., 1–100 nm), compute the curvature-induced excess Gibbs energy ΔG_excess = 2σ V_m / r (σ = 235 mJ/m² = 0.235 J/m², V_m = 16.26 × 10⁻⁶ m³/mol); add this excess to the BCT phase’s mixing Gibbs energy; solve the binary chemical‑potential equalities (μ_Sn^fcc = μ_Sn^bct, μ_Pb^fcc = μ_Pb^bct) using the modified BCT energy to obtain X_Sn^fcc. Output a CSV file with radius_nm and X_Sn_fcc.
- Output file: `/app/outputs/pb_sn_gibbs_thomson.csv`
- Format: csv
- Contract: CSV with columns: radius_nm (float, nm), X_Sn_fcc (float, mole fraction dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pb_sn_gibbs_thomson.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pb_sn_gibbs_thomson.csv
- path: `/app/outputs/pb_sn_gibbs_thomson.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Curvature-dependent equilibrium composition of Sn in the Pb-rich FCC matrix for the Pb-Sn binary alloy at 150 °C. The checker recomputes mean absolute relative error (MARE) of X_Sn_fcc against reference data, using hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `radius_nm`, `X_Sn_fcc`
  - `units`:
    - `radius_nm`: nm
    - `X_Sn_fcc`: mole fraction (dimensionless)

Notes: Scoring is based on recomputed MARE against reference data; tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pb_sn_gibbs_thomson.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius_nm",
          "X_Sn_fcc"
        ],
        "units": {
          "radius_nm": "nm",
          "X_Sn_fcc": "mole fraction (dimensionless)"
        }
      },
      "description": "Curvature-dependent equilibrium composition of Sn in the Pb-rich FCC matrix for the Pb-Sn binary alloy at 150 °C. The checker recomputes mean absolute relative error (MARE) of X_Sn_fcc against reference data, using hidden gold values."
    }
  ],
  "notes": "Scoring is based on recomputed MARE against reference data; tolerances are hidden."
}
```

## How you are scored
A hidden verifier reads your CSV and compares the computed X<sub>Sn</sub><sup>fcc</sup> values to reference data for the same radii. The score is based on the agreement between your curve and the reference (e.g., using mean absolute relative error or a similar measure). Better agreement yields a higher score. The verifier does NOT check self‑reported scalar metrics; it evaluates the raw data you submitted.
