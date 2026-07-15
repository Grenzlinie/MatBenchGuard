# Grüneisen Parameter and Melting Curve for Copper

## Problem background
The Grüneisen parameter γ describes the volume dependence of phonon frequencies in solids and controls melting through the Lindemann criterion. Accurate modeling of γ over a wide density range is essential for calculating melting curves. This work introduces a three-parameter analytic form γ(ρ)=1/2+γ₁/ρ^{1/3}+γ₂/ρ^q, where the constants are determined from zero-pressure data and a high-pressure one-component plasma (OCP) melting relation. The model is designed to match low-compression experimental values and to approach the theoretical limit γ→1/2 at extreme compression. This task reproduces the model for copper (Cu), deriving the parameters and computing the resulting melting curve.

## Approach
The density-dependent Grüneisen parameter γ(ρ)=1/2+γ₁/ρ^{1/3}+γ₂/ρ^q contains three unknown constants (γ₁, γ₂, q). They are found by solving a nonlinear system of three equations:
- The model evaluated at the ambient density ρ₃₀₀ matches a given experimental γ(ρ₃₀₀).
- The model evaluated at the zero-pressure melting density ρm matches a given γ(ρm).
- The OCP melting relation, combined with the Lindemann melting equation integrated with this γ, provides a third condition that ties the parameters to the melting temperature at ρm, the ion charge Z, and the OCP coupling parameter Γm.

Solving this system numerically yields γ₁, γ₂, q. Once the parameters are known, the melting temperature Tm(ρ) at any density follows from the integrated Lindemann expression: Tm(ρ) = Tm(ρm)·(ρ/ρm)^{1/3}·exp{6γ₁(1/ρm^{1/3} - 1/ρ^{1/3}) + 2γ₂/q (1/ρm^{q} - 1/ρ^{q})}. The derived melting curve can then be evaluated for a prescribed set of densities.

## Reproduction target
Solve the nonlinear three-equation system for copper using the supplied input values (ρ₃₀₀=8.93 g/cc, ρm=8.37 g/cc, Tm(ρm)=1357.7 K, γ(ρ₃₀₀)=2.19, γ(ρm)=2.48, Γm=180, Z=29, atomic mass M=63.546 g/mol). From the solution obtain the parameters γ₁, γ₂, q and write them to `gruneisen_parameters.json`. Then use these parameters to compute Tm(ρ) at the following densities (g/cc): 8.37, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 20.0, 30.0, 40.0, 50.0. Write the density and corresponding Tm values to `melting_curve.csv` with columns `density_g_per_cc` and `Tm_K`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Determine Grüneisen parameters for Cu
- Role: scored
- Action: Using the provided Cu input data (ρ300=8.93 g/cc, ρm=8.37 g/cc, Tm(ρm)=1357.7 K, γ(ρ300)=2.19, γ(ρm)=2.48, Γm=180, Z=29, atomic mass M=63.546 g/mol), set up the model γ(ρ)=1/2+γ1/ρ^{1/3}+γ2/ρ^q and the three conditions: (i) the model evaluated at ρ300 equals γ(ρ300), (ii) at ρm equals γ(ρm), (iii) the OCP melting relation Tm(ρm)·v_m^{1/3}·exp(6γ1/ρm^{1/3}+2γ2/(q ρm^q)) = (4π/3)^{1/3}·(e²/k_B)·Z²/Γm, where v_m = M/(ρm·N_A). Solve the nonlinear system numerically for γ1, γ2, q. Write the fitted parameters to gruneisen_parameters.json.
- Output file: `/app/outputs/gruneisen_parameters.json`
- Format: json
- Contract: {"gamma1": <float>, "gamma2": <float>, "q": <float>}
- Scoring: scored by hidden verifier

### Step 2: Calculate melting curve for Cu
- Role: scored (load-bearing)
- Action: Using the fitted parameters γ1, γ2, q from step1 and the reference values ρm and Tm(ρm)=1357.7 K, compute the melting temperature via Tm(ρ) = Tm(ρm)·(ρ/ρm)^{1/3}·exp{6γ1(1/ρm^{1/3} - 1/ρ^{1/3}) + 2γ2/q (1/ρm^q - 1/ρ^q)} for the densities (g/cc): 8.37, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 20.0, 30.0, 40.0, 50.0. Write the densities and corresponding Tm to melting_curve.csv.
- Output file: `/app/outputs/melting_curve.csv`
- Format: csv
- Contract: CSV with columns: density_g_per_cc, Tm_K
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gruneisen_parameters.json`
- `/app/outputs/melting_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gruneisen_parameters.json
- path: `/app/outputs/gruneisen_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted parameters γ1, γ2, q for copper.
- schema:
  - `type`: object
  - `required`:
    - `gamma1`: number
    - `gamma2`: number
    - `q`: number

### melting_curve.csv
- path: `/app/outputs/melting_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Melting curve Tm(ρ) at specified densities.
- schema:
  - `type`: table
  - `required_columns`: `density_g_per_cc`, `Tm_K`
  - `units`:
    - `density_g_per_cc`: g/cc
    - `Tm_K`: K

Notes: Parameters are scored by comparison to the paper's reported values with tolerances (γ1: 5%, γ2: order-of-magnitude, q: ±1); the melting curve is scored by pointwise comparison to a hidden gold curve derived from the paper's parameters, each Tm within 10%.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gruneisen_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gamma1": "number",
          "gamma2": "number",
          "q": "number"
        }
      },
      "description": "Fitted parameters γ1, γ2, q for copper."
    },
    {
      "file": "melting_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "density_g_per_cc",
          "Tm_K"
        ],
        "units": {
          "density_g_per_cc": "g/cc",
          "Tm_K": "K"
        }
      },
      "description": "Melting curve Tm(ρ) at specified densities."
    }
  ],
  "notes": "Parameters are scored by comparison to the paper's reported values with tolerances (γ1: 5%, γ2: order-of-magnitude, q: ±1); the melting curve is scored by pointwise comparison to a hidden gold curve derived from the paper's parameters, each Tm within 10%."
}
```

## How you are scored
Your outputs are checked by an automated verifier. The verifier independently compares your submitted parameters and melting curve against hidden reference values derived from the paper's established results, using tolerances appropriate for the sensitivity of the nonlinear fit and the melting curve calculation. Both output files are scored, and the scores are combined into a final reward between 0 and 1. The verification does not simply accept reported numbers from the literature; it expects results that genuinely follow from solving the system you implemented.
