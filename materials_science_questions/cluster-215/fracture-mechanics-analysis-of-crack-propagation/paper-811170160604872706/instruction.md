# Theoretical Crack Closure Predictions for Martensite Volume Fractions in Dual-Phase Steels

## Problem background
Dual-phase steels consist of a ferrite matrix with islands of martensite. Under cyclic loading, the mismatch in deformation between the soft ferrite and the hard martensite creates local plastic zones ahead of a propagating fatigue crack. These plastic zones, together with the martensite particles, deflect the crack path, leading to roughness-induced crack closure that strongly influences near-threshold fatigue behaviour. This task computes the theoretical dependence of the roughness-induced crack closure ratio on the volume fraction of martensite, using material parameters and a micromechanical model derived from Eshelby inclusion theory.

## Approach
The model treats martensite islands as spherical particles of a fixed diameter distributed in an elastic-plastic ferrite matrix. From the volume fraction of martensite the average particle spacing is determined. By applying Eshelby's equivalent inclusion method to the mismatch strain between ferrite and martensite, and using the von Mises yield criterion with the cyclic yield stress, one obtains a nonlinear equation that governs the size h of the plastic damage zone caused by two neighbouring martensite particles. Solving this equation gives h, which is taken as the roughness height. The crack deflection angle θ is then computed from the pitch of the zig‑zag crack path (θ = arctan(2h/Δ)), and finally the closure stress intensity ratio Kcl/Kmax is obtained from the Suresh–Ritchie roughness‑induced closure model: Kcl/Kmax = sqrt( tan(θ/2) tan(θ) / (1 + tan(θ/2) tan(θ)) ). The entire calculation is performed for four specified volume fractions of martensite, and the results are written to a single CSV file. The numerical implementation uses standard Python scientific libraries for root‑finding and angle arithmetic.

## Reproduction target
Given the fixed material parameters (martensite particle diameter d_m = 50 µm, Young's modulus E = 200 GPa, Poisson's ratio ν = 0.3, ferrite yield stress σ_y = 350 MPa, cyclic yield stress 2σ_y = 700 MPa, misfit strain ε̄ = 0.002), compute, for each of the four martensite volume fractions V_m = 0.051, 0.121, 0.210, 0.314: 1) the plastic damage zone size h (µm), 2) the crack deflection angle θ (degrees), and 3) the closure ratio Kcl/Kmax (dimensionless). Write a CSV file `/app/outputs/predictions.csv` with columns `Vm`, `h_um`, `theta_deg`, `Kcl_Kmax` containing the four rows in the order of the volume fractions. The physical model and the required equations are detailed in the Workflow steps; the agent must implement the root‑finding and the closure formula to produce the artifact.

## Assets

- Python numerical libraries: numpy, scipy, pandas

## Workflow steps

### Step 1: Compute theoretical crack closure predictions
- Role: scored (load-bearing)
- Action: Given material parameters (dm=50 μm, E=200 GPa, ν=0.3, σy=350 MPa, cyclic 2σy=700 MPa, misfit strain ε̄=0.002), compute the constant C = 8(1-ν)(2σy)/(E ε̄). For each volume fraction V_m in {0.051, 0.121, 0.210, 0.314}, compute particle spacing Δ = dm / ((6/π)V_m)^(1/3). Solve the equation 1/h^3 + 1/(Δ−h)^3 = C/dm^3 for h (the plastic damage zone size) in μm. Compute deflection angle θ = arctan(2h/Δ) in degrees. Compute closure ratio Kcl/Kmax using the Suresh-Ritchie roughness model: Kcl/Kmax = sqrt( tan(θ/2) tan(θ) / (1 + tan(θ/2) tan(θ)) ). Write the results to /app/outputs/predictions.csv.
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: Columns: Vm (float, fraction), h_um (float, μm), theta_deg (float, degrees), Kcl_Kmax (float, dimensionless). Four rows for V_m = 0.051, 0.121, 0.210, 0.314.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.csv
- path: `/app/outputs/predictions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The agent's computed theoretical crack closure ratio and associated roughness factors for the four volume fractions of martensite. The hidden checker compares Kcl_Kmax to the paper's experimentally derived closure ratios and verifies monotonic increasing with Vm.
- schema:
  - `type`: table
  - `required_columns`: `Vm`, `h_um`, `theta_deg`, `Kcl_Kmax`
  - `units`:
    - `Vm`: fraction
    - `h_um`: μm
    - `theta_deg`: degrees
    - `Kcl_Kmax`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Vm",
          "h_um",
          "theta_deg",
          "Kcl_Kmax"
        ],
        "units": {
          "Vm": "fraction",
          "h_um": "μm",
          "theta_deg": "degrees",
          "Kcl_Kmax": "dimensionless"
        }
      },
      "description": "The agent's computed theoretical crack closure ratio and associated roughness factors for the four volume fractions of martensite. The hidden checker compares Kcl_Kmax to the paper's experimentally derived closure ratios and verifies monotonic increasing with Vm."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks each workflow step's output. For the scored artifact `predictions.csv`, the verifier re‑computes the closure ratio from the submitted raw quantities and compares the values against a hidden reference; it also verifies that the closure ratio values follow the required structural trend (monotonic behaviour with respect to Vm). The verifier combines the assessments of all scored artifacts into a single reward score. Reporting a plausible number is not enough: the submitted intermediate quantities (h, θ) must be physically consistent with the specified model, and the final closure ratios must pass the hidden numerical and trend checks. The exact tolerances and reference values are not disclosed.
